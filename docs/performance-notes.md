# Front-end performance notes

How the site's Core Web Vitals are read, how to reproduce a measurement without
a local Jekyll, and what has been changed as a result. Written 2026-09-10 after
an INP report on the home page.

## Where the field numbers come from

Cloudflare Web Analytics, injected in `_layouts/default.html` for production
builds only. It reports real sessions, not a lab run, and it names a CSS
selector alongside each metric. **Read the selector against the metric before
acting on it** - they mean different things:

| Metric | What the selector is |
| --- | --- |
| LCP | the element whose paint was the slowest-largest |
| CLS | the element that moved |
| INP | the element the visitor **clicked** - not necessarily a slow one |

The traffic here is small. A metric's p75 can be one visitor on an old phone, so
treat a single "needs improvement" as a lead to investigate, not as a defect.

## Reproducing a measurement

Preview here is a Docker container rather than a host Jekyll (see the README),
which makes it awkward to measure a working-copy change directly. Measure
against the deployed site instead, or against a saved copy of a live page with
`<base href="https://ms3l.org/">` injected and the working copy of
`assets/css/style.css` inlined in place of the `<link>`.

`chrome --headless --dump-dom` is enough for layout assertions - write the
result into an element and read it out of the dumped DOM, since console output
is not captured. Core Web Vitals need real input events, though, which means
driving Chrome over CDP. `pip install websocket-client`; a socket to the URL
listed at `http://127.0.0.1:<port>/json` is all that is required.

```
chrome --headless=new --disable-gpu --no-sandbox
       --remote-debugging-port=9333 --remote-allow-origins=*
       --user-data-dir=<temp> --window-size=1366,900 about:blank
```

`--remote-allow-origins=*` is not optional: without it the WebSocket handshake
is rejected with 403.

Then, over CDP:

- `Runtime.evaluate` to install a `PerformanceObserver`. INP needs
  `{ type: 'event', durationThreshold: 0, buffered: true }` and entries with an
  `interactionId`; LCP needs `{ type: 'largest-contentful-paint' }`.
- `Input.dispatchMouseEvent` for `mouseMoved`, then `mousePressed` and
  `mouseReleased`. Events dispatched this way are trusted, so Chrome assigns
  them an `interactionId`. `element.click()` does **not** work - synthetic
  events are not interactions.
- `Emulation.setCPUThrottlingRate` and `Network.emulateNetworkConditions` for a
  mobile profile. A real low-end phone is slower than 4x.
- To emulate touch, `Emulation.setDeviceMetricsOverride` with `mobile: true`
  plus `Emulation.setTouchEmulationEnabled`. **`Emulation.setEmulatedMedia` does
  not change `hover` or `pointer`** - a test written with it silently measures
  the desktop path twice.
- Clicking a link ends the document. Write the observer's results into
  `sessionStorage` on `pagehide` and read them back after the navigation, which
  is what the `web-vitals` library does in the field.

## What was measured

Click on a home overview card (`index.md`, the four-card grid), including the
navigation to `/join-us`:

| Condition | INP | input delay / processing / presentation |
| --- | --- | --- |
| Desktop, unthrottled | 32ms | 0 / 2 / 30 |
| 4x CPU, 4G | 32ms | 2 / 24 / 6 |

The budget is 200ms. Nothing reproducible was wrong. LCP on the same page is
`p.hero-mission` at 0.4-0.6s, and the overview grid sits below the fold at every
viewport tested, so it is not an LCP candidate on load.

## What changed anyway

Two pieces of work were genuinely happening at the moment of a tap.

**`.card-link:hover` is now behind `@media (hover: hover) and (pointer: fine)`.**
It is the one expensive hover on the site - a 46px blurred shadow and a lift,
eased over 150ms. A touch device applies `:hover` on tap, so that repaint began
exactly as the navigation did, which is the frame INP measures. A finger gets
nothing, which is correct twice over: the card is about to leave the screen, and
touch users no longer get a hover state stuck on after they come back.

The other hover rules are deliberately left unguarded. They change colour,
background or underline only - `.btn-primary`, `.btn-secondary`, `.inline-link`,
`.research-details-button`, the nav - which is cheap, and on touch they double
as tap feedback.

**The nav's document-level click handler no longer clears `open` from every nav
group on every click.** It runs for every click anywhere on the page; it now
only touches groups that actually carry the attribute.

## The reveal now cleans up after itself

Found while verifying the above, and the more consequential fix. See
[the cascade section of the content guide](content-guide.md) for the general
rule.

The scroll reveal in `_layouts/default.html` added `.reveal` and `.is-visible`
and left them on forever. Both of these outrank `.card-link`'s own rules - same
specificity, later in the stylesheet - so on every revealed card:

- `.reveal.is-visible { transform: none }` beat
  `.card-link:hover { transform: translateY(-2px) }`, and the hover lift had
  **never once fired**;
- `.reveal`'s `transition: opacity, transform` beat `.card-link`'s
  `transition: transform, box-shadow`, so the hover shadow snapped instead of
  easing.

A reveal is a one-shot. It now drops both classes on `transitionend` and the
element goes back to being an ordinary card. Guard the listener on
`event.target === el` and `event.propertyName === 'opacity'`, because children
and pseudo-elements bubble their own transitions, and keep the `setTimeout`
fallback for a tab that is never painted and so never fires `transitionend`.

Verified on the deployed site:

```
[desktop] classes=card card-link  hover-lift=matrix(1,0,0,1,0,-2)  shadow=46px
[touch]   classes=card card-link  hover-lift=none                  shadow=40px
```

A side effect worth knowing: cards no longer carry `.reveal.is-visible`, so
selectors in future Cloudflare reports will be shorter than the ones in the
report that started this.

## Still open

- The hero particles animate `left` rather than `transform`. `contain: layout
  paint` hides the symptom; the keyframes are still the real fix. Carried over
  from [the redesign notes](redesign-notes.md).
- Whether any of this moves the Cloudflare INP figure is unknown. It was not
  reproducible in the lab, so the honest expectation is a small change or none.
  If it stays flagged, get the per-page and per-device breakdown first rather
  than guessing again.

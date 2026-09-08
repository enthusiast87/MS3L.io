# MS3L logo and CI

The website itself still uses the SVG wordmarks (`ms3l-logo.svg` in the header,
`ms3l-logo-frame.svg` as the favicon). The PNG set below is the CI set for
everything off the website - chat avatars, slides, documents, posters - and is
built to sit alongside the group's PowerPoint template.

## Palette

Taken from KRICT's own stylesheets rather than picked by eye, so the lab's
identity reads as part of KRICT:

| Role | Hex | Note |
| --- | --- | --- |
| Lab navy | `#0B2F5B` | the site's existing brand navy |
| KRICT blue | `#005CA5` | KRICT secondary, primary ring colour here |
| KRICT teal | `#089892` | KRICT primary |
| KRICT teal, bright | `#12D0BE` | for use on navy, where `#089892` goes too dark to read |

The gradient used across the set is `135deg, #005CA5 → #0A7FA8 → #089892`,
matching the gradient treatment in the group's slide template.

## The set

All squares are 1024x1024 with the ring inset 26/512, sized so a circular crop
cannot clip the M or the L.

| File | Use |
| --- | --- |
| `ms3l-avatar.png` | **Primary.** White ground, navy wordmark, solid `#005CA5` ring. Chat avatars, profile photos |
| `ms3l-avatar-gradient.png` | Same, ring in the blue-to-teal gradient. Use where the slide deck's gradient is present |
| `ms3l-avatar-dark.png` | Navy ground, white wordmark, gradient ring. For dark placements |
| `ms3l-avatar-fill.png` | Full-bleed gradient, white wordmark. Bold placements, slide corners |
| `ms3l-lockup-horizontal.png` | Wordmark plus full lab name, gradient divider. Slides, letterhead, posters |
| `ms3l-lockup-horizontal-dark.png` | The same on navy |
| `ms3l-ci-sheet.png` | Overview of the whole set, including how each reads at 26px |

## Why a ring, and why this thick

The wide SVG wordmarks do not work in a square profile slot - they either float
in empty margin or get cropped. The ring is circular rather than a box so it
lines up with circular cropping instead of losing its corners to it.

Ring thickness was chosen at 26px display size, not at full size. A thin ring
disappears there: 5/512 is invisible, 9/512 is faint. The white-ground tiles
need 20/512 because they have nothing else defining their edge against a light
chat background; the navy tile only needs 14/512.

Inter 700 throughout. 600 thins out at small sizes and 800 is indistinguishable
from 700 once scaled down.

## Older wordmarks

`ms3l-logo.svg`, `ms3l-logo-blue-accent.svg`, `ms3l-logo-frame.svg` and
`ms3l-logo-horizontal.svg` predate this set and are what the site renders. They
are text-based SVGs and depend on Inter being available to the renderer.

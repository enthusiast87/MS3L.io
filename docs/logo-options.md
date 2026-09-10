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
| `ms3l-avatar.png` | **Primary.** White ground, navy wordmark, blue-to-teal gradient ring. Chat avatars, profile photos |
| `ms3l-avatar-circle.png` | The primary with a **transparent** background, so it sits on a coloured slide without a square patch. Use this one in decks |
| `ms3l-avatar-fill.png` | **Co-primary.** Full-bleed gradient, white wordmark. Bold placements, slide corners, social |
| `ms3l-avatar-solid.png` | Solid `#005CA5` ring instead of the gradient. Quieter alternate |
| `ms3l-avatar-dark.png` | Navy ground, white wordmark, gradient ring. For dark placements |
| `ms3l-lockup-horizontal.png` | **Primary lockup.** Wordmark plus full lab name, gradient divider. Slides, letterhead, posters |
| `ms3l-lockup-horizontal-white.png` | White, transparent background, for gradient and dark grounds |
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

## Presentation template

The deck is a 16:9 file built on the
same palette and gradient: title, section divider, content, two-column, figure
and closing. 

Use the transparent assets inside it - `ms3l-avatar-circle.png` and
`ms3l-lockup-horizontal-white.png`. The opaque avatars carry a white or navy
square that shows as a patch once placed on a gradient slide.

The deck sets Inter by name. Where Inter is not installed PowerPoint falls back,
so either install Inter or switch the template's font once to whatever the
group's machines have.

## Poster template

The poster is 36 x 48 in portrait -
the common conference size, and what AIChE boards take. Three columns: text on
the left, figures in the middle, results and conclusions on the right, with a
gradient header band carrying the lockup, title, authors and affiliations, and
a footer bar with contact and the site address.

Body copy is set at 26 pt, which stays readable from about 1.5 m. If you rescale
the board, scale the type with it rather than leaving it at 26 pt.

### Where the template files live

`assets/templates/`, versioned like everything else so they are kept, have a
history, and arrive on every machine with a pull. They are excluded from the
site build, so they never appear on ms3l.org - but this repository is public,
so treat them as internal-by-convention rather than private.

They are also reproducible: `scripts/make_deck_template.py` and
`scripts/make_poster_template.py`. Run either to regenerate into `assets/templates/`:

```
pip install python-pptx
python scripts/make_deck_template.py
python scripts/make_deck_template_gradient.py
python scripts/make_poster_template.py
python scripts/make_poster_template_gradient.py
```

There are two decks on purpose. `MS3L_presentation_template.pptx` follows the
group's existing white deck and is the default for internal and institutional
use. `MS3L_presentation_template_gradient.pptx` leads with the CI ramp and
matches the website; use it for conference talks and anywhere the deck should
look like the lab rather than like a report. Both carry the same marks, palette
and slide set. The poster comes in the same two, on the same rule: the plain
file is white, `_gradient` leads with the ramp.

### Showing the institute

The gradient set carries the KRICT mark joined to the lab's own - lockup,
hairline, wordmark - rather than parking the two in opposite corners, and every
slide that carries a mark carries both. Two marks at opposite ends of a header
read as two organisations of equal standing; joined with a rule they read as a
group and the institute it sits in, which is what MS3L is. The title and closing
slides spell "Korea Research Institute of Chemical Technology" out in full, and
the poster footer names the division, so the affiliation survives a black and
white printout where the logos go flat.

Both resolve their own paths, so they work from any working directory.

To change a layout or a colour, edit the generator and re-run it rather than
editing slides by hand - that is what keeps the deck, the poster and the site on
one palette.

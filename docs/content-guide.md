# Adding content to MS3L.io

Page content lives in `_data/*.yml`. The templates only loop over that data, so
adding a person, a paper or a news item almost never means touching `.md` or
`.html`. This file records the conventions the data already follows, so a new
entry lands consistent with the ones around it.

Before publishing:

```bash
python scripts/validate_site.py     # YAML syntax and required fields
.\scripts\dev-up.ps1                # local preview at http://localhost:4000/
```

`docs/`, `scripts/`, `README.md` and `certs/` are excluded from the build in
`_config.yml`, so nothing in this folder reaches the live site.

## Order matters: file order is display order

No template sorts anything. Whatever order the entries sit in the file is the
order they render. These are all **newest first**, so new entries go at the
**top**:

- `_data/news.yml`
- `_data/publications.yml`
- `_data/patents.yml`
- `lab.recognitions.items`
- `lab.invited_talks.items`

Two things to know about `patents.yml`: a patent family registered in several
countries is one entry with a combined `country` (`Korea (KR), US, China`)
rather than one entry per country, and the oldest block — the 2015-2019
PhD-era filings — is only loosely ordered. Everything from 2023 on is strictly
newest-first; keep new entries that way.

## Members (`_data/members.yml`)

### `role_group` must match exactly

`members.md` selects each section by string:

| Section | Selector |
| --- | --- |
| Postdoctoral Researchers | `role_group == "Postdoctoral Researcher"` |
| Internship Master Researchers | `role_group == "Internship Master Researcher"` |
| Students | `role_group` **contains** `"Student"` |

A typo here does not error — the person silently renders nowhere. The principal
investigator uses `Principal Investigator` and has his own page rather than a
card on `/members`.

### Field conventions

| Field | Convention | Example |
| --- | --- | --- |
| `degree` | `<degree>, <university>` | `Ph.D., KAIST` / `M.S., Yonsei University` |
| `degree` (in progress) | degree only, no university | `Ph.D. Program` |
| `period` | month-level, `YYYY.MM - present` | `2025.03 - present` |
| `position` | role with the same period in parentheses | `Postdoctoral Researcher (2025.03 - present)` |
| `affiliation` | pipe-separated; a current program and its co-supervisor belong here | `UST \| UST-KOICA Program \| Co-supervised with Prof. Young Kyu Hwang` |
| `image_url` | optional — the photo area only renders when present | |

### Highlights (`achievements`)

Renders as the collapsed **Highlights** disclosure on the card. Every line ends
with a year, so entries are comparable within a card and against the
Publications and Patents pages.

| Kind | Format | Example |
| --- | --- | --- |
| Paper | `<Venue> (<First author\|Co-author>, <year>)` | `Chemical Engineering Journal (First author, 2025)` |
| Patent | count word + year(s), no subject matter | `One Korean registered patent (2026)` / `Two Korean registered patents (2024, 2025)` |
| Award / press | year inside the existing parenthesis | `Best oral presentation award (MSK Fall 2025)` |

Patents deliberately do not say what the patent covers: papers are listed as
venue plus author role without titles, so a topic on the patent line alone
would be the odd one out.

Take years from the repo rather than memory — `publications.yml` (`year`),
`patents.yml` (`date`), `news.yml` (`date`). Author roles should match the
`authors` string on the publication.

A venue containing a colon has to be quoted, or YAML reads it as a mapping:

```yaml
- "Applied Catalysis B: Environment and Energy (Co-author, 2026)"
```

### Gotcha: the name highlighter has its own list

`_includes/highlight-members.html` bolds lab members inside author and inventor
lists on the Publications and Patents pages. It uses a **hardcoded** alias list,
**not** the `aliases` field in `members.yml`. Adding a member means editing both,
otherwise their name renders unbolded. Include every spelling that appears in
the paper and patent data — several members are published under two
transliterations (`Kholmizaeva` / `Kholmirzaeva`).

## Alumni (`_data/alumni.yml`)

The file header states the rule: completed degrees supervised in MS3L. Someone
who stays on in the lab keeps a `members.yml` entry as well, and `now` records
where they are today.

- **Co-supervision goes on the alumni `institution` line**, as
  `Korea University | Co-supervised with Prof. Gwang Ho Song`. It is a fact about
  the degree, not about a present role, so it does not belong on a current
  member card or in a news entry.
- **When someone actually leaves**: delete the `members.yml` entry and update
  `now`. Highlights do not move across. The alumni card is deliberately lighter
  than a member card — a completed record, not a roster entry — and their papers
  and patents already live permanently on their own pages.

## News (`_data/news.yml`)

A curated milestone log, not a feed that has to stay current. The bar is a
**dated event worth announcing**: graduation, award, press coverage, a large
grant, a new member, a pilot milestone. Roughly four to eight a year keeps the
home page fresh without creating an obligation to post.

- The home page panel takes the **newest three** automatically
  (`index.md`, `limit: 3`). There is no featured flag for news — date order is
  the only control. `publications.yml` does have `featured: true`, if news ever
  needs the same treatment.
- `image` and `image_alt` are optional. Without an image the card switches to
  full width on its own, via `news-card-text-only` in `news.md`.
- `note` is the italic closing line. Keep it to what is actually news.
- HTML is allowed in `title`, `summary` and `note` — write `MS<sup>3</sup>L`.

## Publications (`_data/publications.yml`)

`featured: true` drives the Featured sections on both the home page and
`/publications`. Six entries carry it today; it is a deliberate selection, not
"most recent".

## Page lead lines (`_data/lab.yml`)

Each page's `lead` is one line about the content itself — never about the state
of the website. Lines like "migrated from the original Google homepage" or
"profiles can be added as the roster is finalized" describe the build rather
than the lab, and go stale silently.

## CSS: keep breakpoint overrides after the base rule

`assets/css/style.css` is long enough that cascade order bites. A media query
adds no specificity, so a stacking rule written in the shared 720px block above
a two-column base rule declared later **silently loses**. This shipped once:
the members roster stayed two cards wide on a phone, breaking names mid-word and
overflowing the viewport.

The `.member-grid` / `.alumni-grid` overrides therefore sit at the bottom of the
file, after both definitions. Put new responsive overrides after the rule they
are meant to beat, and check the computed `grid-template-columns` at a narrow
width rather than reading the cascade.

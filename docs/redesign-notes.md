# Site cleanup notes (2026-08-26)

Record of the review pass that followed the Google Sites migration, so the
reasoning behind the less obvious changes is not lost.

## Rendering bugs that were live in production

- `<title>` and the logo `alt` interpolated `site.title` raw, so browser tabs
  and search results showed `Contact | MS<sup>3</sup>L`. Both now use
  `strip_html`, with `title_plain` in `_config.yml` as the plain-text name.
- `contacts.md` used `redirect_to:`, which needs the `jekyll-redirect-from`
  plugin. It was never enabled, so `/contacts/` published an empty duplicate
  Contact page. It is now a real meta-refresh redirect marked `noindex`.
- Redirect targets must not carry a trailing slash: GitHub Pages resolves
  `/contact/` to `contact/index.html`, which does not exist. `/contact` works.
- `_config.yml` had no `exclude`, so `Dockerfile.dev`, `compose.dev.yaml`,
  `scripts/`, `prompts/`, `docs/` and `README.md` were all being published.
- The home page fetched research themes with four hardcoded title lookups, so
  renaming a theme in `_data/research.yml` silently dropped its card. It now
  loops over the data.

## Structure

Impact mirrors the lab's own site: **Patents / Technology Transfer / Scale-up /
Recognitions**. Industrial Collaboration folded into Technology Transfer (the
Evonik consultancy sits beside the Lotte transfer) and Process Innovation into
Recognitions. Both old URLs redirect. Patents was listed under both Achievements
and Impact; it now appears once.

`lab.experiences` mixed transfers, an award and a grant in one list. It is split
into `technology_transfer`, `scale_up` and `recognitions`, each owned by the page
that renders it.

Scale-up is new writing. The Google Sites page has a title and no body, so the
content is drawn from the lab's real plant-design projects.

## Publications

`featured: true` drives a Featured section on the home and publications pages,
replacing a "six most recent" list. The set is the lab's own selection from the
Google Sites home page, plus Science 2020 and the 2018 JMS paper.

The home theme cards used to carry a per-theme "key paper", but two of the four
were the same papers the Featured section listed further down the same page.
Theme cards now lead with the figure and the one-line research question;
`selected_papers` still render on `/research`.

## Duplication removed

PI details lived in `lab.principal_investigator`,
`lab.introduction.principal_investigator` and `_data/members.yml`.
`members.yml` is now the single source; the footer, home and PI page read from
it. `contact.email` duplicated `contact.emails[0]` and `contact.institution`
duplicated the top-level `institution`; both are gone.

Sixteen unreferenced `lab.yml` keys were removed after auditing every key path
against the templates, resolving Liquid `assign` aliases so nested keys reached
through a local variable were not counted as dead.

## Motion and accessibility

- `prefers-reduced-motion` capped `animation-duration` but not the iteration
  count, which makes an infinite animation flicker at speed rather than stop.
- The hero particles animate `left`, a layout property, so every frame
  invalidated layout document-wide and the sticky header's `backdrop-filter`
  recomposited in step - visible as a shimmer along the top of the page.
  `contain: layout paint` on the visual plus an opaque header base fixes the
  symptom; converting the keyframes to `transform` is the real fix and is still
  open.
- Added a skip link, visible focus rings, canonical/OpenGraph tags, and a
  favicon.

## Naming

The lab is **Membrane-based Sustainable Separation Solutions Laboratory**.
"System" appeared in several files and has been unified to "Solutions".
"Solutions" carries the translation-to-industry positioning that the transfer,
consultancy and plant-design record actually supports.

# MS3L Sub-Agent Playbook

Use the same simple sub-agent structure for this project across future Codex sessions.

## Core Roles

### `전체`
- Purpose: repo-wide orientation, integration review, and final consistency checks
- Use when:
  - starting a new session
  - checking whether recent changes fit together
  - preparing for commit or deployment
- Typical scope:
  - broad repo scan
  - cross-page consistency
  - final risk review

### `구조`
- Purpose: site architecture, layout shell, navigation, routes, page hierarchy
- Owns:
  - `_layouts/`
  - `_config.yml`
  - navigation structure
  - route naming
  - page relationships
- Use when:
  - changing nav
  - merging/removing pages
  - updating shared layout or footer/header

### `데이터`
- Purpose: content model, YAML data, migration from hardcoded content to `_data`
- Owns:
  - `_data/`
  - data-backed content sections
  - page rendering from YAML/Liquid
- Use when:
  - adding members, publications, news, contact data
  - migrating homepage content into `_data`
  - cleaning duplicated content sources

### `디자인`
- Purpose: visual identity, homepage composition, typography, section rhythm, CSS direction
- Owns:
  - `assets/css/style.css`
  - homepage presentation
  - shared visual language
- Use when:
  - redesigning homepage
  - improving type, spacing, and section hierarchy
  - making the site feel less generic

### `도구`
- Purpose: build workflow, preview workflow, validation, scripts, deployment support
- Owns:
  - `scripts/`
  - validation workflow
  - preview/build process
  - GitHub Pages compatibility checks
- Use when:
  - local preview is failing
  - validation scripts need updates
  - build/deployment workflow changes

## Recommended Usage

Do not spawn all roles by default. Start with only the roles needed for the current task.

Examples:

- Homepage redesign:
  - `구조`
  - `디자인`

- Content migration:
  - `데이터`
  - `구조`

- Build/preview troubleshooting:
  - `도구`

- Pre-commit review:
  - `전체`

## Phase 1 Default Setup

For the current migration stage, the default structure is:

- `전체`: overall review and synthesis
- `구조`: page hierarchy and nav cleanup
- `데이터`: content migration and `_data` structure
- `디자인`: homepage and visual refinement
- `도구`: preview/build/validation

## Working Rules

1. Keep role names the same every session.
2. Recreate agents as needed, because agent instances are temporary.
3. Keep ownership boundaries clean to avoid overlap.
4. Prefer file ownership over vague task ownership.
5. Let `전체` synthesize, not duplicate work done by the specialized roles.

## Current Direction

This website migration is not a 1:1 copy of the old Google Site.

The project goal is:
- migrate important content
- improve structure and design
- keep GitHub Pages/Jekyll maintainable
- preview locally before commit

## Current Phase 1 Priorities

1. Improve homepage identity and composition.
2. Simplify navigation to the core page set.
3. Keep `_data` as the source of truth.
4. Strengthen members and publications content.
5. Verify each major round in the local preview workflow.

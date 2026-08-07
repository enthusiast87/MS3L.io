# Image Assets

This directory holds local image assets for the MS3L website.

## Folders

- `members/`: PI, postdoc, and student profile photos
- `research/`: research-theme visuals used in `research.md` and home cards
- `news/`: news and award photos
- `logos/`: partner, institutional, and impact logos
- `imported/google-sites/`: raw imported images and importer manifests

## Suggested Filenames

- `members/jihoon_kim.jpg`
- `members/khilola_kholmizaeva.jpg`
- `members/suyeon_park.jpg`
- `members/yourim_noh.jpg`
- `members/hyeokjun_seo.jpg`
- `research/biorefinery.jpg`
- `research/plastic-recycling.jpg`
- `research/resource-recovery.jpg`
- `research/energy.jpg`
- `logos/lotte-chemical.jpg`
- `logos/evonik-industries.png`
- `logos/kistep-achievement.png`
- `logos/nrf-logo.png`

## Size Guidance

- Member photo cards: 900 x 1200 px, under 500 KB each
- PI hero/profile photo: 1200 x 1500 px, under 700 KB
- Research theme image: 1600 x 1000 px, under 800 KB each
- News images: 1600 px wide or smaller, under 900 KB each
- Logos: transparent PNG where useful, under 300 KB each

Prefer sRGB images. Photos should usually be `.jpg`; graphics or logos that need transparency should use `.png`.

## Adding a Member Photo

1. Crop or export the portrait close to a `3:4` ID-photo ratio. A `900 x 1200 px` JPG under `500 KB` is recommended.
2. Save the file in `assets/images/members/` using a lowercase English name with underscores (`_`).
3. Add `image_url` to that person's entry in `_data/members.yml`. For example:

   ```yaml
   - name: Suyeon Park
     image_url: /assets/images/members/suyeon_park.jpg
   ```

The member card only displays the photo area when `image_url` is present, so missing photos do not leave an empty placeholder.

# Image manifest

Each placeholder on the site names the file it expects. Use real project files only.

## Where originals go

Put original CAD images, plots, and photos in `source-media/`, which is never published. Only optimized copies, with metadata removed, belong in this folder.

## How to replace a placeholder

1. Export a web-sized image and remove sensitive metadata, such as photo GPS data. Check that it doesn't show confidential dimensions or anyone who hasn't given permission.
2. Save it using the exact lowercase filename below. WebP suits photos and renders. PNG or SVG can suit drawings and plots.
3. In the HTML, find the `REPLACE IMAGE` comment for that file and swap the `<div class="image-placeholder">...</div>` beneath it for an image tag.

From a page in `projects/`:

```html
<img src="../assets/images/mark-12/motion-ratio-vs-travel.webp"
     width="1600" height="900" loading="lazy"
     alt="Describe what the image shows and what it tells the reader.">
```

From `index.html`, leave out `../`. Set `width` and `height` to the file's actual pixel dimensions. Leave out `loading="lazy"` for the main image visible when the page first loads.

## Expected files

### `mark-12/`

**In place** (originals in `source-media/mark-12/`):

| File | Content | Used on |
|---|---|---|
| `rear-arb.webp` | Rear ARB assembly CAD render | Case study hero |
| `front-arb.webp` | Front ARB assembly CAD render | Homepage feature |
| `torsion-bar-sizing.webp` | Torsion bar sizing spreadsheet | Case study, Supporting analysis |
| `rear-motion-ratio.webp` | Rear ARB motion ratio from the Motion Study | Case study, Results |
| `front-arb-mounting.webp` | Front ARB on the front roll hoop | Case study, What changed |
| `rear-bearing-block-ansys.webp` | Ansys static structural run on a rear bearing block | Case study, Supporting analysis |
| `lever-arm-trade-study.webp` | Weighted trade study on lever-arm shape | Case study, What changed |
| `rear-bell-crank-pickup.webp` | Rear drop-link pickup on the bell crank, CAD | Case study, Results |
| `front-double-shear.webp` | Front drop-link pickup and double-shear mounting, CAD | Case study, Results |

**Add later, once they exist:** Manufacturing drawings, final Ansys bearing block results, manufacturing photos, and test results.

### `about/` (in place)

| File | Content |
|---|---|
| `aarav-shah.webp` | Aarav's photo, 400 × 400 (About page). Original in `source-media/about/` |
| `aarav-shah-preview.jpg` | JPG copy of the same photo, for the link-preview `og:image` tag after publishing (see `DEPLOYMENT.md`) |

### `mark-11/`

| File | Content |
|---|---|
| `arb-validation.webp` | In place: Mark 11 ARB physical test that Aarav assisted with (About page, Suspension General Member entry). Original in `source-media/mark-11/` |

### `shear-sensor/`

| File | Content |
|---|---|
| `shear-sensor.webp` | Optional, once a real image exists: parts, fixture, or CAM toolpath (needs the lab's permission). The card shows a text panel until then |

### `robotics/`

| File | Content |
|---|---|
| `frc-2023-on-field.webp` | In place: 2023 FRC robot on the field (homepage card, page hero) |
| `frc-2023-robot.webp` | In place: 2023 robot in the pits. Shows a person |
| `frc-2023-auto-balance.mp4` + `-poster.webp` | In place: 8 s silent autonomous balancing clip, metadata stripped. Cropped to 3:4 (480 × 640) on November 17, 2026 to match Fig. 2; the uncropped copies are in `docs/design-backup-2026-11-17/` |
| `fgc-2024-robot.webp` | In place: 2024 FIRST Global Challenge robot |
| `fgc-2024-elevator-extended.webp` | In place: cascading elevator extended. Shows teammates and volunteers, one with a readable name badge |
| `elevator-cad.webp` | Optional: elevator CAD |

### `tembo/` and `renaissance/`

Each needs the company's permission. Each file is used on the homepage card and the page hero.

| File | Content |
|---|---|
| `tembo/fastener-cad-library.webp` | In place: fastener CAD render (homepage card, page hero) |
| `tembo/fastener-drawing.webp` | In place: fastener drawing (page). Approved for public use, with the client company name whited out |
| `renaissance/diamond-seat.webp` | In place: redesigned diamond seat with raised support geometry (homepage card, page hero). Approved |
| `renaissance/diamond-seat-original.webp` | In place: original seat, for the before/after comparison (page). Approved |

On the homepage cards, use `alt=""`, because the card's title already names the project. On the project pages, write full alt text.

### `leadership/`

Optional. Photos need permission from anyone identifiable.

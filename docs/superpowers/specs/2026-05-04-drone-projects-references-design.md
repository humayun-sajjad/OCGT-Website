# Drone Projects — References & Highlight Design

**Date:** 2026-05-04
**Scope:** Add ~30 Reality Capture / drone projects from 2018–2022 to `/referenzen` and highlight them on the existing RC service pages.
**File touched:** `OCGT_website.html` only.

## Goal

Reality Capture is the user's main service. The current site already presents it as a co-equal discipline, but the references are thin (8 RC entries vs. 30+ Geotechnik). The user has supplied a detailed list of ~30 drone projects with clients (Auftraggeber). This spec adds them to `/referenzen` and surfaces highlights on the `b1` / `b2` / `b3` service pages — without restructuring the home page, navigation, or any other section.

## Out of scope

- Home page hero / discipline bento / sticky-scroll order
- Navigation / meta tags / SEO copy
- Geotechnik marquee section (untouched)
- FAQ / testimonials / video sections
- New components or styling systems
- Image assets — text-only entries unless an existing marketing image already fits

## Source data

The user's list, deduplicated against existing entries:

### 2018 – 2019 · Pipeline & integrated drone work
1. Pipeline-Testprojekte zum Aufbau der 3D-Photogrammetry Pipeline — BV Mühlenstraße · BV Heidestraße QH Track · BV Rosenthaler Str. · BV SCALE
2. Integrierte Drohnen-Doku im Zuge OCGT Bauüberwachungs-/Geotechnikprojekte: BV Elbtower Hamburg (Probepfähle) · BV Rosenthaler Straße · BV Tegel Nord · BV Neue Nationalgalerie · BV Bachstraße

### 2020 (4 entries)
1. **BV Eiswerk** · Berlin · 2D/3D-Baudokumentation · AG: PST Grundbau GmbH
2. **BV SCALE** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Townscape GmbH
3. **BV Werder (Havel)** · Werder · 3D-Baudokumentation · AG: BCONsult Bauüberwachung und Fachbauleitung GmbH
4. **BV Heidestraße QH Track (Berlin Europacity)** · Berlin · 3D/2D-Baudokumentation · AG: Bauer Spezialtiefbau GmbH

### 2021 (15 entries)
1. **BV BLUBB** · Berlin · 3D-Photogrammetrie, Abriss-/Aushubmassenermittlung · AG: Meyer Erdbau GmbH
2. **Deponie Golm** · Golm · Drohnenbefliegung, 3D-/Terrainmodell, Hebungs-/Setzungsanalyse · AG: Kummer Erd- und Tiefbau GmbH
3. **BV SCALE** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Townscape GmbH
4. **Liegenschaften Germendorf** · Germendorf · DTM, Geländeschnitte, Massen- und Volumenberechnung Haufwerke/Schutthalden · AG: GBG Germendorf mbH
5. **BV SQUARE** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Bauwert AG
6. **BV CROWN1** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Quartier Heidestraße GmbH
7. **BV SQUARE — Pflasterprotokoll 2.0** · Berlin · Massenberechnung Restaushub, Abgleich BE-Flächen · AG: Keller Grundbau GmbH
8. **BV Tesla Gigafactory Grünheide** · Grünheide · ~60 ha Erweiterungsflächen, 3D-Photogrammetrie + Massenermittlung · AG: Meyer Erdbau GmbH
9. **Fahrrad Fritsch** · Weiden i.d.Opf. · 3D-Laserscan Ladengeschäft, Grundrisse + Ansichten · AG: Fahrrad Fritsch
10. **Sage Restaurant & Sage Beach** · Berlin · 3D-Laserscan Veranstaltungs-/Außenbereich, Grundrisse + Ansichten, 3D-Tour mit 360°-Bildern auf Google Maps · AG: Sage Gastro und Event GmbH
11. **BV GoWest** · Berlin · 3D-Photogrammetrie Abbruch-/Bestandsgebäude, Baufortschritt + Massen · AG: RWG1 GmbH Berlin
12. **Polytapes Maschinenhalle** · Wickede a.d. Ruhr · 3D-Laserscan Halle + Werkstätten + Personalbereich, Umplanung · AG: Polytapes GmbH
13. **Tree House Berlin** · Berlin · 3D-Laserscan Veranstaltungs-/Tagungslokation, Grundrisse + 3D-Tour mit 360°-Bildern auf Google Maps · AG: Frederik & Labots WA GmbH
14. **BV SQUARE — Baufeld C** · Berlin · ~12 ha Aufmaß Urgelände, 3D-Photogrammetrie + Massenermittlung · AG: Keller Grundbau GmbH
15. **BV Heidestraße QH MI3 (Berlin Europacity)** · Berlin · 3D/2D-Baudokumentation · AG: Bauer Spezialtiefbau GmbH

### 2022 (6 entries)
1. **BV SQUARE** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Bauwert AG
2. **BV Storkower Straße 140** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Townscape GmbH
3. **BV Storkower Straße 142-146** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Townscape GmbH
4. **BV Franklinstr. 8** · Berlin · monatliche 3D/2D-Baudokumentation · AG: BCONsult Bauüberwachung und Fachbauleitung GmbH
5. **BV GoWest** · Berlin · monatliche 3D/2D-Baudokumentation · AG: BCONsult Bauüberwachung und Fachbauleitung GmbH
6. **BV Revaler Str. 32** · Berlin · monatliche 3D/2D-Baudokumentation · AG: Townscape GmbH

## Changes

### Change 1 — `/referenzen` chronological list

Replace the single year group `data-year="rc-2020-2024"` (currently 8 entries) with **four** RC year groups, in the existing `<section class="refs-yrgroup">` pattern:

- `data-year="rc-2022"` → "2022 · Reality Capture" — 6 monthly Baudokumentations
- `data-year="rc-2021"` → "2021 · Reality Capture" — 15 entries (mix of monthly + Massenermittlung + Laserscans + Tree House + Tesla); existing **Oldtimer**, **Fischerstraße**, **Doppelsporthalle Gustav Freytag**, **Gasthaus Figl** entries fold in here
- `data-year="rc-2020"` → "2020 · Reality Capture" — 4 new + existing **4D-Baudokumentation Großbaugrube Mitte** + **Pix4D Live**
- `data-year="rc-2018-2019"` → "2018 – 2019 · Reality Capture · Pipeline & integrated drone work" — 2 grouped entries (one for the pipeline test campaign, one for the integrated drone use during Elbtower / Nationalgalerie / Bachstraße / Rosenthaler / Tegel-Nord)

The existing 2024 Pankow entry stays at the top — it can live in its own one-row group `rc-2024` or sit above the 2022 group as a single "2024" header. Use one-row group for consistency.

Each `<li class="refs-row" data-category="reality-capture">` keeps the existing markup pattern. The right column (`refs-row-svc`) gets the **service** + **·** + **AG: <client>** appended, e.g. `Photogrammetrie · Volumen · AG: Meyer Erdbau GmbH`.

Default expanded state: 2022 group open, others collapsed.

### Change 2 — Counts and totals on `/referenzen`

- Hero h1 stays "Über 50 Bauprojekte. 15 Jahre Erfahrung." → change to **"Über 80 Bauprojekte. 15 Jahre Erfahrung."** (DE) / **"Over 80 construction projects. 15 years of experience."** (EN)
- Stats bar `<strong>52</strong>` → `<strong>82</strong>`
- "Vollständige Projektliste" subtitle `60 Projekte · 2008 – 2024` → `82 Projekte · 2008 – 2024`
- Each `refs-yrhead-count` updated to reflect the new entries in that group

### Change 3 — `/referenzen` Reality Capture marquee bento

Section: `<div class="rc-head rv">` immediately followed by `<div class="refs-bento">` (the 8 cards).

Add **4 new cards** as `<div class="ref-card rv" data-cat="reality-capture …">` matching the existing markup. Insert near the top of the bento so they appear above the existing 8 cards (preserving the special wide/tall variants of Oldtimer, Fischerstraße, Sporthalle, Pix4D Live).

The 4 new cards:

1. **BV Tesla Gigafactory Grünheide** — `data-cat="reality-capture"`. Title: "BV Tesla Gigafactory — Grünheide". Sub: "60 ha Erweiterungsflächen · 3D-Photogrammetrie · Massenermittlung". Meta: "Grünheide · 2021" / "60 ha" / "AG: Meyer Erdbau". Variant: standard.
2. **BV SQUARE Berlin** — `data-cat="reality-capture"`. Title: "BV SQUARE — Multi-Year Drone Documentation". Sub: "Monatliche 3D/2D-Baudoku 2021–2022 · Pflasterprotokoll · 12 ha Baufeld C". Meta: "Berlin · 2021–2022" / "Multi-Year" / "AG: Bauwert / Keller". Variant: wide (`ref-card--wide`).
3. **Sage Restaurant & Sage Beach** — `data-cat="reality-capture scan"`. Title: "Sage Restaurant & Sage Beach — Berlin". Sub: "3D-Laserscan · Grundrisse + Ansichten · 360°-Tour auf Google Maps". Meta: "Berlin · 2021" / "LiDAR + 360°" / "AG: Sage Gastro". Variant: standard.
4. **Deponie Golm** — `data-cat="reality-capture"`. Title: "Deponie Golm — Hebungs-/Setzungsanalyse". Sub: "Photogrammetrische Drohnenbefliegung · DTM · 3D-Modell für Bewegungsanalyse". Meta: "Golm · 2021" / "DTM" / "AG: Kummer". Variant: standard.

Each card uses the `onclick="go('refs')"` pattern (or `go('b1')`/`go('b2')`/`go('b3')` to deep-link to the relevant service page when appropriate). No new images needed — reuse `marketing/IMG_20210603_172033.jpg` (drone) for Tesla, `marketing/Screenshot_20210701_221949.jpg` for SQUARE, `marketing/Treehouse-10092021_214546_20211009_220545.jpg` is taken; for Sage and Golm fall back to `marketing/IMG_20200911_151619_962_mix01.jpg` and `marketing/IMG_20210317_121648.jpg` respectively, with TODO-comment in HTML so the user can swap real images later.

### Change 4 — `/referenzen` Reality Capture intro copy

Update the section header copy in `<div class="rc-head rv">`:
- Subtitle "Seit 2020 liefern wir zentimetergenaue Drohnenvermessungen…" → **"Seit 2018 liefern wir zentimetergenaue Drohnenvermessungen, photorealistische 3D-Modelle und LiDAR-Bestandserfassungen — über 35 dokumentierte Reality-Capture-Projekte von der Großbaustelle bis zum Altbau-Interior."**
- EN equivalent updated symmetrically.

### Change 5 — Service-page chip strips

On each of the three pages `<div id="p-b1">`, `<div id="p-b2">`, `<div id="p-b3">`, append a small "Ausgewählte Projekte" strip just before the section that already exists at the bottom of each page (find the last `<div class="sec">` and add a new sibling above the page-closing `</div>`).

Markup pattern (matches existing `tags`/`tag` styling and `lbl` heading style):

```html
<div class="sec">
  <div class="lbl rv" data-de="Ausgewählte Projekte" data-en="Selected Projects">Ausgewählte Projekte</div>
  <div class="tags" style="margin-top:.75rem;gap:.5rem;flex-wrap:wrap">
    <button class="tag" type="button" onclick="go('refs')">BV Tesla Grünheide · 60 ha</button>
    …
  </div>
</div>
```

**Per-page chip rosters:**

- **`b1` (3D-Bestandserfassung):** Sage Restaurant & Beach · Tree House Berlin · Polytapes Maschinenhalle · Fahrrad Fritsch · Doppelsporthalle Gustav Freytag · Altbau Fischerstraße
- **`b2` (Baustellen-Monitoring):** BV SQUARE (monatlich) · BV CROWN1 · BV SCALE · BV GoWest · BV Storkower 140/142 · BV Heidestraße TRACK + MI3
- **`b3` (Inspektion & Wartung — should be Massen / Volumen / Hebung in this context):** BV Tesla Grünheide · Deponie Golm · BV BLUBB · Liegenschaften Germendorf · BV SQUARE Baufeld C · BV Eiswerk

(Note: `b3` is "Inspektion & Wartung" per the home bento — but the user's drone projects with "inspection-like" surface area are actually the volumetric / earth-movement jobs. We use `b3` for those because that's the page closest to "monitoring change over time." If the b3 page is strictly inspection of structures, route those chips to `b2` instead. **Implementation should verify the b3 page intent before placing.**)

All chips link via `onclick="go('refs')"`. No deep-link to specific entries — the `/referenzen` page is the canonical home for the detail.

## Acceptance criteria

1. `/referenzen` chronological list shows 4 RC year groups (plus a single 2024 row) with correct counts in `refs-yrhead-count`. The filter "Reality Capture" surfaces all of them.
2. Each new entry shows `AG: <client>` at the end of the `refs-row-svc` span.
3. Hero count and stats updated to 80 / 82.
4. RC marquee bento has 12 cards (8 existing + 4 new), with the 4 new cards visually consistent with existing card markup (no broken layout, no new CSS).
5. `b1`, `b2`, `b3` each show an "Ausgewählte Projekte" chip strip above the existing closing CTA, with chips clicking through to `/referenzen`.
6. DE / EN parity preserved on every text node (each card/row/chip has `de-only` + `en-only` siblings or `data-de` / `data-en` attributes following the existing pattern).
7. No CSS, no JS function added. All changes are additions/edits inside existing markup conventions.

## Verification

- Open the page in the browser preview.
- Click the "Reality Capture" filter chip — confirm only RC rows are visible across all year groups.
- Expand each new year group — confirm entries match the source list and AG names appear.
- Toggle DE / EN — confirm parity.
- Click each new marquee card — confirm it navigates somewhere sensible (b1 / b2 / b3 / refs).
- Visit `b1`, `b2`, `b3` — scroll to bottom — confirm chip strip appears, chips clickable.

## Risk / open questions

- **`b3` page intent.** If `b3` is strictly facade/structural inspection (drone photo of cracks), the volume-monitoring chips belong on `b2` instead. Verify on first implementation pass and adjust roster if needed.
- **Marquee card images.** Using existing assets means two new marquees share images with prior cards. Acceptable for v1; the user can swap dedicated photos later. Mark with `<!-- TODO: replace with project-specific image when available -->`.
- **Total count "82".** Counting: 52 (existing geotechnik+RC) − 8 (old RC) + 35 (new RC, including the rolled-up 2018-19 entries) − overlaps ≈ 82. Recount during implementation; adjust hero number.

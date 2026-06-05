# Open-Source Design Resources Integration

Sources integrated into this skill from GitHub open-source projects:

---

## Open Color Palette (yeun/open-color)

**Source:** https://github.com/yeun/open-color — 13 colors × 10-step grayscale.

**Purpose in this skill:** Replace manual saturation/lightness calculation in Step 2 with a pre-curated color scale. When deriving 辅助色 / 高亮背景色 from a brand color, find the closest hue in Open Color and use its predefined lighter/darker steps instead of hand-tuning HSL.

**How to use:**
- Brand primary `#C2410C` → closest Open Color: Orange 9
- 辅助色 (降饱和+提明度) → Orange 7 or Orange 6
- 高亮背景色 → Orange 1 or Orange 0 (near-white)
- 语义色 (green/amber/red) → use Open Color's fixed green/red/yellow scale directly

**Key benefit:** Eliminates the need to manually tweak HSL parameters. The 10-step per-hue scale is already visually tested by the Open Color maintainers for equal perceived step sizes.

**Color scales (abbreviated for warm/cool use cases):**

Orange: #FFF4E6(0) → #FFE8CC(1) → #FFD8A8(2) → #FFC078(3) → #FFA94D(4) → #FF922B(5) → #FD7E14(6) → #F76707(7) → #E8590C(8) → #D9480F(9)

Blue: #E7F5FF(0) → #D0EBFF(1) → #A5D8FF(2) → #74C0FC(3) → #4DABF7(4) → #339AF0(5) → #228BE6(6) → #1C7ED6(7) → #1971C2(8) → #1864AB(9)

Teal: #E6FCF5(0) → #C3FAE8(1) → #96F2D7(2) → #63E6BE(3) → #38D9A9(4) → #20C997(5) → #12B886(6) → #0CA678(7) → #099268(8) → #087F5B(9)

Green (semantic): #EBFBEE(0) → #D3F9D8(1) → #B2F2BB(2) → #8CE99A(3) → #69DB7C(4) → #51CF66(5) → #40C057(6) → #37B24D(7) → #2F9E44(8) → #2B8A3E(9)

Yellow (warning): #FFF9DB(0) → #FFF3BF(1) → #FFEC99(2) → #FFE066(3) → #FFD43B(4) → #FCC419(5) → #FAB005(6) → #F59F00(7) → #F08C00(8) → #E67700(9)

Red (error): #FFF5F5(0) → #FFE3E3(1) → #FFC9C9(2) → #FFA8A8(3) → #FF8787(4) → #FF6B6B(5) → #FA5252(6) → #F03E3E(7) → #E03131(8) → #C92A2A(9)

**Integration point in SKILL.md:** Step 2 → "色相环候选值可参考 references/open-source-design-resources.md 中 Open Color 调色板"

---

## Every Layout CSS Patterns (EveryLayout/every-layout)

**Source:** https://github.com/EveryLayout/every-layout — CSS algorithmic layout patterns.

**Purpose in this skill:** Replace hardcoded grid/flex with reusable CSS utility classes for report and comparison table layouts. Zero JS, zero frameworks, pure CSS.

### `.stack` — Vertical rhythm
```css
.stack { display: flex; flex-direction: column; gap: var(--s1, 1.5rem); }
.stack > * + * { margin-block-start: 0; }  /* reset cascading margins */
```

### `.cluster` — Auto-wrapping row of items
```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--s1, 1rem);
  align-items: center;
}
```

### `.sidebar` — Side-by-side with min-width breakpoint
```css
.sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--s1, 1.5rem);
}
.sidebar > :first-child {
  flex-basis: var(--sidebar-width, 20rem);
  flex-grow: 1;
}
.sidebar > :last-child {
  flex-basis: 0;
  flex-grow: 999;
  min-inline-size: 50%;
}
```

### `.switcher` — Layout that collapses at narrow widths
```css
.switcher {
  display: flex;
  flex-wrap: wrap;
  gap: var(--s1, 1rem);
  --threshold: 30rem;
}
.switcher > * {
  flex-grow: 1;
  flex-basis: calc((var(--threshold) - 100%) * 999);
}
```

**Integration point in SKILL.md:** Report HTML template CSS section → add these 4 utility classes as defaults.

---

## WCAG Contrast Ratio Calculation

**Source:** https://github.com/jrvansuita/color-contrast-checker — WCAG AA/AAA verification.

**Formula to embed in Step 3 verification:**

```text
Relative luminance (WCAG 2.1):
  L = 0.2126 * R + 0.7152 * G + 0.0722 * B
  
  where R/G/B are sRGB values linearized:
  if sRGB ≤ 0.04045: linear = sRGB / 12.92
  else: linear = ((sRGB + 0.055) / 1.055) ^ 2.4

Contrast ratio:
  CR = (L1 + 0.05) / (L2 + 0.05)
  where L1 is lighter luminance, L2 is darker

WCAG thresholds:
  AA normal text:  ≥ 4.5:1
  AA large text:   ≥ 3:1
  AAA normal text: ≥ 7:1
```

**Usage in skill:** When generating any color pair, calculate CR before writing to CSS. If CR < 4.5 for body text, warn and adjust.

**Integration point in SKILL.md:** Step 3 → replace vague "WCAG AA ≥ 4.5:1" with the actual formula + a verification example.

---

## Refactoring UI Spacing / Font Scale

**Source:** https://github.com/iptop/refactoring-ui — Chinese translation of Refactoring UI.

**Key rules for this skill:**

**Font size ratio:**
```text
Body: 16px (base)
Small: 14px  (body × 0.875)
Caption: 12px (body × 0.75)
H4: 18px  (body × 1.125)
H3: 22px  (body × 1.375)
H2: 28px  (body × 1.75)
H1: 36px  (body × 2.25)
```
Compare with current skill's own table in 字号层级规则 — the ratios are similar (both use ~1.25x steps) but Refactoring UI uses slightly wider gaps which work better for landing-page style reports.

**Spacing scale (4px base):**
```text
2 → 4 → 8 → 12 → 16 → 24 → 32 → 40 → 48 → 64 → 80 → 96
```
Compare with Fibonacci (8/13/21/34/55) in current skill. The 4px-based scale is more tailwind-like and practical for consistent padding/margin across components. Recommend using the 4px scale for page-level layout and Fibonacci for table-level detail.

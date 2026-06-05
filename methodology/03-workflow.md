# Workflow: From Request to Delivery

The workflow is the execution mechanism — it translates the 10 disciplines from principles into actions. Every step has a clear decision gate.

---

## Step 0: Quick Routing (30 seconds)

Determine output type and approach based on request:

### Page Type Selection
```
Request → Match PAGE_TYPE:
  comparison-matrix  → Flat IA (side-by-side comparison)
  industry-report    → Hierarchical IA (layered analysis)
  guide              → Step IA (phased roadmap)
```

### Style & Data Decision
```
① Data sufficient?        → No → Change topic or downgrade comparison
② Audience?               → Bank/School/Education Bureau/Tech
③ Motive?                 → Risk Aversion/Gain Seeking/Cost Reduction
④ Delivery scenario?      → Projector/Print/Mobile
⑤ Comparison type?        → Type1 PK / Type2 Scenario / Type3 Benchmarking
⑥ IA structure?           → Flat/Hierarchical/Step
```

### Tempo Branch
```
Tight deadline + same-audience template exists   → Adapt content (5 min)
Tight deadline + no template                     → Speed path (15 min)
No deadline                                      → Full workflow (below)
```

---

## Step 1: Data Research & Verification

Research organization: three dimensions regardless of output type.

### Research Dimensions

| Dimension | Focus | comparison-matrix | industry-report | guide |
|-----------|-------|-------------------|-----------------|-------|
| **Supply Side** | Products, vendors, tech stacks | Solution providers | Vendors | Solution providers |
| **Demand Side** | Customers, budgets, procurement | User departments | Clients | Executing teams |
| **Market Side** | Trends, competitive landscape | Industry practices | Industry | Industry benchmarks |

### Risk-Based Research Depth

| Risk Level | Approach | Time |
|-----------|----------|------|
| Low | One search pass | Quick |
| Medium | Two-step search + cross-reference | Moderate |
| High | Full process + independent audit | Thorough |

### Data Audit Table

Every claim gets classified:

| Rating | Meaning | Action |
|--------|---------|--------|
| ✅ Verified | Public data, cross-referenced | Use with source link |
| ⚠️ Estimate | Industry report, aggregated | Use with caveat label |
| ❌ Not Found | Unverifiable | Discard, do not publish |

**If data insufficient**: downgrade comparison type (Type1 PK → Type2 scenario comparison) or inform user to change topic. Never fabricate.

### Comparison Type Selection

| Type | When | Format |
|------|------|--------|
| Type1 — Horizontal PK | Equal-scale options, symmetric data | Side-by-side matrix |
| Type2 — Scenario Best Practice | Asymmetric data, one strong reference | "How X does it" format |
| Type3 — Industry Benchmark | Clear industry leader exists | Against-the-standard format |

**Default recommendation** for most enterprise contexts: Type2 (scenario). It handles data asymmetry gracefully and maps directly to the audience's real work.

---

## Step 2: Audience Profiling

Before any design work: confirm the audience profile.

### Decision Chain Mapping

```
Who reads this?         → Primary audience
Who approves based on this? → Secondary audience
Who implements?         → Tertiary audience
```

Each role gets served in the same document via pyramid structure (conclusion for the decider, detail for the doer).

### Display Scenario

| Scenario | Constraint |
|----------|-----------|
| Projector | Larger font (≥16px), high contrast, minimal text per slide |
| Print | CMYK-safe colors, crop marks consideration |
| Mobile | Single column, touch targets ≥44px |
| Desktop | Multi-column OK, hover states matter |

Reference: `audience-layout-tokens.md` for font sizes, line heights, border radii, page widths per audience type.

---

## Step 2+: Fallback Trigger Check

Two classes of trigger:

### Input Failure
```
Insufficient data / Unclear audience / Unfamiliar industry /
No relevant case studies / Color derivation stuck →
→ Load fallback path → produce 80/100 output (not 40/100)
→ Annotation box explains why fallback was triggered
```

### Reasoning Failure
```
IA can't decompose / MECE grouping fails / Color won't converge /
Semiotic symbols conflict / Recommendation can't be derived →
→ Load fallback path → produce 80/100 output
```

**Threshold**: confidence < 60% on any critical path → trigger fallback.

---

## Step 2+: Information Architecture Confirmation

Confirm content organization before writing a line of HTML:

```
□ Content inventory — main content / supporting / reference separated
□ Labeling system — naming passes "Would user guess the content?"
□ Navigation hierarchy — appropriate for page type
□ Scan path test — decision-maker's journey proves point in 3 seconds
```

---

## Step 3: Color Derivation (Mandatory Before HTML)

Color is never chosen from a palette — it's derived through a three-step process.

### Step 3a: Theory → Direction

**Economics + Sociology** determine the color direction:

| Motive | Color Direction |
|--------|----------------|
| Risk Aversion | Cool tones, low saturation, neutral dominant |
| Gain Seeking | Warm accents, higher saturation, vibrant highlights |
| Cost Reduction | Functional, minimal, neutral-heavy |

### Step 3b: Tool → Values

Use the [Open Color](https://yeun.github.io/open-color/) system to derive a 6-value palette (primary, background, text, border, accent, muted).

### Step 3c: Real-Product Calibration → Stay Current

Before finalizing colors, audit against real products:

```
Derived palette → Compare:
  Stripe: Purple #635BFF + white + light borders (modern)
  Notion: Blue #0075DE + warm white #F6F5F4 (warm)
  Linear: Gray-scale + brand accent (minimal)
  Feishu: Blue #3370FF + white (enterprise)

Self-check: Does my palette look dated next to these?
  → If yes → lighten, reduce dark blocks, use color sparingly
```

**Role of calibration**: It's a negative check ("does this look bad?"), not a positive directive ("copy this color"). It prevents the "2015-era enterprise portal" look.

### Step 4: Accessibility

WCAG 2.1 AA compliance (contrast ratio ≥ 4.5:1) for all text/background pairs.

Special case: on non-white backgrounds, use `color: inherit; opacity: 0.85` instead of CSS `var(--text-muted)`.

---

## Step 4: Preflight Check

Before moving to output generation:

```
□ Color Ready — values derived + calibrated → yes/no
□ Layout Ready — IA structure + product references checked → yes/no
□ Audience Ready — audience parameters loaded → yes/no
```

All three must be YES. Any NO → return to corresponding step.

---

## Step 4+: Conclusion Quality Gates (Universal)

**Applied to every concluding statement** (core findings, recommendations, proposal rationales) — regardless of page type.

### Gate 1: Stakeholder Check
```
Does this conclusion cover:
□ Supply Side (vendor/provider perspective)
□ Demand Side (customer/user perspective)
□ Market Side (industry/market perspective)
Missing any side → Conclusion is biased, research more
```

### Gate 2: Novelty Check
```
If you remove the data/case from this statement, does it still hold?
  YES → It's common sense. Downgrade or rewrite.
  NO → It might be a real insight. Keep.
```

### Gate 3: Actionability Check
```
Would this conclusion change the audience's decision?
  YES → Keep.
  NO → It's a pseudo-insight. Delete or rewrite.
```

**Execution**: After generating all conclusions, run each through all three gates. Only pass statements that clear all three.

---

## Step 5: Output Generation

Structure varies by page type:

### Comparison Matrix — Recommendation First
```
Title + one-line positioning
  → Recommendation (pyramid top)
    → Key differences (top 3 rows, marked)
      → Full comparison (≤10 rows, sticky first column)
        → Objection box (boundary conditions)
          → Footer
```

### Industry Report — SCQA Structure
```
Header (Situation-Complication-Question-Answer)
  → Core findings (3-5 key insights)
    Each insight includes:
      - Specific data point or case evidence
      - Source label (✅/⚠️/❌)
      - Reasoning chain (data → judgment → conclusion)
    → Multiple sections (MECE grouped)
      → Objection box
        → Footer
```

### Guide — SCQA + Roadmap
```
Header (SCQA)
  → Core conclusion (transformation goal + key phases)
    → Phase 1-3 (conclusion-first per phase)
      → Objection box
        → Footer
```

### Recommendation Structure (industry-report, guide)

Every recommendation should include:
- **Timeline**: Next 12 months (short-term) / Next 24 months (medium-term)
- **Priority**: P0/P1/P2
- **Expected outcome + resources needed + risk notes**
- **No-Regret Move** (optional): Action worth taking even if the prediction is wrong

---

## Step 5: Final Acceptance

**7-item gate before delivery:**

```
□ Data     — Verified, traceable sources
□ Structure — IA confirmed + Pyramid argument structure MECE-compliant
□ Audience — Parameters loaded (colors, font sizes, line height, radius)
□ Color    — Derived + calibrated + WCAG passing
□ Accessibility — CTA ≥44px, hover/focus complete, spacing generous
□ Quality  — All conclusions passed 3 gates (Stakeholder/Novelty/Actionability)
□ Recommendation — Conclusion-first, objection box pre-footer
```

All 7 must pass. Any NO → fix before delivery.

---

## Step 6: Delivery & Archive

- Archive: `/output/<YYYY-MM-DD_project-name>/report.html` + `meta.md`
- Record failures to `output-tracker.md` (not successes)
- After 20 recorded failures → root cause analysis

---

## Decision Flow (Summary)

```
Request
  ├── Type + Audience + Tempo
  ├── Data Research → Audit → Sufficient?
  │     ├── Yes → Continue
  │     └── No → Downgrade or change topic
  ├── Audience Profiling → Confirmed?
  ├── Color Derivation → Calibrated + WCAG?
  ├── Preflight → All 3 ready?
  ├── [2D+ Quality Gates on every conclusion]
  ├── Output → Type-specific structure
  └── Final Validation (7 items) → Delivery
```

Every step has an exit path. No step proceeds without its gate passing.

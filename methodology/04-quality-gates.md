# Quality Gates: Preventing Mediocre Output

Quality gates are the difference between "this looks AI-generated" and "this looks professionally done." They are **not optional checks** — they are the mechanism that prevents the system from collapsing to the statistical mean.

---

## Gate Locations in the Workflow

```
Data → [Stakeholder Check] → Analysis → [Novelty + Actionability Checks] →
Color → [Calibration Check] → Layout → [Preflight] →
Output → [Final Validation: 7 gates] → Delivery
```

---

## Gate 1: Stakeholder Check (After Research)

**Location**: After data collection, before writing conclusions.

**Purpose**: Prevent biased analysis that considers only one side of a decision.

**Process**: For every conclusion, verify coverage across three perspectives:

```
This conclusion covers:
☐ Supply Side — Vendor/provider perspectives, product capabilities
☐ Demand Side — Customer/user perspectives, budget constraints, operational needs
☐ Market Side — Industry trends, competitive landscape, market data

Missing any side → the conclusion is biased → supplement research
```

**Common failure**: Comparison matrices that show vendor capabilities (Supply) but ignore operational burden (Demand) or future-proofing (Market). Fix by adding a row for "integration effort" and "vendor roadmap."

---

## Gate 2: Novelty Check (Before Writing)

**Location**: Before writing any insight statement into the output.

**Purpose**: Eliminate common-sense statements masquerading as insight.

**Method**: The "Delete Test"

```
If you delete the data/case evidence from this statement, 
does the statement still hold true?

YES → The statement is common sense. 
      Either back it with stronger specific evidence, 
      or downgrade/demote it.
      
NO → The statement is a potential insight.
      Keep it, ensure the evidence is solid.
```

**Examples of failed novelty check (DO NOT publish)**:
- "AI is transforming the industry" → Common sense, delete
- "Security is important for financial systems" → Universal truth, delete
- "Cloud adoption is increasing" → Everyone knows this, delete

**Examples that pass novelty check**:
- "AI canteen penetration reached 40% with 50%+ YoY growth (source: industry report ⚠️), and competitors haven't entered this niche" → Data-backed, non-obvious
- "At current burn rate, Vendor X's cash runway supports 18 months of R&D, putting their AI roadmap at risk" → Specific, actionable

**Stringency level**: A/B classification
| Grade | Meaning | Action |
|-------|---------|--------|
| A | New insight, data-driven | Publish as core finding |
| B | Data-backed but known | Publish but don't headline |
| C | Common sense even with data | Delete or significantly upgrade evidence |

---

## Gate 3: Actionability Check (After Recommendation)

**Location**: After writing recommendations, before output generation.

**Purpose**: Ensure every output changes someone's decision.

**Method**:

```
Would this conclusion change the audience's decision?
  YES → Keep, this is a real insight
  NO → Pseudo-insight, rewrite or delete
```

**Test**: After reading your recommendation, ask: "What will the reader DO differently?"
- "They might choose vendor A over vendor B" → Pass
- "They would know that AI is important" → Fail (they already know)

---

## Gate 4: Color Calibration (During Visual Design)

**Location**: After color derivation, before writing CSS.

**Purpose**: Prevent the "enterprise portal circa 2015" look.

**Method**: Compare against real products:

```
Self-check questions:
1. Does my palette look dated next to Stripe/Notion/Figma?
2. Am I using large dark blocks? (Modern: minimal dark, brand color as accent)
3. Could this be a Bootstrap 3 theme from 2014?
```

**Common calibration failures and fixes**:

| Problem | Fix |
|---------|-----|
| Dark header bar | White header + 2px brand-color bottom border |
| Large brand-color background blocks | Brand color only on badges/borders/icons |
| Dark row fill in tables | White background + brand-color underline |
| Heavy borders (2px+) | 1px or 0.5px borders, or no borders |
| Multiple saturated colors | One accent color, everything else neutral |
| Gray `#999` text | Use `opacity: 0.85` on non-white backgrounds |

---

## Gate 5: Preflight (Before Code Generation)

**Location**: After all analysis, before writing HTML.

**Purpose**: Prevent wasted effort on incomplete reasoning.

**Checks**:

```
☐ Color Ready — values derived, calibrated against products, WCAG passing
☐ Layout Ready — IA structure confirmed, product reference layouts reviewed
☐ Audience Ready — Tokens loaded (fonts, sizes, spacing, radius)
```

All three must pass. One NO → return to the corresponding step.

---

## Gate 6: Final Validation (Before Delivery)

**Location**: After output generation, before packaging.

**7-item gate**:

```
1. DATA     — All claims have verified, traceable sources
2. STRUCTURE — IA structure confirmed, MECE grouping, pyramid argument
3. AUDIENCE — Tokens loaded and applied (colors, fonts, sizes, radius)
4. COLOR    — Derived + calibrated + WCAG AA (4.5:1) passing
5. ACCESSIBILITY — CTA ≥44px, hover/focus on all interactive elements, spacing
6. QUALITY  — Every conclusion passed Gates 1-3 (Stakeholder/Novelty/Actionability)
7. RECOMMENDATION — Conclusion-first structure, objection box pre-footer, 
                     timeline + priority for report/guide types
```

One failure → return to fix. Zero exceptions.

---

## Gate 7: Output Tracker (Continuous Improvement)

**Location**: After delivery.

**Purpose**: Feed real-world failures back into the system.

**Process**:
```
☐ Output delivered
☐ Any problems? (client complained, looked wrong, felt off)
☐ If YES → Log to output-tracker.md:
    - What went wrong
    - Which step failed
    - Root cause (process flaw vs domain knowledge gap)
☐ If NO → Don't log (only failures are recorded)

After 20 entries → Root cause analysis:
  - Pattern: process issues → fix in workflow
  - Pattern: domain issues → fix in references
```

This is the self-improvement mechanism. Without it, the system learns nothing from production failures.

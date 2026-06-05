# Hermes Design Decision Engine

**A multi-disciplinary reasoning framework that produces context-optimal design decisions and auditable consultancy reports — not templates, not generic output, but analysis and recommendations with traceable evidence chains.**

> "When you ask an LLM to 'generate a professional comparison page,' it outputs the statistical average of every professional page in its training data. Never terrible. Never excellent. Never context-specific."
>
> This framework fixes that.

---

## Why This Exists

Enterprise design work suffers from a specific failure mode: **AI-generated output that looks AI-generated**. It's dense, it's generic, it's safe, and it fails to convince decision-makers who have seen hundreds of vendor comparison tables.

The root cause isn't the LLM's capability — it's the **absence of reasoning constraints**. A designer with 20 years of experience knows intuitively when a blue feels "too corporate" or a layout feels "too crowded." An AI agent has no such intuition. It defaults to the comfortable mean.

This framework replaces tacit intuition with **explicit disciplinary reasoning** — 10 disciplines, each applying a specific constraint that pushes the output toward true contextual fit.

---

## Architecture (v1.7.0)

The framework evolves through four layers, driven by **Report Intent**:

```
Report Intent (decision / education / research)
    ↓
Pipeline Selection
    ↓
Thinking Layer (10 disciplines) → Decision Engine (criteria + rubric + evidence)
                              → Assurance Layer (sensitivity + confidence)
    ↓
Layout Intelligence (section composition + visual hierarchy)
    ↓
HTML（当前仅此一路）
```

### Report Intent Classification

Three pipeline paths, selected automatically at Step 1:

| Intent | What It Does | Includes |
|--------|-------------|----------|
| **decision** | Vendor comparison, procurement, investment | Scoring matrix, rubric, evidence badges, sensitivity analysis |
| **education** | Learning guides, skill roadmaps, conceptual frameworks | Concept maps, taxonomies, learning paths, scenario matrices. No scoring. |
| **research** | Industry analysis, trend reports, market studies | Evidence chains, trend analysis, scenario forecasting, assumption boundaries. No scoring. |

### Decision Engine (2B+3)

Criterion-first scoring with full audit trail:

- **weight_rationale** — why each weight percentage was chosen (all marked ESTIMATE)
- **rubric** — scoring card with grade conditions and score ranges
- **rubric_match** — which grade the facts match, per candidate
- **rubric_level** — source traceability (public / experience / derived)
- **evidence** — FACT / ESTIMATE / ASSUMPTION per score
- **sensitivity** — breakpoint analysis (which weight change flips ranking)
- **layer + maturity annotations** — every field tagged with its architectural layer and validation maturity

### Assurance Layer

Proves the recommendation is defensible:

- Evidence chain (FACT/ESTIMATE/ASSUMPTION with sources)
- Scoring rubric with source traceability (public/experience/derived)
- Sensitivity analysis (weight breakpoint → ranking flip)
- Recommendation confidence (Phase 2)

### Layout Intelligence (2B+4)

Controls visual hierarchy, not just card arrangement:

- page_pattern: executive_summary / comparison_first / roadmap_planning / problem_solving / compliance_report
- hero_type with merged recommendation box
- KPI strip with non-duplicated metrics
- Title system: L1-L4 hierarchical numbering
- Chart layout: insight_driven (each chart paired with its own insight card)
- Section density: compact / medium / spacious
- Visual priority: decision / data / balanced

---

## What You'll Find Here

```
hermes-design-decision-engine/
├── methodology/              # Independent framework documentation
│   ├── 01-core-philosophy.md # Why disciplines, not templates
│   ├── 02-ten-disciplines.md # The 10 reasoning disciplines
│   ├── 03-workflow.md        # Step-by-step execution process
│   ├── 04-quality-gates.md   # Quality control (7 gates)
│   └── 05-glossary.md        # Terminology
├── hermes-skill/             # Hermes Agent implementation (v1.7.0)
│   ├── SKILL.md              # Runnable agent skill definition
│   ├── scripts/chart_svg.py  # Zero-dependency chart generator
│   ├── references/           # 28 reference files
│   │   ├── decision-assurance.md    # Evidence + rubric + sensitivity
│   │   ├── layout-strategy.md       # Page pattern + section composition
│   │   ├── rendering-quality.md     # Visual consistency checklist
│   │   ├── design-tokens.md         # Direction strategy
│   │   ├── color-harmony.md         # Color derivation
│   │   └── ... (23 more)
│   └── templates/           # HTML skeleton templates
├── examples/                 # Real-world output examples
└── CONTRIBUTING.md           # How to improve this framework
```

## Version History

| Version | Milestone |
|---------|-----------|
| v1.0-v1.2 | Report generation capability |
| v1.3 | Chart generation (SVG, zero-dependency) |
| v1.4 | Auditable recommendation scoring |
| v1.5 | Layout Intelligence (page_pattern, hero, KPI strip, title system) |
| v1.6 | Decision Assurance (criterion-first, rubric, evidence, sensitivity) |
| **v1.7** | **Report Intent pipeline (decision/education/research) + layer annotations** |

## Getting Started

### To Use the Methodology (No Software Required)

Just read the `methodology/` directory. The framework is documented as pure reasoning steps — you or your AI agent can apply it to any output with any tool.

### To Run the Hermes Agent Skill

1. Install [Hermes Agent](https://hermes-agent.nousresearch.com)
2. Copy or symlink `hermes-skill/` to your Hermes skills directory
3. The agent will load the skill logic and apply the multi-pipeline workflow

## License

MIT — free to use, modify, and distribute. We'd love your improvements back via PR.

---

**Built from production use in enterprise fintech, campus payments, and smart-campus consulting. Every failure logged in output-tracker, root-caused in batches of 20, continuously improving.**

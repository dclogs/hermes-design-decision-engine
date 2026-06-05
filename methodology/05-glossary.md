# Glossary

## Core Concepts

| Term | Definition |
|------|-----------|
| **Design Decision Engine** | A reasoning framework that produces context-optimal design decisions by applying multiple disciplinary constraints, rather than selecting from pre-built templates. |
| **Discipline** | An academic or professional field whose principles act as a reasoning constraint on the design output. Each discipline contributes a specific perspective on correctness. |
| **Anti-Mean-Collapse** | The effect where an LLM, asked to "generate something professional," outputs the statistical average of its training data. Disciplines counteract this by constraining the solution space toward context-specific optimality. |
| **Constraint** | A rule derived from a discipline that narrows the set of valid design choices. More constraints = less generic output. |
| **Tacit Knowledge Externalization** | The process of converting a human designer's intuitive sense ("this blue doesn't feel right") into explicit, executable steps (hue-wheel derivation + product calibration + WCAG check). |
| **Metacognitive Monitoring** | The agent's ability to self-assess its own output quality at each step and decide whether to continue, fall back, or restart. |

## Methodology

| Term | Definition |
|------|-----------|
| **Pyramid Principle (Minto)** | A communication structure where the conclusion is stated first, followed by grouped supporting arguments (MECE), then detailed evidence. Originated from Barbara Minto's consulting methodology at McKinsey. |
| **Information Architecture (IA)** | The structural design of shared information environments: how content is organized, labeled, and navigated. |
| **MECE** | Mutually Exclusive, Collectively Exhaustive — a grouping principle ensuring categories don't overlap (ME) and cover all possibilities (CE). |
| **SCQA** | Situation-Complication-Question-Answer — a narrative structure for opening analytical documents. |
| **Modular Scale** | A set of font sizes that follow a mathematical ratio (e.g., 1.067, 1.125, 1.25, 1.333), creating harmonic proportion across typographic levels. |
| **4px Grid** | A spacing system where all padding, margin, and gap values are multiples of 4px (or 8px for larger gaps), ensuring visual rhythm. |

## Quality Gates

| Term | Definition |
|------|-----------|
| **Novelty Check** | A gate that identifies and removes common-sense statements by asking: "If you remove the data from this statement, does it still hold?" |
| **Actionability Check** | A gate that removes pseudo-insights by asking: "Would this conclusion change the audience's decision?" |
| **Stakeholder Check** | A gate that prevents biased analysis by verifying coverage of Supply, Demand, and Market side perspectives. |
| **Confidence Level** | A data quality rating system: ✅ Verified, 📊 Industry Estimate, ⚠️ Anecdotal, ❌ Not Found (discarded). |
| | **Calibration** | The process of validating color/design choices against real-world products (Stripe, Notion, Linear) to ensure they don't appear dated. |
| | **Evidence Level** | A score-level traceability tag: FACT (publicly verifiable), ESTIMATE (industry-based inference), ASSUMPTION (no reliable data). Each score must carry one. |
| | **Rubric** | A scoring card per criterion defining grade tiers with verifiable conditions (e.g., "has national certification → 95-100"). Replaces agent intuition with traceable matching. |
| | **Rubric Level** | Source traceability of the rubric itself: Public (industry standard), Experience (domain expertise), Derived (agent-constructed, lowest certainty). |
| | **Weight Rationale** | Free-text explanation per weight percentage, citing audience analysis (2B) and research findings (2A). All weights marked ESTIMATE. |
| | **Sensitivity Analysis** | Breakpoint computation: for each criterion, how much must its weight drop to flip the ranking. Identifies which dimensions are decision-critical. |

## Output Types

| Term | Definition |
|------|-----------|
| **Comparison Matrix** | A side-by-side comparison of multiple options, with recommendation column highlighted and no more than 10 dimensions. |
| **Industry Report** | A hierarchical analytical document presenting 3-5 data-backed findings, organized by MECE sections. |
| **Guide** | A phased transformation roadmap with timeline, priorities, and no-regret moves. |
| **Type1 PK (Horizontal)** | Equal-scale comparison between peers. Only used when data for both sides is symmetric. |
| **Type2 Scenario** | "Best practice" format — compare against a single strong reference when data is asymmetric. Default recommendation. |
| | **Type3 Benchmark** | Compare against an industry standard when a clear leader exists. |
| | **Report Intent** | The user's actual need behind the report: decision (procurement/vendor selection), education (learning/understanding), research (industry analysis). Drives which pipeline steps execute. |
| | **Page Pattern** | The section skeleton for a report, driven by layout_strategy. Examples: executive_summary (conclusion-first), comparison_first (table-first), roadmap_planning (phases). |
| | **Hero Section** | The top-of-page content block. When hero_type=recommendation, contains embedded recommendation box (not duplicated KPI stats). |
| | **KPI Strip** | A horizontal row of 3-4 large-number cards. Numbers are unique — no overlap with hero section content. |
| | **Insight-Driven Chart Layout** | A chart+insight pairing rule: each chart must have its own independent insight card. No standalone chart grids. |

## Technical

| Term | Definition |
|------|-----------|
| **Padding, not margin** | A visual design principle where internal spacing (padding) is preferred over external spacing (margin) for maintainable layouts. |
| **Token (Design)** | A pre-defined design parameter (font size, line height, border radius) mapped to an audience type, stored for reuse across outputs. |
| **Color derivation** | The three-step process of determining colors via theory (motive → direction), tool (Open Color → values), and calibration (product comparison → validation). |
| **WCAG 2.1 AA** | Web Content Accessibility Guidelines minimum contrast ratio of 4.5:1 for normal text. |

## Framework Components

| Term | Definition |
|------|-----------|
| **Fallback Mode** | A reduced-complexity path triggered when confidence drops below 60%, producing an 80/100 output with an explanatory annotation box. |
| **Output Tracker** | A failure-logging mechanism that records every production issue. After 20 entries, triggers a root cause analysis to distinguish process flaws from knowledge gaps. |

## Discipline-Specific Terms

| Term | Source Discipline | Definition |
|------|-------------------|-----------|
| **Fitts's Law** | Experience Design | The time to acquire a target is a function of its size and distance. → All CTAs ≥44px. |
| **Hick's Law** | Psychology | Decision time increases with the number of choices. → Max 5 CTAs per page. |
| **Jakob's Law** | Experience Design | Users prefer familiar patterns. → Use standard layouts, don't innovate on UI. |
| **Choice Overload** | Psychology | Too many options lead to decision paralysis. → Max 10 comparison rows. |
| **Anchoring Effect** | Psychology | The first piece of information disproportionately influences judgment. → Put key data first. |
| **Affordance** | Experience Design | An object's visual properties suggest how to interact with it. → Clickable items look clickable. |

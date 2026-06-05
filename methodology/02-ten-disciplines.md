# Ten Disciplines: The Reasoning Framework

Each discipline plays a specific role in the design decision process. They are organized by their function:

- **7 Foundation Disciplines** — always active, applied sequentially
- **3 Refinement Disciplines** — quality assurance, applied after structural decisions

---

## Foundation Disciplines

### 1. Economics — "Why does the audience care?"

Determines the motivational tone of the entire output. Every audience makes decisions driven by one of three core motivations:

| Motive | Tone | Color Direction | Language |
|--------|------|----------------|----------|
| **Risk Aversion** | Conservative, safe, proven | Muted blues, grays, low saturation | "Reduce risk," "Proven track record" |
| **Gain Seeking** | Ambitious, opportunity-focused | Vibrant accents, warm tones | "Growth opportunity," "Competitive edge" |
| **Cost Reduction** | Pragmatic, ROI-driven | Neutral, functional | "Cost savings," "Efficiency gain" |

**Application**: Before writing a single line, answer: what's the primary motive? This sets the emotional baseline for every subsequent decision.

### 2. Sociology — "Who is in the decision chain?"

Determines complexity and depth based on the audience's role and context.

| Decision Role | Information Needs | Layout Preference |
|--------------|-----------------|-------------------|
| C-level | Summary, ROI, risk | Sparse, high-level, bold numbers |
| Department Head | Feasibility, timeline, resources | Structured, phased, milestones |
| Technical Lead | Implementation details, specs | Dense, precise, references |
| End User | Ease of use, daily workflow | Scenario-based, simple |

**Application**: A single document often serves multiple roles. Use the pyramid structure (conclusion first, then progressively detailed sections) to serve all levels in one output.

### 3. Psychology — "What limits does the human brain have?"

Cognitive constraints that prevent overwhelm and decision paralysis.

| Principle | Application |
|-----------|------------|
| **Choice Overload (Hick's Law)** | Max 10 comparison dimensions, max 5 CTAs per page |
| **Anchoring Effect** | Put the most important data point first |
| **Recency Effect** | Put the key recommendation last (in addition to first) |
| **Cognitive Load** | Max 7±2 items per grouping, generous spacing between groups |
| **Serial Position Effect** | Best option first OR last in any list, never middle |

**Application**: The comparison matrix is intentionally limited. If you have 15 dimensions, group and prioritize to ≤10. The reader will not make a better decision with more data — they will make no decision at all.

### 4. Experience Design (UX) — "Is it easy to use?"

Functional correctness and interaction quality.

| Heuristic | Implementation |
|-----------|---------------|
| **Fitts's Law** | All CTAs ≥44px, primary action has largest target |
| **Jakob's Law** | Use standard layouts (table comparison, card grid, report structure) — don't innovate on UI patterns |
| **Affordance** | Clickable items look clickable (underline links, hover effects on rows, pointer cursor) |
| **Consistency** | Same action → same visual treatment throughout |
| **Error Prevention** | Confirmation before destructive actions, clear data source warnings |

**Application**: Run the affordance checklist before declaring "done." Hover every interactive element. Verify that the recommendation column visually pops out.

### 5. Linguistics — "Does it speak the audience's language?"

Every word choice signals competence or lack thereof.

| Rule | Example |
|------|---------|
| **Use the reader's domain vocabulary** | "Card present transactions" not "in-person payments" for banking |
| **Label dimensions as actions** | "Integration time" not "Integration difficulty" — readers act on verbs |
| **Avoid weasel words** | "Leverage," "synergize," "holistic" → delete them |
| **Short sentences for comparison tables** | Cell descriptions ≤ 15 words, with a "so what" embedded |
| **Consistent terminology** | Pick one term per concept and never switch |

**Application**: After writing, scan for terms that only insiders of the product team would use. Replace with terms the **audience** would search for.

### 6. Statistics — "Can we trust the numbers?"

Three tests every data point must pass before inclusion:

| Test | Question | Outcome |
|------|----------|---------|
| **Comparability** | Are we comparing apples to apples? | If not, downgrade comparison type |
| **Timeliness** | Is the data recent enough for this decision? | Add timestamp footnote or reject |
| **Significance** | Is the difference meaningful or noise? | Use ranges, not false precision |

**Precision Scale (Four Levels)**:

| Level | Label | Meaning | CSS Class |
|-------|-------|---------|-----------|
| ✅ | Verified | Public data, cross-referenced, source link | `badge-verified` |
| 📊 | Industry Estimate | Aggregated from credible reports | `badge-estimate` |
| ⚠️ | Anecdotal | Single source, case study, limited scope | `badge-anecdotal` |
| ❌ | Not Found | Claim cannot be verified → do not publish | (removed) |

**Application**: Every data point in the final output must carry a confidence label. If data is insufficient for a comparison type, downgrade (Type 1 PK → Type 2 scenario comparison) rather than fabricate.

### 7. Ethics — "Is this fair and transparent?"

Design decisions carry ethical weight, especially in enterprise contexts where budgets and careers are at stake.

| Principle | Rule |
|-----------|------|
| **Attribution** | Every data point has a visible source. No unattributed claims. |
| **Balance** | If comparing options, show weaknesses alongside strengths. Use `badge-warning` for known limitations. |
| **Separation** | Clearly distinguish **facts** (with source tags) from **opinions** (labeled as "our assessment"). |
| **No Omission** | A comparison that hides the loser's strengths is misleading. Every option gets its fair column. |
| **Transparency** | Any uncertainty is stated upfront, not buried in footnotes. |

**Application**: Run a bias audit before final output. Would the reader feel misled if they discovered one side's advantages were omitted? If yes, fix it.

---

## Refinement Disciplines

### 8. Narrative Design — "Does it tell a story?"

Information without narrative structure is forgettable. Every output should follow a narrative arc:

```
Problem → Tension/Conflict → Resolution → Call to Action
```

| Element | Purpose |
|---------|---------|
| **Hook** | First paragraph answers "why should I care?" |
| **Conflict** | The challenge, cost of inaction, or competitive pressure |
| **Resolution** | Your recommendation or analysis that resolves the tension |
| **Catharsis** | The outcome — what changes as a result |

**Three-Audience Verification**: The same narrative should work for three perspectives:
1. **Decider** — does it justify a decision? (Economics)
2. **Doer** — does it guide implementation? (Sociology)
3. **Observer** — does it feel true? (Ethics)

**Application**: Read the output from start to finish. Does it feel like reading a memo, or does it feel like a sequence of unconnected facts? If the latter, restructure around a narrative arc.

### 9. Mathematical Aesthetics — "Does it feel right?"

Proportions and spacing that the human eye perceives as "balanced" without conscious awareness.

| Principle | Technical Rule |
|-----------|----------------|
| **Modular Scale** | Font sizes follow a scale (1.067, 1.125, 1.25, 1.333) — not arbitrary steps |
| **4px Grid** | All padding, margin, and gap values are multiples of 4px |
| **Tuning Table** | Replace "safe" CSS values with "comfortable" ones (see design-details.md) |
| **Golden Ratio** | Sidebar : content = 1 : 1.618 (when applicable) |
| **White Space** | At least 40% of page area is empty space — density signals importance |

**Application**: After layout is done, measure. Are your spacing values multiples of 4? Does the font size scale follow a ratio? Did you replace the browser default `1.5` line-height with a tuned value?

### 10. Semiotics — "What does this *mean* beyond its function?"

Every design element carries cultural and contextual meaning beyond its surface function.

| Element | Common Meaning | Cultural Caveat |
|---------|---------------|-----------------|
| **Red** | Urgency, danger, passion | Green = good in China (stocks), Red = bad (loss) |
| **Blue** | Trust, stability, corporate | Universal, but shade matters — navy = tradition |
| **Green** | Success, growth, go | Positive across cultures, but saturation varies |
| **Top position** | Most important | Assumed globally — use for primary recommendation |
| **Borders** | Separation, clarity | Light = modern, heavy = traditional |
| **Rounded corners** | Friendly, approachable | 0px = professional/precise, 12px+ = casual/consumer |
| **Bold weight** | Emphasis, importance | Overuse = noise, use sparingly |

**Application**: After design is complete, run a semiotic audit. Does the visual hierarchy match the content hierarchy? Would the primary action's color be interpreted correctly by the target culture?

---

## Discipline Hierarchy

Disciplines have a priority order when they conflict:

```
Experience Design (function)  >  Semiotics (meaning)
  (Default: UX wins, unless a clear cultural conflict exists)
```

**Default flow**: UX generates → Semiotics audits → only override if cultural mismatch is documented.

Example: If UX says green for "recommended" (functionally correct), but the audience is a Chinese financial institution where green was historically associated with losses → Semiotics overrides. Otherwise, green stays.

---

## Discipline Summary Table

| # | Discipline | One-Liner | Primary Output |
|---|-----------|-----------|----------------|
| 1 | Economics | Motive determines tone | Recommendation voice |
| 2 | Sociology | Decision chain determines complexity | Content depth |
| 3 | Psychology | Cognitive limits prevent overwhelm | Row/column limits |
| 4 | Experience Design | Functional correctness | Interactive quality |
| 5 | Linguistics | Domain vocabulary builds trust | Terminology |
| 6 | Statistics | Data must be trustworthy | Source labeling |
| 7 | Ethics | Fair and transparent presentation | Balanced coverage |
| 8 | Narrative Design | Story structure aids retention | Flow/arc |
| 9 | Mathematical Aesthetics | Proportions feel "right" | Spacing/sizing |
| 10 | Semiotics | Cultural meaning beyond function | Visual interpretation |

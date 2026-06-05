# Core Philosophy: Design Decision Engine

## The Problem with AI-Generated Design

When you ask an LLM to "generate a professional comparison page," it outputs the statistical average of every professional page in its training data. The result is never terrible — but it can never be excellent.

Average is safe. Average is forgettable. Average is not what wins enterprise contracts.

**The gap between "good enough" and "truly professional" is not about prettier templates. It's about the reasoning process that professional designers use unconsciously.**

## The Insight: Disciplines as Constraints

Human designers rely on 20+ years of tacit knowledge. A senior designer sees a blue header and says "this blue feels too corporate" — she's right, but she can't fully articulate why. Her intuition is the product of thousands of decisions absorbed over a career.

An AI agent has no tacit knowledge. It has language, pattern matching, and a tendency toward statistical mean.

Our solution: **Replace tacit intuition with explicit disciplinary reasoning.**

Each discipline acts as a constraint on the output. The more constraints applied, the further the output deviates from the statistical mean — and the closer it gets to the optimal solution for that specific context.

```
Statistical Mean (80/100)
    ↓
+ Economics constraint (motive → tone)
    ↓
+ Psychology constraint (choice overload → ≤10 rows)
    ↓
+ Statistics constraint (data confidence → source labeling)
    ↓
+ Narrative constraint (story arc → conflict-resolution)
    ↓
+ Semiotics constraint (cultural meaning of colors)
    ↓
Optimal Output for Context (95/100)
```

Each constraint narrows the solution space. A narrower solution space means fewer generic choices and more context-specific ones.

## The Three Roles of the 10 Disciplines

### 1. Anti-Mean-Collapse

Without constraints, the LLM collapses to the statistical average. Each discipline pushes against this:

- **Economics** sets the motivational tone (risk-averse → conservative palette, gain-seeking → vibrant)
- **Statistics** demands source verification and confidence labeling
- **Ethics** forces attribution and balanced presentation
- **Semiotics** flags cultural meaning conflicts

### 2. Tacit Knowledge Externalization

What a human does by intuition, the framework makes explicit:

| Human Intuition | Framework Equivalent |
|----------------|---------------------|
| "This blue feels too corporate" | Color derivation via hue wheel + saturation control + product comparison |
| "The layout feels crowded" | Cognitive load theory → max 10 comparison rows |
| "This report lacks professional rigor" | Minto Pyramid Principle → Conclusion-first + MECE grouping |
| "This doesn't feel fresh" | Real-product calibration (Stripe/Notion/Linear color audit) |

### 3. Metacognitive Monitoring

The most critical difference: **the agent stops and questions itself at each step.**

- "Do I have enough data for this claim?"
- "If I remove the data from this statement, does it still hold?" → Novelty Check
- "Would this conclusion change anyone's decision?" → Actionability Check
- "Does my color scheme look dated next to Stripe?" → Calibration Check

Each is not a more complex rule — it's a self-awareness node: **assess current state, decide whether to switch paths** (downgrade comparison type, fall back, trigger root cause analysis).

This mirrors what humans do when they pause mid-work and think, "Something feels off, let me reconsider."

## Design Philosophy (6 Tenets)

```
① Information serves decisions (no decoration, recommendation column pops out)
② Hierarchy before style (CSS order: sticky → highlight → normal → legend)
③ Audience determines density (urgent → compact, relaxed → generous spacing)
④ Consistency builds trust (differences only where meaningful, unified padding)
⑤ Every number has a home (every CSS value has a traceable reason)
⑥ Known→Unknown (new audience = known audience style + hue shift + radius tweak)
```

## What This Framework Is NOT

- **Not a template library** — We don't ask "which template fits?" We ask "what does this context demand?"
- **Not an HTML generator** — HTML is just the delivery format. The framework applies to any output medium.
- **Not rules to memorize** — The disciplines are reasoning heuristics, not coding standards.
- **Not a substitute for human designers** — It's a scaffold for AI agents that lack designer intuition.

## What This Framework IS

- A **reasoning engine** that produces context-optimal design decisions
- A **quality assurance system** with explicit gates (Novelty, Actionability, Stakeholder checks)
- A **knowledge externalization** of design tacit knowledge into AI-executable steps
- A **self-improving system** — every failure is logged, root-cause analyzed in batches of 20

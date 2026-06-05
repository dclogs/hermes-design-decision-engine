# Contributing to Hermes Design Decision Engine

Thanks for considering contributing. This project is explicitly open for improvement — the framework was built from production experience and we know it has gaps in every discipline.

---

## What Needs Contribution

### High-Impact Areas (Pick One)

| Area | What | Skill Needed | Effort |
|------|------|-------------|--------|
| **Discipline expansion** | Add a new discipline (e.g., Law, Political Science, Geography) | Deep knowledge of the discipline's design implications | Medium |
| **Reference content** | Add design tokens for new audience types (e.g., healthcare, manufacturing) | Domain knowledge + design awareness | Medium |
| **Color calibration** | Add more reference products to the calibration set | Design taste + product knowledge | Low |
| **Translation** | Translate methodology to other languages (Japanese, Korean, German) | Bilingual | Medium |
| **Example outputs** | Submit real outputs generated using this framework | Used the framework in production | Low |
| **Fallback paths** | Improve fallback mode for edge cases | Experience with the framework | Medium |
| **Output tracker analysis** | Help analyze failure patterns from output-tracker.md | Analytical | Medium |
| **Bug fixes** | Fix errors in reference files, broken links, typos | Attention to detail | Low |
| **CSS/SVG improvements** | Make the HTML output more accessible, flexible, or performant | CSS | Low |

### Ground Rules

1. **No templates.** This framework is a reasoning engine, not a template collection. Contributions that add "another theme" without reasoning methodology will be rejected.
2. **No unverified data.** Every claim needs a source. Unattributed "industry insight" will be flagged.
3. **No reduction in gates.** Quality gates exist for a reason. If you find a gate too strict, explain why with real examples.
4. **Maintain the 10-discipline structure.** If you add an 11th discipline, it must be distinct from (not overlapping with) the existing 10.

---

## How to Contribute

### Small Fixes (typos, links, docs)

Open a PR directly. No issue needed. Prefix with `[fix]`.

### New Content (reference files, examples)

1. Open an issue first with the outline
2. Get feedback on structure
3. Submit PR

### Adding a New Discipline

This is the highest-impact contribution. Before coding:

1. Open an issue titled `[discipline] <Name>`
2. Answer these questions:
   - What constraint does this discipline impose?
   - Which step in the workflow does it affect?
   - How does it complement or conflict with existing disciplines?
   - Give 3 real examples where this discipline would have improved output
3. Wait for discussion before writing
4. Update all affected files: disciplines doc, workflow, quality gates, glossary

### Translation

1. Translate `methodology/` files (start with `01-core-philosophy.md`)
2. Save in `translations/<language-code>/` (e.g., `translations/ja/01-core-philosophy.md`)
3. Add a note in the top-level README

---

## PR Workflow

```
1. Fork the repo
2. Create a branch: git checkout -b feat/my-change
3. Make changes
4. Test: if you changed methodology, does the workflow still make sense?
   If you changed the Hermes skill, does it load without errors?
5. npm run lint (if applicable) and fix issues
6. Commit: Conventional Commits (feat:, fix:, docs:, refactor:)
7. Push and open PR
8. PR title = one-line summary of what changed and why
```

### PR Checklist

```
☐ Clear description of what changed and why
☐ If fixing a specific issue, reference it (Fixes #12)
☐ If adding content, does it pass its own novelty check?
☐ If changing workflow, are existing quality gates preserved?
☐ If adding references, are sources attributed?
```

---

## Code of Conduct

- Be specific, not vague. "This blue doesn't feel right" → "This blue has 80% saturation which conflicts with the recommended 40% for risk-averse contexts."
- Disagree with evidence. "I think this is wrong because..." + data/citation.
- No gatekeeping. Beginner design decisions are valid contributions — they represent real failure modes.

---

## Communication

- Issues for proposals and bugs
- Discussions for "how would this framework handle X?" questions
- PRs for concrete changes

---

## How the Framework Self-Improves

Every production failure is logged. After 20 failures, root cause analysis separates process issues (fix in workflow) from domain knowledge gaps (fix in references). This is the same mechanism we use internally — contributions that reduce failure rates are especially valued.

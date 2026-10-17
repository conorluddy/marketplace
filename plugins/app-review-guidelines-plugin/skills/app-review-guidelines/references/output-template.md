# REVIEW-RISK.md template

Write to the repo root. Keep it scannable; omit empty sections.

```markdown
# App Review Risk Report

- **App:** <name> (<bundle id>)
- **Audited:** <date> · **Targets:** <app + extensions scanned>
- **Guidelines checked against:** <"bundled snapshot dated YYYY-MM-DD" or "live page, last updated <date shown>">
- **Categories detected:** <IAP · Accounts/social · Sensitive data · Generic>

> Advisory only. App Review is partly subjective; these are risks worth a look, not predictions.

## Summary
<2–4 sentences: biggest themes and what to look at first.>

## Risks
Ordered by likelihood × impact.

### 1. <Short title> — Guideline <n.n.n>
- **Basis:** detected in code | needs human judgement
- **Where:** `path/File.swift:42` (omit for judgement items)
- **Why a reviewer may flag it:** <one or two sentences>
- **Suggested change:** <smallest fix; note if it needs a new binary or only metadata/review notes>

### 2. …

## Needs human judgement
Items the code can't answer (content, business model, metadata). One line each with the guideline.

## Checked, nothing found
<One line listing the areas scanned that came back clean.>

## Next steps
- [ ] Turn top risks into issues
- [ ] Run the pre-submission checklist
- [ ] Re-verify borderline rules against the live guidelines
```

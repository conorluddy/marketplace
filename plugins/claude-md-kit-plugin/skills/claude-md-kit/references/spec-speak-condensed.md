## Requirements & Spec Writing

Whenever you write or edit a spec, PRD, requirements doc, or acceptance criteria in this project, use spec-speak: narrative prose where you're reasoning, EARS/RFC-2119 rigor where you're defining system behaviour.

- Keep problem statement, context, and rationale as narrative prose — hedging welcome ("we believe", "this may"). Write requirements, acceptance criteria, and constraints to full strictness — every statement testable.
- Shape every requirement as EARS: Ubiquitous (`The <system> MUST <response>`), Event (`When <trigger>, the <system> MUST <response>`), State (`While <state>, the <system> MUST <response>`), Unwanted behaviour (`If <failure>, then the <system> MUST <response>`), or Optional (`Where <feature is present>, the <system> MUST <response>`).
- Use exactly one capitalized modal keyword per requirement — MUST / MUST NOT / SHOULD / SHOULD NOT / MAY (RFC 2119). Lowercase "must/should" elsewhere is ordinary prose. Never write "shall".
- Write one thought per requirement — don't join separate obligations with and/or/unless/but; split them. Use active voice with a named actor ("The scheduler MUST retry…"); never open with a pronoun ("It must…").
- Quantify every claim — replace "fast/reliable/scalable" with a number, unit, and tolerance. Avoid unbounded absolutes ("never", "100%", "all") unless genuinely testable. Avoid "eventually/soon/timely" — give a deadline or interval instead.
- Ban weak words from requirements: adequate, appropriate, sufficient, robust, seamless, user-friendly, as appropriate, as required, where possible, etc., and so on.
- Attach one Given/When/Then acceptance criterion per requirement. If you can't write the Then-clause, treat the requirement as not yet verifiable and fix it before moving on.
- Ask, don't invent. Surface product decisions (scope, gating, behaviour under conflict) as an Open Question or a batched question to the author — never guess them. Default engineering parameters (timeouts, retry counts, retention windows) to a sensible value, but flag it inline as `[ASSUMPTION — confirm]`.

For the full rule set with pedigrees, worked examples, and an audit workflow, use the `spec-speak` skill.

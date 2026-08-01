# A Citable Rule Set for PRDs and Technical Specs: Consolidating Documentation & Requirements Standards into a Claude Code Skill

## TL;DR
- **The strongest, most directly citable backbone for your skill is the INCOSE Guide to Writing Requirements v4 (INCOSE-TP-2010-006-04, June 2023, 42 rules) plus EARS (Mavin et al., Rolls-Royce, RE'09) plus ISO/IEC/IEEE 29148:2018** — these three carry most of the requirement-syntax and testability load, while ASD-STE100 Issue 9 (Jan 2025), ISO 24495-1:2023, and the Google/Microsoft style guides supply the sentence-mechanics and structure tiers. Your preliminary three-tier structure is sound and well-grounded; the main corrections are that INCOSE GtWR (not STE) is the richest single rule source, and that STE's rules must be quarantined to requirement/procedure zones and never applied to PRD narrative.
- **Apply rules by document zone, not uniformly.** Requirement and acceptance-criteria sections get the strict tier (EARS syntax, RFC 2119 keywords, INCOSE weak-word bans, one-thought-per-statement); the narrative/problem/context sections get only the plain-language tier and must be allowed to hedge ("may", "could", "we believe"), because a PRD legitimately expresses uncertainty and argument.
- **About half the rules are mechanically checkable (regex/Vale-style):** weak-word blacklists, capitalized-keyword counting, sentence length, noun-stacks, absolutes, "not"/"etc."/oblique-slash bans. The rest — singularity, verifiability, necessity, solution-freeness, and "is this ambiguity actually an undecided product question?" — need LLM judgment. Build the skill as two layers accordingly.

## Key Findings

1. **INCOSE GtWR v4 is the single richest cherry-pickable source** — 42 numbered rules (R1–R42) in 14 categories, mapped to 15 well-formedness characteristics. It is freely summarized in an official INCOSE summary sheet whose copyright terms *permit reproduction with attribution*; the full guide is a paid product (available in the INCOSE store for €25 as a PDF, free to INCOSE members). This is the cleanest licensing situation of any requirements source for your purpose.

2. **EARS gives you the five sentence templates** (ubiquitous, event-driven "When", state-driven "While", unwanted "If…then", optional "Where", plus complex combinations). It is lightweight, needs no tooling, is empirically validated (Rolls-Royce airworthiness case study, RE'09), and maps directly to INCOSE R1 (Structured Statements). Per Mavin's official guide, adopters include "blue chip companies such as Airbus, Bosch, Dyson, Honeywell, Intel, NASA, Rolls-Royce and Siemens."

3. **ISO/IEC/IEEE 29148:2018 supplies the authority for two things**: the 9 characteristics of a single well-formed requirement (necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, conforming) and the "requirements smells" weak-word taxonomy (superlatives, comparatives, subjective language, loopholes/escape clauses, ambiguous adverbs/adjectives, negative statements, vague pronouns, open-ended non-verifiable terms, incomplete references).

4. **RFC 2119 + RFC 8174 (together BCP 14)** define MUST/SHOULD/MAY and the critical clarification that the keywords carry normative force **only when in all-caps**. This is a mechanical, high-value rule.

5. **ASD-STE100 (Issue 9, 15 Jan 2025, 53 rules + ~900-word dictionary) is real and useful but must be handled carefully.** Its sentence-mechanics rules transfer well to requirement/procedure zones; its dictionary is copyright-locked (cannot be redistributed); and its de-facto ban on hedging/speculation actively harms PRD narrative prose.

6. **Empirical backing exists and is strong enough to cite, if reported honestly**: the "cost of a requirements defect rises ~10–1500× by phase" figures trace to Boehm (1981) and a NASA/INCOSE study; the headline "1:10:100" is a downstream simplification and the underlying evidence has been criticised. Still directionally solid and defensible.

## Details

### Tier 0 — Governing principle: apply rules by document zone
A PRD/spec is not one genre. Split every document into two zones and apply different tiers:
- **Normative zones** (functional requirements, non-functional requirements, acceptance criteria, API/interface contracts): full strictness — EARS + RFC 2119 + INCOSE R1–R42 + STE sentence mechanics.
- **Argumentative/exploratory zones** (problem statement, background/context, goals & non-goals, rationale, open questions, alternatives considered, appetite/scope): plain-language tier only. **Hedging and uncertainty are permitted and desirable here** ("we believe", "this may", "the risk is", "TBD/open question"). Applying STE's no-speculation stance here would strip out exactly the calibrated uncertainty a PRD needs.

This zone split is the single most important design decision for the skill.

---

### Standard-by-standard survey

**ASD-STE100 Simplified Technical English — Issue 9 (15 January 2025)**
- Origin: developed from the late 1970s by AECMA at the request of European airlines for aircraft-maintenance manuals readable by non-native English speakers; renamed ASD-STE100 in 2004; became an international "Standard for Technical Documentation" with Issue 9. Maintained by the STEMG working group of ASD. Free to download since Issue 6 (2013); the next issue (10) is scheduled for January 2028.
- Structure: **53 writing rules in 9 sections** (Part 1) + a controlled dictionary of approximately 900 approved words (Part 2). In Issue 9, per *tcworld* magazine, "no new rules have been introduced, [but] 31 of the 53 existing rules have been refined for improved clarity" and "the dictionary has undergone substantial revisions, with 555 entries updated."
- Rules worth taking (for normative/procedural zones only):
  - **Short sentences: max 20 words in procedures, max 25 words in descriptive text.** One topic per paragraph; **no more than 6 sentences per paragraph.** (These numeric caps are confirmed across STE training sources; procedural rules sit in Section 5, descriptive in Section 6.)
  - **Use approved words only, as the single part of speech and single meaning given** (one-word-one-meaning discipline). This is the pedigree for your project-lexicon rule.
  - **Active voice** (in procedures always; in descriptive text passive only when the agent is unknown).
  - **Do not omit words** — keep articles "a/an/the" and demonstratives (Issue 9 Rule 4.5). This is the pedigree for your "no ellipsis/omitted words" rule.
  - **No multi-word noun clusters longer than three words** (Section 2). Pedigree for your "no noun stacks (3+)" rule.
  - **One instruction per sentence** (procedural writing). Restrict the "-ing" form to technical nouns/modifiers; use only simple verb tenses and imperative.
- **Licensing constraint (critical):** the dictionary — per asd-ste100.org, "approximately 900 words, each with one meaning and one part of speech" plus "a list of words that are not approved (approximately 1200) with related alternative suggestions" — is copyrighted by ASD and protected by EU Trade Mark 017966390; **it cannot be reproduced.** The skill must encode STE *principles* (plainest word, used consistently) and cite the free official standard for authoritative word rulings — it must NOT ship the word list. Existing STE Claude skills (nuelcyoung/asd-ste100, danyuchn/asd-ste100-skill) take exactly this approach and explicitly state no tool can guarantee STE compliance.
- **Does-not-transfer warning:** STE permits only the modals *can/will/must* and bans *may/might/could/would/should* as hedges; it is "deliberately flat and literal" and "was never meant to become a general writing standard." Do NOT apply STE to PRD narrative.

**EARS — Easy Approach to Requirements Syntax (Mavin, Wilkinson, Harwood, Novak; Rolls-Royce; RE'09, 2009)**
- General structure: `While <precondition(s)>, When <trigger>, the <system name> shall <system response>`. The ruleset: zero-or-many preconditions, zero-or-one trigger, exactly one system name, one-or-many responses; clauses always in the same temporal order.
- Five templates: **Ubiquitous** (no keyword — always active), **State-driven** ("While"), **Event-driven** ("When"), **Unwanted behaviour** ("If…then"), **Optional feature** ("Where"), plus **Complex** combinations.
- Adoption/validation: developed while analysing jet-engine airworthiness regulations; the RE'09 case study reported qualitative and quantitative improvements vs. conventional textual specs. There is an active feature request (GitHub Issue #1356, "Feature Request: EARS (Easy Approach to Requirements Syntax) Integration") to build EARS into GitHub's spec-kit for AI-assisted development — direct evidence of EARS's fit for AI-authored specs.
- Extensions: **Adv-EARS** (Majumdar et al., 2011) adds a formal context-free grammar so requirements can be parsed into use-case/actor models. It is more formal and aimed at auto-deriving UML — likely too heavy for your skill, but worth a mention.
- Known limits (report honestly): EARS is poorly suited to requirements with more than three preconditions (unwieldy sentences), and to non-functional/architectural constraints not expressible as conditional behaviour; some requirements are better as decision tables, formulae, or state diagrams.

**ISO/IEC/IEEE 29148:2018 (Requirements Engineering)**
- Supersedes and absorbs IEEE 830-1998, IEEE 1233, IEEE 1362. Defines the construct of a well-formed textual requirement.
- **9 characteristics of an individual requirement:** necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, conforming. (INCOSE extends this to 15 by adding set-level characteristics.)
- **Weak-word / "requirements smells" taxonomy** (widely cited, and the basis for NLP tools): superlatives, comparative phrases, subjective language ("user-friendly", "easy to use", "cost-effective"), loopholes/escape clauses ("as appropriate", "if necessary"), ambiguous adverbs & adjectives, open-ended non-verifiable terms ("but not limited to", "as a minimum"), negative statements, vague pronouns, incomplete references, and (in the standard's guidance) passive voice.

**RFC 2119 (Bradner, 1997) + RFC 8174 (Leiba, 2017), together BCP 14**
- Keywords: MUST / MUST NOT / REQUIRED / SHALL / SHALL NOT / SHOULD / SHOULD NOT / RECOMMENDED / NOT RECOMMENDED / MAY / OPTIONAL.
- RFC 8174's clarification: the keywords carry their defined meanings **only when in all-capitals**; lowercase "must/should" have ordinary English meaning. This makes "exactly one capitalized keyword per requirement" both a mechanically checkable rule and a licence to write ordinary prose elsewhere.

**INCOSE Guide to Writing Requirements v4 (INCOSE-TP-2010-006-04, June 2023) — the 42 rules**
Grouped in 14 categories:
- *Accuracy (R1–R9):* R1 Structured Statements (conform to a pattern — where EARS plugs in); R2 Active Voice with named responsible entity; R3 Appropriate Subject-Verb; R4 Defined Terms (glossary/data dictionary); R5 use definite article "the" not "a"; R6 Common Units of Measure; R7 avoid Vague Terms ("some", "several", "adequate", "appropriate", "reasonable", "significant", "flexible", "sufficient", etc. — a long explicit list); R8 avoid Escape Clauses ("so far as possible", "as appropriate", "if necessary", "as required"); R9 avoid Open-Ended Clauses ("including but not limited to", "etc.", "and so on").
- *Concision (R10–R11):* R10 no Superfluous Infinitives ("to be able to", "to be capable of", "to allow"); R11 Separate Clauses for each condition.
- *Non-ambiguity (R12–R17):* R12 grammar, R13 spelling, R14 punctuation; R15 defined convention for Logical Expressions ("[X AND Y]"); R16 **avoid "not"** (write positive verifiable statements); R17 avoid the oblique "/" symbol except in units.
- *Singularity (R18–R23):* R18 Single-Thought Sentence; R19 avoid Combinators ("and", "or", "unless", "but", "however", "whether", "otherwise"); R20 avoid Purpose Phrases ("in order to", "so that" — put in a rationale attribute); R21 avoid Parentheses with subordinate text; R22 Enumerate sets explicitly; R23 refer to a supporting diagram/model/ICD for complex behaviour.
- *Completeness (R24–R25):* R24 **avoid pronouns** ("it", "this", "they" — repeat the noun; this is your dangling-anaphora rule); R25 don't rely on headings for meaning (each requirement self-contained).
- *Realism (R26):* avoid unachievable Absolutes ("100%", "all", "always", "never").
- *Conditions (R27–R28):* R27 state conditions explicitly; R28 make AND vs OR explicit for multiple conditions.
- *Uniqueness (R29–R30):* R29 Classify by type; R30 express each requirement once and only once.
- *Abstraction (R31):* Solution-Free — state "what" not "how" unless there is rationale to constrain design.
- *Quantifiers (R32):* use "each" not "all/any/both" for universal quantification.
- *Tolerance (R33):* define quantities with a range/tolerance.
- *Quantification (R34–R35):* R34 measurable performance targets (replace "fast/reliable/user-friendly"); R35 explicit temporal dependencies (no "eventually", "before", "as", "once").
- *Uniformity (R36–R40):* R36 consistent terms & units; R37 consistent acronyms; R38 avoid abbreviations; R39 project-wide style guide; R40 consistent decimal format.
- *Modularity (R41–R42):* R41 group related requirements; R42 conform to a defined structure/template for the set.
- **Licensing:** the official INCOSE **summary sheet** grants "permission to reproduce and use this summary … with attribution to INCOSE" — so you may cite the rule names and numbers. The full guide is a paid/member product (INCOSE store, €25 PDF; free to members); do not reproduce its example text wholesale.

**ISO 24495-1:2023 Plain Language — Part 1**
- Adopts the International Plain Language Federation definition: communication whose wording, structure and design let intended readers **find what they need, understand what they find, and use it.** Four governing principles commonly rendered as: relevant/reader-focused, findable, understandable, usable. Built by experts from 25 countries; evidence-based. This is the authority for your audience-first / progressive-disclosure / summary-then-detail structure rules. It explicitly applies to technical writing and controlled languages, not just public documents.

**Microsoft Writing Style Guide & Google Developer Documentation Style Guide**
- Both mandate: second person, active voice, present tense, sentence-case headings, the serial (Oxford) comma, short unambiguous sentences, and "don't use the same word to mean different things." Google additionally: put conditions before instructions; use qualifying nouns for code elements ("the example.yaml file"); avoid directional language ("above/below"). These are the practitioner-facing, docs-as-code-friendly restatements of the plain-language tier, and both are free and quotable (Google's guide public since Sept 2017).

**Gherkin / Given-When-Then + user stories + INVEST**
- Gherkin's Given (context) / When (action) / Then (observable outcome) is the natural acceptance-criteria format and pairs cleanly with EARS: EARS for the requirement, Gherkin for its acceptance test. Best practice: describe behaviour not implementation ("Given an unauthenticated user", not "Given I am at /login"). Same weak-word cautions apply ("fast", "user-friendly" are untestable).
- User-story "As a <role>, I want <x>, so that <y>" + INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable) belong in the exploratory zone as the framing device, with Gherkin criteria as the normative attachment.

**Amazon PRFAQ / Working Backwards / six-pager**
- Narrative memos (up to ~6 pages, no slides) because "narratives convey ~10× the information" and force multi-causal reasoning; the PRFAQ (press release + FAQ) is future-looking and forces customer-first clarity. Relevance: this justifies the **narrative/prose** discipline for the exploratory zone and the "write in complete sentences, not bullets, for the problem statement" rule — a useful counterweight to the over-listification that pure STE would push.

**Shape Up (Basecamp / Ryan Singer)**
- The pitch's five ingredients: **Problem, Appetite, Solution, Rabbit holes, No-gos.** Core principle: **fixed time, variable scope** — "appetites start with a number and end with a design; estimates start with a design and end with a number." Two cherry-pickable PRD rules: (1) state an explicit appetite/time-box, and (2) explicitly declare out-of-scope items ("No-gos") — a structural rule that prevents scope ambiguity.

**Diátaxis (Procida)**
- Splits *documentation* into tutorial / how-to / reference / explanation along two axes (action vs. cognition, acquisition vs. application); its core lesson is **don't mix modes on one page.** For PRDs the transferable insight is precisely the zone split above: keep reference-like normative requirements separate from explanation-like rationale. Diátaxis itself targets end-user docs, so borrow the principle, not the four categories.

**arc42 + C4**
- arc42 = a 12-section architecture-doc template (context/scope, constraints, solution strategy, building-block view, runtime view, deployment, crosscutting concepts, decisions, quality requirements, risks/technical debt, glossary). C4 = context/container/component/code diagram hierarchy. Relevance: a proven **section skeleton** for the technical-spec (design-doc) sibling of the PRD; its "quality requirements" + "architecture decisions (ADR)" sections show where non-functional requirements and rationale live.

**Design-doc / RFC culture (Google, Uber, Rust, Oxide RFDs)**
- Google design docs are deliberately informal, written before coding, emphasising trade-offs and decisions. The recurring cultural rule worth encoding: **"Your job as the RFC author is to propose an opinionated solution — ambiguity creates unproductive discussion."** Oxide's RFD ethos: "timely rather than polished." This supports a workflow rule: a spec should take a position, and open questions should be explicitly flagged as open, not left implicit.

**Docs-as-code linting (Vale, textlint, proselint, RedPen)**
- Vale is the de-facto prose linter (used by GitLab, Microsoft, Google, Red Hat, NVIDIA, AWS); it ships ready-made Microsoft and Google style packages and runs offline in CI. Its model — Rules (YAML pattern matches) → Styles (folders) → a `.vale.ini` config — is exactly what the mechanically-checkable subset of your rule set should compile to. Implication: the skill should emit both LLM-checkable guidance AND a Vale-style ruleset for the regex-able rules.

**Controlled natural languages (Kuhn's survey; Attempto ACE)**
- STE and EARS sit at the "naturalistic/lightweight" end of the CNL spectrum; fully formal CNLs like Attempto Controlled English (ACE) are machine-parseable to first-order logic but are too rigid and training-heavy for PRDs. The takeaway: gentle constraint (EARS/STE) is the sweet spot; full formalism is counterproductive for human-authored planning docs.

---

### Empirical "why it matters" backing
- **Cost-of-defect escalation:** Boehm's 1981 dataset (63 projects) found defect-fix cost rises roughly an order of magnitude per phase. The most precise, citable figures come from the NASA/INCOSE study by Haskins et al. ("8.4.2 Error Cost Escalation Through the Project Life Cycle," INCOSE Int'l Symposium 2004 / NASA NTRS 20100036670): *"If the cost of fixing a requirements error discovered during the requirements phase is defined to be 1 unit … at the design phase increases to 3–8 units; at the manufacturing/build phase … 7–16 units; at the integration and test phase … 21–78 units; and at the operations phase … ranged from 29 units to more than 1500 units."* Industry data reported alongside it: *"50% of the product defects and 80% of rework efforts can be traced back to errors during the requirements engineering phase."* **Caveat:** the popular "1:10:100" rule is a downstream simplification (often attributed to the IBM Systems Sciences Institute), and Boehm & Basili's 2001 update noted the slope is flatter for small agile/CI projects — directly relevant to your solo-developer user. Net: direction is real and defensible; exact multipliers are soft.
- **Ambiguity → defects:** the "requirements smells" literature (Femmer et al., "Rapid quality assurance with Requirements Smells") operationalizes ISO 29148 weak words into automatically detectable smells; multiple studies (and deep-learning smell classifiers, e.g. the multi-label Bi-LSTM work in *Scientific Reports* 2025) validate that these lexical patterns predict quality violations.
- **LLM-assisted requirements checking (most relevant to a Claude skill):** recent work shows generic LLMs can evaluate and rewrite requirements, and that **RAG grounding with INCOSE/EARS documents significantly improves results** (MITRE 2025, "Automating SE with AI and NLP," Paper 378; Lubos et al., IEEE RE 2024, "Leveraging LLMs for the Quality Assurance of Software Requirements"; ReqBrain 2025; a 2016 industry paper combining EARS + INCOSE rules with NLP). This is direct evidence that your skill's architecture — ground an LLM in EARS + INCOSE rules — is a validated approach, not speculation.

---

### Conflicts between standards, and which side to take for PRDs
1. **STE "prefer lists/short flat sentences" vs. Amazon "write narrative prose, not bullets."** Resolution: zone-dependent. Lists/tables for enumerable normative content (requirements, criteria, config); narrative prose for problem/rationale. (Kodak ISL and STE favour tables for enumerable content; Amazon favours narrative for reasoning — both are right in their zone.)
2. **STE/INCOSE "ban hedging, no speculation, no 'may/could'" vs. PRD need for calibrated uncertainty.** Resolution: enforce in normative zones only; explicitly permit hedging in exploratory zones. This is the sharpest conflict and the reason a flat STE skill would damage PRDs.
3. **RFC 2119 "MAY/SHOULD as keywords" vs. INCOSE R7/EARS "shall only."** Resolution: pick ONE modal convention per project and state it. Simplest for a solo dev: adopt RFC 2119 keywords wholesale, drop "shall", and require **exactly one capitalized keyword per requirement from a declared set.**
4. **INCOSE R16 "avoid 'not' / negative statements" vs. EARS "If…then" unwanted-behaviour template** (which often describes what must not happen). Resolution: allow negative *conditions* in the trigger clause but require a positive, verifiable *response* clause.
5. **INCOSE R31 "solution-free" vs. technical specs that must specify implementation.** Resolution: solution-free applies to the PRD/requirements; the technical spec/design-doc is explicitly where implementation is chosen. Zone/document-type dependent.
6. **INCOSE R5 "use 'the' not 'a'" and R38 "avoid abbreviations" are calibrated for contractual systems engineering** and can feel heavy for a solo dev — keep as SHOULD-level lints, not hard errors.

---

### Mechanically checkable vs. LLM-judgment rules (drives skill architecture)
**Mechanically checkable (regex / Vale-style — put in a lint layer):**
- Weak-word/smell blacklist (INCOSE R7/R8/R9, ISO 29148 smells): flag "adequate, appropriate, user-friendly, seamless, robust, fast, easy, several, some, etc., including but not limited to, as appropriate, if necessary".
- Absolutes (R26): "100%, always, never, all, every".
- "not" and negative statements (R16); oblique "/" (R17).
- Superfluous infinitives (R10): "be able to, be capable of, designed to".
- Combinators (R19): sentence-level "and/or/unless/but" in a single requirement → singularity flag.
- Pronoun/anaphora check (R24): leading "it/this/that/they".
- Sentence length (STE 20/25-word caps); paragraph ≤6 sentences.
- Noun-cluster length >3 (STE Section 2).
- Modal-keyword check: exactly one capitalized RFC 2119 keyword per requirement; passive-voice heuristic.
- EARS shape check: does each requirement match one of the five templates (keyword + clause order)?
- Units/temporal-vagueness ("eventually, soon, before") flags (R35).
- Terminology consistency against a project glossary (R4/R36).

**Needs LLM judgment (put in the reasoning layer):**
- Singularity in substance (R18/R30): is this really one thought?
- Verifiability/testability: could a tester actually prove this? (Map each requirement to a Gherkin scenario as its test.)
- Necessity & appropriateness (29148 C1/C2), completeness (C4), feasibility (C6), correctness/traceability to a stated need.
- Solution-freeness (R31): is this constraining design without rationale?
- **The Caterpillar-style workflow rule:** when the author writes something ambiguous, decide whether it's a *wording* problem (rewrite) or an *undecided product question* (STOP and ask the author to disambiguate rather than silently inventing a decision). This is inherently LLM-judgment and is arguably the highest-value rule in the whole skill for a solo dev, because PRD ambiguity usually signals an unmade decision.
- Zone classification: decide whether a passage is normative or exploratory, and apply the right tier.

## Recommendations

**Stage 1 — Build the two-layer skill now.**
- Encode a **lint layer** (all mechanically checkable rules above) as a Vale-style ruleset the agent can run or emulate, each rule tagged with its pedigree (e.g., `INCOSE-R7`, `ISO29148-smell`, `STE-S2`, `RFC2119`).
- Encode a **reasoning layer** prompt that: (a) classifies each passage's zone; (b) in normative zones checks EARS shape + the 9 INCOSE/29148 characteristics; (c) attaches a Gherkin acceptance scenario to each requirement to force verifiability; (d) applies the Caterpillar "ask, don't silently rewrite" rule for genuine ambiguity.

**Stage 2 — Ground it (RAG).** Load the INCOSE GtWR summary sheet (reproducible with attribution), the EARS official patterns, RFC 2119/8174, and the ISO 29148 smell list as retrieval context. Evidence (MITRE 2025; IEEE RE 2024) shows this materially improves LLM requirements-QA. Do **not** load the STE dictionary (copyright); load STE *principles* only.

**Stage 3 — Tune thresholds to a solo dev.** Make heavy systems-engineering rules (R5 "the" not "a", R38 abbreviations, R40 decimal format, tolerances R33) SHOULD-level suggestions; make ambiguity/weak-word/singularity/verifiability rules ERROR-level. Because your user is solo with a CI/CD-style flow, cite Boehm-Basili 2001: the cost curve is flatter for you, so optimise for catching genuine ambiguity and undecided decisions, not for contractual formality.

**Benchmarks that would change the recommendation:**
- If the user starts writing safety-critical or regulated software → raise STE and INCOSE rules to ERROR-level and add full traceability attributes (INCOSE A1–A5: rationale, trace-to-parent, trace-to-source, allocation, verification criteria).
- If the docs are consumed mainly by other AI agents rather than humans → tighten STE mechanics further (STE was shown useful precisely for agent-parseable text).
- If false-positive lint noise frustrates the user → demote weak-word rules to warnings and rely more on the LLM layer.

## Caveats
- **Rule-number precision for STE:** the 20-word/25-word caps and section placement (procedural = Section 5, descriptive = Section 6; articles = Rule 4.5) are confirmed, but the exact finer rule numbers (e.g. "Rule 5.1", "Rule 6.4") could not be verified verbatim because the STE rule text is copyrighted. Cite by concept/section, not by fine rule number.
- **Licensing is not uniform:** INCOSE summary sheet = reproducible with attribution; INCOSE full guide = paid/member (€25); STE standard = free to download but reproduction needs ASD written authority and the dictionary is trademark-protected (EU TM 017966390) and must not be shipped; RFCs and the Google/Microsoft guides are freely usable; ISO 24495-1 and ISO 29148 are paywalled (cite the characteristics/smell list via secondary literature, which is legal to summarize).
- **Empirical figures are directional, not exact:** the cost-of-defect multipliers (up to 29–1500× in operations; "50% of defects / 80% of rework") come from Boehm 1981 and the NASA/INCOSE Haskins study and are widely repeated but were criticised (Bossavit, *Leprechauns of Software Engineering*) for weak underlying evidence; present them as "well-supported in direction, contested in magnitude," and note the 2001 Boehm-Basili finding that the slope is flatter for small/agile projects.
- **Some sources are secondary/commercial** (reqi.io, QRA, Visure, Reuse Company) — used to corroborate the INCOSE rule list, but the authoritative source is the INCOSE summary sheet itself, which was verified directly.
- **EARS and STE are not universal:** EARS breaks down beyond ~3 preconditions and for non-behavioural NFRs; STE damages argumentative prose. The zone split mitigates both, but the skill should tell the author when a requirement is better expressed as a table, state diagram, or decision table rather than forced into a template.
- **This report did not independently verify the full text of ISO 29148:2018 or the Microsoft Writing Style Guide** (both partly paywalled); their contents are drawn from official previews, the standards' own abstracts, and well-corroborated secondary literature.

---

### Appendix — Consolidated, deduplicated, tiered rule set (each rule tagged with pedigree)

**Tier A — Sentence mechanics** (apply in normative zones; soft-apply in exploratory zones)
- A1. Cap sentence length: ≤20 words for instructions, ≤25 for descriptive text `[STE §5/§6]`
- A2. One idea per sentence `[STE; INCOSE-R18]`
- A3. Active voice with a named actor as subject `[INCOSE-R2; Google/Microsoft; STE §3]`
- A4. No noun stacks of >3 nouns `[STE §2]`
- A5. No dangling anaphora — repeat the noun, avoid leading "it/this/that/they" `[INCOSE-R24]`
- A6. No nominalizations / superfluous infinitives ("perform validation of" → "validate") `[INCOSE-R10]`
- A7. Don't omit words; keep articles and demonstratives `[STE Rule 4.5]`
- A8. Present tense, second person, sentence-case headings, serial comma `[Google/Microsoft]`

**Tier B — Requirement syntax** (normative zones only)
- B1. Each requirement conforms to one EARS template (Ubiquitous/While/When/If-then/Where) `[EARS; INCOSE-R1]`
- B2. Exactly one capitalized RFC 2119 keyword per requirement `[RFC 2119/8174]`
- B3. No combinators joining clauses in one requirement `[INCOSE-R19]`
- B4. Explicit conditions; explicit AND/OR `[INCOSE-R27/R28]`
- B5. No purpose phrases in the statement (move to rationale) `[INCOSE-R20]`
- B6. Avoid "not"/negatives; write positive statements `[INCOSE-R16]`

**Tier C — Testability / verifiability** (normative zones only)
- C1. Ban weak/vague/subjective words and escape/open-ended clauses `[INCOSE-R7/R8/R9; ISO 29148 smells]`
- C2. Ban unachievable absolutes; use bounded targets `[INCOSE-R26]`
- C3. Measurable performance targets + explicit units + tolerances `[INCOSE-R6/R33/R34]`
- C4. Explicit temporal dependencies (no "eventually/soon/before") `[INCOSE-R35]`
- C5. Attach a Given-When-Then acceptance scenario to each requirement `[Gherkin/BDD]`
- C6. Each requirement is verifiable, singular, complete, necessary `[ISO 29148 C1–C9]`

**Tier D — Document structure**
- D1. Audience-first; summary→detail progressive disclosure `[ISO 24495-1]`
- D2. Don't mix modes; separate normative requirements from rationale `[Diátaxis]`
- D3. Tables/lists for enumerable content; narrative prose for problem/rationale `[Kodak ISL; Amazon PRFAQ]`
- D4. Explicit Problem, Appetite, Solution, Rabbit-holes, No-gos `[Shape Up]`
- D5. For specs, use an arc42-style section skeleton + ADRs for decisions `[arc42/C4]`
- D6. Take an opinionated position; flag open questions explicitly `[Google/Oxide design-doc culture]`

**Tier E — Terminology / lexicon discipline**
- E1. One word, one meaning; one part of speech `[STE; INCOSE-R36]`
- E2. Define all terms in a project glossary/data dictionary `[INCOSE-R4]`
- E3. Consistent acronyms; avoid abbreviations `[INCOSE-R37/R38]`

**Tier F — Workflow / process**
- F1. On genuine ambiguity, ask the author to disambiguate rather than silently rewriting — because PRD ambiguity often reflects an undecided product question `[Caterpillar-inspired]`
- F2. Classify each passage's zone (normative vs. exploratory) before applying tiers `[this report]`
- F3. Compile mechanically-checkable rules into a Vale-style ruleset; reserve judgment rules for the LLM layer `[Vale/docs-as-code]`
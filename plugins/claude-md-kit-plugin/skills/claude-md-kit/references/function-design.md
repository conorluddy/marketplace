## Function Design

Design every function to these constraints:

- Single responsibility — describable in one sentence.
- Pass all dependencies as parameters; no hidden global state.
- Type everything — strict mode, no `any`.
- Use guard clauses over nesting — handle edge cases first, keep the happy path unindented.
- Treat 50 lines as a refactoring trigger, not a hard limit.
- Write functions as self-contained context units — comprehensible without reading other files.

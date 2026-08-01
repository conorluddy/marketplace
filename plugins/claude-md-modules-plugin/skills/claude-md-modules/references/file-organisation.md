## File & Module Organisation

- Group by feature/domain, not file type — `authentication/`, `orders/`, `payments/`.
- Put the public API first, helpers at the bottom. One major export per file.
- Co-locate tests next to source — `UserService.test.ts` beside `UserService.ts`.
- Treat 300 lines per file as a refactoring trigger, not a hard limit.
- Minimize cross-module dependencies — keep each module a clean context boundary.
- Use section comments (`// === PUBLIC API ===`) to create visual hierarchy in larger files.

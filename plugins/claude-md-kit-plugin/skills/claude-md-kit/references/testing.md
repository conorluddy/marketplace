## Testing

- Favor the testing trophy — mostly integration tests. Static analysis → unit → integration (widest) → E2E (critical journeys only).
- Test behaviour, not implementation. One concept per test.
- Name tests to describe the scenario — `test('user can add items to cart')`.
- Target 80% coverage minimum, focused on critical paths, not as an end in itself.

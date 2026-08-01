## Observability

- Log with structured JSON only — include `request_id`, `user_id`, `duration_ms`, and relevant entity IDs.
- Log at critical boundaries: external API calls, database operations, auth decisions, errors.
- Emit one structured event per operation and derive metrics, logs, and traces from that same data — don't hand-roll separate metrics.

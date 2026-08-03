# Services standard

Services coordinate a cohesive use case or integration. They are not a dumping ground for unrelated helpers or a second domain model.

- Give each service one clear responsibility and a verb-based action name where it performs a use case.
- Inject contracts and collaborators; keep framework adapters at the boundary.
- Authorize before protected reads/mutations, establish tenant context, and make transaction scope explicit.
- Return typed results or purpose-built read models; surface expected failures as documented domain/application errors.
- Keep external calls behind provider-neutral adapters with timeouts, retries, rate limits, reconciliation, and audit evidence.

See [CONTRACTS.md](CONTRACTS.md), [CLASSES.md](CLASSES.md), and [Domain-driven design patterns](DOMAIN-DRIVEN-DESIGN-PATTERNS.md).

## Delivery checklist

Name the use case, owner, authorization point, transaction boundary, collaborators, expected failures, and observable result. Keep services composable and testable, avoid god services and hidden queries, and separate provider calls behind contracts with timeout, retry, reconciliation, and audit behavior.

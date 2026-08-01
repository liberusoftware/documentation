# Liberu Testing Standard

## Canonical PHPUnit, Pest, and Coverage Specification

**Applies to:** Laravel applications, modules, themes, APIs, connectors, Composer packages, and distributions
**Related standards:** [MODULES.md](MODULES.md) · [THEMES.md](THEMES.md) · [API.md](API.md) · [BOILERPLATE.md](BOILERPLATE.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [REPOSITORIES.md](REPOSITORIES.md)

## 1. Purpose

Liberu tests provide fast, repeatable evidence that each independently released package works in isolation and that selected packages work together in their host applications. Tests protect user outcomes, business invariants, security boundaries, public contracts, upgrades, failure recovery, and compatibility.

PHPUnit is the underlying test runner and assertion ecosystem. Pest is the preferred concise authoring layer for new tests where it improves readability. Either style is acceptable within a repository when it follows the same suites, isolation rules, and quality requirements. Coverage measures executed code; it does not replace meaningful assertions or risk-based test design.

## 2. Testing principles

1. **Test observable behavior:** assert outcomes and public contracts, not private method arrangement.
2. **Put evidence with its owner:** module behavior is tested in the module; cross-module composition is tested in the application.
3. **Protect boundaries:** test authorization, tenancy, data ownership, package dependencies, API schemas, and provider isolation explicitly.
4. **Keep tests deterministic:** control time, randomness, queues, storage, networks, and provider responses.
5. **Cover failure paths:** duplicates, retries, races, partial completion, denial, timeouts, invalid state, and recovery are first-class scenarios.
6. **Use the smallest useful test:** prefer a unit test for pure behavior and a feature or integration test only when infrastructure is relevant.
7. **Share contracts, not implementation tests:** every interchangeable adapter runs the same contract suite.
8. **Test supported reality:** CI verifies declared minimum/latest dependency combinations and clean installation in representative hosts.
9. **Keep production safe:** tests never contact production services, use live credentials, or mix test and production destinations.
10. **Treat flaky tests as defects:** fix or quarantine with an owner and expiry; never normalize blind reruns.

## 3. Tooling policy

- Use a Composer-managed version of PHPUnit compatible with the repository's Laravel and PHP constraints.
- Pest repositories install compatible `pestphp/pest` and Laravel/plugin packages; Pest still runs on PHPUnit.
- Use Laravel testing helpers and Orchestra Testbench for independently tested Laravel packages where appropriate.
- Use architecture tooling, static analysis, mutation testing, browser tooling, accessibility tooling, and visual regression only where each supplies evidence not covered by ordinary tests.
- Keep `phpunit.xml` or `phpunit.xml.dist`, Pest configuration, bootstrap files, and Composer scripts versioned.
- Never depend on developer-global binaries or configuration.

Do not rewrite a stable PHPUnit suite into Pest solely for syntax consistency. New tests may use Pest alongside PHPUnit unless mixed styles materially harm repository clarity.

## 4. Standard repository layout

```text
tests/
├── Unit/
├── Feature/
├── Contract/
├── Integration/
├── Architecture/
├── Compatibility/
├── Migration/
├── Security/
├── Performance/
├── Fixtures/
├── Fakes/
├── TestCase.php
└── Pest.php
```

Create only suites the repository needs. Test namespaces and paths must be discoverable through Composer and the configured runner. Reusable contract suites may live in a dedicated testing package when multiple independent repositories consume them.

## 5. Test types and ownership

| Test type | Proves | Primary owner |
|---|---|---|
| Unit | Pure rules, value objects, calculations, specifications, and state transitions | Owning package |
| Feature | Laravel actions, validation, policies, persistence, jobs, events, commands, and HTTP/Livewire behavior | Owning package/application |
| Contract | Every implementation satisfies the same provider-neutral behavior | Contract/core package; run by adapters |
| Integration | Real boundaries between selected packages or controlled infrastructure | Adapter or host application |
| Composition/end-to-end | A complete user workflow works across installed modules and presentation | Host application |
| Architecture | Forbidden dependencies, namespaces, SDK leakage, and private data access cannot occur | Every package/application |
| Migration/upgrade | Fresh install, supported upgrade, rollback policy, and data transformation work | Package owning migrations |
| Compatibility | Declared framework, package, database, provider, and host combinations work | Independent repository and host CI |
| Security | Authentication, authorization, isolation, abuse, secrets, and threat-model controls hold | Owning package plus application |
| Performance | Critical budgets and abusive patterns remain within explicit thresholds | Relevant package/application |
| Visual/accessibility | Theme and interactive UI remain usable and visually intentional | Theme/presentation package and host |

Distribution packages test dependency resolution and installation. They do not duplicate implementation suites owned by their dependencies.

## 6. PHPUnit and Pest examples

Use names that describe the rule and expected outcome.

PHPUnit example:

```php
<?php

use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;

final class MoneyTest extends TestCase
{
    #[Test]
    public function it_rejects_addition_of_different_currencies(): void
    {
        $this->expectException(CurrencyMismatch::class);

        Money::gbp(100)->add(Money::usd(100));
    }
}
```

Equivalent Pest example:

```php
<?php

it('rejects addition of different currencies', function (): void {
    Money::gbp(100)->add(Money::usd(100));
})->throws(CurrencyMismatch::class);
```

Tests should follow arrange–act–assert conceptually, even when concise syntax makes the phases implicit. Assert relevant state, emitted events, side effects, and absence of forbidden effects; avoid assertion-free “does not crash” tests unless survival itself is the documented contract.

## 7. Isolation and test data

- Use factories/builders that express valid domain states; named factory states communicate important variations.
- Keep fixtures minimal, synthetic, versioned, and free of production or personal data.
- Use database transactions or refresh strategies appropriate to the database behavior under test.
- Freeze time and seed randomness when outcomes depend on them.
- Fake queues, events, notifications, mail, storage, and HTTP only when the boundary is not the subject of the test.
- Use deterministic provider fakes for normal product tests and recorded/sandbox tests only in a separately controlled suite.
- Give every test its own tenant, organization, identifiers, files, and connector state unless shared state is the explicit subject.
- Parallel-safe tests must not rely on fixed ports, global files, shared cache keys, or ordering.

Mock public boundaries sparingly. Prefer real value objects and domain actions. Do not mock the class under test or assert a sequence of private calls that prevents safe refactoring.

## 8. Laravel application and module tests

Every module implements the evidence required by [MODULES.md](MODULES.md):

- unit tests for domain rules and value objects;
- feature tests for actions, policies, validation, persistence, tenant isolation, events, jobs, and commands;
- shared contract tests for public implementations;
- event and API schema compatibility tests;
- architecture tests blocking `App\` coupling, domain-to-presentation dependencies, provider SDK leakage, and cross-module private-table access;
- migration and upgrade tests from every supported release path;
- failure tests covering retries, duplicates, concurrency, partial workflows, denial, and provider failure;
- a clean independent-install test in a minimal compatible Laravel application.

The root application tests package discovery, configuration, panel and theme composition, routes, permissions, selected adapters, and representative cross-module workflows. Its tests must not become the only evidence for reusable module behavior.

## 9. API, webhook, and connector tests

API testing follows [API.md](API.md) and includes:

- OpenAPI/schema linting, example validation, implementation drift, and breaking-change detection;
- authentication, scopes, permissions, field visibility, tenancy, validation, rate limits, and enumeration resistance;
- stable responses and Problem Details errors for allowed, denied, invalid, missing, stale, duplicate, and conflicting requests;
- pagination, filtering, sorting, sparse fields, includes, dates, money, identifiers, and enum compatibility;
- idempotency, optimistic concurrency, async operations, bulk partial failure, and retry behavior;
- webhook signatures, timestamp/replay protection, rotation overlap, duplicates, ordering, retries, replay, and disabling failed destinations;
- connector mapping, credentials, cursors, backfill, rate limits, timeouts, circuit breaking, sandbox mode, provider drift, and reconciliation;
- generated SDK compile and smoke tests against the released specification;
- representative load and security tests for high-risk or expensive operations.

Contract tests use provider-neutral fixtures and expectations. Adapter-specific tests cover only provider mapping and behavior. Normal CI must not require an external provider; scheduled or release-gated sandbox tests use protected test credentials and non-production destinations.

## 10. Theme and interface tests

Theme and presentation evidence follows [THEMES.md](THEMES.md):

- render tests for layouts, Blade components, extension points, slots, and safe fallbacks;
- Livewire tests for state, validation, authorization, events, loading, and failure behavior;
- browser tests for a small set of critical journeys that cannot be proven below the browser layer;
- automated accessibility checks plus manual keyboard, screen-reader, focus, contrast, zoom, reduced-motion, and responsive checks for primary journeys;
- visual regression at representative viewports, locales, directions, color modes, and supported hosts;
- JavaScript/CSS build, asset existence, CSP compatibility, and performance-budget checks;
- graceful degradation with optional modules absent and compatibility with at least one declared non-optimized host where practical.

Line coverage is required for meaningful PHP and Livewire behavior. Static CSS, imagery, and templates may use render, accessibility, visual, build, and performance evidence instead of misleading line-coverage targets.

## 11. Security and tenant isolation

For each protected operation, test the permitted path and relevant denied paths. Include unauthenticated, wrong tenant/site/team, insufficient role/permission, revoked token/session, hidden field, mass assignment, direct-object reference, and background-job execution where applicable.

High-risk modules derive tests from their threat model. Authentication, payments, files, imports, exports, webhooks, automation, impersonation, infrastructure actions, and marketplace apps require abuse and failure tests proportionate to their impact.

Tests verify that secrets and sensitive data do not leak through responses, logs, exceptions, events, snapshots, exports, metrics, or test artifacts.

## 12. Migrations and compatibility

- Test an empty-database installation and migrations against each supported database family.
- Test upgrades from the oldest supported release and important intermediate schemas using representative data.
- Verify indexes, constraints, defaults, backfills, resumability, locks/downtime expectations, and rollback policy.
- Never depend on migration timestamps or execution order from another independent package unless an explicit dependency contract guarantees it.
- Run a CI matrix covering declared minimum and current supported PHP/Laravel versions and relevant Filament, Livewire, database, package, provider, and host combinations.
- Use Composer lowest-dependency testing where supported and meaningful; keep the lockfile path representative of production installation.

Compatibility claims in manifests and documentation must be generated from or verified by the tested matrix.

## 13. Coverage policy

Coverage answers “which executable lines or branches ran?” It does not answer whether assertions are correct, requirements are complete, boundaries are secure, or failures recover safely.

- Generate line coverage and branch/path coverage where the selected driver and toolchain support it reliably.
- Include owned production source and exclude vendor code, generated files, views/cache, bootstrap output, configuration-only files, migrations when not meaningfully executable, and test support code.
- Do not exclude difficult domain code merely to improve the percentage.
- Set repository thresholds from risk and current evidence, then raise them deliberately. New or changed critical behavior must be thoroughly tested even when the global threshold passes.
- Prefer changed-code and critical-package gates alongside a realistic repository threshold.
- Treat uncovered high-risk paths as explicit review findings; a high percentage never waives required contract, failure, security, migration, or composition tests.
- Do not write empty, redundant, or implementation-coupled tests solely to increase coverage.

CI produces a machine-readable report such as Clover or Cobertura for quality services and an HTML report for diagnosis. Publish reports as protected CI artifacts or approved release assets; do not normally commit generated coverage output. The README badge must reflect the default branch and link to its maintained report, as required by [REPOSITORIES.md](REPOSITORIES.md).

## 14. Local commands

Each repository exposes stable Composer scripts so contributors do not need to remember runner-specific flags. A typical interface is:

```bash
composer test
composer test:unit
composer test:feature
composer test:coverage
composer test:parallel
```

The implementation may invoke Pest or PHPUnit. Document prerequisites such as the coverage driver, database services, browser binaries, or asset build. Commands published in the README and [DOCUMENTATION.md](DOCUMENTATION.md)-conforming guides must be exercised in CI.

Examples of direct commands, when needed for diagnosis:

```bash
vendor/bin/pest
vendor/bin/phpunit
vendor/bin/pest --filter="rejects addition"
XDEBUG_MODE=coverage vendor/bin/pest --coverage
```

Repositories may prefer PCOV or another compatible driver for faster line coverage. Do not hard-code a driver in contributor instructions unless the repository supports and verifies it.

## 15. Continuous integration

Pull-request CI should run formatting/linting, static analysis, architecture rules, unit and feature tests, contract/schema checks, relevant security checks, and coverage. Parallelize suites when isolation is proven.

Use separate jobs or schedules for expensive compatibility matrices, real database families, browser/visual tests, mutation tests, performance tests, provider sandboxes, and full upgrade paths. Required release evidence must still complete before publication.

The canonical workflows described by [REPOSITORIES.md](REPOSITORIES.md) are:

| Workflow | Required testing evidence |
|---|---|
| `install.yml` | Clean install, dependency resolution, migrations, bootstrap, and documented quick start |
| `tests.yml` | Automated suites, static/architecture/security checks, coverage generation and upload |
| `docker.yml` | Image build, container boot/health, migration smoke test, and relevant scan |

CI fails on test failures, prohibited warnings/deprecations according to repository policy, coverage regression beyond policy, schema drift, broken architecture constraints, or unexpected generated `/modules` and `/themes` changes.

## 16. Flaky, slow, and failing tests

- Reproduce failures with the recorded seed, test order, parallel worker, environment, and dependency versions.
- Fix shared state, timing assumptions, eventual consistency, external dependencies, or resource limits at the cause.
- Use bounded polling for asynchronous outcomes; never add arbitrary sleeps to hide races.
- A quarantined test requires a linked issue, owner, reason, risk assessment, and removal date. Quarantine must remain visible and must not silently turn required evidence green.
- Profile slow suites and move setup to the correct layer; do not merge tests or weaken isolation simply to shorten runtime.
- Reruns may collect diagnostic evidence but must not define a passing result.

## 17. Test review checklist

Reviewers confirm that tests:

- map to acceptance criteria, invariants, permissions, and documented public behavior;
- use the correct suite and owning repository;
- cover success, denial, invalid input, failure, retry/recovery, and boundary cases proportionately;
- are deterministic, isolated, parallel-safe, readable, and free of real sensitive data;
- avoid unnecessary mocks and private implementation coupling;
- validate relevant database, event, job, API, connector, theme, migration, and compatibility effects;
- update fixtures, schemas, snapshots, coverage expectations, and documentation intentionally;
- would fail for the defect or missing behavior they claim to protect.

## 18. Implementation sequence

1. Translate the user outcome and acceptance criteria into risks, invariants, boundaries, and failure modes.
2. Assign each behavior to its owning module, adapter, theme, API package, or application.
3. Write unit and feature tests around public actions and policies.
4. Define reusable contract suites before multiple implementations diverge.
5. Add architecture, security, tenant, migration, compatibility, and failure evidence.
6. Add host composition and critical journey tests.
7. Generate coverage, review meaningful gaps, and add risk-based tests rather than percentage fillers.
8. Document local commands, test data, external requirements, and diagnostic workflows.
9. Run the required CI matrix and retain evidence with the release.

## 19. Definition of done

Testing is complete when:

- acceptance criteria and important domain invariants have direct, readable evidence;
- unit, feature, contract, integration, and composition responsibilities are correctly separated;
- permissions, tenant isolation, invalid states, retries, duplicates, concurrency, partial failure, and recovery are tested where relevant;
- public PHP, event, API, webhook, and provider contracts have compatibility evidence;
- fresh install, supported upgrades, declared environments, and independent package installation pass;
- theme behavior has appropriate functional, accessibility, visual, compatibility, and performance evidence;
- coverage is generated, reported, linked, and reviewed without replacing risk-based judgment;
- tests are deterministic, safe for parallel CI, and free from production dependencies or sensitive data;
- local commands and testing documentation are accurate; and
- all required workflows pass before release.

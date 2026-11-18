# Accounting: Employee Expenses Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#employee-expenses). Observed identity: [`liberusoftware/module-accounting-employee-expenses`](../../../modules/source/liberusoftware--module-accounting-employee-expenses.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-employee-expenses`
**Domain specification:** [Employee Expenses](../features/employee-expenses.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Employee Expenses. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

## Domain-driven implementation plan

- Model the capability with small aggregates, entities, value objects, enums, domain services, and explicit lifecycle states. Enforce invariants inside the domain boundary and keep invalid transitions impossible or rejected with typed exceptions.
- Implement one application action per meaningful mutation/use case and purpose-built query/read-model classes for reads. Use typed immutable DTOs and stable identifiers at public boundaries; use repositories only where persistence abstraction adds value.
- Publish past-tense domain events after a successful local transaction. Use an outbox/inbox, idempotent handlers, sagas, or compensating actions for cross-module and distributed work; never mutate another module's private tables.

## Laravel and persistence plan

- Use PHP 8.5 strict types, PSR-compatible names, constructor injection, Laravel contracts, service providers, configuration, policies, validation, and route-independent application services. Format with the repository's Pint rules and keep static analysis clean.
- Keep Eloquent models as persistence mappings, not domain aggregates or API resources. The module owns migrations, constraints, indexes, casts, factories, seeders, retention, export, deletion, and upgrade behavior. Released migrations are immutable; production-safe follow-up migrations document locks, backfills, deployment order, and rollback limits.
- Queue work that exceeds the request budget or depends on external systems. Jobs carry authorized tenant/actor context, have explicit retry/backoff/timeout/idempotency rules, and emit structured logs, metrics, traces, correlation IDs, and operator-visible failure state.

## Security and user outcomes

- Apply policies consistently to HTTP, UI, console, queue, export, search, notification, and bulk paths. Enforce tenant/team/resource ownership, field sensitivity, consent, entitlement, and break-glass auditing; scopes never override domain authorization.
- Treat imports, files, webhooks, provider responses, and user input as untrusted. Redact credentials and protected data from logs, exceptions, events, snapshots, metrics, and test artifacts.
- Make normal workflows understandable for SMEs and personal users: actionable validation, safe defaults, reversible or previewable operations, clear status and recovery guidance, localization/timezone/currency support where relevant, accessibility in adapters, low operational overhead, and export/retention controls.

## Public boundary and adapters

Expose only stable contracts, actions, queries, events, resource data, and capability metadata needed by consumers. Keep provider SDKs, credentials, webhook mappings, and provider identifiers in separate adapter packages. Presentation packages may add validation at their boundary, but the core revalidates invariants and authorization and remains free of presentation dependencies.

## Verification and delivery plan

- Use unit tests for value objects, entities, aggregates, policies, and pure rules; feature/integration tests for actions, persistence, validation, tenancy, events, jobs, commands, migrations, upgrades, and recovery; and shared contract tests for adapters.
- Add architecture tests for forbidden App classes, private cross-module access, provider leakage, presentation dependencies, and dependency cycles. Test empty installs, supported upgrades, rollback policy, representative host composition, and compatibility across the declared Laravel/PHP/database matrix.
- Run the independent repository's Pest 5 suite through Composer scripts and the shared package testbench. Generate meaningful coverage, static-analysis, security, documentation/link, and performance evidence; coverage complements risk-based assertions and never replaces them.
- Release with Composer metadata, module manifest, service provider, changelog, migration notes, README, compatibility matrix, runbook, and safe install/enable/disable/upgrade/uninstall behavior. Disabling or removal never silently deletes user data.

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Claims** | Model `claims` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Categories** | Model `categories` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Policy checks** | Model `policy checks` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Per diem** | Model `per diem` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attendees** | Model `attendees` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Projects/dimensions** | Model `projects/dimensions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Approval** | Model `approval` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reimbursement** | Model `reimbursement` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Rejection** | Model `rejection` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Posting** | Model `posting` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_024000_create_accounting_employee_expense_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/database/migrations/2026_08_25_024000_create_accounting_employee_expense_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExpenseClaimQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Queries/ExpenseClaimQuery.php) | `public function paginate(?int $teamId = null, ?ClaimStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function total(ExpenseClaim $c): float` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddExpenseItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/AddExpenseItem.php) | `public function handle(ExpenseClaim $c, array $a): ExpenseItem` |
| [CreateExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/CreateExpenseClaim.php) | `public function handle(array $a): ExpenseClaim` |
| [DecideExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/DecideExpenseClaim.php) | `public function handle(ExpenseClaim $c, bool $approved, ?string $reason = null, ?string $actor = null): ExpenseClaim` |
| [PostExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/PostExpenseClaim.php) | `public function handle(ExpenseClaim $c, ?string $actor = null): ExpenseClaim` |
| [ReimburseExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/ReimburseExpenseClaim.php) | `public function handle(ExpenseClaim $c, ?string $actor = null): ExpenseClaim` |
| [SubmitExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/SubmitExpenseClaim.php) | `public function handle(ExpenseClaim $c, ?string $actor = null): ExpenseClaim` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ExpenseCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseCategory.php) | `team_id`, `category_ref`, `name`, `daily_limit`, `requires_receipt`, `metadata` |
| [ExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseClaim.php) | `team_id`, `employee_ref`, `claim_ref`, `currency`, `status`, `submitted_on`, `approved_on`, `reimbursed_on`, `posted_on`, `rejection_reason`, `project_ref`, `dimension_ref`, `metadata` |
| [ExpenseHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseHistory.php) | `claim_id`, `event`, `actor_ref`, `metadata` |
| [ExpenseItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseItem.php) | `claim_id`, `category_ref`, `spent_on`, `description`, `amount`, `tax_amount`, `merchant`, `receipt_ref`, `per_diem_days`, `attendees`, `metadata` |
| [Employee.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-api/src/Models/Employee.php) | `name`, `email`, `position`, `hire_date`, `tax_id`, `national_insurance_number`, `starter_declaration`, `p45_issue_date`, `has_student_loan`, `student_loan_plan` |

### Consuming adapter specifications

- [HTTP API contract](../api/employee-expenses.md) · [Filament 5](../filament/employee-expenses.md) · [Livewire 4](../livewire/employee-expenses.md) · [React + Inertia](../react/employee-expenses.md) · [Vue + Inertia](../vue/employee-expenses.md) · [Nuxt 4](../nuxt/employee-expenses.md) · [Next.js](../nextjs/employee-expenses.md) · [React Native](../react-native/employee-expenses.md) · [Flutter & Dart](../flutter/employee-expenses.md)
<!-- core-implementation-plan:end -->

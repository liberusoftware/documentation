# Accounting: Journal Approvals Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#journal-approvals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-journal-approvals-nuxt`
**Matching domain module:** `accounting-journal-approvals`
**Application:** Accounting
**Source feature:** [Journal Approvals](../features/journal-approvals.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/journal-approvals.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-journal-approvals` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Journal sources/types:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Thresholds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preparer/reviewer:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rejection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Posting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Emergency controls:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-journal-approvals-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `journal-sources-types`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `thresholds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preparer-reviewer`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rejection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `posting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `emergency-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-journal-approvals` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/journal-approvals.md)) |
| Capability Nuxt module skeleton | [`module-accounting-journal-approvals-nuxt`](https://github.com/liberusoftware/module-accounting-journal-approvals-nuxt) (`@liberusoftware/module-accounting-journal-approvals-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Journal sources/types** | Expose composable and Vue 3 component for `journal sources/types` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journal-approvals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Thresholds** | Expose composable and Vue 3 component for `thresholds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journal-approvals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Preparer/reviewer** | Expose composable and Vue 3 component for `preparer/reviewer` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journal-approvals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journal-approvals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Rejection** | Expose composable and Vue 3 component for `rejection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journal-approvals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Posting** | Expose composable and Vue 3 component for `posting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journal-approvals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Emergency controls** | Expose composable and Vue 3 component for `emergency controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/journal-approvals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [JournalApprovalQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Queries/JournalApprovalQuery.php) | `public function paginate(?int $teamId = null, ?ApprovalStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/AddEvidence.php) | `public function handle(JournalApproval $approval, array $attributes): JournalEvidence` |
| [ConfigureThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/ConfigureThreshold.php) | `public function handle(array $attributes): ApprovalThreshold` |
| [DecideJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/DecideJournal.php) | `public function handle(JournalApproval $approval, string $actor, bool $approved, ?string $comment = null): JournalApproval` |
| [PostJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/PostJournal.php) | `public function handle(JournalApproval $approval, bool $emergency = false, ?string $reason = null): JournalApproval` |
| [SubmitJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/SubmitJournal.php) | `public function handle(array $attributes, array $evidence = []): JournalApproval` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ApprovalThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/ApprovalThreshold.php) | `team_id`, `journal_type`, `minimum_amount`, `reviewer_role`, `required_approvals`, `emergency_allowed`, `active`, `metadata` |
| [JournalApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalApproval.php) | `team_id`, `approval_ref`, `journal_type`, `journal_source`, `journal_ref`, `preparer_ref`, `reviewer_ref`, `currency`, `amount`, `threshold_amount`, `status`, `submitted_at`, `decided_at`, `posted_at`, `emergency_reason`, `metadata` |
| [JournalDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalDecision.php) | `approval_id`, `actor_ref`, `decision`, `comment`, `decided_at`, `metadata` |
| [JournalEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalEvidence.php) | `approval_id`, `kind`, `file_ref`, `description`, `checksum`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [JournalApprovalsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals-api/src/Http/Controllers/JournalApprovalsController.php) | `public function __construct(private readonly JournalApprovalQuery $query)`<br>`public function index(Request $request): JournalApprovalResource`<br>`public function store(Request $request, SubmitJournal $action): JournalApprovalResource`<br>`public function show(JournalApproval $approval): JournalApprovalResource`<br>`public function decide(Request $request, JournalApproval $approval, DecideJournal $action): JournalApprovalResource`<br>`public function post(Request $request, JournalApproval $approval, PostJournal $action): JournalApprovalResource`<br>`public function evidence(Request $request, JournalApproval $approval, AddEvidence $action): JournalApprovalResource`<br>`public function threshold(Request $request, ConfigureThreshold $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-journal-approvals-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])
Route::get('/', [JournalApprovalsController::class, 'index'])->name('accounting.journal-approvals.list');
Route::post('/', [JournalApprovalsController::class, 'store'])->name('accounting.journal-approvals.create');
Route::get('/{approval}', [JournalApprovalsController::class, 'show'])->name('accounting.journal-approvals.show');
Route::post('/{approval}/decide', [JournalApprovalsController::class, 'decide'])->name('accounting.journal-approvals.decide');
Route::post('/{approval}/post', [JournalApprovalsController::class, 'post'])->name('accounting.journal-approvals.post');
Route::post('/{approval}/evidence', [JournalApprovalsController::class, 'evidence'])->name('accounting.journal-approvals.evidence');
Route::post('/thresholds', [JournalApprovalsController::class, 'threshold'])->name('accounting.journal-approvals.threshold');
```
<!-- layer-implementation-plan:end -->

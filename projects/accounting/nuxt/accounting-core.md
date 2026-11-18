# Accounting: Accounting Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-core-nuxt`
**Matching domain module:** `accounting-core`
**Application:** Accounting
**Source feature:** [Accounting Core](../features/accounting-core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Legal entities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Books:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accounting basis:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fiscal calendars:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Currencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Numbering:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Defaults:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Policies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Domain events:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `legal-entities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `books`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accounting-basis`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fiscal-calendars`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `currencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `numbering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `defaults`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `policies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `domain-events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-core.md)) |
| Capability Nuxt module skeleton | [`module-accounting-core-nuxt`](https://github.com/liberusoftware/module-accounting-core-nuxt) (`@liberusoftware/module-accounting-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Legal entities** | Expose composable and Vue 3 component for `legal entities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Books** | Expose composable and Vue 3 component for `books` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Accounting basis** | Expose composable and Vue 3 component for `accounting basis` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Fiscal calendars** | Expose composable and Vue 3 component for `fiscal calendars` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Currencies** | Expose composable and Vue 3 component for `currencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Numbering** | Expose composable and Vue 3 component for `numbering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Defaults** | Expose composable and Vue 3 component for `defaults` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Policies** | Expose composable and Vue 3 component for `policies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Domain events** | Expose composable and Vue 3 component for `domain events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateNumber.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/AllocateNumber.php) | `public function handle(NumberingSequence $sequence): string` |
| [CreateLegalEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/CreateLegalEntity.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): LegalEntity` |
| [SaveAccountingSetting.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveAccountingSetting.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(string $modelClass, ?Model $setting, array $attributes): Model` |
| [SaveBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveBook.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?Book $book, array $attributes): Book` |
| [SaveFiscalCalendar.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveFiscalCalendar.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?FiscalCalendar $calendar, array $attributes): FiscalCalendar` |
| [SaveNumberingSequence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveNumberingSequence.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?NumberingSequence $sequence, array $attributes): NumberingSequence` |
| [UpdateLegalEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/UpdateLegalEntity.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(LegalEntity $entity, array $attributes): LegalEntity` |
| [AccountingCorePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Policies/AccountingCorePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user): bool`<br>`public function delete(?Authenticatable $user): bool` |
| [LegalEntityPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Policies/LegalEntityPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, LegalEntity $entity): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, LegalEntity $entity): bool`<br>`public function delete(?Authenticatable $user, LegalEntity $entity): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingDefault.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/AccountingDefault.php) | `book_id`, `key`, `value` |
| [AccountingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/AccountingPolicy.php) | `book_id`, `key`, `value` |
| [Book.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/Book.php) | `legal_entity_id`, `name`, `code`, `accounting_basis`, `is_active` |
| [FiscalCalendar.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/FiscalCalendar.php) | `book_id`, `starts_on`, `ends_on`, `is_closed` |
| [LegalEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/LegalEntity.php) | `name`, `registration_number`, `currency_code`, `accounting_basis`, `is_active` |
| [NumberingSequence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/NumberingSequence.php) | `book_id`, `key`, `prefix`, `next_number`, `padding` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FoundationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Controllers/FoundationController.php) | `public function books(Request $request)`<br>`public function book(string $book): BookResource`<br>`public function storeBook(Request $request, SaveBook $save): BookResource`<br>`public function calendars(Request $request, string $book)`<br>`public function storeCalendar(Request $request, string $book, SaveFiscalCalendar $save): FiscalCalendarResource`<br>`public function sequences(Request $request, string $book)`<br>`public function storeSequence(Request $request, string $book, SaveNumberingSequence $save): NumberingSequenceResource`<br>`public function allocateSequence(string $book, string $sequence, AllocateNumber $allocate): JsonResponse` |
| [LegalEntityController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Controllers/LegalEntityController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(LegalEntity $legalEntity): LegalEntityResource`<br>`public function store(StoreLegalEntityRequest $request, CreateLegalEntity $create): JsonResponse`<br>`public function update(UpdateLegalEntityRequest $request, string $legalEntity, UpdateLegalEntity $update): LegalEntityResource`<br>`public function destroy(string $legalEntity): Response` |
| [SettingsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Controllers/SettingsController.php) | `public function index(Request $request, string $book, string $setting)`<br>`public function store(Request $request, string $book, string $setting, SaveAccountingSetting $save): AccountingSettingResource`<br>`public function show(string $book, string $setting, string $record): AccountingSettingResource`<br>`public function update(Request $request, string $book, string $setting, string $record, SaveAccountingSetting $save): AccountingSettingResource`<br>`public function destroy(string $book, string $setting, string $record): Response` |

**Observed route declarations:**

[modules/accounting-core-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounting-core')
Route::get('legal-entities', [LegalEntityController::class, 'index'])
Route::get('legal-entities/{legalEntity}', [LegalEntityController::class, 'show'])
Route::post('legal-entities', [LegalEntityController::class, 'store'])
Route::delete('legal-entities/{legalEntity}', [LegalEntityController::class, 'destroy'])
Route::get('books', [FoundationController::class, 'books'])->middleware('ability:accounting.core.read');
Route::get('books/{book}', [FoundationController::class, 'book'])->middleware('ability:accounting.core.read');
Route::post('books', [FoundationController::class, 'storeBook'])->middleware('ability:accounting.core.write');
Route::get('books/{book}/fiscal-calendars', [FoundationController::class, 'calendars'])->middleware('ability:accounting.core.read');
Route::post('books/{book}/fiscal-calendars', [FoundationController::class, 'storeCalendar'])->middleware('ability:accounting.core.write');
Route::get('books/{book}/numbering-sequences', [FoundationController::class, 'sequences'])->middleware('ability:accounting.core.read');
Route::post('books/{book}/numbering-sequences', [FoundationController::class, 'storeSequence'])->middleware('ability:accounting.core.write');
Route::post('books/{book}/numbering-sequences/{sequence}/allocate', [FoundationController::class, 'allocateSequence'])->middleware('ability:accounting.core.write');
Route::get('books/{book}/{setting}', [SettingsController::class, 'index'])
Route::get('books/{book}/{setting}/{record}', [SettingsController::class, 'show'])
Route::post('books/{book}/{setting}', [SettingsController::class, 'store'])
Route::delete('books/{book}/{setting}/{record}', [SettingsController::class, 'destroy'])
```
<!-- layer-implementation-plan:end -->

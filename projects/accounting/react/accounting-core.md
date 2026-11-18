# Accounting: Accounting Core React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-core-react-inertia`
**Matching domain module:** `accounting-core`
**Application:** Accounting
**Source feature:** [Accounting Core](../features/accounting-core.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Legal entities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Books:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Accounting basis:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Fiscal calendars:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Currencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Numbering:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Defaults:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Policies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Domain events:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-core-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `legal-entities`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `books`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `accounting-basis`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `fiscal-calendars`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `currencies`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `numbering`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `defaults`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `policies`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `domain-events`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-core-react-inertia`](https://github.com/liberusoftware/module-accounting-core-react-inertia) (`@liberusoftware/module-accounting-core-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-core.md) · [Core plan](../core/accounting-core.md) · [API plan](../api/accounting-core.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Legal entities** | Render `legal entities` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Books** | Render `books` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Accounting basis** | Render `accounting basis` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Fiscal calendars** | Render `fiscal calendars` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Currencies** | Render `currencies` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Numbering** | Render `numbering` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Defaults** | Render `defaults` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Policies** | Render `policies` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Domain events** | Render `domain events` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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

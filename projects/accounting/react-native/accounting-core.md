# Accounting Core React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-core-react-native
**Matching core package:** module-accounting-accounting-core ([implementation](../core/accounting-core.md))
**Matching API package:** module-accounting-accounting-core-api ([contract](../api/accounting-core.md))

## Implementation plan

This adapter presents Accounting Core for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-core.md), and [API module](../api/accounting-core.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-core`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-core.md)) |
| Capability React Native module skeleton | [`module-accounting-core-react-native`](https://github.com/liberusoftware/module-accounting-core-react-native) (`@liberusoftware/module-accounting-core-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Legal entities** | Progressive mobile list/detail/sheet flow for `legal entities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Books** | Progressive mobile list/detail/sheet flow for `books` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Accounting basis** | Progressive mobile list/detail/sheet flow for `accounting basis` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fiscal calendars** | Progressive mobile list/detail/sheet flow for `fiscal calendars` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Currencies** | Progressive mobile list/detail/sheet flow for `currencies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Numbering** | Progressive mobile list/detail/sheet flow for `numbering` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Defaults** | Progressive mobile list/detail/sheet flow for `defaults` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Policies** | Progressive mobile list/detail/sheet flow for `policies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Domain events** | Progressive mobile list/detail/sheet flow for `domain events` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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

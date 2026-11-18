# Accounting Supplier Portal Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-supplier-portal). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-supplier-portal-flutter
**Matching core package:** module-accounting-accounting-supplier-portal ([implementation](../core/accounting-supplier-portal.md))
**Matching API package:** module-accounting-accounting-supplier-portal-api ([contract](../api/accounting-supplier-portal.md))

## Implementation plan

This adapter presents Accounting Supplier Portal for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Supplier Portal API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-supplier-portal.md), and [API module](../api/accounting-supplier-portal.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-supplier-portal`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-supplier-portal-flutter`](https://github.com/liberusoftware/module-accounting-supplier-portal-flutter) (`module_accounting_supplier_portal_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-supplier-portal-dart-mobile`](https://github.com/liberusoftware/module-accounting-supplier-portal-dart-mobile) (`module_accounting_supplier_portal_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-supplier-portal-dart-desktop`](https://github.com/liberusoftware/module-accounting-supplier-portal-dart-desktop) (`module_accounting_supplier_portal_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-supplier-portal.md) · [Core plan](../core/accounting-supplier-portal.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Profile/bank-change requests** | Adaptive mobile cards/sheets for `profile/bank-change requests` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `profile/bank-change requests` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Purchase orders** | Adaptive mobile cards/sheets for `purchase orders` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `purchase orders` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Invoices** | Adaptive mobile cards/sheets for `invoices` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `invoices` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statements** | Adaptive mobile cards/sheets for `statements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Disputes** | Adaptive mobile cards/sheets for `disputes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `disputes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Payment status** | Adaptive mobile cards/sheets for `payment status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payment status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Secure documents** | Adaptive mobile cards/sheets for `secure documents` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `secure documents` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PortalResourceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Queries/PortalResourceQuery.php) | `public function paginate(?string $supplierId = null, ?string $type = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AttachPortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/AttachPortalDocument.php) | `public function handle(PortalResource $resource, array $attributes): PortalDocument` |
| [CreatePortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/CreatePortalResource.php) | `public function handle(array $attributes): PortalResource` |
| [TransitionPortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/TransitionPortalResource.php) | `public function handle(PortalResource $resource, PortalStatus\|string $status, ?string $reason = null): PortalResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalDocument.php) | `resource_id`, `path`, `original_name`, `mime_type`, `sha256`, `uploaded_by`, `metadata` |
| [PortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalResource.php) | `supplier_id`, `type`, `reference`, `status`, `currency`, `amount`, `payload`, `submitted_at`, `approved_at`, `rejected_reason`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PortalResourceController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-api/src/Http/Controllers/PortalResourceController.php) | `public function index(Request $request, PortalResourceQuery $query): mixed`<br>`public function show(PortalResource $portalResource): PortalResourceResource`<br>`public function store(Request $request, CreatePortalResource $action): mixed`<br>`public function transition(Request $request, PortalResource $portalResource, TransitionPortalResource $action): PortalResourceResource` |

**Observed route declarations:**

[modules/accounting-supplier-portal-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/supplier-portal')->group(function (): void {
Route::middleware('ability:accounting.supplier-portal.read')->group(function (): void {
Route::get('/', [PortalResourceController::class, 'index']);
Route::get('/{portalResource}', [PortalResourceController::class, 'show']);
Route::middleware('ability:accounting.supplier-portal.write')->group(function (): void {
Route::post('/', [PortalResourceController::class, 'store']);
Route::post('/{portalResource}/transition', [PortalResourceController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->

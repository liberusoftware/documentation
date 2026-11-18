# Catalog Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catalog). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-catalog-flutter
**Matching core package:** module-billing-catalog ([implementation](../core/catalog.md))
**Matching API package:** module-billing-catalog-api ([contract](../api/catalog.md))

## Implementation plan

This adapter presents Catalog for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Catalog API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/catalog.md), and [API module](../api/catalog.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `catalog`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) | [`module-billing-catalog-flutter`](https://github.com/liberusoftware/module-billing-catalog-flutter) (`module_billing_catalog_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) | [`module-billing-catalog-dart-mobile`](https://github.com/liberusoftware/module-billing-catalog-dart-mobile) (`module_billing_catalog_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) | [`module-billing-catalog-dart-desktop`](https://github.com/liberusoftware/module-billing-catalog-dart-desktop) (`module_billing_catalog_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | [API plan](../api/catalog.md) · [Core plan](../core/catalog.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Products** | Adaptive mobile cards/sheets for `products` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `products` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Plans** | Adaptive mobile cards/sheets for `plans` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `plans` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Add-ons** | Adaptive mobile cards/sheets for `add-ons` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `add-ons` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Bundles** | Adaptive mobile cards/sheets for `bundles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `bundles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Configurable options** | Adaptive mobile cards/sheets for `configurable options` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `configurable options` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Eligibility** | Adaptive mobile cards/sheets for `eligibility` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `eligibility` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Channels** | Adaptive mobile cards/sheets for `channels` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `channels` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Lifecycle** | Adaptive mobile cards/sheets for `lifecycle` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `lifecycle` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListCatalogRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListCatalogRecords.php) | `public function execute(string $model, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListProducts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListProducts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCatalogRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateCatalogRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $model, array $attributes): CatalogRecord` |
| [CreateProduct.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateProduct.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Product` |
| [TransitionCatalogLifecycle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionCatalogLifecycle.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CatalogRecord $record, CatalogStatus $status): CatalogRecord` |
| [TransitionProductLifecycle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionProductLifecycle.php) | `public function execute(Product $product, ProductStatus $status): Product` |
| [CatalogRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/CatalogRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, CatalogRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, CatalogRecord $record): bool` |
| [ProductPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/ProductPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Product $product): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Product $product): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Addon.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Addon.php) | No literal fillable array detected; inspect the model and API schema. |
| [Bundle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Bundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [CatalogRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/CatalogRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [Channel.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Channel.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConfigurableOption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/ConfigurableOption.php) | No literal fillable array detected; inspect the model and API schema. |
| [Eligibility.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Eligibility.php) | No literal fillable array detected; inspect the model and API schema. |
| [Plan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Plan.php) | No literal fillable array detected; inspect the model and API schema. |
| [Product.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Product.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CatalogRecordController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-api/src/Http/Controllers/CatalogRecordController.php) | `public function index(string $type, Request $request, ListCatalogRecords $query): JsonResponse`<br>`public function store(string $type, Request $request, CreateCatalogRecord $create): JsonResponse`<br>`public function transition(string $type, int $record, Request $request, TransitionCatalogLifecycle $transition): JsonResponse` |
| [ProductController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-api/src/Http/Controllers/ProductController.php) | `public function index(Request $request, ListProducts $query): JsonResponse`<br>`public function store(Request $request, CreateProduct $create): JsonResponse`<br>`public function transition(Request $request, int $product, TransitionProductLifecycle $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-catalog-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.catalog.read'])
->group(fn () => Route::get('/', [ProductController::class, 'index'])->name('products.index'));
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.catalog.write', 'idempotency'])
Route::post('/', [ProductController::class, 'store'])->name('products.store');
Route::patch('/products/{product}/lifecycle', [ProductController::class, 'transition'])->whereNumber('product')->name('products.lifecycle');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.catalog.read'])
Route::get('/{type}', [CatalogRecordController::class, 'index'])->whereIn('type', explode('|', $catalogTypes))->name('records.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.catalog.write', 'idempotency'])
Route::post('/{type}', [CatalogRecordController::class, 'store'])->whereIn('type', explode('|', $catalogTypes))->name('records.store');
Route::patch('/{type}/{record}/lifecycle', [CatalogRecordController::class, 'transition'])->whereIn('type', explode('|', $catalogTypes))->name('records.lifecycle');
```
<!-- layer-implementation-plan:end -->

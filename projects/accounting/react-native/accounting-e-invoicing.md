# Accounting E Invoicing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-e-invoicing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-e-invoicing-react-native
**Matching core package:** module-accounting-accounting-e-invoicing ([implementation](../core/accounting-e-invoicing.md))
**Matching API package:** module-accounting-accounting-e-invoicing-api ([contract](../api/accounting-e-invoicing.md))

## Implementation plan

This adapter presents Accounting E Invoicing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting E Invoicing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-e-invoicing.md), and [API module](../api/accounting-e-invoicing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-e-invoicing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-e-invoicing.md)) |
| Capability React Native module skeleton | [`module-accounting-e-invoicing-react-native`](https://github.com/liberusoftware/module-accounting-e-invoicing-react-native) (`@liberusoftware/module-accounting-e-invoicing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Structured invoice/credit formats** | Progressive mobile list/detail/sheet flow for `structured invoice/credit formats` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax-ID validation** | Progressive mobile list/detail/sheet flow for `tax-id validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Network/provider routing** | Progressive mobile list/detail/sheet flow for `network/provider routing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Signatures** | Progressive mobile list/detail/sheet flow for `signatures` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery/receipt status** | Progressive mobile list/detail/sheet flow for `delivery/receipt status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Archival** | Progressive mobile list/detail/sheet flow for `archival` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EInvoiceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Queries/EInvoiceQuery.php) | `public function paginate(?int $legalEntityId = null, ?DocumentStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ArchiveEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [CreateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/CreateEInvoice.php) | `public function handle(array $a): EInvoiceDocument` |
| [ReconcileEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ReconcileEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [RecordEInvoiceReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/RecordEInvoiceReceipt.php) | `public function handle(EInvoiceDocument $d, bool $accepted, ?string $message = null, ?string $actor = null): EInvoiceDocument` |
| [SignEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SignEInvoice.php) | `public function handle(EInvoiceDocument $d, string $signature, ?string $actor = null): EInvoiceDocument` |
| [SubmitEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SubmitEInvoice.php) | `public function handle(EInvoiceDocument $d, string $provider, ?string $actor = null): EInvoiceDocument` |
| [ValidateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ValidateEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EInvoiceDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceDocument.php) | `legal_entity_id`, `document_ref`, `document_type`, `format`, `status`, `tax_id`, `counterparty_ref`, `currency`, `provider_ref`, `payload`, `signature`, `submitted_at`, `received_at`, `archived_at`, `metadata` |
| [EInvoiceEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceEvent.php) | `document_id`, `event`, `provider_ref`, `actor_ref`, `message`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EInvoicingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing-api/src/Http/Controllers/EInvoicingController.php) | `public function __construct(private readonly EInvoiceQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, CreateEInvoice $a): EInvoiceResource`<br>`public function show(EInvoiceDocument $d): EInvoiceResource`<br>`public function validateDocument(Request $r, EInvoiceDocument $d, ValidateEInvoice $a): EInvoiceResource`<br>`public function sign(Request $r, EInvoiceDocument $d, SignEInvoice $a): EInvoiceResource`<br>`public function submit(Request $r, EInvoiceDocument $d, SubmitEInvoice $a): EInvoiceResource`<br>`public function receipt(Request $r, EInvoiceDocument $d, RecordEInvoiceReceipt $a): EInvoiceResource`<br>`public function reconcile(Request $r, EInvoiceDocument $d, ReconcileEInvoice $a): EInvoiceResource`<br>`public function archive(Request $r, EInvoiceDocument $d, ArchiveEInvoice $a): EInvoiceResource` |

**Observed route declarations:**

[modules/accounting-e-invoicing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/e-invoicing')->group(function (): void {
Route::middleware('ability:accounting.e-invoicing.read')->group(function (): void {
Route::get('/', [EInvoicingController::class, 'index']);
Route::get('/{d}', [EInvoicingController::class, 'show']);
Route::middleware('ability:accounting.e-invoicing.write')->group(function (): void {
Route::post('/', [EInvoicingController::class, 'store']);
Route::post('/{d}/validate', [EInvoicingController::class, 'validateDocument']);
Route::post('/{d}/sign', [EInvoicingController::class, 'sign']);
Route::post('/{d}/submit', [EInvoicingController::class, 'submit']);
Route::post('/{d}/receipt', [EInvoicingController::class, 'receipt']);
Route::post('/{d}/reconcile', [EInvoicingController::class, 'reconcile']);
Route::post('/{d}/archive', [EInvoicingController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->

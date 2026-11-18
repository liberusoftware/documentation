# Accounting Document Capture Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-document-capture). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-document-capture-flutter
**Matching core package:** module-accounting-accounting-document-capture ([implementation](../core/accounting-document-capture.md))
**Matching API package:** module-accounting-accounting-document-capture-api ([contract](../api/accounting-document-capture.md))

## Implementation plan

This adapter presents Accounting Document Capture for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Document Capture API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-document-capture.md), and [API module](../api/accounting-document-capture.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-document-capture`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-document-capture-flutter`](https://github.com/liberusoftware/module-accounting-document-capture-flutter) (`module_accounting_document_capture_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-document-capture-dart-mobile`](https://github.com/liberusoftware/module-accounting-document-capture-dart-mobile) (`module_accounting_document_capture_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-document-capture-dart-desktop`](https://github.com/liberusoftware/module-accounting-document-capture-dart-desktop) (`module_accounting_document_capture_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-document-capture.md) · [Core plan](../core/accounting-document-capture.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Mobile/web/email upload** | Adaptive mobile cards/sheets for `mobile/web/email upload` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mobile/web/email upload` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **OCR/extraction adapters** | Adaptive mobile cards/sheets for `ocr/extraction adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ocr/extraction adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Supplier matching** | Adaptive mobile cards/sheets for `supplier matching` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `supplier matching` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Line/tax capture** | Adaptive mobile cards/sheets for `line/tax capture` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `line/tax capture` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Confidence** | Adaptive mobile cards/sheets for `confidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `confidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Duplicate checks** | Adaptive mobile cards/sheets for `duplicate checks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `duplicate checks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Review** | Adaptive mobile cards/sheets for `review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Source retention** | Adaptive mobile cards/sheets for `source retention` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `source retention` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CaptureQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Queries/CaptureQuery.php) | `public function paginate(?int $teamId = null, ?CaptureStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ArchiveDocument.php) | `public function handle(CapturedDocument $d, ?string $actor = null): CapturedDocument` |
| [ExtractDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ExtractDocument.php) | `public function handle(CapturedDocument $d, array $extracted, float $confidence, string $adapter, ?string $actor = null): CapturedDocument` |
| [MarkDuplicateDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/MarkDuplicateDocument.php) | `public function handle(CapturedDocument $d, CapturedDocument $original, ?string $actor = null): CapturedDocument` |
| [ReviewDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ReviewDocument.php) | `public function handle(CapturedDocument $d, bool $approved, ?string $reason = null, ?string $actor = null): CapturedDocument` |
| [UploadDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/UploadDocument.php) | `public function handle(array $a): CapturedDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CaptureEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CaptureEvent.php) | `document_id`, `event`, `actor_ref`, `adapter_ref`, `message`, `metadata` |
| [CapturedDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CapturedDocument.php) | `team_id`, `source_channel`, `file_ref`, `checksum`, `mime_type`, `status`, `supplier_ref`, `document_ref`, `extracted_data`, `confidence`, `duplicate_of`, `retention_until`, `reviewed_by`, `reviewed_at`, `rejection_reason`, `metadata` |
| [Document.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-api/src/Models/Document.php) | `documentable_type`, `documentable_id`, `name`, `disk`, `retention_until`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DocumentCaptureController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-api/src/Http/Controllers/DocumentCaptureController.php) | `public function __construct(private readonly CaptureQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, UploadDocument $a): CapturedDocumentResource`<br>`public function show(CapturedDocument $d): CapturedDocumentResource`<br>`public function extract(Request $r, CapturedDocument $d, ExtractDocument $a): CapturedDocumentResource`<br>`public function review(Request $r, CapturedDocument $d, ReviewDocument $a): CapturedDocumentResource`<br>`public function duplicate(Request $r, CapturedDocument $d, MarkDuplicateDocument $a): CapturedDocumentResource`<br>`public function archive(Request $r, CapturedDocument $d, ArchiveDocument $a): CapturedDocumentResource` |

**Observed route declarations:**

[modules/accounting-document-capture-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/document-capture')->group(function (): void {
Route::middleware('ability:accounting.document-capture.read')->group(function (): void {
Route::get('/', [DocumentCaptureController::class, 'index']);
Route::get('/{d}', [DocumentCaptureController::class, 'show']);
Route::middleware('ability:accounting.document-capture.write')->group(function (): void {
Route::post('/', [DocumentCaptureController::class, 'store']);
Route::post('/{d}/extract', [DocumentCaptureController::class, 'extract']);
Route::post('/{d}/review', [DocumentCaptureController::class, 'review']);
Route::post('/{d}/duplicate', [DocumentCaptureController::class, 'duplicate']);
Route::post('/{d}/archive', [DocumentCaptureController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->

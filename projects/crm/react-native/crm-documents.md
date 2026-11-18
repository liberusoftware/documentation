# Crm Documents React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-documents). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-documents-react-native
**Matching core package:** module-crm-crm-documents ([implementation](../core/crm-documents.md))
**Matching API package:** module-crm-crm-documents-api ([contract](../api/crm-documents.md))

## Implementation plan

This adapter presents Crm Documents for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Documents API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-documents.md), and [API module](../api/crm-documents.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-documents`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-documents.md)) |
| Capability React Native module skeleton | [`module-crm-documents-react-native`](https://github.com/liberusoftware/module-crm-documents-react-native) (`@liberusoftware/module-crm-documents-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Sales/service files** | Progressive mobile list/detail/sheet flow for `sales/service files` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Folders** | Progressive mobile list/detail/sheet flow for `folders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Links** | Progressive mobile list/detail/sheet flow for `links` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Access** | Progressive mobile list/detail/sheet flow for `access` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Engagement tracking** | Progressive mobile list/detail/sheet flow for `engagement tracking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versioning** | Progressive mobile list/detail/sheet flow for `versioning` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Retention** | Progressive mobile list/detail/sheet flow for `retention` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **External-storage adapters** | Progressive mobile list/detail/sheet flow for `external-storage adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DocumentsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Queries/DocumentsQuery.php) | `public function documents(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDocument.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Actions/CreateDocument.php) | `public function __construct(private readonly DocumentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CrmDocument` |
| [CreateDocumentLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Actions/CreateDocumentLink.php) | `public function __construct(private readonly DocumentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CrmDocument $document, ?string $expiresAt = null): DocumentLink` |
| [CreateDocumentVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Actions/CreateDocumentVersion.php) | `public function __construct(private readonly DocumentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CrmDocument $document, array $input): DocumentVersion` |
| [RecordDocumentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Actions/RecordDocumentEngagement.php) | `public function execute(int $teamId, ?int $actorId, CrmDocument $document, array $input): DocumentEvent` |
| [DocumentsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Services/DocumentsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CrmDocument.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Models/CrmDocument.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Models/DocumentEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Models/DocumentLink.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents/src/Models/DocumentVersion.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DocumentsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-api/src/Http/Controllers/DocumentsController.php) | `public function __construct(private readonly DocumentsQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateDocument $action): JsonResponse`<br>`public function version(CrmDocument $document, CreateDocumentVersion $action): JsonResponse`<br>`public function link(CrmDocument $document, CreateDocumentLink $action): JsonResponse`<br>`public function engagement(CrmDocument $document, RecordDocumentEngagement $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-documents-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-documents')->group(function (): void {
Route::get('/', [DocumentsController::class, 'index']);
Route::post('/', [DocumentsController::class, 'store']);
Route::post('{document}/versions', [DocumentsController::class, 'version']);
Route::post('{document}/links', [DocumentsController::class, 'link']);
Route::post('{document}/engagement', [DocumentsController::class, 'engagement']);
```
<!-- layer-implementation-plan:end -->

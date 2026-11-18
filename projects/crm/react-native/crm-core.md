# Crm Core React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-core-react-native
**Matching core package:** module-crm-crm-core ([implementation](../core/crm-core.md))
**Matching API package:** module-crm-crm-core-api ([contract](../api/crm-core.md))

## Implementation plan

This adapter presents Crm Core for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-core.md), and [API module](../api/crm-core.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-core`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-core.md)) |
| Capability React Native module skeleton | [`module-crm-core-react-native`](https://github.com/liberusoftware/module-crm-core-react-native) (`@liberusoftware/module-crm-core-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Contacts** | Progressive mobile list/detail/sheet flow for `contacts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Organizations** | Progressive mobile list/detail/sheet flow for `organizations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Households** | Progressive mobile list/detail/sheet flow for `households` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Relationships** | Progressive mobile list/detail/sheet flow for `relationships` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Owners** | Progressive mobile list/detail/sheet flow for `owners` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Teams** | Progressive mobile list/detail/sheet flow for `teams` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tags** | Progressive mobile list/detail/sheet flow for `tags` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Notes** | Progressive mobile list/detail/sheet flow for `notes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Favorites** | Progressive mobile list/detail/sheet flow for `favorites` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Record lifecycle** | Progressive mobile list/detail/sheet flow for `record lifecycle` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Unified timeline** | Progressive mobile list/detail/sheet flow for `unified timeline` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddNote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/AddNote.php) | `public function execute(Record $record, string $body, ?int $authorId = null): Note` |
| [ArchiveRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/ArchiveRecord.php) | `public function execute(Record $record): Record` |
| [CreateRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateRecord.php) | `public function execute(string $type, int $teamId, string $name, array $data = [], ?int $ownerId = null): Record` |
| [CreateRelationship.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateRelationship.php) | `public function execute(Record $from, Record $to, string $type, array $metadata = []): Relationship` |
| [CreateTag.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateTag.php) | `public function execute(int $teamId, string $name): Tag` |
| [TagRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/TagRecord.php) | `public function execute(Record $record, Tag $tag): void` |
| [ToggleFavorite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/ToggleFavorite.php) | `public function execute(Model $record, int $teamId, int $userId): bool` |
| [UpdateRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/UpdateRecord.php) | `public function execute(Record $record, array $attributes): Record` |
| [RecordRepository.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Contracts/RecordRepository.php) | `public function find(string $type, int\|string $id): ?Record`<br>`public function paginate(string $type, int $perPage = 25): LengthAwarePaginator` |
| [EloquentRecordRepository.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Services/EloquentRecordRepository.php) | `public function find(string $type, int\|string $id): ?Record`<br>`public function paginate(string $type, int $perPage = 25): LengthAwarePaginator` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Attachment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Attachment.php) | `team_id`, `uploaded_by`, `disk`, `path`, `name`, `mime_type`, `size`, `metadata` |
| [Contact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Contact.php) | No literal fillable array detected; inspect the model and API schema. |
| [Favorite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Favorite.php) | `team_id`, `user_id` |
| [Household.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Household.php) | No literal fillable array detected; inspect the model and API schema. |
| [Note.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Note.php) | `team_id`, `author_id`, `body` |
| [Organization.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Organization.php) | No literal fillable array detected; inspect the model and API schema. |
| [Record.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Record.php) | `record_type`, `team_id`, `owner_id`, `name`, `status`, `data`, `archived_at` |
| [Relationship.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Relationship.php) | `team_id`, `relationship_type`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [RecordController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-api/src/Http/Controllers/RecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateRecord $create): JsonResponse`<br>`public function show(Request $request, int $record): JsonResponse`<br>`public function tags(Request $request): JsonResponse`<br>`public function createTag(Request $request, CreateTag $create): JsonResponse`<br>`public function addNote(Request $request, int $record, AddNote $add): JsonResponse`<br>`public function timeline(Request $request, int $record): JsonResponse`<br>`public function relationship(Request $request, int $record, CreateRelationship $create): JsonResponse`<br>`public function tag(Request $request, int $record, int $tag, TagRecord $attach): JsonResponse`<br>`public function favorite(Request $request, int $record, ToggleFavorite $toggle): JsonResponse`<br>`public function update(Request $request, int $record, UpdateRecord $update): JsonResponse`<br>`public function destroy(Request $request, int $record, ArchiveRecord $archive): JsonResponse` |

**Observed route declarations:**

[modules/crm-core-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-api/routes/api.php)

```php
Route::prefix('api/v1/crm/crm-core')->middleware(['auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [RecordController::class, 'index'])->name('crm.core.list');
Route::post('/', [RecordController::class, 'store'])->name('crm.core.create');
Route::get('/tags', [RecordController::class, 'tags'])->name('crm.core.tags.list');
Route::post('/tags', [RecordController::class, 'createTag'])->name('crm.core.tags.create');
Route::get('/{record}', [RecordController::class, 'show'])->name('crm.core.get');
Route::patch('/{record}', [RecordController::class, 'update'])->name('crm.core.update');
Route::get('/{record}/timeline', [RecordController::class, 'timeline'])->name('crm.core.timeline');
Route::post('/{record}/notes', [RecordController::class, 'addNote'])->name('crm.core.notes.create');
Route::post('/{record}/relationships', [RecordController::class, 'relationship'])->name('crm.core.relationships.create');
Route::post('/{record}/tags/{tag}', [RecordController::class, 'tag'])->name('crm.core.tags.attach');
Route::post('/{record}/favorite', [RecordController::class, 'favorite'])->name('crm.core.favorite');
Route::delete('/{record}', [RecordController::class, 'destroy'])->name('crm.core.delete');
```
<!-- layer-implementation-plan:end -->

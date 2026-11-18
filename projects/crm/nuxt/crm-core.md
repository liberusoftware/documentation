# CRM: CRM Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-core-nuxt`
**Matching domain module:** `crm-core`
**Application:** CRM
**Source feature:** [CRM Core](../features/crm-core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Contacts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Organizations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Households:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Relationships:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Owners:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Teams:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tags:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Notes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attachments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Favorites:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Record lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Unified timeline:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `contacts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `organizations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `households`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `relationships`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `owners`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `teams`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tags`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `notes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attachments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `favorites`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `record-lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `unified-timeline`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-core.md)) |
| Capability Nuxt module skeleton | [`module-crm-core-nuxt`](https://github.com/liberusoftware/module-crm-core-nuxt) (`@liberusoftware/module-crm-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Contacts** | Expose composable and Vue 3 component for `contacts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Organizations** | Expose composable and Vue 3 component for `organizations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Households** | Expose composable and Vue 3 component for `households` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Relationships** | Expose composable and Vue 3 component for `relationships` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Owners** | Expose composable and Vue 3 component for `owners` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Teams** | Expose composable and Vue 3 component for `teams` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Tags** | Expose composable and Vue 3 component for `tags` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Notes** | Expose composable and Vue 3 component for `notes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Attachments** | Expose composable and Vue 3 component for `attachments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Favorites** | Expose composable and Vue 3 component for `favorites` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Record lifecycle** | Expose composable and Vue 3 component for `record lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Unified timeline** | Expose composable and Vue 3 component for `unified timeline` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

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

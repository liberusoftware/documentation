# CRM: CRM Core Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-core-vue-inertia`
**Matching domain module:** `crm-core`
**Application:** CRM
**Source feature:** [CRM Core](../features/crm-core.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Contacts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Organizations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Households:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Relationships:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Owners:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Teams:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tags:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Notes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attachments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Favorites:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Record lifecycle:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Unified timeline:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-core-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `contacts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `organizations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `households`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `relationships`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `owners`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `teams`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tags`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `notes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `attachments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `favorites`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `record-lifecycle`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `unified-timeline`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `crm-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-core-vue-inertia`](https://github.com/liberusoftware/module-crm-core-vue-inertia) (`@liberusoftware/module-crm-core-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/crm-core.md) · [Core plan](../core/crm-core.md) · [API plan](../api/crm-core.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Contacts** | Render `contacts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Organizations** | Render `organizations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Households** | Render `households` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Relationships** | Render `relationships` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Owners** | Render `owners` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Teams** | Render `teams` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tags** | Render `tags` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Notes** | Render `notes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Attachments** | Render `attachments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Favorites** | Render `favorites` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Record lifecycle** | Render `record lifecycle` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Unified timeline** | Render `unified timeline` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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

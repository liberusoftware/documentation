# Control Panel: DNS Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#dns). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-control-panel-dns-vue-inertia`
**Matching domain module:** `control-panel-dns`
**Application:** Control Panel
**Source feature:** [DNS](../features/dns.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/dns.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Zones:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Records:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **DNSSEC:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Validation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Providers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Propagation checks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-control-panel-dns-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `zones`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `records`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `templates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dnssec`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `validation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `providers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `propagation-checks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-dns` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-control-panel-laravel-inertia-vue`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-control-panel-dns-vue-inertia`](https://github.com/liberusoftware/module-control-panel-dns-vue-inertia) (`@liberusoftware/module-control-panel-dns-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/dns.md) · [Core plan](../core/dns.md) · [API plan](../api/dns.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Zones** | Render `zones` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Records** | Render `records` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Templates** | Render `templates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **DNSSEC** | Render `dnssec` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Validation** | Render `validation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Providers** | Render `providers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Propagation checks** | Render `propagation checks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListZones.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Queries/ListZones.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ActivateZone.php) | `public function execute(Zone $zone): Zone` |
| [ArchiveZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ArchiveZone.php) | `public function execute(Zone $zone): Zone` |
| [CheckDnsPropagation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsPropagation.php) | `public function __construct(private readonly DnsResolver $resolver)`<br>`public function execute(array $attributes): array` |
| [CheckDnsResolution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsResolution.php) | `public function __construct(private readonly DnsResolver $resolver)`<br>`public function execute(array $attributes): array` |
| [CreateRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateRecord.php) | `public function execute(array $a): Record` |
| [CreateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateZone.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Zone` |
| [DeleteRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/DeleteRecord.php) | `public function execute(Record $record): void` |
| [RecordDnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RecordDnsCheck.php) | `public function execute(array $a): DnsCheck` |
| [RegisterDnsFeature.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RegisterDnsFeature.php) | `public function execute(array $a): Model` |
| [SuspendZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/SuspendZone.php) | `public function execute(Zone $zone): Zone` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsCheck.php) | `id`, `team_id`, `zone_id`, `kind`, `status`, `result`, `checked_at` |
| [DnsProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsProvider.php) | `id`, `team_id`, `name`, `driver`, `endpoint`, `credentials`, `settings`, `active` |
| [DnsTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsTemplate.php) | `id`, `team_id`, `name`, `records`, `active` |
| [DnsValidation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsValidation.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `resolver`, `expected`, `observed`, `checked_at`, `details` |
| [DnssecKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnssecKey.php) | `id`, `team_id`, `zone_id`, `key_tag`, `algorithm`, `digest_type`, `digest`, `public_key`, `private_key`, `active`, `rotated_at` |
| [PropagationCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/PropagationCheck.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `nameservers`, `results`, `checked_at` |
| [Record.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Record.php) | `zone_id`, `name`, `type`, `content`, `ttl`, `priority`, `metadata` |
| [Zone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Zone.php) | `team_id`, `domain`, `status`, `provider`, `dnssec_enabled`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ZoneController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-api/src/Http/Controllers/ZoneController.php) | `public function index(Request $request, ListZones $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateZone $create): JsonResponse`<br>`public function update(Request $request, string $id, UpdateZone $update): JsonResponse`<br>`public function record(Request $request, CreateRecord $create): JsonResponse`<br>`public function validateRecord(Request $request, ValidateRecord $validate): JsonResponse`<br>`public function updateRecord(Request $request, string $id, UpdateRecord $update): JsonResponse`<br>`public function deleteRecord(Request $request, string $id, DeleteRecord $delete): JsonResponse`<br>`public function bulkRecords(Request $request, CreateRecord $create): JsonResponse`<br>`public function check(Request $request, RecordDnsCheck $record): JsonResponse`<br>`public function resolutionCheck(Request $request, string $zone, CheckDnsResolution $check): JsonResponse`<br>`public function propagationCheck(Request $request, string $zone, CheckDnsPropagation $check): JsonResponse`<br>`public function feature(Request $request, RegisterDnsFeature $register): JsonResponse`<br>`public function suspend(Request $request, string $zone, SuspendZone $suspend): JsonResponse`<br>`public function archive(Request $request, string $zone, ArchiveZone $archive): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-dns-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/dns')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/zones', [ZoneController::class, 'index'])->name('control-panel.dns.zones.index');
Route::post('/zones', [ZoneController::class, 'store'])->name('control-panel.dns.zones.store');
Route::patch('/zones/{zone}', [ZoneController::class, 'update'])->name('control-panel.dns.zones.update');
Route::post('/records', [ZoneController::class, 'record'])->name('control-panel.dns.records.store');
Route::post('/records/validate', [ZoneController::class, 'validateRecord'])->name('control-panel.dns.records.validate');
Route::patch('/records/{record}', [ZoneController::class, 'updateRecord'])->name('control-panel.dns.records.update');
Route::delete('/records/{record}', [ZoneController::class, 'deleteRecord'])->name('control-panel.dns.records.delete');
Route::post('/records/bulk', [ZoneController::class, 'bulkRecords'])->name('control-panel.dns.records.bulk');
Route::post('/checks', [ZoneController::class, 'check'])->name('control-panel.dns.checks.store');
Route::post('zones/{zone}/resolution-check', [ZoneController::class, 'resolutionCheck'])->name('control-panel.dns.zones.resolution-check');
Route::post('zones/{zone}/propagation-check', [ZoneController::class, 'propagationCheck'])->name('control-panel.dns.zones.propagation-check');
Route::post('/features', [ZoneController::class, 'feature'])->name('control-panel.dns.features.store');
Route::post('zones/{zone}/suspend', [ZoneController::class, 'suspend'])->name('control-panel.dns.zones.suspend');
Route::post('zones/{zone}/archive', [ZoneController::class, 'archive'])->name('control-panel.dns.zones.archive');
Route::get('zones/{zone}', [ZoneController::class, 'show'])->name('control-panel.dns.show');
```
<!-- layer-implementation-plan:end -->

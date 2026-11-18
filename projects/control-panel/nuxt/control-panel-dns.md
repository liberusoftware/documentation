# Control Panel: Control Panel Dns Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-dns). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-control-panel-dns-nuxt`
**Matching domain module:** `control-panel-dns`
**Application:** Control Panel
**Source feature:** [Control Panel Dns](../features/control-panel-dns.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-dns.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-dns` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Zones:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Records:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **DNSSEC:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Providers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Propagation checks:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-control-panel-dns-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `zones`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `records`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dnssec`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `providers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `propagation-checks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-dns` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-dns.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-dns-nuxt`](https://github.com/liberusoftware/module-control-panel-dns-nuxt) (`@liberusoftware/module-control-panel-dns-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Zones** | Expose composable and Vue 3 component for `zones` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-dns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Records** | Expose composable and Vue 3 component for `records` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-dns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-dns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **DNSSEC** | Expose composable and Vue 3 component for `dnssec` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-dns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-dns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Providers** | Expose composable and Vue 3 component for `providers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-dns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Propagation checks** | Expose composable and Vue 3 component for `propagation checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-dns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

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

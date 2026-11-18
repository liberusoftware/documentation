# Control Panel: Control Panel Certificates Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-certificates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-control-panel-certificates-nuxt`
**Matching domain module:** `control-panel-certificates`
**Application:** Control Panel
**Source feature:** [Control Panel Certificates](../features/control-panel-certificates.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-certificates.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-certificates` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **ACME accounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Issuance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deployment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewal:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Revocation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expiry monitoring:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-control-panel-certificates-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `acme-accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `issuance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deployment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewal`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `revocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expiry-monitoring`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-certificates` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-certificates.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-certificates-nuxt`](https://github.com/liberusoftware/module-control-panel-certificates-nuxt) (`@liberusoftware/module-control-panel-certificates-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **ACME accounts** | Expose composable and Vue 3 component for `acme accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-certificates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Issuance** | Expose composable and Vue 3 component for `issuance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-certificates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Deployment** | Expose composable and Vue 3 component for `deployment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-certificates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Renewal** | Expose composable and Vue 3 component for `renewal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-certificates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Revocation** | Expose composable and Vue 3 component for `revocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-certificates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Expiry monitoring** | Expose composable and Vue 3 component for `expiry monitoring` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-certificates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListCertificates.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Queries/ListCertificates.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckCertificateExpiry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/CheckCertificateExpiry.php) | `public function execute(Certificate $certificate, int $thresholdDays = 30): CertificateExpiryAlert` |
| [ExpireCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/ExpireCertificate.php) | `public function execute(Certificate $certificate): Certificate` |
| [IssueCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/IssueCertificate.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Certificate` |
| [RecordCertificateOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RecordCertificateOperation.php) | `public function execute(array $attributes): CertificateOperation` |
| [RegisterAcmeAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RegisterAcmeAccount.php) | `public function execute(array $attributes): AcmeAccount` |
| [RegisterCertificateLifecycle.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RegisterCertificateLifecycle.php) | `public function execute(array $a): Model` |
| [RequestCertificateDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RequestCertificateDeployment.php) | `public function execute(Certificate $certificate, array $attributes): CertificateDeployment` |
| [RequestCertificateRenewal.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RequestCertificateRenewal.php) | `public function execute(Certificate $certificate, ?\DateTimeInterface $scheduledAt = null): CertificateRenewal` |
| [RevokeCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RevokeCertificate.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(Certificate $certificate): Certificate` |
| [UpdateCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/UpdateCertificate.php) | `public function execute(Certificate $certificate, array $attributes): Certificate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AcmeAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/AcmeAccount.php) | `id`, `team_id`, `email`, `directory`, `credentials`, `active` |
| [Certificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/Certificate.php) | `team_id`, `domains`, `status`, `issuer`, `certificate_pem`, `private_key`, `issued_at`, `expires_at`, `metadata` |
| [CertificateDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateDeployment.php) | `id`, `team_id`, `certificate_id`, `target_type`, `target_id`, `status`, `deployed_at`, `error`, `metadata` |
| [CertificateExpiryAlert.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateExpiryAlert.php) | `id`, `team_id`, `certificate_id`, `threshold_days`, `status`, `notified_at`, `metadata` |
| [CertificateOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateOperation.php) | `id`, `team_id`, `certificate_id`, `operation`, `status`, `details`, `completed_at` |
| [CertificateRenewal.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateRenewal.php) | `id`, `team_id`, `certificate_id`, `scheduled_at`, `started_at`, `completed_at`, `status`, `attempts`, `error` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CertificateController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-api/src/Http/Controllers/CertificateController.php) | `public function index(Request $request, ListCertificates $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id, UpdateCertificate $update): JsonResponse`<br>`public function store(Request $request, IssueCertificate $issue): JsonResponse`<br>`public function acme(Request $request, RegisterAcmeAccount $register): JsonResponse`<br>`public function operation(Request $request, RecordCertificateOperation $record): JsonResponse`<br>`public function lifecycle(Request $request, RegisterCertificateLifecycle $register): JsonResponse`<br>`public function deploy(Request $request, string $certificate, RequestCertificateDeployment $deploy): JsonResponse`<br>`public function renew(Request $request, string $certificate, RequestCertificateRenewal $renew): JsonResponse`<br>`public function expiryCheck(Request $request, string $certificate, CheckCertificateExpiry $check): JsonResponse`<br>`public function expire(Request $request, string $certificate, ExpireCertificate $expire): JsonResponse`<br>`public function revoke(Request $request, string $certificate, RevokeCertificate $revoke): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-certificates-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/certificates')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [CertificateController::class, 'index'])->name('control-panel.certificates.index');
Route::post('/', [CertificateController::class, 'store'])->name('control-panel.certificates.store');
Route::post('/acme-accounts', [CertificateController::class, 'acme'])->name('control-panel.certificates.acme');
Route::post('/operations', [CertificateController::class, 'operation'])->name('control-panel.certificates.operations');
Route::post('/lifecycle', [CertificateController::class, 'lifecycle'])->name('control-panel.certificates.lifecycle');
Route::post('/{certificate}/deploy', [CertificateController::class, 'deploy'])->name('control-panel.certificates.deploy');
Route::post('/{certificate}/renew', [CertificateController::class, 'renew'])->name('control-panel.certificates.renew');
Route::post('/{certificate}/expiry-check', [CertificateController::class, 'expiryCheck'])->name('control-panel.certificates.expiry-check');
Route::post('/{certificate}/expire', [CertificateController::class, 'expire'])->name('control-panel.certificates.expire');
Route::post('/{certificate}/revoke', [CertificateController::class, 'revoke'])->name('control-panel.certificates.revoke');
Route::get('/{certificate}', [CertificateController::class, 'show'])->name('control-panel.certificates.show');
Route::patch('/{certificate}', [CertificateController::class, 'update'])->name('control-panel.certificates.update');
```
<!-- layer-implementation-plan:end -->

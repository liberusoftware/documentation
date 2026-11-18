# Control Panel: Certificates Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#certificates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-control-panel-certificates-vue-inertia`
**Matching domain module:** `control-panel-certificates`
**Application:** Control Panel
**Source feature:** [Certificates](../features/certificates.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/certificates.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **ACME accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Issuance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deployment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Renewal:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Revocation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Expiry monitoring:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-control-panel-certificates-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `acme-accounts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `issuance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deployment`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `renewal`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `revocation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `expiry-monitoring`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-certificates` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-control-panel-laravel-inertia-vue`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-control-panel-certificates-vue-inertia`](https://github.com/liberusoftware/module-control-panel-certificates-vue-inertia) (`@liberusoftware/module-control-panel-certificates-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/certificates.md) · [Core plan](../core/certificates.md) · [API plan](../api/certificates.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **ACME accounts** | Render `acme accounts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Issuance** | Render `issuance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deployment** | Render `deployment` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Renewal** | Render `renewal` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Revocation** | Render `revocation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Expiry monitoring** | Render `expiry monitoring` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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

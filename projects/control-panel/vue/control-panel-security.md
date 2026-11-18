# Control Panel: Control Panel Security Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-security). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-control-panel-control-panel-security-vue-inertia`
**Matching domain module:** `control-panel-security`
**Application:** Control Panel
**Source feature:** [Control Panel Security](../features/control-panel-security.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-security.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Hardening:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Patching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **MFA/RBAC:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Secrets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Malware:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Intrusion controls:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Vulnerability and compliance status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-control-panel-control-panel-security-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `hardening`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `patching`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `mfa-rbac`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `secrets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `malware`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `intrusion-controls`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `vulnerability-and-compliance-status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-security` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-control-panel-laravel-inertia-vue`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-control-panel-security-vue-inertia`](https://github.com/liberusoftware/module-control-panel-security-vue-inertia) (`@liberusoftware/module-control-panel-security-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/control-panel-security.md) · [Core plan](../core/control-panel-security.md) · [API plan](../api/control-panel-security.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Hardening** | Render `hardening` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Patching** | Render `patching` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **MFA/RBAC** | Render `mfa/rbac` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Secrets** | Render `secrets` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Malware** | Render `malware` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Intrusion controls** | Render `intrusion controls` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Vulnerability and compliance status** | Render `vulnerability and compliance status` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListFindings.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Queries/ListFindings.php) | `public function execute(string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureFail2ban.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ConfigureFail2ban.php) | `public function execute(array $attributes): Fail2banSetting` |
| [RecordFail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFail2banBan.php) | `public function execute(Fail2banSetting $setting, array $attributes): Fail2banBan` |
| [RecordFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFinding.php) | `public function execute(array $attributes): SecurityFinding` |
| [RecordSecurityResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordSecurityResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [ResolveSecurityFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ResolveSecurityFinding.php) | `public function execute(SecurityFinding $finding): SecurityFinding` |
| [StoreSecret.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/StoreSecret.php) | `public function execute(array $attributes): SecretRecord` |
| [UnbanFail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UnbanFail2banBan.php) | `public function execute(Fail2banBan $ban): Fail2banBan` |
| [UpdateSecurityFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UpdateSecurityFinding.php) | `public function execute(SecurityFinding $finding, array $attributes): SecurityFinding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ComplianceStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/ComplianceStatus.php) | `team_id`, `framework`, `control`, `status`, `score`, `evidence`, `assessed_at`, `expires_at` |
| [Fail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banBan.php) | `team_id`, `jail_name`, `ip_address`, `banned_at`, `unbanned_at`, `ban_count`, `reason` |
| [Fail2banSetting.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banSetting.php) | `team_id`, `jail_name`, `enabled`, `max_retry`, `find_time`, `ban_time`, `whitelist_ips` |
| [HardeningControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/HardeningControl.php) | `team_id`, `subject_type`, `subject_id`, `control`, `desired`, `observed`, `status`, `evidence`, `checked_at` |
| [IntrusionControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/IntrusionControl.php) | `team_id`, `subject_type`, `subject_id`, `kind`, `action`, `threshold`, `window_seconds`, `enabled`, `metadata` |
| [MalwareScan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MalwareScan.php) | `team_id`, `subject_type`, `subject_id`, `status`, `scanner`, `findings`, `started_at`, `finished_at` |
| [MfaRbacPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MfaRbacPolicy.php) | `team_id`, `subject_type`, `subject_id`, `mfa_required`, `roles`, `permissions`, `status`, `metadata` |
| [PatchRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/PatchRecord.php) | `team_id`, `subject_type`, `subject_id`, `package`, `current_version`, `target_version`, `severity`, `status`, `published_at`, `installed_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SecurityFindingController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/src/Http/Controllers/SecurityFindingController.php) | `public function index(Request $request, ListFindings $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RecordFinding $record): JsonResponse`<br>`public function resolve(Request $request, string $id, ResolveSecurityFinding $resolve): JsonResponse`<br>`public function update(Request $request, string $id, UpdateSecurityFinding $update): JsonResponse`<br>`public function hardening(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patch(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patches(Request $request): JsonResponse`<br>`public function policy(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function policies(Request $request): JsonResponse`<br>`public function secret(Request $request, StoreSecret $store): JsonResponse`<br>`public function secrets(Request $request): JsonResponse`<br>`public function malware(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function malwareScans(Request $request): JsonResponse`<br>`public function intrusion(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function intrusionControls(Request $request): JsonResponse`<br>`public function fail2ban(Request $request, ConfigureFail2ban $configure): JsonResponse`<br>`public function fail2banBans(Request $request, string $jail, RecordFail2banBan $record): JsonResponse`<br>`public function listFail2banBans(Request $request, string $jail): JsonResponse`<br>`public function unbanFail2ban(Request $request, string $ban, UnbanFail2banBan $unban): JsonResponse`<br>`public function compliance(Request $request, RecordSecurityResource $record): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-security-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/security')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [SecurityFindingController::class, 'index'])->name('control-panel.security.index');
Route::post('/', [SecurityFindingController::class, 'store'])->name('control-panel.security.store');
Route::post('{finding}/resolve', [SecurityFindingController::class, 'resolve'])->name('control-panel.security.resolve');
Route::patch('{finding}', [SecurityFindingController::class, 'update'])->name('control-panel.security.update');
Route::post('hardening', [SecurityFindingController::class, 'hardening'])->name('control-panel.security.hardening.store');
Route::post('patches', [SecurityFindingController::class, 'patch'])->name('control-panel.security.patches.store');
Route::post('mfa-rbac', [SecurityFindingController::class, 'policy'])->name('control-panel.security.mfa-rbac.store');
Route::get('mfa-rbac', [SecurityFindingController::class, 'policies'])->name('control-panel.security.mfa-rbac.index');
Route::post('secrets', [SecurityFindingController::class, 'secret'])->name('control-panel.security.secrets.store');
Route::get('secrets', [SecurityFindingController::class, 'secrets'])->name('control-panel.security.secrets.index');
Route::post('malware-scans', [SecurityFindingController::class, 'malware'])->name('control-panel.security.malware.store');
Route::get('malware-scans', [SecurityFindingController::class, 'malwareScans'])->name('control-panel.security.malware.index');
Route::post('intrusion-controls', [SecurityFindingController::class, 'intrusion'])->name('control-panel.security.intrusion.store');
Route::get('intrusion-controls', [SecurityFindingController::class, 'intrusionControls'])->name('control-panel.security.intrusion.index');
Route::get('patches', [SecurityFindingController::class, 'patches'])->name('control-panel.security.patches.index');
Route::post('fail2ban', [SecurityFindingController::class, 'fail2ban'])->name('control-panel.security.fail2ban.store');
Route::get('fail2ban/{jail}/bans', [SecurityFindingController::class, 'listFail2banBans'])->name('control-panel.security.fail2ban.bans.index');
Route::post('fail2ban/{jail}/bans', [SecurityFindingController::class, 'fail2banBans'])->name('control-panel.security.fail2ban.bans.store');
Route::post('fail2ban/bans/{ban}/unban', [SecurityFindingController::class, 'unbanFail2ban'])->name('control-panel.security.fail2ban.bans.unban');
Route::post('compliance', [SecurityFindingController::class, 'compliance'])->name('control-panel.security.compliance.store');
Route::get('{finding}', [SecurityFindingController::class, 'show'])->name('control-panel.security.show');
```
<!-- layer-implementation-plan:end -->

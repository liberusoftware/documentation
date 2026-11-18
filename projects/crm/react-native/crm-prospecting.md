# Crm Prospecting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-prospecting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-prospecting-react-native
**Matching core package:** module-crm-crm-prospecting ([implementation](../core/crm-prospecting.md))
**Matching API package:** module-crm-crm-prospecting-api ([contract](../api/crm-prospecting.md))

## Implementation plan

This adapter presents Crm Prospecting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Prospecting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-prospecting.md), and [API module](../api/crm-prospecting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-prospecting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-prospecting.md)) |
| Capability React Native module skeleton | [`module-crm-prospecting-react-native`](https://github.com/liberusoftware/module-crm-prospecting-react-native) (`@liberusoftware/module-crm-prospecting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Ideal-customer profiles** | Progressive mobile list/detail/sheet flow for `ideal-customer profiles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Prospect searches** | Progressive mobile list/detail/sheet flow for `prospect searches` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **List building** | Progressive mobile list/detail/sheet flow for `list building` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Research queues** | Progressive mobile list/detail/sheet flow for `research queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contact reveal/credits** | Progressive mobile list/detail/sheet flow for `contact reveal/credits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider provenance** | Progressive mobile list/detail/sheet flow for `provider provenance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Compliant export/outreach handoff** | Progressive mobile list/detail/sheet flow for `compliant export/outreach handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProspectingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Queries/ProspectingQuery.php) | `public function profiles(int $teamId)`<br>`public function searches(int $teamId)`<br>`public function prospects(int $teamId)`<br>`public function queue(int $teamId)`<br>`public function exports(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateIdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateIdealCustomerProfile.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): IdealCustomerProfile` |
| [CreateProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateProspectSearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectSearch` |
| [ImportProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/ImportProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Prospect` |
| [QueueExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueExport.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectExport` |
| [QueueResearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueResearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectResearchItem` |
| [RevealContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/RevealContact.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectCredit` |
| [UpdateProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/UpdateProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $prospectId, array $input): Prospect` |
| [ProspectingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Services/ProspectingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/IdealCustomerProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [Prospect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/Prospect.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectCredit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectResearchItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectResearchItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectSearch.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProspectingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-api/src/Http/Controllers/ProspectingController.php) | `public function profiles(Request $r, ProspectingQuery $q)`<br>`public function profile(Request $r, CreateIdealCustomerProfile $a)`<br>`public function searches(Request $r, ProspectingQuery $q)`<br>`public function search(Request $r, CreateProspectSearch $a)`<br>`public function prospects(Request $r, ProspectingQuery $q)`<br>`public function prospect(Request $r, ImportProspect $a)`<br>`public function research(Request $r, QueueResearch $a)`<br>`public function reveal(Request $r, RevealContact $a)`<br>`public function export(Request $r, QueueExport $a)` |

**Observed route declarations:**

[modules/crm-prospecting-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/prospecting')->group(function (): void {
Route::get('/profiles', [ProspectingController::class, 'profiles']);
Route::post('/profiles', [ProspectingController::class, 'profile']);
Route::get('/searches', [ProspectingController::class, 'searches']);
Route::post('/searches', [ProspectingController::class, 'search']);
Route::get('/prospects', [ProspectingController::class, 'prospects']);
Route::post('/prospects', [ProspectingController::class, 'prospect']);
Route::post('/research', [ProspectingController::class, 'research']);
Route::post('/reveal', [ProspectingController::class, 'reveal']);
Route::post('/exports', [ProspectingController::class, 'export']);
```
<!-- layer-implementation-plan:end -->

# Parties React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#parties). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-parties-react-native
**Matching core package:** module-real-estate-parties ([implementation](../core/parties.md))
**Matching API package:** module-real-estate-parties-api ([contract](../api/parties.md))

## Implementation plan

This adapter presents Parties for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Parties API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/parties.md), and [API module](../api/parties.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `parties`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/parties.md)) |
| Capability React Native module skeleton | [`module-real-estate-parties-react-native`](https://github.com/liberusoftware/module-real-estate-parties-react-native) (`@liberusoftware/module-real-estate-parties-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Applicants** | Progressive mobile list/detail/sheet flow for `applicants` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Vendors** | Progressive mobile list/detail/sheet flow for `vendors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Landlords** | Progressive mobile list/detail/sheet flow for `landlords` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tenants** | Progressive mobile list/detail/sheet flow for `tenants` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Buyers** | Progressive mobile list/detail/sheet flow for `buyers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Solicitors** | Progressive mobile list/detail/sheet flow for `solicitors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contractors** | Progressive mobile list/detail/sheet flow for `contractors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Relationships** | Progressive mobile list/detail/sheet flow for `relationships` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Consent** | Progressive mobile list/detail/sheet flow for `consent` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PartyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Policies/PartyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Party $party): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Party $party): bool`<br>`public function delete(AuthUser $authUser, Party $party): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Party $party): bool`<br>`public function forceDelete(AuthUser $authUser, Party $party): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Party $party): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contact.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Contact.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactMessage.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/ContactMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [Party.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Party.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyRelationship.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyRelationship.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyReview.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContactController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-api/src/Http/Controllers/ContactController.php) | `public function store(Request $request, CreateContact $create): JsonResponse`<br>`public function update(Request $request, Contact $contact): JsonResponse`<br>`public function show(Request $request, Contact $contact): JsonResponse`<br>`public function destroy(Request $request, Contact $contact): Response` |
| [PartyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-api/src/Http/Controllers/PartyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateParty $create): JsonResponse`<br>`public function show(Request $request, Party $party): JsonResponse`<br>`public function update(Request $request, Party $party, UpdateParty $update): JsonResponse`<br>`public function consent(Request $request, Party $party, ManagePartyConsent $manage): JsonResponse`<br>`public function relationships(Request $request, Party $party): JsonResponse`<br>`public function relationship(Request $request, Party $party, CreatePartyRelationship $create): JsonResponse`<br>`public function destroyRelationship(Request $request, Party $party, PartyRelationship $relationship, DeletePartyRelationship $delete): Response`<br>`public function destroy(Request $request, Party $party, DeleteParty $delete): Response` |
| [ContactEnquiryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/Http/Controllers/ContactEnquiryController.php) | `public function store(Request $request, CreateContactMessage $createContactMessage): RedirectResponse` |

**Observed route declarations:**

[modules/real-estate-parties-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/parties')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PartyController::class, 'index'])->name('real-estate.parties.index');
Route::post('/', [PartyController::class, 'store'])->name('real-estate.parties.store');
Route::get('/{party}', [PartyController::class, 'show'])->name('real-estate.parties.show');
Route::post('/{party}/consent', [PartyController::class, 'consent'])->name('real-estate.parties.consent');
Route::get('/{party}/relationships', [PartyController::class, 'relationships'])->name('real-estate.parties.relationships');
Route::post('/{party}/relationships', [PartyController::class, 'relationship'])->name('real-estate.parties.relationships.store');
Route::delete('/{party}/relationships/{relationship}', [PartyController::class, 'destroyRelationship'])->name('real-estate.parties.relationships.destroy');
Route::delete('/{party}', [PartyController::class, 'destroy'])->name('real-estate.parties.destroy');
Route::prefix('api/v1/real-estate/contacts')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [ContactController::class, 'store'])->name('real-estate.contacts.store');
Route::get('/{contact}', [ContactController::class, 'show'])->name('real-estate.contacts.show');
Route::delete('/{contact}', [ContactController::class, 'destroy'])->name('real-estate.contacts.destroy');
```
<!-- layer-implementation-plan:end -->

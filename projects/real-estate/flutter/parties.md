# Parties Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#parties). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-parties-flutter
**Matching core package:** module-real-estate-parties ([implementation](../core/parties.md))
**Matching API package:** module-real-estate-parties-api ([contract](../api/parties.md))

## Implementation plan

This adapter presents Parties for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Parties API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/parties.md), and [API module](../api/parties.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `parties`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-parties-flutter`](https://github.com/liberusoftware/module-real-estate-parties-flutter) (`module_real_estate_parties_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-parties-dart-mobile`](https://github.com/liberusoftware/module-real-estate-parties-dart-mobile) (`module_real_estate_parties_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-parties-dart-desktop`](https://github.com/liberusoftware/module-real-estate-parties-dart-desktop) (`module_real_estate_parties_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/parties.md) · [Core plan](../core/parties.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Applicants** | Adaptive mobile cards/sheets for `applicants` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `applicants` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Vendors** | Adaptive mobile cards/sheets for `vendors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `vendors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Landlords** | Adaptive mobile cards/sheets for `landlords` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `landlords` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tenants** | Adaptive mobile cards/sheets for `tenants` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tenants` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Buyers** | Adaptive mobile cards/sheets for `buyers` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `buyers` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Solicitors** | Adaptive mobile cards/sheets for `solicitors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `solicitors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contractors** | Adaptive mobile cards/sheets for `contractors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contractors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Relationships** | Adaptive mobile cards/sheets for `relationships` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `relationships` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Consent** | Adaptive mobile cards/sheets for `consent` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `consent` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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

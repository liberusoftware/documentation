# Genealogy Core Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-genealogy-core-flutter
**Matching core package:** module-genealogy-genealogy-core ([implementation](../core/genealogy-core.md))
**Matching API package:** module-genealogy-genealogy-core-api ([contract](../api/genealogy-core.md))

## Implementation plan

This adapter presents Genealogy Core for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Genealogy Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/genealogy-core.md), and [API module](../api/genealogy-core.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `genealogy-core`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-genealogy-mobile-flutter`](https://github.com/liberusoftware/project-genealogy-mobile-flutter) | [`module-genealogy-core-flutter`](https://github.com/liberusoftware/module-genealogy-core-flutter) (`module_genealogy_core_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-genealogy-dart-mobile`](https://github.com/liberusoftware/project-genealogy-dart-mobile) | [`module-genealogy-core-dart-mobile`](https://github.com/liberusoftware/module-genealogy-core-dart-mobile) (`module_genealogy_core_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-genealogy-dart-desktop`](https://github.com/liberusoftware/project-genealogy-dart-desktop) | [`module-genealogy-core-dart-desktop`](https://github.com/liberusoftware/module-genealogy-core-dart-desktop) (`module_genealogy_core_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | [API plan](../api/genealogy-core.md) · [Core plan](../core/genealogy-core.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Trees** | Adaptive mobile cards/sheets for `trees` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `trees` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Ownership** | Adaptive mobile cards/sheets for `ownership` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ownership` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Identifiers** | Adaptive mobile cards/sheets for `identifiers` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `identifiers` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Privacy defaults** | Adaptive mobile cards/sheets for `privacy defaults` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `privacy defaults` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Terminology** | Adaptive mobile cards/sheets for `terminology` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `terminology` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Shared events** | Adaptive mobile cards/sheets for `shared events` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `shared events` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TreeStatistics.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Queries/TreeStatistics.php) | `public function __construct(private readonly ?ParentGraphReader $graph = null)`<br>`public function for(Tree $tree): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/CreateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(array $attributes): Tree` |
| [DeleteTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/DeleteTree.php) | `public function execute(Tree $tree): void` |
| [SetTreeOwner.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeOwner.php) | `public function execute(Tree $tree, string\|int\|null $userId): Tree` |
| [SetTreeVisibility.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeVisibility.php) | `public function execute(Tree $tree, bool $isPublic): Tree` |
| [UpdateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/UpdateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(Tree $tree, array $attributes): Tree` |
| [ParentGraphReader.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/ParentGraphReader.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [PersonReferenceResolver.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/PersonReferenceResolver.php) | `public function existsForTeam(mixed $personId, string $teamId): bool` |
| [TeamOwnedPolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TeamOwnedPolicy.php) | `public function viewAny(?object $actor): bool`<br>`public function view(?object $actor, object $record): bool`<br>`public function create(?object $actor): bool`<br>`public function update(?object $actor, object $record): bool`<br>`public function delete(?object $actor, object $record): bool` |
| [TreePolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TreePolicy.php) | `public function view(?object $actor, Tree $tree): bool`<br>`public function manage(?object $actor, Tree $tree): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Tree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Models/Tree.php) | `team_id`, `name`, `status`, `description`, `root_person_id`, `is_public`, `metadata`, `user_id`, `identifier`, `terminology` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TreeController.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-api/src/Http/Controllers/TreeController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, Tree $tree): TreeResource`<br>`public function store(Request $request, CreateTree $createTree): TreeResource`<br>`public function update(Request $request, Tree $tree, UpdateTree $updateTree): TreeResource`<br>`public function visibility(Request $request, Tree $tree, SetTreeVisibility $visibility): TreeResource`<br>`public function owner(Request $request, Tree $tree, SetTreeOwner $owner): TreeResource`<br>`public function destroy(Request $request, Tree $tree, DeleteTree $delete): void` |

**Observed route declarations:**

[modules/genealogy-core-api/routes/api.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-api/routes/api.php)

```php
Route::get('/', [TreeController::class, 'index'])->name('genealogy.core.index');
Route::get('/{tree}', [TreeController::class, 'show'])->name('genealogy.core.show');
Route::middleware('auth:sanctum')->group(function (): void {
Route::post('/', [TreeController::class, 'store'])->name('genealogy.core.store');
Route::patch('/{tree}/visibility', [TreeController::class, 'visibility'])->name('genealogy.core.visibility');
Route::patch('/{tree}/owner', [TreeController::class, 'owner'])->name('genealogy.core.owner');
Route::patch('/{tree}', [TreeController::class, 'update'])->name('genealogy.core.update');
Route::delete('/{tree}', [TreeController::class, 'destroy'])->name('genealogy.core.destroy');
```
<!-- layer-implementation-plan:end -->

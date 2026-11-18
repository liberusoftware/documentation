# Tree Viewer Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#tree-viewer). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-tree-viewer-flutter
**Matching core package:** module-genealogy-tree-viewer ([implementation](../core/tree-viewer.md))
**Matching API package:** module-genealogy-tree-viewer-api ([contract](../api/tree-viewer.md))

## Implementation plan

This adapter presents Tree Viewer for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Tree Viewer API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/tree-viewer.md), and [API module](../api/tree-viewer.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `tree-viewer`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-genealogy-mobile-flutter`](https://github.com/liberusoftware/project-genealogy-mobile-flutter) | [`module-genealogy-tree-viewer-flutter`](https://github.com/liberusoftware/module-genealogy-tree-viewer-flutter) (`module_genealogy_tree_viewer_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-genealogy-dart-mobile`](https://github.com/liberusoftware/project-genealogy-dart-mobile) | [`module-genealogy-tree-viewer-dart-mobile`](https://github.com/liberusoftware/module-genealogy-tree-viewer-dart-mobile) (`module_genealogy_tree_viewer_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-genealogy-dart-desktop`](https://github.com/liberusoftware/project-genealogy-dart-desktop) | [`module-genealogy-tree-viewer-dart-desktop`](https://github.com/liberusoftware/module-genealogy-tree-viewer-dart-desktop) (`module_genealogy_tree_viewer_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | [API plan](../api/tree-viewer.md) · [Core plan](../core/tree-viewer.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Pedigree** | Adaptive mobile cards/sheets for `pedigree` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pedigree` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Descendants** | Adaptive mobile cards/sheets for `descendants` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `descendants` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fan/chart views** | Adaptive mobile cards/sheets for `fan/chart views` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fan/chart views` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Navigation** | Adaptive mobile cards/sheets for `navigation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `navigation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Filters** | Adaptive mobile cards/sheets for `filters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `filters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Large-tree rendering** | Adaptive mobile cards/sheets for `large-tree rendering` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `large-tree rendering` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TreeGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Queries/TreeGraph.php) | `public function for( Person $root, int $generations = 3, bool $includeLiving = true, string $view = 'chart', bool $includeSiblings = false, int $maxNodes = 2000, ): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/CreateTreeView.php) | `public function execute(array $attributes): TreeView` |
| [DeleteTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/DeleteTreeView.php) | `public function execute(TreeView $tree): void` |
| [UpdateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/UpdateTreeView.php) | `public function execute(TreeView $tree, array $attributes): TreeView` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Models/TreeView.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

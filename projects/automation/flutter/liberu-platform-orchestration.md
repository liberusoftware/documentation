# Liberu Platform Orchestration Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-platform-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-automation-liberu-platform-orchestration-flutter
**Matching core package:** module-automation-liberu-platform-orchestration ([implementation](../core/liberu-platform-orchestration.md))
**Matching API package:** module-automation-liberu-platform-orchestration-api ([contract](../api/liberu-platform-orchestration.md))

## Implementation plan

This adapter presents Liberu Platform Orchestration for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Liberu Platform Orchestration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/liberu-platform-orchestration.md), and [API module](../api/liberu-platform-orchestration.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `liberu-platform-orchestration`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-automation-mobile-flutter`](https://github.com/liberusoftware/project-automation-mobile-flutter) | [`module-liberu-platform-orchestration-7f7db377-flutter`](https://github.com/liberusoftware/module-liberu-platform-orchestration-7f7db377-flutter) (`module_liberu_platform_orchestration_7f7db377_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-automation-dart-mobile`](https://github.com/liberusoftware/project-automation-dart-mobile) | [`module-liberu-platform-orchestration-7f7db377-dart-mobile`](https://github.com/liberusoftware/module-liberu-platform-orchestration-7f7db377-dart-mobile) (`module_liberu_platform_orchestration_7f7db377_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-automation-dart-desktop`](https://github.com/liberusoftware/project-automation-dart-desktop) | [`module-liberu-platform-orchestration-7f7db377-dart-desktop`](https://github.com/liberusoftware/module-liberu-platform-orchestration-7f7db377-dart-desktop) (`module_liberu_platform_orchestration_7f7db377_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | [API plan](../api/liberu-platform-orchestration.md) · [Core plan](../core/liberu-platform-orchestration.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Composition manifest** | Adaptive mobile cards/sheets for `composition manifest` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `composition manifest` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Capability graph** | Adaptive mobile cards/sheets for `capability graph` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `capability graph` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Lifecycle coordination** | Adaptive mobile cards/sheets for `lifecycle coordination` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `lifecycle coordination` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Release gates** | Adaptive mobile cards/sheets for `release gates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `release gates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Ownership registry** | Adaptive mobile cards/sheets for `ownership registry` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ownership registry` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration/src/Actions/CreatePlatformWorkflow.php) | `public function execute(array $attributes): PlatformWorkflow` |
| [TransitionPlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration/src/Actions/TransitionPlatformWorkflow.php) | `public function execute(PlatformWorkflow $record, LifecycleStatus $to): PlatformWorkflow` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration/src/Models/PlatformWorkflow.php) | `tenant_id`, `idempotency_key`, `name`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->

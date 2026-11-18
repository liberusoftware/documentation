# Liberu Executive Insights Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-executive-insights). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-automation-liberu-executive-insights-flutter
**Matching core package:** module-automation-liberu-executive-insights ([implementation](../core/liberu-executive-insights.md))
**Matching API package:** module-automation-liberu-executive-insights-api ([contract](../api/liberu-executive-insights.md))

## Implementation plan

This adapter presents Liberu Executive Insights for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Liberu Executive Insights API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/liberu-executive-insights.md), and [API module](../api/liberu-executive-insights.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `liberu-executive-insights`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-automation-mobile-flutter`](https://github.com/liberusoftware/project-automation-mobile-flutter) | [`module-liberu-executive-insights-b7a299fc-flutter`](https://github.com/liberusoftware/module-liberu-executive-insights-b7a299fc-flutter) (`module_liberu_executive_insights_b7a299fc_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-automation-dart-mobile`](https://github.com/liberusoftware/project-automation-dart-mobile) | [`module-liberu-executive-insights-b7a299fc-dart-mobile`](https://github.com/liberusoftware/module-liberu-executive-insights-b7a299fc-dart-mobile) (`module_liberu_executive_insights_b7a299fc_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-automation-dart-desktop`](https://github.com/liberusoftware/project-automation-dart-desktop) | [`module-liberu-executive-insights-b7a299fc-dart-desktop`](https://github.com/liberusoftware/module-liberu-executive-insights-b7a299fc-dart-desktop) (`module_liberu_executive_insights_b7a299fc_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | [API plan](../api/liberu-executive-insights.md) · [Core plan](../core/liberu-executive-insights.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Metric registry** | Adaptive mobile cards/sheets for `metric registry` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `metric registry` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cross-product projections** | Adaptive mobile cards/sheets for `cross-product projections` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cross-product projections` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Evidence drill-through** | Adaptive mobile cards/sheets for `evidence drill-through` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `evidence drill-through` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Decision snapshots** | Adaptive mobile cards/sheets for `decision snapshots` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `decision snapshots` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Data-quality operations** | Adaptive mobile cards/sheets for `data-quality operations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `data-quality operations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-automation-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateInsightSnapshot.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-executive-insights/src/Actions/CreateInsightSnapshot.php) | `public function execute(array $attributes): InsightSnapshot` |
| [TransitionInsightSnapshot.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-executive-insights/src/Actions/TransitionInsightSnapshot.php) | `public function execute(InsightSnapshot $record, LifecycleStatus $to): InsightSnapshot` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [InsightSnapshot.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-executive-insights/src/Models/InsightSnapshot.php) | `tenant_id`, `idempotency_key`, `name`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->

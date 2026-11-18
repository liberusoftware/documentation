# Liberu: Revenue and Care Orchestration Flutter + Dart

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration-flutter`

Implement the staff daily queue, health detail, guarded click-to-call, recovery request, push alert, and AI approval flows over the [API](../api/revenue-and-care-orchestration.md). Use sound DTOs, secure platform storage, no sensitive offline cache, explicit loading/queued/conflict states, idempotent mutations, deep links, dynamic text, semantics, RTL, and rotation support.

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `revenue-and-care-orchestration`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-liberu-official-mobile-flutter`](https://github.com/liberusoftware/project-liberu-official-mobile-flutter) | [`module-planned-liberu-revenue-and-care-orchestration-40451d50-flutter`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-flutter) (`module_planned_liberu_revenue_and_care_orchestration_40451d50_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-liberu-official-dart-mobile`](https://github.com/liberusoftware/project-liberu-official-dart-mobile) | [`module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-mobile`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-mobile) (`module_planned_liberu_revenue_and_care_orchestration_40451d50_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-liberu-official-dart-desktop`](https://github.com/liberusoftware/project-liberu-official-dart-desktop) | [`module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-desktop`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-desktop) (`module_planned_liberu_revenue_and_care_orchestration_40451d50_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | [API plan](../api/revenue-and-care-orchestration.md) · [Core plan](../core/revenue-and-care-orchestration.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Customer health constellation** | Adaptive mobile cards/sheets for `customer health constellation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `customer health constellation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-liberu-official-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Revenue-aware service recovery** | Adaptive mobile cards/sheets for `revenue-aware service recovery` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `revenue-aware service recovery` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-liberu-official-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contact-protection ledger** | Adaptive mobile cards/sheets for `contact-protection ledger` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contact-protection ledger` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-liberu-official-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cross-brand consent and quiet-hour evaluation** | Adaptive mobile cards/sheets for `cross-brand consent and quiet-hour evaluation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cross-brand consent and quiet-hour evaluation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-liberu-official-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval-gated AI recommendations** | Adaptive mobile cards/sheets for `approval-gated ai recommendations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval-gated ai recommendations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-liberu-official-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Mobile-ready daily queues** | Adaptive mobile cards/sheets for `mobile-ready daily queues` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mobile-ready daily queues` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-liberu-official-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

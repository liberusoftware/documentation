# Ecommerce: Catering — Flutter mobile

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catering). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Delivery boundary

Provide typed Dart API models, accessible widgets, event forms, quote review and status screens. Keep secrets in platform secure storage and isolate local drafts by account/store; refresh accepted/availability status on resume.

## Shared workflow and security

Use the [core lifecycle](../core/catering.md) and [approved API contract](../api/catering.md). Show event requirements (date, timezone, venue, guests, dietary/service needs), menu quantities and revision, quote currency/expiry/revision and a clear acceptance confirmation. Show availability, accepted quote, order creation and payment as separate statuses. A changed menu or stale/expired quotation requires refresh/re-quote; never optimistically claim acceptance or payment success.

Staff-only capabilities maintain meals, recipes/yields and packages and investigate pending conversion. Customer-facing DTOs, caches, exports, notifications and error messages exclude recipes, preparation instructions and ingredient costs. Scope all caches and queries by actor/Team/Store; clear private state on sign-out or account/store switch. The server rechecks every policy and transition. Disable unavailable integrations with an actionable explanation.

Provide loading, empty, validation, permission-denied, conflict, offline, unavailable-capacity, expired-quote and pending-conversion states. Retrying uses the same conversion idempotency key and reconciles with the server. Quote acceptance/order conversion requires online confirmation and must never silently replay a stale offline action.

## Completion evidence

Test customer and staff journeys, keyboard/screen-reader or native semantics, timezone/currency formatting, stale revision recovery, duplicate taps, interrupted network, privacy after account switch and absence of sensitive fields in client storage/logs. Contract tests use approved schemas and a host integration test proves quote-to-order behavior. Keep all business rules in the owning domain; templates/widgets/components only present approved projections.

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `catering`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-ecommerce-mobile-flutter`](https://github.com/liberusoftware/project-ecommerce-mobile-flutter) | `module-ecommerce-catering-flutter` | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-ecommerce-dart-mobile`](https://github.com/liberusoftware/project-ecommerce-dart-mobile) | `module-ecommerce-catering-dart-mobile` | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-ecommerce-dart-desktop`](https://github.com/liberusoftware/project-ecommerce-dart-desktop) | `module-ecommerce-catering-dart-desktop` | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | [API plan](../api/catering.md) · [Core plan](../core/catering.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Meals and ingredient composition** | Adaptive mobile cards/sheets for `meals and ingredient composition` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `meals and ingredient composition` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-ecommerce-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recipes and preparation yields** | Adaptive mobile cards/sheets for `recipes and preparation yields` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recipes and preparation yields` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-ecommerce-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Staff-managed catering packages** | Adaptive mobile cards/sheets for `staff-managed catering packages` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `staff-managed catering packages` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-ecommerce-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Event requirements and venue context** | Adaptive mobile cards/sheets for `event requirements and venue context` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `event requirements and venue context` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-ecommerce-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Immutable menu revisions** | Adaptive mobile cards/sheets for `immutable menu revisions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `immutable menu revisions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-ecommerce-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reproducible quotation context** | Adaptive mobile cards/sheets for `reproducible quotation context` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reproducible quotation context` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-ecommerce-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Availability confirmation and order conversion** | Adaptive mobile cards/sheets for `availability confirmation and order conversion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `availability confirmation and order conversion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-ecommerce-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

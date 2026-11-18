# Ecommerce: Catering — Dart desktop

**Matching domain module:** `ecommerce-catering`<br>
**Host skeleton:** [`project-ecommerce-dart-desktop`](https://github.com/liberusoftware/project-ecommerce-dart-desktop) ([wayfinder](../../wayfinders/dart-desktop.md) · [runbook](../../../guides/presentation/DART.md))<br>
**Shared API backend:** [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md))

## Delivery boundary

Use the desktop Flutter host with resizable event/menu workspaces, keyboard navigation, focus traversal and accessible tables/dialogs. Secure credentials using platform storage; protect exported quote files and printing with customer/staff projections. Refresh version on window resume and coordinate multi-window conversion to avoid duplicate requests.

## Feature and desktop surface matrix

| Feature / aspect | Dart desktop (`Linux` / `macOS` / `Windows`) implementation contract |
| --- | --- |
| **Meals and ingredient composition** | Resizable staff master-detail workspace for meals and ingredient quantities with keyboard navigation and unit validation. |
| **Recipes and preparation yields** | Staff-only recipe/yield editor and prep-sheet print/export; customer projections and exports strictly omit recipes and ingredient costs. |
| **Staff-managed catering packages** | Multi-column package builder and comparison view with keyboard shortcuts and dietary disclosure tags. |
| **Event requirements and venue context** | Structured event intake workspace with explicit IANA timezone display, venue capacity notes, guest count validation, and service schedule. |
| **Immutable menu revisions** | Side-by-side revision history diff and version-locked editing; prevent stale overwrites across multiple open desktop windows. |
| **Reproducible quotation context** | Detailed quote review pane with currency, tax/pricing assumptions, expiry countdown, authorized PDF/print export, and atomic acceptance. |
| **Availability confirmation and order conversion** | Dedicated operations queue showing separate booking availability, accepted quote, order reference, and payment state with idempotent retry/reconciliation. |

## Shared workflow and security

Use the [core lifecycle](../core/catering.md) and [approved API contract](../api/catering.md). Show event requirements (date, timezone, venue, guests, dietary/service needs), menu quantities and revision, quote currency/expiry/revision and a clear acceptance confirmation. Show availability, accepted quote, order creation and payment as separate statuses. A changed menu or stale/expired quotation requires refresh/re-quote; never optimistically claim acceptance or payment success.

Staff-only capabilities maintain meals, recipes/yields and packages and investigate pending conversion. Customer-facing DTOs, caches, exports, notifications and error messages exclude recipes, preparation instructions and ingredient costs. Scope all caches and queries by actor/Team/Store; clear private state on sign-out or account/store switch. The server rechecks every policy and transition. Disable unavailable integrations with an actionable explanation.

Provide loading, empty, validation, permission-denied, conflict, offline, unavailable-capacity, expired-quote and pending-conversion states. Retrying uses the same conversion idempotency key and reconciles with the server. Quote acceptance/order conversion requires online confirmation and must never silently replay a stale offline action.

## Completion evidence

Test customer and staff journeys, keyboard/screen-reader or native semantics, timezone/currency formatting, stale revision recovery, duplicate taps, interrupted network, privacy after account switch and absence of sensitive fields in client storage/logs. Contract tests use approved schemas and a host integration test proves quote-to-order behavior. Keep all business rules in the owning domain; templates/widgets/components only present approved projections.

# Ecommerce: Catering — Dart mobile

**Matching domain module:** `ecommerce-catering`<br>
**Host skeleton:** [`project-ecommerce-dart-mobile`](https://github.com/liberusoftware/project-ecommerce-dart-mobile) ([wayfinder](../../wayfinders/dart-mobile.md) · [runbook](../../../guides/presentation/DART.md))<br>
**Shared API backend:** [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md))

## Delivery boundary

Maintain a distinct host for the Dart mobile repository using Flutter widgets and typed API contracts. Support safe areas, touch, platform back navigation, deep-link validation and secure token storage. Do not assume the separate Flutter mobile host is the same release artifact.

## Feature and mobile surface matrix

| Feature / aspect | Dart mobile (`iOS` / `Android`) implementation contract |
| --- | --- |
| **Meals and ingredient composition** | Staff-only mobile maintenance cards with unit/yield validation; customer views show only approved meal descriptions and dietary disclosures. |
| **Recipes and preparation yields** | Restricted to authorized staff sessions; never cached or serialized in customer DTOs, local storage, or crash/error logs. |
| **Staff-managed catering packages** | Browseable package selection cards and configurable guest/quantity sheets with explicit revision tracking. |
| **Event requirements and venue context** | Native mobile date/time/IANA timezone pickers, venue details, guest counts, and dietary/service requirement inputs. |
| **Immutable menu revisions** | Display active revision badge; any quantity or meal change creates/requests a new revision rather than mutating an accepted snapshot. |
| **Reproducible quotation context** | Show currency, itemized quote snapshot, expiry timestamp, and atomic acceptance confirmation; prompt re-quote when expired or stale. |
| **Availability confirmation and order conversion** | Render availability, quote acceptance, order creation, deposit, and payment as distinct statuses; use a durable `Idempotency-Key` and online reconciliation for conversion. |

## Shared workflow and security

Use the [core lifecycle](../core/catering.md) and [approved API contract](../api/catering.md). Show event requirements (date, timezone, venue, guests, dietary/service needs), menu quantities and revision, quote currency/expiry/revision and a clear acceptance confirmation. Show availability, accepted quote, order creation and payment as separate statuses. A changed menu or stale/expired quotation requires refresh/re-quote; never optimistically claim acceptance or payment success.

Staff-only capabilities maintain meals, recipes/yields and packages and investigate pending conversion. Customer-facing DTOs, caches, exports, notifications and error messages exclude recipes, preparation instructions and ingredient costs. Scope all caches and queries by actor/Team/Store; clear private state on sign-out or account/store switch. The server rechecks every policy and transition. Disable unavailable integrations with an actionable explanation.

Provide loading, empty, validation, permission-denied, conflict, offline, unavailable-capacity, expired-quote and pending-conversion states. Retrying uses the same conversion idempotency key and reconciles with the server. Quote acceptance/order conversion requires online confirmation and must never silently replay a stale offline action.

## Completion evidence

Test customer and staff journeys, keyboard/screen-reader or native semantics, timezone/currency formatting, stale revision recovery, duplicate taps, interrupted network, privacy after account switch and absence of sensitive fields in client storage/logs. Contract tests use approved schemas and a host integration test proves quote-to-order behavior. Keep all business rules in the owning domain; templates/widgets/components only present approved projections.

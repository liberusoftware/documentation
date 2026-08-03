# Liberu official websites and staff apps — implementation guide

This is the build guide for the Liberu official websites and the internal staff web/mobile experience. It turns [LIBERU.md](../../LIBERU.md) into an installable delivery sequence while keeping existing project scopes authoritative.

For the public-facing behavior expected after installation, pair this guide with the [Liberu end-user interface guide](../../../user-guides/projects/liberu/README.md).

## What this guide builds

- Four branded public websites: `liberusoftware.com`, `liberuhosting.com`, `liberuservices.com`, and `liberugroup.com`.
- One authenticated staff workspace for sales, support, delivery, finance, operations, governance, and management.
- Optional React Native/Expo and Flutter staff clients using the same API and core contracts.
- A shared identity, organization, consent, notification, design-system, observability, and deployment foundation.

## Read in this order

1. [Custom module index](CUSTOM-MODULES.md) — what Liberu owns in addition to product modules.
2. [Required project modules](DEPENDENCIES.md) — what must be installed, enabled, configured, or deferred.
3. [Official website plan](OFFICIAL-WEBSITES.md) — brand/site composition and public-to-portal journeys.
4. [Staff mobile plan](STAFF-MOBILE.md) — staff tasks, offline policy, device permissions, and release boundaries.
5. [Build and documentation checklist](DELIVERY-CHECKLIST.md) — the evidence required before each release.

## Repository/application shape

Start from the Boilerplate Laravel application and compose Liberu packages; do not build a second application framework inside this project.

```text
liberu-application/
├── app/                         # composition, policies, brand config, app adapters only
├── config/liberu.php            # enabled sites, modules, environments, providers
├── routes/                      # composition routes and health/status façades
├── resources/themes/liberu/     # shared tokens, layouts, components, assets
├── modules/                     # installed packages; domain ownership stays in packages
├── openapi/                     # released API manifest and bundled schemas
├── apps/staff-mobile/           # React Native or Flutter host, not domain logic
└── docs/                        # ADRs, runbooks, journeys, release evidence
```

The application manifest distinguishes `installed`, `enabled`, `entitled`, and `authorized`. A package being present never grants access or makes a site feature visible.

## First production vertical slice

Build and reconcile this path before expanding breadth:

```text
liberuhosting.com
  → hosting plan/product page
  → consent-aware lead or checkout
  → payment/order accepted by Billing or Ecommerce
  → provisioning request owned by Control Panel
  → service portal and support case in CRM
  → invoice/accounting posting
  → renewal, incident, and recovery status
```

Every arrow has an owner, versioned contract/event, idempotency key, audit record, retry/reconciliation path, and user-visible queued/failure state.

## Non-negotiable boundaries

- CMS owns published content and media; Liberu owns site/brand composition and cross-site navigation.
- CRM owns people, relationships, consent, cases, conversations, sales, and customer success; Liberu owns cross-product queues and projections only.
- Billing/Ecommerce own prices, orders, invoices, subscriptions, payments, and refunds.
- Control Panel owns infrastructure mutations and observed service state.
- Automation owns generic workflows and AI runtime; Liberu supplies approved triggers, policies, and composition actions.
- Core owns invariants; API owns transport; web/mobile packages present contracts; themes never change authorization.

## Definition of ready

An official website or staff screen is ready only when its source-of-truth owner, route/audience, permission, consent behavior, API contract, loading/empty/error/offline state, analytics event, accessibility check, security review, test, runbook, and documentation link are recorded.

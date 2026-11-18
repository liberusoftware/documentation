# Boilerplate: Payment GoCardless Adapter Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-gocardless). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-payment-gocardless-filament`  
**Matching domain module:** `payment-gocardless`  
**Matching core package:** [`module-payment-gocardless`](../core/payment-gocardless.md) (`liberusoftware/payment-gocardless`)  
**Application:** Boilerplate  
**Source feature:** [Payment GoCardless Adapter](../features/payment-gocardless.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `payment-gocardless` public contract boundary (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **GoCardless Billing Requests and Instant Bank Pay (Open Banking):** resource/table/form/action or page behavior for this module's authorized workflow.
- **Direct Debit Mandate lifecycle (Bacs, SEPA, ACH, PAD, BECS):** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank payment collection, cancellation, retry, and refunds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **GoCardless Webhook-Signature HMAC-SHA256 verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Late failure, chargeback claim, and payout batch reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-payment-gocardless-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `gocardless-billing-requests-and-instant-bank-pay-open-banking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `direct-debit-mandate-lifecycle-bacs-sepa-ach-pad-becs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank-payment-collection-cancellation-retry-and-refunds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gocardless-webhook-signature-hmac-sha256-verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `late-failure-chargeback-claim-and-payout-batch-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-payment-gocardless-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payment-gocardless.md) · [API plan](../api/payment-gocardless.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **GoCardless Billing Requests and Instant Bank Pay (Open Banking)** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gocardless billing requests and instant bank pay (open banking)`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Direct Debit Mandate lifecycle (Bacs, SEPA, ACH, PAD, BECS)** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `direct debit mandate lifecycle (bacs, sepa, ach, pad, becs)`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank payment collection, cancellation, retry, and refunds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank payment collection, cancellation, retry, and refunds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **GoCardless Webhook-Signature HMAC-SHA256 verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gocardless webhook-signature hmac-sha256 verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Late failure, chargeback claim, and payout batch reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `late failure, chargeback claim, and payout batch reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

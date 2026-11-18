# Boilerplate: Payment Paddle Adapter Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-paddle). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-payment-paddle-filament`  
**Matching domain module:** `payment-paddle`  
**Matching core package:** [`module-payment-paddle`](../core/payment-paddle.md) (`liberusoftware/payment-paddle`)  
**Application:** Boilerplate  
**Source feature:** [Payment Paddle Adapter](../features/payment-paddle.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `payment-paddle` public contract boundary (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Paddle Billing transactions and Merchant-of-Record checkout:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Paddle adjustments for full/partial refunds and credits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Customer saved payment methods and subscription bridge:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Paddle-Signature ts/h1 HMAC webhook verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax, Merchant-of-Record fee, and payout reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-payment-paddle-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `paddle-billing-transactions-and-merchant-of-record-checkout`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paddle-adjustments-for-full-partial-refunds-and-credits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `customer-saved-payment-methods-and-subscription-bridge`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paddle-signature-ts-h1-hmac-webhook-verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax-merchant-of-record-fee-and-payout-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-payment-paddle-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payment-paddle.md) · [API plan](../api/payment-paddle.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Paddle Billing transactions and Merchant-of-Record checkout** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paddle billing transactions and merchant-of-record checkout`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Paddle adjustments for full/partial refunds and credits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paddle adjustments for full/partial refunds and credits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Customer saved payment methods and subscription bridge** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer saved payment methods and subscription bridge`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Paddle-Signature ts/h1 HMAC webhook verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paddle-signature ts/h1 hmac webhook verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax, Merchant-of-Record fee, and payout reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax, merchant-of-record fee, and payout reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

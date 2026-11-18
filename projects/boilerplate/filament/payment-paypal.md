# Boilerplate: Payment PayPal Adapter Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-payment-paypal-filament`  
**Matching domain module:** `payment-paypal`  
**Matching core package:** [`module-payment-paypal`](../core/payment-paypal.md) (`liberusoftware/payment-paypal`)  
**Application:** Boilerplate  
**Source feature:** [Payment PayPal Adapter](../features/payment-paypal.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `payment-paypal` public contract boundary (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **PayPal Orders v2 creation, approval, and authorization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **PayPal Vault v3 setup tokens and recurring payment tokens:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Order capture, authorization reauthorization/void, and refunds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **PayPal transmission-signature webhook verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **PayPal Customer Disputes and chargeback lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **PayPal transaction search and settlement reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-payment-paypal-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `paypal-orders-v2-creation-approval-and-authorization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paypal-vault-v3-setup-tokens-and-recurring-payment-tokens`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `order-capture-authorization-reauthorization-void-and-refunds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paypal-transmission-signature-webhook-verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paypal-customer-disputes-and-chargeback-lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paypal-transaction-search-and-settlement-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-payment-paypal-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payment-paypal.md) · [API plan](../api/payment-paypal.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **PayPal Orders v2 creation, approval, and authorization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paypal orders v2 creation, approval, and authorization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **PayPal Vault v3 setup tokens and recurring payment tokens** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paypal vault v3 setup tokens and recurring payment tokens`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Order capture, authorization reauthorization/void, and refunds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `order capture, authorization reauthorization/void, and refunds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **PayPal transmission-signature webhook verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paypal transmission-signature webhook verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **PayPal Customer Disputes and chargeback lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paypal customer disputes and chargeback lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **PayPal transaction search and settlement reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paypal transaction search and settlement reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

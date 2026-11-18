# Boilerplate: Payment Square Adapter Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-payment-square-filament`  
**Matching domain module:** `payment-square`  
**Matching core package:** [`module-payment-square`](../core/payment-square.md) (`liberusoftware/payment-square`)  
**Application:** Boilerplate  
**Source feature:** [Payment Square Adapter](../features/payment-square.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `payment-square` public contract boundary (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Square Payments API and Web Payments SDK tokenization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delayed capture, CompletePayment, CancelPayment, and Refunds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Square Cards on File and customer vaulting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Square Terminal API and in-person POS hardware bridge:** resource/table/form/action or page behavior for this module's authorized workflow.
- **HMAC-SHA256 webhook verification, Disputes API, and Payouts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-payment-square-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `square-payments-api-and-web-payments-sdk-tokenization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delayed-capture-completepayment-cancelpayment-and-refunds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `square-cards-on-file-and-customer-vaulting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `square-terminal-api-and-in-person-pos-hardware-bridge`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hmac-sha256-webhook-verification-disputes-api-and-payouts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-payment-square-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payment-square.md) · [API plan](../api/payment-square.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Square Payments API and Web Payments SDK tokenization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `square payments api and web payments sdk tokenization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delayed capture, CompletePayment, CancelPayment, and Refunds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delayed capture, completepayment, cancelpayment, and refunds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Square Cards on File and customer vaulting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `square cards on file and customer vaulting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Square Terminal API and in-person POS hardware bridge** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `square terminal api and in-person pos hardware bridge`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **HMAC-SHA256 webhook verification, Disputes API, and Payouts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hmac-sha256 webhook verification, disputes api, and payouts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

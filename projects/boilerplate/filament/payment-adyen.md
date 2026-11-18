# Boilerplate: Payment Adyen Adapter Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-payment-adyen-filament`  
**Matching domain module:** `payment-adyen`  
**Matching core package:** [`module-payment-adyen`](../core/payment-adyen.md) (`liberusoftware/payment-adyen`)  
**Application:** Boilerplate  
**Source feature:** [Payment Adyen Adapter](../features/payment-adyen.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `payment-adyen` public contract boundary (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Adyen Checkout sessions, /payments, and 3DS2 action handling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Asynchronous capture, technical cancel, and refund modifications:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tokenization and recurring storedPaymentMethod vaulting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adyen HMAC-SHA256 webhook notification verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Omnichannel POS Terminal API and settlement batch reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-payment-adyen-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `adyen-checkout-sessions-payments-and-3ds2-action-handling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `asynchronous-capture-technical-cancel-and-refund-modifications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tokenization-and-recurring-storedpaymentmethod-vaulting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adyen-hmac-sha256-webhook-notification-verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `omnichannel-pos-terminal-api-and-settlement-batch-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-payment-adyen-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payment-adyen.md) · [API plan](../api/payment-adyen.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Adyen Checkout sessions, /payments, and 3DS2 action handling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adyen checkout sessions, /payments, and 3ds2 action handling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Asynchronous capture, technical cancel, and refund modifications** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `asynchronous capture, technical cancel, and refund modifications`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tokenization and recurring storedPaymentMethod vaulting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tokenization and recurring storedpaymentmethod vaulting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Adyen HMAC-SHA256 webhook notification verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adyen hmac-sha256 webhook notification verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Omnichannel POS Terminal API and settlement batch reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `omnichannel pos terminal api and settlement batch reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

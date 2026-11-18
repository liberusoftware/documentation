# Boilerplate: Payment Core Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-payment-core-filament`  
**Matching domain module:** `payment-core`  
**Matching core package:** [`module-payment-core`](../core/payment-core.md) (`liberusoftware/payment-core`)  
**Application:** Boilerplate  
**Source feature:** [Payment Core](../features/payment-core.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `payment-core` public contract boundary (`liberusoftware/payment-contracts (PaymentGatewayRegistryContract, PaymentOrchestratorContract, WebhookInboxProcessorContract, SettlementReconciliationEngineContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Payment gateway registry and tenant/currency routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment intent orchestration and state machine:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Idempotency locking and immutable transaction ledger:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tokenized payment method vault and mandate directory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Verified webhook inbox and out-of-order reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dispute management and settlement batch reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-payment-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `payment-gateway-registry-and-tenant-currency-routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-intent-orchestration-and-state-machine`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `idempotency-locking-and-immutable-transaction-ledger`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tokenized-payment-method-vault-and-mandate-directory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `verified-webhook-inbox-and-out-of-order-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dispute-management-and-settlement-batch-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-payment-core-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payment-core.md) · [API plan](../api/payment-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Payment gateway registry and tenant/currency routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment gateway registry and tenant/currency routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment intent orchestration and state machine** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment intent orchestration and state machine`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Idempotency locking and immutable transaction ledger** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `idempotency locking and immutable transaction ledger`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tokenized payment method vault and mandate directory** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tokenized payment method vault and mandate directory`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Verified webhook inbox and out-of-order reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `verified webhook inbox and out-of-order reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dispute management and settlement batch reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dispute management and settlement batch reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

# Accounting: Customer Portal Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-portal). Observed identity: [`liberusoftware/module-accounting-customer-portal-filament`](../../../modules/source/liberusoftware--module-accounting-customer-portal-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-customer-portal-filament`  
**Matching domain module:** `accounting-customer-portal`  
**Application:** Accounting  
**Source feature:** [Customer Portal](../features/customer-portal.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-customer-portal` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Estimates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Credits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment history:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Documents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Communication preferences:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-customer-portal-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `estimates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `credits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `communication-preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-customer-portal` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-customer-portal-filament`](https://github.com/liberusoftware/module-accounting-customer-portal-filament) (`liberusoftware/accounting-customer-portal-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/customer-portal.md) · [API plan](../api/customer-portal.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Estimates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `estimates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Credits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `credits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disputes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disputes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Documents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `documents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Communication preferences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `communication preferences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomerPortalFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal-filament/src/CustomerPortalFilamentPlugin.php) · [CustomerPortalFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal-filament/src/CustomerPortalFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CustomerPortalQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Queries/CustomerPortalQuery.php) | `public function forTeam(int $teamId): Collection`<br>`public function forCustomer(int $teamId, string $customerId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomerPortalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Actions/CreateCustomerPortalRecord.php) | `public function handle(array $attributes): CustomerPortalRecord` |
| [PublishCustomerPortalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Actions/PublishCustomerPortalRecord.php) | `public function handle(CustomerPortalRecord $record): CustomerPortalRecord` |
| [ResolveCustomerPortalDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Actions/ResolveCustomerPortalDispute.php) | `public function handle(CustomerPortalRecord $record, array $resolution): CustomerPortalRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomerPortalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Models/CustomerPortalRecord.php) | `team_id`, `customer_id`, `type`, `reference`, `status`, `currency`, `amount`, `payload`, `metadata`, `published_at` |
<!-- layer-implementation-plan:end -->

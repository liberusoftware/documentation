# Accounting: Xero Migration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#xero-migration). Observed identity: [`liberusoftware/module-accounting-xero-migration-filament`](../../../modules/source/liberusoftware--module-accounting-xero-migration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-xero-migration-filament`  
**Matching domain module:** `accounting-xero-migration`  
**Application:** Accounting  
**Source feature:** [Xero Migration](../features/xero-migration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-xero-migration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Chart/tracking categories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoices/bills/credits/payments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Projects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expense claims:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attachments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source IDs:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-xero-migration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `chart-tracking-categories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoices-bills-credits-payments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `projects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expense-claims`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attachments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-ids`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-xero-migration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-xero-migration-filament`](https://github.com/liberusoftware/module-accounting-xero-migration-filament) (`liberusoftware/accounting-xero-migration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/xero-migration.md) · [API plan](../api/xero-migration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Chart/tracking categories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `chart/tracking categories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contacts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contacts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoices/bills/credits/payments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoices/bills/credits/payments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Projects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `projects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expense claims** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expense claims`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attachments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attachments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source IDs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source ids`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListXeroConnections.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-filament/src/Resources/Pages/ListXeroConnections.php) · [XeroConnectionResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-filament/src/Resources/XeroConnectionResource.php) · [XeroMigrationFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-filament/src/XeroMigrationFilamentPlugin.php) · [XeroMigrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-filament/src/XeroMigrationFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectXeroTenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/ConnectXeroTenant.php) | `public function handle(array $attributes): XeroConnection` |
| [RecordMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/RecordMigration.php) | `public function handle(XeroConnection $connection, array $attributes): XeroMigrationRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [XeroConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroConnection.php) | `team_id`, `tenant_ref`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at`, `metadata` |
| [XeroMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroMigrationRecord.php) | `team_id`, `connection_id`, `source_type`, `source_id`, `target_type`, `target_id`, `status`, `error`, `payload` |
<!-- layer-implementation-plan:end -->

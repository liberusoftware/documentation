# Accounting: Accounting Sage Accounting Migration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-sage-accounting-migration). Observed identity: [`liberusoftware/module-accounting-sage-accounting-migration-filament`](../../../modules/source/liberusoftware--module-accounting-sage-accounting-migration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-sage-accounting-migration-filament`  
**Matching domain module:** `accounting-sage-accounting-migration`  
**Application:** Accounting  
**Source feature:** [Accounting Sage Accounting Migration](../features/accounting-sage-accounting-migration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-sage-accounting-migration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Chart/analysis types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sales/purchases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank:** resource/table/form/action or page behavior for this module's authorized workflow.
- **VAT/CIS evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Currencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Budgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attachments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source IDs:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-sage-accounting-migration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `chart-analysis-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sales-purchases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `vat-cis-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `currencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `budgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attachments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-ids`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-sage-accounting-migration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-sage-accounting-migration-filament`](https://github.com/liberusoftware/module-accounting-sage-accounting-migration-filament) (`liberusoftware/accounting-sage-accounting-migration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-sage-accounting-migration.md) · [API plan](../api/accounting-sage-accounting-migration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Chart/analysis types** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `chart/analysis types`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contacts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contacts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Products** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `products`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sales/purchases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sales/purchases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **VAT/CIS evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `vat/cis evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Currencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `currencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Budgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `budgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attachments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attachments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source IDs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source ids`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SageAccountingMigrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration-filament/src/SageAccountingMigrationFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Actions/CreateMigrationRun.php) | `public function handle(?int $connectionId, array $metadata = []): SageMigrationRun` |
| [ImportMigrationRecords.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Actions/ImportMigrationRecords.php) | `public function handle(SageMigrationRun $run, array $records): SageMigrationRun` |
| [ReconcileMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Actions/ReconcileMigration.php) | `public function handle(SageMigrationRun $run): SageMigrationRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SageMigrationConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Models/SageMigrationConnection.php) | `team_id`, `provider`, `external_business_id`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at` |
| [SageMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Models/SageMigrationRecord.php) | `run_id`, `entity_type`, `source_id`, `status`, `payload`, `payload_hash`, `error_message`, `metadata` |
| [SageMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Models/SageMigrationRun.php) | `connection_id`, `status`, `total_records`, `imported_records`, `failed_records`, `metadata`, `started_at`, `finished_at` |
<!-- layer-implementation-plan:end -->

# Accounting: Accounting Custom Report Builder Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-custom-report-builder). Observed identity: [`liberusoftware/module-accounting-custom-report-builder-filament`](../../../modules/source/liberusoftware--module-accounting-custom-report-builder-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-custom-report-builder-filament`  
**Matching domain module:** `accounting-custom-report-builder`  
**Application:** Accounting  
**Source feature:** [Accounting Custom Report Builder](../features/accounting-custom-report-builder.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-custom-report-builder` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Governed measures/dimensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Formulas:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Comparisons:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Layouts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Permissions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Saved variants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exports:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-custom-report-builder-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `governed-measures-dimensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `formulas`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `comparisons`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `layouts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `permissions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `saved-variants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-custom-report-builder` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-custom-report-builder-filament`](https://github.com/liberusoftware/module-accounting-custom-report-builder-filament) (`liberusoftware/accounting-custom-report-builder-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-custom-report-builder.md) · [API plan](../api/accounting-custom-report-builder.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Governed measures/dimensions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `governed measures/dimensions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Grouping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `grouping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Formulas** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `formulas`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Comparisons** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `comparisons`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Layouts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `layouts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Permissions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permissions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Saved variants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `saved variants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomReportBuilderFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-filament/src/CustomReportBuilderFilamentPlugin.php) · [CustomReportBuilderFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-filament/src/CustomReportBuilderFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CustomReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Queries/CustomReportQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/CreateCustomReport.php) | `public function handle(array $attributes): CustomReport` |
| [RequestReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/RequestReportExport.php) | `public function handle(CustomReport $report, string $format, array $parameters = []): CustomReportExport` |
| [SaveReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/SaveReportVariant.php) | `public function handle(CustomReport $report, string $variantRef, array $configuration): CustomReportVariant` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReport.php) | `team_id`, `report_ref`, `name`, `measures`, `dimensions`, `filters`, `grouping`, `formulas`, `comparisons`, `layout`, `permissions` |
| [CustomReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportExport.php) | `report_id`, `team_id`, `format`, `status`, `parameters`, `completed_at` |
| [CustomReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportVariant.php) | `report_id`, `team_id`, `variant_ref`, `configuration` |
<!-- layer-implementation-plan:end -->

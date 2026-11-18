# Genealogy: Genealogy Reports Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-reports). Observed identity: [`liberusoftware/module-genealogy-reports-filament`](../../../modules/source/liberusoftware--module-genealogy-reports-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-genealogy-reports-filament`  
**Matching domain module:** `genealogy-reports`  
**Application:** Genealogy  
**Source feature:** [Genealogy Reports](../features/genealogy-reports.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-reports` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Family groups:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pedigrees:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Descendants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Timelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Research:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exportable charts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-genealogy-reports-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `family-groups`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pedigrees`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `descendants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `timelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `research`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exportable-charts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-reports` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-reports-filament`](https://github.com/liberusoftware/module-genealogy-reports-filament) (`liberusoftware/genealogy-reports-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/genealogy-reports.md) · [API plan](../api/genealogy-reports.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Family groups** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `family groups`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pedigrees** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pedigrees`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Descendants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `descendants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Timelines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `timelines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Research** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `research`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exportable charts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exportable charts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ReportsFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports-filament/src/ReportsFilamentServiceProvider.php) · [GenealogyReportResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports-filament/src/Resources/GenealogyReportResource.php) · [CreateGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports-filament/src/Resources/GenealogyReportResource/Pages/CreateGenealogyReport.php) · [EditGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports-filament/src/Resources/GenealogyReportResource/Pages/EditGenealogyReport.php) · [ListGenealogyReports.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports-filament/src/Resources/GenealogyReportResource/Pages/ListGenealogyReports.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BuildGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Queries/BuildGenealogyReport.php) | `public function execute(string $type, string $teamId, array $parameters = []): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/CreateGenealogyReport.php) | `public function execute(array $attributes): GenealogyReport`<br>`public function validate(array $values): void` |
| [DeleteGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/DeleteGenealogyReport.php) | `public function execute(GenealogyReport $report): void` |
| [GenerateGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/GenerateGenealogyReport.php) | `public function __construct(private ?BuildGenealogyReport $builder = null)`<br>`public function execute(GenealogyReport $report, array $parameters = []): GenealogyReport` |
| [UpdateGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/UpdateGenealogyReport.php) | `public function execute(GenealogyReport $report, array $attributes): GenealogyReport` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Models/GenealogyReport.php) | `team_id`, `name`, `type`, `status`, `metadata`, `generated_output`, `generated_at` |
<!-- layer-implementation-plan:end -->

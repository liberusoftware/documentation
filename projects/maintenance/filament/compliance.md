# Maintenance: Compliance Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#compliance). Observed identity: [`liberusoftware/module-maintenance-compliance-filament`](../../../modules/source/liberusoftware--module-maintenance-compliance-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-compliance-filament`  
**Matching domain module:** `maintenance-compliance`  
**Application:** Maintenance  
**Source feature:** [Compliance](../features/compliance.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `maintenance-compliance` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Requirements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Permits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Risk assessments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Incidents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Corrective actions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expiry:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-compliance-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `requirements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `permits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `risk-assessments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `incidents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `corrective-actions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expiry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `maintenance-compliance` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-compliance-filament`](https://github.com/liberusoftware/module-maintenance-compliance-filament) (`liberusoftware/maintenance-compliance-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/compliance.md) · [API plan](../api/compliance.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Requirements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requirements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Permits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Risk assessments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `risk assessments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Incidents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `incidents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Corrective actions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `corrective actions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expiry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expiry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ComplianceFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance-filament/src/ComplianceFilamentPlugin.php) · [ComplianceFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance-filament/src/ComplianceFilamentServiceProvider.php) · [ComplianceResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance-filament/src/Resources/ComplianceResource.php) · [CreateCompliance.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance-filament/src/Resources/ComplianceResource/Pages/CreateCompliance.php) · [EditCompliance.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance-filament/src/Resources/ComplianceResource/Pages/EditCompliance.php) · [ListCompliance.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance-filament/src/Resources/ComplianceResource/Pages/ListCompliance.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateComplianceRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance/src/Actions/CreateComplianceRecord.php) | `public function handle(int $teamId, array $attributes): ComplianceRecord` |
| [DeleteComplianceRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance/src/Actions/DeleteComplianceRecord.php) | `public function handle(int $teamId, ComplianceRecord $record): void` |
| [UpdateComplianceRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance/src/Actions/UpdateComplianceRecord.php) | `public function handle(int $teamId, ComplianceRecord $record, array $attributes): ComplianceRecord` |
| [ComplianceRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance/src/Policies/ComplianceRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ComplianceRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ComplianceRecord $record): bool`<br>`public function delete(object $user, ComplianceRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ComplianceRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-compliance/src/Models/ComplianceRecord.php) | `kind`, `title`, `description`, `status`, `expires_at`, `metadata`, `team_id` |
<!-- layer-implementation-plan:end -->

# CMS: Content Integrity Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-integrity). Observed identity: [`liberusoftware/module-cms-content-integrity-filament`](../../../modules/source/liberusoftware--module-cms-content-integrity-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-content-integrity-filament`  
**Matching domain module:** `cms-content-integrity`  
**Application:** CMS  
**Source feature:** [Content Integrity](../features/content-integrity.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-integrity` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Broken links/embeds/media:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Orphan detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schema validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicate content:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scheduled scans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Repair queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-content-integrity-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `broken-links-embeds-media`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `orphan-detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schema-validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicate-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scheduled-scans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `repair-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-integrity` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-integrity-filament`](https://github.com/liberusoftware/module-cms-content-integrity-filament) (`liberusoftware/cms-content-integrity-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/content-integrity.md) · [API plan](../api/content-integrity.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Broken links/embeds/media** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `broken links/embeds/media`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Orphan detection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `orphan detection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schema validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schema validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicate content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicate content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scheduled scans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scheduled scans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Repair queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `repair queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentIntegrityFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-integrity-filament/src/ContentIntegrityFilamentServiceProvider.php) · [IntegrityFindingResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-integrity-filament/src/Resources/IntegrityFindingResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentIntegrityService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-integrity/src/Services/ContentIntegrityService.php) | `public function findings(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function startScan(?int $teamId, string $scope = 'all'): IntegrityScan`<br>`public function finding(IntegrityScan $scan, array $data): IntegrityFinding`<br>`public function completeScan(IntegrityScan $scan): IntegrityScan`<br>`public function resolve(IntegrityFinding $finding): IntegrityFinding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IntegrityFinding.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-integrity/src/Models/IntegrityFinding.php) | `scan_id`, `team_id`, `subject_type`, `subject_key`, `kind`, `severity`, `message`, `context`, `status`, `resolved_at` |
| [IntegrityScan.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-integrity/src/Models/IntegrityScan.php) | `team_id`, `scope`, `status`, `finding_count`, `started_at`, `completed_at` |
<!-- layer-implementation-plan:end -->

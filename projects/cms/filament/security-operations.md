# CMS: Security Operations Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#security-operations). Observed identity: [`liberusoftware/module-cms-security-operations-filament`](../../../modules/source/liberusoftware--module-cms-security-operations-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-security-operations-filament`  
**Matching domain module:** `cms-security-operations`  
**Application:** CMS  
**Source feature:** [Security Operations](../features/security-operations.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-security-operations` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Update inventory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Extension provenance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content integrity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Upload scanning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Security headers integration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Advisories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Incident aids:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-security-operations-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `update-inventory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `extension-provenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-integrity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `upload-scanning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `security-headers-integration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `advisories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `incident-aids`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-security-operations` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-security-operations-filament`](https://github.com/liberusoftware/module-cms-security-operations-filament) (`liberusoftware/cms-security-operations-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/security-operations.md) · [API plan](../api/security-operations.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Update inventory** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `update inventory`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Extension provenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `extension provenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content integrity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content integrity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Upload scanning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `upload scanning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Security headers integration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `security headers integration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Advisories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `advisories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Incident aids** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `incident aids`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListSecurityOperations.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-security-operations-filament/src/Resources/Pages/ListSecurityOperations.php) · [SecurityOperationResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-security-operations-filament/src/Resources/SecurityOperationResource.php) · [SecurityOperationsFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-security-operations-filament/src/SecurityOperationsFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SecurityOperationsService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-security-operations/src/Services/SecurityOperationsService.php) | `public function inventory(array $packages, ?int $actorId = null): SecurityOperation`<br>`public function provenance(string $extension, string $version, string $source, ?int $actorId = null): SecurityOperation`<br>`public function integrity(string $subject, string $content, ?int $actorId = null): SecurityOperation`<br>`public function scan(UploadedFile $file, ?int $actorId = null): SecurityOperation`<br>`public function advisory(string $title, string $severity, array $details = [], ?int $actorId = null): SecurityOperation`<br>`public function incidentBundle(string $incident): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SecurityOperation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-security-operations/src/Models/SecurityOperation.php) | `kind`, `subject`, `status`, `evidence`, `content_hash`, `actor_id` |
<!-- layer-implementation-plan:end -->

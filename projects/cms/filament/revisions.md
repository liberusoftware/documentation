# CMS: Revisions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revisions). Observed identity: [`liberusoftware/module-cms-revisions-filament`](../../../modules/source/liberusoftware--module-cms-revisions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-revisions-filament`  
**Matching domain module:** `cms-revisions`  
**Application:** CMS  
**Source feature:** [Revisions](../features/revisions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-revisions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Immutable revisions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Autosave:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compare:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Restore:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Branching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attribution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retention:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Published-versus-working copies:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-revisions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `immutable-revisions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `autosave`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compare`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `restore`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `branching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `published-versus-working-copies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-revisions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-revisions-filament`](https://github.com/liberusoftware/module-cms-revisions-filament) (`liberusoftware/cms-revisions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/revisions.md) · [API plan](../api/revisions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Immutable revisions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `immutable revisions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Autosave** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `autosave`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compare** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compare`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Restore** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `restore`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Branching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `branching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Published-versus-working copies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `published-versus-working copies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListRevisions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-revisions-filament/src/Resources/Pages/ListRevisions.php) · [RevisionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-revisions-filament/src/Resources/RevisionResource.php) · [RevisionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-revisions-filament/src/RevisionsFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RevisionService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-revisions/src/Services/RevisionService.php) | `public function create(string $type, int $id, array $snapshot, ?int $userId = null, string $branch = 'main', bool $autosave = false, array $metadata = []): Revision`<br>`public function autosave(string $type, int $id, array $snapshot, ?int $userId = null, string $branch = 'main'): Revision`<br>`public function compare(Revision $from, Revision $to): array`<br>`public function restore(Revision $revision, ?int $userId = null, string $branch = 'main'): Revision`<br>`public function branch(Revision $revision, string $branch, ?int $userId = null): Revision`<br>`public function publish(Revision $revision): Revision`<br>`public function prune(string $type, int $id, int $retain = 20, string $branch = 'main'): int` |
<!-- layer-implementation-plan:end -->

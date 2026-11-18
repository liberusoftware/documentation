# Genealogy: Tree Viewer Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#tree-viewer). Observed identity: [`liberusoftware/module-genealogy-tree-viewer-filament`](../../../modules/source/liberusoftware--module-genealogy-tree-viewer-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-tree-viewer-filament`  
**Matching domain module:** `genealogy-tree-viewer`  
**Application:** Genealogy  
**Source feature:** [Tree Viewer](../features/tree-viewer.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-tree-viewer` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Pedigree:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Descendants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fan/chart views:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Navigation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Large-tree rendering:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-tree-viewer-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `pedigree`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `descendants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fan-chart-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `navigation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `large-tree-rendering`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-tree-viewer` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-tree-viewer-filament`](https://github.com/liberusoftware/module-genealogy-tree-viewer-filament) (`liberusoftware/genealogy-tree-viewer-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/tree-viewer.md) · [API plan](../api/tree-viewer.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Pedigree** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pedigree`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Descendants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `descendants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fan/chart views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fan/chart views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Navigation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `navigation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Large-tree rendering** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `large-tree rendering`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [TreeViewResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer-api/src/Resources/TreeViewResource.php) · [TreeViewResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer-filament/src/Resources/TreeViewResource.php) · [CreateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer-filament/src/Resources/TreeViewResource/Pages/CreateTreeView.php) · [EditTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer-filament/src/Resources/TreeViewResource/Pages/EditTreeView.php) · [ListTreeViews.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer-filament/src/Resources/TreeViewResource/Pages/ListTreeViews.php) · [TreeGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer-filament/src/Resources/TreeViewResource/Pages/TreeGraph.php) · [TreeViewerFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer-filament/src/TreeViewerFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [TreeGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Queries/TreeGraph.php) | `public function for( Person $root, int $generations = 3, bool $includeLiving = true, string $view = 'chart', bool $includeSiblings = false, int $maxNodes = 2000, ): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/CreateTreeView.php) | `public function execute(array $attributes): TreeView` |
| [DeleteTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/DeleteTreeView.php) | `public function execute(TreeView $tree): void` |
| [UpdateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/UpdateTreeView.php) | `public function execute(TreeView $tree, array $attributes): TreeView` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Models/TreeView.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

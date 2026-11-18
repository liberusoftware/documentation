# CMS: Cms Block Editor Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-block-editor). Observed identity: [`liberusoftware/module-cms-block-editor-filament`](../../../modules/source/liberusoftware--module-cms-block-editor-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-block-editor-filament`  
**Matching domain module:** `cms-block-editor`  
**Application:** CMS  
**Source feature:** [Cms Block Editor](../features/cms-block-editor.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-block-editor` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Typed content blocks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Nesting rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Patterns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reusable/global blocks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transforms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Previews:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Revision-safe data:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-block-editor-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `typed-content-blocks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `nesting-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `patterns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reusable-global-blocks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transforms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `previews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `revision-safe-data`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-block-editor` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-block-editor-filament`](https://github.com/liberusoftware/module-cms-block-editor-filament) (`liberusoftware/cms-block-editor-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-block-editor.md) · [API plan](../api/cms-block-editor.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Typed content blocks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `typed content blocks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Nesting rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `nesting rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Patterns** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `patterns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reusable/global blocks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reusable/global blocks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transforms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transforms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Previews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `previews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Revision-safe data** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `revision-safe data`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BlockEditorFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-block-editor-filament/src/BlockEditorFilamentServiceProvider.php) · [BlockDocumentResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-block-editor-filament/src/Resources/BlockDocumentResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BlockEditorService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-block-editor/src/Services/BlockEditorService.php) | `public function __construct(private BlockTypeRegistry $registry, private BlockRenderer $renderer)`<br>`public function save(?int $teamId, string $subjectType, string $subjectId, array $blocks, ?int $expectedVersion = null): BlockDocument`<br>`public function createPattern(?int $teamId, string $name, array $blocks, bool $reusable = true): BlockPattern`<br>`public function lock(BlockDocument $document, bool $locked = true): BlockDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BlockDocument.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-block-editor/src/Models/BlockDocument.php) | `team_id`, `subject_type`, `subject_id`, `blocks`, `version`, `locked`, `preview_html` |
| [BlockPattern.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-block-editor/src/Models/BlockPattern.php) | `team_id`, `name`, `blocks`, `reusable`, `locked` |
<!-- layer-implementation-plan:end -->

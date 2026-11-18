# CMS: Cms Rich Text Editor Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-rich-text-editor). Observed identity: [`liberusoftware/module-cms-rich-text-editor-filament`](../../../modules/source/liberusoftware--module-cms-rich-text-editor-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-rich-text-editor-filament`  
**Matching domain module:** `cms-rich-text-editor`  
**Application:** CMS  
**Source feature:** [Cms Rich Text Editor](../features/cms-rich-text-editor.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-rich-text-editor` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Semantic rich text:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tables:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Embeds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Code:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Paste cleanup:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accessibility hints:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Formats:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sanitization:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-rich-text-editor-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `semantic-rich-text`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tables`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `embeds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `code`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paste-cleanup`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accessibility-hints`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `formats`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sanitization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-rich-text-editor` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-rich-text-editor-filament`](https://github.com/liberusoftware/module-cms-rich-text-editor-filament) (`liberusoftware/cms-rich-text-editor-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-rich-text-editor.md) · [API plan](../api/cms-rich-text-editor.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Semantic rich text** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `semantic rich text`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tables** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tables`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Embeds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `embeds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Code** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `code`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Paste cleanup** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paste cleanup`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accessibility hints** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accessibility hints`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Formats** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `formats`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sanitization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sanitization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EditorResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-rich-text-editor-filament/src/Resources/EditorResource.php) · [RichTextEditorFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-rich-text-editor-filament/src/RichTextEditorFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RichTextService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-rich-text-editor/src/Services/RichTextService.php) | `public function __construct(private HtmlSanitizer $sanitizer)`<br>`public function sanitize(?string $html): string`<br>`public function cleanPaste(string $html): string`<br>`public function prepare(string $html, string $format = 'html'): array`<br>`public function accessibilityHints(string $html): array`<br>`public function embed(string $url, ?string $title = null): string` |
<!-- layer-implementation-plan:end -->

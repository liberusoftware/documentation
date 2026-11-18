# CMS: Module Cms Accessibility Assistant Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-accessibility-assistant). Observed identity: [`liberusoftware/module-cms-accessibility-assistant-filament`](../../../modules/source/liberusoftware--module-cms-accessibility-assistant-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-accessibility-assistant-filament`  
**Matching domain module:** `module-cms-accessibility-assistant`  
**Application:** CMS  
**Source feature:** [Module Cms Accessibility Assistant](../features/module-cms-accessibility-assistant.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-accessibility-assistant` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Authoring checks for headings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tables:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alternatives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contrast metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Language:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Captions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exceptions:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-accessibility-assistant-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `authoring-checks-for-headings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tables`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alternatives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contrast-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `language`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `captions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exceptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-accessibility-assistant` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-accessibility-assistant-filament`](https://github.com/liberusoftware/module-cms-accessibility-assistant-filament) (`liberusoftware/cms-accessibility-assistant-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-accessibility-assistant.md) · [API plan](../api/module-cms-accessibility-assistant.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Authoring checks for headings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `authoring checks for headings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tables** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tables`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Alternatives** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `alternatives`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contrast metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contrast metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Language** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `language`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Captions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `captions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exceptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exceptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccessibilityAssistantFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-accessibility-assistant-filament/src/AccessibilityAssistantFilamentServiceProvider.php) · [AccessibilityResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-accessibility-assistant-filament/src/Resources/AccessibilityResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AccessibilityAssistantService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-accessibility-assistant/src/Services/AccessibilityAssistantService.php) | `public function analyze(string $html, array $exceptions = []): array` |
<!-- layer-implementation-plan:end -->

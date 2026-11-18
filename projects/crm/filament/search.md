# CRM: Search Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#search). Observed identity: [`liberusoftware/search-filament`](../../../modules/source/liberusoftware--search-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-search-filament`  
**Matching domain module:** `search`  
**Application:** CRM  
**Source feature:** [Search](../features/search.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `search` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission-aware global search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Saved views:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Related-record search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suggestions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Index reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-search-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `permission-aware-global-search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `saved-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `related-record-search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suggestions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `index-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `search` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-search-filament`](https://github.com/liberusoftware/module-search-filament) (`liberusoftware/search-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/search.md) · [API plan](../api/search.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Permission-aware global search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permission-aware global search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Saved views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `saved views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Related-record search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `related-record search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suggestions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suggestions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Index reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `index reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [Overview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/search-filament/src/Pages/Overview.php) · [SearchFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/search-filament/src/SearchFilamentPlugin.php) · [SearchFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/search-filament/src/SearchFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SearchIndexer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/search/src/Contracts/SearchIndexer.php) | `public function index(string $type, Model $record): void`<br>`public function remove(string $type, string\|int $id): void`<br>`public function flush(string $type): void` |
| [LocalSearchIndexer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/search/src/Services/LocalSearchIndexer.php) | `public function index(string $type, Model $record): void`<br>`public function remove(string $type, string\|int $id): void`<br>`public function flush(string $type): void` |
| [SearchService.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/search/src/Services/SearchService.php) | `public function __construct(private readonly SearcherRegistry $searchers)`<br>`public function searchUsers(array $filters): LengthAwarePaginator`<br>`public function searchAll(array $filters): array` |
<!-- layer-implementation-plan:end -->

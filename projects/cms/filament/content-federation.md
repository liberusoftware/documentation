# CMS: Content Federation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-federation). Observed identity: [`liberusoftware/module-cms-content-federation-filament`](../../../modules/source/liberusoftware--module-cms-content-federation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-content-federation-filament`  
**Matching domain module:** `cms-content-federation`  
**Application:** CMS  
**Source feature:** [Content Federation](../features/content-federation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-federation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Content APIs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Remote-source adapters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Normalized references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cache/revalidation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source health:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Failure fallbacks:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-content-federation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `content-apis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `remote-source-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `normalized-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cache-revalidation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `failure-fallbacks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-federation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-federation-filament`](https://github.com/liberusoftware/module-cms-content-federation-filament) (`liberusoftware/cms-content-federation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/content-federation.md) · [API plan](../api/content-federation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Content APIs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content apis`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Remote-source adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `remote-source adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Normalized references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `normalized references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cache/revalidation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cache/revalidation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Failure fallbacks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `failure fallbacks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentFederationFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-federation-filament/src/ContentFederationFilamentServiceProvider.php) · [FederationSourceResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-federation-filament/src/Resources/FederationSourceResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RemoteSourceAdapter.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-federation/src/Contracts/RemoteSourceAdapter.php) | `public function fetch(string $externalType, string $externalKey, array $configuration = []): array` |
| [ContentFederationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-federation/src/Services/ContentFederationService.php) | `public function sources(?int $teamId, int $perPage = 25): LengthAwarePaginator`<br>`public function source(array $data, ?int $teamId = null): FederationSource`<br>`public function ingest(FederationSource $source, string $externalType, string $externalKey, array $payload, ?string $etag = null, ?int $cacheMinutes = null): FederationReference`<br>`public function fallback(FederationSource $source, string $externalType, string $externalKey): ?FederationReference`<br>`public function revalidate(FederationReference $reference): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FederationReference.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-federation/src/Models/FederationReference.php) | `source_id`, `external_type`, `external_key`, `payload`, `etag`, `cached_until`, `last_fetched_at` |
| [FederationSource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-federation/src/Models/FederationSource.php) | `team_id`, `name`, `adapter`, `endpoint`, `status`, `last_checked_at`, `last_succeeded_at`, `last_error` |
<!-- layer-implementation-plan:end -->

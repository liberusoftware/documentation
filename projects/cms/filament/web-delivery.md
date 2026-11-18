# CMS: Web Delivery Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#web-delivery). Observed identity: [`liberusoftware/module-cms-web-delivery-filament`](../../../modules/source/liberusoftware--module-cms-web-delivery-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-web-delivery-filament`  
**Matching domain module:** `cms-web-delivery`  
**Application:** CMS  
**Source feature:** [Web Delivery](../features/web-delivery.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-web-delivery` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Canonical route rendering:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Response metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cache tags:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preview mode:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redirects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Errors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Maintenance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Edge invalidation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-web-delivery-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `canonical-route-rendering`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `response-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cache-tags`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preview-mode`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redirects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `errors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `maintenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `edge-invalidation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-web-delivery` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-web-delivery-filament`](https://github.com/liberusoftware/module-cms-web-delivery-filament) (`liberusoftware/cms-web-delivery-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/web-delivery.md) · [API plan](../api/web-delivery.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Canonical route rendering** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `canonical route rendering`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Response metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `response metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cache tags** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cache tags`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preview mode** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preview mode`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redirects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redirects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Errors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `errors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Maintenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `maintenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Edge invalidation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `edge invalidation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DeliveryRouteResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-web-delivery-filament/src/Resources/DeliveryRouteResource.php) · [ListDeliveryRoutes.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-web-delivery-filament/src/Resources/Pages/ListDeliveryRoutes.php) · [WebDeliveryFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-web-delivery-filament/src/WebDeliveryFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DeliveryRouteQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Queries/DeliveryRouteQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $path): ?DeliveryRoute` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WebDeliveryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Actions/WebDeliveryService.php) | `public function __construct(private EdgeInvalidationRegistry $edge)`<br>`public function registerRoute(array $attributes): DeliveryRoute`<br>`public function updateRoute(DeliveryRoute $route, array $attributes): DeliveryRoute`<br>`public function deleteRoute(DeliveryRoute $route): void`<br>`public function render(string $path, ?string $previewToken = null): DeliveryResult`<br>`public function issuePreviewToken(DeliveryRoute $route): string`<br>`public function setMaintenance(DeliveryRoute $route, bool $enabled): DeliveryRoute`<br>`public function invalidate(array $cacheTags, string $idempotencyKey, ?string $provider = null, int\|string\|null $teamId = null): DeliveryInvalidation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DeliveryInvalidation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryInvalidation.php) | `idempotency_key`, `cache_tags`, `status`, `provider`, `failure_reason`, `completed_at`, `team_id` |
| [DeliveryRoute.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryRoute.php) | `path`, `route_type`, `content_type`, `content_id`, `body`, `canonical_url`, `redirect_url`, `redirect_status`, `metadata`, `cache_tags`, `cache_ttl`, `preview_enabled`, `preview_token_hash`, `preview_expires_at`, `maintenance`, `status`, `error_status`, `error_message`, `team_id` |
<!-- layer-implementation-plan:end -->

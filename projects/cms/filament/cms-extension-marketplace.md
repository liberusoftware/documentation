# CMS: Cms Extension Marketplace Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-extension-marketplace). Observed identity: [`liberusoftware/module-cms-extension-marketplace-filament`](../../../modules/source/liberusoftware--module-cms-extension-marketplace-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-extension-marketplace-filament`  
**Matching domain module:** `cms-extension-marketplace`  
**Application:** CMS  
**Source feature:** [Cms Extension Marketplace](../features/cms-extension-marketplace.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-extension-marketplace` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Publishers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Listings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Categories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Signing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reviews:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Licensing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Security status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Support:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Distribution:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-extension-marketplace-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `publishers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `listings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `categories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `signing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reviews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `licensing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `security-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `support`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `distribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-extension-marketplace` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-extension-marketplace-filament`](https://github.com/liberusoftware/module-cms-extension-marketplace-filament) (`liberusoftware/cms-extension-marketplace-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-extension-marketplace.md) · [API plan](../api/cms-extension-marketplace.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Publishers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `publishers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Listings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `listings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Categories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `categories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Versions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Signing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `signing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reviews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reviews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Licensing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `licensing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trials** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trials`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Security status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `security status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Support** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `support`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Distribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `distribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ExtensionMarketplaceFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-extension-marketplace-filament/src/ExtensionMarketplaceFilamentServiceProvider.php) · [ExtensionListingResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-extension-marketplace-filament/src/Resources/ExtensionListingResource.php) · [ListExtensionListings.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-extension-marketplace-filament/src/Resources/Pages/ListExtensionListings.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Queries/ExtensionMarketplaceQuery.php) | `public function catalog(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key): ?ExtensionListing` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Services/ExtensionMarketplaceService.php) | `public function publisher(array $attributes, ?int $teamId = null): ExtensionPublisher`<br>`public function category(array $attributes): ExtensionCategory`<br>`public function listing(array $attributes, ?int $teamId = null): ExtensionListing`<br>`public function version(ExtensionListing $listing, array $attributes): ExtensionVersion`<br>`public function sign(ExtensionVersion $version, string $signature, string $key): ExtensionVersion`<br>`public function security(ExtensionListing $listing, string $status): ExtensionListing`<br>`public function review(ExtensionListing $listing, string $type, int\|string $subject, int $rating, ?string $body = null, ?int $teamId = null): ExtensionReview`<br>`public function license(ExtensionListing $listing, string $subjectType, int\|string $subject, ?int $days = null): ExtensionLicense`<br>`public function trial(ExtensionListing $listing, string $subjectType, int\|string $subject, int $days = 14): ExtensionTrial`<br>`public function support(ExtensionListing $listing, array $attributes): ExtensionSupport`<br>`public function distribute(ExtensionVersion $version, array $attributes): ExtensionDistribution`<br>`public function ratingSummary(ExtensionListing $listing): array`<br>`public function publish(ExtensionListing $listing): ExtensionListing` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ExtensionCategory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionCategory.php) | `key`, `name`, `description` |
| [ExtensionDistribution.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionDistribution.php) | `version_id`, `channel`, `url`, `checksum`, `status` |
| [ExtensionLicense.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionLicense.php) | `listing_id`, `license_key`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |
| [ExtensionListing.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionListing.php) | `publisher_id`, `category_id`, `key`, `name`, `description`, `license`, `status`, `security_status`, `metadata`, `team_id` |
| [ExtensionPublisher.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionPublisher.php) | `key`, `name`, `website`, `status`, `team_id` |
| [ExtensionReview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionReview.php) | `listing_id`, `reviewer_type`, `reviewer_id`, `rating`, `review`, `status`, `team_id` |
| [ExtensionSupport.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionSupport.php) | `listing_id`, `channel`, `url`, `response_hours` |
| [ExtensionTrial.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionTrial.php) | `listing_id`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |
<!-- layer-implementation-plan:end -->

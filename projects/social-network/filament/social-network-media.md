# Social Network: Social Network Media Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-media). Observed identity: [`liberusoftware/module-social-network-media-filament`](../../../modules/source/liberusoftware--module-social-network-media-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-social-network-media-filament`  
**Matching domain module:** `social-network-media`  
**Application:** Social Network  
**Source feature:** [Social Network Media](../features/social-network-media.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-media` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Images:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Video:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audio:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Files:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Processing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alt text:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Captions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rights:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-social-network-media-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `images`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `video`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audio`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `files`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `processing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alt-text`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `captions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rights`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-media` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-media-filament`](https://github.com/liberusoftware/module-social-network-media-filament) (`liberusoftware/social-network-media-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/social-network-media.md) · [API plan](../api/social-network-media.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Images** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `images`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Video** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `video`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audio** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audio`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Files** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `files`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Processing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `processing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Alt text** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `alt text`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Captions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `captions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rights** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rights`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delivery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delivery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MediaFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media-filament/src/MediaFilamentPlugin.php) · [MediaFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media-filament/src/MediaFilamentServiceProvider.php) · [Assets.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media-filament/src/Pages/Assets.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/CreateAlbum.php) | `public function handle(Profile $owner, array $attributes): Album` |
| [DeleteAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteAlbum.php) | `public function handle(Profile $owner, Album $album): void` |
| [DeleteMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteMediaAsset.php) | `public function handle(Profile $owner, MediaAsset $asset): void` |
| [MarkMediaReady.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/MarkMediaReady.php) | `public function handle(Profile $owner, MediaAsset $asset): MediaAsset` |
| [RegisterMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/RegisterMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): MediaAsset` |
| [UpdateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateAlbum.php) | `public function handle(Profile $owner, Album $album, array $attributes): Album` |
| [UpdateMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer)`<br>`public function handle(Profile $owner, MediaAsset $asset, array $attributes): MediaAsset` |
| [MediaAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Contracts/MediaAuthorizer.php) | `public function upload(Profile $owner): void`<br>`public function update(Profile $owner): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Album.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/Album.php) | `id`, `owner_profile_id`, `name`, `description`, `privacy`, `cover_path` |
| [MediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/MediaAsset.php) | `id`, `owner_profile_id`, `album_id`, `type`, `state`, `disk`, `path`, `mime_type`, `size`, `checksum`, `alt_text`, `captions`, `rights`, `metadata` |
<!-- layer-implementation-plan:end -->

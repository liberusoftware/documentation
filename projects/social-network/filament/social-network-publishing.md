# Social Network: Social Network Publishing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-publishing). Observed identity: [`liberusoftware/module-social-network-publishing-filament`](../../../modules/source/liberusoftware--module-social-network-publishing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-social-network-publishing-filament`  
**Matching domain module:** `social-network-publishing`  
**Application:** Social Network  
**Source feature:** [Social Network Publishing](../features/social-network-publishing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-publishing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Posts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Articles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drafts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audiences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Edits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mentions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hashtags:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Polls:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-social-network-publishing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `posts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `articles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drafts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audiences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `edits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mentions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hashtags`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `polls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-publishing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-publishing-filament`](https://github.com/liberusoftware/module-social-network-publishing-filament) (`liberusoftware/social-network-publishing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/social-network-publishing.md) · [API plan](../api/social-network-publishing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Posts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `posts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Articles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `articles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drafts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drafts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audiences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audiences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Edits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `edits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mentions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mentions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Hashtags** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hashtags`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Polls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `polls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [Publications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-filament/src/Pages/Publications.php) · [PublishingFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-filament/src/PublishingFilamentPlugin.php) · [PublishingFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-filament/src/PublishingFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/CreatePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, array $attributes): Publication` |
| [DeletePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/DeletePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, Publication $publication): void` |
| [ListPublications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/ListPublications.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishPublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/PublishPublication.php) | `public function __construct(private PublishingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $author, Publication $publication): Publication` |
| [PublishScheduledPublications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/PublishScheduledPublications.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(?Carbon $now = null, int $limit = 100): int` |
| [UpdatePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/UpdatePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $author, Publication $publication, array $attributes): Publication` |
| [UpdatePublicationEnrichments.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/UpdatePublicationEnrichments.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, Publication $publication, array $data): Publication` |
| [PublishingAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Contracts/PublishingAuthorizer.php) | `public function create(Profile $author): void`<br>`public function update(Profile $author, Publication $publication): void`<br>`public function publish(Profile $author, Publication $publication): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Publication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Models/Publication.php) | `id`, `author_profile_id`, `kind`, `state`, `audience`, `title`, `body`, `metadata`, `scheduled_at`, `published_at` |
<!-- layer-implementation-plan:end -->

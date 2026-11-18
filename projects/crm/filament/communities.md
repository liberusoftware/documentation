# CRM: Communities Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communities). Observed identity: [`liberusoftware/module-crm-communities-filament`](../../../modules/source/liberusoftware--module-crm-communities-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-communities-filament`  
**Matching domain module:** `crm-communities`  
**Application:** CRM  
**Source feature:** [Communities](../features/communities.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-communities` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer/partner groups:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Spaces:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Memberships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Posts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Comments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gamification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Knowledge links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CRM profile activity:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-communities-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customer-partner-groups`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `spaces`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `memberships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `posts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `comments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gamification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `knowledge-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `crm-profile-activity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-communities` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-communities-filament`](https://github.com/liberusoftware/module-crm-communities-filament) (`liberusoftware/crm-communities-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/communities.md) · [API plan](../api/communities.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customer/partner groups** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer/partner groups`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Spaces** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `spaces`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Memberships** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `memberships`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Posts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `posts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Comments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `comments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Moderation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `moderation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gamification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gamification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Knowledge links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `knowledge links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **CRM profile activity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `crm profile activity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CommunitiesFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-filament/src/CommunitiesFilamentPlugin.php) · [CommunitiesFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-filament/src/CommunitiesFilamentServiceProvider.php) · [CommunitySpaceResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-filament/src/Resources/CommunitySpaceResource.php) · [CreateCommunitySpacePage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-filament/src/Resources/CommunitySpaceResource/Pages/CreateCommunitySpacePage.php) · [ListCommunitySpaces.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-filament/src/Resources/CommunitySpaceResource/Pages/ListCommunitySpaces.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CommunityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Queries/CommunityQuery.php) | `public function spaces(int $teamId): Builder`<br>`public function feed(int $teamId, int $spaceId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/CreateCommunitySpace.php) | `public function execute(int $teamId, int $ownerId, string $name, string $kind = 'customer', array $settings = []): CommunitySpace` |
| [JoinCommunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/JoinCommunity.php) | `public function execute(int $teamId, CommunitySpace $space, string $subjectKey, string $role = 'member'): CommunityMembership` |
| [PublishCommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/PublishCommunityContent.php) | `public function execute(int $teamId, CommunitySpace $space, string $authorKey, string $body, string $kind = 'post', ?int $parentId = null, array $metadata = []): CommunityContent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityContent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunityMembership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunitySpace.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

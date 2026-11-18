# CMS: Content Access Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-access). Observed identity: [`liberusoftware/module-cms-content-access-filament`](../../../modules/source/liberusoftware--module-cms-content-access-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-content-access-filament`  
**Matching domain module:** `cms-content-access`  
**Application:** CMS  
**Source feature:** [Content Access](../features/content-access.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-access` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Per-site/type/record/field visibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audience rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scheduled access:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Private links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content partitioning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preview authorization:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-content-access-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `per-site-type-record-field-visibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audience-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scheduled-access`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `private-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-partitioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preview-authorization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-access` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-access-filament`](https://github.com/liberusoftware/module-cms-content-access-filament) (`liberusoftware/cms-content-access-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/content-access.md) · [API plan](../api/content-access.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Per-site/type/record/field visibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `per-site/type/record/field visibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audience rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audience rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scheduled access** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scheduled access`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Private links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `private links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content partitioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content partitioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preview authorization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preview authorization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentAccessFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-access-filament/src/ContentAccessFilamentServiceProvider.php) · [AccessRuleResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-access-filament/src/Resources/AccessRuleResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentAccessService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Services/ContentAccessService.php) | `public function rule(string $subjectType, string $subjectKey, array $data = [], ?int $teamId = null): AccessRule`<br>`public function canAccess(string $subjectType, string $subjectKey, ?int $teamId, array $audiences = [], bool $preview = false, ?string $privateToken = null): bool`<br>`public function createPrivateLink(string $subjectType, string $subjectKey, ?int $teamId, ?int $maxUses = null): string`<br>`public function consumePrivateLink(string $token, string $subjectType, string $subjectKey, ?int $teamId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccessRule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Models/AccessRule.php) | `team_id`, `subject_type`, `subject_key`, `visibility`, `audiences`, `fields`, `available_from`, `available_until`, `preview_allowed` |
| [PrivateLink.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Models/PrivateLink.php) | `team_id`, `token_hash`, `subject_type`, `subject_key`, `expires_at`, `uses`, `max_uses`, `revoked_at` |
<!-- layer-implementation-plan:end -->

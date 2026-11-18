# CRM: White Label Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#white-label). Observed identity: [`liberusoftware/module-crm-white-label-filament`](../../../modules/source/liberusoftware--module-crm-white-label-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-white-label-filament`  
**Matching domain module:** `crm-white-label`  
**Application:** CRM  
**Source feature:** [White Label](../features/white-label.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-white-label` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Brand/domain/email/application settings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Theme selection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Custom client experience:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider abstraction:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Safe platform attribution policy:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-white-label-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `brand-domain-email-application-settings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `theme-selection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `custom-client-experience`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-abstraction`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `safe-platform-attribution-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-white-label` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-white-label-filament`](https://github.com/liberusoftware/module-crm-white-label-filament) (`liberusoftware/crm-white-label-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/white-label.md) · [API plan](../api/white-label.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Brand/domain/email/application settings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `brand/domain/email/application settings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Theme selection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `theme selection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Custom client experience** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `custom client experience`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider abstraction** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider abstraction`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Safe platform attribution policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `safe platform attribution policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [WhiteLabelSettingsResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-filament/src/Resources/WhiteLabelSettingsResource.php) · [EditWhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-filament/src/Resources/WhiteLabelSettingsResource/Pages/EditWhiteLabelSettings.php) · [ListWhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-filament/src/Resources/WhiteLabelSettingsResource/Pages/ListWhiteLabelSettings.php) · [WhiteLabelFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-filament/src/WhiteLabelFilamentPlugin.php) · [WhiteLabelFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-filament/src/WhiteLabelFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WhiteLabelSettingsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Queries/WhiteLabelSettingsQuery.php) | `public function forTeam(int $teamId): WhiteLabelSettings` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [UpdateWhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Actions/UpdateWhiteLabelSettings.php) | `public function execute(int $teamId, int $actorId, array $attributes, ?int $expectedVersion = null): WhiteLabelSettings` |
| [WhiteLabelAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Services/WhiteLabelAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $changes): void` |
| [WhiteLabelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Services/WhiteLabelPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WhiteLabelAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Models/WhiteLabelAudit.php) | `team_id`, `actor_id`, `event`, `changes`, `request_id` |
| [WhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Models/WhiteLabelSettings.php) | `team_id`, `brand_name`, `custom_domain`, `theme`, `email_settings`, `application_settings`, `client_experience`, `provider`, `show_platform_attribution`, `version` |
<!-- layer-implementation-plan:end -->

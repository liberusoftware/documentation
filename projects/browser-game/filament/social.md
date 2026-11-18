# Browser Game: Social Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social). Observed identity: [`liberusoftware/module-browser-game-social-filament`](../../../modules/source/liberusoftware--module-browser-game-social-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-social-filament`  
**Matching domain module:** `browser-game-social`  
**Application:** Browser Game  
**Source feature:** [Social](../features/social.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-social` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Friends:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Parties:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Chat:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mail:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Guilds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alliances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Permissions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Activity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-social-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `friends`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `parties`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `chat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mail`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `guilds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alliances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `permissions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `activity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-social` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-social-filament`](https://github.com/liberusoftware/module-browser-game-social-filament) (`liberusoftware/browser-game-social-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/social.md) · [API plan](../api/social.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Friends** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `friends`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Parties** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `parties`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Chat** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `chat`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mail** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mail`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Guilds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `guilds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Alliances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `alliances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Permissions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permissions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Activity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `activity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SocialResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-filament/src/Resources/SocialResource.php) · [CreateSocial.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-filament/src/Resources/SocialResource/Pages/CreateSocial.php) · [EditSocial.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-filament/src/Resources/SocialResource/Pages/EditSocial.php) · [ListSocial.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-filament/src/Resources/SocialResource/Pages/ListSocial.php) · [SocialFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-filament/src/SocialFilamentPlugin.php) · [SocialFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-filament/src/SocialFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SocialQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Queries/SocialQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SocialActivity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialActivity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialMembership.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

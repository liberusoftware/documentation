# Browser Game: Browser Game Accounts Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-accounts). Observed identity: [`liberusoftware/module-browser-game-accounts-filament`](../../../modules/source/liberusoftware--module-browser-game-accounts-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-browser-game-accounts-filament`  
**Matching domain module:** `browser-game-accounts`  
**Application:** Browser Game  
**Source feature:** [Browser Game Accounts](../features/browser-game-accounts.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-accounts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Player identity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sessions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Age/region policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recovery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Privacy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-browser-game-accounts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `player-identity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sessions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `age-region-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `privacy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-accounts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-accounts-filament`](https://github.com/liberusoftware/module-browser-game-accounts-filament) (`liberusoftware/browser-game-accounts-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/browser-game-accounts.md) · [API plan](../api/browser-game-accounts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Player identity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `player identity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sessions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sessions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Age/region policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `age/region policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Privacy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `privacy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountsFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-filament/src/AccountsFilamentPlugin.php) · [AccountsFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-filament/src/AccountsFilamentServiceProvider.php) · [AccountsResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-filament/src/Resources/AccountsResource.php) · [CreateAccount.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-filament/src/Resources/AccountsResource/Pages/CreateAccount.php) · [EditAccount.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-filament/src/Resources/AccountsResource/Pages/EditAccount.php) · [ListAccounts.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-filament/src/Resources/AccountsResource/Pages/ListAccounts.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AccountsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Queries/AccountsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountBan.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountBan.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountPrivacy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountPrivacy.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountRecovery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountRecovery.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountSession.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountSession.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

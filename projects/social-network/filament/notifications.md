# Social Network: Notifications Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#notifications). Observed identity: [`liberusoftware/module-social-network-notifications-filament`](../../../modules/source/liberusoftware--module-social-network-notifications-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-notifications-filament`  
**Matching domain module:** `social-network-notifications`  
**Application:** Social Network  
**Source feature:** [Notifications](../features/notifications.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-notifications` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Preferences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **In-app/email/push delivery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Digests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quiet hours:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Read state:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-notifications-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `in-app-email-push-delivery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `digests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quiet-hours`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `read-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-notifications` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-notifications-filament`](https://github.com/liberusoftware/module-notifications-filament) (`liberusoftware/notifications-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/notifications.md) · [API plan](../api/notifications.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Preferences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preferences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **In-app/email/push delivery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `in-app/email/push delivery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Grouping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `grouping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Digests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `digests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quiet hours** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quiet hours`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Read state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `read state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [NotificationsFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-filament/src/NotificationsFilamentPlugin.php) · [NotificationsFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-filament/src/NotificationsFilamentServiceProvider.php) · [Notifications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-filament/src/Pages/Notifications.php).
<!-- layer-implementation-plan:end -->

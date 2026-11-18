# Browser Game: Browser Game Commerce Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-commerce). Observed identity: [`liberusoftware/module-browser-game-commerce-filament`](../../../modules/source/liberusoftware--module-browser-game-commerce-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-browser-game-commerce-filament`  
**Matching domain module:** `browser-game-commerce`  
**Application:** Browser Game  
**Source feature:** [Browser Game Commerce](../features/browser-game-commerce.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-commerce` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Premium membership:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Entitlements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Store:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Regional pricing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Receipts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refunds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Parental controls:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-browser-game-commerce-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `premium-membership`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `entitlements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `store`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `regional-pricing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `receipts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refunds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `parental-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-commerce` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-commerce-filament`](https://github.com/liberusoftware/module-browser-game-commerce-filament) (`liberusoftware/browser-game-commerce-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/browser-game-commerce.md) · [API plan](../api/browser-game-commerce.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Premium membership** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `premium membership`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Entitlements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entitlements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Store** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `store`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Regional pricing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regional pricing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Receipts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `receipts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Refunds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `refunds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Parental controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `parental controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CommerceFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-filament/src/CommerceFilamentPlugin.php) · [CommerceFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-filament/src/CommerceFilamentServiceProvider.php) · [CommerceResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-filament/src/Resources/CommerceResource.php) · [CreateCommerce.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-filament/src/Resources/CommerceResource/Pages/CreateCommerce.php) · [EditCommerce.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-filament/src/Resources/CommerceResource/Pages/EditCommerce.php) · [ListCommerce.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-filament/src/Resources/CommerceResource/Pages/ListCommerce.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CommerceQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Queries/CommerceQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommerceEntitlement.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrder.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrderLine.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrderLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceProduct.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceProduct.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

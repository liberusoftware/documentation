# Real Estate: Real Estate Zoopla Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-zoopla). Observed identity: [`liberusoftware/real-estate-zoopla-filament`](../../../modules/source/liberusoftware--real-estate-zoopla-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-real-estate-zoopla-filament`  
**Matching domain module:** `real-estate-zoopla`  
**Application:** Real Estate  
**Source feature:** [Real Estate Zoopla](../features/real-estate-zoopla.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-zoopla` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Zoopla sync state:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider payload boundary:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retry and error state:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-real-estate-zoopla-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `zoopla-sync-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-payload-boundary`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retry-and-error-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-zoopla` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-zoopla-filament`](https://github.com/liberusoftware/module-real-estate-zoopla-filament) (`liberusoftware/real-estate-zoopla-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/real-estate-zoopla.md) · [API plan](../api/real-estate-zoopla.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Zoopla sync state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `zoopla sync state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider payload boundary** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider payload boundary`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retry and error state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retry and error state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ZooplaSyncResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-filament/src/Resources/ZooplaSyncResource.php) · [CreateZooplaSync.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-filament/src/Resources/ZooplaSyncResource/Pages/CreateZooplaSync.php) · [EditZooplaSync.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-filament/src/Resources/ZooplaSyncResource/Pages/EditZooplaSync.php) · [ListZooplaSyncs.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-filament/src/Resources/ZooplaSyncResource/Pages/ListZooplaSyncs.php) · [ZooplaFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-filament/src/ZooplaFilamentPlugin.php) · [ZooplaFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla-filament/src/ZooplaFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ZooplaTransport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla/src/Contracts/ZooplaTransport.php) | `public function sendProperty(string $reference, array $payload, array $credentials): array`<br>`public function removeProperty(string $reference, array $credentials): array`<br>`public function branchPropertyList(array $credentials): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ZooplaSync.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-zoopla/src/Models/ZooplaSync.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

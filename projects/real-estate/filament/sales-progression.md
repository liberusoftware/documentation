# Real Estate: Sales Progression Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-progression). Observed identity: [`liberusoftware/real-estate-sales-progression-filament`](../../../modules/source/liberusoftware--real-estate-sales-progression-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-sales-progression-filament`  
**Matching domain module:** `real-estate-sales-progression`  
**Application:** Real Estate  
**Source feature:** [Sales Progression](../features/sales-progression.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-sales-progression` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Chain:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Milestones:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Memoranda:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Legal/finance contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Risks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Completion:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-sales-progression-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `chain`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `milestones`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `memoranda`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `legal-finance-contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `risks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `completion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-sales-progression` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-sales-progression-filament`](https://github.com/liberusoftware/module-real-estate-sales-progression-filament) (`liberusoftware/real-estate-sales-progression-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sales-progression.md) · [API plan](../api/sales-progression.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Chain** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `chain`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Milestones** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `milestones`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Memoranda** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `memoranda`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Legal/finance contacts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `legal/finance contacts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Risks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `risks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Completion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `completion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SalesProgressionResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-filament/src/Resources/SalesProgressionResource.php) · [CreateSalesProgression.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-filament/src/Resources/SalesProgressionResource/Pages/CreateSalesProgression.php) · [EditSalesProgression.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-filament/src/Resources/SalesProgressionResource/Pages/EditSalesProgression.php) · [ListSalesProgressions.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-filament/src/Resources/SalesProgressionResource/Pages/ListSalesProgressions.php) · [SalesProgressionFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-filament/src/SalesProgressionFilamentPlugin.php) · [SalesProgressionFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression-filament/src/SalesProgressionFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SalesProgressionPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression/src/Policies/SalesProgressionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function delete(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function forceDelete(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, SalesProgression $salesProgression): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesProgression.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-sales-progression/src/Models/SalesProgression.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

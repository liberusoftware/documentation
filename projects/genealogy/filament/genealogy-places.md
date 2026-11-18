# Genealogy: Genealogy Places Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-places). Observed identity: [`liberusoftware/module-genealogy-places-filament`](../../../modules/source/liberusoftware--module-genealogy-places-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-genealogy-places-filament`  
**Matching domain module:** `genealogy-places`  
**Application:** Genealogy  
**Source feature:** [Genealogy Places](../features/genealogy-places.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-places` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Historical/current place hierarchy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Names over time:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coordinates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Jurisdictions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Maps:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-genealogy-places-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `historical-current-place-hierarchy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `names-over-time`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coordinates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `jurisdictions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `maps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-places` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-places-filament`](https://github.com/liberusoftware/module-genealogy-places-filament) (`liberusoftware/genealogy-places-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/genealogy-places.md) · [API plan](../api/genealogy-places.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Historical/current place hierarchy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `historical/current place hierarchy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Names over time** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `names over time`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coordinates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coordinates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Jurisdictions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `jurisdictions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Maps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `maps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PlacesFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places-filament/src/PlacesFilamentServiceProvider.php) · [PlaceResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places-filament/src/Resources/PlaceResource.php) · [CreatePlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places-filament/src/Resources/PlaceResource/Pages/CreatePlace.php) · [EditPlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places-filament/src/Resources/PlaceResource/Pages/EditPlace.php) · [ListPlaces.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places-filament/src/Resources/PlaceResource/Pages/ListPlaces.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PlaceHierarchy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Queries/PlaceHierarchy.php) | `public function execute(bool $flat = false): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/CreatePlace.php) | `public function execute(array $attributes): Place`<br>`public function validate(array $values): void` |
| [CreatePlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/CreatePlaceName.php) | `public function execute(array $attributes): PlaceName`<br>`public function validate(array $values): void` |
| [DeletePlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/DeletePlace.php) | `public function execute(Place $place): void` |
| [DeletePlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/DeletePlaceName.php) | `public function execute(PlaceName $placeName): void` |
| [UpdatePlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/UpdatePlace.php) | `public function execute(Place $place, array $attributes): Place` |
| [UpdatePlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/UpdatePlaceName.php) | `public function execute(PlaceName $placeName, array $attributes): PlaceName` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Place.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Models/Place.php) | `team_id`, `name`, `parent_id`, `historical_names`, `latitude`, `longitude`, `jurisdiction`, `is_current`, `status`, `metadata` |
| [PlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Models/PlaceName.php) | `team_id`, `place_id`, `name`, `type`, `locale`, `valid_from`, `valid_to`, `metadata` |
<!-- layer-implementation-plan:end -->

# Real Estate: Real Estate Offers Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-offers). Observed identity: [`liberusoftware/real-estate-offers-filament`](../../../modules/source/liberusoftware--real-estate-offers-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-real-estate-offers-filament`  
**Matching domain module:** `real-estate-offers`  
**Application:** Real Estate  
**Source feature:** [Real Estate Offers](../features/real-estate-offers.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-offers` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Terms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Qualification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Negotiation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Proof:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Decision history:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accepted-offer controls:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-real-estate-offers-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `terms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `qualification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `negotiation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `proof`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `decision-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accepted-offer-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-offers` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-offers-filament`](https://github.com/liberusoftware/module-real-estate-offers-filament) (`liberusoftware/real-estate-offers-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/real-estate-offers.md) · [API plan](../api/real-estate-offers.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Terms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Qualification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `qualification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Negotiation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `negotiation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Proof** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `proof`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Decision history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `decision history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accepted-offer controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accepted-offer controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OffersFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-filament/src/OffersFilamentPlugin.php) · [OffersFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-filament/src/OffersFilamentServiceProvider.php) · [OfferResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-filament/src/Resources/OfferResource.php) · [CreateOffer.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-filament/src/Resources/OfferResource/Pages/CreateOffer.php) · [EditOffer.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-filament/src/Resources/OfferResource/Pages/EditOffer.php) · [ListOffers.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-filament/src/Resources/OfferResource/Pages/ListOffers.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OfferPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Policies/OfferPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Offer $offer): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Offer $offer): bool`<br>`public function delete(AuthUser $authUser, Offer $offer): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Offer $offer): bool`<br>`public function forceDelete(AuthUser $authUser, Offer $offer): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Offer $offer): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Offer.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Models/Offer.php) | No literal fillable array detected; inspect the model and API schema. |
| [OfferEvent.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Models/OfferEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

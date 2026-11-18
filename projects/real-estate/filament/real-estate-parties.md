# Real Estate: Real Estate Parties Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-parties). Observed identity: [`liberusoftware/real-estate-parties-filament`](../../../modules/source/liberusoftware--real-estate-parties-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-real-estate-parties-filament`  
**Matching domain module:** `real-estate-parties`  
**Application:** Real Estate  
**Source feature:** [Real Estate Parties](../features/real-estate-parties.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-parties` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Applicants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Vendors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Landlords:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tenants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Buyers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Solicitors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contractors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relationships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-real-estate-parties-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `applicants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `vendors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `landlords`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tenants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `buyers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `solicitors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contractors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relationships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-parties` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-parties-filament`](https://github.com/liberusoftware/module-real-estate-parties-filament) (`liberusoftware/real-estate-parties-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/real-estate-parties.md) · [API plan](../api/real-estate-parties.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Applicants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `applicants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Vendors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `vendors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Landlords** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `landlords`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tenants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tenants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Buyers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `buyers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Solicitors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `solicitors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contractors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contractors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Relationships** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `relationships`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PartiesFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-filament/src/PartiesFilamentPlugin.php) · [PartiesFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-filament/src/PartiesFilamentServiceProvider.php) · [PartyResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-filament/src/Resources/PartyResource.php) · [CreateParty.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-filament/src/Resources/PartyResource/Pages/CreateParty.php) · [EditParty.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-filament/src/Resources/PartyResource/Pages/EditParty.php) · [ListParties.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-filament/src/Resources/PartyResource/Pages/ListParties.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PartyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Policies/PartyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Party $party): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Party $party): bool`<br>`public function delete(AuthUser $authUser, Party $party): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Party $party): bool`<br>`public function forceDelete(AuthUser $authUser, Party $party): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Party $party): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contact.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Contact.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactMessage.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/ContactMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [Party.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Party.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyRelationship.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyRelationship.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyReview.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

# Real Estate: Lettings Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#lettings). Observed identity: [`liberusoftware/real-estate-lettings-filament`](../../../modules/source/liberusoftware--real-estate-lettings-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-lettings-filament`  
**Matching domain module:** `real-estate-lettings`  
**Application:** Real Estate  
**Source feature:** [Lettings](../features/lettings.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-lettings` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Applications:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Referencing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deposits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Agreements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Move-in/out:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rent changes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Notices:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-lettings-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `applications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `referencing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deposits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `agreements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `move-in-out`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rent-changes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `notices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-lettings` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-lettings-filament`](https://github.com/liberusoftware/module-real-estate-lettings-filament) (`liberusoftware/real-estate-lettings-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/lettings.md) · [API plan](../api/lettings.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Applications** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `applications`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Referencing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `referencing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deposits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deposits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Agreements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agreements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Move-in/out** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `move-in/out`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renewals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renewals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rent changes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rent changes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Notices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `notices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [LettingsFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/LettingsFilamentPlugin.php) · [LettingsFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/LettingsFilamentServiceProvider.php) · [LettingResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/LettingResource.php) · [CreateLetting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/LettingResource/Pages/CreateLetting.php) · [EditLetting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/LettingResource/Pages/EditLetting.php) · [ListLettings.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/LettingResource/Pages/ListLettings.php) · [RentalApplicationResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/RentalApplicationResource.php) · [CreateRentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/RentalApplicationResource/Pages/CreateRentalApplication.php) · [EditRentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/RentalApplicationResource/Pages/EditRentalApplication.php) · [ListRentalApplications.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-filament/src/Resources/RentalApplicationResource/Pages/ListRentalApplications.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListLettings.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Queries/ListLettings.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [LettingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Policies/LettingPolicy.php) | `public function view($user, Letting $letting): bool`<br>`public function update($user, Letting $letting): bool`<br>`public function delete($user, Letting $letting): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LeaseAgreement.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/LeaseAgreement.php) | No literal fillable array detected; inspect the model and API schema. |
| [Letting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/Letting.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalApplication.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalCharge.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalCharge.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

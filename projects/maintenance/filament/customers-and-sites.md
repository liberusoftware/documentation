# Maintenance: Customers and Sites Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customers-and-sites). Observed identity: [`liberusoftware/module-maintenance-customers-and-sites-filament`](../../../modules/source/liberusoftware--module-maintenance-customers-and-sites-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-customers-and-sites-filament`  
**Matching domain module:** `maintenance-customers-and-sites`  
**Application:** Maintenance  
**Source feature:** [Customers and Sites](../features/customers-and-sites.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `maintenance-customers-and-sites` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sites:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Access details:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hazards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Service windows:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-customers-and-sites-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sites`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `access-details`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hazards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `service-windows`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `maintenance-customers-and-sites` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-customers-and-sites-filament`](https://github.com/liberusoftware/module-maintenance-customers-and-sites-filament) (`liberusoftware/maintenance-customers-and-sites-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/customers-and-sites.md) · [API plan](../api/customers-and-sites.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contacts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contacts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sites** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sites`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Access details** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `access details`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Hazards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hazards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Service windows** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `service windows`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomersAndSitesFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/CustomersAndSitesFilamentPlugin.php) · [CustomersAndSitesFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/CustomersAndSitesFilamentServiceProvider.php) · [CustomerResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource.php) · [CreateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource/Pages/CreateCustomer.php) · [EditCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource/Pages/EditCustomer.php) · [ListCustomers.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource/Pages/ListCustomers.php) · [SiteResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource.php) · [CreateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource/Pages/CreateSite.php) · [EditSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource/Pages/EditSite.php) · [ListSites.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource/Pages/ListSites.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateCustomer.php) | `public function handle(int $teamId, array $attributes): Customer` |
| [CreateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateSite.php) | `public function handle(int $teamId, array $attributes): Site` |
| [DeleteCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteCustomer.php) | `public function handle(int $teamId, Customer $customer): void` |
| [DeleteSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteSite.php) | `public function handle(int $teamId, Site $site): void` |
| [UpdateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateCustomer.php) | `public function handle(int $teamId, Customer $customer, array $attributes): Customer` |
| [UpdateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateSite.php) | `public function handle(int $teamId, Site $site, array $attributes): Site` |
| [CustomerPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/CustomerPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Customer $customer): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Customer $customer): bool`<br>`public function delete(object $user, Customer $customer): bool` |
| [SitePolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/SitePolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Site $site): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Site $site): bool`<br>`public function delete(object $user, Site $site): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Customer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Customer.php) | `team_id`, `name`, `code`, `email`, `phone`, `address`, `city`, `state`, `zip`, `website`, `industry`, `description`, `type`, `contact_person`, `payment_terms`, `notes`, `is_active` |
| [Site.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Site.php) | `team_id`, `customer_id`, `name`, `code`, `address`, `access_details`, `hazards`, `is_active` |
<!-- layer-implementation-plan:end -->

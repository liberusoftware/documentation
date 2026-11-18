# CMS: Cms Contact Directory Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-contact-directory). Observed identity: [`liberusoftware/module-cms-contact-directory-filament`](../../../modules/source/liberusoftware--module-cms-contact-directory-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-contact-directory-filament`  
**Matching domain module:** `cms-contact-directory`  
**Application:** CMS  
**Source feature:** [Cms Contact Directory](../features/cms-contact-directory.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-contact-directory` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **People/departments/contact records:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Categories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contact forms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Protected fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Directory views:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-contact-directory-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `people-departments-contact-records`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `categories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contact-forms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `protected-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `directory-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-contact-directory` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-contact-directory-filament`](https://github.com/liberusoftware/module-cms-contact-directory-filament) (`liberusoftware/cms-contact-directory-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-contact-directory.md) · [API plan](../api/cms-contact-directory.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **People/departments/contact records** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `people/departments/contact records`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Categories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `categories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contact forms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contact forms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Protected fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `protected fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Directory views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `directory views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContactDirectoryFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-contact-directory-filament/src/ContactDirectoryFilamentServiceProvider.php) · [ContactResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-contact-directory-filament/src/Resources/ContactResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContactDirectoryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Services/ContactDirectoryService.php) | `public function contacts(?int $teamId, bool $publicOnly = false, int $perPage = 25): LengthAwarePaginator`<br>`public function saveContact(array $data, ?int $teamId = null): Contact`<br>`public function category(array $data, ?int $teamId = null): ContactCategory`<br>`public function location(array $data, ?int $teamId = null): ContactLocation`<br>`public function form(array $data, ?int $teamId = null): ContactForm` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contact.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/Contact.php) | `team_id`, `category_id`, `location_id`, `name`, `department`, `email`, `phone`, `details`, `is_public` |
| [ContactCategory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/ContactCategory.php) | `team_id`, `name`, `slug` |
| [ContactForm.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/ContactForm.php) | `team_id`, `name`, `schema`, `is_active` |
| [ContactLocation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/ContactLocation.php) | `team_id`, `name`, `address`, `city`, `country` |
<!-- layer-implementation-plan:end -->

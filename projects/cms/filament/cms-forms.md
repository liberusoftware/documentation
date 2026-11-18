# CMS: Cms Forms Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-forms). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-forms-filament`  
**Matching domain module:** `cms-forms`  
**Application:** CMS  
**Source feature:** [Cms Forms](../features/cms-forms.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-forms` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Form schema builder:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Multi-step and conditional fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Spam and rate-limit protection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent and retention tracking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Submission inbox and exports:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-forms-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `form-schema-builder`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `multi-step-and-conditional-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `spam-and-rate-limit-protection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent-and-retention-tracking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `submission-inbox-and-exports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-forms` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-forms-filament`](https://github.com/liberusoftware/module-cms-forms-filament) (`liberusoftware/cms-forms-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-forms.md) · [API plan](../api/cms-forms.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Form schema builder** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `form schema builder`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Multi-step and conditional fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `multi-step and conditional fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Spam and rate-limit protection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `spam and rate-limit protection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent and retention tracking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent and retention tracking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Submission inbox and exports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `submission inbox and exports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FormResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/FormResource.php) · [FormSubmissionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/FormSubmissionResource.php) · [ListFormSubmissions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/Pages/ListFormSubmissions.php) · [ListForms.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/Pages/ListForms.php).

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Form.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Models/Form.php) | `name`, `slug`, `fields`, `team_id` |
| [FormSubmission.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Models/FormSubmission.php) | `form_id`, `data`, `meta`, `team_id` |
<!-- layer-implementation-plan:end -->

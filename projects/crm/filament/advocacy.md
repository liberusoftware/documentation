# CRM: Advocacy Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#advocacy). Observed identity: [`liberusoftware/module-crm-advocacy-filament`](../../../modules/source/liberusoftware--module-crm-advocacy-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-advocacy-filament`  
**Matching domain module:** `crm-advocacy`  
**Application:** CRM  
**Source feature:** [Advocacy](../features/advocacy.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-advocacy` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **References:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Testimonials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reviews:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Case-study consent:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Speakers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Advisory boards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Nominations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recognition history:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-advocacy-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `testimonials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reviews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `case-study-consent`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `speakers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `advisory-boards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `nominations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recognition-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-advocacy` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-advocacy-filament`](https://github.com/liberusoftware/module-crm-advocacy-filament) (`liberusoftware/crm-advocacy-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/advocacy.md) · [API plan](../api/advocacy.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **References** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Testimonials** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `testimonials`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reviews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reviews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Case-study consent** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `case-study consent`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Speakers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `speakers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Advisory boards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `advisory boards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Nominations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `nominations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Requests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recognition history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recognition history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AdvocacyFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-filament/src/AdvocacyFilamentPlugin.php) · [AdvocacyFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-filament/src/AdvocacyFilamentServiceProvider.php) · [AdvocacyRecordResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-filament/src/Resources/AdvocacyRecordResource.php) · [CreateAdvocacyRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-filament/src/Resources/Pages/CreateAdvocacyRecord.php) · [EditAdvocacyRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-filament/src/Resources/Pages/EditAdvocacyRecord.php) · [ListAdvocacyRecords.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-filament/src/Resources/Pages/ListAdvocacyRecords.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AdvocacyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Queries/AdvocacyQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvocacyRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvocacyRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AdvocacyRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Models/AdvocacyRecord.php) | `team_id`, `kind`, `name`, `status`, `contact_id`, `owner_id`, `payload`, `requested_at`, `approved_at`, `completed_at` |
<!-- layer-implementation-plan:end -->

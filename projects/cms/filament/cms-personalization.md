# CMS: Cms Personalization Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-personalization). Observed identity: [`liberusoftware/module-cms-personalization-filament`](../../../modules/source/liberusoftware--module-cms-personalization-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-personalization-filament`  
**Matching domain module:** `cms-personalization`  
**Application:** CMS  
**Source feature:** [Cms Personalization](../features/cms-personalization.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-personalization` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Audience/context rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Variants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Eligibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Priority:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fallback:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Holdouts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Decision evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-personalization-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `audience-context-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `variants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `eligibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `priority`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fallback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `holdouts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `decision-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-personalization` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-personalization-filament`](https://github.com/liberusoftware/module-cms-personalization-filament) (`liberusoftware/cms-personalization-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-personalization.md) · [API plan](../api/cms-personalization.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Audience/context rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audience/context rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Variants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `variants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Eligibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `eligibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Priority** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `priority`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fallback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fallback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Holdouts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `holdouts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Decision evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `decision evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PersonalizationFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-personalization-filament/src/PersonalizationFilamentServiceProvider.php) · [AudienceResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-personalization-filament/src/Resources/AudienceResource.php) · [EditAudience.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-personalization-filament/src/Resources/Pages/EditAudience.php) · [ListAudiences.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-personalization-filament/src/Resources/Pages/ListAudiences.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DecisionEngine.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Services/DecisionEngine.php) | `public function decide(string $audienceKey, array $context = [], ?string $subjectKey = null, bool $consent = false): array` |
| [PersonalizationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Services/PersonalizationService.php) | `public function createAudience(array $attributes, ?int $teamId = null): Audience`<br>`public function updateAudience(Audience $audience, array $attributes): Audience`<br>`public function saveVariant(Audience $audience, array $attributes, ?Variant $variant = null): Variant`<br>`public function deleteVariant(Variant $variant): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Audience.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Models/Audience.php) | `name`, `key`, `rules`, `requires_consent`, `active`, `team_id` |
| [Decision.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Models/Decision.php) | `audience_key`, `variant_key`, `subject_key`, `context`, `reason`, `team_id` |
| [Variant.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Models/Variant.php) | `audience_id`, `key`, `payload`, `priority`, `holdout_percent`, `fallback`, `active`, `team_id` |
<!-- layer-implementation-plan:end -->

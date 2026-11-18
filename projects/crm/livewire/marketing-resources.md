# CRM: Marketing Resources Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing-resources). Observed identity: [`liberusoftware/module-crm-marketing-resources-livewire`](../../../modules/source/liberusoftware--module-crm-marketing-resources-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-marketing-resources-livewire`  
**Matching domain module:** `crm-marketing-resources`  
**Application:** CRM  
**Source feature:** [Marketing Resources](../features/marketing-resources.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Brand kits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reusable content blocks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Campaign files:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approvals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Usage rights:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **CMS/media references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-marketing-resources-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-marketing-resources::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `brand-kits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reusable-content-blocks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `campaign-files`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approvals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `usage-rights`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cms-media-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-marketing-resources` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/marketing-resources.md) · [API plan](../api/marketing-resources.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Brand kits** | Expose a focused Livewire 4 component and namespaced Blade default view for `brand kits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reusable content blocks** | Expose a focused Livewire 4 component and namespaced Blade default view for `reusable content blocks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Campaign files** | Expose a focused Livewire 4 component and namespaced Blade default view for `campaign files` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Templates** | Expose a focused Livewire 4 component and namespaced Blade default view for `templates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approvals** | Expose a focused Livewire 4 component and namespaced Blade default view for `approvals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Usage rights** | Expose a focused Livewire 4 component and namespaced Blade default view for `usage rights` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **CMS/media references** | Expose a focused Livewire 4 component and namespaced Blade default view for `cms/media references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ResourceLibrary.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources-livewire/src/Components/ResourceLibrary.php) · [MarketingResourcesLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources-livewire/src/MarketingResourcesLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [MarketingResourceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources/src/Queries/MarketingResourceQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMarketingResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources/src/Actions/CreateMarketingResource.php) | `public function __construct(private readonly MarketingResourcePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MarketingResource` |
| [RecordResourceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources/src/Actions/RecordResourceEvent.php) | `public function __construct(private readonly MarketingResourcePolicy $policy)`<br>`public function execute(int $teamId, int $userId, MarketingResource $resource, array $input): MarketingResourceEvent` |
| [MarketingResourcePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources/src/Services/MarketingResourcePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MarketingResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources/src/Models/MarketingResource.php) | No literal fillable array detected; inspect the model and API schema. |
| [MarketingResourceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-resources/src/Models/MarketingResourceEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

# CRM: Knowledge Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#knowledge). Observed identity: [`liberusoftware/module-crm-knowledge-livewire`](../../../modules/source/liberusoftware--module-crm-knowledge-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-knowledge-livewire`  
**Matching domain module:** `crm-knowledge`  
**Application:** CRM  
**Source feature:** [Knowledge](../features/knowledge.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Internal/public articles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Categories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Versions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Review/approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Localization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Feedback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Case linking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Suggested answers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Stale-content controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-knowledge-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-knowledge::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `internal-public-articles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `categories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `versions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `review-approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `localization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `feedback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `case-linking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `suggested-answers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `stale-content-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-knowledge` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/knowledge.md) · [API plan](../api/knowledge.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Internal/public articles** | Expose a focused Livewire 4 component and namespaced Blade default view for `internal/public articles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Categories** | Expose a focused Livewire 4 component and namespaced Blade default view for `categories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Versions** | Expose a focused Livewire 4 component and namespaced Blade default view for `versions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Review/approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `review/approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Localization** | Expose a focused Livewire 4 component and namespaced Blade default view for `localization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Search** | Expose a focused Livewire 4 component and namespaced Blade default view for `search` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Feedback** | Expose a focused Livewire 4 component and namespaced Blade default view for `feedback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Case linking** | Expose a focused Livewire 4 component and namespaced Blade default view for `case linking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Suggested answers** | Expose a focused Livewire 4 component and namespaced Blade default view for `suggested answers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Stale-content controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `stale-content controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [KnowledgeSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge-livewire/src/Components/KnowledgeSearch.php) · [KnowledgeLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge-livewire/src/KnowledgeLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [KnowledgeQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge/src/Queries/KnowledgeQuery.php) | `public function forTeam(int $teamId, ?string $search = null)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateArticle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge/src/Actions/CreateArticle.php) | `public function __construct(private readonly KnowledgePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): KnowledgeArticle` |
| [RecordKnowledgeEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge/src/Actions/RecordKnowledgeEvent.php) | `public function __construct(private readonly KnowledgePolicy $policy)`<br>`public function execute(int $teamId, int $userId, KnowledgeArticle $article, array $input): KnowledgeEvent` |
| [KnowledgePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge/src/Services/KnowledgePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [KnowledgeArticle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge/src/Models/KnowledgeArticle.php) | No literal fillable array detected; inspect the model and API schema. |
| [KnowledgeEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge/src/Models/KnowledgeEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [KnowledgeVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-knowledge/src/Models/KnowledgeVersion.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

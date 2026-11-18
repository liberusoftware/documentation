# CRM: Communities Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communities). Observed identity: [`liberusoftware/module-crm-communities-livewire`](../../../modules/source/liberusoftware--module-crm-communities-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-communities-livewire`  
**Matching domain module:** `crm-communities`  
**Application:** CRM  
**Source feature:** [Communities](../features/communities.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Customer/partner groups:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Spaces:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Memberships:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Posts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Comments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Moderation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gamification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Knowledge links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **CRM profile activity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-communities-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-communities::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `customer-partner-groups`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `spaces`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `memberships`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `posts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `comments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `moderation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gamification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `knowledge-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `crm-profile-activity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-communities` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/communities.md) · [API plan](../api/communities.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Customer/partner groups** | Expose a focused Livewire 4 component and namespaced Blade default view for `customer/partner groups` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Spaces** | Expose a focused Livewire 4 component and namespaced Blade default view for `spaces` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Memberships** | Expose a focused Livewire 4 component and namespaced Blade default view for `memberships` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Posts** | Expose a focused Livewire 4 component and namespaced Blade default view for `posts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Comments** | Expose a focused Livewire 4 component and namespaced Blade default view for `comments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Events** | Expose a focused Livewire 4 component and namespaced Blade default view for `events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Moderation** | Expose a focused Livewire 4 component and namespaced Blade default view for `moderation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gamification** | Expose a focused Livewire 4 component and namespaced Blade default view for `gamification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Knowledge links** | Expose a focused Livewire 4 component and namespaced Blade default view for `knowledge links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **CRM profile activity** | Expose a focused Livewire 4 component and namespaced Blade default view for `crm profile activity` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CommunitiesLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-livewire/src/CommunitiesLivewireServiceProvider.php) · [CommunityBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-livewire/src/Components/CommunityBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CommunityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Queries/CommunityQuery.php) | `public function spaces(int $teamId): Builder`<br>`public function feed(int $teamId, int $spaceId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/CreateCommunitySpace.php) | `public function execute(int $teamId, int $ownerId, string $name, string $kind = 'customer', array $settings = []): CommunitySpace` |
| [JoinCommunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/JoinCommunity.php) | `public function execute(int $teamId, CommunitySpace $space, string $subjectKey, string $role = 'member'): CommunityMembership` |
| [PublishCommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/PublishCommunityContent.php) | `public function execute(int $teamId, CommunitySpace $space, string $authorKey, string $body, string $kind = 'post', ?int $parentId = null, array $metadata = []): CommunityContent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityContent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunityMembership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunitySpace.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

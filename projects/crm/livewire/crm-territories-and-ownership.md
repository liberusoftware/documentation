# CRM: Crm Territories And Ownership Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-territories-and-ownership). Observed identity: [`liberusoftware/module-crm-territories-and-ownership-livewire`](../../../modules/source/liberusoftware--module-crm-territories-and-ownership-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-territories-and-ownership-livewire`  
**Matching domain module:** `crm-territories-and-ownership`  
**Application:** CRM  
**Source feature:** [Crm Territories And Ownership](../features/crm-territories-and-ownership.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Territories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Books of business:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Teams:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assignment rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Round-robin/capacity routing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Temporary coverage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ownership history:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-territories-and-ownership-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmTerritoriesAndOwnership::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `territories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `books-of-business`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `teams`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assignment-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `round-robin-capacity-routing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `temporary-coverage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ownership-history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-territories-and-ownership` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-territories-and-ownership.md) · [API plan](../api/crm-territories-and-ownership.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Territories** | Expose a focused Livewire 4 component and namespaced Blade default view for `territories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Books of business** | Expose a focused Livewire 4 component and namespaced Blade default view for `books of business` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Teams** | Expose a focused Livewire 4 component and namespaced Blade default view for `teams` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Assignment rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `assignment rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Round-robin/capacity routing** | Expose a focused Livewire 4 component and namespaced Blade default view for `round-robin/capacity routing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Temporary coverage** | Expose a focused Livewire 4 component and namespaced Blade default view for `temporary coverage` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ownership history** | Expose a focused Livewire 4 component and namespaced Blade default view for `ownership history` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [TerritoryDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership-livewire/src/Components/TerritoryDashboard.php) · [TerritoriesAndOwnershipLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership-livewire/src/TerritoriesAndOwnershipLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [TerritoryQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Queries/TerritoryQuery.php) | `public function rules(int $teamId): LengthAwarePaginator`<br>`public function history(int $teamId): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignOwner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/AssignOwner.php) | `public function execute(int $teamId, int $actorId, string $subjectType, int $subjectId, ?int $previousOwnerId, int $ownerId, string $reason): OwnershipHistory` |
| [CreateCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/CreateCoverage.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryCoverage` |
| [UpsertTerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/UpsertTerritoryRule.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryRule` |
| [TerritoryPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Services/TerritoryPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [OwnershipHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/OwnershipHistory.php) | `team_id`, `subject_type`, `subject_id`, `previous_owner_id`, `owner_id`, `reason`, `actor_id` |
| [TerritoryCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryCoverage.php) | `team_id`, `rule_id`, `covered_user_id`, `substitute_user_id`, `starts_at`, `ends_at` |
| [TerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryRule.php) | `team_id`, `name`, `book_of_business`, `criteria`, `members`, `capacity`, `round_robin_cursor`, `active` |
<!-- layer-implementation-plan:end -->

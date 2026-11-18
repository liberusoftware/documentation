# Genealogy: Relationships Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#relationships). Observed identity: [`liberusoftware/module-genealogy-relationships-livewire`](../../../modules/source/liberusoftware--module-genealogy-relationships-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-relationships-livewire`  
**Matching domain module:** `genealogy-relationships`  
**Application:** Genealogy  
**Source feature:** [Relationships](../features/relationships.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Parent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Partner:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Household:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Adoption:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Guardianship:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Uncertain links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Graph validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-relationships-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-genealogy-relationships::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `parent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `partner`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `household`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `adoption`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `guardianship`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `uncertain-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `graph-validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-relationships` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/relationships.md) · [API plan](../api/relationships.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Parent** | Expose a focused Livewire 4 component and namespaced Blade default view for `parent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Partner** | Expose a focused Livewire 4 component and namespaced Blade default view for `partner` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Household** | Expose a focused Livewire 4 component and namespaced Blade default view for `household` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Adoption** | Expose a focused Livewire 4 component and namespaced Blade default view for `adoption` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Guardianship** | Expose a focused Livewire 4 component and namespaced Blade default view for `guardianship` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Uncertain links** | Expose a focused Livewire 4 component and namespaced Blade default view for `uncertain links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Graph validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `graph validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RelationshipsLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships-livewire/src/RelationshipsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [GraphValidator.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/GraphValidator.php) | `public function validate(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): array`<br>`public function assertValid(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): void` |
| [ParentGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/ParentGraph.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [RelationshipCalculator.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/RelationshipCalculator.php) | `public function between(string $firstPersonId, string $secondPersonId, ?string $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/CreateRelationship.php) | `public function execute(array $attributes): Relationship` |
| [DeleteRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/DeleteRelationship.php) | `public function execute(Relationship $relationship): void` |
| [RecordRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/RecordRelationship.php) | `public function execute(array $attributes): Relationship` |
| [UpdateRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/UpdateRelationship.php) | `public function __construct(private readonly GraphValidator $validator)`<br>`public function execute(Relationship $relationship, array $attributes): Relationship` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Relationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Models/Relationship.php) | `team_id`, `person_id`, `related_person_id`, `type`, `confidence`, `metadata` |
<!-- layer-implementation-plan:end -->

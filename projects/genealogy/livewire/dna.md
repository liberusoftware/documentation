# Genealogy: DNA Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#dna). Observed identity: [`liberusoftware/module-genealogy-dna-livewire`](../../../modules/source/liberusoftware--module-genealogy-dna-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-dna-livewire`  
**Matching domain module:** `genealogy-dna`  
**Application:** Genealogy  
**Source feature:** [DNA](../features/dna.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Kits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Providers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Match segments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Relationships:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Groups:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Notes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Revocation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-dna-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-genealogy-dna::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `kits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `providers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `match-segments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `relationships`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `groups`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `notes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `revocation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-dna` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/dna.md) · [API plan](../api/dna.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Kits** | Expose a focused Livewire 4 component and namespaced Blade default view for `kits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Providers** | Expose a focused Livewire 4 component and namespaced Blade default view for `providers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Consent** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Match segments** | Expose a focused Livewire 4 component and namespaced Blade default view for `match segments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Relationships** | Expose a focused Livewire 4 component and namespaced Blade default view for `relationships` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Groups** | Expose a focused Livewire 4 component and namespaced Blade default view for `groups` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Notes** | Expose a focused Livewire 4 component and namespaced Blade default view for `notes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Revocation** | Expose a focused Livewire 4 component and namespaced Blade default view for `revocation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [DnaLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-livewire/src/DnaLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaGroup.php) | `public function execute(array $attributes): DnaGroup`<br>`public function validate(array $values): void` |
| [CreateDnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaKit.php) | `public function execute(array $attributes): DnaKit` |
| [CreateDnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaMatch.php) | `public function execute(array $attributes): DnaMatch` |
| [CreateDnaNote.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaNote.php) | `public function execute(array $attributes): DnaNote` |
| [CreateDnaProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaProvider.php) | `public function execute(array $attributes): DnaProvider` |
| [CreateDnaRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaRelationship.php) | `public function execute(array $attributes): DnaRelationship` |
| [CreateDnaSegment.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaSegment.php) | `public function execute(array $attributes): DnaSegment` |
| [DeleteDnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaGroup.php) | `public function execute(DnaGroup $group): void` |
| [DeleteDnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaKit.php) | `public function __construct(private readonly DnaFileVault $vault)`<br>`public function execute(DnaKit $kit): void` |
| [DeleteDnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaMatch.php) | `public function execute(DnaMatch $match): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnaConsent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaConsent.php) | `team_id`, `kit_id`, `scope`, `granted`, `policy_version`, `granted_at`, `revoked_at`, `revocation_reason`, `metadata` |
| [DnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaGroup.php) | `team_id`, `name`, `description`, `status`, `metadata` |
| [DnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaKit.php) | `team_id`, `name`, `provider`, `provider_id`, `external_id`, `person_id`, `test_type`, `consent_status`, `consented_at`, `revoked_at`, `revocation_reason`, `status`, `metadata`, `file_path`, `file_hash`, `file_format`, `snp_count` |
| [DnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaMatch.php) | `team_id`, `kit_id`, `external_id`, `display_name`, `predicted_relationship`, `confidence`, `total_cm`, `shared_segments`, `status`, `is_private`, `notes`, `metadata` |
| [DnaNote.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaNote.php) | `team_id`, `noteable_type`, `noteable_id`, `body` |
| [DnaProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaProvider.php) | `team_id`, `name`, `slug`, `status`, `website`, `metadata` |
| [DnaRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaRelationship.php) | `team_id`, `match_id`, `person_id`, `relationship_type`, `confidence`, `status`, `rationale`, `metadata` |
| [DnaSegment.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaSegment.php) | `team_id`, `match_id`, `chromosome`, `start_position`, `end_position`, `centimorgans`, `snps`, `side`, `metadata` |
<!-- layer-implementation-plan:end -->

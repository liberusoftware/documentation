# Genealogy: Evidence Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#evidence). Observed identity: [`liberusoftware/module-genealogy-evidence-livewire`](../../../modules/source/liberusoftware--module-genealogy-evidence-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-evidence-livewire`  
**Matching domain module:** `genealogy-evidence`  
**Application:** Genealogy  
**Source feature:** [Evidence](../features/evidence.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Sources:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Repositories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Citations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Extracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assertions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Confidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Proof conclusions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-evidence-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-genealogy-evidence::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `sources`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `repositories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `citations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `extracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assertions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `confidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `proof-conclusions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-evidence` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/evidence.md) · [API plan](../api/evidence.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Sources** | Expose a focused Livewire 4 component and namespaced Blade default view for `sources` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Repositories** | Expose a focused Livewire 4 component and namespaced Blade default view for `repositories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Citations** | Expose a focused Livewire 4 component and namespaced Blade default view for `citations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Extracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `extracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Assertions** | Expose a focused Livewire 4 component and namespaced Blade default view for `assertions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Confidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `confidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Proof conclusions** | Expose a focused Livewire 4 component and namespaced Blade default view for `proof conclusions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [EvidenceLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-livewire/src/EvidenceLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/ArchiveEvidenceRecord.php) | `public function execute(EvidenceRecord $record): EvidenceRecord` |
| [CreateAssertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateAssertion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Assertion` |
| [CreateCitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitation.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Citation` |
| [CreateCitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitationLink.php) | `public function execute(array $attributes): CitationLink` |
| [CreateEvidenceEntity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceEntity.php) | `public function execute(string $modelClass, array $attributes): Model`<br>`public function validate(array $values, string $modelClass): void` |
| [CreateEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceRecord.php) | `public function execute(array $attributes): EvidenceRecord`<br>`public function validate(array $values): void` |
| [CreateExtract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateExtract.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Extract` |
| [CreateProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateProofConclusion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): ProofConclusion` |
| [CreateRepository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateRepository.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Repository` |
| [CreateSource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateSource.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Source` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Assertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Assertion.php) | `subject_person_id`, `citation_id`, `extract_id`, `statement`, `confidence`, `status`, `metadata` |
| [Citation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Citation.php) | `source_id`, `repository_id`, `title`, `volume`, `page`, `text`, `confidence`, `event_date`, `metadata` |
| [CitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/CitationLink.php) | `team_id`, `citation_id`, `subject_person_id`, `group`, `page`, `quality`, `text`, `metadata` |
| [EvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/EvidenceRecord.php) | `team_id`, `name`, `kind`, `repository`, `citation`, `extract`, `assertion`, `proof_conclusion`, `confidence`, `source_url`, `event_date`, `subject_person_id`, `reviewed_at`, `status`, `metadata` |
| [Extract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Extract.php) | `citation_id`, `content`, `transcription`, `page`, `metadata` |
| [ProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/ProofConclusion.php) | `assertion_id`, `conclusion`, `confidence`, `status`, `metadata` |
| [Repository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Repository.php) | `source_id`, `name`, `description`, `address`, `url`, `email`, `is_active`, `metadata` |
| [Source.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Source.php) | `name`, `description`, `url`, `archive_metadata`, `record_type`, `is_active`, `metadata` |
<!-- layer-implementation-plan:end -->

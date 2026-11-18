# CRM: Crm Consent And Preferences Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-consent-and-preferences). Observed identity: [`liberusoftware/module-crm-consent-and-preferences-livewire`](../../../modules/source/liberusoftware--module-crm-consent-and-preferences-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-consent-and-preferences-livewire`  
**Matching domain module:** `crm-consent-and-preferences`  
**Application:** CRM  
**Source feature:** [Crm Consent And Preferences](../features/crm-consent-and-preferences.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Lawful basis:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Subscriptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channel/topic preferences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Suppression:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quiet hours:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recording consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Proof:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expiry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Withdrawal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Policy evaluation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-consent-and-preferences-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmConsentAndPreferences::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `lawful-basis`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `subscriptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channel-topic-preferences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `suppression`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quiet-hours`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recording-consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `proof`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expiry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `withdrawal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `policy-evaluation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-consent-and-preferences` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-consent-and-preferences.md) · [API plan](../api/crm-consent-and-preferences.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Lawful basis** | Expose a focused Livewire 4 component and namespaced Blade default view for `lawful basis` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Subscriptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `subscriptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Channel/topic preferences** | Expose a focused Livewire 4 component and namespaced Blade default view for `channel/topic preferences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Suppression** | Expose a focused Livewire 4 component and namespaced Blade default view for `suppression` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quiet hours** | Expose a focused Livewire 4 component and namespaced Blade default view for `quiet hours` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recording consent** | Expose a focused Livewire 4 component and namespaced Blade default view for `recording consent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Proof** | Expose a focused Livewire 4 component and namespaced Blade default view for `proof` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expiry** | Expose a focused Livewire 4 component and namespaced Blade default view for `expiry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Withdrawal** | Expose a focused Livewire 4 component and namespaced Blade default view for `withdrawal` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Policy evaluation** | Expose a focused Livewire 4 component and namespaced Blade default view for `policy evaluation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ConsentBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-livewire/src/Components/ConsentBrowser.php) · [ConsentAndPreferencesLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-livewire/src/ConsentAndPreferencesLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/GrantConsent.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): ConsentRecord` |
| [SetPreference.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SetPreference.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic, array $values, ?int $actorId = null): PreferenceRecord` |
| [SuppressSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SuppressSubject.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): SuppressionRecord` |
| [WithdrawConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/WithdrawConsent.php) | `public function execute(ConsentRecord $record): ConsentRecord` |
| [PolicyEvaluator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Services/PolicyEvaluator.php) | `public function evaluate(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic = 'general', ?Carbon $at = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConsentRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/ConsentRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `lawful_basis`, `status`, `source`, `proof`, `consented_at`, `expires_at`, `withdrawn_at`, `actor_id` |
| [PolicyEvaluation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PolicyEvaluation.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `allowed`, `reasons`, `evaluated_at` |
| [PreferenceRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PreferenceRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `state`, `quiet_hours`, `timezone`, `actor_id` |
| [SuppressionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/SuppressionRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `reason`, `source`, `expires_at`, `withdrawn_at`, `actor_id` |
<!-- layer-implementation-plan:end -->

# CRM: Crm Lead Capture Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-lead-capture). Observed identity: [`liberusoftware/module-crm-lead-capture-livewire`](../../../modules/source/liberusoftware--module-crm-lead-capture-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-lead-capture-livewire`  
**Matching domain module:** `crm-lead-capture`  
**Application:** CRM  
**Source feature:** [Crm Lead Capture](../features/crm-lead-capture.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Leads inbox:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Manual/import/API capture:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Forms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Surveys:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **QR codes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Chat:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Advertisements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Referrals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Source metadata:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-lead-capture-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmLeadCapture::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `leads-inbox`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `manual-import-api-capture`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `forms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `surveys`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `qr-codes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `chat`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `advertisements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `referrals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `source-metadata`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-lead-capture` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-lead-capture.md) · [API plan](../api/crm-lead-capture.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Leads inbox** | Expose a focused Livewire 4 component and namespaced Blade default view for `leads inbox` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Manual/import/API capture** | Expose a focused Livewire 4 component and namespaced Blade default view for `manual/import/api capture` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Forms** | Expose a focused Livewire 4 component and namespaced Blade default view for `forms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Surveys** | Expose a focused Livewire 4 component and namespaced Blade default view for `surveys` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **QR codes** | Expose a focused Livewire 4 component and namespaced Blade default view for `qr codes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Chat** | Expose a focused Livewire 4 component and namespaced Blade default view for `chat` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Calls** | Expose a focused Livewire 4 component and namespaced Blade default view for `calls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Advertisements** | Expose a focused Livewire 4 component and namespaced Blade default view for `advertisements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Events** | Expose a focused Livewire 4 component and namespaced Blade default view for `events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Referrals** | Expose a focused Livewire 4 component and namespaced Blade default view for `referrals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Source metadata** | Expose a focused Livewire 4 component and namespaced Blade default view for `source metadata` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CaptureBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture-livewire/src/Components/CaptureBrowser.php) · [CaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture-livewire/src/Components/CaptureForm.php) · [LeadInbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture-livewire/src/Components/LeadInbox.php) · [LeadCaptureLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture-livewire/src/LeadCaptureLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CaptureQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Queries/CaptureQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CaptureLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CaptureLead.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CapturedLead`<br>`public function executeLegacy(int $teamId, ?int $actorId, array $input): LeadCapture` |
| [CreateCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureForm.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureForm` |
| [CreateCaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureQrCode.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureQrCode` |
| [RecordCaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordCaptureEvent.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, CapturedLead $lead, array $input): CaptureEvent` |
| [RecordReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordReferral.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureReferral` |
| [SubmitCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/SubmitCaptureForm.php) | `public function execute(CaptureForm $form, ?int $actorId, array $payload): LeadCapture` |
| [UpdateCaptureStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/UpdateCaptureStatus.php) | `public function execute(LeadCapture $capture, string $status, ?string $failureReason = null): LeadCapture` |
| [CaptureDeduplicator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureDeduplicator.php) | `public function key(array $attributes): string`<br>`public function find(int $teamId, string $key): ?LeadCapture` |
| [CaptureReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [LeadCapturePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/LeadCapturePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureForm.php) | `team_id`, `actor_id`, `kind`, `name`, `slug`, `status`, `schema`, `settings`, `submissions_count` |
| [CaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureQrCode.php) | `team_id`, `actor_id`, `name`, `code`, `destination`, `status`, `metadata`, `scan_count` |
| [CaptureReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureReferral.php) | `team_id`, `actor_id`, `code`, `referrer_type`, `referrer_id`, `referred_type`, `referred_id`, `status`, `metadata` |
| [CapturedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CapturedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [LeadCapture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/LeadCapture.php) | `team_id`, `actor_id`, `kind`, `status`, `name`, `email`, `phone`, `source`, `source_medium`, `source_campaign`, `external_id`, `dedupe_key`, `source_metadata`, `payload`, `provenance`, `captured_at`, `processed_at`, `failure_reason` |
<!-- layer-implementation-plan:end -->

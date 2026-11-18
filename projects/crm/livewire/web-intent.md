# CRM: Web Intent Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#web-intent). Observed identity: [`liberusoftware/module-crm-web-intent-livewire`](../../../modules/source/liberusoftware--module-crm-web-intent-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-web-intent-livewire`  
**Matching domain module:** `crm-web-intent`  
**Application:** CRM  
**Source feature:** [Web Intent](../features/web-intent.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **First-party visits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Account identification adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Page/content engagement:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scoring signals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Alerts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Buyer intent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lead/account conversion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-web-intent-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-web-intent::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `first-party-visits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `account-identification-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `page-content-engagement`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scoring-signals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `alerts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `buyer-intent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lead-account-conversion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-web-intent` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/web-intent.md) · [API plan](../api/web-intent.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **First-party visits** | Expose a focused Livewire 4 component and namespaced Blade default view for `first-party visits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Account identification adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `account identification adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Page/content engagement** | Expose a focused Livewire 4 component and namespaced Blade default view for `page/content engagement` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scoring signals** | Expose a focused Livewire 4 component and namespaced Blade default view for `scoring signals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Alerts** | Expose a focused Livewire 4 component and namespaced Blade default view for `alerts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Buyer intent** | Expose a focused Livewire 4 component and namespaced Blade default view for `buyer intent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Consent** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lead/account conversion** | Expose a focused Livewire 4 component and namespaced Blade default view for `lead/account conversion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [IntentDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent-livewire/src/Components/IntentDashboard.php) · [WebIntentLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent-livewire/src/WebIntentLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WebIntentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Queries/WebIntentQuery.php) | `public function visits(int $teamId): Builder`<br>`public function alerts(int $teamId): Builder`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConvertIntent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ConvertIntent.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $targetType, int $targetId, ?int $visitId, array $metadata, WebIntentPolicy $policy): WebIntentConversion` |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/CreateAlert.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $title, string $severity, ?int $visitId, ?string $details, WebIntentPolicy $policy): WebIntentAlert` |
| [IdentifyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/IdentifyAccount.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $adapter, ?string $accountName, ?string $accountDomain, int $confidence, array $metadata, WebIntentPolicy $policy): WebIntentIdentification` |
| [RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordEngagement.php) | `public function execute(WebIntentVisit $visit, array $attributes, WebIntentScorer $scorer): WebIntentEngagement` |
| [RecordVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordVisit.php) | `public function execute(int $teamId, string $visitorKey, array $attributes = []): WebIntentVisit` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ResolveAlert.php) | `public function execute(WebIntentAlert $alert, int $actorId, WebIntentPolicy $policy): WebIntentAlert` |
| [SetConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/SetConsent.php) | `public function execute(int $teamId, string $visitorKey, string $purpose, string $status, ?string $policyVersion = null): WebIntentConsent` |
| [WebIntentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $data = []): void` |
| [WebIntentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |
| [WebIntentScorer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentScorer.php) | `public function points(string $eventType, ?int $durationSeconds = null): int`<br>`public function level(int $score): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WebIntentAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentAlert.php) | `team_id`, `visitor_key`, `visit_id`, `severity`, `title`, `details`, `status`, `triggered_at`, `resolved_at`, `resolved_by` |
| [WebIntentConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConsent.php) | `team_id`, `visitor_key`, `purpose`, `status`, `policy_version`, `granted_at`, `revoked_at` |
| [WebIntentConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConversion.php) | `team_id`, `visitor_key`, `visit_id`, `target_type`, `target_id`, `actor_id`, `status`, `metadata` |
| [WebIntentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentEngagement.php) | `team_id`, `visit_id`, `visitor_key`, `event_type`, `page_url`, `content_type`, `content_id`, `points`, `duration_seconds`, `dedupe_key`, `metadata`, `occurred_at` |
| [WebIntentIdentification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentIdentification.php) | `team_id`, `visitor_key`, `adapter`, `account_name`, `account_domain`, `confidence`, `status`, `metadata` |
| [WebIntentSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentSignal.php) | `team_id`, `visit_id`, `visitor_key`, `signal`, `points`, `metadata`, `occurred_at` |
| [WebIntentVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentVisit.php) | `team_id`, `visitor_key`, `session_key`, `ip_hash`, `user_agent_hash`, `landing_url`, `referrer`, `consent_status`, `score`, `intent_level`, `status`, `started_at`, `ended_at`, `metadata` |
<!-- layer-implementation-plan:end -->

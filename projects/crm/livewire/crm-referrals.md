# CRM: Crm Referrals Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-referrals). Observed identity: [`liberusoftware/module-crm-referrals-livewire`](../../../modules/source/liberusoftware--module-crm-referrals-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-referrals-livewire`  
**Matching domain module:** `crm-referrals`  
**Application:** CRM  
**Source feature:** [Crm Referrals](../features/crm-referrals.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Referral programs and links/codes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Advocates, prospects, and qualification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rewards, fraud/duplicate controls, status, and attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-referrals-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmReferrals::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `referral-programs-and-links-codes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `advocates-prospects-and-qualification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rewards-fraud-duplicate-controls-status-and-attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-referrals` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-referrals.md) · [API plan](../api/crm-referrals.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Referral programs and links/codes** | Expose a focused Livewire 4 component and namespaced Blade default view for `referral programs and links/codes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Advocates, prospects, and qualification** | Expose a focused Livewire 4 component and namespaced Blade default view for `advocates, prospects, and qualification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rewards, fraud/duplicate controls, status, and attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `rewards, fraud/duplicate controls, status, and attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ReferralsDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-livewire/src/Components/ReferralsDashboard.php) · [ReferralsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-livewire/src/ReferralsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReferralQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Queries/ReferralQuery.php) | `public function programs(int $teamId)`<br>`public function referrals(int $teamId)`<br>`public function rewards(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/CreateProgram.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReferralProgram` |
| [CreateReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/CreateReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Referral` |
| [IssueReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/IssueReward.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReferralReward` |
| [QualifyReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/QualifyReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $referralId, string $status): Referral` |
| [UpdateReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/UpdateReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $referralId, array $input): Referral` |
| [ReferralPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Services/ReferralPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Referral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/Referral.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReferralProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/ReferralProgram.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReferralReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/ReferralReward.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

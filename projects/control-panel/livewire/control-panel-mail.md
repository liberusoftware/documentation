# Control Panel: Control Panel Mail Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-mail). Observed identity: [`liberusoftware/module-control-panel-mail-livewire`](../../../modules/source/liberusoftware--module-control-panel-mail-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-control-panel-control-panel-mail-livewire`  
**Matching domain module:** `control-panel-mail`  
**Application:** Control Panel  
**Source feature:** [Control Panel Mail](../features/control-panel-mail.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Domains:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mailboxes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Aliases:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Routing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quotas:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Spam/virus controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **DKIM:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delivery diagnostics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-control-panel-control-panel-mail-livewire` component namespace and service provider; use explicit aliases such as `<livewire:controlpanelControlPanelMail::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `domains`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mailboxes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `aliases`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `routing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quotas`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `spam-virus-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dkim`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delivery-diagnostics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `control-panel-mail` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/control-panel-mail.md) · [API plan](../api/control-panel-mail.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Domains** | Expose a focused Livewire 4 component and namespaced Blade default view for `domains` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mailboxes** | Expose a focused Livewire 4 component and namespaced Blade default view for `mailboxes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Aliases** | Expose a focused Livewire 4 component and namespaced Blade default view for `aliases` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Routing** | Expose a focused Livewire 4 component and namespaced Blade default view for `routing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quotas** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotas` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Spam/virus controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `spam/virus controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **DKIM** | Expose a focused Livewire 4 component and namespaced Blade default view for `dkim` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delivery diagnostics** | Expose a focused Livewire 4 component and namespaced Blade default view for `delivery diagnostics` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MailFeatureInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-livewire/src/Components/MailFeatureInventory.php) · [MailInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-livewire/src/Components/MailInventory.php) · [MailLivewireServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-livewire/src/MailLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListMailAccounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Queries/ListMailAccounts.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureMailAuthentication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailAuthentication.php) | `public function __construct(private readonly RotateDkimKey $rotateDkimKey)`<br>`public function execute(MailDomain $domain, array $attributes = []): MailDomain` |
| [ConfigureMailControls.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailControls.php) | `public function execute(array $a): MailControl` |
| [CreateMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAccount.php) | `public function execute(array $attributes): MailAccount` |
| [CreateMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAlias.php) | `public function execute(array $a): MailAlias` |
| [CreateMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailRoute.php) | `public function execute(array $attributes): MailRoute` |
| [DeleteMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAccount.php) | `public function execute(MailAccount $account): void` |
| [DeleteMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAlias.php) | `public function execute(MailAlias $alias): void` |
| [DeleteMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailRoute.php) | `public function execute(MailRoute $route): void` |
| [RecordDeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordDeliveryDiagnostic.php) | `public function execute(array $a): DeliveryDiagnostic` |
| [RecordMailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordMailOperation.php) | `public function execute(array $a): MailOperation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DeliveryDiagnostic.php) | `id`, `team_id`, `mail_account_id`, `message_id`, `recipient`, `status`, `response`, `checked_at` |
| [DkimKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DkimKey.php) | `id`, `team_id`, `domain`, `selector`, `public_key`, `private_key`, `active`, `rotated_at` |
| [MailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAccount.php) | `team_id`, `domain`, `address`, `status`, `quota_bytes`, `settings` |
| [MailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAlias.php) | `id`, `team_id`, `domain`, `address`, `destinations`, `active` |
| [MailControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailControl.php) | `id`, `team_id`, `mail_account_id`, `spam_filter_enabled`, `spam_threshold`, `spam_action`, `virus_scan_enabled`, `autoresponder_enabled`, `autoresponder_subject`, `autoresponder_message`, `autoresponder_start_at`, `autoresponder_end_at`, `keep_copy_on_server` |
| [MailDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailDomain.php) | `id`, `team_id`, `domain`, `status`, `dkim`, `spf`, `dmarc` |
| [MailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailOperation.php) | `id`, `team_id`, `mail_account_id`, `operation`, `status`, `details` |
| [MailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailRoute.php) | `id`, `team_id`, `domain`, `source_pattern`, `destination`, `priority`, `active` |
<!-- layer-implementation-plan:end -->

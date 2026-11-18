# CRM: Channel Gateway Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#channel-gateway). Observed identity: [`liberusoftware/module-crm-channel-gateway-livewire`](../../../modules/source/liberusoftware--module-crm-channel-gateway-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-channel-gateway-livewire`  
**Matching domain module:** `crm-channel-gateway`  
**Application:** CRM  
**Source feature:** [Channel Gateway](../features/channel-gateway.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Provider-neutral email:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **SMS/MMS:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **WhatsApp:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Web chat:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Social messaging:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Push contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Routing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Health:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider selection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-channel-gateway-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-channel-gateway::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `provider-neutral-email`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sms-mms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `whatsapp`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `web-chat`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `social-messaging`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `push-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `routing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `health`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-selection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-channel-gateway` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/channel-gateway.md) · [API plan](../api/channel-gateway.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Provider-neutral email** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider-neutral email` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **SMS/MMS** | Expose a focused Livewire 4 component and namespaced Blade default view for `sms/mms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **WhatsApp** | Expose a focused Livewire 4 component and namespaced Blade default view for `whatsapp` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Web chat** | Expose a focused Livewire 4 component and namespaced Blade default view for `web chat` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Social messaging** | Expose a focused Livewire 4 component and namespaced Blade default view for `social messaging` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Push contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `push contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Routing** | Expose a focused Livewire 4 component and namespaced Blade default view for `routing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Templates** | Expose a focused Livewire 4 component and namespaced Blade default view for `templates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Health** | Expose a focused Livewire 4 component and namespaced Blade default view for `health` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provider selection** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider selection` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ChannelGatewayLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-livewire/src/ChannelGatewayLivewireServiceProvider.php) · [GatewayBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-livewire/src/Components/GatewayBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [GatewayQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Queries/GatewayQuery.php) | `public function channels(int $teamId): Builder`<br>`public function deliveries(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [QueueGatewayDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/QueueGatewayDelivery.php) | `public function execute(int $teamId, GatewayChannel $channel, string $idempotencyKey, string $address, string $body, array $metadata = []): GatewayDelivery` |
| [RegisterGatewayChannel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/RegisterGatewayChannel.php) | `public function execute(int $teamId, string $key, string $kind, string $provider, array $configuration = []): GatewayChannel` |
| [UpdateGatewayHealth.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/UpdateGatewayHealth.php) | `public function execute(int $teamId, GatewayChannel $channel, bool $healthy, ?string $failure = null): GatewayChannel` |
| [ChannelAdapter.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Contracts/ChannelAdapter.php) | `public function send(string $address, string $body, array $metadata = []): string`<br>`public function health(): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GatewayChannel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Models/GatewayChannel.php) | No literal fillable array detected; inspect the model and API schema. |
| [GatewayDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Models/GatewayDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

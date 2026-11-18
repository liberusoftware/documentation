# CRM: Crm Omnichannel Service Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-omnichannel-service). Observed identity: [`liberusoftware/module-crm-omnichannel-service-livewire`](../../../modules/source/liberusoftware--module-crm-omnichannel-service-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-omnichannel-service-livewire`  
**Matching domain module:** `crm-omnichannel-service`  
**Application:** CRM  
**Source feature:** [Crm Omnichannel Service](../features/crm-omnichannel-service.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Email/chat/social/phone intake:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Routing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Agent workspace:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Macros:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Suggested replies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Swarming:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Collision control:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Complete interaction history:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-omnichannel-service-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmOmnichannelService::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `email-chat-social-phone-intake`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `routing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `agent-workspace`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `macros`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `suggested-replies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `swarming`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `collision-control`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `complete-interaction-history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-omnichannel-service` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-omnichannel-service.md) · [API plan](../api/crm-omnichannel-service.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Email/chat/social/phone intake** | Expose a focused Livewire 4 component and namespaced Blade default view for `email/chat/social/phone intake` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Routing** | Expose a focused Livewire 4 component and namespaced Blade default view for `routing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Agent workspace** | Expose a focused Livewire 4 component and namespaced Blade default view for `agent workspace` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Macros** | Expose a focused Livewire 4 component and namespaced Blade default view for `macros` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Suggested replies** | Expose a focused Livewire 4 component and namespaced Blade default view for `suggested replies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Swarming** | Expose a focused Livewire 4 component and namespaced Blade default view for `swarming` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Collision control** | Expose a focused Livewire 4 component and namespaced Blade default view for `collision control` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Complete interaction history** | Expose a focused Livewire 4 component and namespaced Blade default view for `complete interaction history` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AgentWorkspace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-livewire/src/Components/AgentWorkspace.php) · [OmnichannelServiceLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-livewire/src/OmnichannelServiceLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Queries/ConversationQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/AssignConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Conversation` |
| [RecordInteraction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordInteraction.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Interaction` |
| [RecordWorkspaceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordWorkspaceEvent.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): WorkspaceEvent` |
| [StartConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/StartConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Conversation` |
| [OmnichannelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Services/OmnichannelPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Conversation.php) | No literal fillable array detected; inspect the model and API schema. |
| [Interaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Interaction.php) | No literal fillable array detected; inspect the model and API schema. |
| [Macro.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Macro.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/WorkspaceEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

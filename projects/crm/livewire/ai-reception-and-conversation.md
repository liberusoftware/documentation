# CRM: AI Reception and Conversation Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#ai-reception-and-conversation). Observed identity: [`liberusoftware/module-crm-ai-reception-and-conversation-livewire`](../../../modules/source/liberusoftware--module-crm-ai-reception-and-conversation-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-ai-reception-and-conversation-livewire`  
**Matching domain module:** `crm-ai-reception-and-conversation`  
**Application:** CRM  
**Source feature:** [AI Reception and Conversation](../features/ai-reception-and-conversation.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Governed chat/voice agents:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approved knowledge/tools:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Qualification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Booking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Summaries:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Confidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Live handoff:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Testing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Human-approval policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-ai-reception-and-conversation-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-ai-reception-and-conversation::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `governed-chat-voice-agents`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approved-knowledge-tools`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `qualification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `booking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `summaries`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `confidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `live-handoff`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `testing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `human-approval-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-ai-reception-and-conversation` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/ai-reception-and-conversation.md) · [API plan](../api/ai-reception-and-conversation.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Governed chat/voice agents** | Expose a focused Livewire 4 component and namespaced Blade default view for `governed chat/voice agents` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approved knowledge/tools** | Expose a focused Livewire 4 component and namespaced Blade default view for `approved knowledge/tools` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Qualification** | Expose a focused Livewire 4 component and namespaced Blade default view for `qualification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Booking** | Expose a focused Livewire 4 component and namespaced Blade default view for `booking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Summaries** | Expose a focused Livewire 4 component and namespaced Blade default view for `summaries` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Confidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `confidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Live handoff** | Expose a focused Livewire 4 component and namespaced Blade default view for `live handoff` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Testing** | Expose a focused Livewire 4 component and namespaced Blade default view for `testing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Human-approval policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `human-approval policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AIReceptionAndConversationLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-livewire/src/AIReceptionAndConversationLivewireServiceProvider.php) · [AgentBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-livewire/src/Components/AgentBrowser.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/ActivateReceptionAgent.php) | `public function execute(int $teamId, ReceptionAgent $agent): ReceptionAgent` |
| [CreateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/CreateReceptionAgent.php) | `public function execute(int $teamId, int $ownerId, array $input): ReceptionAgent` |
| [RecordReceptionTurn.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RecordReceptionTurn.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, array $input): ReceptionConversation` |
| [RequestReceptionHandoff.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RequestReceptionHandoff.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, string $reason): ReceptionConversation` |
| [StartReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/StartReceptionConversation.php) | `public function execute(int $teamId, ReceptionAgent $agent, array $input = []): ReceptionConversation` |
| [ReceptionResponder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Services/ReceptionResponder.php) | `public function respond(ReceptionAgent $agent, ReceptionConversation $conversation, string $input): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionConversation.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

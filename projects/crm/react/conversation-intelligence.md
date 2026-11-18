# CRM: Conversation Intelligence React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#conversation-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-conversation-intelligence-react-inertia`
**Matching domain module:** `crm-conversation-intelligence`
**Application:** CRM
**Source feature:** [Conversation Intelligence](../features/conversation-intelligence.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/conversation-intelligence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Call/meeting recording:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transcription:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Summaries:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Topics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Questions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Objections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Competitors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sentiment policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Action items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Highlights:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Searchable evidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-conversation-intelligence-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `call-meeting-recording`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `transcription`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `summaries`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `topics`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `questions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `objections`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `competitors`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `sentiment-policy`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `action-items`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `highlights`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `searchable-evidence`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `crm-conversation-intelligence` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-conversation-intelligence-react-inertia`](https://github.com/liberusoftware/module-crm-conversation-intelligence-react-inertia) (`@liberusoftware/module-crm-conversation-intelligence-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/conversation-intelligence.md) · [Core plan](../core/conversation-intelligence.md) · [API plan](../api/conversation-intelligence.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Call/meeting recording** | Render `call/meeting recording` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Transcription** | Render `transcription` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Summaries** | Render `summaries` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Topics** | Render `topics` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Questions** | Render `questions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Objections** | Render `objections` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Competitors** | Render `competitors` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Sentiment policy** | Render `sentiment policy` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Action items** | Render `action items` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Highlights** | Render `highlights` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Searchable evidence** | Render `searchable evidence` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Queries/ConversationQuery.php) | `public function conversations(int $teamId): Builder`<br>`public function evidence(int $teamId, string $search): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEvidence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/AddEvidence.php) | `public function execute(int $teamId, Conversation $conversation, string $kind, string $label, string $content, array $metadata = []): ConversationEvidence` |
| [AnalyzeConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/AnalyzeConversation.php) | `public function execute(int $teamId, Conversation $conversation, string $transcript, array $insights = []): Conversation` |
| [RecordConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/RecordConversation.php) | `public function execute(int $teamId, int $userId, array $input): Conversation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Models/Conversation.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConversationEvidence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Models/ConversationEvidence.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversationIntelligenceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence-api/src/Http/Controllers/ConversationIntelligenceController.php) | `public function __construct(private readonly ConversationQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(RecordConversation $a): JsonResponse`<br>`public function analyze(Conversation $c, AnalyzeConversation $a): JsonResponse`<br>`public function evidence(Conversation $c, AddEvidence $a): JsonResponse`<br>`public function search(): JsonResponse` |

**Observed route declarations:**

[modules/crm-conversation-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/conversation-intelligence')->group(function (): void {
Route::get('conversations', [ConversationIntelligenceController::class, 'index']);
Route::post('conversations', [ConversationIntelligenceController::class, 'store']);
Route::post('conversations/{conversation}/analyze', [ConversationIntelligenceController::class, 'analyze']);
Route::post('conversations/{conversation}/evidence', [ConversationIntelligenceController::class, 'evidence']);
Route::get('evidence/search', [ConversationIntelligenceController::class, 'search']);
```
<!-- layer-implementation-plan:end -->

# Crm Proposals And Quotes React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-proposals-and-quotes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-proposals-and-quotes-react-native
**Matching core package:** module-crm-crm-proposals-and-quotes ([implementation](../core/crm-proposals-and-quotes.md))
**Matching API package:** module-crm-crm-proposals-and-quotes-api ([contract](../api/crm-proposals-and-quotes.md))

## Implementation plan

This adapter presents Crm Proposals And Quotes for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Proposals And Quotes API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-proposals-and-quotes.md), and [API module](../api/crm-proposals-and-quotes.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-proposals-and-quotes`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-proposals-and-quotes.md)) |
| Capability React Native module skeleton | [`module-crm-proposals-and-quotes-react-native`](https://github.com/liberusoftware/module-crm-proposals-and-quotes-react-native) (`@liberusoftware/module-crm-proposals-and-quotes-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Branded templates** | Progressive mobile list/detail/sheet flow for `branded templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sections** | Progressive mobile list/detail/sheet flow for `sections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Scope** | Progressive mobile list/detail/sheet flow for `scope` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Line items** | Progressive mobile list/detail/sheet flow for `line items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Optional choices** | Progressive mobile list/detail/sheet flow for `optional choices` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versions** | Progressive mobile list/detail/sheet flow for `versions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Comments** | Progressive mobile list/detail/sheet flow for `comments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery** | Progressive mobile list/detail/sheet flow for `delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Engagement** | Progressive mobile list/detail/sheet flow for `engagement` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Acceptance** | Progressive mobile list/detail/sheet flow for `acceptance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Expiry** | Progressive mobile list/detail/sheet flow for `expiry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProposalQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Queries/ProposalQuery.php) | `public function templates(int $teamId)`<br>`public function proposals(int $teamId)`<br>`public function versions(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddProposalComment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/AddProposalComment.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalEvent` |
| [ChangeProposalStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/ChangeProposalStatus.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, string $status): Proposal` |
| [CreateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Proposal` |
| [CreateProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalTemplate.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalTemplate` |
| [CreateProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalVersion.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalVersion` |
| [UpdateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/UpdateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, array $input): Proposal` |
| [ProposalPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Services/ProposalPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Proposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/Proposal.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalVersion.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProposalsAndQuotesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/src/Http/Controllers/ProposalsAndQuotesController.php) | `public function templates(Request $r, ProposalQuery $q)`<br>`public function template(Request $r, CreateProposalTemplate $a)`<br>`public function proposals(Request $r, ProposalQuery $q)`<br>`public function proposal(Request $r, CreateProposal $a)`<br>`public function version(Request $r, CreateProposalVersion $a)`<br>`public function status(Request $r, int $proposal, string $status, ChangeProposalStatus $a)`<br>`public function comment(Request $r, AddProposalComment $a)` |

**Observed route declarations:**

[modules/crm-proposals-and-quotes-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/proposals-and-quotes')->group(function (): void {
Route::get('/templates', [ProposalsAndQuotesController::class, 'templates']);
Route::post('/templates', [ProposalsAndQuotesController::class, 'template']);
Route::get('/proposals', [ProposalsAndQuotesController::class, 'proposals']);
Route::post('/proposals', [ProposalsAndQuotesController::class, 'proposal']);
Route::post('/versions', [ProposalsAndQuotesController::class, 'version']);
Route::post('/proposals/{proposal}/{status}', [ProposalsAndQuotesController::class, 'status'])->whereIn('status', ['approved', 'delivered', 'accepted', 'rejected', 'expired']);
Route::post('/comments', [ProposalsAndQuotesController::class, 'comment']);
```
<!-- layer-implementation-plan:end -->

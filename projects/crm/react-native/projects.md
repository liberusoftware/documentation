# Projects React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#projects). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-projects-react-native
**Matching core package:** module-crm-projects ([implementation](../core/projects.md))
**Matching API package:** module-crm-projects-api ([contract](../api/projects.md))

## Implementation plan

This adapter presents Projects for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Projects API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/projects.md), and [API module](../api/projects.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `projects`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/projects.md)) |
| Capability React Native module skeleton | [`module-crm-projects-react-native`](https://github.com/liberusoftware/module-crm-projects-react-native) (`@liberusoftware/module-crm-projects-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Post-sale projects** | Progressive mobile list/detail/sheet flow for `post-sale projects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Milestones** | Progressive mobile list/detail/sheet flow for `milestones` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tasks** | Progressive mobile list/detail/sheet flow for `tasks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dependencies** | Progressive mobile list/detail/sheet flow for `dependencies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Owners** | Progressive mobile list/detail/sheet flow for `owners` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Time** | Progressive mobile list/detail/sheet flow for `time` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Files** | Progressive mobile list/detail/sheet flow for `files` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Status** | Progressive mobile list/detail/sheet flow for `status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Risks** | Progressive mobile list/detail/sheet flow for `risks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Client visibility** | Progressive mobile list/detail/sheet flow for `client visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Opportunity handoff** | Progressive mobile list/detail/sheet flow for `opportunity handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Queries/ProjectQuery.php) | `public function templates(int $teamId)`<br>`public function projects(int $teamId)`<br>`public function tasks(int $teamId)`<br>`public function risks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeProjectStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/ChangeProjectStatus.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, string $status): Project` |
| [CreateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Project` |
| [CreateProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProjectTask.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTask` |
| [HandoffOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/HandoffOpportunity.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, int $opportunityId): Project` |
| [LogProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/LogProjectTime.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTime` |
| [RecordProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/RecordProjectRisk.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectRisk` |
| [UpdateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/UpdateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, array $input): Project` |
| [ProjectPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Services/ProjectPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Project.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/Project.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectRisk.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTime.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-api/src/Http/Controllers/ProjectsController.php) | `public function projects(Request $r, ProjectQuery $q)`<br>`public function project(Request $r, CreateProject $a)`<br>`public function task(Request $r, CreateProjectTask $a)`<br>`public function time(Request $r, LogProjectTime $a)`<br>`public function status(Request $r, int $project, string $status, ChangeProjectStatus $a)`<br>`public function risk(Request $r, RecordProjectRisk $a)`<br>`public function handoff(Request $r, int $project, HandoffOpportunity $a)` |

**Observed route declarations:**

[modules/crm-projects-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/projects')->group(function (): void {
Route::get('/', [ProjectsController::class, 'projects']);
Route::post('/', [ProjectsController::class, 'project']);
Route::post('/tasks', [ProjectsController::class, 'task']);
Route::post('/time', [ProjectsController::class, 'time']);
Route::post('/risks', [ProjectsController::class, 'risk']);
Route::post('/{project}/{status}', [ProjectsController::class, 'status'])->whereIn('status', ['planning', 'active', 'at_risk', 'on_hold', 'completed', 'cancelled']);
Route::post('/{project}/handoff', [ProjectsController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->

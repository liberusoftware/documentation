# Learning And Courses React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#learning-and-courses). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-learning-and-courses-react-native
**Matching core package:** module-crm-learning-and-courses ([implementation](../core/learning-and-courses.md))
**Matching API package:** module-crm-learning-and-courses-api ([contract](../api/learning-and-courses.md))

## Implementation plan

This adapter presents Learning And Courses for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Learning And Courses API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/learning-and-courses.md), and [API module](../api/learning-and-courses.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `learning-and-courses`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/learning-and-courses.md)) |
| Capability React Native module skeleton | [`module-crm-learning-and-courses-react-native`](https://github.com/liberusoftware/module-crm-learning-and-courses-react-native) (`@liberusoftware/module-crm-learning-and-courses-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Courses** | Progressive mobile list/detail/sheet flow for `courses` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lessons** | Progressive mobile list/detail/sheet flow for `lessons` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Media** | Progressive mobile list/detail/sheet flow for `media` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cohorts** | Progressive mobile list/detail/sheet flow for `cohorts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Enrollment** | Progressive mobile list/detail/sheet flow for `enrollment` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Access** | Progressive mobile list/detail/sheet flow for `access` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Progress** | Progressive mobile list/detail/sheet flow for `progress` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assessments** | Progressive mobile list/detail/sheet flow for `assessments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Certificates** | Progressive mobile list/detail/sheet flow for `certificates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Drip schedules** | Progressive mobile list/detail/sheet flow for `drip schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Product/contract entitlements** | Progressive mobile list/detail/sheet flow for `product/contract entitlements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LearningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Queries/LearningQuery.php) | `public function forTeam(int $teamId)`<br>`public function records(int $teamId, int $enrollmentId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/CreateCourse.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): LearningCourse` |
| [EnrollLearner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/EnrollLearner.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LearningCourse $course, array $input): LearningEnrollment` |
| [RecordLearningProgress.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/RecordLearningProgress.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LearningEnrollment $enrollment, array $input): LearningRecord` |
| [LearningPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Services/LearningPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LearningCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningCourse.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningEnrollment.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningLesson.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningLesson.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [LearningController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-api/src/Http/Controllers/LearningController.php) | `public function index(Request $r, LearningQuery $q): JsonResponse`<br>`public function store(Request $r, CreateCourse $a): JsonResponse`<br>`public function enroll(Request $r, LearningCourse $course, EnrollLearner $a): JsonResponse`<br>`public function record(Request $r, LearningEnrollment $enrollment, RecordLearningProgress $a): JsonResponse`<br>`public function records(Request $r, LearningEnrollment $enrollment, LearningQuery $q): JsonResponse` |
<!-- layer-implementation-plan:end -->

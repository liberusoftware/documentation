# Forms And Surveys React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#forms-and-surveys). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-forms-and-surveys-react-native
**Matching core package:** module-crm-forms-and-surveys ([implementation](../core/forms-and-surveys.md))
**Matching API package:** module-crm-forms-and-surveys-api ([contract](../api/forms-and-surveys.md))

## Implementation plan

This adapter presents Forms And Surveys for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Forms And Surveys API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/forms-and-surveys.md), and [API module](../api/forms-and-surveys.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `forms-and-surveys`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/forms-and-surveys.md)) |
| Capability React Native module skeleton | [`module-crm-forms-and-surveys-react-native`](https://github.com/liberusoftware/module-crm-forms-and-surveys-react-native) (`@liberusoftware/module-crm-forms-and-surveys-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Drag-and-drop schemas** | Progressive mobile list/detail/sheet flow for `drag-and-drop schemas` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Conditional fields** | Progressive mobile list/detail/sheet flow for `conditional fields` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Progressive profiling** | Progressive mobile list/detail/sheet flow for `progressive profiling` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Validation** | Progressive mobile list/detail/sheet flow for `validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Spam controls** | Progressive mobile list/detail/sheet flow for `spam controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Consent** | Progressive mobile list/detail/sheet flow for `consent` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Hidden attribution** | Progressive mobile list/detail/sheet flow for `hidden attribution` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Embedding** | Progressive mobile list/detail/sheet flow for `embedding` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Submissions** | Progressive mobile list/detail/sheet flow for `submissions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Follow-up** | Progressive mobile list/detail/sheet flow for `follow-up` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FormQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Queries/FormQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateSurveyForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/CreateSurveyForm.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SurveyForm` |
| [RecordFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/RecordFollowUp.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FormSubmission $submission, array $input): FormFollowUp` |
| [SubmitForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/SubmitForm.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SurveyForm $form, array $input): FormSubmission` |
| [FormPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Services/FormPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FormFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/FormFollowUp.php) | No literal fillable array detected; inspect the model and API schema. |
| [FormSubmission.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/FormSubmission.php) | No literal fillable array detected; inspect the model and API schema. |
| [SurveyForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/SurveyForm.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FormsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys-api/src/Http/Controllers/FormsController.php) | `public function index(Request $r, FormQuery $q): JsonResponse`<br>`public function store(Request $r, CreateSurveyForm $a): JsonResponse`<br>`public function submit(Request $r, SurveyForm $form, SubmitForm $a): JsonResponse`<br>`public function followUp(Request $r, FormSubmission $submission, RecordFollowUp $a): JsonResponse` |
<!-- layer-implementation-plan:end -->

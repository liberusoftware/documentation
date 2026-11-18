# Journal Approvals React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#journal-approvals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-journal-approvals-react-native
**Matching core package:** module-accounting-journal-approvals ([implementation](../core/journal-approvals.md))
**Matching API package:** module-accounting-journal-approvals-api ([contract](../api/journal-approvals.md))

## Implementation plan

This adapter presents Journal Approvals for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Journal Approvals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/journal-approvals.md), and [API module](../api/journal-approvals.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `journal-approvals`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/journal-approvals.md)) |
| Capability React Native module skeleton | [`module-accounting-journal-approvals-react-native`](https://github.com/liberusoftware/module-accounting-journal-approvals-react-native) (`@liberusoftware/module-accounting-journal-approvals-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Journal sources/types** | Progressive mobile list/detail/sheet flow for `journal sources/types` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Thresholds** | Progressive mobile list/detail/sheet flow for `thresholds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Preparer/reviewer** | Progressive mobile list/detail/sheet flow for `preparer/reviewer` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Evidence** | Progressive mobile list/detail/sheet flow for `evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rejection** | Progressive mobile list/detail/sheet flow for `rejection` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Posting** | Progressive mobile list/detail/sheet flow for `posting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Emergency controls** | Progressive mobile list/detail/sheet flow for `emergency controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [JournalApprovalQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Queries/JournalApprovalQuery.php) | `public function paginate(?int $teamId = null, ?ApprovalStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/AddEvidence.php) | `public function handle(JournalApproval $approval, array $attributes): JournalEvidence` |
| [ConfigureThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/ConfigureThreshold.php) | `public function handle(array $attributes): ApprovalThreshold` |
| [DecideJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/DecideJournal.php) | `public function handle(JournalApproval $approval, string $actor, bool $approved, ?string $comment = null): JournalApproval` |
| [PostJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/PostJournal.php) | `public function handle(JournalApproval $approval, bool $emergency = false, ?string $reason = null): JournalApproval` |
| [SubmitJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/SubmitJournal.php) | `public function handle(array $attributes, array $evidence = []): JournalApproval` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ApprovalThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/ApprovalThreshold.php) | `team_id`, `journal_type`, `minimum_amount`, `reviewer_role`, `required_approvals`, `emergency_allowed`, `active`, `metadata` |
| [JournalApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalApproval.php) | `team_id`, `approval_ref`, `journal_type`, `journal_source`, `journal_ref`, `preparer_ref`, `reviewer_ref`, `currency`, `amount`, `threshold_amount`, `status`, `submitted_at`, `decided_at`, `posted_at`, `emergency_reason`, `metadata` |
| [JournalDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalDecision.php) | `approval_id`, `actor_ref`, `decision`, `comment`, `decided_at`, `metadata` |
| [JournalEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalEvidence.php) | `approval_id`, `kind`, `file_ref`, `description`, `checksum`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [JournalApprovalsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals-api/src/Http/Controllers/JournalApprovalsController.php) | `public function __construct(private readonly JournalApprovalQuery $query)`<br>`public function index(Request $request): JournalApprovalResource`<br>`public function store(Request $request, SubmitJournal $action): JournalApprovalResource`<br>`public function show(JournalApproval $approval): JournalApprovalResource`<br>`public function decide(Request $request, JournalApproval $approval, DecideJournal $action): JournalApprovalResource`<br>`public function post(Request $request, JournalApproval $approval, PostJournal $action): JournalApprovalResource`<br>`public function evidence(Request $request, JournalApproval $approval, AddEvidence $action): JournalApprovalResource`<br>`public function threshold(Request $request, ConfigureThreshold $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-journal-approvals-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])
Route::get('/', [JournalApprovalsController::class, 'index'])->name('accounting.journal-approvals.list');
Route::post('/', [JournalApprovalsController::class, 'store'])->name('accounting.journal-approvals.create');
Route::get('/{approval}', [JournalApprovalsController::class, 'show'])->name('accounting.journal-approvals.show');
Route::post('/{approval}/decide', [JournalApprovalsController::class, 'decide'])->name('accounting.journal-approvals.decide');
Route::post('/{approval}/post', [JournalApprovalsController::class, 'post'])->name('accounting.journal-approvals.post');
Route::post('/{approval}/evidence', [JournalApprovalsController::class, 'evidence'])->name('accounting.journal-approvals.evidence');
Route::post('/thresholds', [JournalApprovalsController::class, 'threshold'])->name('accounting.journal-approvals.threshold');
```
<!-- layer-implementation-plan:end -->

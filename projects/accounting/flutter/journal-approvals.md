# Journal Approvals Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#journal-approvals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-journal-approvals-flutter
**Matching core package:** module-accounting-journal-approvals ([implementation](../core/journal-approvals.md))
**Matching API package:** module-accounting-journal-approvals-api ([contract](../api/journal-approvals.md))

## Implementation plan

This adapter presents Journal Approvals for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Journal Approvals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/journal-approvals.md), and [API module](../api/journal-approvals.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `journal-approvals`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-journal-approvals-flutter`](https://github.com/liberusoftware/module-accounting-journal-approvals-flutter) (`module_accounting_journal_approvals_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-journal-approvals-dart-mobile`](https://github.com/liberusoftware/module-accounting-journal-approvals-dart-mobile) (`module_accounting_journal_approvals_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-journal-approvals-dart-desktop`](https://github.com/liberusoftware/module-accounting-journal-approvals-dart-desktop) (`module_accounting_journal_approvals_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/journal-approvals.md) · [Core plan](../core/journal-approvals.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Journal sources/types** | Adaptive mobile cards/sheets for `journal sources/types` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `journal sources/types` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Thresholds** | Adaptive mobile cards/sheets for `thresholds` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `thresholds` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Preparer/reviewer** | Adaptive mobile cards/sheets for `preparer/reviewer` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `preparer/reviewer` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Evidence** | Adaptive mobile cards/sheets for `evidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `evidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rejection** | Adaptive mobile cards/sheets for `rejection` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rejection` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Posting** | Adaptive mobile cards/sheets for `posting` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `posting` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Emergency controls** | Adaptive mobile cards/sheets for `emergency controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `emergency controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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

# Cms Translation Management React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-translation-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-translation-management-react-native
**Matching core package:** module-cms-cms-translation-management ([implementation](../core/cms-translation-management.md))
**Matching API package:** module-cms-cms-translation-management-api ([contract](../api/cms-translation-management.md))

## Implementation plan

This adapter presents Cms Translation Management for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Translation Management API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-translation-management.md), and [API module](../api/cms-translation-management.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-translation-management`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-translation-management.md)) |
| Capability React Native module skeleton | [`module-cms-translation-management-react-native`](https://github.com/liberusoftware/module-cms-translation-management-react-native) (`@liberusoftware/module-cms-translation-management-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Jobs** | Progressive mobile list/detail/sheet flow for `jobs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source changes** | Progressive mobile list/detail/sheet flow for `source changes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assignments** | Progressive mobile list/detail/sheet flow for `assignments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Vendor adapters** | Progressive mobile list/detail/sheet flow for `vendor adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Machine translation** | Progressive mobile list/detail/sheet flow for `machine translation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Review** | Progressive mobile list/detail/sheet flow for `review` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Memory/glossaries** | Progressive mobile list/detail/sheet flow for `memory/glossaries` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Status** | Progressive mobile list/detail/sheet flow for `status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cost** | Progressive mobile list/detail/sheet flow for `cost` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TranslationJobQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Queries/TranslationJobQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $publicId): ?TranslationJob` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TranslationManagementService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Actions/TranslationManagementService.php) | `public function __construct(private TranslationVendorRegistry $vendors)`<br>`public function createJob(array $attributes): TranslationJob`<br>`public function addSourceChange(TranslationJob $job, array $attributes): TranslationSourceChange`<br>`public function queue(TranslationJob $job): TranslationJob`<br>`public function cancel(TranslationJob $job): TranslationJob`<br>`public function translate(TranslationSourceChange $change, string $vendorKey, array $context = []): TranslationSourceChange`<br>`public function assign(TranslationSourceChange $change, string $assigneeType, int\|string $assigneeId, string $role, ?string $dueAt = null): TranslationAssignment`<br>`public function review(TranslationSourceChange $change, string $decision, ?string $notes = null): TranslationSourceChange`<br>`public function addVendor(array $attributes): TranslationVendor`<br>`public function remember(string $sourceLocale, string $targetLocale, string $sourceText, string $translatedText, array $metadata = [], int\|string\|null $teamId = null): TranslationMemory`<br>`public function glossary(array $attributes): TranslationGlossary`<br>`public function reconcile(TranslationJob $job): TranslationJob` |
| [TranslationVendorInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Contracts/TranslationVendorInterface.php) | `public function key(): string`<br>`public function translate(string $source, string $sourceLocale, string $targetLocale, array $context = []): TranslationResult` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TranslationAssignment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationAssignment.php) | `job_id`, `source_change_id`, `assignee_type`, `assignee_id`, `role`, `status`, `due_at`, `completed_at`, `team_id` |
| [TranslationGlossary.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationGlossary.php) | `source_locale`, `target_locale`, `source_term`, `preferred_term`, `forbidden_terms`, `team_id` |
| [TranslationJob.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationJob.php) | `public_id`, `external_key`, `name`, `source_locale`, `target_locale`, `status`, `vendor_key`, `total_units`, `completed_units`, `estimated_cost`, `actual_cost`, `currency`, `metadata`, `queued_at`, `completed_at`, `team_id` |
| [TranslationMemory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationMemory.php) | `source_locale`, `target_locale`, `source_hash`, `source_text`, `translated_text`, `status`, `metadata`, `team_id` |
| [TranslationSourceChange.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationSourceChange.php) | `job_id`, `subject_type`, `subject_id`, `field`, `source_text`, `source_hash`, `source_version`, `translated_text`, `translated_hash`, `status`, `provider`, `model`, `cost`, `provenance`, `review_notes`, `translated_at`, `reviewed_at`, `team_id` |
| [TranslationVendor.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationVendor.php) | `key`, `name`, `driver`, `settings`, `status`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TranslationManagementController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Controllers/TranslationManagementController.php) | `public function __construct(private TranslationJobQuery $jobs, private TranslationManagementService $service)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $publicId): TranslationJobResource`<br>`public function create(Request $request): TranslationJobResource`<br>`public function sourceChange(Request $request, string $publicId): TranslationSourceChangeResource`<br>`public function translate(Request $request, int $sourceChange): TranslationSourceChangeResource`<br>`public function review(Request $request, int $sourceChange): TranslationSourceChangeResource`<br>`public function reconcile(string $publicId): TranslationJobResource`<br>`public function queue(string $publicId): TranslationJobResource`<br>`public function cancel(string $publicId): TranslationJobResource`<br>`public function assign(Request $request, int $sourceChange): mixed`<br>`public function vendor(Request $request): TranslationVendorResource`<br>`public function memory(Request $request): TranslationMemoryResource`<br>`public function glossary(Request $request): TranslationGlossaryResource` |
<!-- layer-implementation-plan:end -->

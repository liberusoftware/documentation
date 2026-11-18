# Usage Wallet And Rebilling Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#usage-wallet-and-rebilling). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-usage-wallet-and-rebilling-flutter
**Matching core package:** module-crm-usage-wallet-and-rebilling ([implementation](../core/usage-wallet-and-rebilling.md))
**Matching API package:** module-crm-usage-wallet-and-rebilling-api ([contract](../api/usage-wallet-and-rebilling.md))

## Implementation plan

This adapter presents Usage Wallet And Rebilling for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Usage Wallet And Rebilling API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/usage-wallet-and-rebilling.md), and [API module](../api/usage-wallet-and-rebilling.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `usage-wallet-and-rebilling`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-usage-wallet-and-rebilling-flutter`](https://github.com/liberusoftware/module-crm-usage-wallet-and-rebilling-flutter) (`module_crm_usage_wallet_and_rebilling_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-usage-wallet-and-rebilling-dart-mobile`](https://github.com/liberusoftware/module-crm-usage-wallet-and-rebilling-dart-mobile) (`module_crm_usage_wallet_and_rebilling_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-usage-wallet-and-rebilling-dart-desktop`](https://github.com/liberusoftware/module-crm-usage-wallet-and-rebilling-dart-desktop) (`module_crm_usage_wallet_and_rebilling_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/usage-wallet-and-rebilling.md) · [Core plan](../core/usage-wallet-and-rebilling.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Provider usage imports** | Adaptive mobile cards/sheets for `provider usage imports` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider usage imports` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Wallets/credits** | Adaptive mobile cards/sheets for `wallets/credits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `wallets/credits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Threshold reloads** | Adaptive mobile cards/sheets for `threshold reloads` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `threshold reloads` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cost/markup rules** | Adaptive mobile cards/sheets for `cost/markup rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cost/markup rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Client charges** | Adaptive mobile cards/sheets for `client charges` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `client charges` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Exceptions** | Adaptive mobile cards/sheets for `exceptions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `exceptions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reconciliation** | Adaptive mobile cards/sheets for `reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Billing/Accounting handoff** | Adaptive mobile cards/sheets for `billing/accounting handoff` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `billing/accounting handoff` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [UsageWalletQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Queries/UsageWalletQuery.php) | `public function wallet(int $teamId): ?UsageWallet`<br>`public function imports(int $teamId)`<br>`public function charges(int $teamId)`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/CreateCharge.php) | `public function execute(int $teamId, int $actorId, array $data): UsageCharge` |
| [ImportProviderUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ImportProviderUsage.php) | `public function execute(int $teamId, int $actorId, array $data): UsageImport` |
| [ResolveUsageException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ResolveUsageException.php) | `public function execute(int $teamId, int $actorId, int $exceptionId): void` |
| [UpsertWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/UpsertWallet.php) | `public function execute(int $teamId, int $actorId, array $data): UsageWallet` |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsageAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [UsagePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsagePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageAudit.php) | `team_id`, `actor_id`, `event`, `details`, `request_id` |
| [UsageCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageCharge.php) | `team_id`, `usage_import_id`, `wallet_id`, `client_reference`, `cost`, `charge`, `currency`, `status` |
| [UsageImport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageImport.php) | `team_id`, `provider`, `external_id`, `amount`, `currency`, `status`, `failure_reason`, `payload` |
| [UsageWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageWallet.php) | `team_id`, `currency`, `balance`, `threshold`, `reload_amount`, `status`, `version` |

| Observed API controller | Handler signatures |
| --- | --- |
| [UsageWalletController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-api/src/Http/Controllers/UsageWalletController.php) | `public function summary(Request $r, UsageWalletQuery $q): JsonResponse`<br>`public function imports(Request $r, UsageWalletQuery $q): JsonResponse`<br>`public function charges(Request $r, UsageWalletQuery $q): JsonResponse`<br>`public function import(Request $r, ImportProviderUsage $a): JsonResponse`<br>`public function charge(Request $r, CreateCharge $a): JsonResponse`<br>`public function wallet(Request $r, UpsertWallet $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-usage-wallet-and-rebilling-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/usage-wallet-and-rebilling')->group(function () {
Route::get('/summary', [UsageWalletController::class, 'summary']);
Route::get('/imports', [UsageWalletController::class, 'imports']);
Route::post('/imports', [UsageWalletController::class, 'import']);
Route::get('/charges', [UsageWalletController::class, 'charges']);
Route::post('/charges', [UsageWalletController::class, 'charge']);
Route::put('/wallet', [UsageWalletController::class, 'wallet']);
```
<!-- layer-implementation-plan:end -->

# CRM: Crm Usage Wallet And Rebilling Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-usage-wallet-and-rebilling). Observed identity: [`liberusoftware/module-crm-usage-wallet-and-rebilling-filament`](../../../modules/source/liberusoftware--module-crm-usage-wallet-and-rebilling-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-usage-wallet-and-rebilling-filament`  
**Matching domain module:** `crm-usage-wallet-and-rebilling`  
**Application:** CRM  
**Source feature:** [Crm Usage Wallet And Rebilling](../features/crm-usage-wallet-and-rebilling.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-usage-wallet-and-rebilling` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider usage imports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Wallets/credits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Threshold reloads:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cost/markup rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Client charges:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exceptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Billing/Accounting handoff:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-usage-wallet-and-rebilling-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `provider-usage-imports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `wallets-credits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `threshold-reloads`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cost-markup-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `client-charges`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exceptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `billing-accounting-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-usage-wallet-and-rebilling` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-usage-wallet-and-rebilling-filament`](https://github.com/liberusoftware/module-crm-usage-wallet-and-rebilling-filament) (`liberusoftware/crm-usage-wallet-and-rebilling-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-usage-wallet-and-rebilling.md) · [API plan](../api/crm-usage-wallet-and-rebilling.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Provider usage imports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider usage imports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Wallets/credits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `wallets/credits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Threshold reloads** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `threshold reloads`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cost/markup rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cost/markup rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Client charges** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `client charges`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exceptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exceptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Billing/Accounting handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `billing/accounting handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [UsageWalletResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-filament/src/Resources/UsageWalletResource.php) · [EditUsageWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-filament/src/Resources/UsageWalletResource/Pages/EditUsageWallet.php) · [ListUsageWallets.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-filament/src/Resources/UsageWalletResource/Pages/ListUsageWallets.php) · [UsageWalletAndRebillingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-filament/src/UsageWalletAndRebillingFilamentServiceProvider.php).

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
<!-- layer-implementation-plan:end -->

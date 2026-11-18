# Accounting: Payment Reconciliation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-reconciliation). Observed identity: [`liberusoftware/module-accounting-payment-reconciliation-filament`](../../../modules/source/liberusoftware--module-accounting-payment-reconciliation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-payment-reconciliation-filament`  
**Matching domain module:** `accounting-payment-reconciliation`  
**Application:** Accounting  
**Source feature:** [Payment Reconciliation](../features/payment-reconciliation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-payment-reconciliation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Gateway/merchant settlement imports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gross-to-net fees/refunds/disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Matching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Missing items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider drift:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-payment-reconciliation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `gateway-merchant-settlement-imports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gross-to-net-fees-refunds-disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `matching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `missing-items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-drift`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-payment-reconciliation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-payment-reconciliation-filament`](https://github.com/liberusoftware/module-accounting-payment-reconciliation-filament) (`liberusoftware/accounting-payment-reconciliation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payment-reconciliation.md) · [API plan](../api/payment-reconciliation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Gateway/merchant settlement imports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gateway/merchant settlement imports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gross-to-net fees/refunds/disputes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gross-to-net fees/refunds/disputes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Matching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `matching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Missing items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `missing items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider drift** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider drift`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PaymentReconciliationFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-filament/src/PaymentReconciliationFilamentPlugin.php) · [PaymentReconciliationFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-filament/src/PaymentReconciliationFilamentServiceProvider.php) · [ListSettlementRuns.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-filament/src/Resources/Pages/ListSettlementRuns.php) · [SettlementRunResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-filament/src/Resources/SettlementRunResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SettlementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Queries/SettlementQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IdentifyMissingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/IdentifyMissingItems.php) | `public function handle(SettlementRun $run, array $expected): array` |
| [ImportSettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ImportSettlement.php) | `public function handle(array $attributes, array $items): SettlementRun` |
| [MatchSettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/MatchSettlementItem.php) | `public function handle(SettlementItem $item, string $referenceType, string $referenceId, float $amount, ?int $actorId = null, ?string $idempotencyKey = null): SettlementMatch` |
| [RecordProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/RecordProviderDrift.php) | `public function handle(SettlementRun $run, string $field, mixed $expected, mixed $actual, string $severity = 'warning'): ProviderDrift` |
| [ResolveReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ResolveReconciliationException.php) | `public function handle(ReconciliationException $exception, int $actorId, string $resolution, bool $waive = false): ReconciliationException` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AuditEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/AuditEvidence.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ProviderDrift.php) | `run_id`, `field`, `expected_value`, `actual_value`, `severity`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ReconciliationException.php) | `run_id`, `kind`, `external_ref`, `expected_amount`, `actual_amount`, `currency`, `status`, `severity`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [SettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementItem.php) | `run_id`, `external_ref`, `type`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `reference_type`, `reference_id`, `source_payload`, `source_hash`, `metadata` |
| [SettlementMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementMatch.php) | `run_id`, `item_id`, `reference_type`, `reference_id`, `matched_amount`, `confidence`, `status`, `matched_by`, `matched_at`, `idempotency_key`, `metadata` |
| [SettlementRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementRun.php) | `team_id`, `provider`, `merchant_ref`, `settlement_ref`, `period_start`, `period_end`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `idempotency_key`, `source_hash`, `failure_message`, `metadata` |
| [Payment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Models/Payment.php) | `invoice_id`, `payment_date`, `payment_amount`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id`, `journal_entry_id`, `team_id` |
<!-- layer-implementation-plan:end -->

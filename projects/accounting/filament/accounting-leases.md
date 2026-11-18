# Accounting: Accounting Leases Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-leases). Observed identity: [`liberusoftware/module-accounting-leases-filament`](../../../modules/source/liberusoftware--module-accounting-leases-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-leases-filament`  
**Matching domain module:** `accounting-leases`  
**Application:** Accounting  
**Source feature:** [Accounting Leases](../features/accounting-leases.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-leases` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Lease records:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Right-of-use assets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Liabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Interest/depreciation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Modifications:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disclosures (optional):** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-leases-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `lease-records`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `right-of-use-assets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `liabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `interest-depreciation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `modifications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disclosures-optional`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-leases` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-leases-filament`](https://github.com/liberusoftware/module-accounting-leases-filament) (`liberusoftware/accounting-leases-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-leases.md) · [API plan](../api/accounting-leases.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Lease records** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lease records`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Right-of-use assets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `right-of-use assets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Liabilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `liabilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Interest/depreciation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `interest/depreciation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Modifications** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `modifications`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disclosures (optional)** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disclosures (optional)`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [LeasesFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-filament/src/LeasesFilamentPlugin.php) · [LeasesFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-filament/src/LeasesFilamentServiceProvider.php) · [LeaseResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-filament/src/Resources/LeaseResource.php) · [ListLeases.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-filament/src/Resources/Pages/ListLeases.php).

| Observed core query | Public method signatures |
| --- | --- |
| [LeaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Queries/LeaseQuery.php) | `public function leases(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function disclosure(Lease $lease): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateDisclosure.php) | `public function handle(Lease $lease, string $asOfDate): LeaseDisclosure` |
| [CreateLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateLease.php) | `public function handle(array $attributes): Lease` |
| [GenerateSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/GenerateSchedule.php) | `public function handle(Lease $lease): Lease` |
| [ModifyLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/ModifyLease.php) | `public function handle(Lease $lease, array $attributes): Lease` |
| [PostPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/PostPayment.php) | `public function handle(LeasePayment $payment): LeasePayment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Lease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/Lease.php) | `team_id`, `lease_ref`, `name`, `lessor_ref`, `asset_ref`, `commencement_date`, `end_date`, `currency`, `payment_amount`, `payment_frequency`, `interest_rate`, `discount_rate`, `useful_life_months`, `status`, `right_of_use_asset`, `lease_liability`, `accumulated_depreciation`, `metadata` |
| [LeaseDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseDisclosure.php) | `lease_id`, `as_of_date`, `remaining_liability`, `current_liability`, `non_current_liability`, `future_payments`, `notes`, `metadata` |
| [LeaseModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseModification.php) | `lease_id`, `modification_ref`, `effective_date`, `kind`, `old_term_end`, `new_term_end`, `old_payment_amount`, `new_payment_amount`, `adjustment_amount`, `reason`, `metadata` |
| [LeasePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeasePayment.php) | `lease_id`, `payment_ref`, `due_date`, `amount`, `principal_amount`, `interest_amount`, `depreciation_amount`, `status`, `posted_at`, `metadata` |
<!-- layer-implementation-plan:end -->

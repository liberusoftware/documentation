# Accounting: Anomaly Detection Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#anomaly-detection). Observed identity: [`liberusoftware/module-accounting-anomaly-detection-filament`](../../../modules/source/liberusoftware--module-accounting-anomaly-detection-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-anomaly-detection-filament`  
**Matching domain module:** `accounting-anomaly-detection`  
**Application:** Accounting  
**Source feature:** [Anomaly Detection](../features/anomaly-detection.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-anomaly-detection` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Duplicates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unusual amounts/accounts/timing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Control breaches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Missing sequences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fraud indicators:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Review queues:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-anomaly-detection-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `duplicates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unusual-amounts-accounts-timing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `control-breaches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `missing-sequences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fraud-indicators`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `review-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-anomaly-detection` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-anomaly-detection-filament`](https://github.com/liberusoftware/module-accounting-anomaly-detection-filament) (`liberusoftware/accounting-anomaly-detection-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/anomaly-detection.md) · [API plan](../api/anomaly-detection.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Duplicates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Unusual amounts/accounts/timing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unusual amounts/accounts/timing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Control breaches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `control breaches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Missing sequences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `missing sequences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fraud indicators** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fraud indicators`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Review queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `review queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AnomalyDetectionFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-filament/src/AnomalyDetectionFilamentServiceProvider.php) · [AnomalyResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-filament/src/Resources/AnomalyResource.php) · [CreateAnomaly.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-filament/src/Resources/Pages/CreateAnomaly.php) · [ListAnomalies.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-filament/src/Resources/Pages/ListAnomalies.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AnomalyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Queries/AnomalyQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordAnomaly.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Actions/RecordAnomaly.php) | `public function handle(array $attributes): Anomaly` |
| [SendToReview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Actions/SendToReview.php) | `public function handle(Anomaly $anomaly): Anomaly` |
| [AnomalyPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-api/src/Policies/AnomalyPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Anomaly.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Models/Anomaly.php) | `team_id`, `kind`, `source_type`, `source_id`, `title`, `description`, `confidence`, `status`, `evidence`, `detected_at`, `resolved_at` |
<!-- layer-implementation-plan:end -->

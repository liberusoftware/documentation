# Accounting: Accounting Mileage Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-mileage). Observed identity: [`liberusoftware/module-accounting-mileage-filament`](../../../modules/source/liberusoftware--module-accounting-mileage-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-mileage-filament`  
**Matching domain module:** `accounting-mileage`  
**Application:** Accounting  
**Source feature:** [Accounting Mileage](../features/accounting-mileage.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-mileage` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Vehicles/rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trip capture/import:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Distance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Business purpose:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Projects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reimbursement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Regional reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-mileage-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `vehicles-rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trip-capture-import`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `distance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `business-purpose`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `projects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reimbursement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `regional-reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-mileage` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-mileage-filament`](https://github.com/liberusoftware/module-accounting-mileage-filament) (`liberusoftware/accounting-mileage-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-mileage.md) · [API plan](../api/accounting-mileage.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Vehicles/rates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `vehicles/rates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trip capture/import** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trip capture/import`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Distance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `distance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Business purpose** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `business purpose`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Projects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `projects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reimbursement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reimbursement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Regional reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regional reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MileageFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-filament/src/MileageFilamentPlugin.php) · [MileageFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-filament/src/MileageFilamentServiceProvider.php) · [MileageTripResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-filament/src/Resources/MileageTripResource.php) · [ListMileageTrips.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-filament/src/Resources/Pages/ListMileageTrips.php).

| Observed core query | Public method signatures |
| --- | --- |
| [MileageQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Queries/MileageQuery.php) | `public function trips(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function rates(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function regionalReport(?int $teamId = null, ?string $region = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ApproveTrip.php) | `public function handle(MileageTrip $trip, string $actor, bool $approved = true, ?string $reason = null): MileageTrip` |
| [CaptureTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CaptureTrip.php) | `public function handle(array $attributes): MileageTrip` |
| [CreateVehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CreateVehicle.php) | `public function handle(array $attributes): Vehicle` |
| [RecordMileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/RecordMileageRate.php) | `public function handle(array $attributes): MileageRate` |
| [ReimburseTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ReimburseTrip.php) | `public function handle(MileageTrip $trip, string $payee, ?string $externalRef = null): MileageReimbursement` |
| [SubmitTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/SubmitTrip.php) | `public function handle(MileageTrip $trip): MileageTrip` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MileageApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageApproval.php) | `trip_id`, `actor_ref`, `decision`, `reason`, `decided_at`, `metadata` |
| [MileagePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileagePolicy.php) | `team_id`, `name`, `region`, `max_distance_per_trip`, `max_distance_per_day`, `requires_purpose`, `requires_project`, `approval_threshold`, `currency`, `active`, `metadata` |
| [MileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageRate.php) | `team_id`, `region`, `vehicle_type`, `currency`, `rate_per_distance`, `effective_from`, `effective_until`, `active`, `metadata` |
| [MileageReimbursement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageReimbursement.php) | `trip_id`, `payee_ref`, `currency`, `amount`, `status`, `external_ref`, `failure_message`, `paid_at`, `metadata` |
| [MileageTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageTrip.php) | `team_id`, `trip_ref`, `employee_ref`, `vehicle_id`, `rate_id`, `policy_id`, `project_ref`, `origin`, `destination`, `trip_date`, `distance`, `distance_unit`, `business_purpose`, `region`, `currency`, `reimbursement_amount`, `status`, `source`, `source_hash`, `submitted_at`, `approved_at`, `reimbursed_at`, `metadata` |
| [Vehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/Vehicle.php) | `team_id`, `owner_ref`, `registration`, `make`, `model`, `fuel_type`, `co2_g_per_km`, `active`, `metadata` |
<!-- layer-implementation-plan:end -->

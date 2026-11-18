# CMS: Cms Analytics Integration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-analytics-integration). Observed identity: [`liberusoftware/module-cms-analytics-integration-filament`](../../../modules/source/liberusoftware--module-cms-analytics-integration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-analytics-integration-filament`  
**Matching domain module:** `cms-analytics-integration`  
**Application:** CMS  
**Source feature:** [Cms Analytics Integration](../features/cms-analytics-integration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-analytics-integration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Canonical content/view/conversion events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent-aware analytics mappings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dashboards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Boilerplate analytics adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-analytics-integration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `canonical-content-view-conversion-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent-aware-analytics-mappings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dashboards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `boilerplate-analytics-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-analytics-integration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-analytics-integration-filament`](https://github.com/liberusoftware/module-cms-analytics-integration-filament) (`liberusoftware/cms-analytics-integration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-analytics-integration.md) · [API plan](../api/cms-analytics-integration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Canonical content/view/conversion events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `canonical content/view/conversion events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent-aware analytics mappings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent-aware analytics mappings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dashboards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dashboards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Boilerplate analytics adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `boilerplate analytics adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AnalyticsIntegrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-analytics-integration-filament/src/AnalyticsIntegrationFilamentServiceProvider.php) · [AnalyticsEventResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-analytics-integration-filament/src/Resources/AnalyticsEventResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AnalyticsAdapterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Contracts/AnalyticsAdapterInterface.php) | `public function key(): string`<br>`public function payload(AnalyticsEvent $event, array $mapping): array` |
| [AnalyticsIntegrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Services/AnalyticsIntegrationService.php) | `public function recordEvent(?int $teamId, array $data): AnalyticsEvent`<br>`public function saveMapping(?int $teamId, array $data): AnalyticsMapping`<br>`public function dashboard(?int $teamId, ?string $from = null, ?string $to = null): array`<br>`public function registerAdapter(AnalyticsAdapterInterface $adapter): void`<br>`public function adapterPayload(string $provider, AnalyticsEvent $event, AnalyticsMapping $mapping): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsEvent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Models/AnalyticsEvent.php) | `team_id`, `event_type`, `event_name`, `subject_type`, `subject_id`, `consent_category`, `consent_granted`, `status`, `idempotency_key`, `payload`, `occurred_at` |
| [AnalyticsMapping.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Models/AnalyticsMapping.php) | `team_id`, `event_type`, `provider`, `measurement_key`, `consent_category`, `config`, `enabled` |
<!-- layer-implementation-plan:end -->

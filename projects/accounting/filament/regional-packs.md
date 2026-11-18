# Accounting: Regional Packs Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#regional-packs). Observed identity: [`liberusoftware/module-accounting-regional-packs-filament`](../../../modules/source/liberusoftware--module-accounting-regional-packs-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-regional-packs-filament`  
**Matching domain module:** `accounting-regional-packs`  
**Application:** Accounting  
**Source feature:** [Regional Packs](../features/regional-packs.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-regional-packs` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Country-specific tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Document formats:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filing calendars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terminology:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compliance tests:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-regional-packs-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `country-specific-tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `document-formats`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filing-calendars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terminology`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compliance-tests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-regional-packs` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-regional-packs-filament`](https://github.com/liberusoftware/module-accounting-regional-packs-filament) (`liberusoftware/accounting-regional-packs-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/regional-packs.md) · [API plan](../api/regional-packs.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Country-specific tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `country-specific tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Document formats** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `document formats`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Filing calendars** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `filing calendars`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Terminology** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terminology`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compliance tests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compliance tests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [RegionalPacksFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs-filament/src/RegionalPacksFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRegionalPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Actions/CreateRegionalPack.php) | `public function handle(array $attributes): RegionalPack` |
| [PublishRegionalPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Actions/PublishRegionalPack.php) | `public function handle(RegionalPack $pack, array $artifacts): RegionalPack` |
| [RunComplianceTests.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Actions/RunComplianceTests.php) | `public function handle(RegionalPack $pack): RegionalPack` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RegionalPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Models/RegionalPack.php) | `country_code`, `locale`, `currency`, `version`, `status`, `effective_from`, `effective_to`, `metadata` |
| [RegionalPackArtifact.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-regional-packs/src/Models/RegionalPackArtifact.php) | `pack_id`, `type`, `key`, `definition`, `status`, `test_results`, `metadata` |
<!-- layer-implementation-plan:end -->

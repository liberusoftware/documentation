# liberusoftware/analytics-core: shared adoption review

**Status:** source-backed consolidation design, not a completed migration or stability certification. This profile records differences at the pinned commits and a data-preserving adoption path. Active source projects are unchanged by this documentation review.

## Ownership and decision

The documentation owner is the [boilerplate capability scope](../../projects/boilerplate/README.md). Keep one authoritative capability/release boundary and product-specific behavior behind reviewed extensions. This is a documentation ownership decision; select the actual package maintainer/canonical release repository from verified package governance before changing consumers.

Runtime variants: **2**; selected metadata variants: **1** under this exact manifest identity. Equal names/constraints do not make different schemas or providers interchangeable. Keep the installed identity and its data until a compatible release or explicit migration is reviewed.

See the [implementation reference](../../modules/source/liberusoftware--analytics-core.md), [source comparison](../SHARED-MODULE-COMPARISON.md) and [consolidation procedure](../SHARED-MODULES.md).

## Consumer variants

| Consumer | Pinned module metadata | Variant | Test files |
| --- | --- | ---: | ---: |
| accounting | [analytics-core](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/composer.json) | 1 | 4 |
| automation | [analytics-core](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/analytics-core/composer.json) | 1 | 4 |
| billing | [analytics-core](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/analytics-core/composer.json) | 1 | 4 |
| boilerplate | [analytics-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/analytics-core/composer.json) | 1 | 4 |
| browser-game | [analytics-core](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/analytics-core/composer.json) | 1 | 4 |
| control-panel | [analytics-core](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/analytics-core/composer.json) | 1 | 4 |
| crm | [analytics-core](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/composer.json) | 2 | 4 |
| sap | [analytics-core](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-core/composer.json) | 1 | 4 |
| genealogy | [analytics-core](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/analytics-core/composer.json) | 1 | 4 |
| maintenance | [analytics-core](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/analytics-core/composer.json) | 1 | 4 |
| real-estate | [analytics-core](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-core/composer.json) | 1 | 4 |
| social-network | [analytics-core](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/analytics-core/composer.json) | 1 | 4 |

## Manifest and dependency differences

Each row below is one representative per runtime/metadata combination. Module defaults and providers are declarations, not proof of deployment enablement. Read the actual host resolver and registration path; changing defaults can change the selected graph without changing the application manifest.

| Variant | Module name / version | Default | Provider(s) | Composer runtime requirements |
| --- | --- | --- | --- | --- |
| 1 | `analytics-core` / `1.4.1` | `True` | `"Liberu\\Analytics\\Core\\AnalyticsServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/analytics-contracts": "^1.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 2 | `analytics-core` / `1.4.1` | `True` | `"Liberu\\Analytics\\Core\\AnalyticsServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/analytics-contracts": "^1.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |

## Persistence and data transition

The following database paths differ or are missing in at least one consumer. A missing file does not prove its table/data never existed, and a matching filename does not prove matching contents. Inspect migration history and the deployed database before adoption.

| Differing database path | Variant source and declared table operation |
| --- | --- |
| `database/migrations/2024_02_15_000004_create_reporting_tables.php` | V1: absent<br>V2: [227169d861](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/database/migrations/2024_02_15_000004_create_reporting_tables.php); create report_builders, create sales_forecasts, dropIfExists sales_forecasts, dropIfExists report_builders |
| `database/migrations/2024_10_22_000000_create_dashboard_widgets_table.php` | V1: absent<br>V2: [537fba7c1d](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/database/migrations/2024_10_22_000000_create_dashboard_widgets_table.php); create dashboard_widgets, dropIfExists dashboard_widgets |

Before a shared release, inventory affected tables/columns and tenant/source identifiers in every consumer, then map legacy/current record identities and callers. Use additive backfills or a separate migration with reconciliation and recovery; do not drop a historical table because the chosen package tree lacks its old migration. Reconcile counts, ownership and required evidence before moving callers or removing obsolete implementations.

**Legacy coupling:** 20 differing paths are under `src/Legacy/`. They remain potential runtime/data obligations until provider registration and host callers are traced. Keep product-owned legacy behavior in a documented product adapter/extension or migrate it deliberately; do not copy the entire legacy tree into a new universal foundation package.

Legacy review paths: `src/Legacy/Filament/App/Resources/AnalyticsDashboardResource.php`, `src/Legacy/Filament/App/Widgets/.gitignore`, `src/Legacy/Filament/App/Widgets/SocialLinksWidget.php`, `src/Legacy/Filament/Pages/ReportCustomizer.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/CreateAnalyticsDashboard.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/EditAnalyticsDashboard.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/ListAnalyticsDashboards.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/ViewAnalyticsDashboard.php`, `src/Legacy/Filament/Widgets/AdPerformanceWidget.php`, `src/Legacy/Http/Controllers/ReportController.php`, `src/Legacy/Http/Livewire/Dashboard.php`, `src/Legacy/Http/Livewire/ReportCustomizer.php`, `src/Legacy/Http/Livewire/Widgets/Stats.php`, `src/Legacy/Http/Livewire/Widgets/Tasks.php`, `src/Legacy/Livewire/Dashboard.php`, `src/Legacy/Livewire/ReportCustomizer.php`, `src/Legacy/Livewire/Widgets/Stats.php`, `src/Legacy/Livewire/Widgets/Tasks.php`, `src/Legacy/Models/DashboardWidget.php`, `src/Legacy/Models/ReportBuilder.php`.

## Public contract and extension review

No differing paths were found in the indexed contract/action/query/service/context roots. Review the provider, models, adapters and manifest differences below; this is not a claim of complete behavioral equivalence.

Resolve host-model lookups, actor/tenant policy, source-record references and provider dependencies through explicit public contracts/configuration. Keep product policy and presentation composition outside shared core. Consumer tests must cover the real call paths, including jobs/exports and private-data visibility; do not widen a contract solely to accommodate one host's internal model.

## Registration, route and presentation review

No registration/route/resource path difference was classified. Inspect other changed paths and host wiring before claiming adapter parity.

Validate discovery, manifest schema/version handling, dependency selection, provider boot order and route/plugin identifiers against the consuming host. For UI/API adapters, retain the authorized DTO and domain action semantics rather than exposing private models or bypassing transitions through generic record saves.

React/Inertia and Next.js can share framework-independent components, not page/session/redirect lifecycles. If a shared adapter is proposed, review all relevant variants and declared peers/exports first; a shared documentation home is not a completed code migration.

## Adoption sequence and acceptance

1. Confirm the canonical maintainer/release source and supported versions, then compare every source variant above with its actual host callers and schema. Keep the existing installed identities until that decision is reviewed.
2. Separate genuine shared behavior from product-specific legacy/adapters. Define the required extension points and map source-record IDs/data before removing or redirecting a caller.
3. Release compatible changes or an explicitly versioned migration. Test a clean consumer and upgrade/recovery path without local dependency overrides; package version strings and source tests are not release evidence.
4. Adopt one consumer through a targeted dependency/lockfile update, verify data reconciliation and meaningful permitted/denied/tenant/retry journeys, then expand to other consumers.
5. Record package/source versions, schema/data transition, retained extensions, checks run, remaining limitations and operational recovery. Preserve tracked installed trees and all documented product capabilities until callers/data have moved.

The current documentation supplies source comparisons and a consolidation design. Application refactoring, migration execution, package publication and certification of a stable common release remain separate owning-project work.

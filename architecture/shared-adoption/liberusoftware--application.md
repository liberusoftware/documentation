# liberusoftware/application: shared adoption review

**Status:** source-backed consolidation design, not a completed migration or stability certification. This profile records differences at the pinned commits and a data-preserving adoption path. Active source projects are unchanged by this documentation review.

## Ownership and decision

The documentation owner is the [boilerplate capability scope](../../projects/boilerplate/README.md). Keep one authoritative capability/release boundary and product-specific behavior behind reviewed extensions. This is a documentation ownership decision; select the actual package maintainer/canonical release repository from verified package governance before changing consumers.

Runtime variants: **3**; selected metadata variants: **1** under this exact manifest identity. Equal names/constraints do not make different schemas or providers interchangeable. Keep the installed identity and its data until a compatible release or explicit migration is reviewed.

See the [implementation reference](../../modules/source/liberusoftware--application.md), [source comparison](../SHARED-MODULE-COMPARISON.md) and [consolidation procedure](../SHARED-MODULES.md).

## Consumer variants

| Consumer | Pinned module metadata | Variant | Test files |
| --- | --- | ---: | ---: |
| accounting | [application](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/composer.json) | 3 | 1 |
| automation | [application](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/composer.json) | 2 | 1 |
| billing | [application](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/application/composer.json) | 2 | 1 |
| boilerplate | [application](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/application/composer.json) | 2 | 1 |
| browser-game | [application](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/application/composer.json) | 2 | 1 |
| control-panel | [application](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/application/composer.json) | 2 | 1 |
| crm | [application](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/composer.json) | 1 | 10 |
| sap | [application](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/application/composer.json) | 2 | 1 |
| genealogy | [application](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/application/composer.json) | 2 | 1 |
| maintenance | [application](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/application/composer.json) | 2 | 1 |
| real-estate | [application](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/application/composer.json) | 2 | 1 |
| social-network | [application](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/application/composer.json) | 2 | 1 |

## Manifest and dependency differences

Each row below is one representative per runtime/metadata combination. Module defaults and providers are declarations, not proof of deployment enablement. Read the actual host resolver and registration path; changing defaults can change the selected graph without changing the application manifest.

| Variant | Module name / version | Default | Provider(s) | Composer runtime requirements |
| --- | --- | --- | --- | --- |
| 1 | `application` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApplicationCore\\ApplicationCoreServiceProvider"` | `{"illuminate/http": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 2 | `application` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApplicationCore\\ApplicationCoreServiceProvider"` | `{"illuminate/http": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 3 | `application` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApplicationCore\\ApplicationCoreServiceProvider"` | `{"illuminate/http": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |

## Persistence and data transition

The following database paths differ or are missing in at least one consumer. A missing file does not prove its table/data never existed, and a matching filename does not prove matching contents. Inspect migration history and the deployed database before adoption.

| Differing database path | Variant source and declared table operation |
| --- | --- |
| `database/migrations/0001_01_01_000001_create_cache_table.php` | V1: [627513417f](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/database/migrations/0001_01_01_000001_create_cache_table.php); create cache, create cache_locks, dropIfExists cache, dropIfExists cache_locks<br>V2: absent<br>V3: absent |
| `database/migrations/0001_01_01_000002_create_jobs_table.php` | V1: [758acd3f7a](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/database/migrations/0001_01_01_000002_create_jobs_table.php); create jobs, create job_batches, create failed_jobs, dropIfExists jobs, dropIfExists job_batches, dropIfExists failed_jobs<br>V2: absent<br>V3: absent |
| `database/migrations/2019_09_15_000010_create_tenants_table.php` | V1: [737b110129](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/database/migrations/2019_09_15_000010_create_tenants_table.php); create tenants, dropIfExists tenants<br>V2: absent<br>V3: absent |
| `database/seeders/DatabaseSeeder.php` | V1: [49e276a32c](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/database/seeders/DatabaseSeeder.php); inspect file (no literal Schema operation indexed)<br>V2: absent<br>V3: absent |

Before a shared release, inventory affected tables/columns and tenant/source identifiers in every consumer, then map legacy/current record identities and callers. Use additive backfills or a separate migration with reconciliation and recovery; do not drop a historical table because the chosen package tree lacks its old migration. Reconcile counts, ownership and required evidence before moving callers or removing obsolete implementations.

**Legacy coupling:** 25 differing paths are under `src/Legacy/`. They remain potential runtime/data obligations until provider registration and host callers are traced. Keep product-owned legacy behavior in a documented product adapter/extension or migrate it deliberately; do not copy the entire legacy tree into a new universal foundation package.

Legacy review paths: `src/Legacy/Console/Commands/FreshDatabaseCommand.php`, `src/Legacy/Console/Commands/MakeModuleCommand.php`, `src/Legacy/Console/Commands/ModuleAutoloadCommand.php`, `src/Legacy/Console/Commands/ModuleCommand.php`, `src/Legacy/Contracts/OwnsRecords.php`, `src/Legacy/Filament/Concerns/EnforcesResourcePermissions.php`, `src/Legacy/Filament/ModulePlugins.php`, `src/Legacy/Http/Controllers/Controller.php`, `src/Legacy/Http/Controllers/HomeController.php`, `src/Legacy/Http/Middleware/Authenticate.php`, `src/Legacy/Http/Middleware/EncryptCookies.php`, `src/Legacy/Http/Middleware/PreventRequestsDuringMaintenance.php`, `src/Legacy/Http/Middleware/RedirectIfAuthenticated.php`, `src/Legacy/Http/Middleware/RoleBasedRedirect.php`, `src/Legacy/Http/Middleware/SecurityHeaders.php`, `src/Legacy/Http/Middleware/TrimStrings.php`, `src/Legacy/Http/Middleware/TrustHosts.php`, `src/Legacy/Http/Middleware/TrustProxies.php`, `src/Legacy/Http/Middleware/ValidateSignature.php`, `src/Legacy/Http/Middleware/VerifyCsrfToken.php`, `src/Legacy/Models/Tenant.php`, `src/Legacy/Support/PiiEncryptionBackfill.php`, `src/Legacy/Support/SchemaGraph.php`, `src/Legacy/View/Components/AppLayout.php`, `src/Legacy/View/Components/GuestLayout.php`.

## Public contract and extension review

No differing paths were found in the indexed contract/action/query/service/context roots. Review the provider, models, adapters and manifest differences below; this is not a claim of complete behavioral equivalence.

Resolve host-model lookups, actor/tenant policy, source-record references and provider dependencies through explicit public contracts/configuration. Keep product policy and presentation composition outside shared core. Consumer tests must cover the real call paths, including jobs/exports and private-data visibility; do not widen a contract solely to accommodate one host's internal model.

## Registration, route and presentation review

- `src/ApplicationCoreServiceProvider.php`: V1 [source](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/ApplicationCoreServiceProvider.php), V2 [source](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/ApplicationCoreServiceProvider.php), V3 [source](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/ApplicationCoreServiceProvider.php)

Validate discovery, manifest schema/version handling, dependency selection, provider boot order and route/plugin identifiers against the consuming host. For UI/API adapters, retain the authorized DTO and domain action semantics rather than exposing private models or bypassing transitions through generic record saves.

React/Inertia and Next.js can share framework-independent components, not page/session/redirect lifecycles. If a shared adapter is proposed, review all relevant variants and declared peers/exports first; a shared documentation home is not a completed code migration.

## Adoption sequence and acceptance

1. Confirm the canonical maintainer/release source and supported versions, then compare every source variant above with its actual host callers and schema. Keep the existing installed identities until that decision is reviewed.
2. Separate genuine shared behavior from product-specific legacy/adapters. Define the required extension points and map source-record IDs/data before removing or redirecting a caller.
3. Release compatible changes or an explicitly versioned migration. Test a clean consumer and upgrade/recovery path without local dependency overrides; package version strings and source tests are not release evidence.
4. Adopt one consumer through a targeted dependency/lockfile update, verify data reconciliation and meaningful permitted/denied/tenant/retry journeys, then expand to other consumers.
5. Record package/source versions, schema/data transition, retained extensions, checks run, remaining limitations and operational recovery. Preserve tracked installed trees and all documented product capabilities until callers/data have moved.

The current documentation supplies source comparisons and a consolidation design. Application refactoring, migration execution, package publication and certification of a stable common release remain separate owning-project work.

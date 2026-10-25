# liberusoftware/audit: shared adoption review

**Status:** source-backed consolidation design, not a completed migration or stability certification. This profile records differences at the pinned commits and a data-preserving adoption path. Active source projects are unchanged by this documentation review.

## Ownership and decision

The documentation owner is the [boilerplate capability scope](../../projects/boilerplate/README.md). Keep one authoritative capability/release boundary and product-specific behavior behind reviewed extensions. This is a documentation ownership decision; select the actual package maintainer/canonical release repository from verified package governance before changing consumers.

Runtime variants: **5**; selected metadata variants: **1** under this exact manifest identity. Equal names/constraints do not make different schemas or providers interchangeable. Keep the installed identity and its data until a compatible release or explicit migration is reviewed.

See the [implementation reference](../../modules/source/liberusoftware--audit.md), [source comparison](../SHARED-MODULE-COMPARISON.md) and [consolidation procedure](../SHARED-MODULES.md).

## Consumer variants

| Consumer | Pinned module metadata | Variant | Test files |
| --- | --- | ---: | ---: |
| accounting | [audit](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/audit/composer.json) | 5 | 1 |
| automation | [audit](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit/composer.json) | 4 | 1 |
| billing | [audit](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/audit/composer.json) | 2 | 1 |
| boilerplate | [audit](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/audit/composer.json) | 4 | 1 |
| browser-game | [audit](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/audit/composer.json) | 4 | 1 |
| control-panel | [audit](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/audit/composer.json) | 4 | 1 |
| crm | [audit](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit/composer.json) | 1 | 3 |
| sap | [audit](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/audit/composer.json) | 4 | 1 |
| genealogy | [audit](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/audit/composer.json) | 3 | 1 |
| maintenance | [audit](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/audit/composer.json) | 4 | 1 |
| real-estate | [audit](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/audit/composer.json) | 4 | 1 |
| social-network | [audit](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/audit/composer.json) | 4 | 1 |

## Manifest and dependency differences

Each row below is one representative per runtime/metadata combination. Module defaults and providers are declarations, not proof of deployment enablement. Read the actual host resolver and registration path; changing defaults can change the selected graph without changing the application manifest.

| Variant | Module name / version | Default | Provider(s) | Composer runtime requirements |
| --- | --- | --- | --- | --- |
| 1 | `audit` / `1.4.1` | `True` | `"Liberu\\Foundation\\Audit\\AuditServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 2 | `audit` / `1.4.1` | `True` | `"Liberu\\Foundation\\Audit\\AuditServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 3 | `audit` / `1.4.1` | `True` | `"Liberu\\Foundation\\Audit\\AuditServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 4 | `audit` / `1.4.1` | `True` | `"Liberu\\Foundation\\Audit\\AuditServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 5 | `audit` / `1.4.1` | `True` | `"Liberu\\Foundation\\Audit\\AuditServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |

## Persistence and data transition

The following database paths differ or are missing in at least one consumer. A missing file does not prove its table/data never existed, and a matching filename does not prove matching contents. Inspect migration history and the deployed database before adoption.

| Differing database path | Variant source and declared table operation |
| --- | --- |
| `database/factories/AuditLogFactory.php` | V1: [79df68476e](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit/database/factories/AuditLogFactory.php); inspect file (no literal Schema operation indexed)<br>V2: absent<br>V3: absent<br>V4: absent<br>V5: absent |
| `database/migrations/2024_10_13_020000_create_audit_logs_table.php` | V1: [f0bf9e8858](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit/database/migrations/2024_10_13_020000_create_audit_logs_table.php); create audit_logs, dropIfExists audit_logs<br>V2: absent<br>V3: absent<br>V4: absent<br>V5: absent |
| `database/migrations/2026_06_29_124053_create_activity_log_table.php` | V1: [c1a21562ac](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit/database/migrations/2026_06_29_124053_create_activity_log_table.php); create activity_log<br>V2: [38c5a0b35c](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/audit/database/migrations/2026_06_29_124053_create_activity_log_table.php); create activity_log<br>V3: [38c5a0b35c](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/audit/database/migrations/2026_06_29_124053_create_activity_log_table.php); create activity_log<br>V4: [38c5a0b35c](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit/database/migrations/2026_06_29_124053_create_activity_log_table.php); create activity_log<br>V5: [38c5a0b35c](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/audit/database/migrations/2026_06_29_124053_create_activity_log_table.php); create activity_log |
| `database/migrations/2026_07_06_130000_add_auditable_columns_to_audit_logs.php` | V1: [4f0b91f120](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit/database/migrations/2026_07_06_130000_add_auditable_columns_to_audit_logs.php); table audit_logs, table audit_logs<br>V2: absent<br>V3: absent<br>V4: absent<br>V5: absent |

Before a shared release, inventory affected tables/columns and tenant/source identifiers in every consumer, then map legacy/current record identities and callers. Use additive backfills or a separate migration with reconciliation and recovery; do not drop a historical table because the chosen package tree lacks its old migration. Reconcile counts, ownership and required evidence before moving callers or removing obsolete implementations.

**Legacy coupling:** 10 differing paths are under `src/Legacy/`. They remain potential runtime/data obligations until provider registration and host callers are traced. Keep product-owned legacy behavior in a documented product adapter/extension or migrate it deliberately; do not copy the entire legacy tree into a new universal foundation package.

Legacy review paths: `src/Legacy/Filament/Admin/Resources/AuditLogResource.php`, `src/Legacy/Filament/App/Resources/AuditLogResource.php`, `src/Legacy/Filament/App/Resources/AuditLogResource/Pages/ListAuditLogs.php`, `src/Legacy/Filament/App/Resources/AuditLogResource/Pages/ViewAuditLog.php`, `src/Legacy/Filament/Resources/AuditLogResource/Pages/ListAuditLogs.php`, `src/Legacy/Filament/Resources/AuditLogResource/Pages/ViewAuditLog.php`, `src/Legacy/Models/AuditLog.php`, `src/Legacy/Observers/AuditObserver.php`, `src/Legacy/Observers/TaskObserver.php`, `src/Legacy/Services/AuditLogService.php`.

## Public contract and extension review

Changed action/query/contract/service/context paths are indexed below. Signature differences identify compatibility work; equal signatures alone do not prove matching authorization, validation, side effects or event timing.

| Path | Variant entry points |
| --- | --- |
| `src/Support/ModelAuditListener.php` | V1: absent<br>V2: absent<br>V3: [ModelAuditListener.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/audit/src/Support/ModelAuditListener.php) — `public function handle(string $event, array $payload): void`<br>V4: absent<br>V5: absent |

Resolve host-model lookups, actor/tenant policy, source-record references and provider dependencies through explicit public contracts/configuration. Keep product policy and presentation composition outside shared core. Consumer tests must cover the real call paths, including jobs/exports and private-data visibility; do not widen a contract solely to accommodate one host's internal model.

## Registration, route and presentation review

- `src/AuditServiceProvider.php`: V1 [source](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit/src/AuditServiceProvider.php), V2 [source](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/audit/src/AuditServiceProvider.php), V3 [source](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/audit/src/AuditServiceProvider.php), V4 [source](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit/src/AuditServiceProvider.php), V5 [source](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/audit/src/AuditServiceProvider.php)

Validate discovery, manifest schema/version handling, dependency selection, provider boot order and route/plugin identifiers against the consuming host. For UI/API adapters, retain the authorized DTO and domain action semantics rather than exposing private models or bypassing transitions through generic record saves.

React/Inertia and Next.js can share framework-independent components, not page/session/redirect lifecycles. If a shared adapter is proposed, review all relevant variants and declared peers/exports first; a shared documentation home is not a completed code migration.

## Adoption sequence and acceptance

1. Confirm the canonical maintainer/release source and supported versions, then compare every source variant above with its actual host callers and schema. Keep the existing installed identities until that decision is reviewed.
2. Separate genuine shared behavior from product-specific legacy/adapters. Define the required extension points and map source-record IDs/data before removing or redirecting a caller.
3. Release compatible changes or an explicitly versioned migration. Test a clean consumer and upgrade/recovery path without local dependency overrides; package version strings and source tests are not release evidence.
4. Adopt one consumer through a targeted dependency/lockfile update, verify data reconciliation and meaningful permitted/denied/tenant/retry journeys, then expand to other consumers.
5. Record package/source versions, schema/data transition, retained extensions, checks run, remaining limitations and operational recovery. Preserve tracked installed trees and all documented product capabilities until callers/data have moved.

The current documentation supplies source comparisons and a consolidation design. Application refactoring, migration execution, package publication and certification of a stable common release remain separate owning-project work.

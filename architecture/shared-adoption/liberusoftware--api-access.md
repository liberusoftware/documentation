# liberusoftware/api-access: shared adoption review

**Status:** source-backed consolidation design, not a completed migration or stability certification. This profile records differences at the pinned commits and a data-preserving adoption path. Active source projects are unchanged by this documentation review.

## Ownership and decision

The documentation owner is the [boilerplate capability scope](../../projects/boilerplate/README.md). Keep one authoritative capability/release boundary and product-specific behavior behind reviewed extensions. This is a documentation ownership decision; select the actual package maintainer/canonical release repository from verified package governance before changing consumers.

Runtime variants: **6**; selected metadata variants: **1** under this exact manifest identity. Equal names/constraints do not make different schemas or providers interchangeable. Keep the installed identity and its data until a compatible release or explicit migration is reviewed.

See the [implementation reference](../../modules/source/liberusoftware--api-access.md), [source comparison](../SHARED-MODULE-COMPARISON.md) and [consolidation procedure](../SHARED-MODULES.md).

## Consumer variants

| Consumer | Pinned module metadata | Variant | Test files |
| --- | --- | ---: | ---: |
| accounting | [api-access](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/api-access/composer.json) | 1 | 1 |
| automation | [api-access](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/api-access/composer.json) | 1 | 1 |
| billing | [api-access](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/api-access/composer.json) | 2 | 1 |
| boilerplate | [api-access](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/api-access/composer.json) | 1 | 1 |
| browser-game | [api-access](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/api-access/composer.json) | 1 | 1 |
| control-panel | [api-access](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/api-access/composer.json) | 3 | 1 |
| crm | [api-access](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access/composer.json) | 4 | 1 |
| sap | [api-access](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/api-access/composer.json) | 1 | 1 |
| genealogy | [api-access](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/api-access/composer.json) | 5 | 1 |
| maintenance | [api-access](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/api-access/composer.json) | 1 | 1 |
| real-estate | [api-access](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access/composer.json) | 6 | 1 |
| social-network | [api-access](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/api-access/composer.json) | 1 | 1 |

## Manifest and dependency differences

Each row below is one representative per runtime/metadata combination. Module defaults and providers are declarations, not proof of deployment enablement. Read the actual host resolver and registration path; changing defaults can change the selected graph without changing the application manifest.

| Variant | Module name / version | Default | Provider(s) | Composer runtime requirements |
| --- | --- | --- | --- | --- |
| 1 | `api-access` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApiAccess\\ApiAccessServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "laravel/sanctum": "^4.0", "liberusoftware/identity-core": "^1.0", "php": "^8.5"}` |
| 2 | `api-access` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApiAccess\\ApiAccessServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "laravel/sanctum": "^4.0", "liberusoftware/identity-core": "^1.0", "php": "^8.5"}` |
| 3 | `api-access` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApiAccess\\ApiAccessServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "laravel/sanctum": "^4.0", "liberusoftware/identity-core": "^1.0", "php": "^8.5"}` |
| 4 | `api-access` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApiAccess\\ApiAccessServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "laravel/sanctum": "^4.0", "liberusoftware/identity-core": "^1.0", "php": "^8.5"}` |
| 5 | `api-access` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApiAccess\\ApiAccessServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "laravel/sanctum": "^4.0", "liberusoftware/identity-core": "^1.0", "php": "^8.5"}` |
| 6 | `api-access` / `1.4.1` | `True` | `"Liberu\\Foundation\\ApiAccess\\ApiAccessServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "laravel/sanctum": "^4.0", "liberusoftware/identity-core": "^1.0", "php": "^8.5"}` |

## Persistence and data transition

The following database paths differ or are missing in at least one consumer. A missing file does not prove its table/data never existed, and a matching filename does not prove matching contents. Inspect migration history and the deployed database before adoption.

| Differing database path | Variant source and declared table operation |
| --- | --- |
| `database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php` | V1: [6e479c5e4a](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/api-access/database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php); create personal_access_tokens, dropIfExists personal_access_tokens<br>V2: [6e479c5e4a](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/api-access/database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php); create personal_access_tokens, dropIfExists personal_access_tokens<br>V3: [6e479c5e4a](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/api-access/database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php); create personal_access_tokens, dropIfExists personal_access_tokens<br>V4: [421278ed69](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access/database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php); create personal_access_tokens, dropIfExists personal_access_tokens<br>V5: [6e479c5e4a](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/api-access/database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php); create personal_access_tokens, dropIfExists personal_access_tokens<br>V6: [6e479c5e4a](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access/database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php); create personal_access_tokens, dropIfExists personal_access_tokens |

Before a shared release, inventory affected tables/columns and tenant/source identifiers in every consumer, then map legacy/current record identities and callers. Use additive backfills or a separate migration with reconciliation and recovery; do not drop a historical table because the chosen package tree lacks its old migration. Reconcile counts, ownership and required evidence before moving callers or removing obsolete implementations.

## Public contract and extension review

Changed action/query/contract/service/context paths are indexed below. Signature differences identify compatibility work; equal signatures alone do not prove matching authorization, validation, side effects or event timing.

| Path | Variant entry points |
| --- | --- |
| `src/Support/IdempotencyStore.php` | V1: [IdempotencyStore.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/api-access/src/Support/IdempotencyStore.php) — `public function begin(string $identity, string $key, string $requestBody): ?object` ; `public function complete(string $identity, string $key, int $status, string $body): void`<br>V2: [IdempotencyStore.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/api-access/src/Support/IdempotencyStore.php) — `public function begin(string $identity, string $key, string $requestBody): ?object` ; `public function complete(string $identity, string $key, int $status, string $body): void`<br>V3: [IdempotencyStore.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/api-access/src/Support/IdempotencyStore.php) — `public function begin(string $identity, string $key, string $requestBody): ?object` ; `public function complete(string $identity, string $key, int $status, string $body): void`<br>V4: [IdempotencyStore.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access/src/Support/IdempotencyStore.php) — `public function begin(string $identity, string $key, string $requestBody): ?object` ; `public function complete(string $identity, string $key, int $status, string $body): void`<br>V5: [IdempotencyStore.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/api-access/src/Support/IdempotencyStore.php) — `public function begin(string $identity, string $key, string $requestBody): ?object` ; `public function complete(string $identity, string $key, int $status, string $body): void` ; `public function forget(string $identity, string $key): void`<br>V6: [IdempotencyStore.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access/src/Support/IdempotencyStore.php) — `public function begin(string $identity, string $key, string $requestBody): ?object` ; `public function complete(string $identity, string $key, int $status, string $body): void` |

Resolve host-model lookups, actor/tenant policy, source-record references and provider dependencies through explicit public contracts/configuration. Keep product policy and presentation composition outside shared core. Consumer tests must cover the real call paths, including jobs/exports and private-data visibility; do not widen a contract solely to accommodate one host's internal model.

## Registration, route and presentation review

- `src/ApiAccessServiceProvider.php`: V1 [source](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/api-access/src/ApiAccessServiceProvider.php), V2 [source](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/api-access/src/ApiAccessServiceProvider.php), V3 [source](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/api-access/src/ApiAccessServiceProvider.php), V4 [source](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access/src/ApiAccessServiceProvider.php), V5 [source](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/api-access/src/ApiAccessServiceProvider.php), V6 [source](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access/src/ApiAccessServiceProvider.php)

Validate discovery, manifest schema/version handling, dependency selection, provider boot order and route/plugin identifiers against the consuming host. For UI/API adapters, retain the authorized DTO and domain action semantics rather than exposing private models or bypassing transitions through generic record saves.

React/Inertia and Next.js can share framework-independent components, not page/session/redirect lifecycles. If a shared adapter is proposed, review all relevant variants and declared peers/exports first; a shared documentation home is not a completed code migration.

## Adoption sequence and acceptance

1. Confirm the canonical maintainer/release source and supported versions, then compare every source variant above with its actual host callers and schema. Keep the existing installed identities until that decision is reviewed.
2. Separate genuine shared behavior from product-specific legacy/adapters. Define the required extension points and map source-record IDs/data before removing or redirecting a caller.
3. Release compatible changes or an explicitly versioned migration. Test a clean consumer and upgrade/recovery path without local dependency overrides; package version strings and source tests are not release evidence.
4. Adopt one consumer through a targeted dependency/lockfile update, verify data reconciliation and meaningful permitted/denied/tenant/retry journeys, then expand to other consumers.
5. Record package/source versions, schema/data transition, retained extensions, checks run, remaining limitations and operational recovery. Preserve tracked installed trees and all documented product capabilities until callers/data have moved.

The current documentation supplies source comparisons and a consolidation design. Application refactoring, migration execution, package publication and certification of a stable common release remain separate owning-project work.

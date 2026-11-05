# liberusoftware/identity-core-filament: shared adoption review

**Status:** source-backed consolidation design, not a completed migration or stability certification. This profile records differences at the pinned commits and a data-preserving adoption path. Active source projects are unchanged by this documentation review.

## Ownership and decision

The documentation owner is the [boilerplate capability scope](../../projects/boilerplate/README.md). Keep one authoritative capability/release boundary and product-specific behavior behind reviewed extensions. This is a documentation ownership decision; select the actual package maintainer/canonical release repository from verified package governance before changing consumers.

Runtime variants: **2**; selected metadata variants: **2** under this exact manifest identity. Equal names/constraints do not make different schemas or providers interchangeable. Keep the installed identity and its data until a compatible release or explicit migration is reviewed.

See the [implementation reference](../../modules/source/liberusoftware--identity-core-filament.md), [source comparison](../SHARED-MODULE-COMPARISON.md) and [consolidation procedure](../SHARED-MODULES.md).

## Consumer variants

| Consumer | Pinned module metadata | Variant | Test files |
| --- | --- | ---: | ---: |
| accounting | [identity-core-filament](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/composer.json) | 2 | 6 |
| automation | [identity-core-filament](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/identity-core-filament/composer.json) | 2 | 6 |
| billing | [identity-core-filament](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/identity-core-filament/composer.json) | 2 | 6 |
| boilerplate | [identity-core-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-core-filament/composer.json) | 2 | 6 |
| browser-game | [identity-core-filament](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/identity-core-filament/composer.json) | 2 | 6 |
| control-panel | [identity-core-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/identity-core-filament/composer.json) | 2 | 6 |
| crm | [identity-core-filament](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core-filament/composer.json) | 2 | 6 |
| sap | [identity-core-filament](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-core-filament/composer.json) | 2 | 6 |
| genealogy | [identity-core-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-core-filament/composer.json) | 2 | 6 |
| maintenance | [identity-core-filament](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/identity-core-filament/composer.json) | 2 | 6 |
| real-estate | [identity-core-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/composer.json) | 1 | 6 |
| social-network | [identity-core-filament](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/identity-core-filament/composer.json) | 2 | 6 |

## Manifest and dependency differences

Each row below is one representative per runtime/metadata combination. Module defaults and providers are declarations, not proof of deployment enablement. Read the actual host resolver and registration path; changing defaults can change the selected graph without changing the application manifest.

| Variant | Module name / version | Default | Provider(s) | Composer runtime requirements |
| --- | --- | --- | --- | --- |
| 1 | `identity-core-filament` / `1.4.1` | `True` | `"Liberu\\Foundation\\IdentityFilament\\IdentityFilamentServiceProvider"` | `{"filament/filament": "^5.1", "liberusoftware/organizations-teams": "^1.0", "liberusoftware/roles-permissions": "^1.0", "php": "^8.5"}` |
| 2 | `identity-core-filament` / `1.4.1` | `True` | `"Liberu\\Foundation\\IdentityFilament\\IdentityFilamentServiceProvider"` | `{"filament/filament": "^5.1", "liberusoftware/roles-permissions": "^1.0", "php": "^8.5"}` |

## Persistence and data transition

No database path differs within the comparison roots. This does not prove statelessness or schema equivalence in deployed consumers; check unchanged migrations, models and host-owned tables referenced by the changed runtime code.

## Public contract and extension review

No differing paths were found in the indexed contract/action/query/service/context roots. Review the provider, models, adapters and manifest differences below; this is not a claim of complete behavioral equivalence.

Resolve host-model lookups, actor/tenant policy, source-record references and provider dependencies through explicit public contracts/configuration. Keep product policy and presentation composition outside shared core. Consumer tests must cover the real call paths, including jobs/exports and private-data visibility; do not widen a contract solely to accommodate one host's internal model.

## Registration, route and presentation review

- `module.json`: V1 [source](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/module.json), V2 [source](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/module.json)

Validate discovery, manifest schema/version handling, dependency selection, provider boot order and route/plugin identifiers against the consuming host. For UI/API adapters, retain the authorized DTO and domain action semantics rather than exposing private models or bypassing transitions through generic record saves.

React/Inertia and Next.js can share framework-independent components, not page/session/redirect lifecycles. If a shared adapter is proposed, review all relevant variants and declared peers/exports first; a shared documentation home is not a completed code migration.

## Adoption sequence and acceptance

1. Confirm the canonical maintainer/release source and supported versions, then compare every source variant above with its actual host callers and schema. Keep the existing installed identities until that decision is reviewed.
2. Separate genuine shared behavior from product-specific legacy/adapters. Define the required extension points and map source-record IDs/data before removing or redirecting a caller.
3. Release compatible changes or an explicitly versioned migration. Test a clean consumer and upgrade/recovery path without local dependency overrides; package version strings and source tests are not release evidence.
4. Adopt one consumer through a targeted dependency/lockfile update, verify data reconciliation and meaningful permitted/denied/tenant/retry journeys, then expand to other consumers.
5. Record package/source versions, schema/data transition, retained extensions, checks run, remaining limitations and operational recovery. Preserve tracked installed trees and all documented product capabilities until callers/data have moved.

The current documentation supplies source comparisons and a consolidation design. Application refactoring, migration execution, package publication and certification of a stable common release remain separate owning-project work.

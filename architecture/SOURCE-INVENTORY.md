# Source module inventory

These records come from public `liberusoftware` repositories ending in `-laravel`, discovered through the paginated GitHub organization repositories API on 2026-10-25 and cloned into `/home/liberu/projects`. Commit-pinned links identify the scanned source. Source presence does not establish stability or registry availability.

## Reproduce the scan

Keep `repositories.json` in the projects directory as the discovery input. Refresh that list from every page of `https://api.github.com/orgs/liberusoftware/repos?per_page=100`, selecting names ending in `-laravel`. Clone missing repositories, then run:

```bash
python3 tools/sync_source_inventory.py --projects /home/liberu/projects
```

The scanner rejects dirty checkouts, records each HEAD, inspects immediate children of `modules/`, and reads their `composer.json` and `package.json`. It also records tracked files under application source roots and manifest paths outside `modules/`. It does not install or execute package code. Directories without either manifest remain visible. Dependencies, scripts, and source path lists are preserved in [the machine-readable snapshot](source-inventory.json). Semantic capability mapping still requires reading the code: a directory count cannot establish whether a capability exists.

Compatibility symlinks are recorded as aliases of their repository-local target. They remain visible in project tables, but shared-identity and source comparisons count the actual target once. Non-package directories are not installable packages merely because they occur under `modules/`.

**Ecommerce preservation rule:** its documented module catalogue remains intact. Its implementations also live under `app/`, routes, and resources; see the [Ecommerce application capability map](../projects/ecommerce/SOURCE-APPLICATION.md). Do not remove or downgrade a documented module because it is absent from the immediate `modules/` scan.

## Project coverage

| Repository | Commit | Immediate module directories | Inventory |
| --- | --- | ---: | --- |
| accounting-erp-laravel | `39a49babafc0b8caf12c018abdd765f215ecf207` | 466 | [accounting](../projects/accounting/SOURCE-MODULES.md) |
| automation-laravel | `68e5f07a67041f8438530c71bc86515cbd11da70` | 100 | [automation](../projects/automation/SOURCE-MODULES.md) |
| billing-laravel | `4743bdfebd1c122e10bf80171d0210ab27e34a54` | 146 | [billing](../projects/billing/SOURCE-MODULES.md) |
| boilerplate-laravel | `3ade34046c3de1e2f0fc8e498a2451241c0584dc` | 40 | [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) |
| browser-game-laravel | `790fdffebd3a19bf914aea8a4ef049f87f52c62d` | 100 | [browser-game](../projects/browser-game/SOURCE-MODULES.md) |
| cms-laravel | `5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7` | 357 | [cms](../projects/cms/SOURCE-MODULES.md) |
| control-panel-laravel | `1797f25d705f780bacddcdf228c9a1dc995c3580` | 100 | [control-panel](../projects/control-panel/SOURCE-MODULES.md) |
| crm-laravel | `63aad94e94c0f9a18038e301eb979138c657be64` | 500 | [crm](../projects/crm/SOURCE-MODULES.md) |
| ecommerce-laravel | `af5a2b29c9c26ba89c97b9daccbb3facf20a8c2f` | 0 | [ecommerce](../projects/ecommerce/SOURCE-MODULES.md) |
| enterprise-sap-laravel | `b12a8c841c6a9054e52cac99d9ac1f233924a041` | 40 | [sap](../projects/sap/SOURCE-MODULES.md) |
| genealogy-laravel | `577e93db23cc969fd532086c06524f9f2bb2b5ea` | 113 | [genealogy](../projects/genealogy/SOURCE-MODULES.md) |
| maintenance-laravel | `c267d625e264e86ad223be8a3a08a3728afc7344` | 96 | [maintenance](../projects/maintenance/SOURCE-MODULES.md) |
| real-estate-laravel | `178d8015b601c99dec43acfdc12724aae2b3731a` | 197 | [real-estate](../projects/real-estate/SOURCE-MODULES.md) |
| social-network-laravel | `08bbc484b50fc7e841a499375329c6de32614145` | 101 | [social-network](../projects/social-network/SOURCE-MODULES.md) |

## Repeated package identities

The same identity in multiple applications is a candidate for one shared owner and release stream. Compare source, migrations, dependencies, tests, and compatibility before consolidating. Matching names alone do not prove identical behavior. Applications should consume shared packages rather than publish divergent copies under the same identity.

| Manifest | Package | Source applications |
| --- | --- | --- |
| composer.json | `liberusoftware/activity-comments` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/activity-comments-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/activity-comments-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/activity-comments-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-core` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/analytics-core-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-core-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-core-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-google` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/analytics-google-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-google-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-google-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-meta` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/analytics-meta-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-meta-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/analytics-meta-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/api-access` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/api-access-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/api-access-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/api-access-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/application` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/application-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/application-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/application-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/audit` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/audit-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/audit-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/audit-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/currency-context` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/currency-context-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/currency-context-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/currency-context-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/developer-experience` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/developer-experience-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/developer-experience-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/developer-experience-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/feature-flags` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/feature-flags-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/feature-flags-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/feature-flags-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/files-media` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/files-media-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/files-media-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/files-media-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/identity-core` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/identity-core-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/identity-core-filament` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/identity-core-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/identity-socialstream` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/import-export` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/import-export-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/import-export-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/import-export-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/integrations` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/integrations-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/integrations-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/integrations-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/jetstream-bridge` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/jetstream-bridge-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/jetstream-bridge-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/jetstream-bridge-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/localization-core` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/localization-core-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/localization-core-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/localization-core-livewire` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/localization-mymemory` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/module-billing-billing-core` | billing-laravel, billing-laravel |
| composer.json | `liberusoftware/module-liberu-business-workflow-reconciliation` | accounting-erp-laravel, billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-business-workflow-reconciliation-api` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-business-workflow-reconciliation-filament` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-business-workflow-reconciliation-livewire` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-executive-insights` | accounting-erp-laravel, billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-executive-insights-api` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-executive-insights-filament` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-executive-insights-livewire` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-platform-orchestration` | accounting-erp-laravel, billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-platform-orchestration-api` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-platform-orchestration-filament` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-platform-orchestration-livewire` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-revenue-and-care-orchestration` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-revenue-and-care-orchestration-api` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-revenue-and-care-orchestration-filament` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-liberu-revenue-and-care-orchestration-livewire` | billing-laravel, billing-laravel, genealogy-laravel |
| composer.json | `liberusoftware/module-manager` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/module-manager-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/module-manager-filament` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/module-manager-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/notifications` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/notifications-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/notifications-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/notifications-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/observability` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/observability-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/observability-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/observability-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/organizations-teams` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/organizations-teams-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/organizations-teams-filament` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/organizations-teams-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/profiles` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/profiles-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/profiles-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/profiles-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/roles-permissions` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/roles-permissions-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/roles-permissions-filament` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/roles-permissions-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/scheduler-queues` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/scheduler-queues-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/scheduler-queues-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/scheduler-queues-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/search` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/search-api` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/search-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/search-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/sessions-devices` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/sessions-devices-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/sessions-devices-filament` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/sessions-devices-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/settings` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/settings-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/settings-filament` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/settings-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/theme-support` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/theme-support-livewire` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/two-factor-authentication` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/two-factor-authentication-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/two-factor-authentication-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/two-factor-authentication-livewire` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/webhooks` | accounting-erp-laravel, automation-laravel, billing-laravel, boilerplate-laravel, browser-game-laravel, control-panel-laravel, crm-laravel, enterprise-sap-laravel, genealogy-laravel, maintenance-laravel, real-estate-laravel, social-network-laravel |
| composer.json | `liberusoftware/webhooks-api` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/webhooks-filament` | crm-laravel, real-estate-laravel |
| composer.json | `liberusoftware/webhooks-livewire` | crm-laravel, real-estate-laravel |

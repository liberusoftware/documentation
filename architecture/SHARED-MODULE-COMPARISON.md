# Shared module source comparison

This report compares repeated manifest identities in the [source inventory](SOURCE-INVENTORY.md). It measures tracked file equality at pinned commits; it does not execute code or establish behavioral compatibility.

Compared **133 repeated identities**: **89 have matching runtime files and selected runtime metadata**; **44 differ in at least one of those dimensions**. Equal files still require consumer integration and migration checks before consolidation.

## Method and reproduction

Run `python3 tools/compare_shared_modules.py --projects /home/liberu/projects` after regenerating the source inventory. Dirty checkouts and changed HEADs are rejected.

Runtime comparison includes `src/`, `database/`, `routes/`, `resources/`, `config/`, `lang/`, and `module.json`. Each relative filename and its SHA-256 content digest contribute to the group fingerprint. Selected Composer/npm runtime metadata is compared separately; tests have separate fingerprints. Documentation, release metadata, root build tools, and other files outside those roots are not part of the runtime equality claim. A version/default change in `module.json` counts as a difference.

See [the machine-readable comparisons](shared-module-comparison.json) for all locations, digests, file counts, and differing paths. Read the [reuse and consolidation guide](SHARED-MODULES.md) before changing dependencies.

## Identity summary

| Package | Copies | Runtime variants | Metadata variants | Differing runtime paths |
| --- | ---: | ---: | ---: | ---: |
| [liberusoftware/activity-comments](#package-1) | 12 | 1 | 1 | 0 |
| [liberusoftware/activity-comments-api](#package-2) | 2 | 1 | 1 | 0 |
| [liberusoftware/activity-comments-filament](#package-3) | 2 | 1 | 1 | 0 |
| [liberusoftware/activity-comments-livewire](#package-4) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-core](#package-5) | 12 | 2 | 1 | 22 |
| [liberusoftware/analytics-core-api](#package-6) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-core-filament](#package-7) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-core-livewire](#package-8) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-google](#package-9) | 12 | 1 | 1 | 0 |
| [liberusoftware/analytics-google-api](#package-10) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-google-filament](#package-11) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-google-livewire](#package-12) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-meta](#package-13) | 12 | 1 | 1 | 0 |
| [liberusoftware/analytics-meta-api](#package-14) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-meta-filament](#package-15) | 2 | 1 | 1 | 0 |
| [liberusoftware/analytics-meta-livewire](#package-16) | 2 | 1 | 1 | 0 |
| [liberusoftware/api-access](#package-17) | 12 | 6 | 1 | 6 |
| [liberusoftware/api-access-api](#package-18) | 2 | 1 | 1 | 0 |
| [liberusoftware/api-access-filament](#package-19) | 2 | 1 | 1 | 0 |
| [liberusoftware/api-access-livewire](#package-20) | 2 | 1 | 1 | 0 |
| [liberusoftware/application](#package-21) | 12 | 3 | 1 | 32 |
| [liberusoftware/application-api](#package-22) | 2 | 1 | 1 | 0 |
| [liberusoftware/application-filament](#package-23) | 2 | 1 | 1 | 0 |
| [liberusoftware/application-livewire](#package-24) | 2 | 1 | 1 | 0 |
| [liberusoftware/audit](#package-25) | 12 | 5 | 1 | 17 |
| [liberusoftware/audit-api](#package-26) | 2 | 1 | 1 | 0 |
| [liberusoftware/audit-filament](#package-27) | 2 | 1 | 1 | 0 |
| [liberusoftware/audit-livewire](#package-28) | 2 | 1 | 1 | 0 |
| [liberusoftware/currency-context](#package-29) | 12 | 2 | 1 | 1 |
| [liberusoftware/currency-context-api](#package-30) | 2 | 1 | 1 | 0 |
| [liberusoftware/currency-context-filament](#package-31) | 2 | 1 | 1 | 0 |
| [liberusoftware/currency-context-livewire](#package-32) | 2 | 1 | 1 | 0 |
| [liberusoftware/developer-experience](#package-33) | 12 | 1 | 1 | 0 |
| [liberusoftware/developer-experience-api](#package-34) | 2 | 1 | 1 | 0 |
| [liberusoftware/developer-experience-filament](#package-35) | 2 | 1 | 1 | 0 |
| [liberusoftware/developer-experience-livewire](#package-36) | 2 | 1 | 1 | 0 |
| [liberusoftware/feature-flags](#package-37) | 12 | 1 | 1 | 0 |
| [liberusoftware/feature-flags-api](#package-38) | 2 | 1 | 1 | 0 |
| [liberusoftware/feature-flags-filament](#package-39) | 2 | 1 | 1 | 0 |
| [liberusoftware/feature-flags-livewire](#package-40) | 2 | 1 | 1 | 0 |
| [liberusoftware/files-media](#package-41) | 12 | 1 | 1 | 0 |
| [liberusoftware/files-media-api](#package-42) | 2 | 1 | 1 | 0 |
| [liberusoftware/files-media-filament](#package-43) | 2 | 1 | 1 | 0 |
| [liberusoftware/files-media-livewire](#package-44) | 2 | 1 | 1 | 0 |
| [liberusoftware/identity-core](#package-45) | 12 | 2 | 1 | 30 |
| [liberusoftware/identity-core-api](#package-46) | 2 | 2 | 2 | 4 |
| [liberusoftware/identity-core-filament](#package-47) | 12 | 2 | 2 | 3 |
| [liberusoftware/identity-core-livewire](#package-48) | 2 | 1 | 1 | 0 |
| [liberusoftware/identity-socialstream](#package-49) | 12 | 3 | 1 | 17 |
| [liberusoftware/import-export](#package-50) | 12 | 2 | 1 | 9 |
| [liberusoftware/import-export-api](#package-51) | 2 | 1 | 1 | 0 |
| [liberusoftware/import-export-filament](#package-52) | 2 | 1 | 1 | 0 |
| [liberusoftware/import-export-livewire](#package-53) | 2 | 1 | 1 | 0 |
| [liberusoftware/integrations](#package-54) | 12 | 3 | 1 | 105 |
| [liberusoftware/integrations-api](#package-55) | 2 | 1 | 1 | 0 |
| [liberusoftware/integrations-filament](#package-56) | 2 | 1 | 1 | 0 |
| [liberusoftware/integrations-livewire](#package-57) | 2 | 1 | 1 | 0 |
| [liberusoftware/jetstream-bridge](#package-58) | 12 | 1 | 1 | 0 |
| [liberusoftware/jetstream-bridge-api](#package-59) | 2 | 1 | 1 | 0 |
| [liberusoftware/jetstream-bridge-filament](#package-60) | 2 | 1 | 1 | 0 |
| [liberusoftware/jetstream-bridge-livewire](#package-61) | 2 | 1 | 1 | 0 |
| [liberusoftware/localization-core](#package-62) | 12 | 4 | 1 | 1 |
| [liberusoftware/localization-core-api](#package-63) | 2 | 1 | 1 | 0 |
| [liberusoftware/localization-core-filament](#package-64) | 2 | 1 | 1 | 0 |
| [liberusoftware/localization-core-livewire](#package-65) | 12 | 1 | 1 | 0 |
| [liberusoftware/localization-mymemory](#package-66) | 12 | 1 | 1 | 0 |
| [liberusoftware/module-billing-billing-core](#package-67) | 2 | 2 | 1 | 1 |
| [liberusoftware/module-liberu-business-workflow-reconciliation](#package-68) | 4 | 3 | 3 | 15 |
| [liberusoftware/module-liberu-business-workflow-reconciliation-api](#package-69) | 3 | 2 | 1 | 4 |
| [liberusoftware/module-liberu-business-workflow-reconciliation-filament](#package-70) | 3 | 2 | 1 | 3 |
| [liberusoftware/module-liberu-business-workflow-reconciliation-livewire](#package-71) | 3 | 2 | 1 | 2 |
| [liberusoftware/module-liberu-executive-insights](#package-72) | 4 | 3 | 3 | 14 |
| [liberusoftware/module-liberu-executive-insights-api](#package-73) | 3 | 2 | 1 | 4 |
| [liberusoftware/module-liberu-executive-insights-filament](#package-74) | 3 | 2 | 1 | 3 |
| [liberusoftware/module-liberu-executive-insights-livewire](#package-75) | 3 | 2 | 1 | 2 |
| [liberusoftware/module-liberu-platform-orchestration](#package-76) | 4 | 3 | 3 | 18 |
| [liberusoftware/module-liberu-platform-orchestration-api](#package-77) | 3 | 2 | 1 | 4 |
| [liberusoftware/module-liberu-platform-orchestration-filament](#package-78) | 3 | 2 | 1 | 3 |
| [liberusoftware/module-liberu-platform-orchestration-livewire](#package-79) | 3 | 2 | 1 | 2 |
| [liberusoftware/module-liberu-revenue-and-care-orchestration](#package-80) | 3 | 2 | 2 | 8 |
| [liberusoftware/module-liberu-revenue-and-care-orchestration-api](#package-81) | 3 | 2 | 1 | 4 |
| [liberusoftware/module-liberu-revenue-and-care-orchestration-filament](#package-82) | 3 | 2 | 1 | 3 |
| [liberusoftware/module-liberu-revenue-and-care-orchestration-livewire](#package-83) | 3 | 2 | 1 | 2 |
| [liberusoftware/module-manager](#package-84) | 12 | 4 | 1 | 11 |
| [liberusoftware/module-manager-api](#package-85) | 2 | 1 | 1 | 0 |
| [liberusoftware/module-manager-filament](#package-86) | 12 | 3 | 1 | 2 |
| [liberusoftware/module-manager-livewire](#package-87) | 2 | 1 | 1 | 0 |
| [liberusoftware/notifications](#package-88) | 12 | 2 | 1 | 10 |
| [liberusoftware/notifications-api](#package-89) | 2 | 1 | 1 | 0 |
| [liberusoftware/notifications-filament](#package-90) | 2 | 1 | 1 | 0 |
| [liberusoftware/notifications-livewire](#package-91) | 2 | 1 | 1 | 0 |
| [liberusoftware/observability](#package-92) | 12 | 1 | 1 | 0 |
| [liberusoftware/observability-api](#package-93) | 2 | 1 | 1 | 0 |
| [liberusoftware/observability-filament](#package-94) | 2 | 1 | 1 | 0 |
| [liberusoftware/observability-livewire](#package-95) | 2 | 1 | 1 | 0 |
| [liberusoftware/organizations-teams](#package-96) | 12 | 3 | 1 | 96 |
| [liberusoftware/organizations-teams-api](#package-97) | 2 | 1 | 1 | 0 |
| [liberusoftware/organizations-teams-filament](#package-98) | 12 | 2 | 1 | 1 |
| [liberusoftware/organizations-teams-livewire](#package-99) | 2 | 1 | 1 | 0 |
| [liberusoftware/profiles](#package-100) | 12 | 1 | 1 | 0 |
| [liberusoftware/profiles-api](#package-101) | 2 | 1 | 1 | 0 |
| [liberusoftware/profiles-filament](#package-102) | 2 | 1 | 1 | 0 |
| [liberusoftware/profiles-livewire](#package-103) | 2 | 1 | 1 | 0 |
| [liberusoftware/roles-permissions](#package-104) | 12 | 2 | 2 | 11 |
| [liberusoftware/roles-permissions-api](#package-105) | 2 | 1 | 1 | 0 |
| [liberusoftware/roles-permissions-filament](#package-106) | 12 | 1 | 1 | 0 |
| [liberusoftware/roles-permissions-livewire](#package-107) | 2 | 1 | 1 | 0 |
| [liberusoftware/scheduler-queues](#package-108) | 12 | 2 | 1 | 2 |
| [liberusoftware/scheduler-queues-api](#package-109) | 2 | 1 | 1 | 0 |
| [liberusoftware/scheduler-queues-filament](#package-110) | 2 | 1 | 1 | 0 |
| [liberusoftware/scheduler-queues-livewire](#package-111) | 2 | 1 | 1 | 0 |
| [liberusoftware/search](#package-112) | 12 | 7 | 1 | 5 |
| [liberusoftware/search-api](#package-113) | 12 | 1 | 1 | 0 |
| [liberusoftware/search-filament](#package-114) | 2 | 1 | 1 | 0 |
| [liberusoftware/search-livewire](#package-115) | 2 | 1 | 1 | 0 |
| [liberusoftware/sessions-devices](#package-116) | 12 | 2 | 1 | 2 |
| [liberusoftware/sessions-devices-api](#package-117) | 2 | 1 | 1 | 0 |
| [liberusoftware/sessions-devices-filament](#package-118) | 12 | 2 | 2 | 3 |
| [liberusoftware/sessions-devices-livewire](#package-119) | 2 | 1 | 1 | 0 |
| [liberusoftware/settings](#package-120) | 12 | 5 | 1 | 24 |
| [liberusoftware/settings-api](#package-121) | 2 | 1 | 1 | 0 |
| [liberusoftware/settings-filament](#package-122) | 12 | 2 | 1 | 1 |
| [liberusoftware/settings-livewire](#package-123) | 2 | 1 | 1 | 0 |
| [liberusoftware/theme-support](#package-124) | 12 | 5 | 1 | 4 |
| [liberusoftware/theme-support-livewire](#package-125) | 12 | 1 | 1 | 0 |
| [liberusoftware/two-factor-authentication](#package-126) | 12 | 2 | 1 | 1 |
| [liberusoftware/two-factor-authentication-api](#package-127) | 2 | 1 | 1 | 0 |
| [liberusoftware/two-factor-authentication-filament](#package-128) | 2 | 1 | 1 | 0 |
| [liberusoftware/two-factor-authentication-livewire](#package-129) | 2 | 1 | 1 | 0 |
| [liberusoftware/webhooks](#package-130) | 12 | 3 | 2 | 7 |
| [liberusoftware/webhooks-api](#package-131) | 2 | 1 | 1 | 0 |
| [liberusoftware/webhooks-filament](#package-132) | 2 | 1 | 1 | 0 |
| [liberusoftware/webhooks-livewire](#package-133) | 2 | 1 | 1 | 0 |

## Source locations and review paths

<a id="package-1"></a>

### liberusoftware/activity-comments

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/activity-comments) | 6 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/activity-comments) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/activity-comments) | 6 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/activity-comments) | 6 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/activity-comments) | 6 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/activity-comments) | 6 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/activity-comments) | 6 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/activity-comments) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/activity-comments) | 6 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/activity-comments) | 6 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/activity-comments) | 6 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [activity-comments](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/activity-comments) | 6 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-2"></a>

### liberusoftware/activity-comments-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [activity-comments-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/activity-comments-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [activity-comments-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/activity-comments-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-3"></a>

### liberusoftware/activity-comments-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [activity-comments-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/activity-comments-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [activity-comments-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/activity-comments-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-4"></a>

### liberusoftware/activity-comments-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [activity-comments-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/activity-comments-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [activity-comments-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/activity-comments-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-5"></a>

### liberusoftware/analytics-core

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core) | 7 | 4 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/analytics-core) | 7 | 4 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/analytics-core) | 7 | 4 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/analytics-core) | 7 | 4 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/analytics-core) | 7 | 4 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/analytics-core) | 7 | 4 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core) | 29 | 4 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-core) | 7 | 4 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/analytics-core) | 7 | 4 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/analytics-core) | 7 | 4 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-core) | 7 | 4 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/analytics-core) | 7 | 4 |

Review paths: `database/migrations/2024_02_15_000004_create_reporting_tables.php`, `database/migrations/2024_10_22_000000_create_dashboard_widgets_table.php`, `src/Legacy/Filament/App/Resources/AnalyticsDashboardResource.php`, `src/Legacy/Filament/App/Widgets/.gitignore`, `src/Legacy/Filament/App/Widgets/SocialLinksWidget.php`, `src/Legacy/Filament/Pages/ReportCustomizer.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/CreateAnalyticsDashboard.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/EditAnalyticsDashboard.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/ListAnalyticsDashboards.php`, `src/Legacy/Filament/Resources/AnalyticsDashboardResource/Pages/ViewAnalyticsDashboard.php`, `src/Legacy/Filament/Widgets/AdPerformanceWidget.php`, `src/Legacy/Http/Controllers/ReportController.php` (plus 10 more in the JSON report).

<a id="package-6"></a>

### liberusoftware/analytics-core-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-core-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-core-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-core-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-7"></a>

### liberusoftware/analytics-core-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-core-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-core-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-core-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-8"></a>

### liberusoftware/analytics-core-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-core-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-core-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-core-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-9"></a>

### liberusoftware/analytics-google

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-google) | 5 | 4 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/analytics-google) | 5 | 4 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/analytics-google) | 5 | 4 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/analytics-google) | 5 | 4 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/analytics-google) | 5 | 4 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/analytics-google) | 5 | 4 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-google) | 5 | 4 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-google) | 5 | 4 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/analytics-google) | 5 | 4 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/analytics-google) | 5 | 4 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-google) | 5 | 4 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [analytics-google](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/analytics-google) | 5 | 4 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-10"></a>

### liberusoftware/analytics-google-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-google-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-google-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-google-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-google-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-11"></a>

### liberusoftware/analytics-google-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-google-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-google-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-google-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-google-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-12"></a>

### liberusoftware/analytics-google-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-google-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-google-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-google-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-google-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-13"></a>

### liberusoftware/analytics-meta

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-meta) | 5 | 4 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/analytics-meta) | 5 | 4 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/analytics-meta) | 5 | 4 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/analytics-meta) | 5 | 4 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/analytics-meta) | 5 | 4 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/analytics-meta) | 5 | 4 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-meta) | 5 | 4 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-meta) | 5 | 4 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/analytics-meta) | 5 | 4 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/analytics-meta) | 5 | 4 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-meta) | 5 | 4 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [analytics-meta](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/analytics-meta) | 5 | 4 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-14"></a>

### liberusoftware/analytics-meta-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-meta-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-meta-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-meta-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-meta-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-15"></a>

### liberusoftware/analytics-meta-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-meta-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-meta-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-meta-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-meta-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-16"></a>

### liberusoftware/analytics-meta-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [analytics-meta-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-meta-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [analytics-meta-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-meta-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-17"></a>

### liberusoftware/api-access

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/api-access) | 8 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/api-access) | 8 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/api-access) | 9 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/api-access) | 8 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/api-access) | 8 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/api-access) | 8 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access) | 8 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/api-access) | 8 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/api-access) | 9 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/api-access) | 8 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access) | 9 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [api-access](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/api-access) | 8 | 1 |

Review paths: `database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php`, `src/ApiAccessServiceProvider.php`, `src/Http/Middleware/ApiContract.php`, `src/Http/Middleware/Idempotency.php`, `src/Http/Middleware/ReplayIdempotentRequest.php`, `src/Support/IdempotencyStore.php`.

<a id="package-18"></a>

### liberusoftware/api-access-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [api-access-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [api-access-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-19"></a>

### liberusoftware/api-access-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [api-access-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [api-access-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-20"></a>

### liberusoftware/api-access-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [api-access-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [api-access-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-21"></a>

### liberusoftware/application

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application) | 15 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application) | 13 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/application) | 13 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/application) | 13 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/application) | 13 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/application) | 13 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/application) | 42 | 10 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/application) | 13 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/application) | 13 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/application) | 13 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/application) | 13 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/application) | 13 | 1 |

Review paths: `database/migrations/0001_01_01_000001_create_cache_table.php`, `database/migrations/0001_01_01_000002_create_jobs_table.php`, `database/migrations/2019_09_15_000010_create_tenants_table.php`, `database/seeders/DatabaseSeeder.php`, `src/ApplicationCoreServiceProvider.php`, `src/Legacy/Console/Commands/FreshDatabaseCommand.php`, `src/Legacy/Console/Commands/MakeModuleCommand.php`, `src/Legacy/Console/Commands/ModuleAutoloadCommand.php`, `src/Legacy/Console/Commands/ModuleCommand.php`, `src/Legacy/Contracts/OwnsRecords.php`, `src/Legacy/Filament/Concerns/EnforcesResourcePermissions.php`, `src/Legacy/Filament/ModulePlugins.php` (plus 20 more in the JSON report).

<a id="package-22"></a>

### liberusoftware/application-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [application-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/application-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [application-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/application-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-23"></a>

### liberusoftware/application-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [application-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/application-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [application-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/application-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-24"></a>

### liberusoftware/application-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [application-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/application-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [application-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/application-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-25"></a>

### liberusoftware/audit

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/audit) | 8 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit) | 7 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/audit) | 8 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/audit) | 7 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/audit) | 7 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/audit) | 7 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit) | 20 | 3 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/audit) | 7 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/audit) | 8 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/audit) | 7 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/audit) | 7 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [audit](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/audit) | 7 | 1 |

Review paths: `database/factories/AuditLogFactory.php`, `database/migrations/2024_10_13_020000_create_audit_logs_table.php`, `database/migrations/2026_06_29_124053_create_activity_log_table.php`, `database/migrations/2026_07_06_130000_add_auditable_columns_to_audit_logs.php`, `src/AuditServiceProvider.php`, `src/Legacy/Filament/Admin/Resources/AuditLogResource.php`, `src/Legacy/Filament/App/Resources/AuditLogResource.php`, `src/Legacy/Filament/App/Resources/AuditLogResource/Pages/ListAuditLogs.php`, `src/Legacy/Filament/App/Resources/AuditLogResource/Pages/ViewAuditLog.php`, `src/Legacy/Filament/Resources/AuditLogResource/Pages/ListAuditLogs.php`, `src/Legacy/Filament/Resources/AuditLogResource/Pages/ViewAuditLog.php`, `src/Legacy/Models/AuditLog.php` (plus 5 more in the JSON report).

<a id="package-26"></a>

### liberusoftware/audit-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [audit-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [audit-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/audit-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-27"></a>

### liberusoftware/audit-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [audit-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [audit-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/audit-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-28"></a>

### liberusoftware/audit-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [audit-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [audit-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/audit-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-29"></a>

### liberusoftware/currency-context

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/currency-context) | 15 | 3 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/currency-context) | 15 | 3 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context) | 16 | 3 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/currency-context) | 15 | 3 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/currency-context) | 15 | 3 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/currency-context) | 15 | 3 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context) | 15 | 3 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/currency-context) | 15 | 3 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/currency-context) | 15 | 3 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/currency-context) | 15 | 3 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/currency-context) | 15 | 3 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [currency-context](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/currency-context) | 15 | 3 |

Review paths: `src/Models/Currency.php`.

<a id="package-30"></a>

### liberusoftware/currency-context-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [currency-context-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [currency-context-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/currency-context-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-31"></a>

### liberusoftware/currency-context-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [currency-context-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [currency-context-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/currency-context-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-32"></a>

### liberusoftware/currency-context-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [currency-context-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [currency-context-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/currency-context-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-33"></a>

### liberusoftware/developer-experience

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/developer-experience) | 4 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/developer-experience) | 4 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/developer-experience) | 4 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/developer-experience) | 4 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/developer-experience) | 4 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/developer-experience) | 4 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/developer-experience) | 4 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/developer-experience) | 4 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/developer-experience) | 4 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/developer-experience) | 4 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/developer-experience) | 4 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [developer-experience](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/developer-experience) | 4 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-34"></a>

### liberusoftware/developer-experience-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [developer-experience-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/developer-experience-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [developer-experience-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/developer-experience-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-35"></a>

### liberusoftware/developer-experience-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [developer-experience-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/developer-experience-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [developer-experience-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/developer-experience-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-36"></a>

### liberusoftware/developer-experience-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [developer-experience-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/developer-experience-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [developer-experience-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/developer-experience-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-37"></a>

### liberusoftware/feature-flags

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/feature-flags) | 4 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/feature-flags) | 4 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/feature-flags) | 4 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/feature-flags) | 4 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/feature-flags) | 4 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/feature-flags) | 4 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/feature-flags) | 4 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/feature-flags) | 4 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/feature-flags) | 4 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/feature-flags) | 4 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/feature-flags) | 4 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [feature-flags](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/feature-flags) | 4 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-38"></a>

### liberusoftware/feature-flags-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [feature-flags-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/feature-flags-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [feature-flags-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/feature-flags-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-39"></a>

### liberusoftware/feature-flags-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [feature-flags-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/feature-flags-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [feature-flags-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/feature-flags-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-40"></a>

### liberusoftware/feature-flags-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [feature-flags-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/feature-flags-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [feature-flags-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/feature-flags-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-41"></a>

### liberusoftware/files-media

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/files-media) | 8 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/files-media) | 8 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/files-media) | 8 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/files-media) | 8 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/files-media) | 8 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/files-media) | 8 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media) | 8 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/files-media) | 8 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/files-media) | 8 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/files-media) | 8 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/files-media) | 8 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [files-media](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/files-media) | 8 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-42"></a>

### liberusoftware/files-media-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [files-media-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [files-media-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/files-media-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-43"></a>

### liberusoftware/files-media-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [files-media-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [files-media-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/files-media-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-44"></a>

### liberusoftware/files-media-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [files-media-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [files-media-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/files-media-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-45"></a>

### liberusoftware/identity-core

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core) | 11 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/identity-core) | 11 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/identity-core) | 11 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-core) | 11 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/identity-core) | 11 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/identity-core) | 11 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core) | 41 | 3 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-core) | 11 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-core) | 11 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/identity-core) | 11 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core) | 11 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [identity-core](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/identity-core) | 11 | 1 |

Review paths: `database/factories/UserFactory.php`, `database/migrations/0001_01_01_000000_create_users_table.php`, `database/migrations/0001_01_01_000001_make_password_nullable_on_users_table.php`, `database/migrations/2014_10_12_200000_add_two_factor_columns_to_users_table.php`, `database/seeders/UserSeeder.php`, `src/Legacy/Actions/Fortify/CreateNewUser.php`, `src/Legacy/Actions/Fortify/CreateNewUserWithTeams.php`, `src/Legacy/Actions/Fortify/PasswordValidationRules.php`, `src/Legacy/Actions/Fortify/ResetUserPassword.php`, `src/Legacy/Actions/Fortify/UpdateUserPassword.php`, `src/Legacy/Actions/Fortify/UpdateUserProfileInformation.php`, `src/Legacy/Filament/Resources/Users/Pages/CreateUser.php` (plus 18 more in the JSON report).

<a id="package-46"></a>

### liberusoftware/identity-core-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [identity-core-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [identity-core-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-api) | 4 | 1 |

Review paths: `module.json`, `routes/api.php`, `src/Http/Controllers/AuthTokenController.php`, `src/Http/Controllers/StatusController.php`.

<a id="package-47"></a>

### liberusoftware/identity-core-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament) | 7 | 6 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/identity-core-filament) | 7 | 6 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/identity-core-filament) | 7 | 6 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-core-filament) | 7 | 6 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/identity-core-filament) | 7 | 6 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/identity-core-filament) | 7 | 6 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core-filament) | 7 | 6 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-core-filament) | 7 | 6 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-core-filament) | 7 | 6 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/identity-core-filament) | 7 | 6 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament) | 7 | 6 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/identity-core-filament) | 7 | 6 |

Review paths: `module.json`, `src/Resources/UserResource.php`, `src/Resources/UserResource/Pages/CreateUser.php`.

<a id="package-48"></a>

### liberusoftware/identity-core-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [identity-core-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [identity-core-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-49"></a>

### liberusoftware/identity-socialstream

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream) | 15 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/identity-socialstream) | 15 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/identity-socialstream) | 15 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-socialstream) | 15 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/identity-socialstream) | 15 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/identity-socialstream) | 15 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream) | 29 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-socialstream) | 15 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream) | 15 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/identity-socialstream) | 15 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-socialstream) | 15 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/identity-socialstream) | 15 | 1 |

Review paths: `database/factories/ConnectedAccountFactory.php`, `database/factories/LegacyConnectedAccountFactory.php`, `database/migrations/0001_01_01_000002_create_connected_accounts_table.php`, `database/migrations/2024_02_15_000003_enhance_oauth_and_contacts.php`, `database/migrations/2026_06_29_123955_create_connected_accounts_table.php`, `database/migrations/2026_07_08_000003_encrypt_connected_account_tokens.php`, `src/Legacy/Actions/Socialstream/CreateConnectedAccount.php`, `src/Legacy/Actions/Socialstream/CreateUserFromProvider.php`, `src/Legacy/Actions/Socialstream/CreateUserWithTeamsFromProvider.php`, `src/Legacy/Actions/Socialstream/GenerateRedirectForProvider.php`, `src/Legacy/Actions/Socialstream/HandleInvalidState.php`, `src/Legacy/Actions/Socialstream/ResolveSocialiteUser.php` (plus 5 more in the JSON report).

<a id="package-50"></a>

### liberusoftware/import-export

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export) | 6 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/import-export) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/import-export) | 6 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/import-export) | 6 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/import-export) | 6 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/import-export) | 6 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export) | 15 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/import-export) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/import-export) | 6 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/import-export) | 6 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/import-export) | 6 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/import-export) | 6 | 1 |

Review paths: `database/migrations/2026_07_08_000004_create_exports_table.php`, `src/Legacy/Filament/Exports/AdSetExporter.php`, `src/Legacy/Filament/Exports/AuditLogExporter.php`, `src/Legacy/Filament/Exports/CampaignExporter.php`, `src/Legacy/Filament/Exports/CompanyExporter.php`, `src/Legacy/Filament/Exports/ContactExporter.php`, `src/Legacy/Filament/Exports/DealExporter.php`, `src/Legacy/Filament/Exports/LeadExporter.php`, `src/Legacy/Filament/Exports/OpportunityExporter.php`.

<a id="package-51"></a>

### liberusoftware/import-export-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [import-export-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [import-export-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/import-export-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-52"></a>

### liberusoftware/import-export-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [import-export-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [import-export-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/import-export-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-53"></a>

### liberusoftware/import-export-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [import-export-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [import-export-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/import-export-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-54"></a>

### liberusoftware/integrations

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations) | 7 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/integrations) | 6 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/integrations) | 6 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/integrations) | 6 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/integrations) | 6 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations) | 110 | 18 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/integrations) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/integrations) | 6 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/integrations) | 6 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/integrations) | 6 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/integrations) | 6 | 1 |

Review paths: `database/factories/AccountingIntegrationFactory.php`, `database/factories/CallSettingFactory.php`, `database/factories/EmailFactory.php`, `database/factories/EmailTrackingFactory.php`, `database/factories/LiveChatFactory.php`, `database/factories/MessageFactory.php`, `database/factories/OAuthConfigurationFactory.php`, `database/factories/SamlConnectionFactory.php`, `database/factories/SsoConnectionFactory.php`, `database/factories/WhatsAppNumberFactory.php`, `database/migrations/2023_05_20_000000_create_call_settings_table.php`, `database/migrations/2024_01_10_000000_create_oauth_configurations_table.php` (plus 93 more in the JSON report).

<a id="package-55"></a>

### liberusoftware/integrations-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [integrations-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [integrations-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/integrations-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-56"></a>

### liberusoftware/integrations-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [integrations-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [integrations-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/integrations-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-57"></a>

### liberusoftware/integrations-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [integrations-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [integrations-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/integrations-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-58"></a>

### liberusoftware/jetstream-bridge

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/jetstream-bridge) | 8 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/jetstream-bridge) | 8 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/jetstream-bridge) | 8 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/jetstream-bridge) | 8 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/jetstream-bridge) | 8 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/jetstream-bridge) | 8 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/jetstream-bridge) | 8 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/jetstream-bridge) | 8 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/jetstream-bridge) | 8 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/jetstream-bridge) | 8 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/jetstream-bridge) | 8 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [jetstream-bridge](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/jetstream-bridge) | 8 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-59"></a>

### liberusoftware/jetstream-bridge-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [jetstream-bridge-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/jetstream-bridge-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [jetstream-bridge-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/jetstream-bridge-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-60"></a>

### liberusoftware/jetstream-bridge-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [jetstream-bridge-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/jetstream-bridge-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [jetstream-bridge-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/jetstream-bridge-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-61"></a>

### liberusoftware/jetstream-bridge-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [jetstream-bridge-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/jetstream-bridge-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [jetstream-bridge-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/jetstream-bridge-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-62"></a>

### liberusoftware/localization-core

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/localization-core) | 8 | 5 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/localization-core) | 8 | 5 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/localization-core) | 8 | 5 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/localization-core) | 8 | 5 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/localization-core) | 8 | 5 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/localization-core) | 8 | 5 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/localization-core) | 8 | 5 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/localization-core) | 8 | 5 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/localization-core) | 8 | 5 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/localization-core) | 8 | 5 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/localization-core) | 8 | 5 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [localization-core](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/localization-core) | 8 | 5 |

Review paths: `src/Context/LocaleResolver.php`.

<a id="package-63"></a>

### liberusoftware/localization-core-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [localization-core-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/localization-core-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [localization-core-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/localization-core-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-64"></a>

### liberusoftware/localization-core-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [localization-core-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/localization-core-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [localization-core-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/localization-core-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-65"></a>

### liberusoftware/localization-core-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/localization-core-livewire) | 4 | 4 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/localization-core-livewire) | 4 | 4 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/localization-core-livewire) | 4 | 4 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/localization-core-livewire) | 4 | 4 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/localization-core-livewire) | 4 | 4 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/localization-core-livewire) | 4 | 4 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/localization-core-livewire) | 4 | 4 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/localization-core-livewire) | 4 | 4 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/localization-core-livewire) | 4 | 4 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/localization-core-livewire) | 4 | 4 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/localization-core-livewire) | 4 | 4 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [localization-core-livewire](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/localization-core-livewire) | 4 | 4 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-66"></a>

### liberusoftware/localization-mymemory

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/localization-mymemory) | 3 | 4 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/localization-mymemory) | 3 | 4 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/localization-mymemory) | 3 | 4 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/localization-mymemory) | 3 | 4 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/localization-mymemory) | 3 | 4 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/localization-mymemory) | 3 | 4 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/localization-mymemory) | 3 | 4 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/localization-mymemory) | 3 | 4 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/localization-mymemory) | 3 | 4 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/localization-mymemory) | 3 | 4 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/localization-mymemory) | 3 | 4 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [localization-mymemory](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/localization-mymemory) | 3 | 4 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-67"></a>

### liberusoftware/module-billing-billing-core

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [billing-core](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core) | 36 | 3 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-billing-billing-core](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core) | 36 | 3 |

Review paths: `module.json`.

<a id="package-68"></a>

### liberusoftware/module-liberu-business-workflow-reconciliation

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation) | 7 | 0 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation) | 6 | 2 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-business-workflow-reconciliation](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-business-workflow-reconciliation) | 6 | 2 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation) | 10 | 2 |

Review paths: `database/migrations/2026_08_24_000000_create_liberu_workflow_runs_table.php`, `database/migrations/2026_08_24_010000_create_liberu_reconciliation_cases_table.php`, `module.json`, `src/Actions/CreateReconciliationCase.php`, `src/Actions/StartWorkflowRun.php`, `src/Actions/TransitionReconciliationCase.php`, `src/BusinessWorkflowReconciliationServiceProvider.php`, `src/Capability.php`, `src/Enums/LifecycleStatus.php`, `src/Enums/WorkflowRunState.php`, `src/Events/ReconciliationCaseTransitioned.php`, `src/Events/WorkflowRunStarted.php` (plus 3 more in the JSON report).

<a id="package-69"></a>

### liberusoftware/module-liberu-business-workflow-reconciliation-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-api) | 3 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-business-workflow-reconciliation-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-business-workflow-reconciliation-api) | 3 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-api](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-api) | 4 | 1 |

Review paths: `module.json`, `resources/openapi.yaml`, `src/BusinessWorkflowReconciliationApiServiceProvider.php`, `src/ReconciliationCaseController.php`.

<a id="package-70"></a>

### liberusoftware/module-liberu-business-workflow-reconciliation-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-business-workflow-reconciliation-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-business-workflow-reconciliation-filament) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament) | 6 | 1 |

Review paths: `module.json`, `src/Resources/ReconciliationCaseResource.php`, `src/Resources/ReconciliationCaseResource/Pages/CreateReconciliationCase.php`.

<a id="package-71"></a>

### liberusoftware/module-liberu-business-workflow-reconciliation-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-livewire) | 4 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-business-workflow-reconciliation-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-business-workflow-reconciliation-livewire) | 4 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-livewire](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-livewire) | 4 | 1 |

Review paths: `module.json`, `src/ReconciliationCaseList.php`.

<a id="package-72"></a>

### liberusoftware/module-liberu-executive-insights

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [liberu-executive-insights](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-executive-insights) | 6 | 0 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-executive-insights](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights) | 6 | 2 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-executive-insights](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-executive-insights) | 6 | 2 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-executive-insights](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-executive-insights) | 10 | 2 |

Review paths: `database/migrations/2026_08_24_000000_create_liberu_metric_definitions_table.php`, `database/migrations/2026_08_24_010000_create_liberu_insight_snapshots_table.php`, `module.json`, `src/Actions/CreateInsightSnapshot.php`, `src/Actions/RegisterMetric.php`, `src/Actions/TransitionInsightSnapshot.php`, `src/Capability.php`, `src/Enums/LifecycleStatus.php`, `src/Events/InsightSnapshotTransitioned.php`, `src/Events/MetricRegistered.php`, `src/Exceptions/InvalidLifecycleTransition.php`, `src/ExecutiveInsightsServiceProvider.php` (plus 2 more in the JSON report).

<a id="package-73"></a>

### liberusoftware/module-liberu-executive-insights-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-executive-insights-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-api) | 3 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-executive-insights-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-executive-insights-api) | 3 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-executive-insights-api](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-executive-insights-api) | 4 | 1 |

Review paths: `module.json`, `resources/openapi.yaml`, `src/ExecutiveInsightsApiServiceProvider.php`, `src/InsightSnapshotController.php`.

<a id="package-74"></a>

### liberusoftware/module-liberu-executive-insights-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-executive-insights-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-filament) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-executive-insights-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-executive-insights-filament) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-executive-insights-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-executive-insights-filament) | 6 | 1 |

Review paths: `module.json`, `src/Resources/InsightSnapshotResource.php`, `src/Resources/InsightSnapshotResource/Pages/CreateInsightSnapshot.php`.

<a id="package-75"></a>

### liberusoftware/module-liberu-executive-insights-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-executive-insights-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-livewire) | 4 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-executive-insights-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-executive-insights-livewire) | 4 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-executive-insights-livewire](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-executive-insights-livewire) | 4 | 1 |

Review paths: `module.json`, `src/InsightSnapshotList.php`.

<a id="package-76"></a>

### liberusoftware/module-liberu-platform-orchestration

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [liberu-platform-orchestration](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-platform-orchestration) | 10 | 0 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-platform-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration) | 6 | 2 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-platform-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-platform-orchestration) | 6 | 2 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-platform-orchestration](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration) | 10 | 2 |

Review paths: `database/migrations/2026_08_24_000000_create_liberu_platform_compositions_table.php`, `database/migrations/2026_08_24_010000_create_liberu_platform_workflows_table.php`, `module.json`, `src/Actions/CreateComposition.php`, `src/Actions/CreatePlatformWorkflow.php`, `src/Actions/TransitionComposition.php`, `src/Actions/TransitionPlatformWorkflow.php`, `src/Capability.php`, `src/Enums/CompositionState.php`, `src/Enums/LifecycleStatus.php`, `src/Events/CompositionCreated.php`, `src/Events/CompositionStateChanged.php` (plus 6 more in the JSON report).

<a id="package-77"></a>

### liberusoftware/module-liberu-platform-orchestration-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-platform-orchestration-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration-api) | 3 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-platform-orchestration-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-platform-orchestration-api) | 3 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-platform-orchestration-api](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration-api) | 4 | 1 |

Review paths: `module.json`, `resources/openapi.yaml`, `src/PlatformOrchestrationApiServiceProvider.php`, `src/PlatformWorkflowController.php`.

<a id="package-78"></a>

### liberusoftware/module-liberu-platform-orchestration-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-platform-orchestration-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration-filament) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-platform-orchestration-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-platform-orchestration-filament) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-platform-orchestration-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration-filament) | 6 | 1 |

Review paths: `module.json`, `src/Resources/PlatformWorkflowResource.php`, `src/Resources/PlatformWorkflowResource/Pages/CreatePlatformWorkflow.php`.

<a id="package-79"></a>

### liberusoftware/module-liberu-platform-orchestration-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-platform-orchestration-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration-livewire) | 4 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-platform-orchestration-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-platform-orchestration-livewire) | 4 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-platform-orchestration-livewire](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration-livewire) | 4 | 1 |

Review paths: `module.json`, `src/PlatformWorkflowList.php`.

<a id="package-80"></a>

### liberusoftware/module-liberu-revenue-and-care-orchestration

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration) | 6 | 2 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-revenue-and-care-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-revenue-and-care-orchestration) | 6 | 2 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration) | 10 | 2 |

Review paths: `database/migrations/2026_08_24_010000_create_liberu_care_plans_table.php`, `module.json`, `src/Actions/CreateCarePlan.php`, `src/Actions/TransitionCarePlan.php`, `src/Enums/LifecycleStatus.php`, `src/Events/CarePlanTransitioned.php`, `src/Exceptions/InvalidLifecycleTransition.php`, `src/Models/CarePlan.php`.

<a id="package-81"></a>

### liberusoftware/module-liberu-revenue-and-care-orchestration-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration-api) | 3 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-revenue-and-care-orchestration-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-revenue-and-care-orchestration-api) | 3 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration-api](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration-api) | 4 | 1 |

Review paths: `module.json`, `resources/openapi.yaml`, `src/CarePlanController.php`, `src/RevenueAndCareOrchestrationApiServiceProvider.php`.

<a id="package-82"></a>

### liberusoftware/module-liberu-revenue-and-care-orchestration-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration-filament) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-revenue-and-care-orchestration-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-revenue-and-care-orchestration-filament) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration-filament) | 6 | 1 |

Review paths: `module.json`, `src/Resources/CarePlanResource.php`, `src/Resources/CarePlanResource/Pages/CreateCarePlan.php`.

<a id="package-83"></a>

### liberusoftware/module-liberu-revenue-and-care-orchestration-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [billing](../projects/billing/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-revenue-and-care-orchestration-livewire) | 4 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-liberu-revenue-and-care-orchestration-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-revenue-and-care-orchestration-livewire) | 4 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [liberu-revenue-and-care-orchestration-livewire](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-revenue-and-care-orchestration-livewire) | 4 | 1 |

Review paths: `module.json`, `src/CarePlanList.php`.

<a id="package-84"></a>

### liberusoftware/module-manager

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager) | 17 | 4 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager) | 17 | 4 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager) | 17 | 4 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/module-manager) | 17 | 4 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/module-manager) | 17 | 4 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/module-manager) | 17 | 4 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager) | 23 | 5 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/module-manager) | 17 | 4 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/module-manager) | 17 | 4 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-manager) | 17 | 4 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/module-manager) | 17 | 4 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [module-manager](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/module-manager) | 17 | 4 |

Review paths: `database/migrations/2026_06_02_000001_create_modules_table.php`, `src/Legacy/Events/Module/ModuleDisabled.php`, `src/Legacy/Events/Module/ModuleEnabled.php`, `src/Legacy/Events/Module/ModuleInstalled.php`, `src/Legacy/Events/Module/ModuleUninstalled.php`, `src/Legacy/Models/Module.php`, `src/Manifest.php`, `src/ModuleDiscovery.php`, `src/ModuleManagerServiceProvider.php`, `src/ModuleRegistry.php`, `src/ModuleValidator.php`.

<a id="package-85"></a>

### liberusoftware/module-manager-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [module-manager-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [module-manager-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/module-manager-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-86"></a>

### liberusoftware/module-manager-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/module-manager-filament) | 5 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-manager-filament) | 5 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-manager-filament) | 5 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/module-manager-filament) | 5 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/module-manager-filament) | 5 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/module-manager-filament) | 5 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager-filament) | 5 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/module-manager-filament) | 5 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/module-manager-filament) | 5 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-manager-filament) | 5 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/module-manager-filament) | 5 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [module-manager-filament](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/module-manager-filament) | 5 | 1 |

Review paths: `resources/views/pages/foundation-operations.blade.php`, `src/Pages/FoundationOperations.php`.

<a id="package-87"></a>

### liberusoftware/module-manager-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [module-manager-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [module-manager-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/module-manager-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-88"></a>

### liberusoftware/notifications

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/notifications) | 6 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/notifications) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/notifications) | 6 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/notifications) | 6 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/notifications) | 6 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/notifications) | 6 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/notifications) | 16 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/notifications) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/notifications) | 6 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/notifications) | 6 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/notifications) | 6 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [notifications](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/notifications) | 6 | 1 |

Review paths: `database/migrations/2025_11_20_111132_create_notifications_table.php`, `src/Legacy/Http/Controllers/NotificationController.php`, `src/Legacy/Listeners/SendCRMEventNotification.php`, `src/Legacy/Notifications/CRMEventNotification.php`, `src/Legacy/Notifications/DocumentSharedNotification.php`, `src/Legacy/Notifications/PortalInvitation.php`, `src/Legacy/Notifications/TaskAssignedNotification.php`, `src/Legacy/Notifications/TaskReminderNotification.php`, `src/Legacy/Notifications/TeamInvitation.php`, `src/Legacy/Notifications/TicketReplyNotification.php`.

<a id="package-89"></a>

### liberusoftware/notifications-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [notifications-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/notifications-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [notifications-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/notifications-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-90"></a>

### liberusoftware/notifications-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [notifications-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/notifications-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [notifications-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/notifications-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-91"></a>

### liberusoftware/notifications-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [notifications-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/notifications-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [notifications-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/notifications-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-92"></a>

### liberusoftware/observability

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/observability) | 12 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/observability) | 12 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/observability) | 12 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/observability) | 12 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/observability) | 12 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/observability) | 12 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/observability) | 12 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/observability) | 12 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/observability) | 12 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/observability) | 12 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/observability) | 12 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [observability](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/observability) | 12 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-93"></a>

### liberusoftware/observability-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [observability-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/observability-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [observability-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/observability-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-94"></a>

### liberusoftware/observability-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [observability-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/observability-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [observability-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/observability-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-95"></a>

### liberusoftware/observability-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [observability-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/observability-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [observability-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/observability-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-96"></a>

### liberusoftware/organizations-teams

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams) | 17 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams) | 17 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/organizations-teams) | 17 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams) | 17 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/organizations-teams) | 17 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/organizations-teams) | 17 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams) | 107 | 13 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/organizations-teams) | 17 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/organizations-teams) | 17 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/organizations-teams) | 17 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams) | 17 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/organizations-teams) | 17 | 1 |

Review paths: `config/organizations-teams.php`, `database/factories/LegacyTeamFactory.php`, `database/factories/TeamBackupFactory.php`, `database/factories/TeamFactory.php`, `database/factories/TeamSubscriptionFactory.php`, `database/migrations/2020_05_21_300000_create_team_invitations_table.php`, `database/migrations/2024_01_10_000000_create_team_subscriptions_table.php`, `database/migrations/2024_09_29_093707_add_team_to_resources.php`, `database/migrations/2024_11_17_000000_add_team_id_to-staff_resource_tables.php`, `database/migrations/2026_07_06_000001_add_team_id_to_tenant_scoped_tables.php`, `database/migrations/2026_07_06_000002_enable_spatie_teams_columns.php`, `database/migrations/2026_07_06_190000_add_archived_at_to_teams_table.php` (plus 84 more in the JSON report).

<a id="package-97"></a>

### liberusoftware/organizations-teams-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [organizations-teams-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [organizations-teams-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-98"></a>

### liberusoftware/organizations-teams-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams-filament) | 7 | 6 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams-filament) | 7 | 6 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/organizations-teams-filament) | 7 | 6 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams-filament) | 7 | 6 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/organizations-teams-filament) | 7 | 6 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/organizations-teams-filament) | 7 | 6 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams-filament) | 7 | 6 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/organizations-teams-filament) | 7 | 6 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/organizations-teams-filament) | 7 | 6 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/organizations-teams-filament) | 7 | 6 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-filament) | 7 | 6 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [organizations-teams-filament](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/organizations-teams-filament) | 7 | 6 |

Review paths: `src/Resources/TeamResource.php`.

<a id="package-99"></a>

### liberusoftware/organizations-teams-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [organizations-teams-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [organizations-teams-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-100"></a>

### liberusoftware/profiles

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles) | 7 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/profiles) | 7 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/profiles) | 7 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/profiles) | 7 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/profiles) | 7 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/profiles) | 7 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/profiles) | 7 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/profiles) | 7 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/profiles) | 7 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/profiles) | 7 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/profiles) | 7 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [profiles](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/profiles) | 7 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-101"></a>

### liberusoftware/profiles-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [profiles-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/profiles-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [profiles-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/profiles-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-102"></a>

### liberusoftware/profiles-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [profiles-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/profiles-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [profiles-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/profiles-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-103"></a>

### liberusoftware/profiles-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [profiles-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/profiles-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [profiles-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/profiles-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-104"></a>

### liberusoftware/roles-permissions

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions) | 12 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/roles-permissions) | 12 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/roles-permissions) | 12 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/roles-permissions) | 12 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/roles-permissions) | 12 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/roles-permissions) | 12 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions) | 20 | 2 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/roles-permissions) | 12 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/roles-permissions) | 12 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/roles-permissions) | 12 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions) | 12 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [roles-permissions](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/roles-permissions) | 12 | 1 |

Review paths: `database/migrations/2024_02_21_190705_create_permission_tables.php`, `database/migrations/2026_06_29_124225_create_permission_tables.php`, `database/migrations/2026_07_06_000003_backfill_role_assignment_teams.php`, `database/migrations/2026_07_08_060000_add_role_mappings_to_sso_connections_table.php`, `database/migrations/2026_07_10_000100_seed_role_permissions.php`, `database/seeders/PermissionsSeeder.php`, `database/seeders/RolesSeeder.php`, `src/Legacy/Enums/Role.php`, `src/Legacy/Models/Role.php`, `src/Legacy/Support/PermissionCatalog.php`, `src/Models/Role.php`.

<a id="package-105"></a>

### liberusoftware/roles-permissions-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [roles-permissions-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [roles-permissions-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-106"></a>

### liberusoftware/roles-permissions-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/roles-permissions-filament) | 3 | 3 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/roles-permissions-filament) | 3 | 3 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/roles-permissions-filament) | 3 | 3 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/roles-permissions-filament) | 3 | 3 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/roles-permissions-filament) | 3 | 3 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/roles-permissions-filament) | 3 | 3 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions-filament) | 3 | 3 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/roles-permissions-filament) | 3 | 3 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/roles-permissions-filament) | 3 | 3 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/roles-permissions-filament) | 3 | 3 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions-filament) | 3 | 3 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [roles-permissions-filament](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/roles-permissions-filament) | 3 | 3 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-107"></a>

### liberusoftware/roles-permissions-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [roles-permissions-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/roles-permissions-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [roles-permissions-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/roles-permissions-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-108"></a>

### liberusoftware/scheduler-queues

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/scheduler-queues) | 3 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/scheduler-queues) | 3 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/scheduler-queues) | 3 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/scheduler-queues) | 3 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/scheduler-queues) | 3 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/scheduler-queues) | 3 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues) | 5 | 5 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/scheduler-queues) | 3 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/scheduler-queues) | 3 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/scheduler-queues) | 3 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/scheduler-queues) | 3 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/scheduler-queues) | 3 | 1 |

Review paths: `src/Legacy/Jobs/RestoreTenantContext.php`, `src/Legacy/Jobs/TenantAware.php`.

<a id="package-109"></a>

### liberusoftware/scheduler-queues-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [scheduler-queues-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [scheduler-queues-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/scheduler-queues-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-110"></a>

### liberusoftware/scheduler-queues-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [scheduler-queues-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [scheduler-queues-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/scheduler-queues-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-111"></a>

### liberusoftware/scheduler-queues-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [scheduler-queues-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [scheduler-queues-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/scheduler-queues-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-112"></a>

### liberusoftware/search

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/search) | 11 | 6 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/search) | 11 | 6 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/search) | 12 | 6 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/search) | 11 | 6 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/search) | 11 | 6 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/search) | 11 | 6 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/search) | 11 | 6 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/search) | 11 | 6 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/search) | 11 | 6 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/search) | 11 | 6 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/search) | 11 | 6 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [search](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/search) | 11 | 6 |

Review paths: `database/migrations/2026_02_14_000003_add_search_indexes_to_users_table.php`, `module.json`, `src/Concerns/Searchable.php`, `src/Models/SavedSearch.php`, `src/Services/SearchService.php`.

<a id="package-113"></a>

### liberusoftware/search-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/search-api) | 4 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/search-api) | 4 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/search-api) | 4 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/search-api) | 4 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/search-api) | 4 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/search-api) | 4 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/search-api) | 4 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/search-api) | 4 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/search-api) | 4 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/search-api) | 4 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/search-api) | 4 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [search-api](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/search-api) | 4 | 1 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-114"></a>

### liberusoftware/search-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [search-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/search-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [search-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/search-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-115"></a>

### liberusoftware/search-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [search-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/search-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [search-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/search-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-116"></a>

### liberusoftware/sessions-devices

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices) | 5 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/sessions-devices) | 5 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/sessions-devices) | 5 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/sessions-devices) | 5 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/sessions-devices) | 5 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/sessions-devices) | 5 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices) | 6 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/sessions-devices) | 5 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/sessions-devices) | 5 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/sessions-devices) | 5 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/sessions-devices) | 5 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/sessions-devices) | 5 | 1 |

Review paths: `database/migrations/0001_01_01_000003_create_sessions_table.php`, `database/migrations/2019_12_14_000001_create_personal_access_tokens_table.php`.

<a id="package-117"></a>

### liberusoftware/sessions-devices-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [sessions-devices-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [sessions-devices-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/sessions-devices-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-118"></a>

### liberusoftware/sessions-devices-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices-filament) | 5 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/sessions-devices-filament) | 5 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/sessions-devices-filament) | 5 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/sessions-devices-filament) | 5 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/sessions-devices-filament) | 5 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/sessions-devices-filament) | 5 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices-filament) | 5 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/sessions-devices-filament) | 5 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/sessions-devices-filament) | 5 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/sessions-devices-filament) | 5 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/sessions-devices-filament) | 5 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [sessions-devices-filament](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/sessions-devices-filament) | 5 | 1 |

Review paths: `module.json`, `resources/views/pages/account-security.blade.php`, `src/Pages/AccountSecurity.php`.

<a id="package-119"></a>

### liberusoftware/sessions-devices-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [sessions-devices-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [sessions-devices-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/sessions-devices-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-120"></a>

### liberusoftware/settings

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings) | 9 | 6 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/settings) | 9 | 6 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings) | 10 | 6 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/settings) | 9 | 6 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings) | 10 | 6 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings) | 9 | 6 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings) | 30 | 6 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/settings) | 9 | 6 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/settings) | 9 | 6 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/settings) | 9 | 6 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings) | 9 | 6 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [settings](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/settings) | 9 | 6 |

Review paths: `database/factories/MenuFactory.php`, `database/migrations/2023_05_15_000000_create_site_settings_table.php`, `database/migrations/2024_07_24_080000_create_menus_table.php`, `database/seeders/MenuSeeder.php`, `database/seeders/SiteSettingsSeeder.php`, `database/settings/2024_01_01_000001_create_settings_table.php`, `database/settings/2025_12_10_102854_create_site_settings.php`, `src/Legacy/Filament/Admin/Pages/ManageGeneralSettings.php`, `src/Legacy/Filament/Resources/MenuResource/Pages/CreateMenu.php`, `src/Legacy/Filament/Resources/MenuResource/Pages/EditMenu.php`, `src/Legacy/Filament/Resources/MenuResource/Pages/ListMenus.php`, `src/Legacy/Filament/Resources/SiteSettingsResource/Pages/CreateSiteSettings.php` (plus 12 more in the JSON report).

<a id="package-121"></a>

### liberusoftware/settings-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [settings-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [settings-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-122"></a>

### liberusoftware/settings-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/settings-filament) | 4 | 5 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/settings-filament) | 4 | 5 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/settings-filament) | 4 | 5 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/settings-filament) | 4 | 5 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/settings-filament) | 4 | 5 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/settings-filament) | 4 | 5 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings-filament) | 4 | 5 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/settings-filament) | 4 | 5 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/settings-filament) | 4 | 5 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/settings-filament) | 4 | 5 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings-filament) | 4 | 5 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [settings-filament](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/settings-filament) | 4 | 5 |

Review paths: `src/Pages/ManageSiteSettings.php`.

<a id="package-123"></a>

### liberusoftware/settings-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [settings-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [settings-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/settings-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-124"></a>

### liberusoftware/theme-support

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support) | 11 | 5 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support) | 11 | 5 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support) | 11 | 5 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/theme-support) | 11 | 5 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/theme-support) | 11 | 5 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/theme-support) | 11 | 5 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support) | 11 | 5 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/theme-support) | 11 | 5 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/theme-support) | 11 | 5 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support) | 11 | 5 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/theme-support) | 11 | 5 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [theme-support](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/theme-support) | 11 | 5 |

Review paths: `module.json`, `src/Discovery/ThemeDiscovery.php`, `src/Providers/ThemeServiceProvider.php`, `src/Services/ThemeManager.php`.

<a id="package-125"></a>

### liberusoftware/theme-support-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/theme-support-livewire) | 4 | 3 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/theme-support-livewire) | 4 | 3 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support-livewire) | 4 | 3 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/theme-support-livewire) | 4 | 3 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/theme-support-livewire) | 4 | 3 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/theme-support-livewire) | 4 | 3 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/theme-support-livewire) | 4 | 3 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/theme-support-livewire) | 4 | 3 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/theme-support-livewire) | 4 | 3 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/theme-support-livewire) | 4 | 3 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/theme-support-livewire) | 4 | 3 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [theme-support-livewire](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/theme-support-livewire) | 4 | 3 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-126"></a>

### liberusoftware/two-factor-authentication

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication) | 9 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/two-factor-authentication) | 9 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/two-factor-authentication) | 9 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/two-factor-authentication) | 9 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/two-factor-authentication) | 9 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/two-factor-authentication) | 9 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication) | 9 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/two-factor-authentication) | 9 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/two-factor-authentication) | 9 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/two-factor-authentication) | 9 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/two-factor-authentication) | 9 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/two-factor-authentication) | 9 | 1 |

Review paths: `database/migrations/2026_06_29_123952_add_two_factor_columns_to_users_table.php`.

<a id="package-127"></a>

### liberusoftware/two-factor-authentication-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [two-factor-authentication-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [two-factor-authentication-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/two-factor-authentication-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-128"></a>

### liberusoftware/two-factor-authentication-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [two-factor-authentication-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [two-factor-authentication-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/two-factor-authentication-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-129"></a>

### liberusoftware/two-factor-authentication-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [two-factor-authentication-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [two-factor-authentication-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/two-factor-authentication-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-130"></a>

### liberusoftware/webhooks

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [accounting](../projects/accounting/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/tree/39a49babafc0b8caf12c018abdd765f215ecf207/modules/webhooks) | 6 | 1 |
| [automation](../projects/automation/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-automation-laravel-filament/tree/68e5f07a67041f8438530c71bc86515cbd11da70/modules/webhooks) | 6 | 1 |
| [billing](../projects/billing/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-billing-laravel-filament/tree/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/webhooks) | 6 | 1 |
| [boilerplate](../projects/boilerplate/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/webhooks) | 6 | 1 |
| [browser-game](../projects/browser-game/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-browser-game-laravel-filament/tree/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/webhooks) | 6 | 1 |
| [control-panel](../projects/control-panel/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-control-panel-laravel-filament/tree/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/webhooks) | 6 | 1 |
| [crm](../projects/crm/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/webhooks) | 6 | 1 |
| [sap](../projects/sap/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/webhooks) | 6 | 1 |
| [genealogy](../projects/genealogy/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-genealogy-laravel-filament/tree/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/webhooks) | 6 | 1 |
| [maintenance](../projects/maintenance/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-maintenance-laravel-filament/tree/c267d625e264e86ad223be8a3a08a3728afc7344/modules/webhooks) | 6 | 1 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/webhooks) | 6 | 1 |
| [social-network](../projects/social-network/SOURCE-MODULES.md) | [webhooks](https://github.com/liberusoftware/project-social-network-laravel-filament/tree/08bbc484b50fc7e841a499375329c6de32614145/modules/webhooks) | 12 | 3 |

Review paths: `module.json`, `src/Actions/DeliverWebhook.php`, `src/Actions/QueueWebhook.php`, `src/Actions/RegisterEndpoint.php`, `src/Actions/RotateEndpointSecret.php`, `src/Models/WebhookDelivery.php`, `src/Models/WebhookEndpoint.php`.

<a id="package-131"></a>

### liberusoftware/webhooks-api

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [webhooks-api](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/webhooks-api) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [webhooks-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/webhooks-api) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-132"></a>

### liberusoftware/webhooks-filament

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [webhooks-filament](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/webhooks-filament) | 5 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [webhooks-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/webhooks-filament) | 5 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

<a id="package-133"></a>

### liberusoftware/webhooks-livewire

| Application | Module source | Runtime files | Test files |
| --- | --- | ---: | ---: |
| [crm](../projects/crm/SOURCE-MODULES.md) | [webhooks-livewire](https://github.com/liberusoftware/project-crm-laravel-filament/tree/63aad94e94c0f9a18038e301eb979138c657be64/modules/webhooks-livewire) | 4 | 0 |
| [real-estate](../projects/real-estate/SOURCE-MODULES.md) | [webhooks-livewire](https://github.com/liberusoftware/project-real-estate-laravel-filament/tree/178d8015b601c99dec43acfdc12724aae2b3731a/modules/webhooks-livewire) | 4 | 0 |

The compared runtime paths match across all copies. Review runtime metadata, excluded build/release configuration, and consumer integration before selecting a shared release.

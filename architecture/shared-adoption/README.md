# Divergent shared-package adoption profiles

These **44 package-specific profiles** expand the runtime/metadata differences in the [shared comparison](../SHARED-MODULE-COMPARISON.md). They identify pinned consumers, manifest/provider/dependency differences, changed database paths/table operations, contract signatures and data-preserving adoption steps. They do not certify a stable release or change application code.

The 89 compared identities with matching selected runtime/metadata inputs still need consumer/release verification before adoption; they do not need a fabricated data-migration profile merely because copies are tracked in multiple hosts.

| Identity | Runtime variants | Metadata variants | Profile |
| --- | ---: | ---: | --- |
| `liberusoftware/analytics-core` | 2 | 1 | [Adoption review](liberusoftware--analytics-core.md) |
| `liberusoftware/api-access` | 6 | 1 | [Adoption review](liberusoftware--api-access.md) |
| `liberusoftware/application` | 3 | 1 | [Adoption review](liberusoftware--application.md) |
| `liberusoftware/audit` | 5 | 1 | [Adoption review](liberusoftware--audit.md) |
| `liberusoftware/currency-context` | 2 | 1 | [Adoption review](liberusoftware--currency-context.md) |
| `liberusoftware/identity-core` | 2 | 1 | [Adoption review](liberusoftware--identity-core.md) |
| `liberusoftware/identity-core-api` | 2 | 2 | [Adoption review](liberusoftware--identity-core-api.md) |
| `liberusoftware/identity-core-filament` | 2 | 2 | [Adoption review](liberusoftware--identity-core-filament.md) |
| `liberusoftware/identity-socialstream` | 3 | 1 | [Adoption review](liberusoftware--identity-socialstream.md) |
| `liberusoftware/import-export` | 2 | 1 | [Adoption review](liberusoftware--import-export.md) |
| `liberusoftware/integrations` | 3 | 1 | [Adoption review](liberusoftware--integrations.md) |
| `liberusoftware/localization-core` | 4 | 1 | [Adoption review](liberusoftware--localization-core.md) |
| `liberusoftware/module-billing-billing-core` | 2 | 1 | [Adoption review](liberusoftware--module-billing-billing-core.md) |
| `liberusoftware/module-liberu-business-workflow-reconciliation` | 3 | 3 | [Adoption review](liberusoftware--module-liberu-business-workflow-reconciliation.md) |
| `liberusoftware/module-liberu-business-workflow-reconciliation-api` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-business-workflow-reconciliation-api.md) |
| `liberusoftware/module-liberu-business-workflow-reconciliation-filament` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-business-workflow-reconciliation-filament.md) |
| `liberusoftware/module-liberu-business-workflow-reconciliation-livewire` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-business-workflow-reconciliation-livewire.md) |
| `liberusoftware/module-liberu-executive-insights` | 3 | 3 | [Adoption review](liberusoftware--module-liberu-executive-insights.md) |
| `liberusoftware/module-liberu-executive-insights-api` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-executive-insights-api.md) |
| `liberusoftware/module-liberu-executive-insights-filament` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-executive-insights-filament.md) |
| `liberusoftware/module-liberu-executive-insights-livewire` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-executive-insights-livewire.md) |
| `liberusoftware/module-liberu-platform-orchestration` | 3 | 3 | [Adoption review](liberusoftware--module-liberu-platform-orchestration.md) |
| `liberusoftware/module-liberu-platform-orchestration-api` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-platform-orchestration-api.md) |
| `liberusoftware/module-liberu-platform-orchestration-filament` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-platform-orchestration-filament.md) |
| `liberusoftware/module-liberu-platform-orchestration-livewire` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-platform-orchestration-livewire.md) |
| `liberusoftware/module-liberu-revenue-and-care-orchestration` | 2 | 2 | [Adoption review](liberusoftware--module-liberu-revenue-and-care-orchestration.md) |
| `liberusoftware/module-liberu-revenue-and-care-orchestration-api` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-revenue-and-care-orchestration-api.md) |
| `liberusoftware/module-liberu-revenue-and-care-orchestration-filament` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-revenue-and-care-orchestration-filament.md) |
| `liberusoftware/module-liberu-revenue-and-care-orchestration-livewire` | 2 | 1 | [Adoption review](liberusoftware--module-liberu-revenue-and-care-orchestration-livewire.md) |
| `liberusoftware/module-manager` | 4 | 1 | [Adoption review](liberusoftware--module-manager.md) |
| `liberusoftware/module-manager-filament` | 3 | 1 | [Adoption review](liberusoftware--module-manager-filament.md) |
| `liberusoftware/notifications` | 2 | 1 | [Adoption review](liberusoftware--notifications.md) |
| `liberusoftware/organizations-teams` | 3 | 1 | [Adoption review](liberusoftware--organizations-teams.md) |
| `liberusoftware/organizations-teams-filament` | 2 | 1 | [Adoption review](liberusoftware--organizations-teams-filament.md) |
| `liberusoftware/roles-permissions` | 2 | 2 | [Adoption review](liberusoftware--roles-permissions.md) |
| `liberusoftware/scheduler-queues` | 2 | 1 | [Adoption review](liberusoftware--scheduler-queues.md) |
| `liberusoftware/search` | 7 | 1 | [Adoption review](liberusoftware--search.md) |
| `liberusoftware/sessions-devices` | 2 | 1 | [Adoption review](liberusoftware--sessions-devices.md) |
| `liberusoftware/sessions-devices-filament` | 2 | 2 | [Adoption review](liberusoftware--sessions-devices-filament.md) |
| `liberusoftware/settings` | 5 | 1 | [Adoption review](liberusoftware--settings.md) |
| `liberusoftware/settings-filament` | 2 | 1 | [Adoption review](liberusoftware--settings-filament.md) |
| `liberusoftware/theme-support` | 5 | 1 | [Adoption review](liberusoftware--theme-support.md) |
| `liberusoftware/two-factor-authentication` | 2 | 1 | [Adoption review](liberusoftware--two-factor-authentication.md) |
| `liberusoftware/webhooks` | 3 | 2 | [Adoption review](liberusoftware--webhooks.md) |

Reproduce with `python3 tools/build_shared_adoption_guides.py --projects /tmp/liberu-documentation-sources` after preparing the inventory-pinned views. [General consolidation procedure](../SHARED-MODULES.md).

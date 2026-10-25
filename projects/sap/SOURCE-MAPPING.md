# Sap: design and source reconciliation

This map connects existing design filenames to observed package identities. Matching is based on exact/local naming patterns plus the documented foundation aliases below; it is navigation evidence, not proof of equivalent behavior or complete implementation. Read the source reference before using a proposed field, endpoint, permission or installation example.

**Preservation rule:** all existing product scopes and module documents remain in place. A blank package match means only that this scan did not find a dedicated manifest under the expected naming pattern; implementation can exist elsewhere or use another identity.

See the [project inventory](SOURCE-MODULES.md) for source commits, compatibility aliases and application-owned source roots.

## Read the mapping

Core/API/Filament/Livewire columns show dedicated observed identities where names match. JavaScript/mobile source matches are recorded in the JSON index and individual annotations when present. An adapter can also be application-owned or ship assets through a PHP package; absence of a dedicated npm manifest does not establish absence of UI.

Multiple matches are left visible for review. Repeated design spellings may point to the same package; they must not become independent competing owners. Installation uses the observed manifest name, not a generated design slug.

| Design scope | Core source reference | API source reference | Filament source reference | Livewire source reference |
| --- | --- | --- | --- | --- |
| <a id="assets-and-facilities"></a>[assets-and-facilities](features/assets-and-facilities.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="controlling"></a>[controlling](features/controlling.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="data-and-intelligence"></a>[data-and-intelligence](features/data-and-intelligence.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="enterprise-foundation"></a>[enterprise-foundation](features/enterprise-foundation.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="finance"></a>[finance](features/finance.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="governance-risk-and-compliance"></a>[governance-risk-and-compliance](features/governance-risk-and-compliance.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="hosting-and-cloud"></a>[hosting-and-cloud](features/hosting-and-cloud.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="inventory-and-logistics"></a>[inventory-and-logistics](features/inventory-and-logistics.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="partners-and-portals"></a>[partners-and-portals](features/partners-and-portals.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="people"></a>[people](features/people.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="procurement"></a>[procurement](features/procurement.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="product-and-engineering"></a>[product-and-engineering](features/product-and-engineering.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="projects-and-services"></a>[projects-and-services](features/projects-and-services.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="revenue-operations"></a>[revenue-operations](features/revenue-operations.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="sales-and-crm"></a>[sales-and-crm](features/sales-and-crm.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="service-management"></a>[service-management](features/service-management.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |

## Observed packages without a design-name match

These package references document observed modules even when an existing feature filename did not match. Review their capabilities, call sites and ownership before deciding whether to extend an existing feature or add a distinct product capability. They are not silently omitted or merged by this tool.

The current SAP host installs shared foundation packages. Their presence here is a reuse relationship, not a requirement to create another SAP-owned feature for each foundation module. Use the [foundation source map](../boilerplate/SOURCE-MAPPING.md), [shared implementation references](../../modules/source/README.md), and [current SAP foundation guide](SOURCE-APPLICATION.md).

| Actual directory | Manifest identity and implementation reference |
| --- | --- |
| `activity-comments` | [liberusoftware/activity-comments](../../modules/source/liberusoftware--activity-comments.md) |
| `analytics-core` | [liberusoftware/analytics-core](../../modules/source/liberusoftware--analytics-core.md) |
| `analytics-google` | [liberusoftware/analytics-google](../../modules/source/liberusoftware--analytics-google.md) |
| `analytics-meta` | [liberusoftware/analytics-meta](../../modules/source/liberusoftware--analytics-meta.md) |
| `api-access` | [liberusoftware/api-access](../../modules/source/liberusoftware--api-access.md) |
| `application` | [liberusoftware/application](../../modules/source/liberusoftware--application.md) |
| `audit` | [liberusoftware/audit](../../modules/source/liberusoftware--audit.md) |
| `currency-context` | [liberusoftware/currency-context](../../modules/source/liberusoftware--currency-context.md) |
| `developer-experience` | [liberusoftware/developer-experience](../../modules/source/liberusoftware--developer-experience.md) |
| `feature-flags` | [liberusoftware/feature-flags](../../modules/source/liberusoftware--feature-flags.md) |
| `files-media` | [liberusoftware/files-media](../../modules/source/liberusoftware--files-media.md) |
| `identity-core` | [liberusoftware/identity-core](../../modules/source/liberusoftware--identity-core.md) |
| `identity-core-filament` | [liberusoftware/identity-core-filament](../../modules/source/liberusoftware--identity-core-filament.md) |
| `identity-socialstream` | [liberusoftware/identity-socialstream](../../modules/source/liberusoftware--identity-socialstream.md) |
| `import-export` | [liberusoftware/import-export](../../modules/source/liberusoftware--import-export.md) |
| `integrations` | [liberusoftware/integrations](../../modules/source/liberusoftware--integrations.md) |
| `jetstream-bridge` | [liberusoftware/jetstream-bridge](../../modules/source/liberusoftware--jetstream-bridge.md) |
| `localization-core` | [liberusoftware/localization-core](../../modules/source/liberusoftware--localization-core.md) |
| `localization-core-livewire` | [liberusoftware/localization-core-livewire](../../modules/source/liberusoftware--localization-core-livewire.md) |
| `localization-mymemory` | [liberusoftware/localization-mymemory](../../modules/source/liberusoftware--localization-mymemory.md) |
| `module-manager` | [liberusoftware/module-manager](../../modules/source/liberusoftware--module-manager.md) |
| `module-manager-filament` | [liberusoftware/module-manager-filament](../../modules/source/liberusoftware--module-manager-filament.md) |
| `notifications` | [liberusoftware/notifications](../../modules/source/liberusoftware--notifications.md) |
| `observability` | [liberusoftware/observability](../../modules/source/liberusoftware--observability.md) |
| `organizations-teams` | [liberusoftware/organizations-teams](../../modules/source/liberusoftware--organizations-teams.md) |
| `organizations-teams-filament` | [liberusoftware/organizations-teams-filament](../../modules/source/liberusoftware--organizations-teams-filament.md) |
| `profiles` | [liberusoftware/profiles](../../modules/source/liberusoftware--profiles.md) |
| `roles-permissions` | [liberusoftware/roles-permissions](../../modules/source/liberusoftware--roles-permissions.md) |
| `roles-permissions-filament` | [liberusoftware/roles-permissions-filament](../../modules/source/liberusoftware--roles-permissions-filament.md) |
| `scheduler-queues` | [liberusoftware/scheduler-queues](../../modules/source/liberusoftware--scheduler-queues.md) |
| `search` | [liberusoftware/search](../../modules/source/liberusoftware--search.md) |
| `search-api` | [liberusoftware/search-api](../../modules/source/liberusoftware--search-api.md) |
| `sessions-devices` | [liberusoftware/sessions-devices](../../modules/source/liberusoftware--sessions-devices.md) |
| `sessions-devices-filament` | [liberusoftware/sessions-devices-filament](../../modules/source/liberusoftware--sessions-devices-filament.md) |
| `settings` | [liberusoftware/settings](../../modules/source/liberusoftware--settings.md) |
| `settings-filament` | [liberusoftware/settings-filament](../../modules/source/liberusoftware--settings-filament.md) |
| `theme-support` | [liberusoftware/theme-support](../../modules/source/liberusoftware--theme-support.md) |
| `theme-support-livewire` | [liberusoftware/theme-support-livewire](../../modules/source/liberusoftware--theme-support-livewire.md) |
| `two-factor-authentication` | [liberusoftware/two-factor-authentication](../../modules/source/liberusoftware--two-factor-authentication.md) |
| `webhooks` | [liberusoftware/webhooks](../../modules/source/liberusoftware--webhooks.md) |

Reproduce with `python3 tools/reconcile_source_modules.py` after rebuilding the inventory and package references. The [machine-readable mapping](../../architecture/source-design-mapping.json) includes every layer match. Follow the [reuse guide](../../architecture/SHARED-MODULES.md), [Composer lifecycle](../../guides/COMPOSER.md) and [npm lifecycle](../../guides/NPM.md) when implementing or adopting a module.

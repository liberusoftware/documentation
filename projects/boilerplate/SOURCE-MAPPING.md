# Boilerplate: design and source reconciliation

This map connects existing design filenames to observed package identities. Matching is based on exact/local naming patterns plus the documented foundation aliases below; it is navigation evidence, not proof of equivalent behavior or complete implementation. Read the source reference before using a proposed field, endpoint, permission or installation example.

**Preservation rule:** all existing product scopes and module documents remain in place. A blank package match means only that this scan did not find a dedicated manifest under the expected naming pattern; implementation can exist elsewhere or use another identity.

See the [project inventory](SOURCE-MODULES.md) for source commits, compatibility aliases and application-owned source roots.

## Read the mapping

Core/API/Filament/Livewire columns show dedicated observed identities where names match. JavaScript/mobile source matches are recorded in the JSON index and individual annotations when present. An adapter can also be application-owned or ship assets through a PHP package; absence of a dedicated npm manifest does not establish absence of UI.

Multiple matches are left visible for review. Repeated design spellings may point to the same package; they must not become independent competing owners. Installation uses the observed manifest name, not a generated design slug.

| Design scope | Core source reference | API source reference | Filament source reference | Livewire source reference |
| --- | --- | --- | --- | --- |
| <a id="activity-and-comments"></a>[activity-and-comments](core/activity-and-comments.md) | [liberusoftware/activity-comments](../../modules/source/liberusoftware--activity-comments.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="activity-comments"></a>[activity-comments](features/activity-comments.md) | [liberusoftware/activity-comments](../../modules/source/liberusoftware--activity-comments.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="analytics-core"></a>[analytics-core](features/analytics-core.md) | [liberusoftware/analytics-core](../../modules/source/liberusoftware--analytics-core.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="analytics-google"></a>[analytics-google](features/analytics-google.md) | [liberusoftware/analytics-google](../../modules/source/liberusoftware--analytics-google.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="analytics-meta"></a>[analytics-meta](features/analytics-meta.md) | [liberusoftware/analytics-meta](../../modules/source/liberusoftware--analytics-meta.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="api-access"></a>[api-access](features/api-access.md) | [liberusoftware/api-access](../../modules/source/liberusoftware--api-access.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="application"></a>[application](features/application.md) | [liberusoftware/application](../../modules/source/liberusoftware--application.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="application-core"></a>[application-core](core/application-core.md) | [liberusoftware/application](../../modules/source/liberusoftware--application.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="audit"></a>[audit](features/audit.md) | [liberusoftware/audit](../../modules/source/liberusoftware--audit.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="currency-context"></a>[currency-context](features/currency-context.md) | [liberusoftware/currency-context](../../modules/source/liberusoftware--currency-context.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="developer-experience"></a>[developer-experience](features/developer-experience.md) | [liberusoftware/developer-experience](../../modules/source/liberusoftware--developer-experience.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="feature-flags"></a>[feature-flags](features/feature-flags.md) | [liberusoftware/feature-flags](../../modules/source/liberusoftware--feature-flags.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="files-and-media"></a>[files-and-media](core/files-and-media.md) | [liberusoftware/files-media](../../modules/source/liberusoftware--files-media.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="files-media"></a>[files-media](features/files-media.md) | [liberusoftware/files-media](../../modules/source/liberusoftware--files-media.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="google-analytics"></a>[google-analytics](core/google-analytics.md) | [liberusoftware/analytics-google](../../modules/source/liberusoftware--analytics-google.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="identity"></a>[identity](core/identity.md) | [liberusoftware/identity-core](../../modules/source/liberusoftware--identity-core.md) | No dedicated name match | [liberusoftware/identity-core-filament](../../modules/source/liberusoftware--identity-core-filament.md) | No dedicated name match |
| <a id="identity-core"></a>[identity-core](features/identity-core.md) | [liberusoftware/identity-core](../../modules/source/liberusoftware--identity-core.md) | No dedicated name match | [liberusoftware/identity-core-filament](../../modules/source/liberusoftware--identity-core-filament.md) | No dedicated name match |
| <a id="identity-socialstream"></a>[identity-socialstream](features/identity-socialstream.md) | [liberusoftware/identity-socialstream](../../modules/source/liberusoftware--identity-socialstream.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="import-and-export"></a>[import-and-export](core/import-and-export.md) | [liberusoftware/import-export](../../modules/source/liberusoftware--import-export.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="import-export"></a>[import-export](features/import-export.md) | [liberusoftware/import-export](../../modules/source/liberusoftware--import-export.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="integrations"></a>[integrations](features/integrations.md) | [liberusoftware/integrations](../../modules/source/liberusoftware--integrations.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="jetstream-bridge"></a>[jetstream-bridge](features/jetstream-bridge.md) | [liberusoftware/jetstream-bridge](../../modules/source/liberusoftware--jetstream-bridge.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="localization"></a>[localization](core/localization.md) | [liberusoftware/localization-core](../../modules/source/liberusoftware--localization-core.md) | No dedicated name match | No dedicated name match | [liberusoftware/localization-core-livewire](../../modules/source/liberusoftware--localization-core-livewire.md) |
| <a id="localization-core"></a>[localization-core](features/localization-core.md) | [liberusoftware/localization-core](../../modules/source/liberusoftware--localization-core.md) | No dedicated name match | No dedicated name match | [liberusoftware/localization-core-livewire](../../modules/source/liberusoftware--localization-core-livewire.md) |
| <a id="localization-mymemory"></a>[localization-mymemory](features/localization-mymemory.md) | [liberusoftware/localization-mymemory](../../modules/source/liberusoftware--localization-mymemory.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="meta-server-side-tracking"></a>[meta-server-side-tracking](core/meta-server-side-tracking.md) | [liberusoftware/analytics-meta](../../modules/source/liberusoftware--analytics-meta.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="module-manager"></a>[module-manager](features/module-manager.md) | [liberusoftware/module-manager](../../modules/source/liberusoftware--module-manager.md) | No dedicated name match | [liberusoftware/module-manager-filament](../../modules/source/liberusoftware--module-manager-filament.md) | No dedicated name match |
| <a id="notifications"></a>[notifications](features/notifications.md) | [liberusoftware/notifications](../../modules/source/liberusoftware--notifications.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="observability"></a>[observability](features/observability.md) | [liberusoftware/observability](../../modules/source/liberusoftware--observability.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="organizations-and-teams"></a>[organizations-and-teams](core/organizations-and-teams.md) | [liberusoftware/organizations-teams](../../modules/source/liberusoftware--organizations-teams.md) | No dedicated name match | [liberusoftware/organizations-teams-filament](../../modules/source/liberusoftware--organizations-teams-filament.md) | No dedicated name match |
| <a id="organizations-teams"></a>[organizations-teams](features/organizations-teams.md) | [liberusoftware/organizations-teams](../../modules/source/liberusoftware--organizations-teams.md) | No dedicated name match | [liberusoftware/organizations-teams-filament](../../modules/source/liberusoftware--organizations-teams-filament.md) | No dedicated name match |
| <a id="profiles"></a>[profiles](features/profiles.md) | [liberusoftware/profiles](../../modules/source/liberusoftware--profiles.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="roles-and-permissions"></a>[roles-and-permissions](core/roles-and-permissions.md) | [liberusoftware/roles-permissions](../../modules/source/liberusoftware--roles-permissions.md) | No dedicated name match | [liberusoftware/roles-permissions-filament](../../modules/source/liberusoftware--roles-permissions-filament.md) | No dedicated name match |
| <a id="roles-permissions"></a>[roles-permissions](features/roles-permissions.md) | [liberusoftware/roles-permissions](../../modules/source/liberusoftware--roles-permissions.md) | No dedicated name match | [liberusoftware/roles-permissions-filament](../../modules/source/liberusoftware--roles-permissions-filament.md) | No dedicated name match |
| <a id="scheduler-and-queues"></a>[scheduler-and-queues](core/scheduler-and-queues.md) | [liberusoftware/scheduler-queues](../../modules/source/liberusoftware--scheduler-queues.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="scheduler-queues"></a>[scheduler-queues](features/scheduler-queues.md) | [liberusoftware/scheduler-queues](../../modules/source/liberusoftware--scheduler-queues.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="search"></a>[search](features/search.md) | [liberusoftware/search](../../modules/source/liberusoftware--search.md) | [liberusoftware/search-api](../../modules/source/liberusoftware--search-api.md) | No dedicated name match | No dedicated name match |
| <a id="sessions-and-devices"></a>[sessions-and-devices](core/sessions-and-devices.md) | [liberusoftware/sessions-devices](../../modules/source/liberusoftware--sessions-devices.md) | No dedicated name match | [liberusoftware/sessions-devices-filament](../../modules/source/liberusoftware--sessions-devices-filament.md) | No dedicated name match |
| <a id="sessions-devices"></a>[sessions-devices](features/sessions-devices.md) | [liberusoftware/sessions-devices](../../modules/source/liberusoftware--sessions-devices.md) | No dedicated name match | [liberusoftware/sessions-devices-filament](../../modules/source/liberusoftware--sessions-devices-filament.md) | No dedicated name match |
| <a id="settings"></a>[settings](features/settings.md) | [liberusoftware/settings](../../modules/source/liberusoftware--settings.md) | No dedicated name match | [liberusoftware/settings-filament](../../modules/source/liberusoftware--settings-filament.md) | No dedicated name match |
| <a id="theme-support"></a>[theme-support](features/theme-support.md) | [liberusoftware/theme-support](../../modules/source/liberusoftware--theme-support.md) | No dedicated name match | No dedicated name match | [liberusoftware/theme-support-livewire](../../modules/source/liberusoftware--theme-support-livewire.md) |
| <a id="two-factor-authentication"></a>[two-factor-authentication](features/two-factor-authentication.md) | [liberusoftware/two-factor-authentication](../../modules/source/liberusoftware--two-factor-authentication.md) | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="webhooks"></a>[webhooks](features/webhooks.md) | [liberusoftware/webhooks](../../modules/source/liberusoftware--webhooks.md) | No dedicated name match | No dedicated name match | No dedicated name match |

## Retained foundation design aliases

These 12 older core/adapter spellings map to the current foundation names below. Their documents are retained as compatibility navigation, not new independent capabilities. Current source identities and requirements are in the reference links.

| Retained spelling | Current design spelling |
| --- | --- |
| `activity-and-comments` | [activity-comments](features/activity-comments.md) |
| `application-core` | [application](features/application.md) |
| `files-and-media` | [files-media](features/files-media.md) |
| `google-analytics` | [analytics-google](features/analytics-google.md) |
| `identity` | [identity-core](features/identity-core.md) |
| `import-and-export` | [import-export](features/import-export.md) |
| `localization` | [localization-core](features/localization-core.md) |
| `meta-server-side-tracking` | [analytics-meta](features/analytics-meta.md) |
| `organizations-and-teams` | [organizations-teams](features/organizations-teams.md) |
| `roles-and-permissions` | [roles-permissions](features/roles-permissions.md) |
| `scheduler-and-queues` | [scheduler-queues](features/scheduler-queues.md) |
| `sessions-and-devices` | [sessions-devices](features/sessions-devices.md) |

## Observed packages without a design-name match

These package references document observed modules even when an existing feature filename did not match. Review their capabilities, call sites and ownership before deciding whether to extend an existing feature or add a distinct product capability. They are not silently omitted or merged by this tool.

| Actual directory | Manifest identity and implementation reference |
| --- | --- |
| — | No unmatched dedicated package identities in this scan |

Reproduce with `python3 tools/reconcile_source_modules.py` after rebuilding the inventory and package references. The [machine-readable mapping](../../architecture/source-design-mapping.json) includes every layer match. Follow the [reuse guide](../../architecture/SHARED-MODULES.md), [Composer lifecycle](../../guides/COMPOSER.md) and [npm lifecycle](../../guides/NPM.md) when implementing or adopting a module.

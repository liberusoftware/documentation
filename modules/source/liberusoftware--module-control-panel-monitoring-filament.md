# liberusoftware/module-control-panel-monitoring-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Control Panel Monitoring.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-monitoring-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-monitoring-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-monitoring-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-monitoring-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\MonitoringFilament\\MonitoringFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/module.json).

**Declared capabilities:** control-panel.monitoring.filament

**Declared features:** Health checks, Metrics, Incidents

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-monitoring` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\MonitoringFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-control-panel-monitoring": "^1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/MonitoringFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/MonitoringFilamentPlugin.php) · [src/MonitoringFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/MonitoringFilamentServiceProvider.php) · [src/Resources/AlertRuleResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/AlertRuleResource.php) · [src/Resources/AlertRuleResource/Pages/ListAlertRules.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/AlertRuleResource/Pages/ListAlertRules.php) · [src/Resources/CapacitySnapshotResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/CapacitySnapshotResource.php) · [src/Resources/CapacitySnapshotResource/Pages/ListCapacitySnapshots.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/CapacitySnapshotResource/Pages/ListCapacitySnapshots.php) · [src/Resources/IncidentResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/IncidentResource.php) · [src/Resources/IncidentResource/Pages/ListIncidents.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/IncidentResource/Pages/ListIncidents.php) · [src/Resources/LogEntryResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/LogEntryResource.php) · [src/Resources/LogEntryResource/Pages/ListLogEntries.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/LogEntryResource/Pages/ListLogEntries.php) · [src/Resources/MaintenanceWindowResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MaintenanceWindowResource.php) · [src/Resources/MaintenanceWindowResource/Pages/CreateMaintenanceWindow.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MaintenanceWindowResource/Pages/CreateMaintenanceWindow.php) · [src/Resources/MaintenanceWindowResource/Pages/EditMaintenanceWindow.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MaintenanceWindowResource/Pages/EditMaintenanceWindow.php) · [src/Resources/MaintenanceWindowResource/Pages/ListMaintenanceWindows.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MaintenanceWindowResource/Pages/ListMaintenanceWindows.php) · [src/Resources/MetricSampleResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MetricSampleResource.php) · [src/Resources/MetricSampleResource/Pages/ListMetricSamples.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MetricSampleResource/Pages/ListMetricSamples.php) · [src/Resources/MonitorResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitorResource.php) · [src/Resources/MonitorResource/Pages/CreateMonitor.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitorResource/Pages/CreateMonitor.php) · [src/Resources/MonitorResource/Pages/EditMonitor.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitorResource/Pages/EditMonitor.php) · [src/Resources/MonitorResource/Pages/ListMonitors.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitorResource/Pages/ListMonitors.php) · [src/Resources/MonitoringAssetResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitoringAssetResource.php) · [src/Resources/MonitoringEventResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitoringEventResource.php) · [src/Resources/MonitoringEventResource/Pages/CreateMonitoringEvent.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitoringEventResource/Pages/CreateMonitoringEvent.php) · [src/Resources/MonitoringEventResource/Pages/EditMonitoringEvent.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitoringEventResource/Pages/EditMonitoringEvent.php) · [src/Resources/MonitoringEventResource/Pages/ListMonitoringEvents.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/MonitoringEventResource/Pages/ListMonitoringEvents.php) · [src/Resources/StatusSnapshotResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/StatusSnapshotResource.php) · [src/Resources/StatusSnapshotResource/Pages/ListStatusSnapshots.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/StatusSnapshotResource/Pages/ListStatusSnapshots.php) · [src/Resources/UptimeCheckResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/UptimeCheckResource.php) · [src/Resources/UptimeCheckResource/Pages/ListUptimeChecks.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-filament/src/Resources/UptimeCheckResource/Pages/ListUptimeChecks.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.

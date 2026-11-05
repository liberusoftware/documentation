# Liberu Music: Plugin Hosting and Isolation — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery.

**Required journey:** Scan an approved directory, load a plugin, save state and recover a crashed instance.

**Invariant:** Untrusted plugin scans never run in the main application process.

**Dependencies:** audio-engine, presets. Dependencies use public contracts rather than private tables or models.

## Acceptance

Crash a scanner/worker and reopen a session with the plugin absent. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/plugin-hosting.md), [API plan](../api/plugin-hosting.md) and [surface support](../PRESENTATION.md).

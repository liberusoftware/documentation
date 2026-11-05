# Liberu Music: Plugin Hosting and Isolation — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-plugin-hosting`. See [domain specification](../features/plugin-hosting.md).

## Public application boundary

Own plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** Untrusted plugin scans never run in the main application process.

**Dependencies:** audio-engine, presets. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Crash a scanner/worker and reopen a session with the plugin absent. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).

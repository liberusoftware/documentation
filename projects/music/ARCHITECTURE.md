# Liberu Music runtime architecture

**Status:** proposed boundaries, pending implementation and measured hardware support.

## Runtime ownership

```text
Desktop / browser / mobile UI ── local commands ── native or browser audio runtime
            │                                        │
            │ reviewed HTTP/events                    └─ devices, DSP, sample clock
            ▼
Laravel core + optional API adapters ── database, asset storage, queues
            ▲
Filament / Livewire / Inertia hosts
```

The Laravel core owns shared project metadata, membership policy, stored revision manifests, media authorization and asynchronous job orchestration. The local engine owns active playback state, audio graph execution, recording buffers, MIDI timing and device lifecycle. A desktop app owns local durable journals and immutable media files; remote persistence acknowledges synchronization separately. A cloud outage must not stop an already authorized local recording or prevent local save.

Audio commands cross a versioned, bounded message boundary. Validate graph edits off the callback, publish immutable graph snapshots at safe boundaries and reclaim retired resources off the audio thread. The callback performs no network/file I/O, database access, unbounded allocation or blocking locks. Metering uses bounded telemetry buffers and may drop old readings. Disk workers stream audio through bounded buffers; define overrun behavior and warn before capture capacity is exhausted.

## Engine and host modules

| Runtime module | Responsibility | Corresponding domain plans |
| --- | --- | --- |
| Engine SDK and native DSP runtime | Graph compilation, transport, scheduling, resampling and latency compensation; language/toolchain selected by a recorded architecture decision | [Audio engine](core/audio-engine.md), [mixer](core/mixer-routing.md), [effects](core/effects.md) |
| Device drivers | Platform audio and MIDI integration with declared sample rates, channels and buffer support | [Devices](core/audio-devices.md), [controllers](core/controllers.md) |
| Plugin scanner and worker host | Separate-process discovery/execution, crash recovery, format adapters and state compatibility | [Plugin hosting](core/plugin-hosting.md) |
| Desktop application shell | Windows/macOS/Linux target packaging, local files, secure credentials, updater, engine bridge and crash recovery | [Projects](core/projects.md), [offline](core/sync-offline.md) |
| Browser audio adapter | AudioWorklet-based supported subset, user-gesture activation, feature discovery and degraded modes | [Presentation matrix](PRESENTATION.md) |
| Mobile native audio bridge | iOS/Android capture, playback, MIDI and lifecycle integration for either mobile framework | [React Native](react-native/README.md), [Flutter](flutter/README.md) |
| Offline render worker | Headless execution of pinned graph snapshots, job cancellation, resource budgets and artifact checksums | [Export](core/export-mastering.md) |

These runtime components require independently versioned build artifacts and integration tests. Composer modules describe domain boundaries; they cannot substitute for native DSP binaries. Use a language-neutral engine protocol with schema compatibility checks so React Native and Flutter do not fork audio behavior.

## Project and media model

A session revision records stable track/clip/note identifiers, sample-rate/channel metadata, tempo and meter map, routing, automation, plugin/instrument state, asset checksums and engine/schema versions. Musical ticks, sample frames, seconds and video frames are distinct types; conversions belong to tempo/timecode contracts. Maintain undo groups in a local command journal and checkpoint atomically. Publish only revisions whose required media uploads have completed verification; incomplete synchronization remains visibly pending.

Media storage is content addressed but authorization is workspace scoped. A checksum is never an access token. Upload into quarantine, verify format/size/checksum, then mark an asset ready. Deletion checks revision references, retention rules and offline pins; garbage collection has a grace period and dry-run report. Pack provenance and distribution rights travel with exported manifests.

## Plugins and format policy

Evaluate native plugin formats such as VST3, Audio Units and CLAP through separate adapters; no format or operating system is supported until license, SDK, packaging and compatibility checks pass. Mobile and browser clients must show unsupported plugins and may play approved frozen stems. Do not upload third-party plugin binaries or credentials as session content. Sandboxed workers have explicit file/network permissions and scan timeouts. Preserve opaque plugin state even when a plugin is unavailable.

## Collaboration and security

Server mutations check actor, workspace, role, asset ownership and expected revision. Use idempotency keys and revision preconditions; preserve divergent branches rather than applying last-writer-wins to musical edits. Review comments anchor to revision and musical/sample position. Events carry sequence numbers and reconnect cursors. Pair remote-control devices with short-lived scoped credentials and explicit session approval; revoke access on disconnect/logout as appropriate.

Signed private media URLs expire; public shares are scoped, revocable and separately authorized. Encrypt transport and protected local credentials. Minimize diagnostic uploads and require consent before uploading recordings or crash attachments containing paths/content. Tenant isolation applies to search, waveform previews, exports, caches and background workers.

## Performance and correctness evidence

Define release targets per OS/device, reference interface, project complexity, buffer size and sample rate. Report measured round-trip latency, callback deadline misses, CPU/memory, disk throughput, seek accuracy, recording drift and render duration. No latency claim is valid without that context. Verify reference signals, impulse responses, automation timing, denormals/non-finite output handling, missing plugins and output limiting/safe monitoring. Maintain offline/realtime render comparison tolerances and explain nondeterministic plugins.

See [module architecture](../../architecture/MODULES.md), [API architecture](../../architecture/API.md) and [mobile architecture](../../architecture/MOBILE.md).

# Liberu Music: API

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

Proposed remote control and synchronization contracts. No endpoints are claimed to exist. HTTP and WebSocket traffic must never be a dependency of the audio callback.

See [product scope](../MUSIC.md), [architecture](../ARCHITECTURE.md), [surface support](../PRESENTATION.md) and [foundation adoption](../FOUNDATION.md). All 22 capabilities have a plan here; a plan does not imply equal feature support on every surface.

| Module | Responsibility |
| --- | --- |
| [Projects and Sessions](projects.md) | Project documents, tracks, folders, templates, revision history, autosave and portable session manifests |
| [Audio Engine and Transport](audio-engine.md) | Native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering |
| [Audio Devices and Monitoring](audio-devices.md) | Device discovery, input/output channel mapping, sample rates, buffer sizes and direct/software monitoring |
| [Recording and Take Comping](recording.md) | Track arming, count-in, punch and loop recording, take lanes, comp segments and recoverable disk writes |
| [Arrangement and Audio Editing](arrangement.md) | Timeline clips, fades, splits, slip edits, crossfades, markers, warp anchors and nondestructive pitch/time changes |
| [Clip Launcher and Scenes](clip-launcher.md) | Quantized clip launch, scenes, follow actions and recording performances into the arrangement |
| [MIDI and Expressive Editing](midi-sequencing.md) | Piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export |
| [Tempo, Meter and Groove](tempo-groove.md) | Tempo maps, meter changes, groove templates, swing, metronome and musical/sample-time conversion |
| [Instruments and Samplers](instruments.md) | Built-in synth, drum machine, sampler, multisamples, voice allocation and portable instrument presets |
| [Audio Effects and Amp Processing](effects.md) | EQ, dynamics, delay, reverb, modulation effects and independently designed amp/cabinet processing |
| [Plugin Hosting and Isolation](plugin-hosting.md) | Plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery |
| [Mixer and Routing](mixer-routing.md) | Channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots |
| [Automation and Modulation](automation-modulation.md) | Parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings |
| [Composition, Chords and Score](composition-score.md) | Chord tracks, scales, voicings, articulation maps and notation views with printable parts |
| [Media Library and Content](media-library.md) | Content-addressed audio assets, waveform peaks, metadata, tags, search, packs and rights provenance |
| [Presets, Racks and Templates](presets.md) | Versioned instrument/effect presets, device racks, macros and reusable session templates |
| [Controllers and Hardware Integration](controllers.md) | MIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization |
| [Collaboration and Review](collaboration.md) | Project membership integration, revision sharing, comments, review markers, locks and conflict branches |
| [Offline Storage and Synchronization](sync-offline.md) | Local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas |
| [Export, Mastering and Delivery](export-mastering.md) | Offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests |
| [Video and Timecode](video-timecode.md) | Reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization |
| [Live Performance and Setlists](live-performance.md) | Setlists, cue preparation, preloaded projects, scene transitions and performance recovery |

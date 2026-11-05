# Liberu Music

## Product scope

Liberu Music is a proposed modular Digital Audio Workstation for songwriters, recording musicians, electronic producers, composers, mix engineers and live performers. It covers the journey from an offline idea or multitrack recording to arrangement, sound design, mixing, mastering, collaborative review and live playback.

The intended experience combines an approachable recording and production workflow, an integrated linear arrangement and clip-launching workspace, and detailed MIDI/composition tools. These are independent Liberu design goals inspired by [Fender Studio Pro](https://www.fender.com/pages/fender-studio-pro), [Bitwig Studio](https://www.bitwig.com/overview/) and [Cubase](https://www.steinberg.net/cubase/). The official pages describe their respective production, performance/sound-design and composition offerings; they are reference points rather than a promise of compatibility, endorsement or feature parity. Do not copy proprietary assets, preset libraries or interfaces.

**Status:** product requirements and proposed module plans only. This documentation does not establish an existing application repository, installable packages, benchmarks or supported plugin formats. All module identifiers are provisional.

## Outcomes and scope boundaries

- Record and comp audio without losing original takes; edit audio and expressive MIDI nondestructively.
- Move between arrangement and quantized clip performance; automate and modulate instruments, effects and mix parameters.
- Compose with tempo/meter maps, chords, articulations and score views; align music to reference picture.
- Organize samples and presets with provenance; restore projects with missing-dependency explanations.
- Produce reproducible mixes and stems with loudness analysis; prepare a reliable performance set.
- Work locally while disconnected, then synchronize revisions, media and review comments when connected.

The primary full DAW target is a desktop host with a native real-time audio engine. Web workspaces support project management and a progressively enabled editor. Mobile starts with capture, sketching, review and remote control; advanced production requires device-specific validation. Cloud jobs may render or analyze media asynchronously. Internet collaboration is revision-based; latency-free distributed live recording is outside the initial scope.

A marketplace, commercial sample licensing service, AI composition, automatic stem separation and full interchange with proprietary DAW session formats are later proposals requiring separate scope and rights review. Basic portable session export, WAV/stem exchange and MIDI exchange belong in the initial architecture.

## Required module catalogue

The [feature index](features/README.md) defines 22 domain capabilities, each with a matching core, API and presentation plan. Shared platform capabilities are adopted through the [foundation plan](FOUNDATION.md), rather than reimplemented as Music-owned identity or billing modules.

- [Projects and Sessions](features/projects.md): Project documents, tracks, folders, templates, revision history, autosave and portable session manifests.
- [Audio Engine and Transport](features/audio-engine.md): Native audio graph, sample clock, play/stop/seek, buffers, latency compensation and offline graph rendering.
- [Audio Devices and Monitoring](features/audio-devices.md): Device discovery, input/output channel mapping, sample rates, buffer sizes and direct/software monitoring.
- [Recording and Take Comping](features/recording.md): Track arming, count-in, punch and loop recording, take lanes, comp segments and recoverable disk writes.
- [Arrangement and Audio Editing](features/arrangement.md): Timeline clips, fades, splits, slip edits, crossfades, markers, warp anchors and nondestructive pitch/time changes.
- [Clip Launcher and Scenes](features/clip-launcher.md): Quantized clip launch, scenes, follow actions and recording performances into the arrangement.
- [MIDI and Expressive Editing](features/midi-sequencing.md): Piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export.
- [Tempo, Meter and Groove](features/tempo-groove.md): Tempo maps, meter changes, groove templates, swing, metronome and musical/sample-time conversion.
- [Instruments and Samplers](features/instruments.md): Built-in synth, drum machine, sampler, multisamples, voice allocation and portable instrument presets.
- [Audio Effects and Amp Processing](features/effects.md): EQ, dynamics, delay, reverb, modulation effects and independently designed amp/cabinet processing.
- [Plugin Hosting and Isolation](features/plugin-hosting.md): Plugin discovery, scanning, process isolation, state snapshots, compatibility and missing-plugin recovery.
- [Mixer and Routing](features/mixer-routing.md): Channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots.
- [Automation and Modulation](features/automation-modulation.md): Parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings.
- [Composition, Chords and Score](features/composition-score.md): Chord tracks, scales, voicings, articulation maps and notation views with printable parts.
- [Media Library and Content](features/media-library.md): Content-addressed audio assets, waveform peaks, metadata, tags, search, packs and rights provenance.
- [Presets, Racks and Templates](features/presets.md): Versioned instrument/effect presets, device racks, macros and reusable session templates.
- [Controllers and Hardware Integration](features/controllers.md): MIDI port mapping, controller learn, control surfaces, feedback and external clock synchronization.
- [Collaboration and Review](features/collaboration.md): Project membership integration, revision sharing, comments, review markers, locks and conflict branches.
- [Offline Storage and Synchronization](features/sync-offline.md): Local journals, pinned assets, resumable transfer, revision reconciliation and storage quotas.
- [Export, Mastering and Delivery](features/export-mastering.md): Offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests.
- [Video and Timecode](features/video-timecode.md): Reference video, frame-rate-aware timeline display, timecode offsets and audio-to-picture synchronization.
- [Live Performance and Setlists](features/live-performance.md): Setlists, cue preparation, preloaded projects, scene transitions and performance recovery.

## Required end-to-end journeys

1. Create a local project, select an audio device, record takes, comp a performance, save, simulate a crash and recover it.
2. Program an expressive MIDI part, load an instrument, launch clips, capture an arrangement and automate a bus effect.
3. Open a portable session with missing samples/plugins, locate or substitute dependencies, then render a mix and stems against a named revision.
4. Capture an idea on mobile without a connection, synchronize later, review it in a web workspace and continue editing on desktop.
5. Share a revision with a collaborator, receive timestamped comments, edit concurrently and resolve revisions without losing either contribution.
6. Preflight a setlist, switch prepared songs and recover from a disconnected audio interface during rehearsal.

## Delivery and acceptance

Follow the [delivery gates](DEVELOPMENT.md). A stage is complete only when its supported surfaces pass audio correctness, recovery, security, accessibility and representative hardware checks. A file count is documentation coverage, not implementation progress. The [architecture](ARCHITECTURE.md) defines the real-time boundary; the [support matrix](PRESENTATION.md) defines each presentation layer's actual responsibility.

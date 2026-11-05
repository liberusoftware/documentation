# Liberu Music delivery plan

**Status:** design only. No application source checkout, verified Composer/npm/pub identities, implementation inventory or installation procedure has been established by this documentation change. Do not turn design identifiers into installation commands.

## Delivery sequence

1. **Architecture prototype:** select native engine language/toolchain and desktop shell; record engine protocol, project schema and OS/device support decisions. Prove sample-clock scheduling, local journaling and device recovery before building the full interface.
2. **Recording foundation:** projects, audio engine, devices, media library, recording, arrangement, tempo/MIDI, basic instruments/effects, mixer, export and offline local save. Deliver one complete record → edit → reopen → bounce journey on a declared desktop target.
3. **Creative production:** clip launcher, automation/modulation, presets, controller mapping, expressive MIDI and expanded built-in instruments/effects. Test dense sessions and transitions on reference hardware.
4. **Professional workflows:** isolated plugin hosts, take comp refinements, composition/score, mastering, picture/timecode and preflighted live setlists. Certify formats and platforms individually.
5. **Connected workspaces:** authorized API, verified asset synchronization, collaboration/review and conflict recovery. Add Filament and Livewire operations, one Inertia frontend, and independently enabled Nuxt/Next.js adapters as required by adopters.
6. **Mobile delivery:** select React Native or Flutter for the first product host, integrate the shared native engine, then deliver the second adapter when needed. Start with offline capture, sketch, review and sync; expand only after physical-device evidence.

## Module release requirements

For each of the 22 [domain plans](features/README.md), define the actual repository, maintainers, manifest identities, license, runtime/schema compatibility, permissions, storage migrations and public commands/queries. Publish engine artifacts separately from Composer and frontend packages. Contract-test the enabled adapters against the same revision and capability schemas. Record implementation state and evidence rather than inferring it from this catalogue.

## Acceptance gates

- Audio: representative multitrack capture, callback deadline/underrun measurements, reference render comparison, delay compensation, MIDI cleanup and safe monitoring defaults.
- Recovery: crash during capture/save, disk full, missing plugin/media, device loss, interrupted upload, failed migration and restore from an exported session.
- Collaboration/security: wrong-workspace media denial, revoked shares, scoped event feeds, stale revisions, duplicate jobs and malicious plugin isolation.
- Presentation: a complete supported journey, visible local/save/sync states, keyboard and screen-reader navigation and honest unsupported-feature handling.
- Mobile: physical iOS/Android permission, interruption, background, route-change and low-storage checks with signed release builds.
- Operations: bounded render resources, cancellation, artifact retention, backup restore, alert ownership, redacted diagnostics and documented upgrade/rollback limits.

Release notes must list measured support, known limitations and migration steps. The full DAW is ready only when the scope's required journeys pass for the declared host; the existence of all adapter plans does not constitute release readiness.

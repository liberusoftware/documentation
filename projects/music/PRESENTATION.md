# Liberu Music presentation and mobile support

**Status:** target support tiers, not implemented parity. Every capability has a module plan on every documented layer; availability is discovered from the running host and device.

| Surface | Intended role | Audio and editing boundary |
| --- | --- | --- |
| Native desktop shell | Full arrangement, recording, clip performance, mixing, composition and delivery | Local native engine; plugin/device formats individually certified |
| Filament | Workspace administration, content packs, render jobs, compatibility and support diagnostics | Metadata and operations; no real-time DSP or recording callback |
| Livewire | Projects, library, review, settings and export status | Client player/editor components for supported previews; no server-driven audio clock |
| React + Inertia | Interactive DAW workspace inside Laravel | Client timeline and local engine bridge; server props carry authorized metadata |
| Vue + Inertia | Alternative interactive workspace inside Laravel | Same contract as React; application chooses a frontend rather than bundling both |
| Nuxt | Independent Vue project/review workspace and progressive browser editor | JSON API; browser engine capability checks; SSR excludes device APIs |
| Next.js | Independent React project/review workspace and progressive browser editor | JSON API; client-only audio/device components; no private asset caching across users |
| React Native + Expo | Mobile capture, sketch sequencer, review, asset sync and paired transport | Native modules/development builds for required audio features; device-tested subset |
| Flutter | Alternative mobile capture, sketch sequencer, review, sync and paired transport | Native audio bridge/FFI; DSP off UI isolate; device-tested subset |

React and Vue refer to Inertia adapters here; Nuxt and Next.js are independent API consumers. A desktop shell may reuse a web workspace through a secure engine bridge; shell technology remains an architecture decision. Never grant renderer code unrestricted filesystem or shell access.

## Capability tiers

1. **Management and review:** all presentation surfaces can expose authorized projects, media metadata, revision comments and render status. Device/engine modules present configuration and diagnostics when execution is unavailable.
2. **Capture and sketch:** mobile and capable browsers add audio capture, simple arrangement, MIDI entry, built-in instruments and local draft saving after permission and hardware validation.
3. **Full production:** native desktop adds validated multitrack I/O, native plugins, advanced routing, modulation and live performance. A mobile/browser feature enters this tier only after measured release criteria pass.

Composition/score, video, advanced plugins and live-performance adapters on mobile begin as review, rehearsal or remote-control workflows. Do not display editable controls that silently discard unsupported state. Preserve unfamiliar session data when saving a supported subset; use frozen stems for preview when available.

## Common interaction requirements

Provide a project navigator, transport, arrangement/launcher, inspector, mixer and library as the chosen surface allows. Support keyboard remapping, focus order, non-color recording indicators, screen-reader track/parameter descriptions, touch targets and non-drag alternatives for timeline edits. Rate-limit visual meters without affecting audio scheduling. Display the recording input, monitoring state, local save state, sync state and render revision clearly.

Mobile must handle microphone/Bluetooth permissions, calls, audio focus loss, wired/Bluetooth route changes, lock screen, battery/thermal limits and background suspension. Show actual route/latency limitations; Bluetooth availability does not imply suitability for live monitoring. Keep recordings durable before any upload. Remote control and local audio capture are separate modes with explicit status.

## Release verification

Verify keyboard/screen-reader journeys and reduced motion on web/desktop. Verify mobile on physical iOS and Android devices with signed builds, revoked permissions, interrupted capture, low storage, offline relaunch, conflicts and secure logout. Test browser capability fallback and server-rendering boundaries. Document minimum OS/browser versions only after compatibility testing.

Use the [presentation runbooks](../../guides/presentation/README.md) and [web/mobile standard](../../user-guides/WEB-AND-MOBILE.md). Layer indexes are in the [Music index](README.md).

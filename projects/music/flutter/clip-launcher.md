# Liberu Music: Clip Launcher and Scenes — Flutter

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#clip-launcher). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-clip-launcher-flutter`. Uses [core](../core/clip-launcher.md) and, for remote access, [API](../api/clip-launcher.md).

## Surface workflow

Present: launch a scene, override one clip and capture the performance to the timeline. Domain scope: quantized clip launch, scenes, follow actions and recording performances into the arrangement.

Use a versioned native engine interface and keep DSP off the Dart UI isolate. Handle microphone permission, audio focus, route changes, interruptions and background restrictions. Store credentials in platform secure storage.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify quantized launches during tempo changes and reject invalid follow-action cycles. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: launch decisions execute on the engine clock at the chosen musical boundary.

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `clip-launcher`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-music-daw-mobile-flutter`](https://github.com/liberusoftware/project-music-daw-mobile-flutter) | [`module-music-clip-launcher-flutter`](https://github.com/liberusoftware/module-music-clip-launcher-flutter) (`module_music_clip_launcher_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-music-daw-dart-mobile`](https://github.com/liberusoftware/project-music-daw-dart-mobile) | [`module-music-clip-launcher-dart-mobile`](https://github.com/liberusoftware/module-music-clip-launcher-dart-mobile) (`module_music_clip_launcher_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-music-daw-dart-desktop`](https://github.com/liberusoftware/project-music-daw-dart-desktop) | [`module-music-clip-launcher-dart-desktop`](https://github.com/liberusoftware/module-music-clip-launcher-dart-desktop) (`module_music_clip_launcher_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | [API plan](../api/clip-launcher.md) · [Core plan](../core/clip-launcher.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Quantized clip launch** | Adaptive mobile cards/sheets for `quantized clip launch` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quantized clip launch` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-music-daw-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Scenes** | Adaptive mobile cards/sheets for `scenes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `scenes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-music-daw-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Follow actions** | Adaptive mobile cards/sheets for `follow actions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `follow actions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-music-daw-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recording performances into the arrangement** | Adaptive mobile cards/sheets for `recording performances into the arrangement` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recording performances into the arrangement` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-music-daw-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->

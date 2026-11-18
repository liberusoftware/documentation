# Implement Dart Desktop and Dart Mobile Presentation Layers

The `-dart-desktop` and `-dart-mobile` repositories are independent native applications written in Dart using a Flutter native host for windowing, rendering, accessibility, and platform integration. While `-mobile-flutter` provides the general Flutter mobile foundation, the `-dart-desktop` and `-dart-mobile` families maintain separate application roots, release identities, OS targets, and reusable Dart/pub capability packages.

These applications consume the matching product's [`project-{product}-laravel-api`](../LARAVEL-API-BACKENDS.md) backend. They never execute PHP on a device or duplicate server-side business invariants. Follow [presentation architecture](../../architecture/PRESENTATION.md), [mobile architecture](../../architecture/MOBILE.md), [Flutter standard](../../standards/FLUTTER.md), and the [Flutter implementation runbook](FLUTTER.md).

## 1. Liberu boilerplate and skeleton repositories

| Surface | Application template & product skeletons | Module foundation & capability catalog | Wayfinder specification |
| --- | --- | --- | --- |
| **Dart Desktop** (`Linux`, `macOS`, `Windows`) | [`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) · `project-{product}-dart-desktop` ([catalog](../../projects/REPOSITORIES.md#mobile-and-desktop-applications)) | [`module-boilerplate-dart-desktop`](https://github.com/liberusoftware/module-boilerplate-dart-desktop) · [631 desktop module skeletons](../../modules/skeletons/dart-desktop.md) (`module_{capability}_dart_desktop`) | [dart-desktop.md](../../projects/wayfinders/dart-desktop.md) |
| **Dart Mobile** (`iOS`, `Android`) | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · `project-{product}-dart-mobile` ([catalog](../../projects/REPOSITORIES.md#mobile-and-desktop-applications)) | [`module-boilerplate-dart-mobile`](https://github.com/liberusoftware/module-boilerplate-dart-mobile) · [631 mobile module skeletons](../../modules/skeletons/dart-mobile.md) (`module_{capability}_dart_mobile`) | [dart-mobile.md](../../projects/wayfinders/dart-mobile.md) |

## 2. Choose a target and initialize the skeleton

Use the exact Flutter/Dart version pinned in `.flutter-version` or `.fvmrc` (baseline: Flutter 3.47.9 with Dart 3.13.7). Commit `pubspec.lock` for applications and retain `publish_to: none` in application `pubspec.yaml` files.

For an existing product skeleton clone:

```bash
flutter --version
flutter doctor -v
flutter pub get
flutter analyze
flutter test
flutter devices
```

Run on the target platform with the product's `-laravel-api` origin:

```bash
# Desktop: use the matching operating system and native C++/Xcode/GTK development tools.
flutter run -d linux --dart-define=API_BASE_URL=https://api.example.com
flutter run -d macos --dart-define=API_BASE_URL=https://api.example.com
flutter run -d windows --dart-define=API_BASE_URL=https://api.example.com

# Mobile: select a connected iOS/Android device or simulator.
flutter run -d <device-id> --dart-define=API_BASE_URL=https://api.example.com
```

Do not rerun `flutter create` over an existing skeleton clone. When bootstrapping a brand-new empty directory outside the existing product skeletons, the corresponding upstream commands are:

```bash
flutter create --org com.yourorganization --platforms linux,macos,windows your_desktop
flutter create --org com.yourorganization --platforms android,ios your_mobile
```

Before distribution, replace placeholder bundle/application IDs, display names, window titles, icons, and signing configuration; platform identifiers are distinct from GitHub repository slugs.

## 3. Connect to `project-{product}-laravel-api` and structure layers

```text
lib/
  main.dart                    # environment bootstrap and API_BASE_URL validation
  app/                         # window/navigation shell, theme tokens, session provider
  features/<capability>/       # composition of module_<capability>_dart_desktop or _dart_mobile
  contracts/                   # checked Dart DTOs aligned with OpenAPI 3.1 schemas
  session/                     # platform-secure credential storage and single-flight refresh
  storage/                     # account/workspace-scoped cache and draft persistence
  platform/                    # desktop file/print dialogs or mobile deep links/permissions
```

1. **Checked DTOs and transport:** Validate every JSON field in `fromJson` factories against the product's OpenAPI contract. Map `200`/`201`, `202` (pending operation), `401` (refresh/reauthenticate), `403` (denied), `409`/`412` (revision/idempotency conflict), `422` (field errors), and `429` (rate limit) into explicit typed Dart result states.
2. **Session and tenant isolation:** Store refresh/session tokens in platform-secure storage (Keychain on macOS/iOS, Keystore on Android, Libsecret/Keyring on Linux, Credential Locker on Windows). Isolate local caches and draft queues by authenticated actor and active workspace/tenant/store; purge scoped state on sign-out or workspace switch.
3. **Desktop UX requirements (`-dart-desktop`):**
   - Implement resizable master-detail panes, dense keyboard-navigable tables, explicit focus order (`FocusTraversalGroup`), and shortcut bindings (`Shortcuts` / `Actions`).
   - Coordinate state across window resize, close/reopen, and optional multi-window workflows so two open windows cannot silently overwrite a newer server revision or submit duplicate non-idempotent commands.
   - Scope file-save, print, and export dialogs to authorized projections and safe user-selected directories.
4. **Mobile UX requirements (`-dart-mobile`):**
   - Implement touch-sized controls, `SafeArea` padding, adaptive cards/sheets, semantic screen-reader labels, platform back gestures, and validated app/universal links.
   - Refresh active record revisions on foreground resume and reconcile uncertain network writes via `Idempotency-Key` before retrying.

## 4. Implement and integrate a capability module skeleton

Each capability in [modules/skeletons/dart-desktop.md](../../modules/skeletons/dart-desktop.md) (`module-{capability}-dart-desktop`, pub name `module_{capability}_dart_desktop`) and [modules/skeletons/dart-mobile.md](../../modules/skeletons/dart-mobile.md) (`module-{capability}-dart-mobile`, pub name `module_{capability}_dart_mobile`) starts from `module-boilerplate-dart-desktop` or `module-boilerplate-dart-mobile` and includes `module-skeleton.json`.

1. Clone the capability module skeleton alongside the host skeleton and inspect `module-skeleton.json`, `pubspec.yaml`, and the feature/aspect matrix in `projects/{product}/flutter/{module}.md`.
2. Implement the capability's checked DTOs, abstract repository interface, and desktop or mobile widgets under `lib/src/`, exporting the public contract from `lib/module_{capability}_dart_desktop.dart` (or `_dart_mobile.dart`).
3. Do not add `package.json` to represent a Dart package, and do not import mobile-only native plugins into a `-dart-desktop` module. Declare supported platforms explicitly in `pubspec.yaml`.
4. During local development, wire the package in a temporary workspace using a `path:` dependency, run `flutter analyze` and `flutter test` in both the module and the host, and replace `path:` with the reviewed Git tag or hosted pub version before release.

## 5. Verify native platform delivery

For **Dart desktop (`-dart-desktop`)**, verify keyboard navigation, focus traversal, window resizing, multi-window safety, file/print export permissions, and scoped storage on each target OS:

```bash
flutter build linux --release --dart-define=API_BASE_URL=https://api.example.com
flutter build macos --release --dart-define=API_BASE_URL=https://api.example.com
flutter build windows --release --dart-define=API_BASE_URL=https://api.example.com
```

For **Dart mobile (`-dart-mobile`)**, verify safe areas, permissions, deep links, background/resume, logout cleanup, secure storage, and offline reconciliation on both iOS and Android:

```bash
flutter build appbundle --release --dart-define=API_BASE_URL=https://api.example.com
flutter build ipa --release --dart-define=API_BASE_URL=https://api.example.com
```

`flutter analyze` and widget tests verify Dart-level logic; they do not substitute for a signed native build, physical-device or native-OS verification, installer notarization, store review, or an end-to-end journey against `project-{product}-laravel-api`. Record build artifacts, OS versions, and test evidence in the repository's wayfinder issue before marking a capability complete.

Upstream references: [Flutter desktop support](https://docs.flutter.dev/platform-integration/desktop), [supported platforms](https://docs.flutter.dev/reference/supported-platforms), [Dart project templates](https://dart.dev/tools/dart-create), and [Flutter installation](https://docs.flutter.dev/install).

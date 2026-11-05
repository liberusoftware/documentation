# Initialize Dart desktop and mobile projects

The `-dart-desktop` and `-dart-mobile` repositories are separate applications written in Dart. They use Flutter for the native window, rendering, accessibility and platform host. A standalone Dart console project does not supply a native desktop or mobile interface. The `-mobile-flutter` family is the general Flutter mobile foundation; the Dart families keep independently maintained desktop and mobile application roots, release identities and platform configuration.

These shells consume reviewed Laravel APIs. They do not run PHP on a device or replicate server-side domain rules. Follow [presentation architecture](../../architecture/PRESENTATION.md), [mobile behavior](../../architecture/MOBILE.md) and the [Flutter implementation guide](FLUTTER.md).

## Choose a target and toolchain

Use the exact Flutter version in `.flutter-version` or `.fvmrc`. The initial generated baseline is Flutter 3.47.9 with Dart 3.13.7. Use the Dart SDK bundled with that Flutter version to avoid mismatched framework packages. Commit `pubspec.lock` for applications and keep `publish_to: none` in their pubspecs.

For an existing skeleton clone:

```bash
flutter --version
flutter doctor -v
flutter pub get
flutter analyze
flutter test
flutter devices
```

Select a target listed by `flutter devices`:

```bash
# Desktop: use the matching operating system and native development tools.
flutter run -d linux
flutter run -d macos
flutter run -d windows

# Mobile: select a connected iOS/Android device or simulator.
flutter run -d <device-id>
```

Do not rerun a generator over existing work. For a new empty project, the corresponding upstream bootstrap commands are:

```bash
flutter create --org com.yourorganization --platforms linux,macos,windows your_desktop
flutter create --org com.yourorganization --platforms android,ios your_mobile
```

Use identifiers owned by the intended publisher. Before distribution, replace the skeleton bundle/application IDs, display names, icons and signing configuration; identifiers are distinct from GitHub repository slugs. Desktop builds require the matching OS tools. iOS builds require macOS/Xcode. Android builds require the documented Android SDK/JDK setup.

## Keep the application and packages separate

The application composes `lib/app`, feature presentation, contracts, session, storage, sync and platform boundaries. Widgets render state and emit intent. Inject reviewed transports and session services; keep policy, tenant authorization, database ownership and state transitions in Laravel. API URLs compiled through `--dart-define` are public configuration, not secret storage.

Create reusable Dart contracts with `dart create -t package`; create reusable Flutter widgets with `flutter create --template package`. Each independent module needs its own `pubspec.yaml`, `lib` public entry, README, tests, license and supported-platform declaration. Do not add `package.json` merely to represent a Dart package. Use npm only for actual JavaScript/TypeScript libraries, and Composer only for PHP packages. Review a package's platform support before installing it in desktop and mobile applications.

An application can reference a package in a temporary local integration workspace using a pub path dependency. Before a release, replace it with the reviewed Git/tag or hosted-package dependency, run tests in a clean consumer and verify the release artifact. Keep public package identities separate from application IDs and repository names. See [Dart package creation](https://dart.dev/tools/pub/create-packages) and [Flutter package development](https://docs.flutter.dev/packages-and-plugins/developing-packages).

## Verify platform delivery

For desktop, verify keyboard navigation, focus, resizing, window close/reopen, file dialogs, permissions and scoped storage. Build the matching native target:

```bash
flutter build linux
flutter build macos
flutter build windows
```

For mobile, verify safe areas, permissions, deep links, background/resume, logout, secure storage and offline reconciliation on both operating systems. Build with reviewed signing configuration:

```bash
flutter build appbundle
flutter build ipa
```

`flutter analyze` and widget tests verify Dart-level behavior. They do not prove a signed native build, physical-device behavior, installer notarization, store approval or a production API journey. Record these results separately in each repository's delivery notes. A local draft or queued write must not be shown as an authoritative completed transaction.

Upstream references: [Flutter desktop support](https://docs.flutter.dev/platform-integration/desktop), [supported platforms](https://docs.flutter.dev/reference/supported-platforms), [Dart project templates](https://dart.dev/tools/dart-create), and [Flutter installation](https://docs.flutter.dev/install).

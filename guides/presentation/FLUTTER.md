# Implement Flutter mobile presentation and Dart packages

Flutter is an independent iOS/Android API client using Dart and native device integration. Follow the [foundation/API selection](README.md), [mobile architecture](../../architecture/MOBILE.md) and [Flutter standard](../../standards/FLUTTER.md). Reuse reviewed API schemas, behavior and semantic tokens; implement native mobile layouts instead of copying desktop components. Flutter packages use Dart/pub, while installed apps use signed platform artifacts.

## 1. Create and pin the mobile skeleton

Install the supported stable Flutter SDK and record its exact version in the development/CI toolchain. Install Android SDK/JDK and, for local iOS work, macOS/Xcode with the required native dependency tools. Run:

```bash
flutter --version
flutter doctor -v
flutter create --org com.example --platforms android,ios example_mobile
cd example_mobile
flutter pub get
flutter analyze
flutter test
flutter devices
flutter run -d <device-id>
```

Replace `com.example` with your owned reverse-domain identifier before registering store apps. Keep the app `publish_to: none`, commit its `pubspec.lock`, generated platform projects and safe configuration, and preserve the template's lint rules. Follow [Flutter setup](https://docs.flutter.dev/install) for SDK/platform requirements. API base addresses in `--dart-define` are public binary configuration, not a secret store.

## 2. Separate UI, state and data access

```text
lib/
  main.dart                    # environment bootstrap
  app/                         # navigation, theme, session composition
  features/example/
    data/                      # API mapping and repository implementation
    presentation/              # screen/view-model and state
  contracts/                   # generated/checked public DTOs
  session/                     # secure credentials and refresh coordination
  storage/                     # scoped cache and migrations
  sync/                        # optional queue and reconciliation
  platform/                    # push, files, camera, deep links
```

Inject repositories/transport/session interfaces at application composition. Widgets render state and emit intent; they do not resolve tenants, perform authorization or access Laravel tables. Pick a simple state-management approach compatible with the product, and document it rather than adding several competing frameworks. The app owns route identifiers, environment and platform configuration; reusable capability packages own focused widgets, DTO mapping and contracts.

## 3. Implement the reviewed read contract

Add only required, reviewed dependencies; for a basic HTTP transport:

```bash
flutter pub add http
```

For the illustrative `{ data: [{ id: string, title: string }] }` response, create a checked DTO and repository. Put these types in their used files and export only the public contract:

```dart
class ExampleRecord {
  const ExampleRecord({required this.id, required this.title});
  final String id;
  final String title;

  factory ExampleRecord.fromJson(Object? value) {
    if (value is! Map<String, dynamic> ||
        value['id'] is! String || value['title'] is! String) {
      throw const FormatException('Invalid record');
    }
    return ExampleRecord(id: value['id'] as String, title: value['title'] as String);
  }
}

abstract interface class ExampleRepository {
  Future<List<ExampleRecord>> list();
}
```

Use generated DTOs checked against the API where available and preserve pagination metadata. A public-read implementation can be:

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;
// Import ExampleRecord and ExampleRepository from your contract file.

class HttpExampleRepository implements ExampleRepository {
  HttpExampleRepository(this.client, this.base);
  final http.Client client;
  final Uri base;

  @override
  Future<List<ExampleRecord>> list() async {
    final response = await client.get(
      base.resolve('/api/v1/example-records'),
      headers: {'Accept': 'application/json'},
    ).timeout(const Duration(seconds: 10));
    if (response.statusCode != 200) throw Exception('Records unavailable');
    final Object? value = jsonDecode(response.body);
    if (value is! Map<String, dynamic> || value['data'] is! List) {
      throw const FormatException('Invalid response');
    }
    return (value['data'] as List).map(ExampleRecord.fromJson).toList();
  }
}
```

This intentionally unauthenticated example requires an approved public endpoint. Replace it for protected data with a request-scoped credential/context adapter and typed status mapping. Bound response sizes where appropriate, close the app-owned `http.Client` when disposed and document actual cancellation behavior: timing out a Dart future alone does not guarantee cancellation of the underlying request.

Read `const String.fromEnvironment('API_BASE_URL')` at bootstrap, validate the required HTTPS origin and inject `Uri`/transport. For local devices use a reachable development host rather than assuming `localhost` is your workstation. Keep any development transport exception out of release configuration.

## 4. Render native loading, empty, error and data states

A minimal screen with an injected repository:

```dart
import 'package:flutter/material.dart';
// Import ExampleRecord and ExampleRepository from your contract file.

class ExampleScreen extends StatefulWidget {
  const ExampleScreen({super.key, required this.repository});
  final ExampleRepository repository;
  @override
  State<ExampleScreen> createState() => _ExampleScreenState();
}

class _ExampleScreenState extends State<ExampleScreen> {
  late Future<List<ExampleRecord>> records;
  @override
  void initState() {
    super.initState();
    records = widget.repository.list();
  }
  @override
  void didUpdateWidget(covariant ExampleScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.repository != widget.repository) records = widget.repository.list();
  }
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Records')),
    body: SafeArea(child: FutureBuilder<List<ExampleRecord>>(
      future: records,
      builder: (context, snapshot) {
        // Do not display retained previous-context data while a new load is pending.
        if (snapshot.connectionState != ConnectionState.done) {
          return const Center(child: CircularProgressIndicator(semanticsLabel: 'Loading records'));
        }
        if (snapshot.hasError) return Center(child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text('Records unavailable.'),
            TextButton(onPressed: () => setState(() {
              records = widget.repository.list();
            }), child: const Text('Retry')),
          ],
        ));
        final values = snapshot.data ?? const <ExampleRecord>[];
        if (values.isEmpty) return const Center(child: Text('No records available.'));
        return ListView.builder(itemCount: values.length, itemBuilder: (context, index) =>
          ListTile(title: Text(values[index].title)));
      },
    )),
  );
}
```

Construct it under a `MaterialApp` in the app shell with an injected repository. Replace/remount the authenticated subtree when actor/workspace changes, abort obsolete requests when supported and clear retained view state. Add pagination, refresh, typed denied/expired/offline states and navigation to detail. Use touch-sized controls, safe-area/keyboard behavior, semantic labels, text scaling, RTL and platform back behavior. Avoid fixed desktop widths, hover-only actions and dense tables on phones.

## 5. Integrate sessions and commands

Use the reviewed mobile authentication API: OAuth/OIDC through a system browser with PKCE when supported, or the API's documented first-party token issue/refresh/revoke flow. Do not embed a confidential client secret. Store persistent secrets with an approved Keychain/Keystore-backed plugin, review its supported platform settings/backup behavior and keep access credentials in memory where feasible. Secure storage must be initialized and error handling must support locked/unavailable storage and reauthentication.

At startup load session state, validate/refresh with one coordinated refresh request, establish authorized context, then show authenticated navigation. On logout/revocation/context change clear scoped repositories, cached data and queued work, revoke the credential where supported and reset the navigation stack. A local cache or hidden widget never grants access.

For a command screen:

1. Render a `Form` with labelled `TextFormField` controls and a native submit button. Use input hints/keyboard types and local shape validation for usability.
2. Submit a typed command through an injected repository, with the actual auth/context/idempotency/version contract. Laravel owns final validation, permission checks, transactions and audit.
3. Map actual responses to completed, accepted/pending, validation (422), denied (403), expired (401), conflict (409), rate limited (429) and uncertain network outcomes. Show field errors and move semantic focus to the error summary/first invalid control.
4. Preserve safe drafts on backgrounding or recoverable failure. Query the owner operation after ambiguous submission before replaying. Disable accidental double taps but do not rely on that as server idempotency.
5. Refresh scoped reads only after confirmed success; show an operation reference for pending work and a conflict review path when needed.

## 6. Implement offline and platform features deliberately

Default to online commands until a capability has a defined offline contract. For offline capture, persist a scoped queue with schema version, command identity, actor/workspace, payload, expiry, retries and visible state. Classify/encrypt sensitive retained data, cap storage, document backup/wipe rules and migrate local schemas on upgrade. Local capture is not an approved business transition.

On network recovery/app resume, revalidate identity/context and server state before replay. Reconcile ambiguous commands, then retry eligible work with bounded backoff/jitter; conflicts and denied access need review rather than endless retries. Test process death and restart during persistence/replay. iOS/Android background work is scheduled by the OS and is not guaranteed to run immediately.

Register and validate app/universal links against allowlisted destinations. Treat push data as a notification to refetch authorized state. Request camera/location/notification permissions when needed and provide a denial path. Keep platform entitlement/permission descriptions, privacy manifests and plugin configuration in the app. Test cold/resumed navigation and clean up push/device associations on logout.

## 7. Create a reusable Flutter package

Use Dart's underscore package-name format; the repository basename may remain `module-<capability>-flutter`, while its actual `pubspec.yaml` name might be `module_example_flutter`. Confirm real identities rather than converting names during installation. Create a package separately from the app:

```bash
flutter create --template=package module_example_flutter
cd module_example_flutter
flutter pub get
```

Keep public exports in `lib/module_example_flutter.dart` and implementation in `lib/src/`. Export widgets/contracts and inject transport/session/navigation; do not ship application IDs, signing configuration or a copied backend. Add only the Flutter SDK and actual runtime dependencies to `dependencies`; lint/test/generation tools go in `dev_dependencies`. Set supported Dart/Flutter constraints to the tested range and declare required assets under the package's `flutter` section. A true native plugin uses the Flutter plugin template with explicit platforms and requires native source plus a platform example app. See [package development](https://docs.flutter.dev/packages-and-plugins/developing-packages).

Add an `example/` consumer app. During local integration its `pubspec.yaml` can use:

```yaml
dependencies:
  module_example_flutter:
    path: ../
```

Use the real path for external application clones. Run package analysis/tests and the example's builds on both platforms. Inspect the publication file list, then create an isolated consumer from a copy containing **only** the listed publication files; a path dependency on the working tree can hide omitted assets/source. After publication, replace it with the exact hosted version and repeat integration checks. Keep application locks committed; follow Dart conventions for reusable-library lockfiles and test lower/upper supported dependency resolutions as appropriate.

## 8. Publish the Dart package

Flutter libraries generally distribute source for the consumer's compiler; `flutter build` produces app artifacts, not an npm-style library `dist`. Prepare description, semantic version, repository/homepage, supported platforms, README install/usage, CHANGELOG and LICENSE. Remove `publish_to: none` from the package only when intentionally publishing publicly; retain it in apps. Use the approved private hosted registry configuration if public pub.dev is inappropriate.

```bash
dart format --output=none --set-exit-if-changed .
flutter analyze
flutter test
flutter pub publish --dry-run
```

Review every listed file and warning; use `.pubignore` for exclusions and ensure credentials, private fixtures, build output and signing material are absent. Test the isolated publication file set as described above. Verify the publishing account/verified publisher and package ownership, commit the reviewed version/release notes, and publish from that exact clean source:

```bash
flutter pub publish
```

Complete the authorized authentication/confirmation flow. For automated releases, configure pub.dev's supported CI publishing identity and immutable tag workflow, following [Dart publishing](https://dart.dev/tools/pub/publishing). Verify the hosted version and publisher, install it into a clean mobile consumer, analyze/test/build and record its source ref and results. Publish fixes as new versions; use the registry's documented retraction/discontinuation tools when appropriate and move consumers to a verified compatible version.

## 9. Build, sign and distribute the mobile application

In the **application** directory, configure flavor/environment strategy, identifiers, icons, permissions, release version/build number and store records. Keep keystores, passwords, certificates and provisioning material in approved local/CI stores. Add Android network permission where required in the main manifest and use HTTPS; iOS transport/entitlements and privacy descriptions must match the enabled features. Configure release signing before producing store artifacts.

```bash
flutter pub get
flutter analyze
flutter test
flutter build appbundle --release --dart-define=API_BASE_URL=https://api.example.com
flutter build ipa --release --dart-define=API_BASE_URL=https://api.example.com
```

Use the selected flavor's flags when configured. Android produces its app bundle under `build/app/outputs/bundle/`; iOS archives/IPA are under `build/ios/` and require macOS, a registered bundle ID and valid team/provisioning. Follow [Android signing and release](https://docs.flutter.dev/deployment/android) and [iOS signing and release](https://docs.flutter.dev/deployment/ios) for current platform requirements.

Test signed releases through Play internal testing and TestFlight on actual supported devices. Verify login/refresh/logout, API environment, permissions, push/deep links, offline/uncertain commands, background/process death and upgrade/storage migrations. Retain required symbol/debug artifacts for redacted crash analysis. Complete store privacy/data-safety metadata, SDK disclosures, screenshots and applicable account-deletion requirements before store submission.

Roll out gradually, monitor crashes/API failures and keep the backend compatible with older installed binaries. A bad store release is recovered with server feature controls and a new signed version; changing a pub package or server deployment does not replace an installed mobile binary. Record build numbers, signing identity, source ref, SDK, API versions and recovery instructions with each release.

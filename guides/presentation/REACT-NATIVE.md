# Implement React Native and Expo mobile presentation

React Native is a native iOS/Android API client, not a React DOM/Inertia app. Expo is a React Native framework and delivery workflow. Follow [the foundation/API selection](README.md), [mobile architecture](../../architecture/MOBILE.md) and [mobile standards](../../standards/MOBILE.md). Reuse DTOs, intent/outcome types and design tokens with web when compatible; use native controls, navigation and device services rather than copying desktop pages.

## 1. Select the device baseline and create the skeleton

Record supported iOS/Android versions, phones/tablets, orientations, accessibility requirements, API compatibility window and required native dependencies. Prefer Expo if its development-build/config-plugin model covers them. Use Node LTS, Android Studio/SDK/JDK for local Android builds and macOS/Xcode/CocoaPods for local iOS builds. A cloud build can produce iOS artifacts from another development OS, but simulator/device verification still needs the relevant environment. See [React Native environment setup](https://reactnative.dev/docs/set-up-your-environment).

For a new Expo app:

```bash
npx create-expo-app@latest example-mobile
cd example-mobile
npx expo install expo-secure-store expo-dev-client
npx expo-doctor
npx expo start
```

Review the template SDK against the current [Expo project guide](https://docs.expo.dev/get-started/create-a-project/), especially during SDK transitions; select an explicit supported template when required. Use `npx expo install` for SDK-compatible native dependencies. Set `private: true`, retain the generated lockfile and strict TypeScript settings, and record SDK/React Native/React/Node versions. Add a `typecheck: tsc --noEmit` script. Use a development build for native modules rather than assuming Expo Go supports every capability.

For a deliberate bare React Native app, use the official [without-a-framework setup](https://reactnative.dev/docs/getting-started-without-a-framework), currently `npx @react-native-community/cli@latest init ExampleMobile`. Review generated versions, install the template's native dependencies, and run its Android/iOS commands after environment setup. Native `android/` and `ios/` projects then belong to the application and need their own upgrade/signing process. The API/package/security steps below apply to both shells.

## 2. Arrange application composition

```text
app/ or src/app/              # use the generated Expo Router route root
  _layout.tsx                # session provider, navigation stack
  sign-in.tsx
  (authenticated)/           # protected navigation UX, not server policy
src/
  features/example/          # composition of the capability adapter
  api/                       # fixed-base transport and error mapping
  contracts/                 # reviewed/generated DTOs
  session/                   # session state and secure-storage adapter
  storage/                   # scoped cache, retention and migrations
  sync/                      # explicit queue/reconciliation, if enabled
  platform/                  # notifications, files, camera, deep links
```

Use the selected template's actual route root, without creating a competing one. Keep session/transport/cache providers app-owned and inject them into reusable screens. Do not import Next.js, DOM, Inertia or Laravel internals. Declare stable bundle/application identifiers, scheme, display name, icons and platform permissions in app configuration. An `EXPO_PUBLIC_API_BASE_URL` is public configuration embedded in the app; it must never contain secrets.

On a physical device `localhost` refers to that device. Use a reachable development API host over the intended transport; Android emulator routing differs from iOS simulator routing. Restrict any development transport exception to debug builds. Production uses HTTPS.

## 3. Integrate mobile authentication

Use the actual API's mobile identity contract. If it supports OAuth/OIDC, use the system browser with Authorization Code + PKCE for a public native client and validate state/nonce/callbacks. If it uses first-party API tokens, follow its reviewed issue/refresh/revoke endpoints and scopes. Never embed a confidential client secret, administrator token or browser session workaround in a mobile binary.

Store long-lived refresh/session secrets through a Keychain/Keystore-backed adapter (Expo SecureStore in the Expo shell); keep short-lived access credentials in memory where feasible. Configure backup/accessibility behavior for the threat model. Secure storage is not a general offline database and credentials may need reauthentication after reinstall/restore. See [Expo SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/).

At boot, load session state, validate/refresh it once through a single-flight operation, establish the authorized workspace, then render authenticated routes. On 401, attempt only the documented bounded refresh path; otherwise reauthenticate. On logout revoke the server credential where supported, remove local credentials, clear scoped cache/queues, unregister device push associations and reset navigation. Treat permission/workspace changes as cache invalidation events.

## 4. Implement an injected API client and a native screen

For an illustrative public DTO `{ data: Array<{ id: string; title: string }> }`, define a capability-facing interface:

```ts
export type ExampleRecord = { id: string; title: string };
export interface ExampleApi {
  list(signal: AbortSignal): Promise<ExampleRecord[]>;
}
```

The application implements `list` with the trusted API base, current access credential and established context. Use `Accept: application/json`, bounded timeout/cancellation, and runtime validation of every response field before returning DTOs. Map actual API error codes into typed outcomes, preserve pagination, redact diagnostics and abort requests on context changes. Never capture an old user's token in a shared singleton. This is an integration seam; the endpoint and session resolver must come from the reviewed API.

A minimal adapter screen with cancellation, retry, loading, failure and empty states:

```tsx
import { useEffect, useState } from 'react';
import { ActivityIndicator, Button, FlatList, Text, View } from 'react-native';
import type { ExampleApi, ExampleRecord } from './contracts.js';

export function ExampleScreen({ api }: { api: ExampleApi }) {
  const [records, setRecords] = useState<ExampleRecord[] | null>(null);
  const [failed, setFailed] = useState(false);
  const [attempt, setAttempt] = useState(0);
  useEffect(() => {
    const controller = new AbortController();
    setRecords(null); setFailed(false);
    api.list(controller.signal).then(value => {
      if (!controller.signal.aborted) setRecords(value);
    }).catch(() => {
      if (!controller.signal.aborted) setFailed(true);
    });
    return () => controller.abort();
  }, [api, attempt]);
  if (failed) return <View><Text accessibilityRole="alert">Records unavailable.</Text>
    <Button title="Retry" onPress={() => setAttempt(value => value + 1)} /></View>;
  if (records === null) return <ActivityIndicator accessibilityLabel="Loading records" />;
  return <FlatList data={records} keyExtractor={item => item.id}
    ListEmptyComponent={<Text>No records available.</Text>}
    renderItem={({ item }) => <Text>{item.title}</Text>} />;
}
```

Create `src/contracts.ts` with the interface above and import this screen into an application route. Memoize the injected client for the current session/workspace and replace it when that context changes. Add safe-area layout, a clear page title, pagination/refresh and typed denied/session-expired states before production. Do not use a desktop table compressed into a phone: use progressive detail screens, touch-sized actions, platform back behavior and screen-reader focus.

## 5. Add a mobile command journey

Use native labelled inputs, keyboard types and safe-area/keyboard avoidance. Submit a typed intent to the injected API client, disable accidental repeat submission, and render field validation beside inputs with accessible announcements. The server still validates permissions, tenant context and business state.

Distinguish invalid (422), denied (403), expired (401), conflict (409), rate-limited (429), accepted/pending (202), completed and uncertain network outcomes according to the actual contract. Keep a safe draft on interruption. Reconcile uncertain submissions by operation/command identity before retrying; only reuse idempotency keys when the owner supports them. For pending work, show status and a later recovery path rather than keeping the user on an indefinite spinner.

## 6. Make offline, lifecycle and device behavior explicit

Start online-only unless a capability has a defined offline policy. If offline capture is needed, persist a scoped draft/queue with command identity, payload schema version, creation/expiry time, actor/workspace, retry count and status. Encrypt/classify retained data, cap size and retention, and exclude sensitive content from unapproved backups. Persist queue transitions transactionally.

On resume/network recovery, revalidate credentials, workspace and permissions; reconcile uncertain writes, then replay eligible queued commands with bounded exponential backoff/jitter. A network indicator alone does not prove API reachability. Separate retryable transport failures from validation/denial/conflict; ask for review when necessary. Local queued/accepted/completed states must be visibly distinct. Do not promise background execution that iOS/Android can suspend or kill. Test process death during each queue transition and migrate stored data on upgrade.

Validate deep links and push destinations against allowlisted routes/identifiers and require fresh authorization when opening them. A push payload is a hint to fetch permitted data, not a trusted record. Ask for camera/location/notification permissions at the moment of use, explain why and support denial. Use minimal notification text and scoped expiring downloads. Test screen readers, large text, RTL, reduced motion, rotation and system back gestures on devices.

## 7. Build a reusable mobile package

Use `module-<capability>-react-native` as the documented module basename, substituting the actual npm manifest identity. Share typed contracts and mobile UI, inject API/session/navigation/storage adapters and keep app identifiers, signing, global providers and store configuration out of the library. Declare React/React Native as tested peers and Expo dependencies only for an Expo-specific adapter; never bundle a second runtime.

For a JS-only native package, use this public manifest shape alongside normal metadata/version/license:

```json
{
  "name": "@example/module-example-react-native",
  "version": "0.1.0",
  "type": "module",
  "main": "./lib/index.js",
  "types": "./lib/index.d.ts",
  "react-native": "./src/index.ts",
  "exports": {
    ".": {
      "types": "./lib/index.d.ts",
      "react-native": "./src/index.ts",
      "import": "./lib/index.js",
      "default": "./lib/index.js"
    }
  },
  "files": ["src", "lib", "README.md", "LICENSE", "CHANGELOG.md"]
}
```

Export `ExampleScreen` and its types in `src/index.ts`. Use the [React TypeScript build recipe](PACKAGES.md#2-react-library) with `outDir: lib`, React Native-compatible types, and the host-supported React version; change the clean script to remove `lib`. Metro consumes the shipped TS/TSX source while declarations and ESM are emitted for tooling. Test `.js` source import resolution with the selected Metro version; use the generator's native library setup if its resolution conventions differ. Ship referenced images/fonts and document their loading. Do not apply the web Vite build to native UI.

If native code is required, scaffold a library with its official tooling, register the platform code/config plugin and include required native sources, podspec/Gradle/codegen metadata in the artifact. Follow [React Native library guidance](https://reactnative.dev/docs/the-new-architecture/create-module-library); test supported architectures and native autolinking. A JS-only tarball cannot deliver an omitted native implementation.

Build, inspect `npm pack --dry-run`, create a tarball and install it in clean Expo/development-build and bare consumers if both are supported. Run Metro bundling **and** representative iOS/Android release builds, check peer resolution, assets, autolinking and declarations. Follow [npm publication](PACKAGES.md#6-publish-the-reviewed-tarball) after the device checks. An npm release distributes the library; it does not install a signed app on a phone.

## 8. Build and distribute the mobile app

For Expo, configure EAS with the approved account and CLI version:

```bash
npx eas-cli@latest login
npx eas-cli@latest build:configure
```

Commit `eas.json` with explicit development, preview/internal and production profiles, the chosen environment and production version strategy. Keep signing credentials in the approved credential store. Configure identifiers, app scheme, icons, permission descriptions, push credentials and store records before production. See [EAS build setup](https://docs.expo.dev/build/setup/).

```bash
npx eas-cli@latest build --platform android --profile production
npx eas-cli@latest build --platform ios --profile production
```

Pin the reviewed EAS CLI in CI instead of resolving `@latest` for every release. For local Expo development builds use `npx expo run:android` or `npx expo run:ios` with the native toolchains. Decide whether generated native projects are committed or generated reproducibly from config/plugins; do not hand-edit disposable prebuild output.

For bare projects, configure release signing using the selected RN template, produce the Android release app bundle through its Gradle wrapper (`./gradlew bundleRelease` inside `android` for the unflavored template), and archive/export iOS through Xcode with the correct team/provisioning. Use the platform-specific scripts if flavors/schemes change those defaults.

Install the actual signed artifacts on physical devices through internal testing/TestFlight. Verify cold start, login/refresh/logout, API environment, deep links, push, offline recovery and upgrades. Complete privacy disclosures, required SDK manifests, store metadata, screenshots, permission explanations and account-deletion obligations applicable to the app. Submit selected build IDs through EAS Submit or the store consoles; see [store submission](https://docs.expo.dev/deploy/submit-to-app-stores/).

Roll out gradually and monitor redacted crashes, startup failures and API errors. Keep API compatibility for installed older versions. OTA updates may change compatible JS/assets only within the configured runtime/update policy; native dependency or permission changes require a new binary. A rollback cannot remove an already-installed binary: use compatible server controls, a tested JS rollback when eligible, or a new signed store build.

## 9. Verification gates

Run clean locked installation, typecheck, the declared component/unit/contract tests, Expo doctor where applicable, and both platform release builds. Exercise denied/wrong-workspace calls, token expiry/revocation, offline/uncertain writes, app backgrounding/process death, storage migration, permission denial, accessibility and deep-link attacks. Record actual devices/OS versions and artifacts. A web build or simulator-only debug run does not establish mobile release readiness.

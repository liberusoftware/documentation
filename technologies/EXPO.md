# Expo build and publishing guide

Expo is the recommended React Native delivery workflow for Liberu mobile applications when its managed workflow, development builds, and native modules meet the product requirements. Expo Application Services (EAS) provides hosted builds, signing, internal distribution, store submission, and over-the-air JavaScript/assets updates.

## 1. Create or add Expo to an application

For a new client, use the current Expo starter and commit the generated lockfile:

```bash
npx create-expo-app@latest liberu-mobile --template default@sdk-57
cd liberu-mobile
npm install
npx expo start
```

For an existing React Native app, follow Expo's installation path and verify React Native/Expo SDK compatibility before adding native modules. Keep the mobile client as an API consumer; do not copy Laravel domain code or private models into it.

Official setup: [Create a project](https://docs.expo.dev/get-started/create-a-project/), [Expo tutorial](https://docs.expo.dev/tutorial/introduction/), and [using Expo libraries](https://docs.expo.dev/workflow/using-libraries/).

## 2. Configure identity and environments

Use stable Android application IDs and iOS bundle identifiers. Configure environment-specific API base URLs through app configuration and EAS environments; never put tokens, private keys, signing material, or server secrets in JavaScript bundles.

Example app configuration:

```json
{
  "expo": {
    "name": "Liberu Mobile",
    "slug": "liberu-mobile",
    "scheme": "liberu",
    "ios": { "bundleIdentifier": "com.example.liberu" },
    "android": { "package": "com.example.liberu" },
    "runtimeVersion": { "policy": "appVersion" }
  }
}
```

Initialize the EAS project and inspect the generated configuration:

```bash
npx eas-cli@latest login
eas init
eas build:configure
```

The exact SDK, Node.js, native dependency, and platform versions must remain pinned and verified in CI. See the local [React Native standard](../standards/REACT-NATIVE.md) and [mobile architecture](../architecture/MOBILE.md).

## 3. Use development builds

Expo Go is useful for early learning and simple previews. Use a development build when the app needs custom native modules, native configuration, push notifications, or production-like behavior.

Example eas.json:

```json
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal",
      "channel": "development"
    },
    "preview": {
      "distribution": "internal",
      "channel": "preview"
    },
    "production": {
      "autoIncrement": true,
      "channel": "production"
    }
  }
}
```

Build and install a development client:

```bash
eas build --profile development --platform android
eas build --profile development --platform ios
npx expo start --dev-client
```

Internal distribution builds are for controlled testers, not a replacement for store review. Test authentication, permissions, deep links, push notifications, offline behavior, accessibility, and API error states on representative devices.

See [development builds](https://docs.expo.dev/develop/development-builds/introduction/) and [EAS Build](https://docs.expo.dev/build/introduction/).

## 4. Build release binaries

Before a production build:

1. Confirm app identifiers, version, runtime version, API environment, privacy disclosures, permissions, icons, splash assets, and deep links.
2. Run linting, type checks, unit tests, API contract tests, accessibility checks, and device/integration tests.
3. Review native changes and determine whether an app-store build is required.
4. Confirm signing ownership and recovery procedures; EAS can manage credentials or use organization-controlled credentials.
5. Build from a clean, reviewed commit.

```bash
eas build --profile production --platform all
```

Use [EAS Build](https://docs.expo.dev/build/introduction/), [build configuration](https://docs.expo.dev/build/eas-json/), and [credentials](https://docs.expo.dev/app-signing/managed-credentials/) for the authoritative workflow. Store EXPO_TOKEN only in CI secret storage when automating builds.

## 5. Publish to app stores

Create the required Apple App Store Connect and Google Play records before submission. Confirm package identifiers, signing accounts, store metadata, privacy declarations, age/content ratings, screenshots, support URLs, and review notes.

Submit previously built binaries:

```bash
eas submit --platform android --profile production
eas submit --platform ios --profile production
```

Or connect a successful build to submission with an approved CI workflow. Store credentials in EAS or organization-managed secret storage, never in the repository.

Read [EAS Submit](https://docs.expo.dev/submit/introduction/), [submit to the app stores](https://docs.expo.dev/submit/android/), and [EAS build/submit/update tutorial](https://docs.expo.dev/tutorial/eas/introduction/).

## 6. Publish JavaScript and asset updates

EAS Update can deliver compatible JavaScript, styling, and assets without a new store submission. Configure it before the first production build:

```bash
npx expo install expo-updates
eas update:configure
eas update --channel preview --message "Preview release"
eas update --channel production --message "Fix login validation"
```

An update must target a compatible runtime and channel. Native code, native dependencies, permissions, app identifiers, and other binary changes require a new EAS Build and usually a store submission. Use staged channels, observe adoption and crashes, and keep a known-good update available for republishing if a release is faulty.

See [EAS Update](https://docs.expo.dev/eas-update/introduction/), [getting started](https://docs.expo.dev/eas-update/getting-started/), and [runtime versions](https://docs.expo.dev/eas-update/runtime-versions/).

## 7. CI/CD and release evidence

Automated workflows should:

- run from protected branches and reviewed tags;
- install dependencies from the lockfile and verify the Expo SDK;
- run tests, lint, type checking, and API contract validation;
- use short-lived or revocable CI tokens and least-privilege EAS access;
- build preview artifacts for review and production artifacts from an approved commit;
- record build IDs, runtime version, channel, commit SHA, changelog, and deployment evidence;
- monitor crash reports, failed updates, API compatibility, adoption, and rollback readiness.

For personal users, a local development build and manual store submission may be sufficient. SMEs should add preview distribution, protected secrets, device coverage, and restore/rollback procedures. Enterprise releases should add approval gates, managed identities, MDM distribution where needed, audit evidence, staged rollout, incident response, and formal separation between development, preview, and production.

Related Liberu documentation: [React Native technology](REACT-NATIVE.md), [React Native module index](../modules/react-native/README.md), [mobile architecture](../architecture/MOBILE.md), [mobile standards](../standards/MOBILE.md), [security architecture](../architecture/SECURITY.md), and [testing](../standards/TESTING.md).

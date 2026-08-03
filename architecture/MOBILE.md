# Mobile application architecture

## Purpose and boundary

React Native/Expo and Flutter are optional clients for Liberu APIs. The Laravel application and core Composer modules remain authoritative for domain rules, persistence, authorization, tenancy, consent, audit, and integration workflows.

```text
Mobile client (React Native/Expo or Flutter)
        |
        | versioned HTTPS API, auth, idempotency, telemetry
        v
API presentation package
        |
        v
Core module actions, queries, policies, events, jobs
        |
        v
Persistence and provider adapters
```

Mobile clients must not query private module tables, infer permissions from hidden controls, or implement a second tenant resolver. Platform-specific code belongs in the mobile adapter and must be replaceable without changing the core domain package.

## Client responsibilities

Mobile packages own navigation, screen composition, local view state, platform permissions, secure storage integration, push/deep-link handling, cache policy, offline queue UX, accessibility behavior, and release configuration. They consume OpenAPI schemas and public resource/action contracts and map server errors into platform-appropriate feedback.

## Offline and synchronization

Offline support is capability-specific. Before enabling it, document data classification, cache ownership, expiry, encryption/wipe policy, mutation idempotency keys, retry/backoff, conflict resolution, server reconciliation, and user-visible pending state. A client cache is never an authorization source and must be invalidated after logout, account disablement, permission loss, or tenant change.

## Security and privacy

Use short-lived credentials, platform secure storage, least-privilege scopes, certificate/transport protections appropriate to the threat model, redacted crash/analytics payloads, and explicit revocation. Treat push notifications, deep links, files, clipboard contents, sensors, device identifiers, and all API responses as untrusted. High-risk actions require server-side recent authentication and policy checks.

## Release architecture

Maintain a support matrix for iOS, Android, device classes, OS versions, API versions, and native dependencies. Use signed reproducible builds, environment-specific configuration, staged rollout, crash/error monitoring with consent, feature kill switches, store compliance evidence, and rollback procedures. Enterprise profiles may add SSO, MDM, managed distribution, stronger device policy, and audit; personal/SME profiles should remain operable without that infrastructure.

## Verification

Test core contracts independently, then test API authorization and schemas, client state transitions, navigation/deep links, permission denial, offline/retry/conflict behavior, accessibility, localization, app lifecycle, upgrade/migration, and release artifacts on supported platforms.

Related documents: [API architecture](API.md), [security](SECURITY.md), [tenancy](TENANCY.md), [modules](MODULES.md), [mobile standard](../standards/MOBILE.md), [React Native standard](../standards/REACT-NATIVE.md), [Flutter standard](../standards/FLUTTER.md), and [mobile module index](../modules/mobile/README.md).

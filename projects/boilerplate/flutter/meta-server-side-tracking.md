# Meta Server-Side Tracking domain packages Flutter + Dart

**Package:** module-meta-server-side-tracking-flutter
**Matching core package:** module-meta-server-side-tracking ([implementation](../core/meta-server-side-tracking.md))
**Matching API package:** module-meta-server-side-tracking-api ([contract](../api/meta-server-side-tracking.md))

## Implementation plan

This adapter presents Meta Server-Side Tracking domain packages for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Meta Server-Side Tracking domain packages API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/meta-server-side-tracking.md), and [API module](../api/meta-server-side-tracking.md).

# Product And Service Items Flutter + Dart

**Package:** module-accounting-product-and-service-items-flutter
**Matching core package:** module-accounting-product-and-service-items ([implementation](../core/product-and-service-items.md))
**Matching API package:** module-accounting-product-and-service-items-api ([contract](../api/product-and-service-items.md))

## Implementation plan

This adapter presents Product And Service Items for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Product And Service Items API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/product-and-service-items.md), and [API module](../api/product-and-service-items.md).

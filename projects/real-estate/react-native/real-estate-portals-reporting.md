# Real Estate Portals Reporting React Native + Expo

**Package:** module-real-estate-real-estate-portals-reporting-react-native
**Matching core package:** module-real-estate-real-estate-portals-reporting ([implementation](../core/real-estate-portals-reporting.md))
**Matching API package:** module-real-estate-real-estate-portals-reporting-api ([contract](../api/real-estate-portals-reporting.md))

## Implementation plan

This adapter presents Real Estate Portals Reporting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Portals Reporting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/real-estate-portals-reporting.md), and [API module](../api/real-estate-portals-reporting.md).

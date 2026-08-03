# Sales Tax And Gst React Native + Expo

**Package:** module-accounting-sales-tax-and-gst-react-native
**Matching core package:** module-accounting-sales-tax-and-gst ([implementation](../core/sales-tax-and-gst.md))
**Matching API package:** module-accounting-sales-tax-and-gst-api ([contract](../api/sales-tax-and-gst.md))

## Implementation plan

This adapter presents Sales Tax And Gst for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Sales Tax And Gst API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/sales-tax-and-gst.md), and [API module](../api/sales-tax-and-gst.md).

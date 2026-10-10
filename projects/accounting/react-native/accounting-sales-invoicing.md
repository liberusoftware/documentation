# Accounting Sales Invoicing React Native + Expo

**Package:** module-accounting-accounting-sales-invoicing-react-native
**Matching core package:** module-accounting-accounting-sales-invoicing ([implementation](../core/accounting-sales-invoicing.md))
**Matching API package:** module-accounting-accounting-sales-invoicing-api ([contract](../api/accounting-sales-invoicing.md))

## Implementation plan

This adapter presents Accounting Sales Invoicing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Sales Invoicing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-sales-invoicing.md), and [API module](../api/accounting-sales-invoicing.md).

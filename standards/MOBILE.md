# Mobile application standard

This standard applies to React Native, Expo, Flutter, and any future mobile adapter.

## Product and UX

Mobile screens must remain useful on small displays, intermittent networks, touch input, keyboard/switch access, device rotation, dynamic text, localization, and platform back behavior. Every async flow needs loading, empty, validation, unauthorized, offline, conflict, failure, retry, and recovery states.

## Security and privacy

Use least-privilege API scopes, secure credential storage, certificate/transport protections appropriate to the threat model, redacted diagnostics, device lock assumptions, and explicit logout/revocation behavior. Do not trust device identity, push payloads, deep links, local caches, or client-side feature flags as authorization.

## Data and offline behavior

Cache only classified data with an owner, expiry, invalidation rule, and deletion behavior. Offline writes use an idempotency key, visible pending state, retry policy, conflict policy, and server reconciliation. Sensitive data must have a documented local-retention and wipe strategy.

## Delivery

Maintain a device/OS compatibility matrix, signed reproducible builds, environment-specific configuration, crash/error telemetry with consent and redaction, staged rollout, rollback/kill-switch procedures, and store compliance evidence. Keep personal/SME profiles operationally simple while allowing enterprise profiles to add SSO, MDM, stronger policy, and audit requirements.

See [mobile architecture](../architecture/MOBILE.md), [accessibility](../technologies/ACCESSIBILITY.md), [testing](../technologies/TESTING.md), [React Native](REACT-NATIVE.md), and [Flutter](FLUTTER.md).

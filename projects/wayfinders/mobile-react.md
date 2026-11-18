# Wayfinder technical specification: React Native Expo

This is the technology-specific implementation specification for `mobile-react` project hosts. Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.

- Boilerplate template: https://github.com/liberusoftware/project-boilerplate-mobile-react
- Reusable module foundation: https://github.com/liberusoftware/module-boilerplate-react-native
- Capability skeleton catalog: [`modules/skeletons/mobile-react.md`](../../modules/skeletons/mobile-react.md)
- Presentation layer directory in product docs: `react-native/`
- Adapter identity pattern: `module-{capability}-react-native`
- Consumes product `-laravel-api`: yes

## Delivery boundary

Consume the product `-laravel-api` with typed clients, secure device credentials, validated deep links, native accessibility, foreground refresh and explicit offline/reconnect behavior.

## Authoritative documentation

- [React Native standard](../../standards/REACT-NATIVE.md)
- [Mobile architecture](../../architecture/MOBILE.md)
- [Mobile standard](../../standards/MOBILE.md)
- [Laravel API backends](../../guides/LARAVEL-API-BACKENDS.md)
- [Foundation and presentation build](../../guides/presentation/README.md)
- [React Native / Expo implementation runbook](../../guides/presentation/REACT-NATIVE.md)
- [Module index](../../modules/react-native/README.md)
- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)
- [Testing / coverage policy](../../standards/TESTING.md)

## Robust implementation method

1. Start from the React Native Expo Boilerplate; install with the Expo-compatible toolchain; run `expo-doctor`, typecheck and a development build—do not assume Expo Go covers every native module.
2. Record supported iOS/Android versions, orientations and accessibility requirements; configure bundle IDs, scheme, icons and permissions for this product host.
3. Point the app at the matching `project-{product}-laravel-api` base URL (public config only); implement the reviewed mobile auth contract (PKCE/OAuth or first-party tokens)—never embed confidential secrets.
4. Store refresh/session secrets in Keychain/Keystore-backed SecureStore; keep short-lived access tokens in memory where feasible; single-flight refresh; logout revokes and clears scoped caches/queues.
5. Inject typed API clients per session/workspace; validate every response field; map status codes to typed outcomes; abort in-flight work on context change.
6. Build native screens (not compressed desktop tables): safe areas, touch targets, screen-reader labels, platform back behavior, deep-link validation.
7. Define explicit offline/queue/reconciliation rules before enabling draft writes; never present a local draft as an authoritative completed server transaction.
8. Deliver one vertical journey end-to-end on simulator and at least one physical-platform path; then expand via `react-native/` plans and SOURCE-MAPPING.md.
9. Prove evidence: auth lifecycle, 401 refresh bounds, tenant denial, connectivity loss/resume, signed build pipeline notes and clean lockfile installs.

## Technical specification

### Host ownership
- This repository is a native iOS/Android client (React Native + Expo). It consumes HTTP APIs; it does not run Laravel or own domain tables.
- Application owns navigation, session providers, secure storage adapters, native permissions and store release configuration.
- Reusable adapters supply screens/hooks/DTO mapping for a capability without importing Next.js, DOM or Inertia.

### Transport and session
- Fixed API base URL per environment; HTTPS in production; reachable host for device/emulator networking.
- Use the API’s mobile identity contract; Authorization Code + PKCE for public OAuth clients when applicable.
- Bound timeouts, cancellation and retry; preserve idempotency keys for commands that require them.

### Package and directory contracts
- Prefer `module-{capability}-react-native` (or the layer’s documented identity) with Metro-compatible exports.
- Keep session/transport/cache as app-injected dependencies; avoid singletons that retain a previous user’s token.
- `EXPO_PUBLIC_*` values are embedded public configuration—never secrets.

### Security and tenancy
- Server remains authoritative for authorization and tenancy; hide unavailable actions for UX only.
- Deep links must be validated (signed routes/state) before acting on them.
- Scoped local caches must clear on logout and workspace/permission changes.

### Verification and release
- Verify on both OS families where the product supports them; record signed build/store evidence separately from unit tests.
- Monitor token refresh failures, crash-free sessions and API error rates after release.

## Related

- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)
- [Issue matrix](../IMPLEMENTATION-ISSUES.md)
- [Repository map](../REPOSITORIES.md)

# JavaScript presentation testing standard

Every React, Vue, Nuxt, Inertia, React Native, Expo, and Vite presentation package must have tests appropriate to its public behavior. Presentation tests complement, and never replace, core module, API, policy, tenancy, security, and persistence tests.

## Required evidence

- Unit tests cover pure formatters, hooks, composables, reducers, state machines, and error mapping.
- Component tests assert accessible roles/names, user interactions, validation, loading, empty, denied, queued, failure, retry, and recovery states.
- Contract tests verify API paths, methods, headers, schemas, pagination, idempotency, field visibility, and RFC 9457 error mapping.
- Browser or device tests cover critical authenticated journeys, navigation, deep links, lifecycle interruption, and responsive/platform behavior.
- Accessibility tests cover keyboard/focus behavior for web and semantic labels, announcements, dynamic type, contrast, and screen-reader behavior for mobile.
- Production build tests verify environment configuration, asset loading, source-map policy, bundle errors, and supported browser/device targets.

## Boundaries and safety

Mock only at an explicit boundary. Do not mock away authorization, tenant context, server validation, or core actions. Never put real credentials, personal data, provider secrets, or production endpoints in fixtures. Keep asynchronous tests deterministic with controlled clocks, abort signals, retries, and network responses.

## Quality gates

Run formatting, linting, type checking, unit/component tests, API contract validation, accessibility checks, and the critical browser/device suite in CI. A failed test must identify the user-visible behavior, contract, or platform assumption that regressed. Pin browser/device matrices and record flaky-test ownership and remediation dates.

See [FRONTEND-TESTING.md](../technologies/FRONTEND-TESTING.md), [testing standard](TESTING.md), [React](REACT.md), [Vue](VUE.md), [Nuxt](NUXT.md), [Inertia](INERTIA.md), [React Native](REACT-NATIVE.md), [mobile](MOBILE.md), and [CI](CI.md).

# JavaScript presentation testing guide

This guide covers the JavaScript-based presentation layers used by Liberu: React/Inertia, Vue/Inertia, Nuxt, React Native/Expo, and Vite-powered shared components. Tests prove the presentation contract and user experience; core domain behavior remains tested by the owning Laravel module.

## Testing layers

| Layer           | Recommended focus                                                     | Typical tools                                              |
| --------------- | --------------------------------------------------------------------- | ---------------------------------------------------------- |
| Pure logic      | Formatters, reducers, composables, hooks, state transitions           | Vitest                                                     |
| Component       | Roles, labels, props, events, validation, loading/error/empty states  | Testing Library, React Native Testing Library              |
| API contract    | Request mapping, schemas, auth/tenant denial, error envelopes         | Laravel/Pest feature tests, MSW, OpenAPI validation        |
| Browser journey | Navigation, forms, authentication, responsive behavior, accessibility | Playwright                                                 |
| Mobile journey  | Deep links, permissions, lifecycle, offline/retry, native builds      | Expo development builds, device/emulator integration tests |
| Accessibility   | Keyboard/focus, screen readers, semantics, contrast, announcements    | axe-core, platform accessibility inspectors                |

## Example component test

```tsx
import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { EmptyState } from "./EmptyState";

describe("EmptyState", () => {
  it("exposes a useful heading and action", () => {
    render(
      <EmptyState heading="No records" action={<button>Try again</button>} />,
    );

    expect(screen.getByRole("heading", { name: "No records" })).toBeVisible();
    expect(screen.getByRole("button", { name: "Try again" })).toBeEnabled();
  });
});
```

## Contract and failure testing

Do not test only successful rendering. Cover unauthorized and wrong-tenant responses, validation errors, rate limits, stale data, request cancellation, queued operations, conflict responses, offline recovery, retries, duplicate submissions, and partial API failure. Assert the user-visible result and the request contract without coupling tests to private Laravel tables or implementation details.

Use fixture factories or typed builders for representative API payloads. Validate fixtures against the released schema, include sensitive-field omission cases, and keep dates, currencies, locales, permissions, and feature flags explicit. Mock external providers at the adapter boundary, not the core domain boundary.

## Layer-specific guidance

- React/Inertia: test page props, forms, navigation, preserved state, server validation, and authorization outcomes; use Laravel feature tests for server responses.
- Vue/Inertia: test composables, emitted events, page props, form state, focus management, and error mapping; keep business rules server-side.
- Nuxt: test SSR/client boundaries, route middleware, server routes, runtime configuration, hydration, caching, and public/private data separation.
- React Native/Expo: test native permission denial, deep links, secure-storage failures, app background/foreground transitions, offline queues, and development/release builds.
- Vite/shared UI: test package exports, production builds, CSS tokens, browser support, and tree-shaking of optional features.

Official references: [Vitest](https://vitest.dev/guide/), [Testing Library](https://testing-library.com/docs/), [React Native Testing Library](https://callstack.github.io/react-native-testing-library/), [Playwright](https://playwright.dev/docs/intro), [Nuxt testing](https://nuxt.com/docs/4.x/getting-started/testing), [axe-core](https://github.com/dequelabs/axe-core), and [Expo development builds](https://docs.expo.dev/develop/development-builds/introduction/).

Related Liberu documentation: [testing technology](TESTING.md), [frontend testing standard](../standards/FRONTEND-TESTING.md), [testing standard](../standards/TESTING.md), [API architecture](../architecture/API.md), [mobile architecture](../architecture/MOBILE.md), and [themes](../standards/THEMES.md).

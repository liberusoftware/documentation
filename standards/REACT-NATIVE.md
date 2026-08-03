# React Native and Expo standard

## Boundary

React Native packages are optional presentation clients. They consume the matching API/core contracts and never contain authoritative domain rules, Laravel model access, tenant resolution, or permission decisions.

## Implementation requirements

- Use TypeScript strict mode, typed navigation, schema-validated API responses, and explicit nullable/loading/error states.
- Prefer Expo when its managed or development-build workflow satisfies the product; document native modules, config plugins, build profiles, and platform exceptions.
- Keep access and refresh credentials in Keychain/Keystore-backed storage or an approved equivalent; never use local storage for long-lived secrets.
- Treat deep links, push payloads, clipboard data, files, sensors, and native responses as untrusted input.
- Make network writes idempotent and recoverable; show queued/offline/conflict states rather than silently dropping work.
- Build accessible native controls with labels, hints, focus order, dynamic type, contrast, reduced motion, and screen-reader announcements.
- Test unit logic, hooks, API contracts, navigation, permissions, offline recovery, accessibility, and representative iOS/Android release builds.

```tsx
const response = await fetch(apiBaseUrl + "/api/v1/records", {
  headers: { Accept: "application/json", Authorization: "Bearer " + token },
});
if (!response.ok) throw new Error("Unable to load records");
```

Review [MOBILE.md](MOBILE.md), [security architecture](../architecture/SECURITY.md), [API architecture](../architecture/API.md), [React Native technology reference](../technologies/REACT-NATIVE.md), and [Expo documentation](https://docs.expo.dev/).

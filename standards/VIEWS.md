# Views standard

Views render explicit, authorized data and provide accessible presentation. They do not query private tables or implement domain mutations.

- Pass typed/purpose-built view models or explicit props; do not depend on ambient database state.
- Cover loading, empty, error, unauthorized, offline, validation, and success states where the surface can encounter them.
- Escape output by default, sanitize approved rich content through a shared service, and localize all user-facing copy.
- Keep layout regions, slots, test IDs, semantic landmarks, focus behavior, and extension points stable.
- For client adapters, follow [React](REACT.md), [Vue](VUE.md), [Nuxt](NUXT.md), or [INERTIA.md](INERTIA.md).

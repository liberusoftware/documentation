# Vue 3 standard

Liberu targets Vue 3 with TypeScript and Vite. For Laravel-driven pages use Inertia 3; for independently SSR-rendered/API-consuming applications use Nuxt 4. The [Vue 3 documentation](https://vuejs.org/guide/introduction.html) and [Vue GitHub repository](https://github.com/vuejs/core) are authoritative for framework behavior.

## Rules

- Use `<script setup lang="ts">`, typed props/emits, focused SFCs, composables, and explicit package exports.
- Keep page routing and server authorization in Laravel when using Inertia; use Nuxt routing/runtime conventions in Nuxt applications.
- Avoid hydration mismatches, browser-only APIs during SSR, global mutable state, and duplicated domain validation.
- Handle loading, empty, stale, error, unauthorized, forbidden, offline, and success states accessibly.
- Use semantic HTML, keyboard operation, focus management, localization, RTL, reduced motion, and automated accessibility checks.

See [INERTIA.md](INERTIA.md), [NUXT.md](NUXT.md), [TypeScript](../technologies/TYPESCRIPT.md), and [Vue style guide](https://vuejs.org/style-guide/).

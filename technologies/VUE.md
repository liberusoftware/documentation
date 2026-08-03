# Vue 3 technology reference

Vue 3 is used for typed, component-based interfaces, generally with Inertia 3 for Laravel-driven applications. Keep domain behavior and authorization on the server and use composables for reusable presentation behavior.

## Component example

```vue
<script setup lang="ts">
defineProps<{ heading: string }>();
</script>

<template>
  <section aria-labelledby="empty-heading">
    <h2 id="empty-heading">{{ heading }}</h2>
  </section>
</template>
```

Use strict TypeScript, accessible semantic elements, explicit async states, validated forms, and safe rendering. Keep API/page contracts versioned and avoid embedding credentials in browser code.

Official references: [Vue quick start](https://vuejs.org/guide/quick-start.html), [Vue guide](https://vuejs.org/guide/introduction.html), [Vue TypeScript guide](https://vuejs.org/guide/typescript/overview.html), and [Vue GitHub](https://github.com/vuejs/core). Related local guides: [Vue standard](../standards/VUE.md), [Inertia](INERTIA.md), and [Vue module index](../modules/vue/README.md).

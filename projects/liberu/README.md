# Liberu project index

This is the navigation index for the Liberu platform project. Start with the [Liberu business platform scope](../LIBERU.md) for business ownership and composition rules, then choose the domain, API, presentation, mobile, or implementation index required for the work.

## Project scope

- [LIBERU.md](../LIBERU.md) — canonical business platform scope, package composition, workflows, milestones, and acceptance.
- [End-user guide](../../user-guides/projects/liberu/README.md) — what customers, staff, and mobile users experience.
- [Official websites and staff apps implementation](implementation/README.md) — build sequence and composition rules.

## Domain and contract indexes

| Surface | Index | Purpose |
| --- | --- | --- |
| Features | [features/README.md](features/README.md) | Liberu-specific cross-product feature contracts |
| Core | [core/README.md](core/README.md) | Reusable Liberu domain packages |
| API | [api/README.md](api/README.md) | Versioned HTTP/API adapters |
| Implementation | [implementation/README.md](implementation/README.md) | Official website and staff-app composition |
| Custom modules | [implementation/custom-modules/README.md](implementation/custom-modules/README.md) | Narrow Liberu-owned composition modules |

## Presentation indexes

| Surface | Index | Package role |
| --- | --- | --- |
| Filament | [filament/README.md](filament/README.md) | Administrative and operational panels |
| Livewire | [livewire/README.md](livewire/README.md) | Server-driven staff workflows |
| React + Inertia | [react/README.md](react/README.md) | React web application adapters |
| Vue + Inertia | [vue/README.md](vue/README.md) | Vue web application adapters |
| Nuxt | [nuxt/README.md](nuxt/README.md) | Public/SSR website adapters |
| React Native + Expo | [react-native/README.md](react-native/README.md) | Staff mobile adapters |
| Flutter + Dart | [flutter/README.md](flutter/README.md) | Staff mobile adapters |

## Build navigation

1. Confirm ownership and required dependencies in [DEPENDENCIES.md](implementation/DEPENDENCIES.md).
2. Select existing Liberu modules and review the [custom module index](implementation/CUSTOM-MODULES.md).
3. Build the first `liberuhosting.com` vertical slice using [OFFICIAL-WEBSITES.md](implementation/OFFICIAL-WEBSITES.md).
4. Add staff workflows and device behavior from [STAFF-MOBILE.md](implementation/STAFF-MOBILE.md).
5. Use [DELIVERY-CHECKLIST.md](implementation/DELIVERY-CHECKLIST.md) for tests, runbooks, documentation, and release evidence.

Every directory in this project has its own README index. Module files are linked from the matching index and must not be discovered by convention alone.

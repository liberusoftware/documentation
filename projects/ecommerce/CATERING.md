# Catering delivery map

Start with [feature scope](features/catering.md), [core and boundary decisions](core/catering.md), then [API](api/catering.md). These are planning specifications, not evidence of released endpoints. One domain owner serves all presentations; mobile and desktop clients never fork catering rules.

## Presentation plans

- [Filament](filament/catering.md)
- [Livewire](livewire/catering.md)
- [Laravel Inertia React](react/catering.md)
- [Laravel Inertia Vue](vue/catering.md)
- [Nuxt Vue](nuxt/catering.md)
- [Next.js React](nextjs/catering.md)
- [React Native Expo](react-native/catering.md)
- [Flutter mobile](flutter/catering.md)
- [Dart mobile](dart-mobile/catering.md)
- [Dart desktop](dart-desktop/catering.md)

## Implementation sequence

1. Approve the catalogue owner, dependencies and quote/booking/order transition decisions recorded in core.
2. Verify existing public contracts and version constraints; document the dependency ADR and privacy projections.
3. Implement and test the domain, snapshots, concurrency and recoverable conversion.
4. Publish/test the OpenAPI fragment and generated client contracts where HTTP is used.
5. Deliver each selected surface against the shared contracts, with tenant/privacy, accessibility, conflict and retry evidence.
6. Validate host composition, upgrade/runbook, locked install and committed `/modules` and `/themes` copies.

Use the [project wayfinders](../IMPLEMENTATION-WAYFINDERS.md) for repository tracking. The existing Filament programme has a separate [Catering epic and core/API/Filament/Livewire issue register](catering-filament-issues.json), linked from its existing wayfinder. Other Filament implementation issues remain outside this addition.

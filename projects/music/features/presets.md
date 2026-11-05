# Liberu Music: Presets, Racks and Templates — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Versioned instrument/effect presets, device racks, macros and reusable session templates.

**Required journey:** Save a rack with macro mappings, share it and preview migration before loading.

**Invariant:** Preset loading validates schema and dependencies before changing the active graph.

**Dependencies:** projects, media-library. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test version migration, unavailable devices and safe restoration after failed load. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/presets.md), [API plan](../api/presets.md) and [surface support](../PRESENTATION.md).

# Liberu Music: Instruments and Samplers — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Built-in synth, drum machine, sampler, multisamples, voice allocation and portable instrument presets.

**Required journey:** Load a sampler, map zones, record a part and freeze the result.

**Invariant:** Voice limits are bounded and missing samples produce explicit recoverable state.

**Dependencies:** audio-engine, media-library, presets. Dependencies use public contracts rather than private tables or models.

## Acceptance

Test voice stealing, sustained notes, missing samples and deterministic seeded patches. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/instruments.md), [API plan](../api/instruments.md) and [surface support](../PRESENTATION.md).

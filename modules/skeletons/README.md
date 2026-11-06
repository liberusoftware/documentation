# Capability module repositories

Applications use `project-`; independent reusable packages use `module-`. This catalog maps 631 documented capability/source groups across the nine requested presentations. Documented aliases share their canonical capability home; distinct source identities and naming conflicts remain explicit instead of being silently merged. Music contributes 22 capability groups in addition to the 609 groups recorded by the Next.js ownership inventory.

The complete matrix contains **5,679 module repository slots**. Of these, 567 were existing repositories and 5,112 require new skeletons. A repository link appears only after remote publication or an existing-source check; queued names remain plain text. New skeletons contain package structure and registration/extension entries, not completed business features or published registry releases.

| Presentation | Catalog | Published skeletons | Verified existing source | Other slots |
| --- | --- | ---: | ---: | ---: |
| Laravel · Filament | [631 capabilities](laravel-filament.md) | 131 | 443 | 57 |
| Laravel · Inertia · Vue | [631 capabilities](laravel-inertia-vue.md) | 130 | 0 | 501 |
| Laravel · Inertia · React | [631 capabilities](laravel-inertia-react.md) | 130 | 0 | 501 |
| Nuxt · Vue | [631 capabilities](nuxt-vue.md) | 130 | 0 | 501 |
| Next.js · React | [631 capabilities](next-react.md) | 130 | 0 | 501 |
| React Native · Expo | [631 capabilities](mobile-react.md) | 130 | 0 | 501 |
| Flutter · Mobile | [631 capabilities](mobile-flutter.md) | 129 | 0 | 502 |
| Dart · Desktop | [631 capabilities](dart-desktop.md) | 128 | 0 | 503 |
| Dart · Mobile | [631 capabilities](dart-mobile.md) | 128 | 0 | 503 |

## Use and verify

Start a capability package from its matching [module foundation](../../projects/REPOSITORIES.md#reusable-module-foundations). Follow the package README, `AGENTS.md`, public owner contracts and the layer runbook. PHP packages use Composer; JavaScript/TypeScript libraries use npm; Dart/Flutter packages use pub metadata. Keep application navigation, session integration, platform identity and deployment outside reusable capability code.

Each new package records its exact source/plan key and foundation commit in `module-skeleton.json`. Type/source checks and clean-consumer template checks cover the package setup; they do not establish authorization behavior, API compatibility, physical-device behavior or signed releases. Existing source repositories retain their implementations and actual package identities. Recheck current manifests and releases before adoption.

The [machine-readable snapshot](../../architecture/module-skeleton-repositories.json) records the same matrix and verified publication state. Catalog states are snapshots; they are updated as the requested repository rollout proceeds.

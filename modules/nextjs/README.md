# Next.js presentation module plans

Optional API-consuming React adapters cover **1420 documented module spellings** in **16 scopes**. The [ownership registry](OWNERSHIP.md) consolidates them into **645 plan groups** using observed core identities where established. These are target plans, not published packages.

Use the [Next.js standard](../../standards/NEXTJS.md) for server/client boundaries, sessions, authorization, caching and deployment, and the [npm lifecycle guide](../../guides/NPM.md) for development and release. Framework-independent React UI can be shared with Inertia; routing, forms and transport require distinct adapters.

| Project | Documented module spellings |
| --- | ---: |
| [accounting](../../projects/accounting/nextjs/README.md) | 241 |
| [automation](../../projects/automation/nextjs/README.md) | 57 |
| [billing](../../projects/billing/nextjs/README.md) | 82 |
| [boilerplate](../../projects/boilerplate/nextjs/README.md) | 55 |
| [browser-game](../../projects/browser-game/nextjs/README.md) | 61 |
| [cms](../../projects/cms/nextjs/README.md) | 249 |
| [control-panel](../../projects/control-panel/nextjs/README.md) | 61 |
| [crm](../../projects/crm/nextjs/README.md) | 218 |
| [ecommerce](../../projects/ecommerce/nextjs/README.md) | 108 |
| [genealogy](../../projects/genealogy/nextjs/README.md) | 62 |
| [liberu](../../projects/liberu/nextjs/README.md) | 4 |
| [maintenance](../../projects/maintenance/nextjs/README.md) | 60 |
| [music](../../projects/music/nextjs/README.md) | 22 |
| [real-estate](../../projects/real-estate/nextjs/README.md) | 65 |
| [sap](../../projects/sap/nextjs/README.md) | 16 |
| [social-network](../../projects/social-network/nextjs/README.md) | 59 |

## Build the application and adapter

Follow the [implementation runbook](../../guides/presentation/NEXTJS.md) for a skeleton, concrete integration steps, package builds and releases. Begin with the [shared architecture/foundation setup](../../guides/presentation/README.md); the module plans above do not imply registry availability.

# Browser Game: Social Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-social-filament`  
**Matching domain module:** `browser-game-social`  
**Application:** Browser Game  
**Source feature:** [Social](../features/social.md)  
**Architecture:** [FILAMENT.md](../BROWSER-GAME.md) · [MODULES.md](../BROWSER-GAME.md) · [TESTING.md](../BROWSER-GAME.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-social` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Friends:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Parties:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Chat:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mail:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Guilds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alliances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Permissions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Activity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-social-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `friends`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `parties`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `chat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mail`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `guilds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alliances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `permissions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `activity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-social` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

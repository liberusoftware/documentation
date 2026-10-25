# Liberu: design and source reconciliation

This map connects existing design filenames to observed package identities. Matching is based on exact/local naming patterns plus the documented foundation aliases below; it is navigation evidence, not proof of equivalent behavior or complete implementation. Read the source reference before using a proposed field, endpoint, permission or installation example.

**Preservation rule:** all existing product scopes and module documents remain in place. A blank package match means only that this scan did not find a dedicated manifest under the expected naming pattern; implementation can exist elsewhere or use another identity.

No corresponding application repository was included in the requested `liberusoftware/*-laravel` discovery set. Use the enterprise/platform composition documents and owning product sources rather than inventing a source package.

Existing platform code is present in other application trees. The [cross-project reuse guide](REUSE.md) records the two identity families, namespaces and tables; a missing direct application match here must not be interpreted as no implementation or a need for a third owner.

## Read the mapping

Core/API/Filament/Livewire columns show dedicated observed identities where names match. JavaScript/mobile source matches are recorded in the JSON index and individual annotations when present. An adapter can also be application-owned or ship assets through a PHP package; absence of a dedicated npm manifest does not establish absence of UI.

Multiple matches are left visible for review. Repeated design spellings may point to the same package; they must not become independent competing owners. Installation uses the observed manifest name, not a generated design slug.

| Design scope | Core source reference | API source reference | Filament source reference | Livewire source reference |
| --- | --- | --- | --- | --- |
| <a id="business-workflow-reconciliation"></a>[business-workflow-reconciliation](features/business-workflow-reconciliation.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="executive-insights"></a>[executive-insights](features/executive-insights.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="platform-orchestration"></a>[platform-orchestration](features/platform-orchestration.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="revenue-and-care-orchestration"></a>[revenue-and-care-orchestration](features/revenue-and-care-orchestration.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |

## Observed packages without a design-name match

These package references document observed modules even when an existing feature filename did not match. Review their capabilities, call sites and ownership before deciding whether to extend an existing feature or add a distinct product capability. They are not silently omitted or merged by this tool.

| Actual directory | Manifest identity and implementation reference |
| --- | --- |
| — | No unmatched dedicated package identities in this scan |

Reproduce with `python3 tools/reconcile_source_modules.py` after rebuilding the inventory and package references. The [machine-readable mapping](../../architecture/source-design-mapping.json) includes every layer match. Follow the [reuse guide](../../architecture/SHARED-MODULES.md), [Composer lifecycle](../../guides/COMPOSER.md) and [npm lifecycle](../../guides/NPM.md) when implementing or adopting a module.

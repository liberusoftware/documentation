#!/usr/bin/env python3
"""Clarify Inertia page transport separately from domain/API contracts."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
START='<!-- inertia-transport:start -->';END='<!-- inertia-transport:end -->'
TEXT='''### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
'''


def main():
    count=0
    for project in sorted((ROOT/'projects').iterdir()):
        if project.name=='sap':continue # Domain-specific authored plans already describe this boundary.
        for layer in ('react','vue'):
            for path in (project/layer).glob('*.md'):
                if path.name=='README.md':continue
                original=path.read_text()
                updated=original.replace('presentation package presents exactly one matching API module.','presentation package adapts the matching domain contract through Laravel-owned Inertia routes.')
                updated=updated.replace('to the matching public API boundary.','to the matching public application/API boundary.')
                block=START+'\n'+TEXT+END
                if START in updated:updated=re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:block,updated,flags=re.S)
                elif '## 4. API contract and Inertia consumption' in updated:
                    updated=updated.replace('## 4. API contract and Inertia consumption\n','## 4. API contract and Inertia consumption\n\n'+block+'\n',1)
                else:updated+='\n'+block+'\n'
                # An older categorical API-only instruction conflicts with the clarified local public boundary.
                updated=updated.replace('- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.','- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.')
                if updated!=original:path.write_text(updated);count+=1
    print(f'Clarified Inertia transport in {count} React/Vue module plans.')


if __name__=='__main__':main()

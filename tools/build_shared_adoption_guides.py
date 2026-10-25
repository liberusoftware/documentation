#!/usr/bin/env python3
"""Document divergent shared-package variants and data-preserving adoption decisions."""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

from build_source_reference import methods,safe

ROOT=Path(__file__).resolve().parents[1]


def source(observation,path,label=None):
    url=f'https://github.com/liberusoftware/{observation["repository"]}/blob/{observation["commit"]}/modules/{observation["directory"]}/{path}'
    return f'[{safe(label or path)}]({url})'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects',type=Path,default=Path('/tmp/liberu-documentation-sources'))
    args=parser.parse_args()
    comparisons=json.loads((ROOT/'architecture/shared-module-comparison.json').read_text())['comparisons']
    divergent=[c for c in comparisons if c['runtime_variants']>1 or c['metadata_variants']>1]
    output=ROOT/'architecture/shared-adoption';output.mkdir(exist_ok=True)
    for comparison in divergent:
        identity=comparison['identity'];tail=identity.split('/')[-1]
        owner='liberu' if tail.startswith(('module-liberu-','liberu-')) else 'billing' if tail.startswith(('module-billing-','billing-')) else 'boilerplate'
        variants=defaultdict(list)
        for observation in comparison['observations']:
            repo=args.projects/observation['repository']
            actual=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
            dirty=subprocess.check_output(['git','-C',str(repo),'status','--porcelain'],text=True).strip()
            if actual!=observation['commit'] or dirty:raise SystemExit(f'{repo}: source differs from the pinned clean comparison')
            variants[(observation['runtime_digest'],observation['metadata_digest'])].append(observation)
        numbered={key:i+1 for i,key in enumerate(sorted(variants))}
        page=output/(identity.replace('/','--')+'.md')
        lines=[f'# {identity}: shared adoption review','',
               '**Status:** source-backed consolidation design, not a completed migration or stability certification. This profile records differences at the pinned commits and a data-preserving adoption path. Active source projects are unchanged by this documentation review.','',
               '## Ownership and decision','',
               f'The documentation owner is the [{owner} capability scope](../../projects/{owner}/README.md). Keep one authoritative capability/release boundary and product-specific behavior behind reviewed extensions. This is a documentation ownership decision; select the actual package maintainer/canonical release repository from verified package governance before changing consumers.','',
               f'Runtime variants: **{comparison["runtime_variants"]}**; selected metadata variants: **{comparison["metadata_variants"]}** under this exact manifest identity. Equal names/constraints do not make different schemas or providers interchangeable. Keep the installed identity and its data until a compatible release or explicit migration is reviewed.','',
               'See the [implementation reference](../../modules/source/'+identity.replace('/','--')+'.md), [source comparison](../SHARED-MODULE-COMPARISON.md) and [consolidation procedure](../SHARED-MODULES.md).','',
               '## Consumer variants','', '| Consumer | Pinned module metadata | Variant | Test files |','| --- | --- | ---: | ---: |']
        for o in comparison['observations']:
            n=numbered[(o['runtime_digest'],o['metadata_digest'])]
            lines.append(f'| {o["project"]} | {source(o,"composer.json",o["directory"])} | {n} | {o["test_file_count"]} |')
        changed=comparison['differing_runtime_paths']
        database=[p for p in changed if p.startswith('database/')]
        contracts=[p for p in changed if p.startswith(('src/Contracts/','src/Actions/','src/Queries/','src/Services/','src/Support/','src/Context/')) and p.endswith('.php')]
        legacy=[p for p in changed if p.startswith('src/Legacy/')]
        registration=[p for p in changed if p=='module.json' or p.startswith(('config/','routes/','resources/')) or 'Provider' in p or any(t in p for t in ('ModuleRegistry','ModuleDiscovery','ModuleValidator','Manifest.php'))]
        lines+=['','## Manifest and dependency differences','',
                'Each row below is one representative per runtime/metadata combination. Module defaults and providers are declarations, not proof of deployment enablement. Read the actual host resolver and registration path; changing defaults can change the selected graph without changing the application manifest.','',
                '| Variant | Module name / version | Default | Provider(s) | Composer runtime requirements |','| --- | --- | --- | --- | --- |']
        for key in sorted(variants):
            o=variants[key][0];base=args.projects/o['repository']/'modules'/o['directory']
            composer=json.loads((base/'composer.json').read_text());manifest=json.loads((base/'module.json').read_text()) if (base/'module.json').exists() else {}
            lines.append(f'| {numbered[key]} | `{safe(manifest.get("name","not declared"))}` / `{safe(manifest.get("version","not declared"))}` | `{safe(manifest.get("default_enabled","not declared"))}` | `{safe(json.dumps(manifest.get("provider",manifest.get("service_providers",[]))))}` | `{safe(json.dumps(composer.get("require",{}),sort_keys=True))}` |')
        lines+=['','## Persistence and data transition','']
        if database:
            lines+=['The following database paths differ or are missing in at least one consumer. A missing file does not prove its table/data never existed, and a matching filename does not prove matching contents. Inspect migration history and the deployed database before adoption.','',
                    '| Differing database path | Variant source and declared table operation |','| --- | --- |']
            for path in database:
                cells=[]
                for key in sorted(variants):
                    o=variants[key][0];local=args.projects/o['repository']/'modules'/o['directory']/path
                    if path not in o['runtime_files']:
                        cells.append(f'V{numbered[key]}: absent');continue
                    content=local.read_bytes();assert hashlib.sha256(content).hexdigest()==o['runtime_files'][path]
                    ops=re.findall(r"Schema::(create|table|dropIfExists|drop|rename)\(\s*['\"]([^'\"]+)",content.decode())
                    detail=', '.join(f'{verb} {table}' for verb,table in ops) or 'inspect file (no literal Schema operation indexed)'
                    cells.append(f'V{numbered[key]}: {source(o,path,o["runtime_files"][path][:10])}; {safe(detail)}')
                lines.append(f'| `{safe(path)}` | '+'<br>'.join(cells)+' |')
            lines+=['','Before a shared release, inventory affected tables/columns and tenant/source identifiers in every consumer, then map legacy/current record identities and callers. Use additive backfills or a separate migration with reconciliation and recovery; do not drop a historical table because the chosen package tree lacks its old migration. Reconcile counts, ownership and required evidence before moving callers or removing obsolete implementations.','']
        else:
            lines+=['No database path differs within the comparison roots. This does not prove statelessness or schema equivalence in deployed consumers; check unchanged migrations, models and host-owned tables referenced by the changed runtime code.','']
        if legacy:
            lines += [f'**Legacy coupling:** {len(legacy)} differing paths are under `src/Legacy/`. They remain potential runtime/data obligations until provider registration and host callers are traced. Keep product-owned legacy behavior in a documented product adapter/extension or migrate it deliberately; do not copy the entire legacy tree into a new universal foundation package.','',
                      'Legacy review paths: '+', '.join('`'+safe(p)+'`' for p in legacy)+'.','']
        lines+=['## Public contract and extension review','']
        if contracts:
            lines+=['Changed action/query/contract/service/context paths are indexed below. Signature differences identify compatibility work; equal signatures alone do not prove matching authorization, validation, side effects or event timing.','',
                    '| Path | Variant entry points |','| --- | --- |']
            for path in contracts:
                cells=[]
                for key in sorted(variants):
                    o=variants[key][0]
                    if path not in o['runtime_files']:
                        cells.append(f'V{numbered[key]}: absent');continue
                    local=args.projects/o['repository']/'modules'/o['directory']/path
                    data=local.read_bytes();assert hashlib.sha256(data).hexdigest()==o['runtime_files'][path]
                    signatures=[signature for signature,_ in methods(data.decode())]
                    cells.append(f'V{numbered[key]}: '+source(o,path,local.name)+' — '+(' ; '.join('`'+safe(s)+'`' for s in signatures) or 'inspect implementation'))
                lines.append(f'| `{safe(path)}` | '+'<br>'.join(cells)+' |')
        else:
            lines+=['No differing paths were found in the indexed contract/action/query/service/context roots. Review the provider, models, adapters and manifest differences below; this is not a claim of complete behavioral equivalence.']
        lines+=['','Resolve host-model lookups, actor/tenant policy, source-record references and provider dependencies through explicit public contracts/configuration. Keep product policy and presentation composition outside shared core. Consumer tests must cover the real call paths, including jobs/exports and private-data visibility; do not widen a contract solely to accommodate one host\'s internal model.','',
                '## Registration, route and presentation review','']
        if registration:
            for path in registration:
                locations=[]
                for key in sorted(variants):
                    o=variants[key][0]
                    if path in o['runtime_files']:locations.append(f'V{numbered[key]} '+source(o,path,'source'))
                lines.append(f'- `{safe(path)}`: '+', '.join(locations))
            lines+=['']
        else:
            lines+=['No registration/route/resource path difference was classified. Inspect other changed paths and host wiring before claiming adapter parity.','']
        lines+=['Validate discovery, manifest schema/version handling, dependency selection, provider boot order and route/plugin identifiers against the consuming host. For UI/API adapters, retain the authorized DTO and domain action semantics rather than exposing private models or bypassing transitions through generic record saves.','',
                'React/Inertia and Next.js can share framework-independent components, not page/session/redirect lifecycles. If a shared adapter is proposed, review all relevant variants and declared peers/exports first; a shared documentation home is not a completed code migration.','',
                '## Adoption sequence and acceptance','',
                '1. Confirm the canonical maintainer/release source and supported versions, then compare every source variant above with its actual host callers and schema. Keep the existing installed identities until that decision is reviewed.',
                '2. Separate genuine shared behavior from product-specific legacy/adapters. Define the required extension points and map source-record IDs/data before removing or redirecting a caller.',
                '3. Release compatible changes or an explicitly versioned migration. Test a clean consumer and upgrade/recovery path without local dependency overrides; package version strings and source tests are not release evidence.',
                '4. Adopt one consumer through a targeted dependency/lockfile update, verify data reconciliation and meaningful permitted/denied/tenant/retry journeys, then expand to other consumers.',
                '5. Record package/source versions, schema/data transition, retained extensions, checks run, remaining limitations and operational recovery. Preserve tracked installed trees and all documented product capabilities until callers/data have moved.','',
                'The current documentation supplies source comparisons and a consolidation design. Application refactoring, migration execution, package publication and certification of a stable common release remain separate owning-project work.','']
        page.write_text('\n'.join(lines))
    index=output/'README.md'
    lines=['# Divergent shared-package adoption profiles','',
           f'These **{len(divergent)} package-specific profiles** expand the runtime/metadata differences in the [shared comparison](../SHARED-MODULE-COMPARISON.md). They identify pinned consumers, manifest/provider/dependency differences, changed database paths/table operations, contract signatures and data-preserving adoption steps. They do not certify a stable release or change application code.','',
           'The 89 compared identities with matching selected runtime/metadata inputs still need consumer/release verification before adoption; they do not need a fabricated data-migration profile merely because copies are tracked in multiple hosts.','',
           '| Identity | Runtime variants | Metadata variants | Profile |','| --- | ---: | ---: | --- |']
    for c in divergent:lines.append(f'| `{c["identity"]}` | {c["runtime_variants"]} | {c["metadata_variants"]} | [Adoption review]({c["identity"].replace("/","--")}.md) |')
    lines+=['','Reproduce with `python3 tools/build_shared_adoption_guides.py --projects /tmp/liberu-documentation-sources` after preparing the inventory-pinned views. [General consolidation procedure](../SHARED-MODULES.md).','']
    index.write_text('\n'.join(lines))
    print(f'Built {len(divergent)} shared adoption profiles with verified pinned-source hashes and schema/contract review evidence.')


if __name__=='__main__':main()

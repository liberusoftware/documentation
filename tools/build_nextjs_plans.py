#!/usr/bin/env python3
"""Build module-specific Next.js plans with shared homes and pinned source references."""
import argparse
from collections import defaultdict
import json
import os
from pathlib import Path
import re
import subprocess

from build_source_reference import methods, safe, source_url

ROOT=Path(__file__).resolve().parents[1]
MARKER='<!-- nextjs-plan:generated -->'


def relative_link(origin,destination,label):
    return f'[{label}]({os.path.relpath(destination,origin.parent)})'


def scope_file(project,stem):
    for layer in ('features','core'):
        path=ROOT/'projects'/project/layer/(stem+'.md')
        if path.exists():return path
    raise ValueError(f'{project}/{stem}: missing scope document')


def title_for(project,stem):
    title=scope_file(project,stem).read_text().splitlines()[0].removeprefix('# ')
    return title.split(': ',1)[-1].removesuffix(' domain packages')


def scope_labels(project,stem):
    content=scope_file(project,stem).read_text()
    section=re.search(r'## 2\. Full feature scope\n(.*?)(?=\n## |\Z)',content,re.S)
    return re.findall(r'^- \*\*([^*]+):\*\*',section.group(1),re.M) if section else []


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects',type=Path,default=Path('/home/liberu/projects'))
    args=parser.parse_args()
    mapping=json.loads((ROOT/'architecture/source-design-mapping.json').read_text())['projects']
    snapshot=json.loads((ROOT/'architecture/source-inventory.json').read_text())['repositories']
    references=json.loads((ROOT/'architecture/source-reference-index.json').read_text())['packages']
    records={r['project']:r for r in snapshot}
    tracked={}
    for record in snapshot:
        repo=args.projects/record['repository']
        actual=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
        dirty=subprocess.check_output(['git','-C',str(repo),'status','--porcelain'],text=True).strip()
        if actual!=record['commit'] or dirty:raise SystemExit(f'{repo}: differs from pinned clean source')
        tracked[record['project']]=subprocess.check_output(['git','-C',str(repo),'ls-files'],text=True).splitlines()
    groups=defaultdict(list)
    for project,info in mapping.items():
        for stem,design in info['designs'].items():
            core=design['layers']['core']
            key=core[0]['identity'] if len(core)==1 else f'planned:{project}:{stem}'
            groups[key].append((project,stem))
    def home_score(pair):
        project,stem=pair
        feature=(ROOT/'projects'/project/'features'/(stem+'.md')).exists()
        return (project!='boilerplate',not feature,len(stem),project,stem)
    homes={key:min(pairs,key=home_score) for key,pairs in groups.items()}
    proposals=defaultdict(set)
    for key in groups:
        project,stem=homes[key]
        name=('module-'+key.split('/')[-1].removeprefix('module-')+'-nextjs') if not key.startswith('planned:') else f'module-{project}-{stem}-nextjs'
        proposals[name].add(key)
    collision_keys=set().union(*(keys for keys in proposals.values() if len(keys)>1)) if any(len(v)>1 for v in proposals.values()) else set()
    output={};canonical_written=0;aliases_written=0;preserved=0
    for key,pairs in sorted(groups.items()):
        project,stem=homes[key]
        home=ROOT/'projects'/project/'nextjs'/(stem+'.md')
        home.parent.mkdir(exist_ok=True)
        design=mapping[project]['designs'][stem]
        core=design['layers']['core']
        api_sources={}
        for consumer_project,consumer_stem in [(project,stem)]+sorted(pair for pair in pairs if pair!=(project,stem)):
            for choice in mapping[consumer_project]['designs'][consumer_stem]['layers']['api']:
                api_sources.setdefault(choice['identity'],(consumer_project,choice))
        api=[choice for _,choice in api_sources.values()]
        name=('module-'+key.split('/')[-1].removeprefix('module-')+'-nextjs') if not key.startswith('planned:') else f'module-{project}-{stem}-nextjs'
        title=title_for(project,stem)
        keep_existing=home.exists() and MARKER not in home.read_text()
        if keep_existing:
            # Retain authored enterprise plans and other hand-maintained module details.
            preserved+=1
        else:
            labels=scope_labels(project,stem)
            source_locations=[]
            for origin_project,choice in [(project,c) for c in core]+list(api_sources.values()):
                record=records.get(origin_project)
                if not record:continue
                prefix=f'modules/{choice["directory"]}/'
                files=[p for p in tracked[origin_project] if p.startswith(prefix)]
                source_locations.append((record,choice,prefix,files))
            commands=[];queries=[];models=[];routes=[];declared=[]
            for record,choice,prefix,files in source_locations:
                repo=args.projects/record['repository']
                manifest_path=repo/prefix/'module.json'
                if manifest_path.exists():
                    manifest=json.loads(manifest_path.read_text())
                    declared.extend(str(v) for v in manifest.get('features',[]) if isinstance(v,str))
                for file in files:
                    local=file.removeprefix(prefix)
                    path=repo/file
                    if not path.is_file():continue
                    if local.startswith(('src/Actions/','src/Queries/','src/Services/')) and file.endswith('.php'):
                        sigs=[signature for signature,_ in methods(path.read_text()) if not re.search(r'function __construct\(',signature)]
                        if sigs:
                            entry=(record,file,sigs)
                            if local.startswith('src/Queries/'):queries.append(entry)
                            else:commands.append(entry)
                    elif local.startswith('src/Models/') and file.endswith('.php'):
                        match=re.search(r'\$fillable\s*=\s*\[(.*?)\]',path.read_text(),re.S)
                        fields=re.findall(r"['\"]([a-zA-Z_]\w*)['\"]",match.group(1)) if match else []
                        models.append((record,file,fields))
                    elif local.startswith('routes/') and file.endswith('.php'):
                        declarations=[]
                        for line in path.read_text().splitlines():
                            clean=line.strip()
                            if re.search(r'Route::(?:get|post|put|patch|delete|apiResource|resource|middleware|prefix)\(',clean):declarations.append(clean)
                        routes.append((record,file,declarations))
            labels=labels or list(dict.fromkeys(declared)) or [title]
            lines=[f'# {title}: Next.js presentation plan','',MARKER,'',
                   '**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.','',
                   f'**Adapter group:** `{key}`.','',
                   ('**Package naming:** deferred because prefixed and unprefixed source identities would produce the same proposed adapter name. Resolve source ownership/compatibility before assigning a publishable identity.' if key in collision_keys else f'**Proposed design identifier:** `{name}`. Confirm the actual npm scope/name, exports and peer versions before publishing.'),'',
                   '## Scope and ownership','',
                   'The '+relative_link(home,scope_file(project,stem),'domain specification')+' owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.','']
            if len(pairs)>1:
                lines += [f'This plan is the shared documentation home for **{len(pairs)} existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.','']
            if core or api:
                lines+=['| Boundary | Observed package reference |','| --- | --- |']
                for role,choices in [('Core',core),('API',api)]:
                    for choice in choices:lines.append(f'| {role} | {relative_link(home,ROOT/choice["reference"],choice["identity"])} |')
                lines+=['']
            if not api:
                lines += ['No dedicated API package name match is established among the mapped consumers of this core identity. Review routes in the core/application tree and define an authorized HTTP contract before implementing browser mutations; PHP actions are not directly callable by JavaScript.','']
            if project=='liberu':
                lines += ['The [platform reuse guide](../REUSE.md) identifies existing cross-project implementations and their namespace/table differences. This design scope is not an instruction to create a third parallel owner; reconcile those source families before assigning an npm identity.', '']
            if project=='ecommerce':
                lines += ['Ecommerce implementation also lives outside `modules/`. Preserve this scope and use the [application capability map](../SOURCE-APPLICATION.md) for current services, policies, REST/GraphQL entry points and checkout behavior. A blank package match does not remove the capability.','']
                for row in (ROOT/'projects/ecommerce/SOURCE-APPLICATION.md').read_text().splitlines():
                    if f'](features/{stem}.md)' in row:
                        lines+=['Observed application sources for this capability: '+row.split('|')[-2].strip()+'.','']
            headless=stem.endswith('-contracts') or (core and core[0]['directory'].endswith('-contracts'))
            lines+=['## Module surfaces and component contracts','']
            if headless:
                lines+=['This is a contract/integration capability. It does not require a standalone end-user CRUD page by default. Expose only a necessary configuration/diagnostic surface in a consuming workflow; keep its DTOs and integration contracts reusable.','']
            lines+=['| Capability in the domain scope | Next.js composition target |','| --- | --- |']
            for label in labels:
                lines.append(f'| {safe(label)} | A focused authorized view or workflow section for {safe(label.lower())}; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |')
            lines+=['','Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.','',
                    '## Query and command integration','']
            if queries:
                lines+=['These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.','', '| Source query | Signatures |','| --- | --- |']
                for record,file,sigs in queries:lines.append(f'| [{Path(file).name}]({source_url(record,file)}) | '+'<br>'.join(f'`{safe(s)}`' for s in sigs)+' |')
                lines+=['']
            if commands:
                lines+=['Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.','', '| Source action/service | Signatures |','| --- | --- |']
                for record,file,sigs in commands:lines.append(f'| [{Path(file).name}]({source_url(record,file)}) | '+'<br>'.join(f'`{safe(s)}`' for s in sigs)+' |')
                lines+=['']
            if not commands and not queries:
                lines+=['No concrete action/query signatures were established in the indexed source roots for this design. Use its source reference and owning application routes/contracts to resolve the integration, rather than inventing create/update/delete operations from the module name.','']
            lines+=['The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.','']
            if models:
                lines+=['### Record-field review','', 'These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.','', '| Source model | Observed fillable fields |','| --- | --- |']
                for record,file,fields in models:
                    lines.append(f'| [{Path(file).name}]({source_url(record,file)}) | '+(', '.join(f'`{safe(f)}`' for f in fields) if fields else 'No literal fillable array detected; inspect the model and API schema.')+' |')
                lines+=['']
            if routes:
                lines+=['### Route source evidence','', 'The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.','']
                for record,file,declarations in routes:
                    lines+= [f'[{file}]({source_url(record,file)})','']
                    if declarations:
                        lines+=['```php',*declarations,'```','']
            lines+=['## Server/client and React reuse','',
                    'Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.','',
                    'Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application\'s private frontend state.','',
                    '## State, failures and verification','',
                    '| Situation | User-facing behavior and integration requirement |','| --- | --- |',
                    '| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |',
                    '| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |',
                    '| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |',
                    '| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |',
                    '| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |',
                    '| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |','',
                    'Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.','',
                    'Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.','',
                    'See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).','']
            if project=='crm' and stem in ('sales-pipelines','crm-sales-pipelines'):
                lines+=['Read the [source-backed sales-pipeline walkthrough](../guides/SALES-PIPELINES.md) before relying on the API pagination, move retry behavior, close rules or current UI parity.','']
            home.write_text('\n'.join(lines));canonical_written+=1
        for other_project,other_stem in pairs:
            path=ROOT/'projects'/other_project/'nextjs'/(other_stem+'.md');path.parent.mkdir(exist_ok=True)
            if path==home:continue
            content=[f'# {title_for(other_project,other_stem)}: shared Next.js adapter','',MARKER,'',
                     '**Status:** proposed consumer/alias reference. This document preserves the existing module scope; it does not create another npm package or certify source compatibility.','',
                     '## Shared implementation home','',
                     'Use '+relative_link(path,home,title+': Next.js presentation plan')+f' for adapter group `{key}`. Its component, API, validation, cache and recovery contracts belong to that shared plan.','',
                     'The local '+relative_link(path,scope_file(other_project,other_stem),'domain specification')+' remains the application scope. Enable only the UI needed by this consumer and keep product-specific policy in documented extension points. Review the source variants and API contract before adopting a common adapter release.','',
                     'A directory alias or alternate design spelling is not a separate authoritative record owner. The application owns its routes, navigation and session integration; the shared adapter owns reusable components and transport boundaries.','',
                     'See the [project source map](../SOURCE-MAPPING.md#'+other_stem+'), [reuse guide](../../../architecture/SHARED-MODULES.md), and [npm lifecycle guide](../../../guides/NPM.md).','']
            path.write_text('\n'.join(content));aliases_written+=1
        output[key]={'home':str(home.relative_to(ROOT)),'proposed_name':None if key in collision_keys else name,'source_identity_review_required':key in collision_keys,
                     'consumers':[{'project':p,'design':s,'document':str((ROOT/'projects'/p/'nextjs'/(s+'.md')).relative_to(ROOT))} for p,s in sorted(pairs)]}
    project_counts={}
    for project,info in mapping.items():
        path=ROOT/'projects'/project/'nextjs/README.md'
        lines=[f'# {project.replace("-"," ").title()}: Next.js module plans','',
               'These are proposed API-consuming React adapters, not verified npm releases. Laravel owns domain behavior; the Next.js application owns routing, session integration and deployment. Share framework-independent React UI with Inertia through separate transport/navigation wrappers.','',
               'Each documented spelling below has a module plan. Multiple spellings or applications that match one observed core identity reference one shared adapter home; no existing domain scope is removed. Different source variants still require compatibility review.','',
               '| Module scope | Adapter plan | Shared home |','| --- | --- | --- |']
        for stem,design in sorted(info['designs'].items()):
            core=design['layers']['core'];key=core[0]['identity'] if len(core)==1 else f'planned:{project}:{stem}'
            home=ROOT/output[key]['home'];page=path.parent/(stem+'.md')
            lines.append('| '+relative_link(path,scope_file(project,stem),title_for(project,stem))+' | '+relative_link(path,page,'Next.js plan')+' | '+relative_link(path,home,'Shared plan' if page!=home else 'This module')+' |')
        lines+=['','See the [Next.js standard](../../../standards/NEXTJS.md), [source map](../SOURCE-MAPPING.md), [npm guide](../../../guides/NPM.md) and [adapter ownership registry](../../../modules/nextjs/OWNERSHIP.md).','']
        path.write_text('\n'.join(lines));project_counts[project]=len(info['designs'])
    (ROOT/'architecture/nextjs-adapter-plans.json').write_text(json.dumps({'groups':output},indent=2)+'\n')
    home=ROOT/'modules/nextjs/OWNERSHIP.md'
    lines=['# Next.js adapter ownership and reuse','',
           f'The documentation preserves **{sum(project_counts.values())} module spellings** across **{len(project_counts)} scopes**, with **{len(output)} adapter plan groups**. {sum(len(v["consumers"])-1 for v in output.values())} consumer/alias documents reference shared homes rather than claiming separate implementations. These are design/documentation homes, not a registry availability or stability claim.','',
           'Groups use exact observed core identities where one name match exists. Different PHP identities are not silently merged by similar spelling. Planned scopes without a source match remain separate, including all Ecommerce modules. Source variants and PHP/API compatibility must be reviewed before a shared npm release.','',
           '## Adapter groups','', '| Core identity or planned scope | Canonical plan | Consumer/design spellings |','| --- | --- | ---: |']
    for key,item in sorted(output.items()):lines.append(f'| `{key}` | {relative_link(home,ROOT/item["home"],"Plan")} | {len(item["consumers"])} |')
    lines+=['','## Naming collisions requiring source review','',
            'Some Liberu platform capabilities have both prefixed and unprefixed PHP identities. Normalizing the names would produce the same adapter name. The plans leave npm naming unassigned until ownership, source/schema differences and consumer compatibility are reconciled; two incompatible implementations must not publish under one identity/version.','']
    for name,keys in sorted(proposals.items()):
        if len(keys)>1:lines.append(f'- `{name}`: '+', '.join(f'`{key}`' for key in sorted(keys)))
    lines+=['','Reproduce with `python3 tools/build_nextjs_plans.py` after rebuilding source references/mapping. Authored enterprise module plans are retained; generated plans carry a marker. [Machine-readable adapter registry](../../architecture/nextjs-adapter-plans.json).','']
    home.write_text('\n'.join(lines))
    index=ROOT/'modules/nextjs/README.md'
    lines=['# Next.js presentation module plans','',
           f'Optional API-consuming React adapters cover **{sum(project_counts.values())} documented module spellings** in **{len(project_counts)} scopes**. The [ownership registry](OWNERSHIP.md) consolidates them into **{len(output)} plan groups** using observed core identities where established. These are target plans, not published packages.','',
           'Use the [Next.js standard](../../standards/NEXTJS.md) for server/client boundaries, sessions, authorization, caching and deployment, and the [npm lifecycle guide](../../guides/NPM.md) for development and release. Framework-independent React UI can be shared with Inertia; routing, forms and transport require distinct adapters.','',
           '| Project | Documented module spellings |','| --- | ---: |']
    for project,count in sorted(project_counts.items()):lines.append(f'| [{project}](../../projects/{project}/nextjs/README.md) | {count} |')
    index.write_text('\n'.join(lines)+'\n')
    print(f'Next.js: {len(output)} canonical groups, {canonical_written} generated plans, {preserved} authored plans retained, {aliases_written} consumer/alias references; {sum(project_counts.values())} documents.')


if __name__=='__main__':main()

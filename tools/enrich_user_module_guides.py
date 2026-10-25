#!/usr/bin/env python3
"""Add module-specific scope and source/availability guidance without removing journeys."""
import json
import os
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
START='<!-- module-scope:start -->';END='<!-- module-scope:end -->'


def main():
    mapping=json.loads((ROOT/'architecture/source-design-mapping.json').read_text())['projects']
    registry=json.loads((ROOT/'architecture/nextjs-adapter-plans.json').read_text())['groups']
    count=0;module_counts={}
    for project,info in mapping.items():
        folder=ROOT/'user-guides/projects'/project/'modules'
        for stem,design in info['designs'].items():
            page=folder/(stem+'.md')
            if not page.exists() or project=='sap':continue # Keep the authored enterprise task guides.
            core=design['layers']['core'];key=core[0]['identity'] if len(core)==1 else f'planned:{project}:{stem}'
            home=Path(registry[key]['home']);owner_project=home.parts[1];owner_stem=home.stem
            scope=ROOT/'projects'/owner_project/'features'/(owner_stem+'.md')
            if not scope.exists():scope=ROOT/'projects'/project/'core'/(stem+'.md')
            content=scope.read_text();title=content.splitlines()[0].removeprefix('# ').split(': ',1)[-1].removesuffix(' domain packages')
            group=re.search(r'^## 2\. Full feature scope\n(.*?)(?=^## |\Z)',content,re.M|re.S)
            labels=re.findall(r'^- \*\*([^*]+):\*\*',group.group(1),re.M) if group else []
            purpose=re.search(r'^## 1\. Purpose\n\n(.*?)(?=\n\n|\n## |\Z)',content,re.M|re.S)
            summary=purpose.group(1) if purpose else ''
            summary=re.sub(r'^The .+? module owns ','',summary)
            summary=re.sub(r'\. It is the authoritative boundary.*','.',summary)
            if len(summary)>750:summary=summary[:747]+'...'
            lines=['**Availability:** this is a task/experience contract. Confirm the enabled application and your permitted actions; a documented capability or source package does not prove that every screen is deployed.','',
                   '## Module-specific scope','',
                   (f'The intended **{title}** workspace covers '+summary[0].lower()+summary[1:] if summary else f'Use this guide for the **{title}** capability and its authorized workflow.'),'']
            if labels:
                lines+=['The relevant capability areas are '+', '.join('**'+label+'**' for label in labels)+'. Use their actual enabled screens/operations rather than treating every area as an interchangeable create/edit/delete resource.','']
            if stem.endswith('-contracts'):
                lines+=['This is a supporting contract/integration capability. A consuming workspace may use it without exposing an independent end-user page; configuration and diagnostics are offered only where the application needs them.','']
            lines+=['## Follow the task safely','',
                    '1. Open the enabled module from the appropriate project workspace and confirm the current account/team and any relevant entity, store, site or record scope.',
                    '2. Review the selected record/context, current state, source evidence and available actions. A visible action can still be restricted by record policy, approval, version or effective date.',
                    '3. Enter the required information using the actual form labels and authorized choices. Review any preview/approval summary and submit the explicit action; a generic status edit is not a substitute for a business transition.',
                    '4. Read the result. Queued/running means work continues; confirm a final business outcome only when the owner reports it. Keep an operation/reference link for long-running or uncertain work.',
                    '5. Correct field errors with the safe draft preserved. Reload/review a changed record before resubmitting; after a timeout, inspect the existing operation/current record before repeating a write.','',
                    'Different modules have different valid commands, permissions and correction rules. Posted, accepted, published or otherwise finalized records may require a dedicated correction/reversal process rather than ordinary deletion. The owning module contract determines the actual behavior.','',
                    '## Administrator and developer references','']
            local_map=ROOT/'projects'/project/'SOURCE-MAPPING.md'
            lines+=['The '+f'[source map]({os.path.relpath(local_map,page.parent)}#{stem})'+' distinguishes target requirements, source identities and layer availability. It does not certify runtime parity.','']
            if project=='ecommerce':
                app=ROOT/'projects/ecommerce/SOURCE-APPLICATION.md'
                lines+=['Ecommerce also implements this product scope in application-owned code outside `modules/`. Preserve the module and review its '+f'[application capability map]({os.path.relpath(app,page.parent)})'+'.','']
            if core:
                lines+=['Observed implementation references: '+ ' · '.join(f'[{c["identity"]}]({os.path.relpath(ROOT/c["reference"],page.parent)})' for c in core)+'. These technical references identify current metadata/code, not a promise that every target journey is enabled.','']
            nextjs=ROOT/'projects'/project/'nextjs'/(stem+'.md')
            api=ROOT/'projects'/project/'api'/(stem+'.md')
            lines+=['Presentation/transport detail: '+f'[API plan]({os.path.relpath(api,page.parent)})'+' · '+f'[Next.js plan and shared adapter home]({os.path.relpath(nextjs,page.parent)})'+'. Inertia and independent API clients can share domain/UI contracts while keeping their navigation, session and form lifecycles separate.','']
            if (owner_project,owner_stem)!=(project,stem):
                canonical=ROOT/'user-guides/projects'/owner_project/'modules'/(owner_stem+'.md')
                if canonical.exists():lines+=['This spelling/consumer maps to the same observed core identity as '+f'[{title}]({os.path.relpath(canonical,page.parent)})'+'. Its local scope remains preserved; avoid creating a competing record owner or assuming every consumer has identical deployed UI.','']
            block=START+'\n'+'\n'.join(lines)+END
            original=page.read_text()
            if START in original:updated=re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:block,original,flags=re.S)
            else:
                split=original.find('\n## ')
                if split<0:updated=original+'\n'+block+'\n'
                else:updated=original[:split]+'\n\n'+block+'\n'+original[split:]
            if updated!=original:page.write_text(updated);count+=1
        module_counts[project]=len([p for p in folder.glob('*.md') if p.name!='README.md'])
        project_readme=ROOT/'user-guides/projects'/project/'README.md'
        if project_readme.exists() and '## Availability and implementation' not in project_readme.read_text():
            source_map=ROOT/'projects'/project/'SOURCE-MAPPING.md'
            project_readme.write_text(project_readme.read_text()+'\n## Availability and implementation\n\nThese are target experience/task guides. Use the '+f'[current source map]({os.path.relpath(source_map,project_readme.parent)})'+' to identify observed packages and source locations; confirm enabled UI and permissions in the installed application. Business state and operation progress remain separate across every presentation.\n')
    index=ROOT/'user-guides/modules/README.md'
    lines=['# End-user module guides','',
           'Choose a project, then the module/task guide. The catalogue preserves all documented spellings, including compatibility aliases; counts are documents, not deployed features or separate independent packages. Source maps and module-specific references distinguish current code from target behavior.','',
           '| Project | Module/task documents |','| --- | ---: |']
    for project,document_count in sorted(module_counts.items()):lines.append(f'| [{project}](../projects/{project}/modules/README.md) | {document_count} |')
    lines+=['','The [shared experience standard](../WEB-AND-MOBILE.md) covers accessible web/mobile states. Administrators can use the [presentation guide](../../architecture/PRESENTATION.md) and [implementation references](../../modules/source/README.md) for transport, source and package details.','']
    index.write_text('\n'.join(lines))
    print(f'Updated {count} module-specific guide blocks across {len(module_counts)} projects; refreshed document counts.')


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Audit project/module/layer/source coverage; semantic review remains a separate gate."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
LAYERS=('core','api','filament','livewire','react','vue','nuxt','nextjs','react-native','flutter')


def normal(value,project):
    value=value.split('/')[-1];previous=None
    while previous!=value:
        previous=value;value=value.removeprefix('module-').removeprefix(project+'-')
    return value


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects',type=Path,default=Path('/tmp/liberu-documentation-sources'))
    parser.add_argument('--report',type=Path,required=True)
    args=parser.parse_args()
    mapping=json.loads((ROOT/'architecture/source-design-mapping.json').read_text())['projects']
    inventory=json.loads((ROOT/'architecture/source-inventory.json').read_text())['repositories']
    references=json.loads((ROOT/'architecture/source-reference-index.json').read_text())['packages']
    plans=json.loads((ROOT/'architecture/nextjs-adapter-plans.json').read_text())['groups']
    failures=[];metadata_checked=0;fence_checked=0;counts={}
    for project,info in mapping.items():
        stems=set(info['designs']);counts[project]={}
        for layer in LAYERS:
            folder=ROOT/'projects'/project/layer
            actual={p.stem for p in folder.glob('*.md') if p.name!='README.md'}
            if actual!=stems:failures.append(f'{project}/{layer}: document spellings differ from the source map')
            index=(folder/'README.md').read_text()
            linked={target.split('#',1)[0] for target in re.findall(r'\]\(([^)]+)\)',index)}
            absent={stem+'.md' for stem in actual}-linked
            if absent:failures.append(f'{project}/{layer}: {len(absent)} documents absent from index')
            counts[project][layer]=len(actual)
            for stem in actual:
                page=folder/(stem+'.md');text=page.read_text();expected=normal(info['designs'][stem].get('design_alias') or stem,project)
                for label,value in re.findall(r'\*\*(Matching domain module|Domain module):\*\* `([^`]+)`',text):
                    metadata_checked+=1
                    if normal(value,project)!=expected:failures.append(f'{page.relative_to(ROOT)}: mismatched {label}')
                opened=None
                for line_no,line in enumerate(text.splitlines(),1):
                    m=re.match(r'^\s*(`{3,}|~{3,})([^`]*)$',line)
                    if m:
                        if opened is None:opened=(m[1][0],len(m[1]),line_no)
                        elif m[1][0]==opened[0] and len(m[1])>=opened[1] and not m[2].strip():opened=None
                    elif opened and re.match(r'^##? ',line):failures.append(f'{page.relative_to(ROOT)}:{line_no}: heading swallowed by code fence')
                if opened:failures.append(f'{page.relative_to(ROOT)}: unclosed code fence')
                fence_checked+=1
                if layer=='api' and ('example-value' in text or 'additionalProperties: true' in text):
                    failures.append(f'{page.relative_to(ROOT)}: invented payload/unrestricted prototype remains')
        features={p.stem for p in (ROOT/'projects'/project/'features').glob('*.md') if p.name!='README.md'}
        if not features.issubset(stems):failures.append(project+': feature has no source/design mapping')
        user_folder=ROOT/'user-guides/projects'/project/'modules'
        guides={p.stem for p in user_folder.glob('*.md') if p.name!='README.md'}
        if guides!=stems:failures.append(project+': task guide coverage differs')
        user_links={p.split('#',1)[0] for p in re.findall(r'\]\(([^)]+)\)',(user_folder/'README.md').read_text())}
        if {s+'.md' for s in guides}-user_links:failures.append(project+': incomplete task index')
        for stem in guides:
            text=(user_folder/(stem+'.md')).read_text()
            if project=='sap':
                if '## Complete the illustrated task' not in text:failures.append(project+'/'+stem+': missing concrete enterprise journey')
            elif '<!-- module-scope:start -->' not in text:failures.append(project+'/'+stem+': missing module-specific task scope')
        counts[project]['features']=len(features);counts[project]['task_guides']=len(guides)
    physical={(r['repository'],m['directory']) for r in inventory for m in r['modules'] if m['manifests'] and not m.get('alias_of')}
    documented={(o['repository'],o['directory']) for info in references.values() for o in info['locations']}
    if physical!=documented:failures.append('Observed physical package/reference coverage differs')
    for identity,info in references.items():
        page=ROOT/info['reference']
        if not page.is_file():failures.append(identity+': missing implementation reference');continue
        text=page.read_text()
        for heading in ('## Source locations','### Manifest and registration','### Dependencies and namespace mapping','### Source entry points','### Persistence and lifecycle evidence','### Verification and consumer use'):
            if heading not in text:failures.append(identity+': missing reference section '+heading)
    expected_consumers={(project,stem) for project,info in mapping.items() for stem in info['designs']}
    consumers={(c['project'],c['design']) for group in plans.values() for c in group['consumers']}
    if consumers!=expected_consumers:failures.append('Next.js registry does not cover every documented spelling')
    for key,group in plans.items():
        if not (ROOT/group['home']).is_file():failures.append(key+': missing shared adapter home')
        for consumer in group['consumers']:
            page=ROOT/consumer['document']
            if not page.is_file():failures.append(key+': missing consumer/alias document')
            elif str(page.relative_to(ROOT))!=group['home']:
                targets=[target.split('#',1)[0] for target in re.findall(r'\]\(([^)]+)\)',page.read_text()) if '://' not in target]
                if (ROOT/group['home']).resolve() not in {(page.parent/target).resolve() for target in targets}:
                    failures.append(key+': consumer has no exact link to its canonical plan')
    discovered={r['name'] for r in json.loads((ROOT/'architecture/source-repositories.json').read_text())}
    if discovered!={r['repository'] for r in inventory}:failures.append('Discovery and scanned repository sets differ')
    for record in inventory:
        primary=Path('/home/liberu/projects')/record['repository'];snapshot=args.projects/record['repository']
        if not (primary/'.git').exists():failures.append(record['repository']+': original clone missing')
        if subprocess.check_output(['git','-C',str(snapshot),'rev-parse','HEAD'],text=True).strip()!=record['commit']:failures.append(record['repository']+': snapshot HEAD mismatch')
        if subprocess.check_output(['git','-C',str(snapshot),'status','--porcelain'],text=True).strip():failures.append(record['repository']+': snapshot dirty')
        if not (ROOT/'projects'/record['project']/'DEVELOPMENT.md').is_file():failures.append(record['project']+': missing clone development guide')
    old_scope=subprocess.check_output(['git','-C',str(ROOT),'show','HEAD:projects/ecommerce/ECOMMERCE.md'])
    if old_scope!=(ROOT/'projects/ecommerce/ECOMMERCE.md').read_bytes():failures.append('Original Ecommerce scope catalogue changed')
    comparison=json.loads((ROOT/'architecture/shared-module-comparison.json').read_text())['comparisons']
    divergent=[c for c in comparison if c['runtime_variants']>1 or c['metadata_variants']>1]
    for c in divergent:
        if not (ROOT/'architecture/shared-adoption'/(c['identity'].replace('/','--')+'.md')).is_file():failures.append(c['identity']+': missing adoption profile')
    result={'projects':counts,'source_repositories':len(inventory),'physical_package_locations':len(physical),'package_identities':len(references),
            'nextjs_plan_groups':len(plans),'nextjs_consumer_alias_documents':len(consumers)-len(plans),
            'shared_adoption_profiles':len(divergent),'domain_metadata_fields_checked':metadata_checked,'module_fences_checked':fence_checked,'failures':failures,
            'scope':'Coverage, navigation, metadata and pinned-source integrity. Does not prove semantic completeness, runtime parity, package stability or rendered browser behavior; use the written objective audit and source review.'}
    args.report.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Coverage: {len(mapping)} scopes, {len(consumers)} spellings, {len(references)} identities/{len(physical)} locations, {len(plans)} Next.js groups, {len(divergent)} shared-adoption profiles.')
    print(f'Metadata checks: {metadata_checked}; module fence checks: {fence_checked}; failures: {len(failures)}.')
    for failure in failures[:25]:print(failure)
    if failures:raise SystemExit(1)


if __name__=='__main__':main()

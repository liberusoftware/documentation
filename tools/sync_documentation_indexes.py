#!/usr/bin/env python3
"""Keep existing project/layer indexes complete without deleting module documents."""
import json
import os
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
LAYERS=('features','core','api','filament','livewire','react','vue','nuxt','react-native','flutter')


def links(line,expected):
    return any(target.split('#',1)[0] in expected for target in re.findall(r'\]\(([^)]+)\)',line))


def replace_catalogue(text,expected,table):
    lines=text.splitlines();result=[];inserted=False;i=0
    while i<len(lines):
        if lines[i].startswith('|'):
            end=i+1
            while end<len(lines) and lines[end].startswith('|'):end+=1
            block=lines[i:end]
            if any(links(line,expected) for line in block):
                if not inserted:result.extend(table);inserted=True
                i=end;continue
        if re.match(r'^[-*] ',lines[i]) and links(lines[i],expected):
            if not inserted:result.extend(table);inserted=True
            i+=1;continue
        result.append(lines[i]);i+=1
    if not inserted:result+=['','## Complete module catalogue','',*table]
    return '\n'.join(result).rstrip()+'\n'


def main():
    mapping=json.loads((ROOT/'architecture/source-design-mapping.json').read_text())['projects']
    changed=0
    for project,info in mapping.items():
        for layer in LAYERS:
            directory=ROOT/'projects'/project/layer;index=directory/'README.md'
            if not index.exists():continue
            pages=sorted(p for p in directory.glob('*.md') if p.name!='README.md')
            expected={p.name for p in pages}
            table=['| Module document | Source/target reference | Related plans |','| --- | --- | --- |']
            for page in pages:
                title=page.read_text().splitlines()[0].removeprefix('# ').split(': ',1)[-1]
                design=info['designs'].get(page.stem)
                choices=design['layers']['core' if layer=='features' else layer] if design else []
                source=' · '.join(f'[{c["identity"]}]({os.path.relpath(ROOT/c["reference"],directory)})' for c in choices) or f'[Target/source map](../SOURCE-MAPPING.md#{page.stem})'
                related=' · '.join(f'[{name}](../{name}/{page.name})' for name in ('core','api','nextjs') if name!=layer and (directory.parent/name/page.name).exists())
                table.append(f'| [{title}]({page.name}) | {source} | {related} |')
            original=index.read_text();updated=replace_catalogue(original,expected,table)
            start='<!-- catalogue-status:start -->';end='<!-- catalogue-status:end -->'
            note=start+f'\nThis index preserves **{len(pages)} module documents/spellings**. Counts are specifications, not released packages or deployed features. Exact source identities and aliases are in the [source map](../SOURCE-MAPPING.md); [shared ownership](../../../architecture/SHARED-MODULES.md) and [Next.js adapter homes](../../../modules/nextjs/OWNERSHIP.md) prevent alternate spellings from becoming competing implementations.\n'+end
            if start in updated:updated=re.sub(re.escape(start)+r'.*?'+re.escape(end),lambda _:note,updated,flags=re.S)
            else:
                heading,rest=updated.split('\n',1);updated=heading+'\n\n'+note+'\n'+rest
            if updated!=original:index.write_text(updated);changed+=1
        index=ROOT/'projects'/project/'README.md'
        if index.exists():
            original=index.read_text()
            def update_count(match):
                target=index.parent/match.group(2)
                count=len([p for p in target.parent.glob('*.md') if p.name!='README.md'])
                return f'[{match.group(1)}]({match.group(2)}) — {count} specification documents'
            updated=re.sub(r'\[([^\]]+)\]\(([^)]+/README.md)\)\s*[—–-]\s*\d+ (?:modules|specification documents)',update_count,original)
            if updated!=original:index.write_text(updated);changed+=1
        directory=ROOT/'user-guides/projects'/project/'modules';index=directory/'README.md'
        if index.exists():
            pages=sorted(p for p in directory.glob('*.md') if p.name!='README.md');expected={p.name for p in pages}
            table=['| Module/task guide | Design/source context |','| --- | --- |']
            for page in pages:
                title=page.read_text().splitlines()[0].removeprefix('# ').removesuffix(' — end-user guide')
                target=ROOT/'projects'/project/'SOURCE-MAPPING.md'
                table.append(f'| [{title}]({page.name}) | [Context]({os.path.relpath(target,directory)}#{page.stem}) |')
            original=index.read_text();updated=replace_catalogue(original,expected,table)
            if updated!=original:index.write_text(updated);changed+=1
    print(f'Synchronized {changed} project/layer/task indexes; all sibling module documents remain listed.')


if __name__=='__main__':main()

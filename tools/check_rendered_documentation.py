#!/usr/bin/env python3
"""Parse GFM-like Markdown and check local heading fragments with github-slugger."""
import argparse
from html import escape
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parents[1]
PREVIEWS=('GETTING-STARTED.md','modules/source/README.md','modules/source/liberusoftware--module-crm-sales-pipelines.md',
          'projects/crm/SOURCE-MAPPING.md','projects/crm/guides/SALES-PIPELINES.md',
          'projects/ecommerce/SOURCE-APPLICATION.md','projects/sap/SOURCE-APPLICATION.md',
          'projects/sap/design/finance.md','guides/COMPOSER.md','guides/NPM.md','standards/NEXTJS.md',
          'projects/crm/nextjs/sales-pipelines.md','projects/crm/nextjs/crm-sales-pipelines.md',
          'projects/crm/api/sales-pipelines.md','projects/sap/api/finance.md',
          'projects/sap/filament/procurement.md','user-guides/projects/accounting/modules/general-ledger.md',
          'architecture/PRESENTATION.md')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--slugger-module',type=Path,required=True,help='Installed github-slugger index.js')
    parser.add_argument('--report',type=Path,required=True)
    parser.add_argument('--preview-dir',type=Path)
    args=parser.parse_args()
    renderer=MarkdownIt('gfm-like',{'html':True,'linkify':False})
    links=[];headings={};explicit={};h1_issues=[]
    pages=sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts)
    for number,page in enumerate(pages,1):
        text=page.read_text();tokens=renderer.parse(text)
        page_headings=[];h1s=0
        for i,token in enumerate(tokens):
            if token.type=='heading_open':
                h1s+=token.tag=='h1'
                content=tokens[i+1]
                page_headings.append(''.join(c.content for c in content.children or [] if c.type in ('text','code_inline','image')))
            if token.type=='inline':
                for child in token.children or []:
                    if child.type!='link_open':continue
                    href=child.attrGet('href') or ''
                    if '#' not in href or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',href):continue
                    raw,fragment=href.split('#',1)
                    if not fragment:continue
                    destination=(ROOT/raw.lstrip('/') if raw.startswith('/') else page.parent/unquote(raw)) if raw else page
                    links.append((str(page.relative_to(ROOT)),str(destination.resolve()),unquote(fragment),href))
        key=str(page.resolve());headings[key]=page_headings
        explicit[key]=re.findall(r'<(?:a|h[1-6])\b[^>]*\b(?:id|name)=["\']([^"\']+)',text,re.I)
        if h1s!=1 and page.name not in ('LICENSE.md','LICENSE'):
            h1_issues.append({'page':str(page.relative_to(ROOT)),'h1_count':h1s})
        if number%4000==0:print(f'Parsed {number}/{len(pages)} Markdown documents.',flush=True)
    js="""import fs from 'node:fs';import {pathToFileURL} from 'node:url';const {default:Slugger}=await import(pathToFileURL(process.argv[1]).href);const input=JSON.parse(fs.readFileSync(0,'utf8'));const result={};for(const [page,headings] of Object.entries(input)){const slugger=new Slugger();result[page]=headings.map(text=>slugger.slug(text));}process.stdout.write(JSON.stringify(result));"""
    slugs=json.loads(subprocess.check_output(['node','--input-type=module','-e',js,str(args.slugger_module.resolve())],input=json.dumps(headings),text=True))
    missing=[]
    for page,target,fragment,href in links:
        if target not in slugs:continue # File existence is checked by check_documentation.py.
        if fragment not in slugs[target] and fragment not in explicit.get(target,[]):
            missing.append({'page':page,'target':href})
    previews=[]
    if args.preview_dir:
        args.preview_dir.mkdir(parents=True,exist_ok=True)
        css='body{font:16px/1.6 system-ui,sans-serif;max-width:90rem;margin:auto;padding:2rem;color:#18202a}table{border-collapse:collapse;display:block;overflow:auto}th,td{border:1px solid #ccd4dc;padding:.5rem;vertical-align:top}th{background:#eef3f7}pre{background:#f3f5f7;padding:1rem;overflow:auto}code{font-size:.9em;overflow-wrap:anywhere}a{color:#075b9f}h1,h2,h3{line-height:1.25;margin-top:1.6em}'
        for relative in PREVIEWS:
            path=ROOT/relative
            if not path.exists():continue
            filename=relative.replace('/','--')+'.html'
            output=args.preview_dir/filename
            output.write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(relative)+'</title><style>'+css+'</style><body>'+renderer.render(path.read_text())+'</body></html>')
            previews.append({'source':relative,'preview':str(output)})
    report={'markdown_files_parsed':len(pages),'fragment_links_checked':len(links),'missing_fragments':missing,'h1_issues':h1_issues,'previews':previews,
            'scope':'GFM-like syntax parsed by markdown-it-py; headings use github-slugger plus explicit HTML anchors. This is a rendered-structure/navigation check, not browser visual review, external availability or semantic implementation verification.'}
    args.report.write_text(json.dumps(report,indent=2)+'\n')
    print(f'Parsed {len(pages)} Markdown files; checked {len(links)} fragments: {len(missing)} missing; {len(h1_issues)} unexpected H1 counts; wrote {len(previews)} previews.')
    for item in missing[:20]:print(item)
    if missing or h1_issues:raise SystemExit(1)


if __name__=='__main__':
    main()

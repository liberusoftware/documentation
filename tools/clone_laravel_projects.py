#!/usr/bin/env python3
"""Discover every public organization *-laravel repository and clone missing checkouts."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects',type=Path,default=Path('/home/liberu/projects'))
    parser.add_argument('--list-only',action='store_true',help='Refresh discovery snapshots without cloning')
    args=parser.parse_args()
    args.projects.mkdir(parents=True,exist_ok=True)
    repositories=[]
    page=1
    while True:
        request=urllib.request.Request(f'https://api.github.com/orgs/liberusoftware/repos?per_page=100&page={page}',headers={'Accept':'application/vnd.github+json','User-Agent':'liberu-documentation-source-discovery'})
        with urllib.request.urlopen(request,timeout=30) as response:
            data=json.load(response)
        if not isinstance(data,list):
            raise SystemExit('GitHub repository listing did not return an array')
        repositories.extend({key:r[key] for key in ('name','clone_url','default_branch','archived')} for r in data if r['name'].endswith('-laravel'))
        print(f'Discovery page {page}: {len(data)} public repositories, {len(repositories)} matching so far.',flush=True)
        if len(data)<100:
            break
        page+=1
    repositories=sorted(repositories,key=lambda r:r['name'])
    # Write only after every page succeeded; a failed discovery never replaces a complete input.
    encoded=json.dumps(repositories,indent=2)+'\n'
    (args.projects/'repositories.json').write_text(encoded)
    (ROOT/'architecture/source-repositories.json').write_text(encoded)
    if args.list_only:
        print(f'Discovered {len(repositories)} matching repositories across {page} complete API pages; no clones changed.')
        return
    def clone(record):
        destination=args.projects/record['name']
        if destination.exists():
            if not (destination/'.git').exists():
                raise RuntimeError(f'{destination}: existing destination is not a Git checkout')
            return f'{record["name"]}: existing checkout preserved'
        process=subprocess.run(['git','clone','--depth','1',record['clone_url'],str(destination)],capture_output=True,text=True)
        if process.returncode:
            raise RuntimeError(f'{record["name"]}: clone failed: {process.stderr}')
        return f'{record["name"]}: cloned'
    failures=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures={pool.submit(clone,record):record['name'] for record in repositories}
        for future in as_completed(futures):
            try:
                print(future.result(),flush=True)
            except Exception as error:
                failures.append(str(error))
                print(str(error),flush=True)
    if failures:
        raise SystemExit(f'{len(failures)} clones failed; existing checkouts were preserved')
    print(f'All {len(repositories)} matching repositories have checkouts under {args.projects}.')


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Prepare detached source worktrees at inventory commits, preserving active project edits."""
import argparse
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]


def git(repo,*args):
    return subprocess.check_output(['git','-C',str(repo),*args],text=True).strip()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects',type=Path,default=Path('/home/liberu/projects'))
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    records=json.loads((ROOT/'architecture/source-inventory.json').read_text())['repositories']
    for record in records:
        source=args.projects/record['repository'];target=args.output/record['repository']
        if target.resolve().is_relative_to(source.resolve()):
            raise SystemExit(f'{target}: snapshot must not be inside the active source checkout')
        if target.exists():
            if git(target,'rev-parse','HEAD')!=record['commit'] or git(target,'status','--porcelain'):
                raise SystemExit(f'{target}: existing snapshot differs; choose a fresh output directory')
        else:
            process=subprocess.run(['git','-C',str(source),'worktree','add','--detach',str(target),record['commit']],capture_output=True,text=True)
            if process.returncode:raise SystemExit(f'{record["repository"]}: snapshot failed: {process.stderr}')
        assert git(target,'rev-parse','HEAD')==record['commit']
        assert not git(target,'status','--porcelain')
        print(f'{record["repository"]}: detached snapshot at {record["commit"][:12]}',flush=True)
    discovery=json.loads((ROOT/'architecture/source-repositories.json').read_text())
    (args.output/'repositories.json').write_text(json.dumps(discovery,indent=2)+'\n')
    print(f'Prepared {len(records)} clean pinned source views; active source files/branches were preserved.')


if __name__=='__main__':main()

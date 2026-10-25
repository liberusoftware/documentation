#!/usr/bin/env python3
"""Repair local links whose standard filename label points to a different file."""
import argparse
from collections import Counter
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[([^\]\n]+)\]\(([^)\n]+)\)')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report mismatches without modifying files')
    args = parser.parse_args()
    counts = Counter()
    files = 0
    standards = {p.name: p for p in (ROOT / 'standards').glob('*.md')}
    standards.update({p.name: p for p in (ROOT / 'architecture').glob('*.md')})
    for path in sorted((ROOT / 'projects').rglob('*.md')):
        original = path.read_text()

        def replace(match):
            label, target = match.groups()
            name = label.removeprefix('architecture/').removeprefix('standards/')
            if name not in standards or '://' in target or target.startswith(('#', 'mailto:')):
                return match.group(0)
            destination = target.split('#', 1)[0]
            if (path.parent / destination).resolve().name == name:
                return match.group(0)
            # Only resolve unambiguous filename labels. Product references and prose labels stay intact.
            counts[name] += 1
            relative = os.path.relpath(standards[name], path.parent)
            return f'[{label}]({relative})'

        result = LINK.sub(replace, original)
        if result != original:
            files += 1
            if not args.check:
                path.write_text(result)
    print(f'{"Found" if args.check else "Repaired"} {sum(counts.values())} standard links in {files} files.')
    for name, count in sorted(counts.items()):
        print(f'  {name}: {count}')
    if args.check and counts:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

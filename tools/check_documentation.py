#!/usr/bin/env python3
"""Check repository Markdown file links and preservation of the Ecommerce catalogue."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, help='Write missing local targets as JSON')
    args = parser.parse_args()
    missing = []
    checked = 0
    pages = sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts)
    for page in pages:
        content = page.read_text()
        # Example Markdown embedded in code fences is not a rendered navigation link.
        content = re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', content, flags=re.M | re.S)
        for match in re.finditer(r'!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', content):
            target = match.group(1).strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith(('#', '//')):
                continue
            path = unquote(target.split('#', 1)[0].split('?', 1)[0])
            if not path:
                continue
            checked += 1
            destination = ROOT / path.lstrip('/') if path.startswith('/') else page.parent / path
            if not destination.exists():
                missing.append({'page': str(page.relative_to(ROOT)), 'target': target,
                                'line': content[:match.start()].count('\n') + 1})
    baseline = subprocess.check_output(['git', '-C', str(ROOT), 'ls-tree', '-r', '--name-only', 'HEAD', '--', 'projects/ecommerce', 'user-guides/projects/ecommerce'], text=True).splitlines()
    removed = [p for p in baseline if not (ROOT / p).is_file()]
    result = {'markdown_files': len(pages), 'local_links_checked': checked,
              'missing_targets': missing, 'removed_ecommerce_files': removed,
              'scope': 'Inline Markdown local file links outside fenced examples; heading anchors, reference-style links, external links and rendered layout require separate review.'}
    if args.report:
        args.report.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Checked {len(pages)} Markdown files and {checked} local file links; {len(missing)} missing targets.')
    print(f'Ecommerce catalogue preservation: {len(baseline)} existing files checked, {len(removed)} removed.')
    counts = Counter(item['target'] for item in missing)
    for target, count in counts.most_common(20):
        print(f'  {count} missing: {target}')
    if missing or removed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

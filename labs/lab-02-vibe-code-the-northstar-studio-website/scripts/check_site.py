#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else 'working-site')
checks={'index.html': ['<main','<nav','<form','aria-label','role="status"'],'styles.css':['@media',':focus-visible','grid-template-columns'],'script.js':['preventDefault','checkValidity']}
failed=[]
for name,needles in checks.items():
    text=(root/name).read_text(encoding='utf-8') if (root/name).exists() else ''
    for n in needles:
        if n not in text: failed.append(f'{name}: missing {n}')
print('PASS' if not failed else 'FAIL')
for item in failed: print('-',item)
raise SystemExit(bool(failed))

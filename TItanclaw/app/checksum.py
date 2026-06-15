from __future__ import annotations
import argparse, hashlib
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    p = Path(a.file)
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    Path(a.out).write_text(f"{digest}  {p.name}\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations
import argparse, hashlib
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--sha", required=True)
    a = ap.parse_args()
    p = Path(a.file)
    expected = Path(a.sha).read_text().split()[0].strip()
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(2)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

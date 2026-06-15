from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root = Path(a.root)
    files = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and "output" not in p.parts:
            files.append({"path": p.relative_to(root).as_posix(), "size": p.stat().st_size, "sha256": sha256(p)})
    Path(a.out).write_text(json.dumps({"root": str(root), "files": files}, indent=2) + "\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations
import argparse, tarfile
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root = Path(a.root)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(out, "w:gz") as tf:
        for rel in ["app", "README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md", ".gitignore", "build.sh", "deploy.sh"]:
            tf.add(root / rel, arcname=rel, recursive=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

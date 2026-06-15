from __future__ import annotations
import argparse, os, tarfile
from pathlib import Path

def safe_path(base: Path, target: Path) -> bool:
    base = base.resolve()
    target = target.resolve()
    return str(target) == str(base) or str(target).startswith(str(base) + os.sep)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tar", required=True)
    ap.add_argument("--dest", required=True)
    a = ap.parse_args()
    dest = Path(a.dest)
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(a.tar, "r:gz") as tf:
        for m in tf.getmembers():
            target = dest / m.name
            if not safe_path(dest, target):
                raise SystemExit(3)
            if m.issym() or m.islnk():
                raise SystemExit(4)
        tf.extractall(dest)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

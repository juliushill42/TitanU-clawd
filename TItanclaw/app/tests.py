from __future__ import annotations
import json, subprocess, sys

def main() -> int:
    out = subprocess.check_output([sys.executable, "app/main.py", "--healthcheck"], text=True)
    data = json.loads(out)
    assert data["status"] == "ok"
    assert data["service"] == "openclaw-monolith"
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

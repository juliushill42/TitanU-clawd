from __future__ import annotations
import argparse, json, os

def healthcheck() -> dict:
    return {"status": "ok", "service": "openclaw-monolith", "pid": os.getpid()}

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--healthcheck", action="store_true")
    a = p.parse_args()
    if a.healthcheck:
        print(json.dumps(healthcheck(), sort_keys=True))
    else:
        print(json.dumps({"service": "openclaw-monolith"}, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

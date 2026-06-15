#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="$ROOT_DIR/output/openclaw-monolith"
DIST_DIR="$OUT_DIR/dist"
LOG_DIR="$OUT_DIR/logs"
AUDIT_DIR="$OUT_DIR/audit"
mkdir -p "$DIST_DIR" "$LOG_DIR" "$AUDIT_DIR"
exec > >(tee "$LOG_DIR/build.log") 2>&1
python3 "$ROOT_DIR/app/tests.py"
python3 "$ROOT_DIR/app/record.py" --root "$ROOT_DIR" --out "$AUDIT_DIR/manifest.json"
python3 "$ROOT_DIR/app/package.py" --root "$ROOT_DIR" --out "$DIST_DIR/openclaw-monolith.tar.gz"
python3 "$ROOT_DIR/app/checksum.py" --file "$DIST_DIR/openclaw-monolith.tar.gz" --out "$DIST_DIR/openclaw-monolith.sha256"
printf 'build complete\n'

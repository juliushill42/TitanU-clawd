#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="$ROOT_DIR/output/openclaw-monolith"
DIST_DIR="$OUT_DIR/dist"
DEPLOY_DIR="$OUT_DIR/deploy/current"
LOG_DIR="$OUT_DIR/logs"
mkdir -p "$LOG_DIR"
exec > >(tee -a "$LOG_DIR/deploy.log") 2>&1
python3 "$ROOT_DIR/app/verify.py" --file "$DIST_DIR/openclaw-monolith.tar.gz" --sha "$DIST_DIR/openclaw-monolith.sha256"
rm -rf "$DEPLOY_DIR"
mkdir -p "$DEPLOY_DIR"
python3 "$ROOT_DIR/app/safe_extract.py" --tar "$DIST_DIR/openclaw-monolith.tar.gz" --dest "$DEPLOY_DIR"
python3 "$DEPLOY_DIR/app/main.py" --healthcheck
printf 'deployed to %s\n' "$DEPLOY_DIR"

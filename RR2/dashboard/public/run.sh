#!/usr/bin/env bash
# RoadRakshak dashboard launcher.
#   ./run.sh                 -> http://localhost:8090
#   ./run.sh --host 0.0.0.0  -> reachable from other machines
set -euo pipefail
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python  >/dev/null 2>&1; then PY=python
else
  echo "Python 3 not found. Install it:"
  echo "  sudo apt install -y python3      # Debian/Ubuntu"
  echo "  sudo dnf install -y python3      # Fedora/RHEL"
  echo "  sudo pacman -S python            # Arch"
  exit 1
fi
exec "$PY" serve.py "$@"

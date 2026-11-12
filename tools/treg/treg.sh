#!/bin/sh
# Project-scoped treg wrapper. Always uses this repo's login (.treg/config.json)
# and keeps telemetry off, from any directory or terminal.
# Usage: tools/treg/treg.sh <any treg command>   e.g. tools/treg/treg.sh balance
ROOT=$(cd "$(dirname "$0")/../.." && pwd)
export TREG_CONFIG="$ROOT/.treg/config.json"
export TREG_TELEMETRY=0
export DO_NOT_TRACK=1
BIN="${TREG_BIN:-$HOME/.local/bin/treg}"
if [ ! -x "$BIN" ]; then
  echo "treg CLI not found at $BIN. See tools/treg/README.md (Install)." >&2
  exit 1
fi
if [ ! -s "$TREG_CONFIG" ]; then
  echo "Not signed in for this project. Run: TREG_CONFIG=\"$TREG_CONFIG\" $BIN login" >&2
  exit 1
fi
exec "$BIN" "$@"

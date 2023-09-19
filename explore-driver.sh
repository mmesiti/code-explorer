#!/bin/bash --login
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd)"

DIR="$1"
TMPDB=$(mktemp)
cloc --sql=1 "$DIR" | sqlite3 "$TMPDB"

cd "$SRC"
poetry run ./plot-db.py "$TMPDB" $(basename "$DIR").cloc.db.html

#!/bin/bash --login
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd)"

REPO="$1"
DEFAULT_BRANCH="$2"
LOCALDIR=$(mktemp -d)

git clone --branch $DEFAULT_BRANCH --depth=1 $REPO $LOCALDIR

TMPDB=$(mktemp)
cloc --sql=1 "$LOCALDIR" | sqlite3 "$TMPDB"

cd "$SRC"
poetry run ./plot-db.py "$TMPDB" $(basename "$LOCALDIR").cloc.db.html $REPO $LOCALDIR $DEFAULT_BRANCH

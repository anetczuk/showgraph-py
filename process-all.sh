#!/bin/bash

set -eu


## works both under bash and sh
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")


if [ -f "$SCRIPT_DIR/doc/generate-doc.sh" ]; then
    "$SCRIPT_DIR"/doc/generate-doc.sh
fi

if [ -f "$SCRIPT_DIR/examples/generate-all.sh" ]; then
    echo "generating examples results"
    "$SCRIPT_DIR"/examples/generate-all.sh --venv
fi

$SCRIPT_DIR/src/testshowgraph/runtests.py

$SCRIPT_DIR/tools/checkall.sh


echo "processing completed"

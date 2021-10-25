#!/usr/bin/env bash
set -e

run() {
    if [[ $1 =~ .*.py$ ]]; then
        PYLINTHOME=/tmp pylint $1
    fi
}

task() {
    echo "Running Pylint"

    foreach_changed_file run
}

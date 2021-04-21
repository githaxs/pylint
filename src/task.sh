#!/usr/bin/env bash
set -e

exit_code=0

run_pylint() {
    if [[ $1 =~ .*.py$ ]]; then
        pylint $1
        # If any checks fail we want the entire task to fail
        ret=$?
        (( exit_code += $ret ))
    fi
}
task() {
    foreach_changed_file run_pylint

    exit $exit_code
}
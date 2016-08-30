#!/usr/bin/env bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set some environmental variables here
# export PYTHONPATH=$CURDIR

COMMAND="$1"

if [ "$COMMAND" = "run" ]
then
    python app.py

elif [ "$COMMAND" = "test" ]
then
    python tests/simple_test.py

elif [ "$COMMAND" = "build_ui" ]
then
    pyside-uic resources/main_window.ui -o ui/main_window.py

else
    echo "Command is unknown"
fi

#!/usr/bin/env bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set some environmental variables here
export PYTHONPATH=/Applications//Shotgun.app/Contents/Resources/Python/lib/python2.7/site-packages/

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
    pyside-uic resources/drop_area.ui -o ui/drop_area.py

    pyside-rcc resources/icons.qrc -o ui/icons_rc.py

else
    echo "Command is unknown"
fi

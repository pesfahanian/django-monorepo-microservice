#!/bin/bash

set -e

here=`pwd`

if [ "$1" = "--all" -o "$1" = "-A" ]; then
    services=`ls ./service`
    for service in $services
    do
        echo "$here"
        gnome-terminal --title="${service^} Service" -x sh -c \
            "python $here/service/$service/manage.py ${@:2}"
    done
else
    gnome-terminal --title="${1^} Service" -- \
        python $here/service/$1/manage.py ${@:2}
fi

#!/bin/bash

set -e

here=`pwd`

if [ "$2" = "--all" -o "$2" = "-A" ]; then
    services=`ls ./service`
    for service in $services
    do
        gnome-terminal --title="${service^} Service" -- \
            ./service/$service/scripts/$1.sh $here/service/$service
    done
else
    gnome-terminal --title="${1^} Service" -- \
        ./service/$2/scripts/$1.sh $here/service/$2
fi

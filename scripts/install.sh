#!/bin/bash

set -e

here=`pwd`

pip install -r requirements.txt

# TODO: Error if the first argument is empty.

if [ "$1" = "--all" -o "$1" = "-A" -o "$1" = "" ]; then
    services=`ls ./service`
    for service in $services
    do
        pip install -r $here/service/$service/requirements.txt
    done
else
    pip install -r $here/service/$1/requirements.txt
fi

if [ "$2" = "--dev" -o "$2" = "-D" ]; then
    pip install -r requirements.dev.txt
fi

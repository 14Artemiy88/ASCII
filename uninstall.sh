#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root"
    exit 1
fi

usrBinScriptPath="/usr/local/bin/ascii"
pythonPath='/usr/local/lib/python3.10/dist-packages/ascii'

rm $usrBinScriptPath
rm -r $pythonPath
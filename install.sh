#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root"
    exit 1
fi

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 || exit ; pwd -P )"

#ln -s "$SCRIPTPATH/ascii" '/usr/local/lib/python3.10/dist-packages/ascii'
mkdir -p '/usr/local/lib/python3.11/dist-packages/ascii'
cp -r "$SCRIPTPATH/ascii" '/usr/local/lib/python3.10/dist-packages'

usrBinScriptPath="/usr/local/bin/ascii"
bash -c "echo '#!/usr/bin/python3' >> $usrBinScriptPath"
bash -c "echo '# -*- coding: utf-8 -*-' >> $usrBinScriptPath"
bash -c "echo 'import sys' >> $usrBinScriptPath"
bash -c "echo 'from ascii.main import main' >> $usrBinScriptPath"
bash -c "echo 'if __name__ == \"__main__\":' >> $usrBinScriptPath"
bash -c "echo '    sys.exit(main())' >> $usrBinScriptPath"

chmod +x $usrBinScriptPath
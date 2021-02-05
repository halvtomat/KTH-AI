# /bin/bash

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
. /usr/local/bin/virtualenvwrapper.sh
workon fishingderby
python3 main.py settings.yml
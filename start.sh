#!/bin/bash

ENV_NAME="venv"

source $ENV_NAME/Scripts/activate

py -3.10 -m pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    py -3.10 -m pip install -r requirements.txt
else
    echo "Arquivo requirements.txt não encontrado."
    deactivate
    exit 1
fi

py -3.10 -m loop
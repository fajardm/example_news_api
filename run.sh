#!/usr/bin/env bash

sleep 30s

export FLASK_APP=run.py && flask db init && flask db migrate && flask db upgrade

python run.py
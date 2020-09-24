#!/bin/bash
echo $(cd $(dirname $0) && pwd)
python3 app.py
sh run.sh
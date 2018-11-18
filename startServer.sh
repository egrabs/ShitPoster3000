#!/bin/bash
export PYTHONPATH=${PYTHONPATH}:${PWD}
export FLASK_APP=ShitPoster3000Server.py
export FLASK_ENV=development
flask run
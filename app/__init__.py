#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

"""
Copyright 2020 Tianyun Zhang

Initialization of the flask server application.
From https://github.com/gtalarico/flask-vuejs-template/ (MIT License)
"""

import os
from flask import Flask, current_app, send_file
from flask_cors import CORS
from .config import Config

app = Flask(__name__, static_folder='../dist/static')
app.config.from_object(Config)

if app.config['FLASK_ENV'] == 'development':
    cors = CORS(app)  # enable CORS for developing env

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)

#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

"""
Copyright 2020 Tianyun Zhang

Initialization of the flask server application.
From https://github.com/gtalarico/flask-vuejs-template/ (MIT License)
"""

from flask import Flask
from .config import Config
from .data.database import db
from .data.database.db import get_db
from .data.model import music


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(music.bp)


@app.route('/')
def index():
    return 'Home Page'


@app.route('/hello')
def hello():
    return 'Hello World'


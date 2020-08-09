#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

"""
Copyright 2020 Tianyun Zhang

Initialization of the flask server application.
From https://github.com/gtalarico/flask-vuejs-template/ (MIT License)
"""

from flask import Flask
from flask_cors import CORS
from .config import Config
from .data.database import db
from .data.database.db import get_db
from .data.model import music
from .data.model import player
from .data.model import practice
from .data.model import artist

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(music.bp)
app.register_blueprint(practice.bp)
app.register_blueprint(player.bp)
app.register_blueprint(artist.bp)

if app.config['FLASK_ENV'] == 'development':
    """
    We need to enable CORS header in development environment, as the host of
    client-side and server-side differs. Besides, Access-Control-Allow-Credentials
    header must be set to make session and user authentication work.
    """
    CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return 'Home Page'


@app.route('/hello')
def hello():
    return 'Hello World'


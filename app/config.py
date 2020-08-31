#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

"""
Copyright 2020 Tianyun Zhang

Configuration the flask server application.
From https://github.com/gtalarico/flask-vuejs-template/ (MIT License)
"""

import os


class Config(object):
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    SECRET_KEY = os.getenv('FLASK_SECRET', 'secret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')
    DATABASE = 'tracelog'

    if not os.path.exists(DIST_DIR):
        raise Exception('DIST_DIR not found: {}'.format(DIST_DIR))

#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

"""
Copyright 2020 Tianyun Zhang

Main entry point of the web server program.
From https://github.com/gtalarico/flask-vuejs-template/ (MIT License)
"""

from app import app

if __name__ == '__main__':
    app.run(port=5000)

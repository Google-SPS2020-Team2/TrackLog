#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

"""
Copyright 2020 Tianyun Zhang

Initialization of the flask server application.
From https://github.com/gtalarico/flask-vuejs-template/ (MIT License)
"""

import json
from flask import Flask
from flask import request
from flask import flash
from flask import url_for
from .config import Config
from flask import redirect
from .data.database import db
from .data.database.db import get_db
from .data.json.encoder import ComplexEncoder as encoder


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route("/show")
def show():
    cur = (get_db().cursor().execute("SELECT * FROM music"))
    my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    return json.dumps(my_query, cls=encoder)


@app.route("/add", methods=("GET", "POST"))
def add():
    """Create a new post for the current user."""
    if request.method == "POST":
        music_name = request.form["music_name"]
        artist_id = request.form["artist_id"]
        difficulty = request.form["difficulty"]
        error = None

        if not music_name:
            error = "Music name is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO music (music_name, artist_id, difficulty) VALUES (?, ?, ?)",
                (music_name, artist_id, difficulty),
            )
            db.commit()
            return redirect(url_for("hello"))  # TODO change the url

    return redirect(url_for("hello"))  # TODO change the url


@app.route('/add_test')  # just for test
def add_test():
    get_db().execute("INSERT INTO music (music_name) VALUES ('See you again')")
    get_db().commit()
    return 'Cur'


@app.route("/delete", methods=("GET", "POST"))
def delete():
    """Delete a post.
    """
    if request.method == "POST":
        music_name = request.form["music_name"]
    else:  # just for test
        music_name = 'See you again'
    db = get_db()
    db.execute("DELETE FROM music WHERE music_name = ?", (music_name,))
    db.commit()

    return redirect(url_for("hello"))  # TODO change the url

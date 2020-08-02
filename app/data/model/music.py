from flask import Blueprint
import json
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from app.data.database.db import get_db
from app.data.json.encoder import ComplexEncoder as encoder

bp = Blueprint("music", __name__)


@bp.route("/show")
def show():
    cur = (get_db().cursor().execute(
        "select id,created,music_name,artist_id,difficulty,\
        (case when id in (select music_id from practice) then 1\
        else 0\
        end) as played \
        from music"
    ))
    my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    return json.dumps(my_query, cls=encoder)

@bp.route("/add", methods=("GET", "POST"))
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
            cur = (get_db().cursor().execute("SELECT * FROM music where music_name=?", (music_name,)))
            if len(cur.fetchall()) != 0:
                return "Music named "+music_name+" already exists"
            else:
                db = get_db()
                db.execute(
                    "INSERT INTO music (music_name, artist_id, difficulty) VALUES (?, ?, ?)",
                    (music_name, artist_id, difficulty),
                )
                db.commit()
                return redirect(url_for("hello"))  # TODO change the url

    return redirect(url_for("hello"))  # TODO change the url


@bp.route('/add_test')  # just for test
def add_test():
    cur = (get_db().cursor().execute("SELECT * FROM music where music_name='See you again'"))
    if len(cur.fetchall())!=0:
        return "Music named 'See you again' already exists"
    else:
        get_db().execute("INSERT INTO music (music_name) VALUES ('See you again')")
        get_db().commit()
        return 'Add a music successfully'


@bp.route("/delete", methods=("GET", "POST"))
def delete():
    """Delete a music.
    """
    if request.method == "POST":
        music_name = request.form["music_name"]
    else:  # just for test
        music_name = 'See you again'
    db = get_db()
    db.execute("DELETE FROM music WHERE music_name = ?", (music_name,))
    db.commit()

    return redirect(url_for("hello"))  # TODO change the url


class Music(object):
    def __init__(self, music_name, duration, artist_id, difficulty):
        self.music_name = music_name
        self.duration = duration
        self.artist_id = artist_id
        self.difficulty = difficulty

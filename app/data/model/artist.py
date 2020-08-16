from flask import Blueprint
import json
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from app.data.database.db import get_db
from app.data.json.encoder import ComplexEncoder as encoder

bp = Blueprint("artist", __name__,url_prefix='/api')


@bp.route("/get_artist_info")
def show():
    error=None
    id = request.args.get("id")
    if not id:
        error = "Artist ID is required."
    if error is not None:
        flash(error)
    else:
        cur = (get_db().cursor().execute(
            "select artist_name,introduction\
            from artist\
            where id="+str(id)
        ))
        my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return json.dumps(my_query, cls=encoder,ensure_ascii=False)


@bp.route("/show_artist")
def show_artist():
    cur = (get_db().cursor().execute(
        "select id, artist_name from artist"
    ))
    my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    return json.dumps(my_query, ensure_ascii=False, cls=encoder)


@bp.route("/add_artist", methods=("GET", "POST"))
def add_artist():
    if request.method == "POST":
        jsonData=request.get_json()
        artist_name = jsonData["name"]
        introduction = jsonData["introduction"]
        error = None

        if not artist_name:
            error = "Artist name is required."

        if error is not None:
            flash(error)
        else:
            cur = (get_db().cursor().execute("SELECT * FROM artist where artist_name=?", (artist_name,)))
            if len(cur.fetchall()) != 0:
                return "Artist named " + artist_name + " already exists"
            else:
                db = get_db()
                db.execute(
                    "INSERT INTO artist (artist_name, introduction) VALUES (?, ?)",
                    (artist_name, introduction),
                )
                db.commit()
                return redirect(url_for("hello"))  # TODO change the url
    else:
        cur = (get_db().cursor().execute("SELECT * FROM artist where artist_name='Mozart'"))
        if len(cur.fetchall()) != 0:
            return "Artist named 'Mozart' already exists"
        else:
            get_db().execute("INSERT INTO artist (artist_name) VALUES ('Mozart')")
            get_db().commit()
            return 'Add a artist successfully'
    return redirect(url_for("hello"))  # TODO change the url


@bp.route("/delete_artist", methods=("GET", "POST"))
def delete_artist():
    if request.method == "POST":
        jsonData=request.get_json()
        artist_name = jsonData["artist_name"]
    else:  # just for test
        artist_name = 'Mozart'
    db = get_db()
    db.execute("DELETE FROM artist WHERE artist_name = ?", (artist_name,))
    db.commit()

    return redirect(url_for("hello"))  # TODO change the url


class Artist(object):
    def __init__(self, artist_id, name, introduction):
        self.artist_id = artist_id
        self.name = name
        self.introduction = introduction

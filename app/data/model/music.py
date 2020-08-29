# -*- coding:utf-8 -*-
from flask import Blueprint
import json
from flask import session
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from app.data.database.db import get_db
from app.data.json.encoder import ComplexEncoder as encoder

bp = Blueprint("music", __name__,url_prefix='/api')


@bp.route("/show")
def show():
    page_index = 1
    page_max_size = 20
    page_size = 20

    if "page" in request.args:
        page_index = int(request.args["page"])

    if "size" in request.args:
        page_max_size = int(request.args["size"])

    cur = get_db().cursor().execute("select count(*) as total_items from music").fetchone()
    total_items = int(cur["total_items"])
    total_pages = int(total_items / page_max_size)
    if total_items % page_max_size > 0:
        total_pages += 1
        if page_index == total_pages:
            page_size = total_items % page_max_size

    if total_items == 0:
        page_index = 0
        page_size = 0

    cur = (get_db().cursor().execute(
        "select id,created,music_name,artist_id,difficulty,(case when id in (select music_id from practice where player_id=" + str(
            session['user_id']) + ") then 1 else 0 end) as played from music limit ? offset ?",
        (page_size, (page_index - 1) * page_max_size))
    )
    my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    res = {'pageIndex': page_index, 'pageSize': page_size, 'totalItems': total_items, 'totalPages': total_pages,
           'items': my_query}
    return json.dumps(res, cls=encoder, ensure_ascii=False)


@bp.route("/add", methods=("GET", "POST"))
def add():
    """Create a new post for the current user."""
    if request.method == "POST":
        jsonData = request.get_json()
        music_name = jsonData["music_name"]
        artist_id = jsonData["artist_id"]
        difficulty = jsonData["difficulty"]
        error = None

        if not music_name:
            error = "Music name is required."

        if error is not None:
            flash(error)
        else:
            cur = (get_db().cursor().execute("SELECT * FROM music where music_name=?", (music_name,)))
            if len(cur.fetchall()) != 0:
                return "Music named " + music_name + " already exists"
            else:
                db = get_db()
                db.execute(
                    "INSERT INTO music (music_name, artist_id, difficulty) VALUES (?, ?, ?)",
                    (music_name, artist_id, difficulty),
                )
                db.commit()
                return redirect(url_for("hello"))  # TODO change the url
    else:
        cur = (get_db().cursor().execute("SELECT * FROM music where music_name='See you again'"))
        if len(cur.fetchall()) != 0:
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
        jsonData=request.get_json()
        music_name = jsonData["music_name"]
    else:  # just for test
        music_name = 'See you again'
    db = get_db()
    db.execute("DELETE FROM music WHERE music_name = ?", (music_name,))
    db.commit()

    return redirect(url_for("hello"))  # TODO change the url

@bp.route("/getCommentAndScore")
def getCommentAndScore():
    error = None
    id = request.args.get("musicId")
    if not id:
        error = "Music ID is required."
    if error is not None:
        flash(error)
    else:
        cur = (get_db().cursor().execute(
            "select music_id,player_id,nickname,score,content \
            from practice,user \
            where user.id=practice.player_id and practice.music_id=" + str(id)
        ))
        my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return json.dumps(my_query, cls=encoder, ensure_ascii=False)

@bp.route("/getAverageScore")
def getAverageScore():
    error = None
    id = request.args.get("musicId")
    if not id:
        error = "Music ID is required."
    if error is not None:
        flash(error)
    else:
        cur = (get_db().cursor().execute(
            "select avg(score) \
            from practice \
            where music_id=" + str(id)
        ))
        my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return json.dumps(my_query, cls=encoder, ensure_ascii=False)

class Music(object):
    def __init__(self, music_name, duration, artist_id, difficulty):
        self.music_name = music_name
        self.duration = duration
        self.artist_id = artist_id
        self.difficulty = difficulty

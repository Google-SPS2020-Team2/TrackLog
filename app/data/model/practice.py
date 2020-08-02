from flask import Blueprint
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from app.data.database.db import get_db

bp = Blueprint("practice", __name__)


@bp.route("/add_practice",methods=("GET", "POST"))
def add_practice():
    """Mark a music piece to have been played"""
    error = None
    if request.method == "POST":
        music_id = request.form["music_id"]
        player_id = request.form["player_id"]
        score = request.form["score"]
        content = request.form["content"]
    else: # for test
        music_id=6
        player_id=0
        score=0
        content="miao"

    if not music_id:
        error = "Music ID is required."

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            "INSERT INTO practice (music_id, player_id, score, content) VALUES (?, ?, ? ,?)",
            (music_id, player_id, score, content),
        )
        db.commit()
        return "Add success!"


@bp.route("/delete_practice", methods=("GET", "POST"))
def delete_practice():
    """Marked a piece of music as not played"""
    if request.method == "POST":
        music_name = request.form["music_id"]
        player_id = request.form["player_id"]
    else:  # just for test
        music_id=6
        player_id=0
    db = get_db()
    db.execute("DELETE FROM practice WHERE music_id = ? and player_id=? ", (music_id,player_id))
    db.commit()
    return "Delete success!"


class Practice(object):
    def __init__(self, practice_id, music_id, player_id, score, content):
        self.practice_id = practice_id
        self.music_id = music_id
        self.player_id = player_id
        self.score = score
        self.content = content

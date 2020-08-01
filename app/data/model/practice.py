from flask import Blueprint

bp = Blueprint("music", __name__)


@bp.route("/add_practice")
def add_practice():
    return ''  # TODO add practice


@bp.route("/delete_practice", methods=("GET", "POST"))
def delete_practice():
    return ''  # TODO add practice


class Practice(object):
    def __init__(self, practice_id, music_id, player_id, score, content):
        self.practice_id = practice_id
        self.music_id = music_id
        self.player_id = player_id
        self.score = score
        self.content = content

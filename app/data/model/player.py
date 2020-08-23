from flask import Blueprint
import json
from flask import request
from flask import flash
from flask import url_for
from flask import redirect
from flask import session
from app.data.database.db import get_db
from app.data.json.encoder import ComplexEncoder as encoder

bp = Blueprint("player", __name__,url_prefix='/api')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    db = get_db()
    if request.method == 'POST':
        jsonData=request.get_json()
        username = jsonData['username']
        nickname = jsonData['nickname']
        password = jsonData['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not nickname:
            error = 'Nickname is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is not None:
            flash(error)
        else:
            db.execute(
                'INSERT INTO user (username, nickname, password) VALUES (?, ?, ?)',
                (username, nickname, password)
            )
            db.commit()
            return redirect(url_for('hello'))  # TODO change the url
    else:  # just for test
        username = 'test'
        nickname = 'test'
        password = 'test'
        db.execute('INSERT INTO user (username, nickname, password) VALUES (?, ?, ?)',
                (username, nickname, password))
        db.commit()
        return "Add success!"


@bp.route('/login', methods=('GET', 'POST'))
def login():
    db = get_db()
    if request.method == 'POST':
        jsonData=request.get_json()
        username = jsonData['username']
        password = jsonData['password']
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not user['password'] == password:
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('hello'))

        flash(error)
    else:  # just for test
        username = 'test'
        password = 'test'
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if user is None:
            error = 'Incorrect username.'
        elif not user['password'] == password:
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))  # TODO change the url

        flash(error)
        return error  # TODO change the url


@bp.route('/status')
def status():
    db = get_db()
    error = None
    if session['user_id'] is None:
        error = "Not log in"
    if error is None:
        user = db.execute(
            'SELECT * FROM user WHERE id = ?', (session['user_id'],)
        ).fetchone()
        res = {'username': user['username'], 'nickname': user['nickname']}
        return json.dumps(res, ensure_ascii=False, cls=encoder)
    flash(error)
    return error  # TODO change the url


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('hello'))  # TODO change the url


@bp.route("/add_favourite",methods=("GET", "POST"))
def add_favourite():
    error = None
    if request.method == "POST":
        jsonData=request.get_json()
        music_id = jsonData["music_id"]
        user_id = session['user_id']
    else: # for test
        music_id = 6
        user_id = 1

    if not music_id:
        error = "Music ID is required."

    if not user_id:
        error = "User ID is required."

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            "INSERT INTO favourite (user_id, music_id) VALUES (? ,?)", (user_id, music_id),)
        db.commit()
    return "Add success!"


@bp.route("/delete_favourite", methods=("GET", "POST"))
def delete_favourite():
    if request.method == "POST":
        jsonData = request.get_json()
        music_id = jsonData["music_id"]
        user_id = session['user_id']
    else:  # just for test
        music_id = 6
        user_id = 1
    db = get_db()
    db.execute("DELETE FROM favourite WHERE music_id = ? and user_id = ? ", (music_id, user_id))
    db.commit()
    return "Delete success!"


@bp.route("/show_favourite")
def show_favourite():
    jsonData = request.get_json()
    page_index = 1
    page_max_size = 20
    page_size = 20


    if (jsonData is not None) and ("page" in jsonData):
        page_index = int(jsonData["page"])

    if (jsonData is not None) and ("size" in jsonData):
        page_max_size = int(jsonData["size"])

    cur = get_db().cursor().execute("select count(*) as total_items from music where id in (select music_id from favourite where user_id = " + str(session['user_id']) + ")").fetchone()
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
        "select id,created,music_name,artist_id,difficulty,\
        (case when id in (select music_id from practice where player_id="+str(session['user_id']) +
        ") then 1 else 0 end) as played from music where id in (select music_id from favourite where user_id = " + str(session['user_id']) + ") limit ? offset ? ", (page_size, (page_index - 1) * page_max_size)
    ))
    my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    res = {'pageIndex': page_index, 'pageSize': page_size, 'totalItems': total_items, 'totalPages': total_pages,
           'items': my_query}
    return json.dumps(res, cls=encoder)


class Player(object):
    def __init__(self, player_id, name, nickname, password):
        self.player_id = player_id
        self.name = name
        self.nickname = nickname
        self.password = password

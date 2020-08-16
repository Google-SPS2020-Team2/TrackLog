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


class Player(object):
    def __init__(self, player_id, name, nickname, password):
        self.player_id = player_id
        self.name = name
        self.nickname = nickname
        self.password = password

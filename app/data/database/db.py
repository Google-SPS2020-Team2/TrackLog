# -*- coding:utf-8 -*-
import sqlite3
import click
import requests
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('TraceLog', detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        g.db.text_factory = str

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def add_song(song_name, artist):
    # for chinese
    song_name = str(song_name).encode().decode('utf-8')
    artist = str(artist).encode().decode('utf-8')

    db = get_db()
    cur = db.cursor().execute("select id from artist where artist_name = ?", (artist,)).fetchone()
    if cur is None:
        db.execute('INSERT INTO artist (artist_name, introduction) VALUES (?, ?)', (artist, ''))
        db.commit()
        cur = db.cursor().execute("select id from artist where artist_name = ?", (artist,)).fetchone()
    artist_id = int(cur['id'])
    cur = db.cursor().execute("select id from music where music_name = ?", (song_name, )).fetchone()
    if cur is None:
        db.execute('INSERT INTO music (music_name, artist_id) VALUES (?, ?)', (song_name, artist_id))
        db.commit()


def init_db():
    db = get_db()

    with current_app.open_resource('./data/database/schema.sql') as f:
        # print(f.read().decode('utf8'))
        db.executescript(f.read().decode('utf8'))

    # init song book
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    name = '钢琴古典'
    page = 300
    for x in range(page):
        params = {
            'ct': '24',
            'qqmusic_ver': '1298',
            'new_json': '1',
            'remoteplace': 'sizer.yqq.song_next',
            'searchid': '64405487069162918',
            't': '0',
            'aggr': '1',
            'cr': '1',
            'catZhida': '1',
            'lossless': '0',
            'flag_qc': '0',
            'p': str(x + 1),
            'n': '20',
            'w': name,
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
        }
        res = requests.get(url, params=params)
        json = res.json()
        list = json['data']['song']['list']
        for music in list:
            song_name = music['name']
            artist = music['singer'][0]['name']
            add_song(song_name, artist)
        print("init progress:" + str((x + 1)) + "/" + str(page))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


if __name__ == '__main__':
    init_db()


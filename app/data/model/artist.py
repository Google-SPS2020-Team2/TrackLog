@bp.route("/get_artist_info",methods=("GET", "POST"))
def show():
    if request.method == "POST":
        error=None
        jsonData = request.get_json()
        id = jsonData["id"]
        if not id:
            error = "Artist ID is required."
        if error is not None:
            flash(error)
        else:
            cur = (get_db().cursor().execute(
                "select name,introduction\
                from artist\
                where id="+str(id)
            ))
            my_query = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            return json.dumps(my_query, cls=encoder)

class Artist(object):
    def __init__(self, artist_id, name, introduction):
        self.artist_id = artist_id
        self.name = name
        self.introduction = introduction

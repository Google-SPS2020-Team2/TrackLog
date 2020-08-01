class Player(object):
    def __init__(self, player_id, name, nickname):
        self.player_id = player_id
        self.name = name
        self.nickname = nickname
        self.favor_list = {}
        self.played_music_history = {}

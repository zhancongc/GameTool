from . import db


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode(128))

    def __repr__(self):
        return 'Game: {0}'.format(self.name)


class Server(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    version = db.Column(db.Unicode(32))
    language = db.Column(db.Unicode(32))
    host = db.Column(db.Unicode(128))
    socket_port = db.Column(db.Integer)
    http_port = db.Column(db.Integer)

    def __repr__(self):
        return '<Server: {0} {1} {2} {3}>'.format(self.game_id, self.version, self.language, self.host)

from . import db


class Game(db.Model):
    __tablename__ = 'games'
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_name = db.Column(db.Unicode(128))
    game_version = db.Column(db.Unicode(32))
    country = db.Column(db.Unicode(32))
    server = db.relationship('Server', backref='game', lazy='dynamic')

    def __repr__(self):
        return 'Game {0}'.format(self.game_name)


class Server(db.Model):
    __tablename__ = 'servers'
    server_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game_id'))
    game_version = db.Column(db.Unicode(32), db.ForeignKey('game_version'))
    country = db.Column(db.Unicode(32), db.ForeignKey('country'))
    ip_address = db.Column(db.Unicode(128))
    socket_port = db.Column(db.Integer)
    http_port = db.Column(db.Integer)

    def __repr__(self):
        return '<Server {0} {1}>'.format(self.game_id, self.game_version)


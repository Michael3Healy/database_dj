"""Models for Playlist app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.init_app(app)


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    description = db.Column(db.Text, nullable=False)

    songs = db.relationship('Song', secondary='playlists_songs', backref='playlists')


class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text, nullable=False)

    artist = db.Column(db.Text, nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlists_songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    playlist_id = db.Column(db.ForeignKey('playlists.id', ondelete='CASCADE'), nullable=False)

    song_id = db.Column(db.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)




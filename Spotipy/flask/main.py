import json
import os

from flask import Flask

from Spotipy import ManagerConstants
from Spotipy.spotipy import Spotipy


def spotipy_flask_server():
    my_spotipy = Spotipy()
    for file in os.listdir("../" + ManagerConstants.songs_path):
        with open("../" + ManagerConstants.songs_path + "/" + file, "r") as file_fd:
            my_spotipy.song_manager.add_song(json.load(file_fd))

    app = Flask(__name__)

    @app.route("/")
    def home():
        return '<html><head><title>Spotipy Home</title></head><body style="background-color: grey;color:white' \
               + ';font-size:10cm">Spotipy</body></html'

    @app.route("/search/artists")
    def get_artists():
        return "<br>".join([artist.name for artist in my_spotipy.search_engine.get_artists()])

    @app.route("/search/artist_album/<id>")
    def get_artist_album(id):
        return "<br>".join([album[1].name for album in my_spotipy.search_engine.get_artist_albums(id)])

    @app.route("/search/artists/popular_songs/<id>")
    def most_popular_songs(id):
        return "<br>".join([song.name for song in my_spotipy.search_engine.get_top_songs(id)])

    @app.route("/search/songs/album/<id>")
    def get_album_songs(id):
        return "<br>".join([song.name for song in my_spotipy.search_engine.get_album_songs(id)])

    app.run(host="0.0.0.0", port=27015, debug=True)


if __name__ == '__main__':
    spotipy_flask_server()

from Spotipy.spotipy import Spotipy


def spotipy_flask_server(spotipy_client: Spotipy):
    from flask import Flask
    from loguru import logger

    logger.debug("Initiating a Spotipy instance...")
    spotipy_client = spotipy_client
    logger.success("Initiated a Spotipy instance!")

    logger.debug("Initiating Flask instance...")
    app = Flask(__name__)
    logger.success("Successfully Initiated a Spotipy instance!")

    @app.route("/")
    def home():
        return '<html><head><title>Spotipy Home</title></head><body style="background-color: grey;color:white' \
               + ';font-size:10cm">Spotipy</body></html'

    @app.route("/search/artists")
    def get_artists():
        logger.debug("Getting artists list from spotipy object...")
        return "<br>".join([artist.name for artist in spotipy_client.search_engine.get_artists()])

    @app.route("/search/artist_album/<id>")
    def get_artist_album(id):
        logger.debug(f"Getting artist's ({id}) albums...")
        return "<br>".join([album[1].name for album in spotipy_client.search_engine.get_artist_albums(id)])

    @app.route("/search/artists/popular_songs/<id>")
    def most_popular_songs(id):
        logger.debug(f"Getting artist's ({id}) list of most popular songs...")
        return "<br>".join([song.name for song in spotipy_client.search_engine.get_top_songs(id)])

    @app.route("/search/songs/album/<id>")
    def get_album_songs(id):
        logger.debug(f"Getting songs from an the album {id} ...")
        return "<br>".join([song.name for song in spotipy_client.search_engine.get_album_songs(id)])

    app.run(host="0.0.0.0", port=27015, debug=True)


if __name__ == '__main__':
    import json
    import os

    from loguru import logger

    from Spotipy import ManagerConstants

    my_spotipy = Spotipy()
    logger.debug("Adding songs to the Spotipy instance...")
    for file in os.listdir("../" + ManagerConstants.songs_path):
        with open("../" + ManagerConstants.songs_path + "/" + file, "r") as file_fd:
            my_spotipy.song_manager.add_song(json.load(file_fd))
    logger.success("Successfully added set of songs!")

    spotipy_flask_server(my_spotipy)

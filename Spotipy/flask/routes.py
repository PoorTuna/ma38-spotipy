from flask import current_app as app


# @app.route("/")
# def home():
#     return '<html><head><title>Spotipy Home</title></head><body style="background-color: grey;color:white' \
#            + ';font-size:10cm">Spotipy</body></html'
#
#
# @app.route("/search/artists")
# def get_artists():
#     return "<br>".join([artist.name for artist in my_spotipy.search_engine.get_artists()])
#
#
# @app.route("/search/artist_album/<id>")
# def get_artist_album(id):
#     return "<br>".join([album[1].name for album in my_spotipy.search_engine.get_artist_albums(id)])
#
#
# @app.route("/search/artists/popular_songs/<id>")
# def most_popular_songs(id):
#     return "<br>".join([song.name for song in my_spotipy.search_engine.get_top_songs(id)])
#
#
# @app.route("/search/songs/album/<id>")
# def get_album_songs(id):
#     return "<br>".join([song.name for song in my_spotipy.search_engine.get_album_songs(id)])
#

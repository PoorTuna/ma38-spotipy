import operator

from Spotipy.core.music.spotipy_song_manager import SpotipySongManager
from Spotipy.config.constants import SearchConstants


class SpotipySearch:
    def __init__(self, song_manager: SpotipySongManager):
        self.song_manager = song_manager

    def get_artists(self):
        return [self.song_manager.artists[artist] for artist in self.song_manager.artists]

    def get_artist_albums(self, artist_id):
        return [self.song_manager.albums[album_id] for album_id in self.song_manager.artists[artist_id].album_ids]

    def get_top_songs(self, artist_id):
        songs_list = []
        for album_id in self.song_manager.artists[artist_id].album_ids:
            for song in self.song_manager.albums[album_id][0]:
                songs_list.append(song)

        return sorted([song for song in songs_list],
                      key=lambda x: x.popularity)[:SearchConstants.most_popular_songs_count]

    def get_album_songs(self, album_id):
        return self.song_manager.albums[album_id][0]

    # TODO : Implement genres (find where is the definition of a song genre??).
    # TODO : Implement get top genre songs function with constant variables
    def get_top_genre_songs(self, genre_name):
        pass

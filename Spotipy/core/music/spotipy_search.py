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

    # def get_top_songs(self):
    #     return sorted([test for test in range(10)],
    #                   key=operator.itemgetter(-1))[:SearchConstants.most_popular_songs_count]

    def get_album_songs(self, album_id):
        return self.song_manager.albums[album_id][0]

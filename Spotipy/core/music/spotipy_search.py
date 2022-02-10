from Spotipy.core.music.spotipy_song_manager import SpotipySongManager
from Spotipy.config.constants import SearchConstants
from loguru import logger

from Spotipy.core.users.spotipy_users.spotipy_free_user import SpotipyFreeUser
from Spotipy.core.users.spotipy_users.spotipy_user_manager import SpotipyUserManager


class SpotipySearch:
    def __init__(self, song_manager: SpotipySongManager, user_manager: SpotipyUserManager):
        self.song_manager = song_manager
        self.user_manager = user_manager

    def get_artists(self):
        logger.debug("Getting artist objects...")
        if isinstance(self.user_manager.current_user.curr_user,
                      SpotipyFreeUser) or self.user_manager.current_user.curr_user is None:
            return [self.song_manager.artists[artist] for artist in self.song_manager.artists][
                   :SearchConstants.free_user_search_limit]

        return [self.song_manager.artists[artist] for artist in self.song_manager.artists]

    def get_artist_albums(self, artist_id: str):
        logger.debug(f"Getting artist's albums from id = {artist_id}...")
        if isinstance(self.user_manager.current_user.curr_user,
                      SpotipyFreeUser) or self.user_manager.current_user.curr_user is None:
            return [self.song_manager.albums[album_id] for album_id in self.song_manager.artists[artist_id].album_ids][
                   :SearchConstants.free_user_search_limit]

        return [self.song_manager.albums[album_id] for album_id in self.song_manager.artists[artist_id].album_ids]

    def get_top_songs(self, artist_id: str):
        logger.debug(logger.debug(f"Getting top songs from artist id = {artist_id}..."))
        songs_list = []
        for album_id in self.song_manager.artists[artist_id].album_ids:
            for song in self.song_manager.albums[album_id][0]:
                songs_list.append(song)
        songs_list = list(dict.fromkeys(songs_list))  # might not be needed?
        logger.success("Got the list filled with the artist's top songs!")
        logger.debug("Sorting the top artist's songs list...")
        if isinstance(self.user_manager.current_user.curr_user,
                      SpotipyFreeUser) or self.user_manager.current_user.curr_user is None:
            return sorted([song for song in songs_list],
                          key=lambda x: x.popularity)[:SearchConstants.most_popular_songs_count][
                   :SearchConstants.free_user_search_limit]

        return sorted([song for song in songs_list],
                      key=lambda x: x.popularity)[:SearchConstants.most_popular_songs_count]

    def get_album_songs(self, album_id: str):
        logger.debug(logger.debug(f"Getting every song from album id = {album_id}..."))
        return self.song_manager.albums[album_id][0]

    # TODO : Implement genres (find where is the definition of a song genre??).
    # TODO : Implement get top genre songs function with constant variables
    def get_top_genre_songs(self, genre_name: str):
        pass

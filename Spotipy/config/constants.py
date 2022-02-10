class UserConstants:
    free_user_playlist_limit = 5
    free_user_playlist_songs_limit = 20


class SearchConstants:
    most_popular_songs_count = 10
    genre_most_popular_songs_count = 10
    free_user_search_limit = 5


class ManagerConstants:
    import os

    from Spotipy.core.exceptions.spotipy_config_exceptions import SpotipyInvalidConfigFile

    logs_path = r"../Resources/Logs/spotipy.log"
    songs_path = r"../Resources/Music/Songs"

    if os.path.exists(r"spotipy.ini"):
        try:
            with open("spotipy.ini", "r") as spotipy_fd:
                logs_path = next(spotipy_fd)
                songs_path = next(spotipy_fd)
        except StopIteration:
            raise SpotipyInvalidConfigFile

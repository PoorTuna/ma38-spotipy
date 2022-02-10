from Spotipy.core.exceptions.spotipy_exception import SpotipyException


class SpotipyMusicPlaylistCountException(SpotipyException):
    pass


class SpotipyMusicPlaylistNameExistsException(SpotipyException):
    pass


class SpotipyInvalidSongFormatException(SpotipyException):
    pass

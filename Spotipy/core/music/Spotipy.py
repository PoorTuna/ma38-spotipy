from typing import Dict

from Spotipy.core.music.album import Album
from Spotipy.core.music.artist import Artist
from Spotipy.core.music.song import Song


class Spotipy:
    def __init__(self):
        self.albums = {}
        self.artists = []

    def add_song(self, dictionary: Dict[str, str]):
        """
        This function takes the dictionary formatted song and converts it into a series of objects.
        :param dictionary: the dictionary formatted song.
        :return: None
        """
        temp_song = Song(dictionary["track"]["id"], dictionary["track"]["name"], dictionary["track"]["popularity"],
                         dictionary["track"]["album"]["id"])

        temp_album = Album(*dictionary["track"]["album"].values())

        for artist in dictionary["track"]["artists"]:
            artist_temp = Artist(*artist)
            artist_temp.album_ids.append(temp_album.album_id)

            temp_song.artists.append(artist_temp)
            self.artists.append(artist_temp)

        self.__add_song(temp_album, temp_song)

    def __add_song(self, album, song):
        if album.album_id in self.albums:
            self.albums[album.album_id][0].append(song)

        else:
            self.albums[album.album_id] = []
            self.albums[album.album_id].append([])  # songs list
            self.albums[album.album_id].append(album.name)

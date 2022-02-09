from typing import Dict

from Spotipy.core.music.album import Album
from Spotipy.core.music.artist import Artist
from Spotipy.core.music.song import Song


class SpotipySongManager:
    def __init__(self):
        self.albums = {}
        self.artists = {}

    def add_song(self, dictionary: Dict[str, str]):
        """
        This function takes the dictionary formatted song and converts it into a series of objects.
        :param dictionary: the dictionary formatted song.
        :return: None
        """
        # TODO : Might have to prevent the same song from being created again (if that's possible)
        temp_song = Song(dictionary["track"]["id"], dictionary["track"]["name"], dictionary["track"]["popularity"],
                         dictionary["track"]["album"]["id"])

        self.__add_album(dictionary["track"]["album"], temp_song)

        for artist in dictionary["track"]["artists"]:
            if artist["id"] not in self.artists:
                self.artists[artist["id"]] = Artist(*artist)

            temp_artist = self.artists[artist["id"]]
            temp_artist.album_ids.append(dictionary["track"]["album"]["id"])

            temp_song.artists.append(temp_artist)

    def __add_album(self, album, song):
        if album["id"] in self.albums:
            self.albums[album["id"]][0].append(song)

        else:
            self.albums[album["id"]] = []
            self.albums[album["id"]].append([song])  # songs list
            self.albums[album["id"]].append(Album(*album.values()))

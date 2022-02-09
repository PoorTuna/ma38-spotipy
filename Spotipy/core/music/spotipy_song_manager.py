from typing import Dict

from Spotipy.core.exceptions.spotipy_music_exceptions import SpotipyInvalidSongFormatException
from Spotipy.core.music.album import Album
from Spotipy.core.music.artist import Artist
from Spotipy.core.music.song import Song


class SpotipySongManager:
    def __init__(self):
        self.albums = {}
        self.artists = {}
        self.songs = {}

    def add_song(self, dictionary: Dict[str, str]):
        """
        This function takes the dictionary formatted song and converts it into a series of objects.
        :param dictionary: the dictionary formatted song.
        :return: None
        """
        # TODO : Might have to prevent the same song from being created again (if that's possible)
        try:
            if dictionary["track"]["id"] not in self.songs:
                self.songs[dictionary["track"]["id"]] = Song(dictionary["track"]["id"], dictionary["track"]["name"],
                                                             dictionary["track"]["popularity"],
                                                             dictionary["track"]["album"]["id"])

            temp_song = self.songs[dictionary["track"]["id"]]

            self.__add_album(dictionary["track"]["album"], temp_song)

            for artist in dictionary["track"]["artists"]:
                if artist["id"] not in self.artists:
                    self.artists[artist["id"]] = Artist(*artist.values())

                temp_artist = self.artists[artist["id"]]
                if dictionary["track"]["album"]["id"] not in temp_artist.album_ids:
                    temp_artist.album_ids.append(dictionary["track"]["album"]["id"])

                if temp_artist not in temp_song.artists:
                    temp_song.artists.append(temp_artist)
        except KeyError:
            raise SpotipyInvalidSongFormatException

    def __add_album(self, album, song):
        if album["id"] in self.albums:
            if song.name not in [song_name.name for song_name in self.albums[album["id"]][0]]:
                self.albums[album["id"]][0].append(song)
            else:
                print("already exists")
        else:
            self.albums[album["id"]] = []
            self.albums[album["id"]].append([song])  # songs list
            self.albums[album["id"]].append(Album(*album.values()))

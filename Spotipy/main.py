def main():
    my_spotipy = Spotipy()

    for file in os.listdir(ManagerConstants.songs_path):
        with open(ManagerConstants.songs_path + "/" + file, "r") as file_fd:
            my_spotipy.song_manager.add_song(json.load(file_fd))
    for artist in my_spotipy.song_manager.artists:
        # print(my_spotipy.song_manager.artists[artist].name)
        pass

    print([(artist.artist_id, artist.name) for artist in my_spotipy.search_engine.get_artists()])
    print([(song.name, song.popularity) for song in my_spotipy.search_engine.get_top_songs("2l6M7GaS9x3rZOX6nDX3CM")])

    for item in my_spotipy.search_engine.get_artist_albums("2l6M7GaS9x3rZOX6nDX3CM"):
        for song in item[0]:
            # print(song.name)
            pass


if __name__ == '__main__':
    import json
    import os

    from Spotipy.config.constants import ManagerConstants
    from Spotipy.spotipy import Spotipy

    main()

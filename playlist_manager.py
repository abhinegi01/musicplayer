import os

class PlaylistManager:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = self.load_playlist()

    def load_playlist(self):
        return [os.path.join(self.music_folder, song) for song in os.listdir(self.music_folder) if song.endswith('.mp3')]

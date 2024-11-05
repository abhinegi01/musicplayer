import pygame

class AudioManager:
    def __init__(self, playlist):
        pygame.mixer.init()
        self.playlist = playlist
        self.current_track_index = 0
        self.load(self.current_track_index)  # Load the first track initially

    def load(self, track_index):
        """Load a track from the playlist."""
        if 0 <= track_index < len(self.playlist):
            pygame.mixer.music.load(self.playlist[track_index])
            self.current_track_index = track_index
        else:
            print("Track index out of range.")

    def play(self):
        """Play the currently loaded track."""
        if self.current_track_index is not None:
            pygame.mixer.music.play()
        else:
            print("No track loaded.")

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def next_track(self):
        """Load and play the next track."""
        self.current_track_index += 1
        if self.current_track_index >= len(self.playlist):
            self.current_track_index = 0  # Loop back to the first track
        self.load(self.current_track_index)
        self.play()

    def previous_track(self):
        """Load and play the previous track."""
        self.current_track_index -= 1
        if self.current_track_index < 0:
            self.current_track_index = len(self.playlist) - 1  # Loop to the last track
        self.load(self.current_track_index)
        self.play()

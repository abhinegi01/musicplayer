import tkinter as tk
from tkinter import filedialog

class MusicPlayerGUI:
    def __init__(self, audio_manager):
        self.audio_manager = audio_manager
        self.window = tk.Tk()
        self.window.title("Music Player")
        self.create_widgets()

    def create_widgets(self):
        # Play button
        play_button = tk.Button(self.window, text="Play", command=self.audio_manager.play)
        play_button.pack()

        # Next button
        next_button = tk.Button(self.window, text="Next", command=self.audio_manager.next_track)
        next_button.pack()

        # Previous button
        prev_button = tk.Button(self.window, text="Previous", command=self.audio_manager.previous_track)
        prev_button.pack()

        # Add more buttons for pause, stop, etc.

    def run(self):
        self.window.mainloop()
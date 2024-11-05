import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Import PIL for better image handling with Tkinter
import os
from gui import MusicPlayerGUI
from audio_manager import AudioManager
from playlist_manager import PlaylistManager

class MusicPlayerGUI:
    def __init__(self, audio_manager):
        self.audio_manager = audio_manager
        self.window = tk.Tk()
        self.window.title("Music Player")
        self.window.geometry("400x400")
        self.window.configure(bg="#add8e6")  # Set background to light blue

        self.track_var = tk.StringVar()  # Variable to display current track name

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(
            self.window, text="Music Player", 
            font=("Helvetica", 16, "bold"), 
            fg="#222222", bg="#add8e6"  # Set text color and background color
        )
        title_label.pack(pady=10)

        # Track display
        track_label = tk.Label(
            self.window, textvariable=self.track_var, 
            font=("Helvetica", 12), 
            fg="#0077b6", bg="#add8e6"  # Set text color and background color
        )
        track_label.pack(pady=10)

        # Control Frame for Buttons
        control_frame = tk.Frame(self.window, bg="#add8e6")  # Set frame background to light blue
        control_frame.pack(pady=20)

        # Styled buttons
        button_style = {
            "font": ("Helvetica", 10, "bold"),
            "bg": "#e0f7fa",  # Light cyan for buttons
            "fg": "#000000",  # Black text color
            "activebackground": "#b2ebf2", 
            "width": 8, 
            "height": 2
        }

        play_button = tk.Button(control_frame, text="Play", command=self.play_track, **button_style)
        play_button.grid(row=0, column=1, padx=5)

        next_button = tk.Button(control_frame, text="Next", command=self.audio_manager.next_track, **button_style)
        next_button.grid(row=0, column=2, padx=5)

        prev_button = tk.Button(control_frame, text="Previous", command=self.audio_manager.previous_track, **button_style)
        prev_button.grid(row=0, column=0, padx=5)

        pause_button = tk.Button(control_frame, text="Pause", command=self.audio_manager.pause, **button_style)
        pause_button.grid(row=1, column=1, padx=5, pady=10)

        stop_button = tk.Button(control_frame, text="Stop", command=self.audio_manager.stop, **button_style)
        stop_button.grid(row=1, column=0, padx=5, pady=10)

        # Volume slider
        volume_label = tk.Label(self.window, text="Volume", font=("Helvetica", 10), fg="#222222", bg="#add8e6")
        volume_label.pack()

        volume_slider = tk.Scale(
            self.window, from_=0, to=1, resolution=0.1, orient="horizontal", 
            command=self.set_volume, bg="#add8e6", fg="#0077b6", 
            troughcolor="#e0f7fa", width=15, length=200
        )
        volume_slider.set(0.5)  # Set initial volume to 50%
        volume_slider.pack(pady=10)

    def play_track(self):
        self.audio_manager.play()
        current_track = self.audio_manager.playlist[self.audio_manager.current_track_index]
        track_name = os.path.basename(current_track)  # Extract filename for display
        self.track_var.set(f"Now Playing: {track_name}")

    def set_volume(self, volume):
        self.audio_manager.set_volume(float(volume))

    def run(self):
        self.window.mainloop()


# Main execution remains the same
if __name__ == "__main__":
    music_folder = r"C:\Users\abhyudaya\Desktop\musicplayer_daa\musicplayer\music"
    playlist_manager = PlaylistManager(music_folder)
    audio_manager = AudioManager(playlist_manager.playlist)
    audio_manager.load(0)  
    app = MusicPlayerGUI(audio_manager)
    app.run()

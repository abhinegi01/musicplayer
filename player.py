from gui import MusicPlayerGUI
from audio_manager import AudioManager
from playlist_manager import PlaylistManager

if __name__ == "__main__":
    music_folder = r"C:\Users\abhyudaya\Desktop\musicplayer_daa\musicplayer\music"  
    playlist_manager = PlaylistManager(music_folder)
    audio_manager = AudioManager(playlist_manager.playlist)
    audio_manager.load(0)  
    app = MusicPlayerGUI(audio_manager)
    app.run()

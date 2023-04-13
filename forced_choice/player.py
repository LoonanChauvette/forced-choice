import time
import vlc

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL


class VolumeManager:
    def __init__(self):
        self.system_volume_interface = (
            AudioUtilities.GetSpeakers()
            .Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            .QueryInterface(IAudioEndpointVolume)
        )
        self.vlc_instance = vlc.Instance()
        self.vlc_player = self.vlc_instance.media_player_new()

    def set_system_volume(self, volume):
        if isinstance(volume, float) and (0.0 <= volume <= 1.0):
            self.system_volume_interface.SetMasterVolumeLevelScalar(volume, None)
        elif isinstance(volume, int) and (0 <= volume <= 100):
            volume = float(volume) / 100.0
            self.system_volume_interface.SetMasterVolumeLevelScalar(volume, None)
        else:
            raise ValueError("System volume must be between 0.0 and 1.0 or between 0 and 100")
    
    def get_system_volume(self):
        return round(self.system_volume_interface.GetMasterVolumeLevelScalar() * 100)
    
    def set_vlc_volume(self, volume):
        if isinstance(volume, int) and (0 <= volume <= 100):
            self.vlc_player.audio_set_volume(volume)
        elif isinstance(volume, float) and (0 <= int(volume*100) <= 100):
            self.vlc_player.audio_set_volume(int(volume*100))
        else:
            raise ValueError("VLC volume must be between 0.0 and 1.0 or between 0 and 100")

    def get_vlc_volume(self):
        return self.vlc_player.audio_get_volume()


class Player(VolumeManager):
    def __init__(self):
        super().__init__()
        self.media = None
        self.duration =  0 # in ms

    def load_file(self, filepath):
        self.media = self.vlc_instance.media_new(filepath)
        self.media.parse()
        self.duration = self.media.get_duration()

    def play(self):
        if not self.media:
            raise ValueError("No file to play. Use the Player.load_file() method")
        self.vlc_player.set_media(self.media)
        self.vlc_player.play()
        time.sleep(self.duration / 1000)

if __name__ == "__main__":
    player = Player()
    player.load_file("C:/Users/loona/OneDrive/Desktop/250hz_05vol_2sec.wav")
    player.play()

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import numpy as np


class VolumeManager:
    def __init__(self):
        self.volume_interface = self.create_volume_interface()
    
    def create_volume_interface(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        return interface.QueryInterface(IAudioEndpointVolume)

    def set_volume(self, volume):
        if isinstance(volume, float) and (0.0 <= volume <= 1.0):
            self.volume_interface.SetMasterVolumeLevelScalar(volume, None)
        elif isinstance(volume, int) and (0 <= volume <= 100):
            volume = float(volume) / 100.0
            self.volume_interface.SetMasterVolumeLevelScalar(volume, None)
        else:
            raise ValueError("Volume must be between 0.0 and 1.0 or between 0 and 100")
    
    def get_volume(self):
        return round(self.volume_interface.GetMasterVolumeLevelScalar() * 100)




if __name__ == "__main__":
    vm = VolumeManager()
    vm.set_volume(10)
    x = vm.get_volume()
    print(x)
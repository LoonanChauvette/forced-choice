import pytest
from forced_choice.player import VolumeManager

class TestVolumeManager:
    def test_set_system_volume_float(self):
        vm = VolumeManager()
        vm.set_system_volume(0.4)
        assert vm.get_system_volume() == 40

    def test_set_system_volume_int(self):
        vm = VolumeManager()
        vm.set_system_volume(30)
        assert vm.get_system_volume() == 30

    def test_set_system_volume_out_of_range(self):
        vm = VolumeManager()
        with pytest.raises(ValueError):
            vm.set_system_volume(101)

    def test_set_system_volume_invalid_input(self):
        vm = VolumeManager()
        with pytest.raises(ValueError):
            vm.set_system_volume("not a number")
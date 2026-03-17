import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Energy_Consumption(object):

    # Suite should not run on commecial devices.
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_non_supported_platform_C51250974(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is False, "Energy consumption module is visible"
        
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_non_supported_platform_C51250992(self):
        bios_version = self.driver.ssh.send_command("Get-WmiObject -Class Win32_BIOS | Select-Object -ExpandProperty Name")
        self.fc.swipe_window(direction="down", distance=2)
        if bios_version['stdout'].strip() != "W97 Ver. 92.40.01":
            assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is False, "Energy consumption module is visible"
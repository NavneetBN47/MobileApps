import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Energy_Consumption(object):

    # Suite supposed to be run on Ernesto as it has unsupporting bios with energy consumption card
    @pytest.mark.function
    @pytest.mark.ota 
    def test_01_energy_consumption_supported_platform_with_older_bios_C51250991(self):
        time.sleep(10)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is True, "Energy consumption module is not visible"
        self.fc.fd["energy_consumption"].click_energy_consumption()
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        assert self.fc.fd["energy_consumption"].verify_update_bios_message(), "Update BIOS message is not present in an older BIOS device"
        assert self.fc.fd["energy_consumption"].verify_learn_more_link(), "Learn more link is not present"
        assert self.fc.fd["energy_consumption"].verify_data_unavailable_label(), "Data unavailable label is not present"
        assert self.fc.fd["energy_consumption"].verify_total_energy_consumption() == False, "Total energy consumption is present in older BIOS device"
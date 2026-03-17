import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Energy_Consumption(object):

    # Suite supposed to be run longhornz and supported BIOS
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_consistency_check_for_total_energy_consumption_dropdown_C51250969(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is True, "Energy consumption module is  not visible"
        self.fc.fd["energy_consumption"].click_energy_consumption()
        #click on total energy consumption dropdown
        self.fc.fd["energy_consumption"].click_total_energy_consumption_dropdown()
        #last week and last month drop down should be seen in Total Energy consumption
        assert self.fc.fd["energy_consumption"].verify_last_week_option() == "Last Week", "Last Week option is not seen in Total Energy consumption"
        assert self.fc.fd["energy_consumption"].verify_last_month_option() == "Last Month", "Last Month option is not seen in Total Energy consumption"
        #While Switching from last week to last month--App should not crash
        self.fc.fd["energy_consumption"].select_last_month_option()
        #verify energy consumption header still displayed/visible
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        self.fc.close_myHP()
    
    @pytest.mark.function
    def test_02_deep_links_support_for_Energy_Consumption_C52992699(self):
        self.fc.launch_module_using_deeplink("hpx://pcenergyconsumption")
        time.sleep(5)
        assert self.fc.fd["energy_consumption"].verify_energy_consumption_header(), "Energy consumption header is  not visible"

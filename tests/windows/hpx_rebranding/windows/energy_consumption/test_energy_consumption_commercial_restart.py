import time
import pytest
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Energy_Consumption(object):

    # Suite supposed to be run longhornz and supported BIOS
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_restart_post_restart_fusion_restart_C51250993(self):
        self.fc.close_myHP()
        #restart fusion service
        task_utilities = TaskUtilities(self.driver.ssh)
        task_utilities.restart_fusion_service()
        #launch myHP app
        self.fc.launch_myHP_command()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["energy_consumption"].scroll_to_element("energy_consumption")
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is True, "Energy consumption module is  not visible"
        self.fc.fd["energy_consumption"].click_energy_consumption()
        assert self.fc.fd["energy_consumption"].get_collect_data_text_on_energy_consumption_page() == "Collecting data...", "Collecting data... text is not visible on energy consumption page"
        self.fc.close_myHP()
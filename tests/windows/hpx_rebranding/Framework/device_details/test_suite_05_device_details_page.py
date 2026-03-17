import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_05_Device_Details_Page(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(request.cls.driver)
        cls.fc.kill_hpx_process()
        cls.fc.kill_chrome_process()
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
               
    @pytest.mark.regression
    def test_01_verify_campaign_ads_on_device_details_page_C57081693(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), " Back to devices button is not displayed"
        assert self.devices_details_pc_mfe.verify_campaign_ads_show_up(), " Campaign Ads is not displayed"
        
        
    
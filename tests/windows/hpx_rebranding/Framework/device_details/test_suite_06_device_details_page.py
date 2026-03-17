import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_06_Device_Details_Page(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(request.cls.driver)
        cls.fc.kill_hpx_process()
        cls.fc.kill_chrome_process()
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.energy_consumption = request.cls.fc.fd["energy_consumption"]
        request.cls.fc.change_system_region_to_united_states()
        yield
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_campaign_ads_navigating_to_external_browser_C57081694(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_campaign_ads_contextual_card_show_up(), " Campaign Ads is not displayed"
        self.devices_details_pc_mfe.click_campaign_ads_contextual_card_show_up()
        self.devices_details_pc_mfe.click_on_shop_now_ads_button()
        actual_url = self.energy_consumption.get_webpage_url()
        expected_texts = ["contextual", "suggested"]
        assert any(text in actual_url for text in expected_texts), \
            f"Expected one of {expected_texts} in URL, but got: {actual_url}"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_02_verify_campaign_ads_are_showing_only_in_US_C65480881(self):
        assert self.devices_details_pc_mfe.verify_campaign_ads_contextual_card_show_up(), " Campaign Ads is not displayed in US"
        self.fc.change_system_region_to_india()
        self.fc.restart_myHP()
        assert not self.devices_details_pc_mfe.verify_campaign_ads_contextual_card_show_up(), " Campaign Ads is displayed in India"
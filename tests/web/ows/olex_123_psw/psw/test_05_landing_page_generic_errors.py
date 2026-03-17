import time
import pytest
import datetime
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.stack = request.config.getoption("--stack")
        self.printer_type = request.config.getoption("--printer-operation")
        self.browser_type = request.config.getoption("--browser-type")
        self.locale = request.config.getoption("--locale")
        
        self.traffic_director = self.fc.fd["traffic_director"]
        self.td_url = self.traffic_director.td_url
        self.hp_123 = self.fc.fd["hp_123"]        

        """
        https://hp-testrail.external.hp.com/index.php?/suites/view/3624&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3677718
        """
    def test_01_landing_page_generic_error(self):
        if self.printer_profile != "marconi_base":
            pytest.skip("Skipping test - this is to validate not-found page no printer needed.")
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, self.td_url)
        self.driver.navigate(self.td_url.replace("4V2M9C", "4VLD2J7") if self.stack != "prod" else self.td_url.format("4V2M9C", "4VZD2J7"))
        self.hpid.handle_privacy_popup(timeout=15)
        self.traffic_director.verify_incorrect_url_landing_page()
        assert self.traffic_director.verify_start_setup_btn(clickable=True,raise_e=False) is False, "Start Setup button should not be visible on incorrect URL landing page"
        assert self.traffic_director.verify_watch_video_btn(raise_e=False) is False, "Watch Video button should not be visible on incorrect URL landing page"
        self.traffic_director.click_hp_support_url()
        self.driver.add_window("support-site")
        self.driver.switch_window("support-site")
        assert "support" in self.driver.current_url, "Current URL should contain 'support'"
        self.driver.close_window("support-site")
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, self.td_url)
        self.driver.navigate(self.td_url.replace("4V2M9C", "4VLD2J7") if self.stack != "prod" else self.td_url.format("4V2M9C", "4VZD2J7"))
        self.traffic_director.verify_incorrect_url_landing_page()
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, self.td_url)
        self.traffic_director.verify_start_setup_btn()
        self.traffic_director.verify_watch_video_btn()
        self.traffic_director.verify_country_language_selector_link()
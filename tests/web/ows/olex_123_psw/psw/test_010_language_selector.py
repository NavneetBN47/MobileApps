import pytest
import time

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.printer_type = request.config.getoption("--printer-operation")
        self.browser_type = request.config.getoption("--browser-type")
        self.traffic_director = self.fc.fd["traffic_director"]
        
        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/3624&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3809236 
        """
    def test_01_language_selector(self):
        if self.printer_profile.startswith(("cherry", "lotus")):
            pytest.skip("Skipping test - only cherry/lotus specific tests should run on cherry/lotus profiles")
        self.hpid.handle_privacy_popup()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.verify_start_setup_btn()
        self.traffic_director.verify_country_language_selector_link()
        assert "US" in self.traffic_director.get_default_locale_from_selector(), "Default locale is not shown as United States"
        self.traffic_director.click_locale_selector_link()
        self.traffic_director.verify_locale_selector_overlay()
        self.traffic_director.verify_language_region_selector()
        self.traffic_director.click_locale_selector_close_btn()
        self.traffic_director.click_locale_selector_link()
        self.traffic_director.verify_locale_selector_overlay()
        self.traffic_director.click_locale_selector_close_btn()
        assert self.traffic_director.verify_locale_selector_overlay(invisible=True), "Select language/region overlay modal still shown"
        self.traffic_director.click_locale_selector_link()
        self.traffic_director.verify_locale_selector_overlay()
        self.traffic_director.select_region_from_selector(region="FR_FR")
        assert "fr/fr" in self.driver.get_current_url(), "Clicking on given region did not re-direct user to france region website"
        time.sleep(3)
        assert "FR" in self.traffic_director.get_default_locale_from_selector(), "Default locale is not shown as France"
        self.traffic_director.click_locale_selector_link()
        self.traffic_director.select_region_from_selector(region="EN_US")
        assert "us/en" in self.driver.get_current_url(), "Clicking on given region did not re-direct user to US/EN region website"
        time.sleep(3)
        assert "US" in self.traffic_director.get_default_locale_from_selector(), "Default locale is not shown as United States"
        self.traffic_director.click_locale_selector_link()
        self.traffic_director.verify_locale_selector_overlay()
        self.traffic_director.click_locale_selector_close_btn()
        self.traffic_director.click_start_setup_btn()
        self.fc.verify_traffic_director_load_paper_step()
        assert self.traffic_director.verify_locale_selector_overlay(invisible=True), "language/region selector is still showing"
        self.traffic_director.click_back_btn()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.click_printer_features_btn()
        self.traffic_director.verify_learn_tab()
        self.driver.navigate((self.driver.get_current_url()).replace("us/en", "br/pt"))
        self.driver.click_browser_back_button()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.click_setup_tab()
        self.traffic_director.click_locale_selector_link()
        self.traffic_director.verify_locale_selector_overlay()
        self.traffic_director.verify_taiwan_region_flag_not_shown()
        self.traffic_director.verify_hongkong_region_flag_not_shown()
        self.driver.navigate(self.traffic_director.td_url.replace("us/en", "tw/zh"))
        self.hpid.handle_privacy_popup()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.verify_start_setup_btn()
        self.traffic_director.verify_country_language_selector_link()
        assert "TW" in self.traffic_director.get_default_locale_from_selector(), "Default locale is not shown as Taiwan"
        assert self.traffic_director.verify_default_region_flag("data-testid") is None, "Default region flag is shown for taiwan region"
        assert self.traffic_director.verify_default_region_flag("id") == "", "Default region flag is shown for taiwan region"
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, url=(self.traffic_director.td_url).replace("us/en", "hk/zh"))
        self.hpid.handle_privacy_popup()
        self.traffic_director.verify_onboarding_center_page()
        self.traffic_director.verify_country_language_selector_link()
        assert "HK" in self.traffic_director.get_default_locale_from_selector(), "Default locale is not shown as hongkong"
        assert self.traffic_director.verify_default_region_flag("data-testid") is None, "Default region flag is shown for hongkong region"
        assert self.traffic_director.verify_default_region_flag("id") == "", "Default region flag is shown for hongkong region"
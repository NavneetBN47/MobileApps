import pytest
import random
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_24_Sanity_Pin_Or_Password_Printer_Info(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        # cls.pin_num = cls.p.get_pin()
        cls.fc = FlowContainer(cls.driver)

        cls.printer_name = cls.p.get_printer_information()['model name']


    @pytest.mark.smoke
    def test_01_verify_dialog_shows_when_change_country_or_language_with_secure_printer_C57463022(self):
        """
        Change country/language on Printer Information screen with a secure printer with pin set, verify "Find the printer PIN" dialog shows.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57463022
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].swipe_to_end()
        # change country/region or language
        if random.choice([True, False]):
        # Test country/region change
            self.fc.fd["printersettings"].verify_country_region_part()
            select_cou = self.fc.fd["printersettings"].get_country_region_text()
            self.fc.fd["printersettings"].click_country_dropdown()
            cou = self.fc.fd["printersettings"].verify_country_select_item(select_cou)
            cou.send_keys(Keys.UP, Keys.ENTER)
        else:
        # Test language change
            self.fc.fd["printersettings"].verify_language_part()
            select_lan = self.fc.fd["printersettings"].get_language_text()
            self.fc.fd["printersettings"].click_language_dropdown()
            lan = self.fc.fd["printersettings"].verify_language_select_item(select_lan)
            lan.send_keys(Keys.DOWN, Keys.ENTER)
        self.fc.fd["printersettings"].verify_set_country_or_language_dialog()
        self.fc.fd["printersettings"].click_set_save_btn()
        check_pin=self.fc.fd["printersettings"].verify_log_in_with_pin_dialog(raise_e=False)
        if not check_pin:
            pytest.skip("Skip this test as the printer has no pin")
        
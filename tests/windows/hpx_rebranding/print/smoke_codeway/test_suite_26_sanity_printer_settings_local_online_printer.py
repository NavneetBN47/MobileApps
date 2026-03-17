import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging
import re


pytest.app_info = "HPX"
class Test_Suite_26_Sanity_Printer_Settings_Local_Online_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session, chrome_account_data_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)

        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_add_printer(self):
        """
        Add a printer in device card.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)

    test_items = ["select_printer_status_item",
                  "select_printer_information",
                  "select_network_information",
                  "select_advanced_settings_item",
                  "select_printer_reports",
                  "select_print_quality_tools"]
    @pytest.mark.parametrize("method_name", test_items)
    @pytest.mark.smoke
    def test_02_verify_printer_device_card_shows_after_clicking_back_arrow_C57462906(self,method_name):
        """
        Click back arrow on "Printer Settings" screen, verify main UI shows.
        HPXG-3271: https://hp-jira.external.hp.com/browse/HPXG-3271
        [Function] The 'Install driver to print' screen shows after clicking top back arrow on Printer settings page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462906
        """
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        getattr(self.fc.fd["printersettings"], method_name)()
        sleep(3)
        self.fc.fd["printersettings"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_view_all_button()
        self.web_driver.set_size('min')

    @pytest.mark.smoke
    def test_03_verify_webpage_url_after_clicking_printer_dashboard_tile_C57462899(self):
        """
        Click "Printer dashboard" tile on main UI, verify "Consumer Portal" screen opens

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462899
        """
        detected_stack = self.fc.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["stage"]
        elif detected_stack == "Prod":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["prod"]
        self.sign_in_email, self.sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]
        self.fc.fd["devicesDetailsMFE"].click_print_dashboard(direction="up")
        self.fc.sign_in(self.sign_in_email, self.sign_in_password, self.web_driver, user_icon_click=False, send_before_click=False, min_win=None)
        sleep(2)
        current_url = self.web_driver.get_current_url()
        logging.info("Current URL: {}".format(current_url))
        url_patterns = {
            "Stage": r"https://consumer.[a-z]+.portalshell",
            "Prod": r"https://portal.hpsmart.com"
        }
        pattern = url_patterns[detected_stack]
        result = re.search(pattern, current_url)
        assert result is not None, "Expected URL pattern not found in {}".format(current_url)

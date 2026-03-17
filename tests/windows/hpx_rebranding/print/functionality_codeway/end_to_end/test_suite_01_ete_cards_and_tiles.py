import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep
import logging
import re


pytest.app_info = "HPX"
class Test_Suite_01_Ete_Cards_And_Tiles(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session, chrome_account_data_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        # cls.product_number = cls.p.get_printer_information()["product number"]
        # cls.serial_number = cls.p.get_printer_information()["serial number"]

    ##############################################################
    #    One simulator printer can't trigger offline status      #
    ##############################################################
    # @pytest.mark.regression
    # def test_01_add_a_printer_and_trigger_door_open(self):
    #     """
    #     Add a printer
    #     Trigger door open status, simulator printer doesn't support door open status.
    #     """
    #     self.fc.launch_hpx_to_home_page()
    #     # The login account type depends on build stack.
    #     detected_stack = self.fc.check_hpx_default_stack()
    #     if detected_stack == "Stage":
    #        onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["stage"]
    #     elif detected_stack == "Prod":
    #        onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["prod"]
    #        self.sign_in_email, self.sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]
    #     self.fc.add_a_printer(self.p)
        # self.p.fake_action_door_open()
        # sleep(5)
        # self.fc.fd["devicesMFE"].refresh_device_mfe()
    
    # @pytest.mark.regression
    # def test_02_verify_printer_device_card_C59058015(self):
    #     """
    #     Verify Printer Device Card

    #     The printer name and image should be seen on the printer device card.
    #     The supply gauge with proper supply levels should appear on the printer card.
    #     Click on the SMS should open the Printer Status screen inside the printer setting.

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/59058015
    #     """
    #     self.fc.fd["devicesMFE"].verify_supply_levels_card()
    #     self.fc.fd["devicesMFE"].click_door_open_sms_btn()
    #     self.fc.fd["printer_status"].verify_ps_ioref_list()
    #     self.fc.fd["printersettings"].click_top_back_arrow()
    #     self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name)

    # @pytest.mark.regression
    # def test_03_verify_printer_device_page_C59058020(self):
    #     """
    #     Verify Printer Device Page

    #     The device is listed with the correct name, image, and ink (Supply) gauge.
    #     SMS should be visible and clickable, redirecting to the Printer Status screen in printer settings.
    #     Product information should be clearly and accurately displayed.
    #     Printer Settings should be clearly displayed.
    #     'View all' under the Printer Settings tab is clickable and navigates to the Product Information screen.
    #     The back button should be visible, labeled 'Back', and navigate to the PDP screen when clicked.
    #     All the supported action tiles should be visible and clickable.

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/59058020
    #     """
    #     self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)

    #     # The device is listed with the correct name, image, and ink (Supply) gauge.
    #     self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    #     # SMS should be visible and clickable, redirecting to the Printer Status screen in printer settings.
    #     self.fc.fd["devicesDetailsMFE"].click_door_open_sms_btn()
    #     self.fc.fd["printer_status"].verify_ps_ioref_list()
    #     self.fc.fd["printersettings"].click_top_back_arrow()
    #     self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    #     # Product information should be clearly and accurately displayed.
    #     self.fc.fd["devicesDetailsMFE"].verify_product_information_mfe()
    #     self.fc.fd["devicesDetailsMFE"].verify_product_number_info(self.product_number)
    #     self.fc.fd["devicesDetailsMFE"].verify_serial_number_info(self.serial_number)
    #     self.fc.fd["devicesDetailsMFE"].verify_printer_name_info(self.printer_name)
    #     self.fc.fd["devicesDetailsMFE"].verify_warranty_status_info()
    #     self.fc.fd["devicesDetailsMFE"].verify_more_info_and_reports_info()

    #     # Printer Settings should be clearly displayed.
    #     # 'View all' under the Printer Settings tab is clickable and navigates to the Product Information screen.
    #     # The back button should be visible, labeled 'Back', and navigate to the PDP screen when clicked.
    #     self.fc.fd["devicesDetailsMFE"].verify_settings_view_all_item()
    #     self.fc.fd["devicesDetailsMFE"].click_view_all_button() 
    #     self.fc.fd["printersettings"].verify_progress_bar()
    #     sleep(5)
    #     self.fc.fd["printersettings"].click_top_back_arrow()

    #     # All the supported action tiles should be visible and clickable.
    #     sleep(5)
    #     self.fc.fd["devicesDetailsMFE"].win_scroll_element("device_details_page_nick_name", direction="up")
    #     self.fc.fd["devicesDetailsMFE"].verify_all_tiles_printer_device_page(check_flag=False)

    # def test_04_restore_door_open(self):
    #     """
    #     restore door open status
    #     """
    #     self.fc.fd["devicesDetailsMFE"].win_scroll_element("device_details_page_nick_name", direction="up")
    #     self.p.fake_action_door_close()
    #     sleep(5) 

    @pytest.mark.regression
    def test_05_verify_printables_tile_C59058662(self):
        """
        Verify Printables tile

        Clicking the 'Printables' tile should open the external website https://printables.hp.com/ in a browser.

        https://hp-testrail.external.hp.com/index.php?/cases/view/59058662
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_printables_tile()
        self.web_driver.add_window("printables")
        if "printables" not in self.web_driver.session_data["window_table"].keys():
            self.fc.fd["devicesDetailsMFE"].click_printables_tile()
            self.web_driver.add_window("printables")
        self.web_driver.switch_window("printables")
        self.web_driver.set_size("max")
        sleep(2)
        current_url = self.web_driver.get_current_url()
        assert "https://printables.hp.com/" in current_url

    @pytest.mark.regression
    def test_06_verify_print_dashboard_tile_C59058665(self):
        """
        Verify Print Dashboard tile

        Clicking the 'Print dashboards' tile should open the external website https://consumer.stage.portalshell.int.hp.com for Stage and https://portal.hpsmart.com/ for Prod in a browser
        Verify Print dashboard is launched.

        https://hp-testrail.external.hp.com/index.php?/cases/view/59058665
        """
        self.fc.restart_hpx()
        # The login account type depends on build stack.
        detected_stack = self.fc.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["stage"]
        elif detected_stack == "Prod":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["prod"]
        self.sign_in_email, self.sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_dashboard()
        self.fc.sign_in(self.sign_in_email, self.sign_in_password, self.web_driver, user_icon_click=False, send_before_click=False, min_win=None)
        sleep(2)
        current_url = self.web_driver.get_current_url()
        logging.info("Current URL: {}".format(current_url))
        
        # Check for both possible URL patterns: portal.hpsmart.com (Prod) and consumer.*.portalshell (Stage)
        prod_pattern = re.search(r"https://portal\.hpsmart\.com", current_url)
        stage_pattern = re.search(r"https://consumer\.[a-z]+\.portalshell", current_url)
        
        assert prod_pattern is not None or stage_pattern is not None, \
            "Expected URL pattern not found. Current URL: {}. Expected either 'https://portal.hpsmart.com' or 'https://consumer.[a-z]+.portalshell'".format(current_url)


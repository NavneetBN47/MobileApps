import pytest
import time
import logging

import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.flow_container import FlowContainer


pytest.app_info = "GOTHAM"
class Test_Suite_01_Advance_Settings_Basic(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        # # Initializing Printer1
        cls.p = load_printers_session

        # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.p2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p2.get_printer_information()
        logging.info("Printer Information:\n {}".format(cls.printer_info2))

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer = cls.fc.fd["printers"]
        cls.ews = cls.fc.fd["ews"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_add_two_printers(self):
        """
        Add two printers
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.fc.select_a_printer(self.p2)

        if self.printer.verify_pin_dialog(raise_e=False) is not False:
            if self.printer.input_pin(self.p.get_pin()) is True:
                self.printer.select_pin_dialog_submit_btn()

    def test_02_check_ews_load(self):
        """
        (+) Go to "Advance Settings" with an online applicable printer, verify printer EWS displays
        (+) Randomly check some information in the printer EWS webview, verify accuracy
        (+) Switch between a few different printers, verify EWS info
        Click back arrow on printer EWS screen, verify app home page shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16942852
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541084
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541087
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541086
        """
        printer_model_name2 = self.home.get_carousel_printer_model_name(index=1)
        self.home.select_printer_settings_tile(change_check={"wait_obj": "printer_settings_tile", "invisible": True})
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p2)
        self.ews.get_printer_name_text() == printer_model_name2
        self.home.select_navbar_back_btn()

        self.home.click_previous_device_btn()
        assert self.home.verify_previous_device_btn_enabled_status() == "true"
        assert self.home.verify_next_device_btn_enabled_status() == "true"
        
        printer_model_name1 = self.home.get_carousel_printer_model_name()
        self.home.select_printer_settings_tile(change_check={"wait_obj": "printer_settings_tile", "invisible": True})
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        self.ews.get_printer_name_text() == printer_model_name1

    def test_03_check_hidden_url(self):
        """
        Ctrl + Shift + right click combo below the title of the EWS screen, verify EWS hidden url shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15959478
        """
        self.ews.trigger_hidden_url()
        self.ews.verify_hidden_url()
        self.home.select_navbar_back_btn()
        
import pytest
import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"

class Test_Suite_05_Ios_Smart_Printer_Settings_Advanced(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.printer_settings = cls.fc.flow["printer_settings"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        ma_misc.get_hpid_account_info(stack=request.config.getoption("--stack"), a_type="hp+", instant_ink=True, driver=cls.driver)
        # Navigate to Home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_printer_information_screen_ui_elements(self):
        """
            C27655173: Verify Printer Information Screen
            Navigate to printer information screen and verify UI Elements - C13927549
        """
        self.fc.go_to_printer_settings_screen(self.p)
        printer_info = self.p.get_printer_information()
        self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.PS_PRINTER_INFORMATION)
        assert printer_info["bonjour name"] == self.fc.fd["printer_settings"].verify_title_and_get_value("Printer Name")
        assert self.p.get_printer_status() == self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Status").lower()
        assert printer_info["model name"] == self.fc.fd["printer_settings"].verify_title_and_get_value("Model Name")
        assert printer_info["ip address"] == self.fc.fd["printer_settings"].verify_title_and_get_value("IP Address")
        assert self.p.get_printer_current_sku() == self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Product Number")
        assert printer_info["serial number"] == self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Serial Number")
        assert printer_info["service id"] == self.fc.fd["printer_settings"].verify_title_and_get_value("Service ID")
        assert printer_info["firmware version"] == self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Firmware Version")
        # Preferences
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Printer Language") == "English"

    def test_02_verify_network_information_screen_ui_elements(self):
        """
        Navigate to Network information screen and verify UI Elements - C13927550
        """
        self.fc.go_to_printer_settings_screen(self.p)
        wireless_info = self.p.get_wireless_network_information()
        wifi_direct_info = self.p.get_wifi_direct_information()
        self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.PS_NETWORK_INFORMATION)
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Wireless").lower() == wireless_info["state"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Status") == wireless_info["status"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Bonjour Name") == wireless_info[
            "bonjour name"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("IP Address") == wireless_info["ip address"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Network Name (SSID)") == str(
            wireless_info["ssid"])
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Mac Address").replace(':', '') == \
               wireless_info["mac address"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Host Name") == wireless_info["host name"]
        if self.fc.fd["printer_settings"].get_ethernet_status() is not False:
            assert self.fc.fd["printer_settings"].get_ethernet_status() == ("not connected" or "connected")
        else:
            logging.info("Ethernet status not displayed")
        self.fc.fd["printer_settings"].go_to_wi_fi_direct()
        if self.fc.fd["printer_settings"].verify_ui_option_displayed(
                PrinterSettings.WIFI_DIRECT_FIND_PRINTER_PIN) is not False:
            logging.debug("Printer WiFi Direct looking for printer pin")
        else:
            assert self.fc.fd["printer_settings"].verify_title_and_get_value("Direct") == wifi_direct_info["state"]
            assert self.fc.fd["printer_settings"].verify_title_and_get_value("Security") == ("On" or "Off")
            assert self.fc.fd["printer_settings"].verify_title_and_get_value("Direct Name") == str(
                wifi_direct_info["name"])
        self.fc.fd["printer_settings"].select_navigate_back()

    def test_03_shortcuts_help_from_printer_settings(self):
        """
        Requirements:
         1. C31461881	Shortcut Options under My Printer screen 
         2. C31461887	Redirection by tapping on 'Shortcuts' setting under Printer Information 
         3. C31461882	Verify help icon on Shortcuts Setting screen 
         4. C31461883	Verify back button behavior on Shortcuts Setting screen 
        Description: C31461887, C31461882, C31461883 & C31461881 
         1. Launch Smart app
         2. Load Printer
         3. Tap on Printer Icon
         4. Select Shortcuts
         5. Select Help Icon
         6. Select Back Button
        Expected Results:
         4. Verify Shortcuts screen
            Verify Printer Access Option
         5. Verify Shortcuts help screen
         6. Verify Shortcuts screen
        """
        if "novelli" not in self.p.p_obj.projectName:
            pytest.skip("Novelli printer is unavailable for testing this time")
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(self.printer_settings.PS_SHORTCUTS, verify_nav=False)
        self.shortcuts.verify_shortcuts_title(timeout=30)
        self.shortcuts.click_help_btn()
        self.shortcuts.verify_shortcuts_help_screen(timeout=20)
        self.printer_settings.select_done()
        self.shortcuts.verify_shortcuts_title(timeout=30)
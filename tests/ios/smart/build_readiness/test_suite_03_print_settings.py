import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"

class Test_Suite_03_Print_Settings:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]
        cls.p = load_printers_session

    def test_01_verify_print_from_other_devices_screen(self):
        """
        Navigate to Print from other devices screen and verify UI elements, tap 123.hp.com link and navigate back
        C50698976
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].go_to_print_from_other_devices_screen()
        self.fc.fd["printer_settings"].verify_print_from_other_device_screen_ui_elements()
        self.fc.fd['printer_settings'].go_to_123_hp_com_page_and_navigate_back()

    def test_02_verify_supported_supplies(self):
        """
        Description: C50698977
         1. Load Home screen with HPID login
         2. Add a printer from Printer list
         3. Click on Printer icon from Smart Home screen
         4. Click on Supported Supplies screen

        Expected Result:
         4. Verify Printer's page
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(PrinterSettings.PS_SUPPORTED_SUPPLIES, verify_nav=False)
        assert self.printer_settings.verify_support_supplies_screen_or_ink_trial_btn() or self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4

    @pytest.mark.parametrize("report_name", ["printer_status", "network_configuration", "print_quality_report", "wireless_test_report", "web_access_report"])
    def test_03_printer_settings_printer_report_by_name(self, report_name):
        """
        Description: C50698978
         1. Load Home screen with HPID login
         2. Add a printer from Printer list
         3. Click on Printer icon from Smart Home screen
         4. Click on Printer Reports button
         5. Click on Print button for below report:
            - Printer Status report
            - Network Configuration report
            - Wireless Test Report
            - Print Quality Report
            - Web Access Report

        Expected Result:
         4. Verify Printer Reports screen
         5. Verify Print jobs send success
        """
        reports_name = {"printer_status": [self.printer_settings.REPORT_PRINTER_STATUS, "configurationPage"],
                        "network_configuration": [self.printer_settings.REPORT_NETWORK_CONFIG, "networkDiagnosticPage"],
                        "print_quality_report": [self.printer_settings.REPORT_PRINT_QUALITY, "pqDiagnosticsPage"],
                        "wireless_test_report": [self.printer_settings.REPORT_WIRELESS_TEST, "wirelessNetworkPage"],
                        "web_access_report": [self.printer_settings.REPORT_WEB_ACCESS, "webAccessReport"]
                        }
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        reports_from_printer = self.p.get_printer_supported_reports()
        report_in_printer = reports_name[report_name][1] in reports_from_printer
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(PrinterSettings.PS_PRINTER_REPORTS)
        report_in_app = self.printer_settings.verify_printer_report_by_name(reports_name[report_name][0], raise_e=False)
        if bool(report_in_app) != report_in_printer:
            raise AssertionError("{} on app is mismatch with {} on printer".format(report_in_app, report_in_printer))
        elif not bool(report_in_app) and not report_in_printer:
            pytest.skip("skip test this item, printer doesn't support this report {}".format(reports_name[report_name][0]))
        else:
            self.printer_settings.select_printer_reports_report_btn(reports_name[report_name][0])
            self.printer_settings.verify_printer_status_popup(raise_e=False, timeout=15)
            self.printer_settings.verify_printer_report_by_name(reports_name[report_name][0])

    def test_04_verify_printer_information_page_ui_elements(self):
        """
            C50698979: Verify Printer Information Screen
            Navigate to printer information screen and verify UI Elements - C13927549
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.go_to_printer_settings_screen(self.p)
        printer_info = self.p.get_printer_information()
        self.fc.fd["printer_settings"].select_ui_option(
            PrinterSettings.PS_PRINTER_INFORMATION)
        self.printer_settings.verify_printer_info_page() # verify the printer info page is present
        assert printer_info["bonjour name"] == self.fc.fd[
            "printer_settings"].verify_title_and_get_value("Printer Name")
        # All printer states
        assert self.p.get_printer_status() in self.printer_settings.PRINTER_STATES, "Printer status is UNAVAILABLE"
        assert printer_info["model name"] == self.fc.fd[
            "printer_settings"].verify_title_and_get_value("Model Name")
        assert printer_info["ip address"] == self.fc.fd[
            "printer_settings"].verify_title_and_get_value("IP Address")
        assert self.p.get_printer_current_sku() == self.fc.fd[
            "printer_settings"].verify_title_and_get_value("Product Number")
        assert printer_info["serial number"] == self.fc.fd[
            "printer_settings"].verify_title_and_get_value("Serial Number")
        assert printer_info["service id"] == self.fc.fd[
            "printer_settings"].verify_title_and_get_value("Service ID")
        assert printer_info["firmware version"] == self.fc.fd[
            "printer_settings"].verify_title_and_get_value("Firmware Version")
        # Assert for the available printer languages in the environment
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Printer Language"
                ) in self.printer_settings.PRINTER_LANGUAGES, "Printer language is UNAVAILABLE"
        
    def test_05_verify_first_printer_network_info(self):
        """
        C50698980 - Verify Network Information
        Click Printer Settings->Network Information
        Use Network Information_values.xlsx to check all applicable settings display correctly.
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        wireless_info = self.p.get_wireless_network_information()
        wifi_direct_info = self.p.get_wifi_direct_information()
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(PrinterSettings.PS_NETWORK_INFORMATION)
        self.printer_settings.verify_network_info_page() # verify the network info page is present
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Wireless").lower() == wireless_info["state"].lower()
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Status") == wireless_info["status"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Bonjour Name") == wireless_info["bonjour name"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("IP Address") == wireless_info["ip address"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Network Name (SSID)") == str(wireless_info["ssid"])
        assert self.fc.fd["printer_settings"].verify_title_and_get_value("Mac Address").replace(':', '') == wireless_info["mac address"]
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
            assert self.fc.fd["printer_settings"].verify_title_and_get_value(
                "Direct") == wifi_direct_info["state"]
            assert self.fc.fd["printer_settings"].verify_title_and_get_value(
                "Security") == ("On" or "Off")
            assert self.fc.fd["printer_settings"].verify_title_and_get_value(
                "Direct Name") == str(wifi_direct_info["name"])
        self.fc.fd["printer_settings"].select_navigate_back()
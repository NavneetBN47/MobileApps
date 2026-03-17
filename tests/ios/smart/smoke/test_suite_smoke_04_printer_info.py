"""
Printer information flow and functionality smoke test suite for iOS
"""
import logging
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"


class Test_Suite_Smoke_04_Printer_Info:
    """
    Printer information flow class for smoke testing for iOS
    """

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.printer_settings = cls.fc.flow["printer_settings"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_home(self):
        """
        Fixture setup for autouse of go_home function
        Verify navigation to home page after:
        1. App installation on the mobile device
        2. Clicking on Sign In on the ows screen and navigating to home page
        """
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_verify_printer_information_page_ui_elements(self):
        """
            C27655173: Verify Printer Information Screen
            Navigate to printer information screen and verify UI Elements - C13927549
        """
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

    def test_02_verify_network_information_page_ui_elements(self):
        """
        Navigate to Network information screen and verify UI Elements - C13927550
        """
        self.fc.go_to_printer_settings_screen(self.p)
        wireless_info = self.p.get_wireless_network_information()
        wifi_direct_info = self.p.get_wifi_direct_information()
        self.fc.fd["printer_settings"].select_ui_option(
            PrinterSettings.PS_NETWORK_INFORMATION)
        self.printer_settings.verify_network_info_page() # verify the network info page is present
        assert self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Wireless").lower() == wireless_info["state"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Status") == wireless_info["status"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Bonjour Name") == wireless_info["bonjour name"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value(
            "IP Address") == wireless_info["ip address"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Network Name (SSID)") == str(wireless_info["ssid"])
        assert self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Mac Address").replace(':', '') == wireless_info["mac address"]
        assert self.fc.fd["printer_settings"].verify_title_and_get_value(
            "Host Name") == wireless_info["host name"]
        if self.fc.fd["printer_settings"].get_ethernet_status() is not False:
            assert self.fc.fd["printer_settings"].get_ethernet_status() == (
                "not connected" or "connected")
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

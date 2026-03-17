import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"

class Test_Suite_03_Ios_Smart_Printer_Settings_Preferences(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.supported_pages = cls.p.get_ews_supported_pages(raise_e=False)
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.stack = request.config.getoption("--stack")
        # Navigate to Home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_tray_and_paper_screen_ui_elements(self):
        """
           Navigate to Tray and Paper screen and verify UI Elements - C13927546
        """
        self.check_option_displayed("pgTrayAndPaperMgmt", self.printer_settings.PS_TRAY_AND_PAPER)
        self.printer_settings.select_ok_btn()
        self.printer_settings.verify_ui_elements(self.printer_settings.TRAY_AND_PAPER_UI_ELEMENTS)
        self.printer_settings.select_navigate_back()

    def test_02_verify_quite_mode_screen_ui_elements(self):
        """
           Navigate to Quite Mode screen and verify UI Elements - C16815269
        """
        self.check_option_displayed("pgQuietMode", self.printer_settings.PS_QUIET_MODE)
        self.printer_settings.select_ok_btn()
        self.printer_settings.verify_ui_elements(self.printer_settings.QUITE_MODE_UI_ELEMENTS)
        assert self.printer_settings.get_radio_button_value(PrinterSettings.OFF_RADIO_BUTTON) == 1
        assert self.printer_settings.get_radio_button_value(PrinterSettings.ON_RADIO_BUTTON) == 0
        self.printer_settings.select_navigate_back()

    def check_option_displayed(self, supported_page_name, ui_option):
        if not self.supported_pages or supported_page_name not in self.supported_pages:
            pytest.skip("Printer does not support Quite Mode pages".format(self.printer_name))
        else:
            self.fc.go_to_printer_settings_screen(self.p)
            option_displayed = self.printer_settings.find_ui_element_exists(ui_option)
            if not option_displayed:
                pytest.skip("QuiteMode pages not displayed for Printer -".format(self.printer_name))
            else:
                self.printer_settings.select_ui_option(ui_option)
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest


pytest.app_info = "SMART"

class Test_Suite_05_Hide_Printers(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]

    def test_01_hide_the_printer_ui(self):
        """
        Description: C33405100
         1. Load Home screen
         2. Click on big "+" or small "+" icon on Home screen
         3. Select Add Printer
         4. Click on Printer icon from Home screen
         5. Click on Hide Printer from Printers Settings
        Expected Results:
         4 Verify "Hide Printer" display on the screen
         5. Verify Home screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_select_network_printer(self.p)
        self.fc.flow_home_verify_ready_printer(self.p.get_printer_information()["bonjour name"])
        self.home.load_printer_info()
        self.printer_settings.verify_printer_settings_items(self.printer_settings.HIDE_PRINTER, invisible=False)
        self.printer_settings.select_printer_setting_opt(self.printer_settings.HIDE_PRINTER)
        self.home.verify_home_nav()
        self.home.verify_add_new_printer(invisible=False)
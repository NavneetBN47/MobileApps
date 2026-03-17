from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import PACKAGE
import pytest
import time


pytest.app_info = "SMART"

class Test_Suite_03_Printer_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]

        # Define the variable
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]

    def test_01_printer_settings_ui(self):
        """
        Description: C36510551, C33557829
         1. Load Home screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Settings tile or icon from navigation bar on Home screen

        Expected Result:
         4. Verify Printer Settings screen with below points:
            + Title (Printer Bonjour name)
            + Printer Status
        """
        self.__load_printer_settings_screen()
        self.printer_settings.verify_my_printer(self.p.get_printer_information()["bonjour name"])

    def test_02_printer_settings_print_from_other_device(self):
        """
        Description: C31297684
         1. Load Printer Settings screen
         2. Click on Print from other device

        Expected Result:
         2. Verify Print from other device screen
        """
        self.__load_printer_settings_opt(self.printer_settings.PRINT_FROM_OTHER_DEVICES)
        self.printer_settings.verify_print_from_other_devices_screen()

    def test_03_printer_settings_supported_supplies(self):
        """
        Description: C31297685
         1. Load Printer Settings screen
         2. Click on Supported Supplies

        Expected Result:
         2. Verify if browser popup or not
        """
        self.__load_printer_settings_opt(self.printer_settings.SUPPORTED_CARTRIDGES)
        self.printer_settings.verify_supported_supplies_webview()

    @pytest.mark.parametrize("item_name", ["printer_display_lights", "tray_and_paper", "quiet_mode", "print_quality_tools"])
    def test_04_printer_settings_preferences_by_opt(self, item_name):
        """
         Description: C31297686, C31297687, C33405098
         1. Load Printer Settings screen
         2. Click on below items under Preference one by one: (Depends on Printer we connect to, some printers doesn't support all below items )
            + Naples / Naples Plus/ Naples Super doesn't have mobile EWS page, so this test cases for all printers except Naples/Plus/Super
            + Printer Display Lights
            + Tray and Paper
            + Quiet Mode
        Or Click below items on Printer Settings screen (If Printer doesn't support this item, then won't display on App)
            + Print Quality Tools

        Expected Result:
         2. Verify each item screen popup in browser
        """
        items_name = {"printer_display_lights": [self.printer_settings.PRINTER_DISPLAY_LIGHTS, "pgDisplaySettings"],
                      "tray_and_paper": [self.printer_settings.TRAY_PAPER, ["pgTrayAndPaperMgmt", "pgSimpleTrayMgmt"]],
                      "quiet_mode": [self.printer_settings.QUIET_MODE, "pgQuietMode"],
                      "print_quality_tools": [self.printer_settings.PRINT_QUALITY_TOOLS, "pgDevServ"]
                      }
        current_printer_name = self.printer_name[0:self.printer_name.rfind("[")]
        if not self.p.get_ews_supported_pages(raise_e=False):
            pytest.skip("skip test this item since {} printer doesn't support mobile version EWS".format(current_printer_name))
        else:
            items_from_printer = self.p.get_ews_supported_pages()
            if item_name == "tray_and_paper":
                in_printer = any(item in items_from_printer for item in items_name[item_name][1])
            else:
                in_printer = items_name[item_name][1] in items_from_printer
            self.__load_printer_settings_screen()
            if self.printer_settings.verify_printer_settings_items(items_name[item_name][0], invisible=True, raise_e=False):
                pytest.skip("skip test this item since {} printer doesn't support mobile version EWS".format(items_name[item_name][0]))
            else:
                if not in_printer:
                    raise AssertionError("item in app {} is mismatch with item in printer {}".format(items_name[item_name][0], in_printer))
                self.printer_settings.select_printer_setting_opt(items_name[item_name][0])
                time.sleep(10)
                assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    @pytest.mark.parametrize("report_name",["printer_status", "network_configuration", "pq_diagnostics_report", "wireless_test_report", "web_access_report"])
    def test_05_printer_settings_printer_report_by_name(self, report_name):
        """
         Description: C33557796, C33557797, C33557800, C33557803, C33557809, C33557812, C33557830, C33557834, C31297688,
         C31297696, C31297697, C31297698, C31297699, C31297700, C31297701
         1. Load Printer Settings screen
         2. Click on Printer Reports
         3. Click on report by name one by one:
            PRINTER_STATUS_REPORT
            NETWORK CONFIGURATION REPORT
            PRINT QUALITY REPORT
            WIRELESS REPORT
            WEB ACCESS REPORT
         4. Click on Back button

        Expected Result:
         2. Verify Printer Reports screen
         3. Verify a print job is on the printer
         4. Verify Printer settings screen with Printer Reports item shows on the screen
        :param report_name:
        """
        reports_name = {"printer_status": [self.printer_settings.REPORT_PRINTER_STATUS, "configurationPage"],
                        "network_configuration": [self.printer_settings.REPORT_NETWORK_CONFIG, "networkDiagnosticPage"],
                        "pq_diagnostics_report": [self.printer_settings.REPORT_PQ_DIAGNOSTICS, "pqDiagnosticsPage"],
                        "wireless_test_report": [self.printer_settings.REPORT_WIRELESS_TEST, "wirelessNetworkPage"],
                        "web_access_report": [self.printer_settings.REPORT_WEB_ACCESS, "webAccessReport"]
                        }
        reports_from_printer = self.p.get_printer_supported_reports()
        report_in_printer = reports_name[report_name][1] in reports_from_printer
        self.__load_printer_settings_opt(self.printer_settings.PRINTER_REPORTS)
        report_in_app = self.printer_settings.verify_printer_report_by_name(reports_name[report_name][0], raise_e=False)
        if bool(report_in_app) != report_in_printer:
            raise AssertionError("{} on app is mismatch with {} on printer".format(report_in_app, report_in_printer))
        elif not bool(report_in_app) and not report_in_printer:
            pytest.skip("skip test this item, printer doesn't support this report {}".format(reports_name[report_name][0]))
        else:
            self.printer_settings.select_printer_reports_report_btn(reports_name[report_name][0])
            self.printer_settings.verify_printer_report_by_name(reports_name[report_name][0])
        self.fc.select_back()
        self.printer_settings.verify_printer_settings_items(self.printer_settings.PRINTER_REPORTS)

    def test_06_printer_settings_advanced_settings(self):
        """
        Description: C31297692, C31297695, C33655202
         1. Load Printer Settings screen
         2. Click on Advanced Settings item

        Expected Result:
         2. Should be open a page with the browser
        """
        current_printer_name = self.printer_name[0:self.printer_name.rfind("[")]
        in_link = bool (self.p.get_ews_supported_pages(raise_e=False))
        self.__load_printer_settings_screen()
        in_app = self.printer_settings.verify_printer_settings_items(self.printer_settings.ADVANCED_SETTINGS, invisible=False, raise_e=False)
        if not in_link and not in_app:
            pytest.skip("skip test this item since {} printer doesn't support advanced settings option".format(current_printer_name))
        elif in_link != in_app:
            raise AssertionError("Advanced Settings should be displayed on screen")
        else:
            self.printer_settings.select_printer_setting_opt(self.printer_settings.ADVANCED_SETTINGS)
            assert(self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    def test_07_quick_reference(self):
        """
        Description: C31297705
         1. Load Printer Settings screen
         2. Click on Quick Reference item from Printer Settings page if "Quick Reference" item displays on screen

        Expected Result:
         2. Verify if browser popup or not
        """
        self.__load_printer_settings_screen()
        if self.printer_settings.verify_printer_settings_items(self.printer_settings.QUICK_REFERENCE, invisible=True, raise_e=False):
            pytest.skip("skip this item since quick reference item doesn't support on this printer")
        else:
            self.printer_settings.select_printer_setting_opt(self.printer_settings.QUICK_REFERENCE)
            assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    def test_08_print_quality_tools(self):
        """
        Description: C31297689
         1. Load Printer Settings screen
         2. Click on Print Quality Tools item from Printer Settings page if "Print Quality Tools" item displays on screen

        Expected Result:
         2. Verify if browser popup or not
        """
        self.__load_printer_settings_screen()
        if self.printer_settings.verify_printer_settings_items(self.printer_settings.PRINT_QUALITY_TOOLS, invisible=True, raise_e=False):
            pytest.skip("skip this item since print quality tools item doesn't support on this printer")
        else:
            self.printer_settings.select_printer_setting_opt(self.printer_settings.PRINT_QUALITY_TOOLS)
            assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_printer_settings_screen(self):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
              otherwise clicking on small "+" button on Home screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.home.load_printer_info()

    def __load_printer_settings_opt(self, opt):
        """
        - Load to Printer Settings screen.
        - click on the each item from printer settings screen
        :param opt:
        """
        self.__load_printer_settings_screen()
        self.printer_settings.select_printer_setting_opt(opt=opt)
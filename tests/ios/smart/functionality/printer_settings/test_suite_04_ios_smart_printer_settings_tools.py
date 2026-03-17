from time import sleep
import pytest
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"

class Test_Suite_04_Ios_Smart_Printer_Settings_Tools(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.printer_settings = cls.fc.fd["printer_settings"]

        # Navigate to Home screen
        cls.fc.go_home(stack=cls.stack, button_index=2)

    @pytest.mark.parametrize("report_name", ["printer_status", "network_configuration", "print_quality_report", "wireless_test_report", "web_access_report"])
    def test_01_printer_settings_printer_report_by_name(self, report_name):
        """
        Description: C31297696, C31297698, C31297700, C31297701, C31297699, C31297688
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

    def test_02_verify_print_quality_tools_ui_elements(self):
        """
        Description: C31297689
         1. Load Home screen with HPID login
         2. Add a printer from Printer list
         3. Click on Printer icon from Smart Home screen
         4. Click on Print Quality Tools button
         5. Click on Clean button

        Expected Result:
         4. Verify Print Quality tools screen
         5. Verify Clean Printhead popup
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(PrinterSettings.PS_PRINT_QUALITY_TOOLS)
        if self.printer_settings.verify_clean_printhead(raise_e=False):
            self.printer_settings.select_clean_btn()
            self.printer_settings.verify_clean_printhead_popup()

    def test_03_verify_supported_supplies(self):
        """
        Description: C31297685
         1. Load Home screen with HPID login
         2. Add a printer from Printer list
         3. Click on Printer icon from Smart Home screen
         4. Click on Supported Supplies screen

        Expected Result:
         4. Verify Printer's page
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(PrinterSettings.PS_SUPPORTED_SUPPLIES, verify_nav=False)
        assert self.printer_settings.verify_support_supplies_screen_or_ink_trial_btn() or self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4
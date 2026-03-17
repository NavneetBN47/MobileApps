import pytest
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_02_Printer_Reports_Error_Con(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.report_item_dir = {}

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

        cls.report_opts = {"Status" : cls.printer_settings.STATUS, 
                            "Demo" : cls.printer_settings.DEMO, 
                            "Diagnostic" :cls.printer_settings.DIAGNOSTIC,
                            "Network" : cls.printer_settings.NETWORK, 
                            "Wireless" : cls.printer_settings.WIRELESS, 
                            "Quality" :cls.printer_settings.QUALITY, 
                            "Web" : cls.printer_settings.WEB}

    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_go_to_print_report_screen(self):
        """        
        Select Print Reports
        """
        self.home.verify_printer_settings_tile()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        sleep(2)
        self.printer_settings.select_printer_reports()
        check_feature = self.printer_settings.verify_this_feature_is_not_available_screen()
        if check_feature:
            pytest.skip("Skip this test as the printer has no this feature")
        self.printer_settings.verify_printer_reports_page()

    def test_03_get_print_report_item(self):
        all_item_list = ["Status", "Demo", "Diagnostic", "Network", "Wireless", "Quality", "Web"]
        for each_item in all_item_list:
            if self.printer_settings.get_printer_reports_items(self.report_opts[each_item]):
                self.report_item_dir[each_item] = 1

    def test_04_each_opt_door_open_flow(self):
        """        
        Create a random error condition from the following:
        - Cartridge Missing
        - Door Open
        - Out of Paper
        - Out of Supplies
        - Printer Problem
        - Printer Jam

        Click on Print button for any report
        Repeat for other reports

        Should generate accurate errors based on type.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965617
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965618
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965677
        """
        try:
            for each_item in self.report_item_dir.keys():
                self.p.fake_action_door_open()
                self.printer_settings.select_report_opt(self.report_opts[each_item])
                self.printer_settings.click_report_print_btn()
                if self.printer_settings.verify_door_open_dialog():
                    self.printer_settings.click_dialog_cancel_btn()
                else:
                    self.printer_settings.verify_print_status_unknown_dialog()
                    self.printer_settings.click_dialog_cancel_btn()
                sleep(2)
                self.printer_settings.click_report_print_btn()
                if self.printer_settings.verify_door_open_dialog():
                    self.p.fake_action_door_close()
                    self.printer_settings.click_retry_btn()
                    if self.printer_settings.verify_cancel_print_dialog(invisible=True, raise_e=False, timeout=60):
                        if self.printer_settings.verify_printing_is_completed_dialog(raise_e=False):
                            self.printer_settings.click_report_close_btn()
                        else:
                            self.printer_settings.verify_print_status_unknown_dialog()
                            self.printer_settings.click_dialog_cancel_btn()
                    else:
                        self.printer_settings.verify_print_status_unknown_dialog()
                        self.printer_settings.click_dialog_cancel_btn()
                else:
                    self.printer_settings.verify_print_status_unknown_dialog()
                    self.printer_settings.click_dialog_cancel_btn()
                sleep(2)
        finally:
            self.p.fake_action_door_close()

    def test_05_each_opt_printer_off_flow(self):
        """        
        Turn off printer
        Click the Print button for any report

        When printer becomes offline after a report is selected to be printed, there should be an error message displayed

        https://hp-testrail.external.hp.com/index.php?/cases/view/15967999
        """
        for each_item in self.report_item_dir.keys():
            self.fc.trigger_printer_offline_status(self.p)
            self.printer_settings.select_report_opt(self.report_opts[each_item])
            self.printer_settings.click_report_print_btn()
            if self.printer_settings.verify_unable_to_connect_dialog():
                self.printer_settings.click_dialog_cancel_btn()
            else:
                self.printer_settings.verify_print_status_unknown_dialog()
                self.printer_settings.click_dialog_cancel_btn()
            sleep(2)
            self.printer_settings.click_report_print_btn()
            if self.printer_settings.verify_unable_to_connect_dialog():
                self.fc.restore_printer_online_status(self.p)
                self.printer_settings.click_retry_btn()
                if self.printer_settings.verify_cancel_print_dialog(invisible=True, raise_e=False, timeout=45):
                    if self.printer_settings.verify_printing_is_completed_dialog(raise_e=False):
                        self.printer_settings.click_report_close_btn()
                    else:
                        self.printer_settings.verify_print_status_unknown_dialog()
                        self.printer_settings.click_dialog_cancel_btn()
                else:
                    self.printer_settings.verify_print_status_unknown_dialog()
                    self.printer_settings.click_dialog_cancel_btn()
            else:
                self.printer_settings.verify_print_status_unknown_dialog()
                self.printer_settings.click_dialog_cancel_btn()
            sleep(2)
        
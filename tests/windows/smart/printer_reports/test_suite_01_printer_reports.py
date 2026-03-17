import pytest
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Printer_Reports(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.report_item_dir = {}

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

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
        View report options on the right

        Report options include:
        * Printer Status Report
        * Demo Page
        * Print Diagnostic Information
        * Network Configuration Report (If available)
        * Print Quality Report
        * Wireless Test Report (If wireless)
        * Web Access Report (2015 or greater)

        https://hp-testrail.external.hp.com/index.php?/cases/view/15961890
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965663
        https://hp-testrail.external.hp.com/index.php?/cases/view/16004230
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965679
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

    def test_04_each_opt_back_flow(self):
        """        
        Select any setting option
        Now select Reports
        Click the back arrow

        User should always return to Main UI when hitting back arrow on Win.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15961892
        """
        for each_item in self.report_item_dir.keys():
            self.printer_settings.select_report_opt(self.report_opts[each_item])
            self.home.select_navbar_back_btn()
            self.home.select_printer_settings_tile()
            self.printer_settings.verify_printer_settings_page()
            sleep(2)
            self.printer_settings.select_printer_reports()
            self.printer_settings.verify_printer_reports_page()

    def test_05_each_opt_cancel_flow(self):
        """        
        Select Reports
        Click on each option button 
        Immediately click Cancel button

        Should cancel report and return user to Printer Settings-> Printer Report details page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15962717
        https://hp-testrail.external.hp.com/index.php?/cases/view/15962720
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965605
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965608
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965611
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965614
        https://hp-testrail.external.hp.com/index.php?/cases/view/19402945
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965665
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965669
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965671
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965673
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965675
        https://hp-testrail.external.hp.com/index.php?/cases/view/15966069
        https://hp-testrail.external.hp.com/index.php?/cases/view/19402947
        """
        for each_item in self.report_item_dir.keys():
            self.printer_settings.select_report_opt(self.report_opts[each_item])
            self.printer_settings.click_report_print_btn()
            self.printer_settings.click_dialog_cancel_print_btn()
            self.printer_settings.verify_dialog_disappear()
            sleep(2)

    def test_06_each_opt_print_flow(self):
        """        
        Click on Printer Settings
        Select Reports
        Click on each option button 
        Click the Close button when report has finished

        Dialogue should close.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15961893
        https://hp-testrail.external.hp.com/index.php?/cases/view/15962718
        https://hp-testrail.external.hp.com/index.php?/cases/view/15962721
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965606
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965609
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965612
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965615
        https://hp-testrail.external.hp.com/index.php?/cases/view/19402946
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965667
        https://hp-testrail.external.hp.com/index.php?/cases/view/15962719
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965604
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965607
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965610
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965613
        https://hp-testrail.external.hp.com/index.php?/cases/view/17889778

        """
        for each_item in self.report_item_dir.keys():
            self.printer_settings.select_report_opt(self.report_opts[each_item])
            self.printer_settings.click_report_print_btn()
            if self.printer_settings.verify_cancel_print_dialog(invisible=True, raise_e=False, timeout=30):
                if self.printer_settings.verify_printing_is_completed_dialog(raise_e=False):
                    self.printer_settings.click_report_close_btn()
                else:
                    self.printer_settings.verify_print_status_unknown_dialog()
                    self.printer_settings.click_dialog_cancel_btn()      
            else:
                self.printer_settings.verify_print_status_unknown_dialog()
                self.printer_settings.click_dialog_cancel_btn()
            sleep(2)

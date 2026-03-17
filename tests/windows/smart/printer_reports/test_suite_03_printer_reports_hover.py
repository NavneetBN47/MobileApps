import pytest
from time import sleep
import logging
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_03_Printer_Reports_Hover(object):
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
        
    def test_01_go_to_print_report_screen(self):
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
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_printer_settings_tile()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        sleep(2)
        self.printer_settings.select_printer_reports()
        check_feature = self.printer_settings.verify_this_feature_is_not_available_screen()
        if check_feature:
            pytest.skip("Skip this test as the printer has no this feature")
        self.printer_settings.verify_printer_reports_page()
        for item in list(self.report_opts.keys()):
            if not self.printer_settings.get_printer_reports_items(self.report_opts[item]):
                del self.report_opts[item]
        print(self.report_opts)

    def test_02_hover_report_item(self):
        """        
        Check hover state for report options

        Verify correct hover state for report options.

        https://hp-testrail.external.hp.com/index.php?/cases/view/19402959
        """
        option_list = list(self.report_opts.keys())
        for option in option_list:
            self.printer_settings.hover_reports_item(self.report_opts[option])
            value = self.fc.check_element_background('report_list', 'printer_reports', 'reports_org.png', value=0.0)
            logging.info("hover vs org: {}".format(value))
            assert 0.009 > value > 0.008
            value = self.fc.check_element_background('report_list', 'printer_reports', option + '_h.png', value=0.0)
            logging.info("hover vs hover: {}".format(value))
            assert value < 0.001

    def test_03_hover_print_button(self):
        """        
        Check hover state for print report buttons according to the attached hover states file

        Verify correct hover state for print report button for each report option.

        https://hp-testrail.external.hp.com/index.php?/cases/view/19402959
        """
        option_list = list(self.report_opts.keys())
        for option in option_list:
            self.printer_settings.select_report_opt(self.report_opts[option])
            self.printer_settings.hover_reports_item("report_print_btn")
            value = self.fc.check_element_background('report_print_btn', 'printer_reports', 'print_btn_org.png', value=0.0)
            logging.info("hover vs org: {}".format(value))
            assert 0.48 > value > 0.46
            value = self.fc.check_element_background('report_print_btn', 'printer_reports', 'print_btn_s.png', value=0.0)
            logging.info("hover vs select: {}".format(value))
            assert value < 0.01

    def test_04_hover_print_information_option(self):
        """        
        Check the highlight of Printer Information item.

        1. Verify white background color for the "Printer Information" when not selected
        2. Verify the background color for the "Printer Information" is changed to light gray when hover
        3. Verify the background color for the "Printer Information" is changed to draker gray when click and hold on
        4. Verify the background color for the "Printer Information" is changed to blue when selected.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078897
        """
        self.printer_settings.hover_reports_item("printer_information_opt")
        value = self.fc.check_element_background('info_group', 'printer_info', 'info_o.png', value=0.0)
        logging.info("hover vs org: {}".format(value))
        assert 0.048 > value > 0.045
        value = self.fc.check_element_background('info_group', 'printer_info', 'info_h.png', value=0.0)
        logging.info("hover vs hover: {}".format(value))
        assert value < 0.001
        self.printer_settings.select_printer_information()
        value = self.fc.check_element_background('info_group', 'printer_info', 'info_o.png', value=0.0)
        logging.info("select vs org: {}".format(value))
        assert 0.004 > value > 0.003
        value = self.fc.check_element_background('info_group', 'printer_info', 'info_s.png', value=0.0)
        logging.info("select vs select: {}".format(value))
        assert value < 0.001

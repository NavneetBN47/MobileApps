import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_02_Printer_Reports(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        pytest.skip("Skipping test suite temporarily due to ONESIM printer limitation.")

        """
        Check the test printer with the feature of printing reports feature.
        If the printer doesn't support this feature, skip all tests.
        """
        cls.fc.launch_hpx_to_home_page()
        cls.fc.add_a_printer(cls.p)
        cls.fc.fd["devicesMFE"].click_windows_dummy_printer(cls.printer_name)
        cls.fc.fd["devicesDetailsMFE"].verify_printer_device_page(cls.printer_name)
        cls.fc.fd["devicesDetailsMFE"].click_view_all_button() 
        cls.fc.fd["printersettings"].verify_progress_bar()
        cls.fc.fd["printersettings"].select_printer_reports()
        check_feature = cls.fc.fd["printersettings"].verify_this_feature_is_not_available_screen()
        if check_feature:
            pytest.skip("Skipping test suite temporarily due to ONESIM printer limitation.")
        cls.item_list = cls.fc.fd["printersettings"].verify_printer_reports_page()

    @pytest.mark.regression
    def test_01_print_demo_page_c57707033_c57707055(self):
        """
        Click Demos Page Print button, verify report is printed and accurate

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707033

        Printing Completed UI
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/57707055
        """
        self.item_list = self.fc.fd["printersettings"].verify_printer_reports_page()
        self.__select_opt_to_complete_print_report('DEMO')

    @pytest.mark.regression
    def test_02_close_demo_page_print_c57707035(self):
        """
        Click Close button on Demo Page dialogue, verify dialogue closes

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707035
        """
        self.__select_complete_ok_button('DEMO')

    @pytest.mark.regression
    def test_03_print_network_con_report_c57707036(self):
        """
        Click Network Configuration Report Print button, verify report is printed and accurate

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707036
        """
        self.__select_opt_to_complete_print_report('NETWORK')

    @pytest.mark.regression
    def test_04_close_network_con_report_print_c57707038(self):
        """
        Click Close button on Network Configuration Report dialogue, verify dialogue closes

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707038
        """
        self.__select_complete_ok_button('NETWORK')

    @pytest.mark.regression
    def test_05_print_print_quality_report_c57707039(self):
        """
        Click Print Quality Report Print button, verify report is printed and accurate

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707039
        """
        self.__select_opt_to_complete_print_report('QUALITY')

    @pytest.mark.regression
    def test_06_close_print_quality_report_print_c57707041(self):
        """
        Click Close button on Print Quality Report dialogue, verify dialogue closes

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707041
        """
        self.__select_complete_ok_button('QUALITY')

    @pytest.mark.regression
    def test_07_print_wireless_test_report_c57707042(self):
        """
        Click Wireless Test Report Print button, verify report is printed and accurate

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707042
        """
        self.__select_opt_to_complete_print_report('WIRELESS')

    @pytest.mark.regression
    def test_08_close_wireless_report_print_c57707044(self):
        """
        Click OK button on Wireless Test Report dialogue, verify dialogue closes

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707044
        """
        self.__select_complete_ok_button('WIRELESS')

    @pytest.mark.regression
    def test_09_print_web_access_report_c57707045(self):
        """
        Click Web Access Report Print button, verify report is printed and accurate

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707045
        """
        self.__select_opt_to_complete_print_report('WEB')

    @pytest.mark.regression
    def test_10_close_web_access_report_print_c57707047(self):
        """
        Click Close button on Wireless Web Access dialogue, verify dialogue closes

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707047
        """
        self.__select_complete_ok_button('WEB')

    @pytest.mark.regression
    def test_11_print_print_diag_infor_c57707048(self):
        """
        Click Print Diagnostic Information Print button, verify report is printed and accurate

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707048
        """
        self.__select_opt_to_complete_print_report('DIAGNOSTIC')

    @pytest.mark.regression
    def test_12_close_print_diag_infor_print_c57707050(self):
        """
        Click Close button on Print Diagnostic Information dialogue, verify dialogue closes

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707050
        """
        self.__select_complete_ok_button('DIAGNOSTIC')

    def __select_opt_to_complete_print_report(self, opt):
        if opt not in self.item_list:
            pytest.skip("Skip this test as no '{}'".format(opt))
        self.fc.fd["printersettings"].select_report_opt(opt)
        self.fc.fd["printersettings"].click_report_print_btn()
        printing_dialog = self.fc.fd["printersettings"].verify_report_printing_dialog(opt, timeout=10, raise_e=False)
        if printing_dialog is False:
            unknown_dialog = self.fc.fd["printersettings"].verify_print_status_unknown_dialog(raise_e=False)
            if unknown_dialog:
                self.fc.fd["printersettings"].click_report_ok_btn()
                pytest.skip("Printer Status Unknown")
            else:
                raise NoSuchElementException("Printing dialog or unknown status dialog is not displayed")
        self.fc.fd["printersettings"].verify_printing_is_completed_dialog(opt)

    def __select_complete_ok_button(self, opt):
        if opt not in self.item_list:
            pytest.skip("Skip this test as no '{}'".format(opt))
        if self.fc.fd["printersettings"].click_report_ok_btn(raise_e=False) is False:
            pytest.skip("Skip this test as OK button is missing")
        assert self.fc.fd["printersettings"].verify_printing_is_completed_dialog(opt, timeout=3, raise_e=False) is False
        sleep(3)

    
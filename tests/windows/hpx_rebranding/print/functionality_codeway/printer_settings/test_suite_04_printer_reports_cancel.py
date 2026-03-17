import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "HPX"
class Test_Suite_04_Printer_Reports_Cancel(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


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
            pytest.skip("Skip all tests as the printer has no this feature")
        cls.item_list = cls.fc.fd["printersettings"].verify_printer_reports_page()
    
    @pytest.mark.regression
    def test_01_printing_status_report_c57707058(self):
        """
        Printing the Printer Status Report UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707058
        """
        self.__select_opt_to_printing_report('STATUS')
        self.__select_printing_cancel_button('STATUS')

    @pytest.mark.regression
    def test_02_printing_demo_page_c57707059(self):
        """
        Printing Demo Page UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707059
        """
        self.__select_opt_to_printing_report('DEMO')

    @pytest.mark.regression
    def test_03_cancel_printing_demo_page_c57707034(self):
        """
        Click Cancel button on Demo Page dialogue, verify job is cancelled

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707034
        """
        self.__select_printing_cancel_button('DEMO')
        
    @pytest.mark.regression
    def test_04_printing_network_con_report_c57707060(self):
        """
        Printing the Network Configuration Report UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707060
        """
        self.__select_opt_to_printing_report('NETWORK')

    @pytest.mark.regression
    def test_05_cancel_printing_network_con_report_c57707037(self):
        """
        Click Cancel button on Network Configuration Report dialogue, verify job is cancelled

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707037
        """
        self.__select_printing_cancel_button('NETWORK')
    
    @pytest.mark.regression
    def test_06_printing_print_quality_report_c57707061(self):
        """
        Printing the Print Quality Report UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707061
        """
        self.__select_opt_to_printing_report('QUALITY')

    @pytest.mark.regression
    def test_07_cancel_printing_print_quality_report_c57707040(self):
        """
        Click Cancel button on Print Quality Report dialogue, verify job is cancelled

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707040
        """
        self.__select_printing_cancel_button('QUALITY')

    @pytest.mark.regression
    def test_08_printing_wireless_test_report_c57707062(self):
        """
        Printing the Wireless Test Report UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707062
        """
        self.__select_opt_to_printing_report('WIRELESS')

    @pytest.mark.regression
    def test_09_cancel_printing_wireless_test_report_c57707043(self):
        """
        Click Cancel button on Wireless Test Report dialogue, verify job is cancelled

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707043
        """
        self.__select_printing_cancel_button('WIRELESS')

    @pytest.mark.regression
    def test_10_printing_web_access_report_c57707063(self):
        """
        Printing the Web Access Report UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707063
        """
        self.__select_opt_to_printing_report('WEB')

    @pytest.mark.regression
    def test_11_cancel_printing_web_access_report_c57707046(self):
        """
        Click Cancel button on Wireless Web Access dialogue, verify job is cancelled

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707046
        """
        self.__select_printing_cancel_button('WEB')
    
    @pytest.mark.regression
    def test_12_printing_print_diag_infor_c57707064(self):
        """
        Printing Print Diagnostic Information UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707064
        """
        self.__select_opt_to_printing_report('DIAGNOSTIC')

    @pytest.mark.regression
    def test_13_cancel_printing_print_diag_infor_c57707049(self):
        """
        Click Cancel button on Print Diagnostic Information dialogue, verify job is cancelled

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707049
        """
        self.__select_printing_cancel_button('DIAGNOSTIC')

    def __select_opt_to_printing_report(self, opt):
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

    def __select_printing_cancel_button(self, opt):
        if opt not in self.item_list:
            pytest.skip("Skip this test as no '{}'".format(opt))
        if self.fc.fd["printersettings"].click_dialog_cancel_btn(raise_e=False) is not False:
            assert self.fc.fd["printersettings"].verify_report_printing_dialog(opt, timeout=2, raise_e=False) is False
        else:
            raise NoSuchElementException("Printing dialog or unknown status dialog is not displayed")

import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import random


pytest.app_info = "HPX"
class Test_Suite_05_Printer_Reports_Error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.opt_dic = {'opt': False}  # Dictionary to store the selected report option


    @pytest.mark.regression
    def test_01_verify_feature_not_available_screen_c57707028_c57707057(self):
        """
        Click on Print Reports for printer doesn't support printer report, verify "This feature is not available for the selected printer..." shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707028

        Report Not Available UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707057
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button() 
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_printer_reports()
        check_feature = self.fc.fd["printersettings"].verify_this_feature_is_not_available_screen()
        if check_feature is False:
            self.opt_dic['opt'] = True
            pytest.skip("Skip this test as the printer has no this feature")

    @pytest.mark.regression
    def test_02_verify_printer_reports_screen_c57707054(self):
        """
        Reports UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707054
        """
        if self.opt_dic['opt'] is False:
            pytest.skip("Skip this test as the printer has no this feature")
        item_list= self.fc.fd["printersettings"].verify_printer_reports_page()
        self.opt_dic['opt'] = random.choice(item_list)
    #################################################################################################
    # The simulated printer information doesn't support door open or trigger printer offline action. #
    #################################################################################################
    # @pytest.mark.regression
    # def test_03_generate_door_open_and_print_c57707051(self):
    #     """
    #     Click Print button on a random report while printer in error state, verify accurate error handling
    #     The simulated printer information doesn't support door open action.
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/57707051 (Door Open)
    #     """
    #     if self.opt_dic['opt'] is False:
    #         pytest.skip("Skip this test as the printer has no this feature")
    #     self.p.fake_action_door_open()
    #     self.fc.fd["printersettings"].select_report_opt(self.opt_dic['opt'])
    #     self.fc.fd["printersettings"].click_report_print_btn()
    #     self.fc.fd["printersettings"].verify_door_open_dialog()

    # @pytest.mark.regression
    # def test_04_fix_door_open_and_retry_c57707052(self):
    #     """
    #     Generate/fix a printer error when trying to run a report, verify dialog goes away if fixed or returns if not
        
    #     https://hp-testrail.external.hp.com/index.php?/cases/view/57707052
    #     """
    #     if self.opt_dic['opt'] is False:
    #         pytest.skip("Skip this test as the printer has no this feature")
    #     self.p.fake_action_door_close()
    #     self.fc.fd["printersettings"].click_retry_btn()
    #     printing_dialog = self.fc.fd["printersettings"].verify_report_printing_dialog(self.opt_dic['opt'], timeout=10, raise_e=False)
    #     if printing_dialog is False:
    #         unknown_dialog = self.fc.fd["printersettings"].verify_print_status_unknown_dialog(raise_e=False)
    #         if unknown_dialog:
    #             self.fc.fd["printersettings"].click_report_ok_btn()
    #             pytest.skip("Printer Status Unknown")
    #         else:
    #             raise NoSuchElementException("Printing dialog or unknown status dialog is not displayed")
    #     self.fc.fd["printersettings"].verify_printing_is_completed_dialog(self.opt_dic['opt'], timeout=60)

    # @pytest.mark.regression
    # def test_05_turn_off_printer_and_print_c57707053(self):
    #     """
    #     Click on a report and then immediately turn printer off, verify printer offline error is received

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/57707053
    #     """
    #     if self.opt_dic['opt'] is False:
    #         pytest.skip("Skip this test as the printer has no this feature")
    #     self.fc.trigger_printer_offline_status(self.p)
    #     self.fc.fd["printersettings"].select_report_opt(self.opt_dic['opt'])
    #     self.fc.fd["printersettings"].click_report_print_btn()
    #     self.fc.fd["printersettings"].verify_unable_to_connect_dialog()
    #     self.fc.fd["printersettings"].click_dialog_cancel_btn()

    # @pytest.mark.regression
    # def test_06_restore_printer_online_status(self):
    #     self.fc.restore_printer_online_status(self.p)
        

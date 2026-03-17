import pytest
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
# pytest.set_info = "HPX"
class Test_Suite_01_Scan_Error_Handling(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"] 
        cls.hostname = cls.p.get_printer_information()['serial number']


    @pytest.mark.regression
    def test_01_go_to_scanner_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_02_scan_cancelled_for_glass_c43738715(self):
        """
        "Scan Cancelled" for glass scan UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738715
        """
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].GLASS)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_600)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].click_cancel_btn()
        self.fc.fd["scan"].verify_scan_canceled_dialog()

    @pytest.mark.regression
    def test_03_cancel_a_scan_with_glass_c43738716(self):
        """
        Cancel a scan with glass bed, verify functionality

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738716
        """
        self.fc.fd["scan"].click_close_on_scan_canceled_dialog()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_04_scan_cancelled_for_adf_c43738717(self):
        """
        "Scan Canceled" for ADF scan UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738717
        """
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_300)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].click_cancel_btn()
        self.fc.fd["scan"].verify_scan_canceled_dialog()

    @pytest.mark.regression
    def test_05_cancel_a_scan_with_adf_c43738718(self):
        """
        Cancel a scan with ADF, verify functionality

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738718
        """
        self.fc.fd["scan"].click_close_on_scan_canceled_dialog()
        self.fc.fd["scan"].verify_scan_btn()

    ##############################################################
    #    One simulator printer can't trigger offline status      #
    ##############################################################
    # def test_06_simulate_scanner_not_found(self):
    #     """
    #     Simulator printer doesn't support trigger offline status.
    #     Simulate a ScanUnreachable (Scanner Not found) issue, verify functionality
    #     """
    #     self.fc.trigger_printer_offline_status(self.p)
    #     self.fc.fd["scan"].click_scan_btn()
    #     self.fc.fd["scan"].verify_scanning_screen()
    #     self.fc.fd["scan"].verify_scanner_not_found_dialog()

    # def test_07_fix_scanner_not_found_c43738730(self):
    #     """
    #     Fix simulated ScanUnreachable issue, verify error does not return and scan job is successful

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/43738730
    #     """
    #     self.fc.restore_printer_online_status(self.p)
    #     self.fc.fd["scan"].click_dialog_close_btn()
    #     sleep(5)
    #     self.fc.fd["scan"].click_scan_btn()
    #     self.fc.fd["scan"].verify_scanning_screen()
    #     self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_08_edit_save_share_print_c43738398(self):
        """
        [Unhappy path] Trigger a printer error during scanning, fix and then continue to save/share/print.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738398
        """
        # Click on the edit button in the preview screen.
        # Click on the 'Markup' button.
        # Make some changes in the settings.
        # Verify that changes are reflected in the image.
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_markup_item()
        self.fc.fd["scan"].verify_edit_makup_setting_screen()
        self.fc.fd["scan"].click_red_pen_btn()
        self.fc.fd["scan"].click_center_image()
        self.fc.fd["scan"].click_edit_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # Save, share, or print the edited image.
        # Verify that the image is saved, shared, or printed successfully.
        # save
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        flie_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("del " + flie_path)

        # print
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_printer(self.hostname)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # share
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        self.fc.fd["scan"].click_dialog_share_btn()
        self.fc.fd["scan"].verify_share_picker_popup()
        self.fc.fd["scan"].dismiss_share_picker_popup()
        self.fc.fd["scan"].verify_share_picker_popup(invisible=True)
 
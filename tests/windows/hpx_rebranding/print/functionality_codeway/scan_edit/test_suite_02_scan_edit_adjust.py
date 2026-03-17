import pytest
import random
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep
import logging


pytest.app_info = "HPX"
class Test_Suite_02_Scan_Edit_Adjust(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"] 


    @pytest.mark.regression
    def test_01_go_to_scanner_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_02_verify_scanning_page_c43738442(self):
        """
        Perform scan job.
        Verify Back button is not seen on the "Scanning" screen when scanning is in progress.
        Verify "Scanning..." screen shows with progress ring.
        Verify the "Cancel" button shows in the screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738442
        """
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            source_list = ["Document Feeder", "Scanner Glass"]
            set_source = random.choice(source_list)
            logging.info("Scanner Source: {}".format(set_source))
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, set_source)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(invisible=False)

    @pytest.mark.regression
    def test_03_click_done_button_back_to_scan_intro_page_c43738444(self):
        """
        Initiate Scan step by step to "Scanning.." screen.
        Click "Cancel" button on "Scanning.." screen.
        Verify user goes back to Scan intro page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738444
        """
        self.fc.fd["scan"].verify_scanning_screen(invisible=True)
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn()
        # Start a new scan and immediately click cancel button due to simulator printer speed
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_600)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].click_cancel_btn()
        self.fc.fd["scan"].verify_scan_canceled_dialog()
        self.fc.fd["scan"].click_close_on_scan_canceled_dialog()
        self.fc.fd["scan"].verify_scan_btn()
        # Continue with the rest of the test
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen()
 
    @pytest.mark.regression
    def test_04_verify_adjust_default_setting_c43738500(self):
        """
        Click on Adjust button.
        'Adjust' default setting should be 0 by default.
        Slider should be in the middle by default.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738500
        """
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_adjust_item()
        self.fc.fd["scan"].verify_adjust_setting_default_value()
        custom = self.fc.fd["hpx_rebranding_common"].compare_image_diff("tool_navigation_menu", folder_n="scan", image_n="slider_default.png")
        assert custom < 0.02

    @pytest.mark.regression
    def test_05_check_reset_adjust_button_c43738501_c43738502(self):
        """
        CLick on 'Adjust' button.
        'Adjust' setting should change according to the user's input.
        'Pointer' should accurately reflect according to the adjustments made by the user.(not covered)

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738501

        Adjust the scanned settings.
        Click on 'Reset Adjust' button.
        Adjust settings should be rest to the default settings and it should be reflected in the image.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738502
        """
        self.fc.fd["scan"].change_adjust_contrast_edit_value("50")
        self.fc.fd["scan"].click_reset_adjust_btn()
        self.fc.fd["scan"].verify_adjust_contrast_edit_value('0')

    @pytest.mark.regression
    def test_06_check_undo_and_redo_button_c43738503(self):
        """
        Ajust the scanned page.
        Click on 'undo'/'redo' icon.
        Clicking the "Undo" icon should revert the last adjustment and restore its previous state.
        Clicking the "Redo" icon should reapply the last adjustment accordingly.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738503
        """
        self.fc.fd["scan"].change_adjust_contrast_edit_value("50")
        self.fc.fd["scan"].click_undo_btn()
        self.fc.fd["scan"].verify_adjust_contrast_edit_value('0')
        self.fc.fd["scan"].click_redo_btn()
        self.fc.fd["scan"].verify_adjust_contrast_edit_value('50')

    @pytest.mark.regression
    def test_07_back_to_scanner_screen(self):
        """
        Back to Scanner screen from Edit screen.
        """
        self.fc.fd["scan"].click_edit_cancel_btn()
        self.fc.fd["scan"].verify_exit_without_saving_dialog_for_edit_screen()
        self.fc.fd["scan"].click_exit_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_08_select_resolution_to_1200dpi_c43738492(self):
        """
        Select 'Resolution' to 1200dpi
        Click on scan button.
        Click on edit
        verify warning dialog shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738492
        """
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_1200)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(timeout=300)
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_processing_scan_dialog()
        self.fc.fd["scan"].verify_edit_screen()
  
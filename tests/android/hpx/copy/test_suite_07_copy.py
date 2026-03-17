import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_07_Copy:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.home = cls.fc.fd[FLOW_NAMES.HOME]
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]
        cls.edit = cls.fc.fd["edit"]
        cls.fc.hpx = True

    def test_01_select_and_verify_flash_mode(self):
        """
        C52636853 - Verify the 'Copy' feature when the user selects any option from 'Flash' mode.
        1.Click on the 'Copy' tile.
        2.Tap on Flash option, choose 'ON' and capture an image in manual/auto mode. Verify the behavior.
        4.Navigate to camera screen, Choose the flash option as 'OFF' and capture an image in manual/auto mode.Verify the behavior.
        6.Navigate to camera screen, Choose the flash option as 'Auto' and capture an image in manual/auto mode.
        7.Navigate to camera screen, Choose the flash option as 'Torch' and capture an image in manual/auto mode.
        8.Click on Start Black\Color button from preview screen to print. Verify the behavior.
        Expected Result:
        After step 9: The user should be able to print successfully without any errors.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        modes = ['Auto Flash', 'Flash On', 'Flash Off','Fill Flash']
        for _ in range(3):
            assert self.camera_scan.get_camera_scan_flash_mode() in modes
            self.camera_scan.click_camera_scan_flash_mode()
            self.camera_scan.click_shutter()
            self.print_preview.verify_print_preview_screen()
            self.driver.back()
            self.print_preview.select_leave_button()
            self.hpx_printer_details.click_copy_tile(raise_e=False)
        assert self.hpx_printer_details.click_copy_tile(raise_e=False)

    def test_02_copy_tile_when_user_select_paper_size(self):
        """
        C52637152 - Verify the 'Copy' feature when the user selects a 'Paper size' option.
        1.Install and launch the app. Add the target device on the root view.
        3.Navigate to the device details page. Click on the 'Copy' tile.
        5.Select any 'Paper size' option (A4/4*6in/10*15cm/5*7in/13*8cm/ID card/Business card) from camera screen.
        6.Navigate to preview screen by capturing the image in Manual/Auto mode.
        7.Click on start Black\Color button to print.Verify the behavior.
        Expected Result:After step 7: The success modal screen should be displayed as below screen and user should be able to print successfully.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.digital_copy.select_object_size_screen("digital_paper_size_business_card")
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_03_copy_tile_when_user_signed_in(self):
        """
        C52641096 - Verify the 'Copy' feature when the user selects a 'Paper size' option.
        1.Install and launch the app. Add the target device on the root view.
        3.Navigate to the device details page. Click on the 'Copy' tile.
        3.Then click on the Add button in preview screen.
        4.Click on the 'Paper size' button and observe the behavior.
        5.Repeat the step 2 and 3.
        7.Click on start Black\Color button to print.Verify the behavior.
        Expected Result:After Step 4: The 'Paper size' button should be 'Disabled'.
        After Step 7: 1.The user should be able to add multiple files, and each file should be printed successfully without any errors.
        2.Left and Right arrow should be visible when user adds more than '2' pages and user should be able to navigate all the pages.
        3.The pagination number should be visible, indicating the current page and the total number of pages.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_app_page_btn()
        self.digital_copy.verify_paper_size_dropbox(is_enabled=False)
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_app_page_btn()
        self.camera_scan.click_shutter()
        self.print_preview.get_no_pages_from_print_preview() == 3, "Print preview show images."
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_04_user_prints_multiple_copies(self):
        """
        C52641930 - Verify the Copy' feature' when the user prints multiple copies.
        1.Install and launch the app. Add the target device on the root view.
        3.Navigate to the device details page. Click on the 'Copy' tile.
        5.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        6.Select a value greater than '1' from the 'Copy' button. (e.g., 3, 4, 5, etc.).
        7.Click on start Black\Color button to print. Verify the behavior.
        Expected Result:After step 6: The 'Copies' label should be displayed on the 'Print Preview' screen when the user selects a value greater than '1'.
        After step 8: The user should be able to successfully print the selected number of copies (e.g., 3, 4, 5, etc.).
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_num_of_copies(3)
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()
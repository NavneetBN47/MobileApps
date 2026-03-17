import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_08_Copy:
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
    
    def test_05_copy_tile_when_user_signed_in(self):
        """
        C52641973 - Verify the 'Copy' feature when the user selects the 'Original' option from the 'Resize' option.
        1.Install and launch the app. Add the target device on the root view.
        3.Navigate to the device details page. Click on the 'Copy' tile.
        6.Click on 'Resize' button.
        7.Select 'Original Size' option and observe the print preview screen.
        8.Click on start Black\Color button to print.Verify the behavior.
        Expected Result: The success modal screen should be displayed as below screen and user should be able to print successfully.
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
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_option("original_size")
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_06_print_multiple_copies_on_black_mode(self):
        """
        C52644332 - Verify the 'Copy' feature, when the user prints in 'Black' mode.
        1.Install and launch the app. Add the target device on the root view.
        3.Navigate to the device details page. Click on the 'Copy' tile.
        4.Select any value from the Copy button (From 1-99).
        5.Click on Start Black button to print.
        Expected Result: The user should be able to print the selected number of copies in 'Black' mode.
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
        self.digital_copy.select_num_of_copies(2)
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_07_print_multiple_copies_on_color_mode(self):
        """
        C52644429 - Verify the 'Copy' feature, when the user prints in 'Color' mode.
        1.Install and launch the app. Add the target device on the root view.
        3.Navigate to the device details page. Click on the 'Copy' tile.
        4.Select any value from the Copy button (From 1-99).
        5.Click on Start Color button to print.
        Expected Result: The user should be able to print the selected number of copies in 'Black' mode.
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
        self.digital_copy.select_num_of_copies(2)
        self.digital_copy.select_start_color_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_08_delete_single_page_from_multiple_copies(self):
        """
        C52646518 - Verify the 'Copy' feature with multiple pages and deletion of one page.
        1.Install and launch the app. Add the target device on the root view.
        3.Navigate to the device details page. Click on the 'Copy' tile.
        4.Select any value from the Copy button (From 1-99).
        5.Click on Start Color button to print.
        Expected Result: The user should be able to print the selected number of copies in 'Black' mode.
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
        for _ in range(2):
            self.print_preview.click_app_page_btn()
            self.camera_scan.click_shutter()
            self.print_preview.verify_print_preview_screen()
        self.preview.select_delete_page_icon_in_print_preview()
        assert self.print_preview.get_no_pages_from_print_preview() == 2, "Print preview does not show only one image after removal."
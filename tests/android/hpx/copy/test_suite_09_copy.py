import pytest
from time import sleep
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_09_Copy:
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

    def test_09_copy_work_flow(self):
        """
        C52647812 - Verify end-to-end Flow of the reskinned 'Copy' Feature.
        1.Install and launch the app.
        2.Add the device on the root view and navigate to the device details screen.
        3.Perform the 'Copy' workflow. Observe the screen.
        Expected Result: The 'Copy' workflow should be reskinned as per the Figma design. 'Copy' functionality should perform as expected.
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
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_10_copy_for_flex_users(self):
        """
        C52715024 - Verify the end-to-end flow of the 'Copy' feature for 'Flex' users.
        1.Install and launch the app.
        2.Add the device on the root view and navigate to the device details screen.
        3.Perform the 'Copy' workflow. Observe the screen.
        Expected Result: The 'Copy' workflow should be reskinned as per the Figma design. 'Copy' functionality should perform as expected.
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
        self.digital_copy.select_num_of_copies(2)
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_option("original_size")
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_11_copy_for_hpplus_users(self):
        """
        C52716112 - Verify the end-to-end flow of the 'Copy' feature, when the user has 'HP+ ' account.
        1.Click on the 'Copy' tile.
        2.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        3.Select any value from the Copy button (From 1-99).
        4.Then click on the 'Start black/color button to print. Observe the screen.
        Expected Result: The user should be able to print successfully using the specified settings.
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

    def test_12_verify_copy_leave_popup(self):
        """
        C53016326 - Verify the 'Copy' feature, after clicking the 'Back' button on the 'Print Preview' screen.
        1.Click on the 'Copy' tile.
        2.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        6.Click on the 'Back' button and observe the screen.
        7.Click on the 'Cancel' button on the dialog. Observe the behavior.
        8.Again, click on the 'Back' button and click on the 'Leave' button. Observe the behavior.
        9.Then click on the 'Start black/color button to print. Observe the screen.
        Expected Result:The 'Are you sure?' pop-up window should be displayed as shown in the below screen.
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
        self.driver.back()
        self.print_preview.select_cancel_button()
        self.print_preview.verify_print_preview_screen()
        self.driver.back()
        self.digital_copy.verify_are_you_sure_popup()
        self.print_preview.select_leave_button()
        assert self.hpx_printer_details.click_copy_tile(raise_e=False)
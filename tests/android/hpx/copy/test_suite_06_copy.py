import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_06_Copy:
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
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.system_flow = cls.fc.flow[FLOW_NAMES.SYSTEM_FLOW]
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]
        cls.edit = cls.fc.fd["edit"]
        cls.fc.hpx = True

    def test_06_resize_with_original_size(self):
        """
        C51924696 - Verify the Functionality of Resize option select Original and see the pop up that says "The selected size of the original document is larger than the paper currently loaded in the printer" with OK Button.
        1,Tap on "Object Size" at the bottom right corner of the capture screen and select 4*6 in/10*15 cm or 5*7 in/13*18 cm.
        2,Tap on the "Capture" button.
        3,Select the Resize option as "Original Size"
        4,Print the captured image using the Black or Colour button option.
        5,Observe the screen.
        Expected Result:
        The user able to see the popup saying that "The selected size of the original document is larger than the paper currently loaded in the printer" with OK Button
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
        self.digital_copy.select_object_size_screen("digital_paper_size_5x7")
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_option("original_size")
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_resize_mismatch_screen()

    def test_07_copy_tile_when_user_signed_in(self):
        """
        C52631559 - Verify the 'Copy' feature with the user signed in
        1.Install and launch the app.
        2.Add the target device on the root view.
        3.Navigate to the device details page.
        4.Click on the 'Copy' tile.
        5.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        6.Click on start Black\Color button to print.
        7.Verify the behavior.
        8.In success model screen click on the 'Home' button.
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
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_08_copy_tile_user_allow_access(self):
        """
        C52636468 - Verify the 'Copy' feature after user allowing the camera access.
        1.Install and launch the app.
        2.Add the target device on the root view.
        3.Navigate to the device details page.
        4.Click on the 'Copy' tile.
        5.Click on the capture button in Manual or Auto mode to navigate to the print preview screen.
        6.Click on start Black\Color button to print.
        7.Verify the behavior.
        8.In success model screen click on the 'Home' button.
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
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    def test_09_copy_tile_user_allow_access(self):
        """
        C52636549 - Verify the 'Copy' feature, when the user captures an image using 'Manual' mode.
        1.Install and launch the app.
        2.Add the target device on the root view.
        3.Navigate to the device details page.
        4.Click on the 'Copy' tile.
        5.Capture an image in 'Manual' mode to navigate to the print preview screen.
        6.Click on start Black\Color button to print.
        7.Verify the behavior.
        Expected Result:The user should be able to print successfully without any error in 'Manual' mode.
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

    def test_10_resize_fill_page(self):
        """
        C53014634 - Verify the 'Copy' feature when the user selects the 'Fill Page' option from the 'Resize' option.
        1.Install and launch the app.
        2.Add the target device on the root view.
        3.Navigate to the device details page.
        4.Click on the 'Copy' tile.
        5.Click on the capture button in 'Manual' or 'Auto' mode to navigate to the print preview screen.
        6.Click on 'Resize' button.
        7.Select 'Fill Page' option and observe the print preview screen.
        8.Click on start Black\Color button to print.
        9.Verify the behavior.
        Expected Result:
        After step 7: The captured image should be resized to 'Fill Page' on the 'Print preview' screen.
        After step 9: The document should be printed successfully using the 'Fill Page'.
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
        self.digital_copy.select_resize_option("fill_page")
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_home_btn()

    
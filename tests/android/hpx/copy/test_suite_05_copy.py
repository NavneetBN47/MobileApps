import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_05_Copy:
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

    def test_01_object_size_select(self):
        """
        C51924691, C51949483 - Verify that the printed page's object size is set to A4 when the "Start Black" or "Start Colour" button is clicked.
        1,Tap on "Object Size" at the bottom right corner of the capture screen.
        2,Select the desired document size.
        3,Tap on the "Capture" button.
        4,Print the captured image using the Black or Colour option.
        Expected Result:
        The user is able to see that the image is printed successfully in A4 size and in Black or Colour.
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
        self.digital_copy.select_object_size_screen("digital_paper_size_letter")
        self.camera_scan.click_shutter()
        assert self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()

    def test_02_object_size_4x6_in_10x15(self):
        """
        C51924692, C51949484 - Verify that the printer page's object size is set to 4*6 in/10*15 cm when the "Start Black" or "Start Colour" button is clicked
        1,Tap on "Object Size" at the bottom right corner of the capture screen.
        2,Select the desired document size.
        3,Tap on the "Capture" button.
        4,Print the captured image using the Black or Colour option.
        Expected Result:
        The user is able to see that the image is printed successfully in 4*6 in/10*15 cm size and in Black or Colour.
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
        self.digital_copy.select_object_size_screen("digital_paper_size_4x6")
        self.camera_scan.click_shutter()
        self.print_preview.verify_print_preview_screen()
        for _ in range(2):
            self.print_preview.click_app_page_btn()
            self.camera_scan.click_shutter()
            self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_num_of_copies(3)
        self.digital_copy.select_start_color_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
        assert self.digital_copy.verify_home_btn()

    def test_03_object_size_5x7_in_13x18(self):
        """
        C51924693, C51949485 - Verify that the printer page's object size is set to 5*7 in/13*18 cm when the "Start Black" or "Start Colour" button is clicked
        1,Tap on "Object Size" at the bottom right corner of the capture screen.
        2,Select the desired document size.
        3,Tap on the "Capture" button.
        4,Print the captured image using the Black or Colour option.
        Expected Result:
        The user is able to see that the image is printed successfully in 5*7 in/13*18 cm size and in Black or Colour.
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
        assert self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()

    def test_04_object_size_id_card(self):
        """
        C51924694, C51949486 - Verify that the printer page's object size is set to ID Card when the "Start Black" or "Start Colour" button is clicked.
        1,Tap on "Object Size" at the bottom right corner of the capture screen.
        2,Select the desired document size.
        3,Tap on the "Capture" button.
        4,Print the captured image using the Black or Colour option.
        Expected Result:
        The user is able to see that the image is printed successfully in ID Card size and in Black or Colour.
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
        self.digital_copy.select_object_size_screen("digital_paper_size_driver_license")
        self.camera_scan.click_shutter()
        assert self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()

    def test_05_object_size_Business_card(self):
        """
        C51924695, C51949487 - Verify that the printer page's object size is set to Business Card when the "Start Black" or "Start Colour" button is clicked.
        1,Tap on "Object Size" at the bottom right corner of the capture screen.
        2,Select the desired document size.
        3,Tap on the "Capture" button.
        4,Print the captured image using the Black or Colour option.
        Expected Result:
        The user is able to see that the image is printed successfully in Business Card size and in Black or Colour.
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
        assert self.print_preview.verify_print_preview_screen()
        self.digital_copy.select_start_black_copy_btn()
        assert self.digital_copy.verify_sent_text_on_copy_preview_screen()
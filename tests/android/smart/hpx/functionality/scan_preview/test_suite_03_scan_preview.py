import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_Suite_03_Scan_Preview(object):
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
        cls.edit = cls.fc.fd["edit"]
        cls.fc.hpx = True

    def test_01_printing_from_scan_preview(self):
        """
        C44018926 - Verify printing is successful from Scan preview screen
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Print preview" button.
        4. Tap "Print" button.
        Expected Result:
        The job can be printed out successfully.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False, create_acc=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_print_preview_button()
        self.print_preview.click_print_btn()

    def test_02_android_save_ui(self):
        """
        C44018924 - (Android) Save UI
        1. Tap "Camera Scan" tile.
        2. Capture a document and go to preview screen.
        3. Tap "Save" button.
        4. Check the "Save" UI.
        5. Tap on File Type and observe the menu.
        6. Tap on Document size option and observe the menu.
        Expected Result:
        - The "Save" screen shows as per design with right font, color, padding, etc.
        - The menu font color, type, pop up and padding is as per Figma for File Type and Document size options.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_save_btn()
        self.print_preview.verify_save_and_share_option_title()
        self.preview.select_file_type()
        self.preview.verify_file_types([self.preview.IMAGE_JPG, self.preview.BASIC_PDF])
        self.preview.select_file_type(self.preview.BASIC_PDF)
        self.preview.verify_document_size(invisible=False)
        self.preview.verify_file_types([self.preview.PAPER_SIZE_5x7, self.preview.PAPER_SIZE_4x6, self.preview.PAPER_SIZE_A4, self.preview.PAPER_SIZE_LETTER, self.preview.PAPER_SIZE_LEGAL, self.preview.PAPER_SIZE_DRIVER_LICENSE, self.preview.IMAGE_JPG])

    def test_03_android_share_ui(self):
        """
        C44018925 - (Android) Share UI
        1. Tap "Camera Scan" tile.
        2. Capture a document and go to preview screen.
        3. Tap "Share" button.
        4. Check the "Share" UI.
        5. Tap on the options available like File Type, File Size, Document Size etc.
        Expected Result:
        - The "Share" screen shows as per design with right font, color, padding etc.
        - The menu font color, type, pop up and padding is as per Figma for all options.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.verify_save_and_share_option_title()
        self.preview.select_file_type()
        self.preview.verify_file_types([self.preview.IMAGE_JPG, self.preview.BASIC_PDF])
        self.preview.select_file_size()
        self.preview.verify_file_types([self.preview.FILE_SIZE_ACTUAL, self.preview.FILE_SIZE_SMALL, self.preview.FILE_SIZE_MEDIUM])
        self.print_preview.select_share_btn()

    def test_04_shortcuts_from_scan_preview(self):
        """
        C44018928 - Verify Shortcuts is successful from Scan preview screen
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Shortcuts" button.
        4. Select a shortcut from the list.
        Expected Result:
        Verify the shortcut job can be sent out successfully.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_shortcut_btn()
        self.print_preview.verify_shortcut_name_txt_btn()
        self.driver.click("shortcuts_image")
        self.hpx_shortcuts.verify_your_shortcut_is_running_title()

    def test_05_rotate_icon_at_bottom(self):
        """
        C44018929 - Rotate icon at bottom
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap the rotate icon at the bottom right corner of the image.
        Expected Result:
        Verify the image can be rotated correctly.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_rotate_page_btn()
        self.print_preview.click_on_image_selected_to_rotate()
        self.print_preview.verify_rotate_delete_btn()

    def test_06_print_preview_ui(self):
        """
        C44018930 - Scan First Flow: Verify Print Preview UI
        1. Tap scan tile.
        2. Perform a scan job and go to preview screen.
        3. Tap "Print Preview" button.
        Expected Result:
        1. The print preview screen is shown as per Figma/design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_print_preview_button()
        self.print_preview.verify_print_preview_ui()

    def test_07_mobile_fax_ui(self):
        """
        C44018931 - Scan First Flow: Verify Mobile Fax UI
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Mobile Fax" button.
        Expected Result:
        - For Android, the Mobile Fax UI is shown as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_on_fax(self.preview.FAX_BTN)
        self.print_preview.verify_fax_page()

    def test_08_shortcuts_ui(self):
        """
        C44018932 - Scan First Flow: Verify Shortcuts UI
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Shortcuts" button.
        Expected Result:
        1. When user is not signed in, the "Save time with shortcuts" UI displays as per design.
        2. (Android) The Shortcuts UI is shown as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_shortcut_btn()
        self.print_preview.verify_shortcuts_page()

    def test_09_print_settings_ui(self):
        """
        C44018935 - Scan First Flow: Verify Print Settings UI
        1. Tap scan tile.
        2. Complete the scan job to preview screen.
        3. Tap "Print Preview" button.
        4. Tap each option of print settings to check the UI.
        Expected Result:
        Verify the print settings can be shown as per Figma/design for Android and iOS.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_print_preview_button()
        self.driver.swipe()
        self.preview.click_print_settings_more_btn()
        self.print_preview.verify_print_preview_ui()
        self.print_preview.verify_paper_size_screen()
        self.print_preview.verify_options_on_photo_tab()
        self.print_preview.select_document_btn()
        self.print_preview.verify_doument_options()
	
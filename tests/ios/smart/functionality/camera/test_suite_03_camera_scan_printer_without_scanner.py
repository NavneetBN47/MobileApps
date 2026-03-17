import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_03_Camera_Scan_Printer_Without_Scanner(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]["username"]
        cls.camera = cls.fc.fd["camera"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.copy = cls.fc.fd["copy"]
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.ios_system = cls.fc.fd["ios_system"]
        cls.stack = request.config.getoption("--stack")

        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()

        request.addfinalizer(clean_up_class)

    @pytest.fixture(scope="function", autouse="true")
    def return_home(self):
        self.fc.go_home(reset=True, stack=self.stack)

    def test_02_verify_enable_access_to_camera(self):
        """
        C31299870   Precondition: fresh install
        1. add a printer and navigate to scan tile then tap on "Don't Allow" on the popup
        2. tap on the link 'Enable Access to Camera' and enable camera option in ios settings and go back to HP Smart
        Expected Results:
            - after verify the enable allow access screen
        :return:
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        self.camera.select_allow_access_to_camera_on_popup(allow_access=False)
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.camera.verify_allow_access_to_camera_text()
        self.camera.verify_enable_access_to_camera_link()
        self.copy.select_enable_access_to_camera_link_text()
        # set access in ios settings
        self.copy.enable_camera_access_toggle_in_settings()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.verify_home_tile()

    def test_05_verify_file_renaming_functionality(self):
        """
        C31299894 - Verify Save to HP Smart for camera scan
        C31299785 - Save captured image from camera scan
        C31299895, C31299869 - Ok/Go Home buttons behavior on your file has been saved pop up
        1. Take an image from the camera
        2. Tap on the save icon from toolbar and rename the image and save it to HP smart
        3. tap Home button and go to "files & photos" using bottom pane
        Expected results:
            - after step 3 verify that file is renamed successfully and exists in HP smart Files
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.fc.multiple_manual_camera_capture(1, flash_option=i_const.FLASH_MODE.FLASH_AUTO)
        file_name = self.test_05_verify_file_renaming_functionality.__name__
        self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.common_preview.SHARE_SAVE_TITLE, go_home=False)
        self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.common_preview.SHARE_SAVE_TITLE)
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.verify_file_name_exists("{}.jpg".format(file_name))

    def test_10_verify_print_functionality(self):
        """
        C31299784 - Print captured image from camera scan
        1. Select any printer and tap the Scan tile
        2. Select source as camera and perform manual image capture and go to print preview
        3. On the preview page, tap on print button
        Expected Results:
            - verify that print is successful
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(1, flash_option=i_const.FLASH_MODE.FLASH_AUTO)
        self.common_preview.dismiss_print_preview_coachmark()
        self.common_preview.dismiss_feedback_popup()
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_12_verify_zoom_mode(self):
        """
        C31299882
        1. Select a printer, tap on scan tile, take an image, tap on the preview image and cancel out of edit screen
        2. Back in preview screen, expand the preview image
        Expected Results:
            - verify user goes to edit screen after tapping on image preview
            - verify images goes into zoom mode after expanding preview image
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(1)
        self.common_preview.zoom_preview_image()
        self.common_preview.verify_zoomed_mode()

    def test_13_verify_preview_back_button_functionality(self):
        """
        C31299788 - Capture Images and tap back button from preview screen and leave
        1. Add a printer, tap the scan tile, take picture and go to preview screen
        2. Click the back button and then click the "Yes, Go Home" button
        Expected Results:
            - verify popup after clicking back button and selecting go home will redirect user home
        :return:
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(1)
        self.common_preview.select_navigate_back()
        self.common_preview.verify_exit_popup()
        self.common_preview.select_exit_popup_home_btn()
        self.home.verify_home_tile()

    def test_14_verify_source_elements_for_printer_without_scanner(self):
        """
        C37667651 - Verify source elements for printer without scanner
        1. Install and Open the HP Smart app
        2. Tap on the scan icon on navigation bar
        3. Tap on source
        Expected result: verify that the Source button has 
        - Files & Photos
        - Camera
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.verify_rootbar_scan_icon()
        self.home.select_scan_icon()
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.select_source_button()
        self.scan.verify_source_options_for_printer_without_scanner()
        if self.scan.verify_scan_source_btn(printer_name=self.printer_name, timeout=3, raise_e=False):
            pytest.skip("Scan source button is present while testing for printers without scanner")
        else:
            return True

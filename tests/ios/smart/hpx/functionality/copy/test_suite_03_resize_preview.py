import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_03_Resize_Preview:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.fc.hpx = True
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.camera = cls.fc.fd["camera"]
        cls.copy = cls.fc.fd["copy"]
        cls.preview = cls.fc.fd["preview"]

    def test_01_verify_copy_button(self):
        """
        Description: C51924672
        Click on Capture button and Click on Copy button in print preview screen.Verify the print preview screen.
        Expected Result:
            Pop up window should be displayed with 1-99 values.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_copy_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.copy.verify_manual_button()
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_number_of_copies(change_copies=5)
        self.copy.select_navigate_back()
        self.preview.select_yes_btn()

    def test_02_resize_popup_in_preview_screen(self):
        """
        Test Steps: C51924661
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Verify the resize popup is displayed.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_and_verify_options()
        self.driver.click(i_const.RESIZE.RESIZE_ORIGINAL_SIZE)
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_03_resize_original_size_and_verify_print_preview(self):
        """
        Test Steps: C51924662
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select original size.
        4. Verify the print preview screen is displayed.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_ORIGINAL_SIZE)
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_04_resize_original_size_and_verify_print_preview(self):
        """
        Test Steps: C51924663
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select Fit to page.
        4. Verify the print preview screen is displayed.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_FIT_TO_PAGE)
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_05_resize_original_size_and_verify_print_preview(self):
        """
        Test Steps: C51924664
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select fill page.
        4. Verify the print preview screen is displayed.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_FILL_PAGE)
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_06_resize_original_size_and_click_start_black(self):
        """
        Test Steps: C51924665
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select original size.
        4. Verify the print preview screen is displayed.
        5. Click on Start Black button and print.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_ORIGINAL_SIZE)
        self.copy.select_start_black()
        self.copy.select_ok_btn()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_07_resize_original_size_copy_count_and_click_start_back(self):
        """
        Test Steps: C51924666
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select original size ("_shared_original_size").
        4. Click on Copy button and select number of copies to be printed.
        5. Click on Start Black button and print.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_ORIGINAL_SIZE)
        self.copy.select_number_of_copies(change_copies=2)
        self.copy.select_start_black()
        self.copy.select_ok_btn()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_08_resize_fit_and_click_start_back(self):
        """
        Test Steps: C51924667
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select fit to page option.
        4. Click on Copy button and select number of copies to be printed.
        5. Click on Start Black button and print.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_FIT_TO_PAGE)
        self.copy.select_start_black()
        self.copy.select_ok_btn()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_09_resize_fit_to_page_copy_count_and_click_start_back(self):
        """
        Test Steps: C51924668
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select fit to page option.
        4. Click on Copy button and select number of copies to be printed.
        5. Click on Start Black button and print.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_FIT_TO_PAGE)
        self.copy.select_number_of_copies(change_copies=2)
        self.copy.select_start_black()
        self.copy.select_ok_btn()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_10_resize_fill_page_and_print_black(self):
        """
        Test Steps: C51924669
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select fill page option.
        4. Click on Start Black button and print.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_FILL_PAGE)
        self.copy.select_start_black()
        self.copy.select_ok_btn()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_11_resize_fill_page_copy_count_and_print_black(self):
        """
        Test Steps: C51924670
        1. Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select fill page option.
        4. Verify the print preview screen is displayed.
        5. Click on Copy button and select number of copies to be printed.
        6. Click on Start Black button and print.
        """
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_FILL_PAGE)
        self.copy.select_number_of_copies(change_copies=2)
        self.copy.select_start_black()
        self.copy.select_ok_btn()
        self.preview.select_navigate_back()
        self.preview.select_yes_btn()

    def test_12_resize_fill_page_copy_count_and_print_black(self):
        """
        Test Steps: C51924671
        1. Select the paper size(Ex: A4, 4X6 in /10X15cm) and Capture the image.
        2. Click on "Resize" button in preview screen.
        3. Select fill page option.
        4. Verify the print preview screen is displayed.
        5. Click on Start Black button and print.
        """
        self.copy.select_object_size(object_size=i_const.OBJECT_SIZE.SIZE_4x6)
        self.camera.select_capture_btn()
        self.copy.verify_copy_preview_screen()
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_ORIGINAL_SIZE)
        self.copy.select_start_black()
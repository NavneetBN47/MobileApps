"""
Copy flow and functionality smoke test suite for iOS
"""
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"


class Test_Suite_Smoke_09_Copy:
    """
    Copy flow class for smoke testing for iOS
    """

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.copy = cls.fc.fd["copy"]
        cls.camera = cls.fc.fd["camera"]
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        """
        Fixture setup for autouse of go_home function
        Verify navigation to home page after:
        1. App installation on the mobile device
        2. Clicking on Sign In on the ows screen and navigating to home page
        """
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_verify_copy_camera_screen_functionality(self):
        """
        C31297179 - Copy screen popup buttons
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        # verify X button
        self.copy.select_x_to_close()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_COPY)
        # check for flash modes
        modes = [attr for attr in dir(
            i_const.FLASH_MODE) if not attr.startswith("__")]
        for mode in modes:
            self.camera.select_flash_mode(getattr(i_const.FLASH_MODE, mode))
            self.camera.verify_flash_mode_state(
                getattr(i_const.FLASH_MODE, mode))
        # check for object size options
        obj_sizes = [attr for attr in dir(
            i_const.OBJECT_SIZE) if not attr.startswith("__")]
        for size in obj_sizes:
            self.copy.select_object_size(getattr(i_const.OBJECT_SIZE, size))

    def test_02_verify_add_copy_functionality(self):
        """
        C31297191, C31297190 - Copy - Add more pages
        C31297198, C31297199, C31297200, C31297201 - Verify start black functionality
        C31297392
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        # Add copy
        self.add_page_to_copy_screen(pages_scanned=2)
        self.copy.select_start_black()

    def test_03_copy_pages_delete_single_page(self):
        """
        C31297193 - Scan number_of_pages pages by Copy Tile; Delete single page;
                    Verify number_of_pages is visible and equals number_of_pages - 1
        C31297160, C31297194 - Exit Copy Preview Screen;
                    Verify for Object size clickable, Auto / Manual button, Capture button
        C31297192 - Scan number_of_pages=2 pages; Delete single page;
                    Verify for number_of_pages invisible
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        self.add_page_to_copy_screen(pages_scanned=2)
        self.add_page_to_copy_screen(pages_scanned=3)
        assert self.common_preview.verify_delete_page_x_icon()
        self.common_preview.select_delete_page_icon()
        self.common_preview.verify_preview_screen()
        assert self.common_preview.verify_preview_page_info()[1] == 2
        self.common_preview.select_delete_page_icon()
        self.common_preview.verify_preview_screen()
        self.common_preview.verify_preview_page_info(is_one_page=True)
        self.common_preview.select_navigate_back()
        self.copy.verify_copy_preview_screen_exit_popup()
        self.copy.select_yes()
        self.camera.verify_camera_screen()
        self.camera.verify_manual_btn()
        self.camera.verify_auto_btn()
        # check for object size options
        obj_sizes = [attr for attr in dir(
            i_const.OBJECT_SIZE) if not attr.startswith("__")]
        for size in obj_sizes:
            self.copy.select_object_size(getattr(i_const.OBJECT_SIZE, size))

    @pytest.mark.parametrize("pages_number, copies_number", [([1, 1]), ([2, 1]), ([2, 3])])
    def test_04_color_copy_by_pages(self, pages_number, copies_number):
        """
        C31297195, C31297196, C31297197 - By case: Add more pages and/or multiple copies
                                        - Click on Start Color button
        C31297187, C31297203            - Checking for Resize and Object Size buttons
                                            on multiple pages and copies
                                        - Click on any OBJECT Size
                                        - Click on RESIZE Original Size button
                                        - Click on Start Color button
        C31297391
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_object_size(i_const.OBJECT_SIZE.SIZE_LETTER)
        self.copy.select_capture_button()
        self.copy.verify_copy_preview_screen()
        if pages_number > 1:
            for i_pages_number in range(2, pages_number+1):
                self.add_page_to_copy_screen(pages_scanned=i_pages_number)
        if copies_number > 1:
            self.copy.select_number_of_copies(change_copies=copies_number)
        sizes = [attr for attr in dir(
            i_const.RESIZE) if not attr.startswith("__")]
        for size in sizes:
            self.copy.select_resize_in_digital_copy(
                getattr(i_const.RESIZE, size))
        self.copy.select_resize_in_digital_copy(
            i_const.RESIZE.RESIZE_ORIGINAL_SIZE)
        self.copy.select_start_color()

    def navigate_to_copy_screen(self):
        """
        Function defining the navigation to copy screen from home screen after adding printer
        """
        self.fc.go_to_home_screen()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.dismiss_tap_here_to_start()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_COPY)

    def add_page_to_copy_screen(self, pages_scanned=None):
        """
        Function defining the adding of page to the copy screen and capturing the image
        """
        self.common_preview.select_add_page()
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        if pages_scanned:
            assert self.common_preview.verify_preview_page_info()[
                1] == pages_scanned

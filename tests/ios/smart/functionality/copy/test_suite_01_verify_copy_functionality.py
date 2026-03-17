import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.copy import Copy
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_Verify_Copy_Functionality(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.copy = cls.fc.fd["copy"]
        cls.camera = cls.fc.fd["camera"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.ios_system = cls.fc.fd["ios_system"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.COPY_ELEMENTS = Copy.COPY_PREVIEW_ELEMENTS
        cls.fc.go_home(stack=cls.stack)
    
    def test_01_pop_up_for_allowing_access_to_camera_dont_allow(self):
        """
        C31297158 - Verify Pop up for allowing access to camera
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=False)
        self.copy.select_x_to_close()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_COPY)
        self.camera.verify_allow_access_to_camera_text()
        self.camera.verify_enable_access_to_camera_link()
        self.copy.select_enable_access_to_camera_link_text()
        # set access in ios settings
        self.copy.enable_camera_access_toggle_in_settings()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.fc.dismiss_tap_here_to_start()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_COPY)
        self.camera.verify_camera_screen()

    def test_02_copy_pop_up_when_printer_not_connected(self):
        """
        C31297157, C31297176 - Copy- Pop up when printer is not connected
        - Tap on "Copy" tile of the Home Screen.
        Result:
            Error pop up should display 
            Title: Feature Unavailable 
            Message: "Your printer is either offline....this feature"
            Button: OK
        - Tap on OK
        Result:
            Verify the popup is dismissed
        """
        self.fc.go_to_home_screen()
        self.fc.remove_default_paired_printer()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_COPY)
        self.home.select_ok()
        self.home.verify_home()

    def test_03_verify_pop_up_for_allowing_access_to_camera_ok_btn(self):
        """
        C31297159 - Pop up for allowing access to camera(OK button)
        Steps:
            1. Click on Copy Tile on Home screen
            For IOS:
            2. Click OK button on pop up.
        Result:
            - Verify the user should be allowed to access camera and Camera screen should open.
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_ui_elements_for_copy_functionality()

    def test_04_verify_copy_camera_screen_functionality(self):
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
        modes = [attr for attr in dir(i_const.FLASH_MODE) if not attr.startswith("__")]
        for mode in modes:
            self.camera.select_flash_mode(getattr(i_const.FLASH_MODE, mode))
            self.camera.verify_flash_mode_state(getattr(i_const.FLASH_MODE, mode))
        # check for object size options
        obj_sizes = [attr for attr in dir(i_const.OBJECT_SIZE) if not attr.startswith("__")]
        for size in obj_sizes:
            self.copy.select_object_size(getattr(i_const.OBJECT_SIZE, size))

    def test_05_verify_copy_preview_screen_functionality(self):
        """
        C31297183, C31297185, C31297184, C31297188, C31297189
         1. Load to Copy preview screen
         2. Click on Resize button
         3. Select Resize type on Resize screen
            + Original Size
            + Fit to page
            + Fill page
        Expected Result:
         2. Verify Resize screen with below points:
            + Original Size
            + Fit to page
            + Fill page
         3. Verify Copy screen
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        self.copy.verify_copy_preview_screen()
        self.copy.verify_array_of_elements(self.COPY_ELEMENTS)
        #verify number of copies functionality
        self.copy.select_number_of_copies(4)
        # Check for print RESIZE  options
        sizes = [attr for attr in dir(i_const.RESIZE) if not attr.startswith("__")]
        for size in sizes:
            self.copy.select_resize_in_digital_copy(getattr(i_const.RESIZE, size))

    def test_06_verify_pop_up_for_leaving_the_preview_screen(self):
        """
        C31297178 - Pop up for leaving the Preview screen
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        self.copy.select_navigate_back()
        self.copy.verify_copy_preview_screen_exit_popup()
        self.copy.select_no_option()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.copy.verify_copy_preview_screen_exit_popup()
        self.copy.select_yes()
        self.camera.verify_camera_screen()

    def test_07_verify_add_copy_functionality(self):
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

    def test_08_copy_pages_delete_single_page(self):
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
        obj_sizes = [attr for attr in dir(i_const.OBJECT_SIZE) if not attr.startswith("__")]
        for size in obj_sizes:
            self.copy.select_object_size(getattr(i_const.OBJECT_SIZE, size))

    @pytest.mark.parametrize("pages_number, copies_number", [([1,1]), ([2,1]), ([2,3])])
    def test_09_color_copy_by_pages(self, pages_number, copies_number):
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
        sizes = [attr for attr in dir(i_const.RESIZE) if not attr.startswith("__")]
        for size in sizes:
            self.copy.select_resize_in_digital_copy(getattr(i_const.RESIZE, size))
        self.copy.select_resize_in_digital_copy(i_const.RESIZE.RESIZE_ORIGINAL_SIZE)

        self.copy.select_start_color()

    def navigate_to_copy_screen(self):
        self.fc.go_to_home_screen()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.dismiss_tap_here_to_start()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_COPY)
    
    def add_page_to_copy_screen(self, pages_scanned=None):
        self.common_preview.select_add_page()
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        if pages_scanned:
            assert self.common_preview.verify_preview_page_info()[1] == pages_scanned

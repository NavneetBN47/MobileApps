import pytest
import datetime
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import HOME_TILES

pytest.app_info = "SMART"

class Test_Suite_03_Verify_Run_Shortcuts(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.preview = cls.fc.fd["preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.camera = cls.fc.fd["camera"]
        cls.photos = cls.fc.fd["photos"]
        cls.notifications = cls.fc.fd["notifications"]
        cls.fc.go_home(button_index=1, stack=cls.stack)
        cls.fc.add_printer_by_ip(printer_ip=cls.p.get_printer_information()["ip address"])
    
    def test_01_verify_shortcuts_through_camera_scan(self):
        """
        Requirements:
            1.C31461812 - Scan first flow > Preview page
            2.C31461813 - Scan first flow > "i" button behavior on Shortcuts preview page
            3.C31461814 - Scan first flow > Start shortcut behavior
        Steps:
            1.Launch HP Smart app
            2.Sign In to your account
            3.Get to Home page
            4.Tap on Camera Scan tile
            5.Capture a file
            6.Tap on "Next" on Adjust Boundaries
            7.Tap on Shortcuts
            8.Swipe up the shortcuts list
            9.Tap on "i" button on any shortcut
        Expected result:
            1. Document name section is present.
            2. List of existing shortcuts is present.
            3. Text in TextBox is alighned to left.
            4. The information coachmarks is aligned with each shortcuts.
            5. The information coachmarks are not moving when scroll the shortcuts list.
            6. Shortcut information is shown.
        """
        self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.select_scan_job_button(verify_messages=False)
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_toolbar_icon(self.preview.SMART_TASKS)
        self.shortcuts.verify_shortcuts_start_preview_screen(timeout=25)
        # only verifying info icon because of a defect
        self.shortcuts.verify_info_btn()
        self.shortcuts.click_start_btn()

    def test_02_verify_shortcuts_view_print(self):
        """
        Requirements:
            C31461815 - "View&Print" first flow > Start Shortcut behavior
            C31461816 - Document name on landing page
        Steps:
            1.Launch HP Smart app
            2.Sign In to your account
            3.Get to Home page
            4.Tap on View&Print tile
            5.Select a file
            6.Get to Preview page
            7.Tap on Shortcuts
            8.Tap on Start Shortcut... at any shortcut
        Expected results:
            1.shortcut execution started successfully
            2.Name section is shown and user can add name to shortcut
        """
        self.__add_shortcut()
        self.home.select_rootbar_view_and_print_icon()
        self.photos.select_allow_access_to_photos_popup()
        self.fc.select_photo_from_photo_picker()
        self.preview.handle_print_size_and_verify_print_preview_screen()
        self.preview.select_toolbar_icon(self.preview.SMART_TASKS)
        self.shortcuts.verify_shortcuts_start_preview_screen(timeout=20)
        self.shortcuts.verify_info_btn()
        self.shortcuts.click_start_btn()
        sleep(5)
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.verify_finish_shortcut_btn()

    def __add_shortcut(self):
        shortcuts_name = self.generate_shortcut_name("test")
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.fc.save_shortcut(shortcuts_name=shortcuts_name, invisible=True)
        if self.home.verify_close(raise_e=False):
            self.home.select_close()

    def generate_shortcut_name(self, name):
        return "{}_{:%Y_%m_%d_%H_%M_%S}".format(name, (datetime.datetime.now()))
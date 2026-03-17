import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_06_Copy:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.camera = cls.fc.fd["camera"]
        cls.copy = cls.fc.fd["copy"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_add_copy_functionality(self):
        """
        C31297191, C31297190 - Copy - Add more pages
        C31297198, C31297199, C31297200, C31297201 - Verify start black functionality
        C31297392
        Description: C50698995
            start_black_copy_with_multi_pages
                Load to Copy preview screen
                Click on Add more page button
                Click on Capture button with manual mode
                Click on 'Start Black' button

        Expected Result:
            Verify for following steps:
            4. Verify Copy sent screen with below points:
            + Sent! Message
            + Home button
            + Back button
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        # Add copy
        self.add_page_to_copy_screen(pages_scanned=2)
        self.copy.select_start_black()

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
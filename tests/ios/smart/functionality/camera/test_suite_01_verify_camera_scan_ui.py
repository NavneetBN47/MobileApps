import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_01_Verify_Camera_Scan_Ui(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)
    
    def test_01_verify_camera_ui_elements(self):
        """
        C31299872
        Precondition: fresh install
        Click camera tile and verify camera screen UI
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_ui_elements()
        self.camera.select_source_button()
        self.camera.verify_source_options()
        self.camera.select_source_option(self.camera.OPTION_CAMERA)
        self.camera.verify_preset_default_capture_mode()
        modes = [attr for attr in dir(i_const.FLASH_MODE) if not attr.startswith("__")]
        for mode in modes:
            self.camera.select_flash_mode(getattr(i_const.FLASH_MODE, mode))
            self.camera.verify_flash_mode_state(getattr(i_const.FLASH_MODE, mode))
    
    def test_02_verify_camera_ui_elements_hpplus(self):
        """
        C31299179
        Description:
            1 - Launch the app 
            2 - Sign in to HPID account
            3 - Navigate to app home screen
            4 - Tap on Camera scan tile or Camera scan in bottom navigation bar
            5 - Observe the UI under the capture area
        Expected Result:
            - Verify preset options on the slider
        """
        login_info = ma_misc.get_hpid_account_info(stack=self.stack, a_type="hp+", instant_ink=True)
        self.username, self.password = login_info["email"], login_info["password"]
        # TODO: reset takes a long time, can log out from regular user and login with hp+ user
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_ui_elements(acc_type="hpplus")
        self.camera.verify_preset_mode(self.camera.PHOTO)
        self.camera.verify_preset_mode(self.camera.DOCUMENT)
        self.camera.select_preset_mode(self.camera.BOOK)
        self.driver.restart_app(i_const.BUNDLE_ID.SMART)
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_preset_mode(self.camera.BOOK)
        self.camera.verify_preset_mode(self.camera.MULTI_ITEM)
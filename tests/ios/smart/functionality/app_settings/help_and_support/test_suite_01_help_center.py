import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Ios_Smart_Help_Center(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.help_support = cls.fc.fd["help_support"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_help_center(self):
        """
        IOS & MAC:
        C31297663, C33408325, C31297511
        Description:
            1. Launch the app
            2. Select 'App Settings' from Home Screen
            3. Select 'Help Center' under 'Help and Support'
        Expected Result:
            Verify the user is taken to Help Center screen with a Back button.
        """
        self.fc.go_home(stack=self.stack)
        self.home.select_app_settings()
        self.app_settings.select_help_center()
        self.help_support.verify_help_center_screen()
        if pytest.platform == "IOS":
            self.help_support.select_navigate_back()
        else:
            self.help_support.select_close_btn()
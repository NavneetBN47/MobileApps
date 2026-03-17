import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Not_Signed_In_Ui(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.settings = cls.fc.fd["app_settings"]

    def test_01_verify_delete_account_invisible(self):
        """
        TESTRAIL:
        C31504381: Delete Account invisible without sign in
        """
        self.fc.go_home(stack=self.stack, button_index=2)
        self.home.select_app_settings()
        self.settings.select_notification_n_privacy_option()
        self.settings.verify_delete_account_option(invisible=True)
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_02_create_account_ows(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_create_account_screen_ows(self):
        self.fc.verify_create_account_screen(stack=self.stack)

    def test_02_verify_create_account_ows(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=1, create_account=True)
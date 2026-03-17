import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"


class Test_Suite_03_HPX_MFE(object):
    
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_hpx_home_screen_verification(self):
        self.fc.go_home(stack=self.stack, button_index=2, enable_hpx_web_mfe=True)
        if pytest.platform == "MAC":
            self.fc.fd["home"].verify_home_screen_with_hpx_mfe_enabled()
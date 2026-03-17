import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_03_Hpid_Sigin(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_basic_account_sigin(self):
        self.fc.go_home(stack=self.stack)

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_02_veerify_account_signin(self, account_type):
        """
        Login with different HP users and verify home screen
        """
        account = ma_misc.get_hpid_account_info(stack=self.stack, a_type=account_type, instant_ink=True)
        self.fc.go_home(reset=True, stack=self.stack, username=account["email"], password=account["password"])
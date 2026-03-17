import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Smart_Dashboard_Printers_and_Users(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.hp_connect = cls.fc.fd["hp_connect"]
        cls.hpc_printers_users = cls.fc.fd["hpc_printers_users"]

    @pytest.mark.parametrize("account_type",["hp+", "ucde"])
    def test_01_printers_screen(self, account_type):
        """
            C28353790: Verify My printers screen (hp+)
            C28590354: Verify my printer's screen (ucde)
            1. Load to Home screen with hp plus account
            2. Click on Account button on navigation bar of Home screen
            3. Click on More option
            4. Click on Printers button
            5. Verify Printers screen
        """
        self.fc.load_account_and_go_to_smart_dashboard(stack=self.stack, account_type=account_type)
        self.hp_connect.click_menu_toggle()
        self.hpc_printers_users.click_printers_btn()
        self.hpc_printers_users.verify_printers_screen()
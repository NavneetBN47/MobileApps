import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_suite_02_Cec_Hp_Smart_Advance(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.cec = cls.fc.fd["cec"]
        cls.cec_home = cls.fc.fd["cec_home"]
        cls.p = load_printers_session

        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]

    @pytest.fixture(scope="function", autouse=True)
    def reset_app_go_home(self):
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)

    def test_01_hp_plus_user_signed_in(self):
        """
         C29690012
         Description:
         1. Load Home screen with a HP+ account login
         2. Click on See All button

        Expected Result:
         2. Verify below tiles show on CEC section:
            + Unlock cloud feature tile disappear
        """
        self.fc.add_printer_by_ip(self.p.get_printer_information()["ip address"])
        self.cec_home.click_see_all()
        self.cec.verify_unlock_cloud_features_tile(invisible=True)

    def test_02_try_camera_scan_learn_more(self):
        """
        C29707834:
        Description:
         1. Load Home screen with a HP+ account login
         2. Click on See All button
         3. Click on learn more button on Try camera scan tile
         4. Click on Back button

        Expected Result:
         2. Verify Camera scan tile on Do more with HP Smart screen
         3. Verify Try Camera scan screen
         4. Verify Camera scan tile on Do more with HP Smart screen
        """
        self.cec_home.click_see_all()
        self.cec.verify_try_camera_scan_tile()
        self.cec.click_try_camera_scan_tile()
        self.cec.verify_try_camera_scan_screen()
        self.cec.click_back_btn()
        self.cec.verify_try_camera_scan_tile()
        self.cec.click_try_camera_scan_close_btn()
        self.cec.verify_try_camera_scan_tile(invisible=True)

    def test_03_shortcuts_save_time_learn_more(self):
        """
        C29707834
         Description:
         1. Load Home screen with a HP+ account login
         2. Click on See All button
         3. Click on learn more button on Shortcuts save time tile
         4. Click on Back button

        Expected Result:
         2. Verify Shortcuts save time tile on Do more with HP Smart screen
         3. Verify Shortcuts save time screen
         4. Verify Shortcuts save time tile on Do more with HP Smart screen
        """
        self.cec_home.click_see_all()
        self.cec.verify_shortcuts_save_time_tile()
        self.cec.click_shortcuts_save_time_tile()
        self.cec.verify_shortcut_save_time_screen()
        self.cec.click_back_btn()
        self.cec.verify_shortcuts_save_time_tile()
        self.cec.click_shortcuts_save_time_close_btn()
        self.cec.verify_shortcuts_save_time_tile(invisible=True)
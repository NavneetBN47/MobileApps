import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_suite_01_Cec_Basic_Ui(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.cec_home = cls.fc.fd["cec_home"]
        cls.cec = cls.fc.fd["cec"]

    def test_01_verify_onboarding_from_cec_create_account(self):
        """
        C28761381, C29707835, C29692202, C29690021
        Description:
         1. Load Home screen without HPID login
         2. Click on See All button

        Expected Result:
         2. Verify below tiles won't show on CEC section if login with basic and ucde account:
            + User HP Smart Advance tile
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.cec_home.click_see_all()
        self.cec.verify_use_hp_smart_advance_tile(invisible=True)

        if self.stack == "stage":
            self.cec.verify_never_run_out_save_tile(invisible=False)
            self.cec.click_never_run_out_save_close_btn()
            self.cec.verify_never_run_out_save_tile(invisible=True)
        self.cec.verify_unlock_cloud_features_tile()
        self.cec.click_unlock_cloud_features_tile()
        self.cec.verify_create_account_or_sign_in_screen()
    
    def test_02_ucde_user_signed_in(self):
        """
        C29690014, C29692117
        Description:
         1. Load Home screen with ucde account login
         2. Make sure no printers add into carousel

        Expected Result:
         2. Verify below tiles won't show on CEC section if login with basic and ucde account:
            + User HP Smart Advance tile
        """
        login_info = ma_misc.get_hpid_account_info(stack=self.stack, a_type="ucde", instant_ink=True)
        self.username, self.password = login_info["email"], login_info["password"]
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(self.p.get_printer_information()["ip address"])
        self.cec_home.click_see_all()
        self.cec.verify_use_hp_smart_advance_tile(invisible=True)

        self.cec.verify_never_run_out_save_tile(invisible=True)
        self.cec.verify_unlock_cloud_features_tile(invisible=True)
        self.cec.verify_try_camera_scan_tile()
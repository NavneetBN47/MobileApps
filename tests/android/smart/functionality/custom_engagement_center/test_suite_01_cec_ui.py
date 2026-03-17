from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_CEC_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.cec = cls.fc.flow[FLOW_NAMES.CUSTOM_ENGAGEMENT_CENTER]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_user_onboarding_from_cec_create_account(self):
        """
        Description:
         1. Load Home screen without HPID login
         2. Click on Unlock cloud feature tile on Home screen
         3. Click on Create Account button
        Expected Result:
         1. Verify CEC will be show on the Home screen
            + Unlock cloud feature tile
         2. Verify Unlock cloud features screen
         3. Verify HPID login screen, and user can create a new HID account success
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.verify_hp_logo(timeout=10)
        self.cec.click_see_all()
        self.cec.verify_use_hp_smart_advance_tile(invisible=True)
        if self.stack == "stage":
            self.cec.verify_never_run_out_save_tile(invisible=False)
            self.cec.click_never_run_out_save_close_btn()
            self.cec.verify_never_run_out_save_tile(invisible=True)
        self.cec.verify_unlock_cloud_features_tile()
        self.cec.click_unlock_cloud_features_tile()
        self.cec.verify_create_account_or_sign_in_screen()

    def test_02_user_signed_in_ucde(self):
        """
        Description:
         1. Load Home screen with ucde account login
         2. Make sure no printers add into carousel

        Expected Result:
         2. Verify below tiles won't show on CEC section if login with basic and ucde account:
            + User HP Smart Advance tile
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer(invisible=False)
        self.cec.click_see_all()
        self.cec.verify_use_hp_smart_advance_tile(invisible=True)
        self.cec.verify_never_run_out_save_tile(invisible=True)
        self.cec.verify_unlock_cloud_features_tile(invisible=True)
        self.cec.verify_try_camera_scan_tile()
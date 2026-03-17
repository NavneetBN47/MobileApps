import pytest
import time
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_29_Sanity_Login(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
       
    @pytest.mark.smoke
    def test_01_verify_user_logout_C55516458(self):
        """
        Test Case: Verify User Logout in the HPX app
        
        Steps:
        Launch the HPX app.
        Ensure the user is logged in.
        Click on the Profile icon.
        Click on Settings.
        Click on the "Sign out" button.
        
        Expected Result:
        The user is logged out successfully.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/55516458
        """
        self.fc.launch_hpx_to_home_page()
        # The login account type depends on build stack.
        detected_stack = self.fc.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["stage"]
        elif detected_stack == "Prod":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        self.sign_in_email, self.sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]

        self.fc.fd["devicesMFE"].click_profile_button() 
        self.fc.sign_in(self.sign_in_email, self.sign_in_password, self.web_driver, sign_in_from_profile=True, send_before_click=False)
        self.fc.fd["devicesMFE"].verify_login_successfully()
        if self.fc.fd["devices_details_pc_mfe"].verify_pc_device_name_show_up(raise_e=False):
            self.fc.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up()
            time.sleep(5)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].verify_device_card_show_up()

        self.fc.sign_out(hpx_logout=True)

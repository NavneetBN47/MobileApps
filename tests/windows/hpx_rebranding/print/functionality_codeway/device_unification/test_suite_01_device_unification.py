import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_29_Sanity_Login(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session, logout_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name=cls.p.get_printer_information()["model name"]
      
    @pytest.mark.regression
    def test_01_verify_network_printer_not_removed_after_sign_out_C63798891_C63800216_C63805650(self):
        """
        1.The cloud printer is automatically added to the app and displayed in the device list.
        2.The HP account is signed out successfully and cloud printer is removed.
        3.Verify behavior when a guest user adds a printer locally, signs in with an account that has a different printer, and then signs out.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/63798891
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/63800216
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/63805650
        """
        self.fc.launch_hpx_to_home_page()
        # The login account type depends on build stack.
        detected_stack = self.fc.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["stage"]
        elif detected_stack == "Prod":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["prod"]
        self.sign_in_email, self.sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]

        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.sign_in(self.sign_in_email, self.sign_in_password, self.web_driver, send_before_click=False, min_win=True)
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["devicesMFE"].verify_login_successfully()
        
        # Check for cloud printer after successful login and track which one is found
        cloud_printer_model = None
        if self.fc.fd["devicesMFE"].verify_windows_dummy_printer('8030', raise_e=False):
            cloud_printer_model = '8030'
        elif self.fc.fd["devicesMFE"].verify_windows_dummy_printer('9010', raise_e=False):
            cloud_printer_model = '9010'
        self.fc.sign_out(hpx_logout=True)
        # Verify the cloud printer that was found during login is removed after sign out
        if cloud_printer_model:
            self.fc.fd["devicesMFE"].verify_windows_dummy_printer_removed(cloud_printer_model)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
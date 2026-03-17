import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_01_Print_Dashboard_Without_Sign_In(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session, chrome_account_data_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_print_dashboard_without_sign_in_C58418311_C58545281(self):
        """
        Sign-in screen should be displayed in external browser and not reflect in the HPX app.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/58418311
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/58545281
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
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_dashboard()
        self.fc.sign_in(self.sign_in_email, self.sign_in_password, self.web_driver, user_icon_click=False, send_before_click=False, min_win=True)
        self.fc.fd["devicesDetailsMFE"].verify_sign_in_btn()

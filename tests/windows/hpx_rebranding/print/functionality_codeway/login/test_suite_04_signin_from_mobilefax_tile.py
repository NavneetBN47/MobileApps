import pytest
from SAF.misc import saf_misc
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_04_Signin_From_Mobilefax_Tile(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session, logout_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.fc.web_password_credential_delete()
        cls.fc.kill_hpx_process()
        cls.printer_name=cls.p.get_printer_information()["model name"]

    @pytest.mark.regression
    def test_01_add_test_printer(self):
        """
        Add a test printer.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)

    @pytest.mark.regression
    def test_02_sign_in_from_mobilefax_C55536533(self):
        """
        Test Case: Verify sign in from mobile fax in the HPX app
        
        Steps:
        Open the HPX app.
        Click Mobile Fax → Sign In.
        
        Expected Result:
        Verify Sign In from the Mobile Fax in the HPX App
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/55536533
        """
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_mobile_fax_tile()
        self.fc.fd["mobilefax"].click_sign_in_btn()
        detected_stack = self.fc.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["adv_scan_stg"]
        else:
           detected_stack == "Prod"
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["adv_scan_prod"]
        self.sign_in_email, self.sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]
        self.fc.sign_in(self.sign_in_email, self.sign_in_password, self.web_driver, user_icon_click=False)
        sleep(3)
        self.fc.fd["mobilefax"].verify_mobile_fax_screen()
        self.fc.fd["mobilefax"].click_compose_fax_menu()
        self.fc.fd["mobilefax"].verify_compose_fax_menu_screen()

 
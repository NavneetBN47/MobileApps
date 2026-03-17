import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_Manage_Option:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.fc.hpx = True
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.welcome = cls.fc.fd["welcome"]

    def test_01_verify_manage_options_title(self):
        """
        Description: C41556542
                1. Fresh install and launch the app.
                2. Navigate to Data and Privacy screen.
                3. Tap on Manage Options button.
            Expected Result:
                3. Verify the user is directed to "Manage your preferences" screen.
        """
        self.fc.reset_hp_smart()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.click_manage_options()
        self.welcome.verify_manage_options_title()

    def test_02_click_and_verify_manage_options_back_btn(self):
        """
        Description: C41556545
                1. Fresh install and launch the app.
                2. Navigate to Welcome to HP Smart(App Consents) screen.
                3. Tap on Manage Options button.
                4. Tap on Back button on Manage your preferences page.
            Expected Result:
                4. Verify the user is back on App consents screen.
        """
        self.fc.reset_hp_smart()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.click_manage_options()
        self.welcome.verify_manage_options_title()
        self.welcome.click_manage_options_back_btn()
        self.welcome_web.verify_welcome_screen()

    def test_03_verify_decline_optional_data_option_C66708427(self):
        """
        Description: C66708427
                1. Fresh install and launch the app.
                2. Navigate to Welcome to HP Smart(App Consents) screen.
                3. Tap on Decline optional data button at bottom.
            Expected Result:
                3. Verify the user is directed to sign in page.
        """
        self.fc.reset_hp_smart()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.click_decline_optional_data_btn()
        self.fc.fd["ows_value_prop"].verify_sign_in_btn_hpx()

    def test_04_verify_accept_all_btn(self):
        """
        Description: C41556543
                1. Fresh install and launch the app.
                2. Navigate to Data and Privacy screen.
                3. Tap on Accept all button at bottom.
            Expected Result:
                3. Verify the user is directed to Sign in/Create account screen.
        """
        self.fc.reset_hp_smart()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.click_accept_all_btn()
        self.fc.fd["ows_value_prop"].verify_continue_as_guest_btn()
        self.fc.fd["ows_value_prop"].verify_sign_in_btn_hpx()
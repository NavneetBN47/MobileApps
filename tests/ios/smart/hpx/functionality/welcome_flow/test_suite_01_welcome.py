import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"

class Test_Suite_01_Welcome:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.fc.hpx = True

    def test_01_skip_signin_screen(self):
        """
        Description: C66193435, C50712699
                1. Launch MyHP App
                2. Tap on Accept all on App consents screen.
                3. Tap on Skip for now on sign in screen.
            Expected Result:
                3. Verify the user is navigated to root view screen without signing in.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.verify_hpx_home()

    def test_02_signin_in_value_prop_screen_C66253801(self):
        """
        Description: C66253801, C52900868
                1. Launch MyHP App
                2. Tap on Accept all on App consents screen.
                3. Tap 'Sign in' on value prop screen.
                4. Observe
            Expected Result:
                4. Verify the user is taken to existing sign in page. Verify that user is able to sign in successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=False)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.verify_hpx_home()

    def test_03_verify_continue_as_guest_button_in_value_prop_screen_C66253802(self):
        """
        Description: C66253802, C50712700
                1. Launch MyHP App
                2. Tap on Accept all on App consents screen.
                3. Tap 'Continue as guest' on value prop screen
                4. Observe
            Expected Result:
                4. Verify the user is taken to the rootview.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.verify_hpx_home()

    def test_04_verify_signin_in_value_prop_screen(self):
        """
        Description: C50712696
                1. Launch MyHP App
                2. Tap on Accept all on App consents screen.
                3. Tap 'Sign in' on HPX what's new popup.
                4. Observe
            Expected Result:
                4. Verify the user is taken to existing sign in page. Verify that user is able to sign in successfully.
        """
        self.fc.reset_hp_smart()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.click_accept_all_btn()
        self.home.allow_notifications_popup(raise_e=False)
        self.ows_value_prop.verify_continue_as_guest_btn()
        self.ows_value_prop.verify_sign_in_btn_hpx()
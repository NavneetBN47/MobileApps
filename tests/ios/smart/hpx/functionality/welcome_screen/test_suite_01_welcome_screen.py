import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_Welcome_Screen:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.fc.hpx = True
        cls.welcome = cls.fc.fd["welcome"]
        cls.welcome_web = cls.fc.fd["welcome_web"]

    def test_01_app_consents_screen_ui_your_data_and_privacy_screen(self):
        """
        Description: C49559984
            Fresh install and launch the app. 
            Observe the App Consents screen.
        Expected Result:
            Verifies the Welcome to HP Smart screen
        """
        self.fc.reset_hp_smart()
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.verify_decline_all_btn()
        self.welcome_web.verify_manage_options()

    def test_02_verify_behavior_of_manage_options_button_on_app_consents_screen(self):
        """
        Description: C49560734
            Fresh install and launch the app.
            User is on App Consents screen.
            Tap on Manage Options button.
        Expected Result:
            Verify the user is navigated to Manage choices screen
        """
        self.welcome_web.click_manage_options()
        self.welcome.verify_manage_options_title()
        assert self.welcome.get_manage_option_welcome_title() == "Manage your HP Smart privacy preferences", "The expected title is 'Manage your HP Smart privacy preferences' but the actual title is {}".format(self.welcome.get_manage_option_welcome_title())

    def test_03_verify_behavior_of_back_button_on_manage_choices_screen(self):
        """
        Description: C49560747
            Fresh install and launch the app.
            User is on App Consents screen.
            Tap on Manage Options button.
            Tap on Back button.
        Expected Result:
            Verify the user is navigated back to consent screen
        """
        self.welcome.click_manage_options_back_btn()
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.verify_decline_all_btn()
        self.welcome_web.verify_manage_options()

    def test_04_verify_behavior_of_continue_button_on_manage_choices_screen_C66708431(self):
        """
        Description: C66708431
            Fresh install and launch the app.
            User is on App Consents screen.
            Tap on Manage Options button.
            Tap on Continue button.
        Expected Result:
            Verify the user is navigated to Value prop screen.
        """
        self.welcome_web.click_manage_options()
        self.welcome.verify_manage_options_title()
        self.welcome.click_manage_options_continue_btn()
        self.fc.fd["ows_value_prop"].verify_continue_as_guest_btn()
        self.fc.fd["ows_value_prop"].verify_sign_in_btn_hpx()


    def test_05_verify_behavior_of_decline_all_button_on_app_consents_screen(self):
        """
        Description: C49560483
            Fresh install and launch the app.
            User is on App Consents screen.
            Tap on Decline All button.
        Expected Result:
            Verify the user is navigated to value prop screen.
        """
        self.fc.reset_hp_smart()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.click_decline_all_btn()
        self.fc.fd["ows_value_prop"].verify_continue_as_guest_btn()
        self.fc.fd["ows_value_prop"].verify_sign_in_btn_hpx()

    def test_06_verify_behavior_of_accept_all_button_on_app_consents_screen(self):
        """
        Description: C49560207
            Fresh install and launch the app.
            User is on App Consents screen.
            Tap on Accept All button.
        Expected Result:
            Verify the user is navigated to value prop screen.
        """
        self.fc.reset_hp_smart()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.click_accept_all_btn()
        self.fc.fd["ows_value_prop"].verify_continue_as_guest_btn()
        self.fc.fd["ows_value_prop"].verify_sign_in_btn_hpx()
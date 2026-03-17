import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time


pytest.app_info = "Smart"

class Test_Suite_01_Manage_Privacy_Settings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.web_smart_welcome = cls.fc.fd[FLOW_NAMES.WEB_SMART_WELCOME]
        cls.home = cls.fc.fd[FLOW_NAMES.HOME]
        #Enabling the HPX Flag
        cls.fc.hpx = True

    def test_01_verify_manage_privacy_settings_screen(self):
        """
        Description: C41556419
           App consents screen UI- Manage privacy settings screen
        Steps:
           Go through steps mentioned in Preconditions test case (first test case in this folder)
           Tap Manage privacy settings link
           Observe..
        Expected:
            Verify the UI for Manage privacy settings
            The UI matches the design
            All the links show as shown in design and are clickable
            All consents switchers show in disabled state by default
            Consent switchers can be toggled to On and Off states
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen()
        self.web_smart_welcome.click_manage_options()
        assert self.web_smart_welcome.is_app_analytics_toggle_disabled()
        assert self.web_smart_welcome.is_advertising_toggle_disabled()
        self.web_smart_welcome.click_app_analytics_toggle()
        self.web_smart_welcome.click_advertising_toggle()
        assert self.web_smart_welcome.verify_terms_of_use_link()
        assert self.web_smart_welcome.verify_eula_link()
        assert self.web_smart_welcome.verify_hp_privacy_statement_link()

    def test_02_verify_hp_privacy_statement_link_redirection(self):
        """
        Description: C41556422
           App consents screen UI- Manage privacy settings screen
        Steps:
            Go through steps mentioned in Preconditions test case (first test case in this folder)
            Navigate to Manage privacy settings screen
            Tap on HP Privacy Statement link
        Expected:
            Verify the user is directed to correct page
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen()
        self.web_smart_welcome.click_manage_options()
        self.web_smart_welcome.click_hp_privacy_statement_link()
        assert self.web_smart_welcome.verify_privacy_statement_page()
        assert self.web_smart_welcome.verify_privacy_statement_page() == 'OUR APPROACH TO PRIVACY ', "Expected title is : 'OUR APPROACH TO PRIVACY ' but found : {}".format(self.web_smart_welcome.verify_privacy_statement_page())

    def test_03_verify_hp_smart_terms_of_use_link_redirection(self):
        """
        Description: C41556538
           App consents screen UI- Manage privacy settings screen
        Steps:
            Go through steps mentioned in Preconditions test case (first test case in this folder)
            Navigate to Manage privacy settings screen
            Tap on HP Smart Terms of Use link
        Expected:
            Verify the user is directed to correct page
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen()
        self.web_smart_welcome.click_manage_options()
        self.web_smart_welcome.click_terms_of_use_link()
        assert self.web_smart_welcome.verify_terms_of_use_page()
        assert self.web_smart_welcome.verify_terms_of_use_page() == 'myHP Terms of Use – Worldwide', "Expected title is : 'myHP Terms of Use – Worldwide' but found : {}".format(self.web_smart_welcome.verify_terms_of_use_page())

    def test_04_verify_end_user_license_agreement_link_redirection(self):
        """
        Description: C41556539
           App consents screen UI- Manage privacy settings screen
        Steps:
            Go through steps mentioned in Preconditions test case (first test case in this folder)
            Navigate to Manage privacy settings screen
            Tap on End User License Agreement link
        Expected:
            Verify the user is directed to correct page
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen()
        self.web_smart_welcome.click_manage_options()
        self.web_smart_welcome.click_eula_link()
        assert self.web_smart_welcome.verify_eula_page()
        assert self.web_smart_welcome.verify_eula_page() == 'End-User License Agreement', "Expected title is : 'End-User License Agreement' but found : {}".format(self.web_smart_welcome.verify_eula_page())

    def test_05_verify_ui_for_manage_privacy_settings_page(self):
        """
        Description: C41556539
           App consents screen UI- Manage privacy settings screen
        Steps:
            Fresh install and launch the app
            User is on App Consents screen
            Tap on Manage Options button
        Expected:
            Verify the UI as per design
            Verify all consents switchers show in disabled state
            Verify the buttons 'Save' and 'Back' show at bottom
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen() 
        self.web_smart_welcome.click_manage_options()
        assert self.web_smart_welcome.is_app_analytics_toggle_disabled()
        assert self.web_smart_welcome.is_advertising_toggle_disabled()
        assert self.web_smart_welcome.verify_back_btn()
        assert self.web_smart_welcome.verify_continue_btn()

    def test_06_back_button_behavior(self):
        """
        Description: C41556545
           App consents screen UI- Manage privacy settings screen
        Steps:
            Fresh install and launch the app
            Navigate to Welcome to HP Smart(App Consents) screen
            Tap on Manage privacy settings button
            Tap on Back button on Manage privacy settings page
        Expected:
            Verify the user is back on App consents screen
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen() 
        self.web_smart_welcome.click_manage_options()
        self.web_smart_welcome.click_back_btn()
        assert self.web_smart_welcome.verify_manage_options()

    def test_07_save_button_behavior(self):
        """
        Description: C41556546
           App consents screen UI- Manage privacy settings screen
        Steps:
            Fresh install and launch the app
            Navigate to consents screen
            Tap on Manage privacy settings button
            Tap on Save button
        Expected:
            Verify the user is directed to Sign in/Create account value prop screen
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen()
        self.web_smart_welcome.click_manage_options()
        self.web_smart_welcome.click_continue_btn()
        assert self.home.verify_sign_in_btn()

    def test_08_verify_manage_options_button_behavior(self):
        """
        Description: C41556542
           App consents screen UI- Manage privacy settings screen
        Steps:
            Fresh install and launch the app
            Navigate to Data and Privacy screen
            Tap on Manage Options button
        Expected:
            Verify the UI as per design
            Verify all consents switchers show in disabled state
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.fc.check_is_home()
        self.web_smart_welcome.verify_welcome_screen() 
        self.web_smart_welcome.click_manage_options()
        assert self.web_smart_welcome.verify_manage_options()
        assert self.web_smart_welcome.is_app_analytics_toggle_disabled()
        assert self.web_smart_welcome.is_advertising_toggle_disabled()
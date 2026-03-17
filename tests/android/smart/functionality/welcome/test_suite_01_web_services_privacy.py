import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import LAUNCH_ACTIVITY

pytest.app_info = "SMART"

class Test_suite_01_Web_Service_Privacy(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.web_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]
        cls.value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.privacy_preference = cls.fc.flow[FLOW_NAMES.PRIVACY_PREFERENCES]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        #Defind variable
        cls.pkg_name = cls.fc.pkg_name
        cls.smart_context = cls.fc.smart_context

    def test_01_web_services_privacy_with_relaunch_app(self):
        """
        Description: C31298102
         1. Start app as first launch
         2. Relaunch app

        Expected Result:
         1. Webservice privacy of welcome screen
         2. Webservice privacy of welcome screen
                + There are 3 links
        """
        self.__load_app_first_screen_welcome()
        self.driver.terminate_app(self.pkg_name)
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.wait_for_context(self.smart_context, timeout=15)
        self.web_welcome.verify_welcome_screen()
        self.web_welcome.verify_manage_options()

    def test_02_term_of_use_link(self):
        """
        Description:
         1. Start app as first launch
         2. Click on HP Smart term of Usage link

        Expected Result:
         2. "Term of Use - Worldwide" screen
            https://www.hpsmart.com/us/en/tou
        """
        self.__load_app_first_screen_welcome()
        self.web_welcome.click_link(self.web_welcome.TERM_USE_LINK)
        if self.app_settings.verify_accept_cookies_popup(raise_e=False):
            self.app_settings.dismiss_accept_cookies_popup()
        self.web_welcome.verify_terms_of_use_page()

    def test_03_press_mobile_back_btn(self):
        """
        Description: C34746791
         1. Start app as first launch
         2. Press Back button of mobile device
         3. Launch app again

        Expected Result:
         2. Exit Android Smart app
         3.  Webservice privacy of welcome screen
        """
        self.__load_app_first_screen_welcome()
        self.driver.press_key_back()
        self.driver.terminate_app(self.pkg_name)
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.wait_for_context(self.smart_context, timeout=15)
        self.web_welcome.verify_welcome_screen()

    def test_04_verify_all_btn(self):
        """
        Description: C31298102, C31298106, C31298107, C31298108,  C31298112,  C31298111,  C31298110,  C31298109
        1. Launch the App
        2. HP Smart Suite and Web services (Privacy) screen is launched.
        3. Tap on "Accept All" Button
        4. Tap on "Manager Options" Button
        5. Click on Back button
        6. Click on Manager Options button
        7. Click on Continue button

        Expected Results:
        3. Verify tapping on "Accept All" Button should launch the OWS Value Prop Screen.
        4. Verify Tapping on "Manager Options" should launch "Manage Privacy Preferences" screen.
        7. Verify the OWS value prop screen
        """
        self.__load_app_first_screen_welcome()
        self.web_welcome.click_accept_all_btn()
        self.driver.wait_for_context(self.smart_context, timeout=40)
        self.value_prop.verify_ows_value_prop_screen(timeout=20)
        self.__load_app_first_screen_welcome()
        self.web_welcome.verify_manage_options()
        self.web_welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen()
        self.privacy_preference.click_back_btn()
        self.web_welcome.verify_welcome_screen()
        self.web_welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen()
        self.privacy_preference.click_continue()
        self.driver.wait_for_context(self.smart_context, timeout=10)
        self.value_prop.verify_ows_value_prop_screen(timeout=20)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_app_first_screen_welcome(self):
        """
        Load first screen of Welcome
        """
        self.fc.reset_app()
        self.fc.launch_smart()
        self.driver.wait_for_context(self.smart_context, timeout=10)
        self.web_welcome.verify_welcome_screen()
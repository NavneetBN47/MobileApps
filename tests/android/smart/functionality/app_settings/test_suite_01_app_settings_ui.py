from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import *

pytest.app_info = "SMART"

class Test_Suite_01_App_Settings_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.hpid_url = cls.fc.hpid_url 

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.about = cls.fc.flow[FLOW_NAMES.ABOUT]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.privacy_preferences = cls.fc.flow[FLOW_NAMES.PRIVACY_PREFERENCES]
        cls.smart_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_app_settings_ui_without_sign_in(self):
        """
        Description: C31297652, C31297654
         1. Load to Home screen (reset app to make sure not any hpc account logged in on App Settings screen)
         2. Click on 3 dots on the screen
         3. Click on App Settings
        Expected Result:
         3. Verify App Settings screen without hpc account logged in:
            + Title
            + Sign In button
        """
        self.__load_app_settings_screen()
        self.app_settings.verify_app_settings()
        self.app_settings.verify_sign_in_btn()

    def test_02_app_settings_help_center(self):
        """
        Description: C31297663, C31297511, C33408325
         1. Load Home screen
         2. Click on App Settings icon from navigation bar of Home screen
         3. Click on Help Center button
        Expected Result:
         3. Verify Welcome to HP Smart App Help and Support screen popup on chrome browser
        """
        self.__load_app_settings_screen(is_nav_app_settings_btn=True)
        self.app_settings.select_app_settings_opt(self.app_settings.HELP_CENTER)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    @pytest.mark.parametrize("app_settings_opt", ["about", "use_5ghz_wifi", "notification_and_privacy"])
    def test_03_app_settings_opt_verify(self, app_settings_opt):
        """
        Description: C31297658, C31297655, C31297662
         1. Load Home screen
         2. Click on App Settings from more option screen
         3. Click on the item on App Settings screen:
            - About
            - Use 5GHz WiFi
            - Notifications and Privacy
        Expected Result:
         3. Verify each item screen
            - About screen
            - Use 5GHz WiFi screen
            - Notifications and Privacy screen
        """
        app_settings_opts = {"about": self.app_settings.ABOUT,
                             "use_5ghz_wifi": self.app_settings.USE_5GHZ_WIFI,
                             "notification_and_privacy": self.app_settings.NOTIFICATIONS_AND_PRIVACY,
                      }
        self.__load_app_settings_screen(is_nav_app_settings_btn=True)
        self.app_settings.select_app_settings_opt(app_settings_opts[app_settings_opt])
        if app_settings_opt == "about":
            self.about.verify_about_screen()
        elif app_settings_opt == "use_5ghz_wifi":
            self.app_settings.verify_notification_privacy_opt_screen(self.app_settings.USE_5GHZ_WIFI)
            self.app_settings.toggle_on_off_btn(enable=True)
        else:
            self.app_settings.verify_notification_privacy_screen()

    def test_04_notification_and_pricy_opt_verify(self):
        """
        Description: C31297657, C31297655, C31297656
         1. Load to App Settings screen
         2. Click on Notifications and Privacy
         3. Click on each item on Notifications and Privacy screen:
            - Supply Status

        Expected Result:
         3. Verify each item's screen with below points:
            + Title
            + On/Off Switch icon
            + Message
        """
        self.__load_app_settings_screen()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(self.app_settings.SUPPLY_STATUS)
        self.app_settings.verify_notification_privacy_opt_screen(self.app_settings.SUPPLY_STATUS)

    @pytest.mark.parametrize("opt_name", ["sign_out_success", "cancel_sign_out"])
    def test_05_app_settings_hpc_account_sign_out_options(self, opt_name):
        """
        Description: C31297653, C31297659, C31297660
         1. Load to App Settings screen with account signed in
         2. Click on Sign In button
         3. Enter account email and pwd
         4. Click on Sign Out button on App Settings screen
         5. Click on Sign Out button
        Expected Result:
         3. Verify App Settings screen with below points:
            + Title
            + Sign In button
            + Account Information
         5. Verify App Settings screen with below points:
            + Title
            + Sign In button
        """
        self.fc.reset_app()
        self.__load_app_settings_screen(is_nav_app_settings_btn=True)
        self.fc.flow_app_settings_sign_in_hpid()
        if opt_name == "sign_out_success":
            self.app_settings.sign_out_hpc_acc()
            self.app_settings.verify_app_settings()
        else:
            self.app_settings.click_sign_out_btn()
            self.app_settings.click_cancel_btn()
            self.app_settings.verify_app_settings_with_hpc_account(self.driver.session_data["hpid_user"])

    def test_06_app_settings_hpc_account_sign_in_cancel(self):
        """
        Description: C33416285
         1. Load to App Settings screen without account sign in
         2. Click on Sign In button
         3. Click on Close button on Sign in page
        Expected Result:
         3. Verify App Settings screen with below points:
            + Title
            + Sign In button
        """
        self.fc.reset_app()
        self.__load_app_settings_screen()
        self.app_settings.click_sign_in_btn()
        self.chrome.handle_welcome_screen_if_present()
        self.driver.switch_to_webview(webview_url=self.hpid_url)
        self.hpid.verify_hp_id_sign_in()
        self.chrome.click_webview_close_btn()
        if self.app_settings.verify_having_trouble_sigining(raise_e=False):
            self.app_settings.click_close_button()
        #App need to take sometime to go back App settings screen from HPID login cancel screen
        self.app_settings.verify_app_settings(timeout=20)

    def test_07_app_settings_privacy_preferences(self):
        """
        Description: C31297668, C31297671
        1. Launch the App and Tap on Manage Options
        2. Click on Manage my Privacy Settings button
        3. Click on Save button

        Expected Result:
        2. Verify Manage your HP Smart privacy preferences screen
        3. Verify Notifications abd Privacy screen
        """
        self.__load_app_settings_screen()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(self.app_settings.MANAGEMENT_MY_PERSONALIZED_PROMOTIONS)
        self.privacy_preferences.verify_privacy_preference_screen()
        self.privacy_preferences.click_continue()
        self.app_settings.verify_notification_privacy_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_app_settings_screen(self, is_nav_app_settings_btn=False):
        """
        If current screen is not Home screen, load to Home screen.
        Click on 3 dots on Home screen
        Click on App Settings icon
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        if is_nav_app_settings_btn:
            self.home.select_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN)
        else:
            self.home.select_more_options_app_settings()
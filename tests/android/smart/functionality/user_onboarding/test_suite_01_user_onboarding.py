from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_User_Onboarding(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.notification = cls.fc.flow[FLOW_NAMES.NOTIFICATION]
        cls.ows_value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.privacy_preferences = cls.fc.flow[FLOW_NAMES.PRIVACY_PREFERENCES]
        cls.smb = cls.fc.flow[FLOW_NAMES.SMB]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        # Define the variable
        cls.smart_context = cls.fc.smart_context  
        cls.hpid_url = cls.fc.hpid_url
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    @pytest.mark.parametrize("sign_type",["new_account", "existed_account"])
    def test_01_create_account_sign_in(self, sign_type):
        """
        Description: C28073477, C28073476, C27864743
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on Account button
         3. If sign_type == "existed_account": then Sign In an HPID account
            If sign_type == "new_account", then Login with a new HPID account
        Expected Result:
         3. Verify HPID create new account screen:
         3. Verify Home screen with account login success:
            - Buttons on navigation bar are visible: Printer Scan / Camera Scan / View & Print
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.switch_to_webview(webview_url=self.hpid_url)
        if not self.hpid.verify_hp_id_sign_up(raise_e=False):
            self.hpid.click_create_account_link()
        self.hpid.verify_hp_id_sign_up()
        if sign_type == "existed_account":
            self.hpid.click_sign_in_link_from_create_account()
            self.hpid.verify_hp_id_sign_in()
            self.hpid.login()
            if self.smb.select_my_printers(raise_e=False):
                self.smb.select_continue()
        else:
            self.hpid.create_account()
        #After UCDE privacy screen, app still will take some time to load to HPID information before go to next screen
        self.home.verify_bottom_nav_btn(btn=self.home.NAV_PRINTER_SCAN_BTN, timeout=20)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)

    def test_02_sign_in_from_app_settings(self):
        """
        Description: C27212800
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on App Settings
         3. Click on Sign In button
         4. Login an HPID account
         5. Click on Back button from App Settings
        Expected Result:
         5. Verify Home screen with account login success:
            - Buttons on navigation bar are visible: Printer Scan / Camera Scan / View & Print
        """
        self.fc.flow_home_sign_in_hpid_account()
        self.fc.select_back()
        self.home.verify_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)

    def test_03_user_onboarding_not_offered_again(self):
        """
        Description: C27212766
         1. Load Home screen with user onboarding account login
         2. Click on Print Photos tile

        Expected Result:
         2. Verify View & Print screen
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.file_photos.verify_limited_access_popup()
        self.file_photos.select_continue_btn()
        self.local_photos.verify_photo_picker_optional_screen(raise_e=False)

    def test_04_personalized_promotions(self):
        """
        Description: C27891989
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on App Settings
         3. Click on Notification and Privacy
         4. Click on Manage my Personalized Promotions consent
         5. Click on Sign In button
         6. Login with an HPID account
        Expected Result:
         5. Verify HPID create new account screen
         6. Verify Privacy Setting screen with webview mode
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_app_settings()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(self.app_settings.MANAGEMENT_MY_PERSONALIZED_PROMOTIONS)
        self.driver.wait_for_context(self.smart_context, timeout=15)
        self.privacy_preferences.verify_privacy_preference_screen(timeout=15)

    def test_05_signin_btn_validation(self):
        """
        Description: C28800002
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on Sign In button from Home screen
         3. login HPID

        Expected Result:
         2. Verify HPID sign in screen
         3. HPID should be able to login success
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_bottom_nav_btn(self.home.NAV_SIGN_IN_BTN)
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.switch_to_webview(webview_url=self.hpid_url)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.verify_bottom_nav_btn(btn=self.home.NAV_PRINTER_SCAN_BTN, timeout=20)

    def test_06_user_onboarding_close(self):
        """
        Description: C28073479
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on Camera Scan tile, and allow the permission if permission screen popup
         3. Click on Close button

        Expected Result:
         2. Verify OWS value prop screen
         3. Verify Home screen
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True, simple=False, timeout=20)
        self.ows_value_prop.select_value_prop_buttons(index=2)
        self.home.verify_home_nav()

    def test_07_user_onboarding_from_notification(self):
        """
        Description: C28536123, C28536124
        1. Launch Smart app without HPID login
        2. Tap on bell icon from Home page to go to Notification page
        3. Click on Supplies item from Notification screen
        4. Click on Close button
        5. Click on Account item from Notification screen
        6. Click on Close button

        Expected Results:
        3. Verify ows value prop screen
        4. Verify Notifications screen
        5. Verify ows value prop screen
        6. Verify Notifications screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_notifications_icon()
        self.notification.select_supplies()
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True, simple=False, timeout=20)
        self.ows_value_prop.select_value_prop_buttons(index=2)
        self.notification.verify_notification_screen()
        self.notification.select_account()
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True, simple=False, timeout=20)
        self.ows_value_prop.select_value_prop_buttons(index=2)
        self.notification.verify_notification_screen()
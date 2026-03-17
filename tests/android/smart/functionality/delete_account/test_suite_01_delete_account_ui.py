from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
import time

pytest.app_info = "SMART"

class Test_Suite_01_Delete_Account_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.hpid_url = cls.fc.hpid_url 

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_delete_account_ui_without_sign_in(self):
        """
        Description: C31504381
         1. Load to Home screen (reset app to make sure not any hpc account logged in on App Settings screen)
         2. Click on 3 dots on the screen
         3. Click on App Settings
         4. Click on Notifications and Privacy

        Expected Result:
         3. Verify the delete account option doesn't display on Notifications and Privacy screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_app_settings()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.verify_delete_account_item(invisible=True)

    def test_02_delete_account_ui_without_active_subscription(self):
        """
        Description: C31504378, C31504379, C31504385, C31504386, C31504394, C31738107, C31504397, C31504399, C31504398, C315004392, C315004390, C315004389, C315004387, C36679068
                     C33556892, C33556894, C33556900, C33556901, C33556902
         1. Load Home screen with a new HPID account
         2. Add a printer to the carousel
         3. Click on App Settings icon from navigation bar of Home screen
         4. Click on Notifications and Privacy
         5. Click on Delete Account button
         6. Click on No, keep account button
         7. Click on Delete Account button
         8. Click on Delete Account button
         9. Click on Done button
         10. CLick on back button
         11. Click on Back button
         12. Click on Sign In button
         13. Type same account information from step1
         14. Click on Shortcuts tile

        Expected Result:
         5. Verify Delete HP Smart account screen
         6. Verify Notification and Privacy screen
         8. Verify HP Smart account has been deleted screen
         9. Verify Notification and Privacy screen without delete account button
         11. Verify Home screen without HPID login, verify the printer still is in carousel
         13. Verify the user is able to login again
         14. User is able to go to Shortcuts screen with this new account
        """
        self.fc.reset_app()
        username, password = self.fc.flow_load_home_screen(create_acc=True)
        self.home.select_more_options_app_settings()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.verify_delete_account_item(invisible=False)
        self.app_settings.select_notification_privacy_opt(self.app_settings.DELETE_ACCOUNT)
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.hp_connect.select_no_keep_account_btn()
        self.app_settings.verify_notification_privacy_screen()
        self.app_settings.select_notification_privacy_opt(self.app_settings.DELETE_ACCOUNT)
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.hp_connect.select_delete_account_btn()
        self.hp_connect.verify_hp_smart_account_has_been_deleted_screen()
        self.hp_connect.select_done_btn()
        self.app_settings.verify_notification_privacy_screen(timeout=20)
        self.fc.select_back()
        self.app_settings.click_sign_in_btn()
        time.sleep(7)
        self.google_chrome.handle_welcome_screen_if_present()
        # Should be a the sign in page now and continue signing in with the account i want
        self.driver.switch_to_webview(webview_url=self.hpid_url)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(username, password)
        self.app_settings.verify_app_settings_with_hpc_account(username, timeout=30, raise_e=True)
        self.fc.select_back()
        self.home.verify_home_nav()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.SMART_TASKS))
        self.shortcuts.verify_shortcuts_screen(timeout=20)

    def test_03_delete_account_ui_with_active_subscription(self):
        """
        Description:  C31504396, C31504393, C31504382
         1. Load Home screen with an HPID account which has active subscription
         2. Click on App Settings from more option screen
         3. Click on Notifications and Privacy
         4. Click on Delete Account button
         5. Click on Delete Account button
         6. Click on Open Dashboard button

        Expected Result:
         5. Verify You must cancel services screen
         6. Verify Smart Dashboard screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_more_options_app_settings()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(self.app_settings.DELETE_ACCOUNT)
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.hp_connect.select_delete_account_btn()
        self.hp_connect.verify_you_must_be_cancel_service_screen()
        self.hp_connect.select_open_dashboard_btn()
        #Should verify the Smart Dashboard screen after above step, but now it's blockec by CR SDASH-7840

    def test_04_user_is_unable_to_create_new_account_with_same_deleted_account(self):
        """
        Description: C31504391
         1. Load Home screen with a new HPID account
         2. Click on App Settings icon from navigation bar of Home screen
         3. Click on Notifications and Privacy
         4. Click on Delete Account button
         5. Click on Delete Account button
         6. Click on Done button
         7. CLick on back button
         8. Click on Back button
         9. Click on Create Account button
         10. Type same account information from step1

        Expected Result:
        10. Verify the user cannot create a new account with same deleted account
        """
        self.fc.reset_app()
        username, password = self.fc.flow_load_home_screen(create_acc=True)
        self.home.select_more_options_app_settings()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.verify_delete_account_item(invisible=False)
        self.app_settings.select_notification_privacy_opt(self.app_settings.DELETE_ACCOUNT)
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.hp_connect.select_delete_account_btn()
        self.hp_connect.verify_hp_smart_account_has_been_deleted_screen()
        self.hp_connect.select_done_btn()
        self.app_settings.verify_notification_privacy_screen(timeout=20)
        self.fc.select_back()
        self.app_settings.click_create_account_btn()
        time.sleep(7)
        self.google_chrome.handle_welcome_screen_if_present()
        # Should be a the sign in page now and continue signing in with the account i want
        self.driver.switch_to_webview(webview_url=self.hpid_url)
        self.hpid.verify_hp_id_sign_up()
        self.hpid.verify_unable_to_create_account(email=username, password=password)
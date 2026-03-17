import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES

pytest.app_info = "SMART"

class Test_suite_01_home_nav_notification(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.notification = cls.fc.flow[FLOW_NAMES.NOTIFICATION]
        cls.hpps = cls.fc.flow[FLOW_NAMES.HPPS]
        cls.web_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]
        cls.fax_history = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.smart_context = cls.fc.smart_context
        cls.hp_connect_account = cls.fc.flow[FLOW_NAMES.HP_CONNECT_ACCOUNT]
        cls.shortcuts_notification = cls.fc.flow[FLOW_NAMES.SHORTCUTS_NOTIFICATION]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_home_nav_notifications_btn(self):
        """
        Description: C31297136
        1. Tap on bell icon from Home page to go to Notification page

        Expected Results:
        1.Verify notification page
           Verify "Mobile Fax" and "Smart Task" options under Activity tab
           Verify "Supplies" and "Account" options under Activity tab
        """
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.verify_mobile_fax_option()
        self.notification.verify_shortcuts_option()
        self.notification.verify_supplies_option()
        self.notification.verify_account_option()

    def test_02_verify_mobile_fax_activity_user_logged_out(self):
        """
        Description: C31297150, C31297152, C31297153, C31297155, C27864739
        Steps:
        1.Install and launch app.
        2.Add printer to the carousel
        3.Make sure user is logged in into App settings (HPID)
        4.Tap on bell icon from Home page to go to Notification page
        5.Tap on "Mobile Fax" option under "Activity" tab
        6.Now go to App Settings and Log out
        7.Tap on the bell icon from Home page to go to Notification page
        8.Tap on "Mobile Fax" option under "Activity" Tab

        Expected Results:
        5. Verify Mobile Fax screen
        8. Value Prop screen to Create Account or login HPID.
        """
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_mobile_fax()
        self.fax_history.verify_fax_history_screen(invisible=False, timeout=25)
        self.fc.flow_home_log_out_hpid_from_app_settings()
        self.driver.back()
        self.home.select_notifications_icon()
        self.notification.select_mobile_fax()
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.value_prop.verify_ows_value_prop_screen(tile=True)

    def test_03_shortcuts_from_notification(self):
        """
        Description: C31297137, C31297140, C33611220, C27735802
        1. Login HPID which has Shortcuts in the list
        2. Tap on bell icon from Home page to go to Notification page
        3. Click on Shortcuts item from Notification screen
        4. Click on Back button

        Expected Results:
        3. Verify Shortcuts screen with a shortcuts list
        4. Verify Notification screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_shortcuts()
        self.shortcuts_notification.verify_shortcuts_list_from_notification()
        self.driver.press_key_back()
        self.notification.verify_notification_screen()

    def test_04_no_shortcuts_activity_screen(self):
        """
        Description: C31297138, C33610701
        1. Launch Smart app with new HPID account
        2. Tap on bell icon from Home page to go to Notification page
        3. Click on Shortcuts item from Notification screen

        Expected Results:
        3. Verify Shortcuts screen with an empty shortcuts list
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(create_acc=True)
        self.home.select_notifications_icon()
        self.notification.select_shortcuts()
        self.shortcuts_notification.verify_no_shortcut_activity_available_msg()

    def test_05_supplies_account(self):
        """
        Description: C33626429, C33626430
        1. Launch Smart app with new HPID account
        2. Tap on bell icon from Home page to go to Notification page
        3. Click on Supplies item from Notification screen

        Expected Results:
        3. Verify View Notification screen
        """
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_supplies()
        self.hp_connect_account.verify_view_notifications_screen()
        self.driver.press_key_back()
        self.notification.select_account()
        self.hp_connect_account.verify_view_notifications_screen()
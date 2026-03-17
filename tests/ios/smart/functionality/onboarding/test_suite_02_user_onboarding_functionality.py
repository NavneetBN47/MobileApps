import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const


pytest.app_info = "SMART"

class Test_Suite_02_User_Onboarding_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.privacy_preferences = cls.fc.fd["privacy_preferences"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_notification_onboarding(self):
        """
        C27864739: User Onboarding from Mobile Fax notifications view
        C27735802: User On-boarding from "Print Photos" Tile On new Install
        C28536123: User Onboarding from Account notifications view
        C28536124: User Onboarding from Supplies notifications view
        """
        self.fc.go_home(stack=self.stack, button_index=2)
        self.home.verify_notification_bell()
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        for tab in self.home.ACTIVITY_TABS:
            sleep(5)
            self.home.verify_an_element_and_click(tab)
            self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
            self.ows_value_prop.select_value_prop_buttons(index=2)

    def test_02_create_account_app_settings(self):
        '''
        C28370571: create account button under app settings
        skip value prop screen
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_settings_icon()
        assert self.app_settings.verify_create_account_btn()
        self.app_settings.select_create_account_btn()
        sleep(5)
        self.hpid.handle_privacy_popup()
        assert self.hpid.verify_create_an_account_page()

    def test_03_signin_btn_validation(self):
        '''
        C28370572: signin btn is available under bottom nav bar if not signed in
        should skip value prop screen
        C28800002: signin screen
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        assert self.home.verify_sign_in_icon()
        self.home.select_sign_in_icon()
        self.hpid.handle_privacy_popup()
        self.driver.wait_for_context(self.fc.hpid_url, timeout=60)

    def test_04_onboarding_personalize_promotion_link(self):
        '''
        C28873934: Manage my Privacy Settings
        C27891989: user onboarding personalize promotion link
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_settings_icon()
        self.app_settings.select_notification_n_privacy_option()
        self.app_settings.select_manage_privacy_settings_option()
        self.privacy_preferences.verify_privacy_preference_screen()

    def test_05_cancel_onboarding_app_settings(self):
        '''
        C27735800: cancel onboarding to UCDE
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_settings_icon()
        assert self.app_settings.verify_sign_in_option()
        self.app_settings.select_sign_in_option()
        self.driver.restart_app(i_const.BUNDLE_ID.SMART)
        self.home.select_settings_icon()
        assert self.app_settings.verify_sign_in_option()

    def test_06_create_account_app_settings_and_creation_of_smart_task(self):
        """
        C28299209: Validate successful user Onboarding from App settings and creation of Smart Task
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.verify_bottom_navigation_bar_icons(signed_in=False)
        self.home.select_app_settings()
        self.app_settings.select_create_account_btn()
        self.fc.create_new_user_account(timeout=30)
        self.app_settings.verify_bottom_navigation_bar_icons()
        self.home.select_home_icon()
        self.fc.clear_popups_on_first_login(smart_task=True)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_SMART_TASK)
        self.shortcuts.verify_shortcuts_screen(timeout=35)

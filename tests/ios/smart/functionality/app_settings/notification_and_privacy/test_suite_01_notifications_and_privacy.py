import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const
from MobileApps.libs.flows.mac.system.flows.flows_system import SystemFlows
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_01_Notifications_And_Privacy(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.privacy_preferences = cls.fc.fd["privacy_preferences"]
        cls.privacy_statement = cls.fc.fd["privacy_statement"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        if pytest.platform == "IOS":
            cls.ios_system = cls.fc.fd["ios_system"]
        else:
            cls.system_flows = SystemFlows(cls.driver, append=True)
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_ui_notification_privacy_creen(self):
        """
        IOS & MAC:
        C31297655 - Verify UI for Notification & Privacy Screen
        """
        self.fc.go_home(button_index=2, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        assert self.app_settings.get_switch_status(self.app_settings.SUPPLY_STATUS_SWITCH) == 0
        if pytest.platform == "MAC":
            self.app_settings.select_close()
    
    def test_02_verify_supply_status_n_promotional_message_switcher(self):
        """
        IOS & MAC:
        C33416290 - Verify supply status switcher
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        if pytest.platform == "MAC":
            self.system_flows.allow_hp_smart_app_notifications()
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)
        assert self.app_settings.get_switch_status(self.app_settings.SUPPLY_STATUS_SWITCH) == 1
        if pytest.platform == "IOS":
            self.app_settings.toggle_switch(self.app_settings.SUPPLY_STATUS_SWITCH, uncheck=True)
        else:
            self.app_settings.toggle_switch(self.app_settings.SUPPLY_STATUS_SWITCH, offset_x=5, offset_y=5)
        assert self.app_settings.get_switch_status(self.app_settings.SUPPLY_STATUS_SWITCH) == 0
        if pytest.platform == "MAC":
            self.app_settings.select_close()

    def test_03_verify_data_collection_notice_link(self):
        """
        IOS & MAC:
        C31297664 - Verify 'HP Print Account Data Usage Notice'under Notifications and Privacy
        C33595252 - Verify Privacy URLs (Data Collection Notice for the HP Smart Experience) under Notifications and Privacy
        C33595253, C33595254 - Verify Privacy URLs (HP Printer Data Collection Notice) under Notifications and Privacy
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_account_data_usage_notice_link()
        self.app_settings.verify_account_data_usage_notice_page()
        self.app_settings.select_navigate_back()
        self.app_settings.select_data_collection_notice_link()
        self.app_settings.verify_data_collection_notice_page()
        self.app_settings.select_navigate_back()
        self.app_settings.select_printer_data_collection_notice_link()
        self.app_settings.verify_printer_data_collection_notice_page()
        if pytest.platform == "MAC":
            self.app_settings.select_close()
    
    def test_04_verify_hp_privacy_hyperlink(self):
        """
        IOS & MAC:
        C31297665 - Verify Privacy URLs (HP Privacy Statement) under Notifications and Privacy
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_hp_privacy_statement(scroll=True)
        self.privacy_statement.verify_our_approach_to_privacy()
        if pytest.platform == "MAC":
            self.app_settings.select_close()
    
    def test_05_verify_links_on_notifications_n_privacy_screen(self):
        """
        IOS & MAC:
        C31297666 - Verify 'End User License Agreement' under Terms and Agreements sections
        C33409891 - Verify 'HP Smart Terms of Use' under Terms and Agreements
        C33409947 - Verify App Improvement URLs (Google Analytics Privacy Policy) under Notifications and Privacy
        C33416284 - Verify App Improvement URLs (Adobe Privacy Policy) under Notifications and Privacy
        C33416289 - Verify App Improvement URLs (Optimizely) under Notifications and Privacy
        C31297673 - Validate [App Setting- Privacy] - Links to Manage Privacy
        C31297670 - Validate [App Setting- Notifications and Privacy] - App Improvement
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        # EULA link
        self.app_settings.select_eula_link()
        verify_eula_page = True
        if pytest.platform == "IOS":
            self.app_settings.select_i_accept_btn(timeout=10)
        else:
            verify_eula_page = self.app_settings.naviate_to_eula_page()
        if verify_eula_page:
            self.app_settings.verify_eula_page()
        if pytest.platform == "MAC":
            self.app_settings.select_navigate_back()
        self.app_settings.select_navigate_back()
        # Terms of Use link
        self.app_settings.select_terms_of_use_link()
        self.app_settings.verify_terms_of_use_page(timeout=25)
        self.app_settings.select_navigate_back()
        # Google Analytics policy link
        self.app_settings.select_google_analytics_privacy_policy_link()
        self.app_settings.verify_google_analytics_privacy_policy_page()
        self.app_settings.select_navigate_back()
        # Adobe privacy policy link
        self.app_settings.select_adobe_privacy_link()
        self.app_settings.verify_adobe_privacy_policy_page()
        self.app_settings.select_navigate_back()
        # Optimizely privacy link
        self.app_settings.select_optimizely_link()
        self.app_settings.verify_optimizely_page()
        if pytest.platform == "MAC":
            self.app_settings.select_close()
    
    def test_06_verify_manage_my_privacy_settings(self):
        """
        IOS & MAC:
        C31297671 - Verify App privacy settings set during welcome flow
        C33416291 - Verify Privacy Settings URLs (Manage my Privacy Settings) under Notifications and Privacy
        """
        stack = self.stack.lower()
        self.fc.reset_hp_smart()
        if pytest.platform == "MAC":
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)
        if pytest.platform == "IOS":
            self.ios_system.clear_safari_cache()
        if stack != "pie":
            self.fc.change_stack(stack)
        if pytest.platform == "MAC":
            self.home.enter_full_screen_mode()
        else:
            self.driver.launch_app(i_const.BUNDLE_ID.SMART)
            self.driver.wait_for_context(w_const.WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type), timeout=30)
        self.welcome_web.verify_welcome_screen()
        if not self.welcome_web.verify_manage_options(raise_e=False):
            pytest.skip("Skipped because of old welcome screen")
        self.welcome_web.click_manage_options()
        if pytest.platform == "IOS":
            self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS, uncheck=False)
        else:
            self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS)
            app_analytics_switch = self._screenshot_switch(self.privacy_preferences.APP_ANALYTICS)
        self.privacy_preferences.click_continue()
        if pytest.platform == "IOS":
            self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.login_value_prop_screen(tile=False)
        if pytest.platform == "IOS":
            self.fc.clear_popups_on_first_login()
        else:
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)
        self.home.verify_home()
        self.fc.remove_default_paired_printer()
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_manage_privacy_settings_option()
        self.privacy_preferences.verify_privacy_preference_screen()
        if pytest.platform == "IOS":
            assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=False, attribute="aria-checked")
        else:
            assert saf_misc.img_comp(self._screenshot_switch(self.privacy_preferences.APP_ANALYTICS), app_analytics_switch) < 5
    
    def test_07_verify_change_n_back_on_privacy_settings(self):
        """
        IOS & MAC:
        C37527605 - Verify change and Save on "Manage my Privacy Settings" page
        C37528051 - Verify change and Back on "Manage my Privacy Settings" page
        C37528286 - Verify "Save" button on "Manage my Privacy Settings" page
        C37528541 - Verify "Back" button on "Manage my Privacy Settings" page
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_manage_privacy_settings_option()
        self.privacy_preferences.verify_privacy_preference_screen(timeout=20)
        if pytest.platform == "IOS":
            assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=True, attribute="aria-checked")
            assert self.privacy_preferences.get_switch_status(self.privacy_preferences.ADVERTISING, state=True, attribute="aria-checked")
            assert self.privacy_preferences.get_switch_status(self.privacy_preferences.PERSONALIZED_SUGGESTIONS, state=True, attribute="aria-checked")
            self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS, uncheck=False)
            self.privacy_preferences.click_back_btn()
            self.app_settings.select_manage_privacy_settings_option()
            self.privacy_preferences.verify_privacy_preference_screen(timeout=20)
            assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=True, attribute="aria-checked")
            self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS, uncheck=True)
            self.privacy_preferences.click_continue()
            self.app_settings.select_manage_privacy_settings_option()
            self.privacy_preferences.verify_privacy_preference_screen(timeout=20)
            assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=False, attribute="aria-checked")
        else:
            analytics_switch = self._screenshot_switch(self.privacy_preferences.APP_ANALYTICS)
            advertising_switch = self._screenshot_switch(self.privacy_preferences.ADVERTISING)
            personalized_suggestions_switch = self._screenshot_switch(self.privacy_preferences.PERSONALIZED_SUGGESTIONS)
            assert saf_misc.img_comp(analytics_switch, advertising_switch) < 4
            assert saf_misc.img_comp(analytics_switch, personalized_suggestions_switch) < 6
            self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS)
            self.privacy_preferences.click_back_btn()
            self.app_settings.select_manage_privacy_settings_option()
            self.privacy_preferences.verify_privacy_preference_screen()
            assert saf_misc.img_comp(analytics_switch, self._screenshot_switch(self.privacy_preferences.APP_ANALYTICS)) < 2
            self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS)
            self.privacy_preferences.click_continue()
            self.app_settings.select_manage_privacy_settings_option()
            self.privacy_preferences.verify_privacy_preference_screen()
            assert saf_misc.img_comp(analytics_switch, self._screenshot_switch(self.privacy_preferences.APP_ANALYTICS)) > 0
    
    def navigate_to_notification_n_privacy_settings(self):
        self.home.select_app_settings()
        self.app_settings.select_notification_n_privacy_option()
    
    def _screenshot_switch(self, locator):
        """
        Switches on the Privacy Settings screen aren't being captured in the page source,
        Use their screenshot to compare their state instead.
        """
        return saf_misc.load_image_from_base64(self.driver.screenshot_element(locator))
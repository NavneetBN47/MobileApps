import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_Profile_Settings:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fc.hpx = True
        cls.home = cls.fc.fd["home"]
        cls.profile = cls.fc.fd["profile"]
        cls.app_settings = cls.fc.fd["app_settings"]

    def test_01_click_verify_hp_privacy_statement_link(self):
        """
        Description: C41784147
                1. Fresh install and launch the app.
                2. Tap on Notification & Privacy from Settings page.
                3. Tap on HP Privacy Statement link under Data Collection.
            Expected Result:
                3.  Verify the redirection of leads to correct page.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.profile.click_profile_view_privacy_resources_btn()
        self.profile.click_hp_privacy_statement_link()
        self.profile.verify_hp_privacy_statement_link_title()

    def test_02_click_verify_google_analytics_privacy_statement_link(self):
        """
        Description: C41784148
                1. Fresh install and launch the app.
                2. click on profile and settings button.
                3. Tap on Privacy resources.
                4. Tap on Google Analytics privacy policy link under App Improvement.
                5. Observe
            Expected Result:
                3. Verify the user is directed to correct page
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.profile.click_profile_view_privacy_resources_btn()
        self.profile.click_google_analytics_policy_link()
        self.profile.verify_google_analytics_policy_link_title()

    def test_03_click_verify_adobe_privacy_link(self):
        """
        Description: C41791430
                1. Fresh install and launch the app.
                2. click on profile and settings button.
                3. Tap on Privacy resources.
                4. Tap on adobe privacy link under App Improvement.
                5. Observe
            Expected Result:
                3. Verify the user is directed to correct page
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.profile.click_profile_view_privacy_resources_btn()
        self.profile.click_adobe_privacy_link()
        self.profile.verify_adobe_privacy_link_title()

    def test_04_click_verify_google_optimizing_link(self):
        """
        Description: C41791902
                1. Fresh install and launch the app.
                2. click on profile and settings button.
                3. Tap on Privacy resources.
                4. Tap on Optimizely link under App Improvement.
                5. Observe
            Expected Result:
                3. Verify the user is directed to correct page
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.profile.click_profile_view_privacy_resources_btn()
        self.driver.swipe()
        self.profile.click_optimizing_link()
        self.profile.verify_optimizing_link_title()

    def test_05_click_verify_manage_privacy_settings_link(self):
        """
        Description: C41791924
                1. Fresh install and launch the app.
                2. Tap on Notification & Privacy from Settings page.
                3. Tap on Manage Privacy Settings link under Privacy.
                4. Tap on all the links shown on the Manage privacy settings.
            Expected Result:
                3.  Verify all the links are clickable and direct to the correct pages.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.profile.click_profile_manage_privacy_settings_btn()
        self.app_settings.click_hp_smart_term_of_use_link()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.app_settings.verify_eula_page()

    def test_06_manage_privacy_settings_link_redirection(self):
        """
        Description: C41791753
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Tap on Manage Privacy Settings link under Privacy and observe.
                4. Tap on Back arrow button on top left of Manage privacy settings screen.
                5. Observe
            Expected Result:
                3. Verify user is directed to Manage privacy settings screen.
                5. Verify user is back on Settings screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.profile.click_profile_manage_privacy_settings_btn()
        self.home.click_hpx_whats_new_popup_back_btn()
        self.profile.verify_settings_page_title()

    def test_07_view_privacy_resources_link_redirection(self):
        """
        Description: C56910061
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Tap on View privacy resources link under Privacy and observe.
                4. Tap on Back arrow button on top left of Manage privacy settings screen.
                5. Observe
            Expected Result:
                3. Verify user is directed to Privacy resources screen.
                5. Verify user is back on Settings screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.profile.click_profile_view_privacy_resources_btn()
        self.app_settings.verify_privacy_resources_screen()
        self.app_settings.click_settings_button_legal_information_screen()
        self.profile.verify_settings_page_title()
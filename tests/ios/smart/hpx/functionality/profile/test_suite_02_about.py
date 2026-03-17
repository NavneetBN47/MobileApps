import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_About:

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
        cls.printers = cls.fc.fd["printers"]

    def test_01_verify_app_version_from_about(self):
        """
        Description: C41784137
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
        self.driver.swipe()
        self.profile.click_term_of_use()
        self.profile.verify_term_of_use_title()

    def test_02_verify_end_user_license_from_about(self):
        """
        Description: C41784143
                1. Fresh install and launch the app.
                2. Tap on Notification & Privacy from Settings page.
                3. Tap on End User License Agreement link under About section.
            Expected Result:
                3.  Verify the link redirection leads to external page and it shows correctly.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.driver.swipe()
        self.profile.click_end_user_license_agreement()
        self.printers.verify_end_user_license_agreement_link()

    def test_03_verify_legal_info_link_redirection(self):
        """
        Description: C42221984
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar.
                3. Tap on Settings.
                4. Tap on Legal Information link under About section.
                5. Observe
                6. Tap on back arrow 'Settings' button.
                7. Observe
            Expected Result:
                5. Verify 'Legal Information' screen is opened.
                6. Verify user is back on Settings screen.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.driver.swipe()
        self.profile.click_legal_information()
        self.app_settings.verify_legal_information_screen()
        self.app_settings.click_settings_button_legal_information_screen()
        self.driver.swipe(direction="up")
        self.profile.verify_settings_page_title()

    def test_04_verify_legal_info_from_about(self):
        """
        Description: C56538875
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar.
                3. Tap on Settings.
                4. Tap on Legal Information link under About section.
            Expected Result:
                3. Verify 'Legal Information' screen is opened.
                5. Verify user is back on Settings screen.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.driver.swipe()
        self.profile.click_legal_information()
        self.app_settings.verify_legal_information_screen()
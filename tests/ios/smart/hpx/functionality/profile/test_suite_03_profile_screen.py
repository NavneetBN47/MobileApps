import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_03_Profile_Screen:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc.hpx = True
        cls.home = cls.fc.fd["home"]
        cls.profile = cls.fc.fd["profile"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.feedback = cls.fc.fd["feedback"]
        cls.hpid = cls.fc.fd["hpid"]

    def test_01_verify_profile_settings_screen(self):
        """
        Description: C41736081
                1. Fresh install and launch the app.
                2. Sign in.
                3. Tap on person icon on top nav bar.
                4. Tap on Settings on global side bar.
            Expected Result:
                4. Verify user is on Settings page.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        self.hpid.login()
        self.home.allow_notifications_popup(raise_e=False)
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        assert self.profile.verify_settings_page_title()

    def test_02_menu_button_behaviour(self):
        """
        Description: C41738214
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Tap on Menu button on top left of Settings page.
            Expected Result:
                3. Verify user exits out of Settings screen and is taken back to global side bar.
        """
        self.profile.verify_settings_page_title()
        self.profile.click_profile_settings_page_back_btn()
        self.profile.verify_profile_settings_btn()

    def test_03_verify_delete_account_button_redirection(self):
        """
        Description: C41791903
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Tap on Delete Account link under Privacy.
                4. Observe.
            Expected Result:
                4. Verify the user is directed to external browser: https://www.hp.com/us-en/privacy/ww-privacy-form.html
        """
        self.profile.click_profile_settings_btn()
        assert self.profile.verify_settings_page_title()
        self.profile.click_delete_your_account_link()
        self.profile.verify_hp_privacy_statement_link_title()

    def test_04_settings_screen_when_user_not_signedin(self):
        """
        Description: C41736331
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Observe the UI of Settings page.
            Expected Result:
                3. The back arrow is with "Menu" string, Settings page UI is as per design, No top bar on setting page.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        assert self.profile.verify_settings_page_title()
        self.profile.verify_profile_settings_page_back_btn()
        self.home.verify_notification_btn()
        self.app_settings.verify_icloud_backup_button()

    def test_05_settings_screen_when_user_signedin(self):
        """
        Description: C41736330
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Observe the UI of Settings page.
            Expected Result:
                4. Verify the Settings page UI is as per design for iOS
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        self.hpid.login()
        self.home.allow_notifications_popup(raise_e=False)
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        assert self.profile.verify_settings_page_title()
        self.profile.verify_profile_settings_page_back_btn()
        self.driver.swipe()
        self.app_settings.verify_sign_out_btn()

    def test_06_sign_in_from_global_sidebar(self):
        """
        Description: C52905632
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Observe the UI of Settings page.
            Expected Result:
                3. The back arrow is with "Menu" string, Settings page UI is as per design, No top bar on setting page.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.home.click_sign_btn_from_avatar()
        self.home.select_cancel()
        self.home.click_sign_btn_from_avatar()
        self.hpid.login()

    def test_07_sign_out_from_global_sidebar(self):
        """
        Description: C52905605
                1. Fresh install and launch the app.
                2. Tap on person icon on top nav bar and Tap on profile Settings page.
                3. Observe the UI of Settings page.
            Expected Result:
                3. The back arrow is with "Menu" string, Settings page UI is as per design, No top bar on setting page.
        """
        self.fc.go_home(reset=False, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.home.click_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.driver.swipe()
        self.app_settings.verify_sign_out_btn()
        self.app_settings.select_sign_out_btn()
        self.home.select_cancel()
        self.driver.swipe(direction="up")
        self.profile.verify_settings_page_title()
        self.app_settings.select_sign_out_btn()
        self.app_settings.select_sign_out_btn()
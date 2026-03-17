import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_HPX_Mfe(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()        
        cls.p = load_printers_session
        cls.edit = cls.fc.fd["edit"]
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.profile = cls.fc.fd["profile"]
        cls.stack = request.config.getoption("--stack")
        cls.printers = cls.fc.fd["printers"]
        cls.notification = cls.fc.fd["notifications"]
        cls.fc.hpx = True
    
    def test_01_verify_mfe(self):
        """
        C52683910
            Install and launch the app.
            Accept consents
            Skip sign in and navigate to rootview.
            Observe the device list/root view screen.
        Verifies the PrinterAdd button is displayed in the Home screen
        Verified the Sign In button is displayed in the Home screen
        Verifies the Let's get started! title is displayed in the Home screen
        Veified the Let's get started sub test is displayed in the Home screen
        """
        # Navigating to home screen
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        assert self.driver.wait_for_object("hpx_printer_add_btn", timeout=5)
        assert self.driver.wait_for_object("hpx_home_sign_btn", timeout=5)
        assert self.home.get_lets_get_started_text() == "Let’s get started!", "Title Expected: Let’s get started! Actual got: {}".format(self.home.get_lets_get_started_text())
        assert self.home.get_lets_get_started_sub_text() == "Add your printer to get started", "The Expected subtitle is: Add your printer to get started, Actual got: {}".format(self.home.get_lets_get_started_sub_text())

    def test_02_verify_avatar_icon(self):
        """
        C52683961
            Tap on the avatar icon.
        Verifies the avatar icon is displayed
        """
        self.home.click_avatar_btn()
        assert self.profile.verify_global_nav_bar()
        assert self.profile.verify_profile_support_link()
        assert self.profile.verify_profile_subcription_link()
        assert self.profile.verify_profile_settings_link()

    def test_03_sign_in_redirection(self):
        """
        C52683918, C52683915
            Tap on Sign In button.
        Verifies the Sign In username textbox is displayed
        """
        self.profile.click_profile_close_btn()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.verify_home(raise_e=False)
    
    def test_04_verify_redirection_to_add_printer(self):
        """
        C52683913
            Tap on "+" on top bar
        Verify user is directed to Add printer page.
        """
        self.home.click_hpx_add_printer_btn()
        assert self.printers.verify_add_new_printer_screen()
        self.printers.add_printer_ip(printer_ip=self.p.get_printer_information()["ip address"])

    
    def test_05_notification_screen_redirection(self):        
        """
        C52683916
            Tap on the notification icon.
        Verifies the notification screen is displayed and comes back
        """
        self.home.click_notification_btn()
        assert self.notification.verify_hpx_notification_screen()
        assert self.notification.verify_hpx_notification_print_txt()
        assert self.notification.verify_hpx_notification_mobile_fax_txt()
        assert self.notification.verify_hpx_notification_shortcuts_txt()
        assert self.notification.verify_hpx_notification_supplies_txt()
        assert self.notification.verify_hpx_notification_account_txt()
        
    
    def test_06_global_side_bar_verification(self):
        """
        C52683959
            Tap on the profile icon.
        Verifies the profile screen is displayed
        """
        self.notification.hpx_notification_close_btn()
        self.home.click_profile_btn()
        assert self.profile.verify_profile_close_btn()
        assert self.profile.verify_profile_support_link()
        assert self.profile.verify_profile_subcription_link()
        assert self.profile.verify_profile_settings_link()
        
    
    def test_07_verify_profile_link(self):
        """
        C52683957
            Tap on the profile link.
        Verifies the profile link is displayed
        """
        self.profile.click_profile_close_btn()
        self.home.click_profile_btn()
        assert self.profile.verify_profile_link()
    
    def test_08_verify_settings_page_in_profile(self):
        """
        C52683963
            Tap on the profile icon.
            click Settings button and verify the settings screen
        """
        self.profile.click_profile_settings_btn()
        assert self.profile.verify_settings_page_title()
        

    def test_09_verify_feedback_page_in_profile(self):
        """
        C52683965
            Tap on the profile icon.
            click feedback button and verify the feedback screen
        """
        self.profile.click_profile_settings_page_back_btn()
        self.profile.click_profile_feedback_btn()
        assert self.profile.verify_feedback_page_title()

    def test_10_verify_global_sidebar_UI_user_not_signedin(self):
        """
        C52683956
            Tap on the profile icon.
            click feedback button and verify the feedback screen
        """
        self.home.click_avatar_btn()
        assert self.profile.verify_global_nav_bar()
        assert self.profile.verify_profile_support_link()
        assert self.profile.verify_profile_subcription_link()
        assert self.profile.verify_profile_settings_link()
        self.profile.click_profile_feedback_btn()
        assert self.profile.verify_feedback_page_title()
        self.profile.click_profile_settings_page_back_btn()
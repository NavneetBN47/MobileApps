import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Home_Bottom_Navigation_Bar(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.smb = cls.fc.fd["smb"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.files = cls.fc.fd["files"]
        cls.photos = cls.fc.fd["photos"]
        cls.stack = request.config.getoption("--stack")

    @pytest.mark.parametrize('sign_in', [(1,True), (2,False)])
    def test_01_verify_toolbar(self, sign_in):
        """
        IOS & MAC:
        @param sign_in: tuple (int, bool)
        C31297226 - Verify Bottom Action Bar icons - Signed-in case
        C31297227 - Verify Bottom Action Bar icons - user not Signed-in case
        """
        self.fc.go_home(reset=True, button_index=sign_in[0], stack=self.stack)
        self.home.verify_bottom_navigation_bar()
        self.home.verify_bottom_navigation_bar_icons(signed_in=sign_in[1])

    def test_02_verify_toolbar_after_sign_out(self):
        """
        C27725933 Sign in on value prop, go home, and sign out in app settings
        verify: Home, Create Account, Settings icons
        """
        if pytest.platform == "MAC":
            pytest.skip("Skipping test for MAC")
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.verify_bottom_navigation_bar()
        self.home.verify_bottom_navigation_bar_icons(signed_in=True)
        self.home.select_app_settings()
        self.app_settings.select_sign_out_btn()
        self.app_settings.verify_sign_out_confirmation_popup()
        self.app_settings.dismiss_sign_out_popup()
        self.home.select_home_icon()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_bottom_navigation_bar_icons(signed_in=False, already_signed_in=True)
    
    def test_03_verify_hpid_screen(self):
        '''
            C28389845: navigation for sign in
            C28389846: navigation for create account
        '''
        if pytest.platform == "MAC":
            pytest.skip("Skipping test for MAC")
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_sign_in_icon()
        self.driver.wait_for_context(self.fc.hpid_url, timeout=60)
        self.home.select_cancel()
        self.home.select_create_account_icon(timeout=15)
        self.driver.wait_for_context(self.fc.hpid_url, timeout=60)

    @pytest.mark.parametrize("option", ["manage hp account", "sign out"])
    def test_04_account_icon_drawer_menu(self, option):
        """
        IOS & MAC:
        C30735952: Verify drawer menu for personal Org from Account Button
        C30735953: Verify "Manage HP Account" button functionality form drawer menu
        C30735954: Verify "Sign Out" button functionality form drawer menu
        C30735955: Verify "Sign Out" is successful
        C31297236: Verify Account icon from bottom action bar
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_account_icon()
        self.smb.verify_account_menu()
        if option == "manage hp account":
            self.smb.select_manage_hp_account()
            # defect: dashboard not loading correctly
            # self.fc.fd["hp_connect"].verify_new_printer_page(timeout=40)
        else:
            self.smb.click_sign_out_btn()
            self.smb.are_you_sure_sign_out_popup()
            self.smb.click_are_you_sure_sign_out_btn()
            self.home.verify_bottom_navigation_bar_icons(signed_in=False, already_signed_in=True)

    def test_05_view_and_print_icon_bottom_action_bar(self):
        """
        IOS & MAC:
        C31297234: Verify View & Print icon from bottom action bar
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.verify_bottom_navigation_bar()
        self.home.verify_rootbar_account_icon()
        self.home.select_rootbar_view_and_print_icon()
        self.photos.select_allow_access_to_photos_popup()
        self.files.verify_view_and_print_screen()

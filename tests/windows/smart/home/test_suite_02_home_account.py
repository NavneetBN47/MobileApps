import pytest
from MobileApps.libs.ma_misc import ma_misc

class ItemsNotInOrderException(Exception):
    pass

pytest.app_info = "GOTHAM"
class Test_Suite_02_Home_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.account = cls.fc.fd["account"]

        cls.locale = request.config.getoption("--locale")
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
        cls.username, cls.password = cls.login_info["email"], cls.login_info["password"]


    def test_01_verify_buttons_are_hidden(self):
        """
        w/o user signed in
        Verify Bell icon is not available on the Navigation Pane w/o user signed in
        Verify the "Sign Out", "Notification Settings" are not listed in the app settings list
        Check the order of items under Settings, verify order shows as design specs
        Check main UI (not logged in, any lang), verify blank user icon displays
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932008
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/19446919
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932009
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17217691
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17217692
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932010
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28469670
            
        """
        self.fc.go_home()

        assert self.home.get_text_of_left_menu_my_hp_account_btn() == "Manage HP Account"
        self.home.select_my_hp_account_btn()
        self.home.verify_fly_out_sign_in_page()
        self.home.select_my_hp_account_btn()

        assert self.home.verify_activity_btn(raise_e=False) is False
        
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        
        assert self.home.verify_sign_out_listview(raise_e=False) is False

        item_order_no_sign_in = ["Personalize Tiles", "Pin HP Smart to Start",\
             "Send Feedback", "Privacy Settings", "About"]

        self.__check_app_settings_items_order(item_order_no_sign_in)

        self.home.select_navbar_back_btn()

    def test_02_verify_listitems_shows(self):
        """
        w/ user signed in
        Verify the "Sign Out", "Notification Settings" are listed in the app settings list
        Check main UI (logged in, latin lang), verify first and last initial displays

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932007
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17217689
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17217690
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17217687
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17217688
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932010
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300351
            
        """      
        self.fc.sign_in(self.username, self.password)

        if self.home.verify_welcome_back_dialog(raise_e=False) is not False:
            self.home.select_welcome_back_continue_btn()
        self.home.verify_home_screen()

        self.home.select_my_hp_account_btn()
        self.home.verify_fly_out_my_account_page()
        self.home.select_my_hp_account_btn()

        if self.locale in ["zh", "ja", "ru", "ko", "el"]:
            assert self.home.get_text_of_left_menu_my_hp_account_btn() is False
        else:
            assert len(self.home.get_text_of_left_menu_my_hp_account_btn()) == 2

        self.home.select_app_settings_btn()

        # The app might need refresh after signing in.
        # Collapse the pane and expand again, the listitem shows.
        if self.home.verify_sign_out_listview(raise_e=False) is False:
            self.home.select_navbar_back_btn()
            self.home.select_app_settings_btn()

        self.home.verify_app_settings_pane()
        assert self.home.verify_sign_out_listview(raise_e=False) is not False

        item_order_sign_in = ["Personalize Tiles", "Pin HP Smart to Start",\
             "Send Feedback", "Privacy Settings", "About", "Sign Out"]

        self.__check_app_settings_items_order(item_order_sign_in)

        self.home.select_navbar_back_btn()

    def test_03_verify_bell_icon_shows(self):
        """
        w/ user signed in
        Verify bell icon is available on the navigation pane.
        Check bell icon on main UI, verify bell icon is moved from shell title bar to the navigation pane 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212378
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16931999
        """
        self.home.menu_expansion(expand=True)
        self.home.verify_activity_btn()

    def test_04_verify_activity_without_printer(self):
        """
        w/o printer selected in main UI
        Verify activity navigation pane unfolds after clicking the bell icon.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212349
        """
        self.home.select_activity_btn()
        self.home.verify_activity_pane(add_printer=False)

        self.home.select_navbar_back_btn()

    def test_05_check_sign_out_dialog_shows(self):
        """
        Verify "Sign out of your HP account?" dialog shows.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212364
        """
        self.home.select_app_settings_btn()
        self.home.select_sign_out_listview()
        self.account.verify_sign_out_dialog()

    def test_06_cancel_button(self):
        """
        Verify Main UI shows after clicking "Cancel" button in sign out dialog.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212367
        """
        self.account.select_cancel_btn()
        self.home.verify_home_screen()
    
    def test_07_sign_out_button(self):
        """
        Verify Main UI shows and user signs out after clicking Sign out button in sign out dialog.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212368
        """
        self.fc.sign_out()
        
        assert self.home.verify_logged_in() is False


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __check_app_settings_items_order(self, item_order):
        idx = 0
        for item_text in item_order:
            el = self.home.verify_app_settings_items_by_index(idx + 1)

            if el.text in item_text:
                idx += 1
            else:    
                raise ItemsNotInOrderException()
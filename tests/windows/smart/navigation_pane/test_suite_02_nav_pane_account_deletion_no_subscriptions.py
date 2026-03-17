import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_02_Nav_Pane_Account_Deletion_No_Subscriptions(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.smart_dashboard = cls.fc.fd["smart_dashboard"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.cec = cls.fc.fd["cec"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.fc.go_home()
        cls.email, cls.passwd = cls.fc.create_account()
        logging.info(f"New create account is: {cls.email} - {cls.passwd}")

    def test_01_check_privacy_settings_screen(self):
        """
        Account deletion: Deleting app data (Happy Path) - No subscriptions
        Account deletion: "Privacy settings" screen GUI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463284
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463293
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721564
        """
        self.home.verify_home_screen(timeout=30)
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        # Click see all button for web plugin manager to invoke the updation
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)
            self.cec.click_back_btn_do_more_with_hp_smart_screen()
            self.home.verify_home_screen()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)    
        self.cec.verify_unlock_cloud_features_tile(invisible=True)
        if self.cec.verify_do_more_with_hp_smart_screen(timeout=3, raise_e=False):
            self.cec.click_back_btn_do_more_with_hp_smart_screen()
        self.home.verify_home_screen()

        self.__add_shortcuts()
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen(sign_in=True)

    def test_02_check_delete_account_data_screen(self):
        """
        Verify Delete Account Data screen displays after clicking delete account data link.
        """
        self.privacy_settings.select_delete_account_data_link()
        self.smart_dashboard.verify_delete_hp_smart_account_screen()

        ## According to defect https://hp-jira.external.hp.com/browse/GOTH-24279, app back to home screen is acceptable behavior.
        self.smart_dashboard.select_no_keep_account_btn()
        # self.privacy_settings.verify_privacy_settings_screen(sign_in=True)
        self.home.verify_home_screen()

    def test_03_check_hp_smart_account_has_been_deleted_screen(self):
        """
        Verify HP Smart account has been deleted screen load after clicking delete account button.
        """
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen(sign_in=True)
        self.privacy_settings.select_delete_account_data_link()
        self.smart_dashboard.verify_delete_hp_smart_account_screen()

        self.smart_dashboard.select_delete_account_btn()
        self.smart_dashboard.verify_hp_smart_account_has_been_deleted_screen()

    def test_04_check_go_back_to_home_and_sign_out(self):
        """
        Account deletion: Deleting app data - Post deletion state: logged out/redirected to main ui
        Account deletion: Deleting app data - Post deletion state: local printers available
        Account deletion: Post deletion state: CEC should show only generic messages after deleting data 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463286
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463289
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463295
        """
        self.smart_dashboard.select_done_btn()
        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()
        assert self.home.verify_logged_in() is False
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)
        self.cec.verify_unlock_cloud_features_tile()
        if self.cec.verify_do_more_with_hp_smart_screen(timeout=3, raise_e=False):
            self.cec.click_back_btn_do_more_with_hp_smart_screen()
            self.home.verify_home_screen()

    def test_05_check_shortcuts_deleted_and_added(self):
        """
        Account deletion: Deleting app data - Post deletion state: no shortcuts
        Account deletion: Deleting app data - User is able to login with HPID post app data deletion
        Account deletion: Post deletion state: App does not react as a Grandfather user 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463287
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463290
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463294
        """
        self.home.select_shortcuts_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.email, password=self.passwd)
        self.shortcuts.verify_shortcuts_screen(timeout=60)
        ##Uncomment the following two lines when defect https://hp-jira.external.hp.com/browse/SRTC-2459 is solved
        # self.shortcuts.dismiss_coachmark()
        # assert self.shortcuts.select_shortcut(shortcut_name="test_shortcut", click_obj=False, raise_e=False) is False
        self.__add_shortcuts(first_create=False, shortcuts_name="test_shortcut_2")
        assert self.shortcuts.select_shortcut(shortcut_name="test_shortcut_2", click_obj=False)
        self.shortcuts.click_back_btn()
        self.home.verify_home_screen()
        self.fc.sign_out()

    def test_06_create_delete_account_data(self):
        """
        Account deletion: Deleting app data - User is not able to create new user with same HPID post app data deletion 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463291
        """
        self.fc.create_account(email=self.email)
        self.fc.close_hp_id_sign_in_up_page()


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __add_shortcuts(self, first_create=True, shortcuts_name="test_shortcut"):
        if first_create:
            self.home.select_shortcuts_tile()
            self.shortcuts.verify_default_shortcuts_shows()
            self.shortcuts.verify_not_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(shortcuts_name)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        if first_create:
            self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)
            self.shortcuts.click_home_btn()
            self.home.verify_home_screen()
        else:
            self.shortcuts.verify_shortcut_saved_screen()
            self.shortcuts.click_my_shortcuts_btn()

        


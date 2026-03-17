import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_10_Shortcuts_from_diff_views(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session


        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_check_back_button(self):
        """
        Launch App and select the printer under test to main UI.
        Click "Shortcuts" tile on main UI.
        Follow the flow to go back from Smart Task Home screen.  
        Follow the flow to go back from Empty Shortcuts screen.
        Follow the flow to go back from "Add Shortcut" screen.  
        Follow the flow to go back from "Edit Shortcut" screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13460666
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13460664
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29106079
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136482 
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_files_type_back_btn()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_files_type_back_btn()
        self.shortcuts.verify_empty_shortcuts_screen()
    
    @pytest.mark.parametrize("option", ["yes", "no"])
    def test_02_check_cancel_button_on_creat_screen(self, option):
        """
        Follow the flow to cancel a Shortcut creating
        Verify "Are you sure you want to cancel creating this Shortcut?" dialog shows 
        after clicking on "Cancel" button from Shortcut Settings screen
        Verify the flow back to Shortcut Settings screen after 
        clicking on "No, Continue Shortcut" button on "Are you sure you want to cancel creating this Shortcut?" dialog
        Verify the flow back to Add Shortcut screen after clicking 
        on "Yes, Cancel Shortcut" button on "Are you sure you want to cancel creating this Shortcut?" dialog, 
        and verify the shortcut does not show on Shortcut home screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29142877
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792451
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792452
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943188
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792453
        """
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.verify_shortcuts_cancel_popup()
        if option == "yes":
            self.shortcuts.click_yes_cancel_shortcut_btn()
            self.shortcuts.verify_add_shortcuts_screen()
            self.shortcuts.click_files_type_back_btn()
            self.shortcuts.verify_empty_shortcuts_screen()
        else:
            self.shortcuts.click_no_continue_shortcut_btn()
            self.shortcuts.verify_save_shortcut_screen()

    def test_03_check_cancel_btn_on_edit_screen(self):
        """
        creat shortcut job
        """
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()    

    @pytest.mark.parametrize("option", ["yes", "no"])
    def test_04_check_cancel_btn_on_edit_screen(self, option):
        """
        Follow the flow to go back from "Edit Shortcut" screen 
        Follow the flow to check the cancel deleting a Shortcuts from "Edit Shortcut" screen
        Verify the flow should back to Shortcut home screen after clicking on "Cancel" that shows on the top right 
        on "Edit Shortcuts" screen and then 
        click on "Yes, Cancel Edits" button from "Are you sure you want to cancel editing this shortcut?" confirmation dialog
        Verify the flow back to "Edit Shortcut" screen after clicking on "No, Cancel" button on "Exit without saving?" dialog
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13755188
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13769910
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136930
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13762560
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943219
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943303
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943306
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943304
        """
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_edit_btn()
        self.shortcuts.verify_edit_shortcut_screen_for_win()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.verify_shortcut_cancel_edits_popup()
        if option == "yes":
            self.shortcuts.click_edits_cancel_popup_yes_btn(is_win=True)
            self.shortcuts.verify_shortcuts_screen()
        else:
            self.shortcuts.click_edits_cancel_popup_no_btn(is_win=True)
            self.shortcuts.verify_edit_shortcut_screen_for_win()

    @pytest.mark.parametrize("option", ["no", "yes"])
    def test_05_check_delete_btn_on_edit_screen(self, option):
        """
        Follow the flow to check the deleting a Shortcuts from "Edit Shortcut" screen
        Click on "Delete" button from "Edit Shortcut" screen
        Follow the flow to check the deleting a Shortcuts from "Edit Shortcut" screen
        Verify "Delete Shortcut" dialog shows.
        Verify Shortcuts home screen should display after click "Yes, Delete" button on "Delete Shortcut" dialog.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13755189
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13755192
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943307
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943310
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943308
        """
        self.shortcuts.click_edit_delete_btn()
        self.shortcuts.verify_shortcut_delete_screen()
        if option == "no":
            self.shortcuts.click_delete_popup_cancel_btn(is_win=True)
            self.shortcuts.verify_edit_shortcut_screen_for_win()
        else:
            self.shortcuts.click_delete_popup_delete_btn(is_win=True)
            self.shortcuts.verify_empty_shortcuts_screen()

    def test_06_scan_landing_with_exit_flow(self):
        """
        Create/edit/execute a shortcut, start the execution but exit from scan, etc;
        Back to main UI
        Click on Scan Tile
        Verify Scan landing page should show, but not Shortcuts landing page
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29595504
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792467
        """
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)
        self.shortcuts.click_start_shortcut_btn()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.home.select_navbar_back_btn(return_home=False)
        self.shortcuts.verify_shortcuts_screen() 
        self.shortcuts.click_files_type_back_btn()
        self.home.verify_home_screen()
        self.home.select_scan_tile()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.verify_start_test_tab_not_display()

    def test_07_delete_shortcut(self):
        """
        Click on 3 vertical dots to bring up flyout menu, and click "Delete".
        Verify the "Delete Shortcut?" dialog dismiss and the selected Shortcut still displayed on 
        Shortcut home screen after click "No, Cancel" button.
        Verify the "Delete Shortcut?" dialog dismiss and the 
        selected Shortcut is deleted after click "Yes, Delete" button.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943220   
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943270
        """ 
        self.driver.restart_app()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_delete_btn()
        self.shortcuts.verify_shortcut_delete_screen()
        self.shortcuts.click_delete_popup_delete_btn(is_win=True)
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.verify_empty_shortcuts_screen()
        
import pytest
import random, string


from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_11_Shortcuts_create_common_cases(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup


        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_check_add_shortcuts_main_screen(self):
        """
        Click "Add Shortcuts" button on Empty Shortcuts screen.
        Select "Save to Google Drive" preset shortcut
        Verify Add Shortcuts main screen should display.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792448
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136366
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136367
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792449
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_save_to_google_drive_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.verify_save_toggle_is_on()
        self.shortcuts.dismiss_connecting_to_service_dialog()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.click_yes_cancel_shortcut_btn()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_print_email_and_save_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.verify_all_the_toggles_is_on()

    def test_02_check_file_type_section(self):
        """
        Toggle Email destination on on Shortcut Settings screen.
        Toggle Save destination on on Shortcut Settings screen.
        Toggle Print destination on on Shortcut Settings screen.
        Verify File Type section shows with basic file type (Standard PDF, Image (*.jpg) 
        if non-sync printer is selected on printer card
        Verify File Type section doesn't show for sync and non-sync printer selected on printer card.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29215206
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29215207
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29215208
        """
        self.shortcuts.click_cancel_btn()
        self.shortcuts.click_yes_cancel_shortcut_btn()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.click_email_toggle()
        self.shortcuts.verify_file_type_screen()
        self.shortcuts.click_email_toggle()
        self.shortcuts.click_save_toggle()
        self.shortcuts.verify_file_type_screen()
        self.shortcuts.close_save_toggle()
        self.shortcuts.click_print_toggle()
        self.shortcuts.verify_file_type_screen_not_show()
        self.shortcuts.click_print_toggle()

    def test_03_check_save_shortcut_button(self):
        """
        Enter a name, leave all destination toggles off
        Select one of colored box in Tile Color section, leave all destination toggles off
        Check the "Quick Run" checkbox, leave all destination toggles off
        Turn on 1 or more destination toggles, but do not enter a name
        Verify "Save Shortcut" button is disable.
        Turn on 1 or more destination toggles, and leave the rest of the 
        shortcut options unselected/select 1 or more the rest of the shortcut options 
        Verify "Save Shortcut" button is enabled.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14811725
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136357
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136358
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136359
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14811726
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29215205
        """
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_quick_run_checkbox()
        self.shortcuts.select_tile_color(2)
        self.shortcuts.verify_save_shortcuts_btn(is_enabled=False)
        self.shortcuts.click_print_toggle()
        self.shortcuts.verify_save_shortcuts_btn()
        self.shortcuts.clear_shortcut_name(is_win=True)
        self.shortcuts.verify_save_shortcuts_btn(is_enabled=False)

    def test_04_check_enter_shortcut_name_item(self):
        """
        Enter a name that is longer than 255 characters.
        Verify the max character limit is:
        255 for Window
        255 for Mac
        Verify the long shortcut name is not truncated and end with an ellipsis
        Enter a name with not permitted special characters 
        Remove the name entered.
        (%#/:*?"<>()|{}[]~`!@$^&+=’\ and cannot begin or end with space or a period).
        Verify "Shortcut name is invalid" message display under Shortcut name text box.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556066
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556067
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25406772
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25406773
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29169665
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24336946 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792457
        """
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=300))
        special_characters = "%#/:*?"
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.clear_shortcut_name(is_win=True)
        self.shortcuts.verify_shortcut_name_required_txt()
        # self.shortcuts.clear_shortcut_name(is_win=True)
        self.shortcuts.enter_shortcut_name(random_string)
        assert len(self.shortcuts.get_current_shortcut_name()) == 255
        # self.shortcuts.clear_shortcut_name(is_win=True)
        self.shortcuts.enter_shortcut_name(special_characters)
        self.shortcuts.verify_invalid_shortcut_name_text()
        self.shortcuts.verify_save_shortcuts_btn(is_enabled=False)

    def test_05_check_email_address(self):
        """
        Try to enter more than 20 email addresses in the To: field in Email Destination per shortcut
        Verify the 21 email address is not accepted in the To: field
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136369
        """
        email_address = (self.login_info["email"]+',')*21
        self.shortcuts.clear_shortcut_name(is_win=True)
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_email_toggle()
        self.shortcuts.enter_email_receiver(email_address)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_limited_email_message()
        
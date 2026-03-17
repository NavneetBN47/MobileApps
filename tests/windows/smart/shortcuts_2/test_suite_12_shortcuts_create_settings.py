import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_12_Shortcuts_create_settings(object):
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

    def test_01_check_print_settings(self):
        """
        Turn Print destination toggle ON
        Check the dropdown values on Print destination.
        Turn Print destination toggle back to off
        Verify settings are selectable and can be saved
        Verify correct values show as follows:
        Copies: 1 to 50
        Color mode: Color/Grayscale
        Two-sided: "Off", "Short-edge", "Long-edge"
        Verify values can be changed.
        Verify print settings hide
        verify "Save Shortcut" button is enabled
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793682 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793685
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793688
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793695
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793696
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943208
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29215193
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29215209
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29151333
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793689
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793691
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793693
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793737
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793683
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793686
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_help_btn(is_win=True)
        self.home.verify_help_and_support_page()
        self.shortcuts.click_back_btn()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_toggle()
        self.shortcuts.verify_print_toggle_is_on()
        self.shortcuts.click_copies_dropdown()
        self.shortcuts.verify_copies_settings_opt()
        self.shortcuts.click_shortcuts_title()
        self.shortcuts.click_color_dropdown()
        self.shortcuts.verify_color_settings_opt()
        self.shortcuts.click_shortcuts_title()
        self.shortcuts.click_two_sided_dropdown()
        self.shortcuts.verify_two_sided_settings_opt()
        self.shortcuts.click_shortcuts_title()
        self.shortcuts.verify_save_shortcuts_btn()

    def test_02_check_email_settings(self):
        """
        Turn Email destination toggle ON on the Shortcuts Settings screen
        Turn Email destination toggle back to Off on the Shortcuts Settings screen
        Click on "Subject" field/Modify the "Subject" text/Remove all text from "Subject" field
        Verify Email settings show
        Verify the "To/Subject/Body" fields match with below description
        "To: " field empty & a person icon
        "Subject" field is prefilled with a text message
        Body" field is prefilled with a text message
        verify Email settings hides
        Verify the text string on the "Subjet" field does not go away./Verify the text string on 
        the "Subjet" field can be modified./Verify "Save Shortcut" button is disabled
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793725
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793739
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846505
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29169661
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793696
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846833 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846839
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29169657
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846895
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846972
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793740
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846530
        """
        email_address = self.login_info["email"]
        self.shortcuts.click_print_toggle()
        self.shortcuts.click_email_toggle()
        self.shortcuts.verify_email_toggle_is_on()
        self.shortcuts.verify_save_shortcuts_btn(is_enabled=False)
        self.shortcuts.enter_email_receiver('test')
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_invalid_emails_txt()
        self.shortcuts.enter_email_receiver(email_address)
        self.shortcuts.clear_email_subject_text()
        self.shortcuts.verify_save_shortcuts_btn(is_enabled=False)
        self.shortcuts.enter_subject_receiver("gotham")
        self.shortcuts.enter_body_receiver("this is a test!")
        self.shortcuts.verify_save_shortcuts_btn()

    def test_03_check_save_to_settings(self):
        """
        Turn Save destination toggle ON on the Shortcuts Settings screen
        Verify Save settings show
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846488
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136381
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846491
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846492
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846499
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29179240
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846501
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846489
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846495
        """
        self.shortcuts.click_email_toggle()
        self.shortcuts.click_save_toggle()
        self.shortcuts.verify_save_toggle_is_on()
        self.shortcuts.click_onedrive_menu_btn()
        opt=["Add Destination", "Remove", "Edit Account Name"]
        for item in opt:
            el = self.shortcuts.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"
        self.shortcuts.click_remove_listitem()
        self.shortcuts.verify_remove_hp_smart_access_dialog()
        self.shortcuts.click_ok_btn()
        self.shortcuts.click_one_drive_checkbox()
        self.shortcuts.verify_save_shortcuts_btn()

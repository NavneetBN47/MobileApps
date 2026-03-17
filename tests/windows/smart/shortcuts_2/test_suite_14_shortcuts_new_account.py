import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_14_Shortcuts_new_account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.scan = cls.fc.fd["scan"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_to_shortcuts_tile_with_new_account(self):
        """
        Click "Shortcuts" tile -> Signin / Create Account dialog show.
        Sign in with new account that has no shortcuts created before
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.select_shortcuts_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=0)
        self.fc.verify_hp_id_sign_in_up_page(is_sign_up=True)
        self.fc.handle_web_login(create_account=True)

    def test_02_check_screen_with_new_account_on_shortcuts_home(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29151290
        """
        self.shortcuts.verify_default_shortcuts_shows()
        self.shortcuts.verify_not_empty_shortcuts_screen()
        self.shortcuts.verify_coach_mark_dialog_page_1()
        self.shortcuts.click_right_arrow_btn()
        self.shortcuts.verify_coach_mark_dialog_page_2()
        self.shortcuts.click_right_arrow_btn()
        self.shortcuts.verify_coach_mark_dialog_page_3()
        self.shortcuts.click_left_arrow_btn()
        self.shortcuts.verify_coach_mark_dialog_page_2()

    def test_03_check_shortcuts_job_from_scan_preview(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29151287
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29142860
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29142744
        """
        self.home.select_navbar_back_btn()
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog()
        self.scan.verify_shortcuts_item_displays()
        self.scan.click_shortcuts_item()
        self.scan.verify_your_shortcut_dialog()

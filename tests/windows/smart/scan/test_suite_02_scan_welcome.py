import pytest

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_02_Scan_welcome(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    def test_01_verify_ows_ucde_value(self):
        """
        Click on Scan tile the first time on Main UI.
        Verify OWS ucde value prop shows 
        Make sure user is not signed in
        Verify tiles are locked and the user can't use them without sign in
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572532
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777819
        """
        self.fc.go_home()
        self.home.select_scan_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()

    def test_02_verify_new_scan_auto_enhancements_dialog_shows(self):
        """
        Sign in / Create Account
        Verify New Scan Auto-Enhancements dialog shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572534
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572535
        """
        self.ows_ucde_value_prop.select_native_value_prop_buttons(1)
        self.fc.verify_hp_id_sign_in_up_page()
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        self.scan.verify_new_scan_auto_enhancements_dialog()

    def test_03_verify_scan_welcome_modal_dialog_does_not_show(self):
        """
        Click "X" to dismiss the Scan welcome modal.
        Back to Main UI and then click the "Scan" tile.

        Verify My Scan screen shows
        Verify the Scan welcome modal dialog does not show anymore.    

        Click Scan tile without printer added.
        Check the Scanner screen. 
        Verify "Scanning is Currently Unavailable..." on the scan home screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572538
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13453287
        """
        self.scan.click_auto_enhancement_cancel_btn()
        self.home.select_navbar_back_btn()
        self.home.select_scan_tile()
        assert self.scan.verify_new_scan_auto_enhancements_dialog(raise_e=False) is False
        self.scan.verify_scanning_unavailable_screen()
        
    def test_04_verify_print_btn_not_available_on_preview_without_printer(self):
        """
        No printer added on the Main UI
        Observe Preview page for Print button
        Verify the "Print" button is not available on the Previwe screen without a printer.
        Observe print button on the scan result screen when no printer added, verify print button is not available

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/26949051
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/26949047
        """
        self.scan.select_import_btn()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()
        self.scan.verify_print_btn_not_display()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanning_unavailable_screen()
        
    @pytest.mark.parametrize("buttons", ["back", "return_home", "get_more_help"])
    def test_05_check_each_button_on_scanning_unavailavle_screen(self, buttons):
        """
        Click on "Return Home" button.
        Click on "Get More Help" button.
        Click back arrow.
        Verify user back to the Main UI.
        Verify Help Center opens
        Verify user back to the Main UI.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572538
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13453311
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28564530 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639458
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846504
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072338 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28564534
        """
        webpage = "Help_Center"
        if buttons == "back":
            self.home.select_navbar_back_btn()
        elif buttons == "return_home":
            self.scan.click_return_home_btn()
            self.home.verify_home_screen()
        else:
            self.scan.click_get_more_help_btn()
            if webpage not in self.web_driver.session_data["window_table"].keys():
                self.scan.click_get_more_help_btn()
                self.web_driver.add_window(webpage)
            self.web_driver.switch_window(webpage)

            current_url = self.web_driver.get_current_url()

            for sub_url in self.scan.HELP_CENTER:
                assert sub_url in current_url
        if buttons !="get_more_help":
            self.home.select_scan_tile()

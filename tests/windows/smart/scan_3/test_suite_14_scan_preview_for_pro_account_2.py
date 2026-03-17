import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_14_Scan_Preview_For_Pro_Account_2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.ip_addr = request.config.getoption("--mobile-device")

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        
        cls.stack = request.config.getoption("--stack")
        if cls.stack == 'production':
            pytest.skip("Skip this test as there is no account with production stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=False, pro=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_check_preview_screen_with_single_page_pro_account(self):
        """
        go to scaner screen
        Click Scan tile from main UI and try to scan 1/multi  page document
        Verify "Redact" shows along with "+Add" and "Scribble" in the top right of the Preview screen.
        Verify "Text Extract" shows in the Preview screen along with "Fax", 
        "Print", "Save", "Share"
        Click on "Scribble" on the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31419125
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31419128
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31419130(one half)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31419132(one half high)
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_welcome_back_dialog()
        self.home.select_an_organization_list_item(2)
        self.home.select_welcome_back_continue_btn()
        sleep(5)
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()   
        self.scan.click_get_started_btn()
        self.scan.select_dropdown_listitem(self.scan.preset, "Document")
        self.scan.click_scan_btn()
        self.scan.verify_pro_scan_result_screen()
        self.scan.verify_all_the_button_on_preview()
        sleep(3)
        self.scan.click_scribble_btn()
        self.scan.verify_place_your_mark_screen()
        self.scan.click_new_mark_cancel_btn()
        self.scan.verify_scribble_scan_result_screen()

    def test_02_go_to_preview_screen_with_single_page_text_extract_btn(self):
        """
        Click on "Text Extract" on the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794748
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794750
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794751
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794754
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31084371
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31084372
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31084374
        """
        self.scan.click_text_extract_btn()
        self.scan.verify_select_language_dialog()
        self.scan.click_install_new_language_btn()
        self.scan.verify_install_language_dialog()
        self.scan.click_language_item(1)
        self.scan.click_install_btn()
        # self.scan.verify_downloading_language_dialog()
        self.scan.verify_select_language_dialog()
        self.scan.click_continue_btn()
        # self.scan.verify_extracting_text_dialog()
        if self.scan.verify_text_not_detected_dialog(raise_e=False) is False:
            # self.scan.verify_extracting_text_dialog()
            self.scan.verify_text_edit_screen()
            self.scan.click_copy_all_btn()
            self.scan.verify_copie_text_message()
            self.scan.click_copy_all_btn()
            self.scan.click_done_btn()
            self.scan.verify_scribble_scan_result_screen()
        else:
            self.scan.click_extract_ok_btn()
            self.scan.verify_scribble_scan_result_screen()


    def test_03_go_to_preview_screen_with_multi_page_text_extract_btn(self):
        """
        Click on "Text Extract" on the Preview screen
        Click on "Cancel" button from "Extracting text..." dialog
        Verify the flow back to Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794749
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794752(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31211300
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31419126
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794754
        """
        if self.scan.verify_scan_result_screen(raise_e=False):
            self.scan.click_add_pages_btn()
            self.scan.verify_scanner_screen()
            self.scan.click_multi_scan_btn()
            self.scan.verify_multi_scribble_scan_result_screen()
            self.scan.verify_all_the_button_on_preview()
        self.scan.click_text_extract_btn()
        self.scan.verify_select_language_dialog()
        self.scan.click_install_new_language_btn()
        self.scan.verify_install_language_dialog()
        self.scan.click_language_item(1)
        self.scan.click_install_btn()
        # self.scan.verify_downloading_language_dialog()
        self.scan.verify_select_language_dialog()
        self.scan.click_continue_btn()
        if self.scan.verify_text_not_detected_dialog(raise_e=False) is False:
            # self.scan.verify_extracting_text_dialog()
            self.scan.verify_text_edit_screen()
            self.scan.click_copy_all_btn()
            self.scan.verify_copie_text_message()
            self.scan.click_copy_all_btn()
            self.scan.click_done_btn()
            self.scan.verify_scribble_scan_result_screen()
            self.scan.click_text_extract_btn()
            self.scan.verify_select_language_dialog()
            self.scan.click_continue_btn()
            self.scan.click_extract_cancel_btn()
            self.scan.verify_scribble_scan_result_screen()
        else:
            self.scan.click_extract_ok_btn()
            self.scan.verify_scribble_scan_result_screen()
        self.scan.click_thumbnail_view_icon()
        self.scan.verify_thumbnail_view_screen_displays(is_pro_account=True)

    def test_04_go_to_preview_screen_with_multi_page_scribble_btn(self):
        """
        Click on "Scribble" on the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31211303
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31419129

        """
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_pro_scan_result_screen()
        self.scan.click_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_multi_pages_scan_result_screen()
        self.scan.click_multi_scribble_btn()
        self.scan.verify_place_your_mark_screen()
        self.scan.click_new_mark_cancel_btn()
        self.scan.verify_multi_pages_scan_result_screen()
       
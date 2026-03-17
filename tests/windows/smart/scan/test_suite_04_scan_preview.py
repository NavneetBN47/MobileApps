import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_04_Scan_Preview(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.softfax_home = cls.fc.fd["softfax_home"]
        cls.softfax_landing = cls.fc.fd["softfax_landing"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_click_print_button_on_preview(self):
        """
        Click Print button on the Preview screen.

        Verify the print dialog displays.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235306  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572580  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29308739(only check button) 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235443
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.verify_rotate_button_display()
        self.scan.click_print_btn()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_cancel_btn()
        self.scan.verify_scan_result_screen()

    def test_02_click_shortcuts_button_on_preview(self):
        """
        Click shortcuts button on the Preview screen.

        Verify Shortcuts flyout shows with no Shortcuts 
        if Shortcut home screen wasn't entered before entering Scan Preview screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24850509
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061550
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061563
        """
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog()
        self.scan.click_shortcuts_btn()

    def test_03_click_fax_button_on_preview(self):
        """
        Click Fax button on Preview screen

        Verify Mobil Fax starts
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28005342
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17361147
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17411204
        """
        self.scan.click_fax_btn()
        self.softfax_home.verify_mobile_fax_home_screen()
        self.home.select_navbar_back_btn()
  
    def test_04_click_save_button_on_preview(self):
        """
        Click Save button on Preview screen

        Verify Save flyout shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235290
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24336939
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29634838
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24336940
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30344352
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286589 
        """
        self.home.select_scan_tile()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.verify_file_name_text_box_not_empty()
        self.scan.verify_smart_file_name_text_not_display()
        self.scan.verify_doc_language_text_not_display()
        self.scan.click_dialog_close_btn()

    def test_05_click_edit_button_on_preview(self):
        """
        Click Edit button on Preview screen

        Verify Edit screen shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13227897
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13046622 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28256857 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13077030
                     https://hp-testrail.external.hp.com/index.php?/cases/view/27362146
        """
        self.scan.click_menu_btn()
        self.scan.click_edit_btn()
        self.scan.verify_edit_screen()
        self.scan.click_adjust_item()
        self.scan.change_adjust_contrast_edit_vaule("50")
        self.scan.click_cancel_btn()
        self.scan.verify_exit_without_saving_dialog_for_edit_screen()
        self.scan.click_no_btn()
        self.scan.click_done_btn()
        self.scan.verify_scan_result_screen()

    def test_06_click_replace_button_on_preview(self):
        """
        Click Replace button on Preview screen

        Verify Replace shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28580907
        """
        self.scan.click_menu_btn()
        self.scan.click_replace_btn()
        self.scan.verify_replace_screen()
        self.scan.click_replace_cancel_btn()
        self.scan.verify_scan_result_screen()

    def test_07_click_share_button_on_preview(self):
        """
        Click Share button on Preview 

        Verify Share flyout shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235309
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24336939
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30427143
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30624547
        """
        self.scan.click_share_btn()
        self.scan.verify_share_dialog()
        self.scan.verify_smart_file_name_toggle_is_hidden()
        self.scan.verify_file_name_text_box_not_empty()
        self.scan.click_dialog_close_btn()

    def test_08_check_thumbnail_view_screen(self):
        """
        Click the thumbnail view icon on Preview screen

        Verify thumbnail view screen displays
        Verify some function on thumbnail view screen 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235327
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28581102
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13235378
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13235389
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28581102
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13235319
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29880323
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13235260
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13235459
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13235461
        """
        self.scan.click_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_multi_pages_scan_result_screen()
        self.scan.hover_thumbnail_view_icon()
        self.scan.verify_thumbnail_view_images_display()
        self.scan.click_thumbnail_view_icon()
        self.scan.verify_thumbnail_view_screen_displays()
        self.scan.right_click_pic_item_thumbnail_view(1)
        self.scan.click_delete_image_btn()
        self.scan.verify_delete_dialog()
        self.scan.click_cancel_btn_on_dialog()
        self.scan.right_click_pic_item_thumbnail_view(2)
        self.scan.click_delete_image_btn()
        self.scan.verify_delete_dialog()
        self.scan.click_delete_btn_on_dialog()
        self.scan.click_rotate_btn()
        self.scan.click_select_all_btn()
        self.scan.verify_all_the_button_can_be_used()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_no_btn()
        self.scan.click_delete_btn()
        self.scan.verify_delete_dialog()
        self.scan.click_delete_btn()
        self.scan.verify_scanner_screen()

import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_08_Scan_Different_Presets_For_Advance_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_go_to_scaner_screen(self):
        """
        go to scaner screen
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()   
        self.scan.click_get_started_btn()

    @pytest.mark.parametrize('preset', ["Book","Multi-Item","ID Card"])
    def test_02_check_different_presets_on_preview(self, preset):
        """
        Perform scan job with Advance Presetes is set Book/Multi-items/ID Card.

        Verify All kinds of tile on preview.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29628398
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29628414 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29628404 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29628405
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29504572
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29628416  
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28735567
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28734604 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28735569  
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28734603 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29511050   
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29595506  
                     https://hp-testrail.external.hp.com/index.php?/cases/view/30799111    
                     https://hp-testrail.external.hp.com/index.php?/cases/view/30799112
                     https://hp-testrail.external.hp.com/index.php?/cases/view/30799113
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28735568
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28734602 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29511049 
                     https://hp-testrail.external.hp.com/index.php?/cases/view/13227898
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29511048
                     https://hp-testrail.external.hp.com/index.php?/cases/view/28735563
                     https://hp-testrail.external.hp.com/index.php?/cases/view/29504489
        """
        self.scan.select_dropdown_listitem(self.scan.preset, preset)
        if preset == "ID Card":
            self.scan.click_scan_btn()
            self.scan.verify_another_scanner_screen()
            self.scan.click_scan_btn()
            self.scan.verify_id_card_front_screen()
            self.scan.click_multi_scan_btn()
            self.scan.verify_id_card_back_screen()
            self.scan.click_multi_scan_btn()
        else:
            self.scan.click_scan_btn()
        self.scan.verify_scribble_scan_result_screen()
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.select_file_type_dropdown()
        file_type = ["Basic PDF", "Image(*.jpg)","Searchable PDF","Word Document (*.docx)","Plain Text (*.txt)"]
        for type in file_type:
            el = self.scan.verify_dropdown_listitem(type)
            assert el.get_attribute("IsEnabled").lower() == "true"
        self.scan.click_save_text()
        self.scan.click_dialog_close_btn()
        self.scan.click_share_btn()
        self.scan.verify_share_dialog()
        self.scan.select_file_type_dropdown()
        for type in file_type:
            el = self.scan.verify_dropdown_listitem(type)
            assert el.get_attribute("IsEnabled").lower() == "true"
        self.scan.click_save_text()
        self.scan.click_dialog_close_btn()
        self.scan.click_print_btn()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_cancel_btn()
        self.scan.verify_scribble_scan_result_screen()
        self.scan.click_menu_btn()
        self.scan.click_edit_btn()
        self.scan.verify_edit_screen()
        self.scan.click_done_btn()
        self.scan.verify_scribble_scan_result_screen()
        self.scan.click_menu_btn()
        self.scan.click_replace_btn()
        if preset == "ID Card":
            self.scan.verify_id_card_front_replace_screen()
            self.scan.click_replace_scan_btn()
            self.scan.verify_id_card_back_replace_screen()
            self.scan.click_replace_scan_btn()
            self.scan.verify_id_card_front_screen()
            self.scan.click_multi_scan_btn()
            self.scan.verify_id_card_back_screen()
            self.scan.click_multi_scan_btn()
        else:
            self.scan.verify_replace_screen()
            self.scan.click_replace_scan_btn()
        self.scan.verify_scribble_scan_result_screen()
        sleep(3)
        self.scan.click_menu_btn()
        self.scan.click_single_delete_btn()
        self.scan.verify_delete_dialog()
        self.scan.click_delete_btn_on_dialog()
        self.scan.verify_scanner_screen()

    def test_03_check_id_card_front_and_back_screen_on_preview(self):
        """
        Perform scan job with Advance Presetes is set ID Card.

        check edit/replace button on preview.
        https://hp-testrail.external.hp.com/index.php?/cases/view/29543445   
        https://hp-testrail.external.hp.com/index.php?/cases/view/29543450 
        https://hp-testrail.external.hp.com/index.php?/cases/view/29543429  
        https://hp-testrail.external.hp.com/index.php?/cases/view/29543453  
        """
        self.scan.select_dropdown_listitem(self.scan.preset, "ID Card")
        self.scan.verify_id_card_message_display()
        self.scan.click_scan_btn()
        self.scan.verify_another_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_id_card_front_screen()
        sleep(3)
        self.scan.click_id_card_menu_btn()
        self.scan.click_edit_btn()
        self.scan.verify_edit_screen()
        self.scan.click_done_btn()
        self.scan.verify_id_card_front_screen()
        sleep(3)
        self.scan.click_id_card_menu_btn()
        self.scan.click_replace_btn()
        self.scan.verify_id_card_replace_screen()
        self.scan.click_replace_scan_btn()
        self.scan.verify_id_card_front_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_id_card_back_screen()
        sleep(3)
        self.scan.click_id_card_menu_btn()
        self.scan.click_edit_btn()
        self.scan.verify_edit_screen()
        self.scan.click_done_btn()
        self.scan.verify_id_card_back_screen()
        sleep(3)
        self.scan.click_id_card_menu_btn()
        self.scan.click_replace_btn()
        self.scan.verify_id_card_replace_screen()
        self.scan.click_replace_scan_btn()
        self.scan.verify_id_card_back_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_scribble_scan_result_screen()

    def test_04_check_smart_file_name_on_save_or_share_flyout(self):
        """
        Check smart file name on save flyout.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30624541  
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30624543
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30624544
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30624546
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30737741
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794753
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_dropdown_listitem(self.scan.preset, "Multi-Item")
        self.scan.verify_multi_item_message_display()
        self.scan.click_scan_btn()
        self.scan.verify_scribble_scan_result_screen()
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.verify_smart_file_name_toggle_is_off_by_default()
        smart_file_name=self.scan.get_current_file_name()
        self.scan.click_smart_file_name_toggle("open")
        if self.scan.verify_text_not_detected_dialog(raise_e=False):
            self.scan.click_extract_ok_btn()
            self.scan.verify_save_dialog()
        else:
            original_name=self.scan.get_current_file_name()
            assert smart_file_name!=original_name
            self.scan.click_dialog_close_btn()
            self.scan.click_save_btn()
            self.scan.verify_save_dialog()
            self.scan.verify_smart_file_name_toggle_is_on()
            current_name=self.scan.get_current_file_name()
            assert original_name==current_name

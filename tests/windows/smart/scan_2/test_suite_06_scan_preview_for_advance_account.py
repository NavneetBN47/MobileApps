import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from SAF.misc.ssh_utils import SSH
import MobileApps.resources.const.windows.const as w_const
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_06_Scan_Preview_For_Advance_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.ip_addr = request.config.getoption("--mobile-device")

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_scan_job_with_id_card_flow(self):
        """
        Perform scan job with Advance Presetes is set to "ID Card" and the ID card is on glass bed
        click on "Scan" button
        Check the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29504489
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29880329
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()   
        self.scan.click_get_started_btn()
        self.scan.select_dropdown_listitem(self.scan.preset, "ID Card")
        self.scan.verify_id_card_message_display()
        self.scan.click_scan_btn()
        self.scan.verify_another_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_id_card_front_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_id_card_back_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_scribble_scan_result_screen()
        
    def test_02_scan_job_with_book(self):
        """
        Perform scan job with Advance Presetes is set to "Book" and open book is in glass bed
        Check the Preview screen
        Select 1200 dpi in resolution
        Perform scan job
        Cick on save option enable smart file name
        Verify "Smart File Name" works properly
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28734593
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13281209
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13281212
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13281213 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29880327
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/44453669
        """
        self.scan.click_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_dropdown_listitem(self.scan.preset, "Book")
        self.scan.verify_book_message_display()
        self.scan.select_resolution_dropdown()
        if self.scan.verify_dropdown_listitem("1200 dpi", raise_e=False):
            self.scan.verify_dropdown_listitem("1200 dpi").click()
            self.scan.click_multi_scan_btn()
            self.scan.verify_multi_scribble_scan_result_screen(300)
            sleep(2)
            self.scan.click_save_btn()
            self.scan.verify_save_dialog()
            self.scan.click_smart_file_name_toggle("open")
            if self.scan.verify_text_not_detected_dialog(raise_e=False):
                self.scan.click_extract_ok_btn()
                self.scan.verify_save_dialog()
                self.scan.click_dialog_close_btn()
            else:
                original_name=self.scan.get_current_file_name()
                self.scan.click_save_dialog_save_btn()
                self.scan.input_file_name(original_name)
                self.scan.verify_file_has_been_saved_dialog()
                flie_path = self.scan.verify_the_saved_file_name_is_correct(original_name)
                self.scan.click_dialog_close_btn()
                ssh = SSH(self.ip_addr, "exec")
                ssh.send_command("del " + flie_path)
        else:
            pytest.skip("The printer not support 1200 dpi, can not do this test")
    
    def test_03_scan_job_with_multi_item(self):
        """
        Perform scan job with Advance Presetes is set to "Multi-Item" and multiple items in 
        scanner bed ((docs, business cards, photos, receipts, etc.)
        Check the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28734592
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29880328
        """
        self.scan.click_multi_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_dropdown_listitem(self.scan.preset, "Multi-Item")
        self.scan.verify_multi_item_message_display()
        self.scan.select_resolution_dropdown()
        self.scan.verify_dropdown_listitem("300 dpi").click()
        self.scan.click_multi_scan_btn()
        self.scan.verify_multi_scribble_scan_result_screen()

    def test_04_click_scribble_button_on_preview(self):
        """
        Click on "Scribble" on the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31410924
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31410925 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31410928 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31410920 
        """
        self.scan.click_multi_scribble_btn()
        self.scan.verify_place_your_mark_screen()
        self.scan.click_create_btn()
        self.scan.verify_new_mark_screen()
        self.scan.click_new_mark_cancel_btn()
        self.scan.verify_place_your_mark_screen()
        self.scan.click_new_mark_cancel_btn()
        self.scan.verify_scribble_scan_result_screen()

    def test_05_click_save_button_on_preview(self):
        """
        Click on "Save"/"Share" from Preview screen to bring up Save/Share flyout
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30344285
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30624548
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13846485 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235275  
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30405407 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30240710 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30427142 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064648
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072315
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30427144
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30427142
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30737740
        """
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.verify_password_protection_not_display()
        self.scan.select_file_type_dropdown()
        file_type = ["Basic PDF", "Image(*.jpg)","Searchable PDF","Word Document (*.docx)","Plain Text (*.txt)"]
        for type in file_type:
            el = self.scan.verify_dropdown_listitem(type)
            assert el.get_attribute("IsEnabled").lower() == "true"
        self.scan.click_save_text()
        self.scan.click_install_new_language_btn()
        self.scan.verify_install_language_dialog()
        self.scan.click_language_item(1)
        self.scan.click_install_btn()
        # self.scan.verify_downloading_language_dialog() The screen has appeared, but too fast can`t verify
        self.scan.click_dialog_cancel_btn()
        self.scan.verify_save_dialog()
        self.scan.click_install_new_language_btn()
        self.scan.verify_install_language_dialog()
        self.scan.click_language_item(1)
        self.scan.click_install_btn()
        # self.scan.verify_downloading_language_dialog() The screen has appeared, but too fast can`t verify
        self.scan.verify_save_dialog(30)
        self.scan.click_smart_file_name_toggle("open")
        if self.scan.verify_text_not_detected_dialog(raise_e=False) is False:
            self.scan.click_save_dialog_save_btn()
            self.scan.input_file_name(w_const.TEST_TEXT.TEST_TEXT_00)
            self.scan.verify_file_has_been_saved_dialog()
            flie_path = self.scan.verify_the_saved_file_name_is_correct(w_const.TEST_TEXT.TEST_TEXT_00)
            self.scan.click_dialog_close_btn()
            ssh = SSH(self.ip_addr, "exec")
            ssh.send_command("del " + flie_path)
        else:
            self.scan.click_extract_ok_btn()
            self.scan.click_dialog_close_btn()
        
    def test_06_click_text_extract_button_on_preview(self):
        """
        Click on "Text Extract" on the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30799115
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30799114 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30799117 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30799118
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31206010 
        """
        if self.scan.verify_are_you_enjoying_dialog(raise_e=False):
            self.scan.click_are_you_dialog_not_now_btn()
            self.scan.verify_are_you_enjoying_dialog_disappear()
            self.scan.verify_sorry_to_hear_dialog()
            self.scan.click_sorry_to_dialog_not_now_btn()
            self.scan.verify_sorry_to_hear_dialog_disappear()
        self.scan.verify_scribble_scan_result_screen()
        self.scan.click_text_extract_btn()
        self.scan.verify_select_language_dialog()
        self.scan.click_continue_btn()
        self.scan.verify_extracting_text_dialog()#The screen has appeared, but sometime too fast can`t verify
        self.scan.click_extract_cancel_btn()
        self.scan.verify_scribble_scan_result_screen()
        self.scan.click_text_extract_btn()
        self.scan.verify_select_language_dialog()
        self.scan.click_install_new_language_btn()
        self.scan.verify_install_language_dialog()
        self.scan.click_language_item(1)
        self.scan.click_install_btn()
        self.scan.verify_downloading_language_dialog()
        self.scan.verify_select_language_dialog()
        self.scan.click_continue_btn()
        if self.scan.verify_text_not_detected_dialog(raise_e=False) is False:
            self.scan.verify_text_edit_screen()
            self.scan.click_copy_all_btn()
            self.scan.verify_copie_text_message()
            self.scan.click_copy_all_btn()
            self.scan.click_done_btn()
            self.scan.verify_multi_scribble_scan_result_screen()
        else:
            self.scan.click_extract_ok_btn()
            self.scan.verify_scribble_scan_result_screen()
        
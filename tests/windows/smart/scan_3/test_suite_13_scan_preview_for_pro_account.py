import pytest
import random, string

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from SAF.misc.ssh_utils import SSH
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_13_Scan_Preview_For_Pro_Account(object):
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


    def test_01_go_to_scaner_screen(self):
        """
        go to scaner screen
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
        self.scan.verify_scan_result_screen()

    def test_02_check_save_share_on_preview(self):
        """
        Toggle Advance Preset to "Document" or "Multi Item" or "Book"
        Perform the scan job
        Ensure Document language that is set to English shows in the Save/Share flyout
        Select any file type: Searchable PDF, Plain Text (*.txt), Word Document (*.docx),
        Basic PDF, Iage*(.jpg) [Please test with all of 5 file types]
        Verify "Document Language" option shows
        Select "Install new language" from "Document Language"
        Verify "Downloading Language Pack..." dialog with "Cancel" button shows
        Verify new selected language is installed successfully
        Verify multi language can be selected
        Verify clicking on "Cancel" button from "Downloading Language Pack..." dialog 
        the dialog is dismissed and the low back to Save/Share flyout
        Perform OCR job with one of the language
        Verify the select Language for OCR job become as default
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30309651(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30344287
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30344288
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30344353(GOTH-22656)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30727243(GOTH-22656)
        """
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.click_language_dropdown_listitem()
        el = self.scan.verify_dropdown_listitem("English (US)")
        assert el.get_attribute("IsEnabled").lower() == "true"
        self.scan.click_save_text()
        self.scan.verify_document_language_by_default()
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

    def test_03_check_password_protection_opt(self):
        """
        Click on Save on the Scan Preview screen
        Click on Share on the Scan Preview screen
        Verify "Add Password Protection" option shows when Basic PDF / Searchable PDF file type is selected
        Verify the toggle for "Add Password Protection" option is off by default
        Turn "Add Password Protection" toggle ON
        Verify verify Enter Password text box shows
        Open Share flyout Verify the toggle for "Add Password Protection" should not be ON after opening Share flyout
        Enter valid password
        verify the scanned image is saved successfully
        and then turn it Off
        Verify Enter Password text box hides
        Enter invalid password -> Click Save button
        Verify error message
        Toggle "Smart File Name" On
        Verify File Name gets auto-updated
        Toggle "Smart File Name" back to Off
        Verify File Name gets changed to original name
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30240706
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30241707
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30241719
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30241716
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30241717
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30240712
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30241720
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30240709
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30241709
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30241824(critical)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30344286
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30727239
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30727240
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30368573(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30368577(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286568
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286578
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286580
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286583
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286591
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286594
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30286598
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30737738
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30737739
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30799119
        """
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
            self.scan.find_password_protection_opt()
            self.scan.click_password_protection_toggle()
            self.scan.verify_password_textbox_shows()
            self.scan.enter_password('12345678')
            self.scan.click_save_dialog_save_btn()
            self.scan.input_file_name(w_const.TEST_TEXT.TEST_TEXT_01)
            self.scan.verify_file_has_been_saved_dialog()
            flie_path = self.scan.verify_the_saved_file_name_is_correct(w_const.TEST_TEXT.TEST_TEXT_01)
            self.scan.click_dialog_close_btn()
            ssh = SSH(self.ip_addr, "exec")
            ssh.send_command("del " + flie_path)
            self.scan.click_save_btn()
            self.scan.verify_save_dialog()
            self.scan.click_password_protection_toggle()
            self.scan.click_smart_file_name_toggle("close")
            now_name=self.scan.get_current_file_name()
            assert smart_file_name == now_name
        self.scan.find_password_protection_opt()
        self.scan.verify_password_protection_toggle_status()
        self.scan.select_file_type_listitem('Image(*.jpg)')
        self.driver.swipe()
        self.scan.verify_password_protection_not_display()
        self.scan.select_file_type_listitem('Basic PDF')
        self.scan.find_password_protection_opt()
        self.scan.click_password_protection_toggle()
        self.driver.swipe()
        self.scan.verify_password_textbox_shows()
        self.scan.click_dialog_close_btn()
        self.scan.click_save_btn()
        self.scan.enter_password('12345678')
        self.scan.click_save_dialog_save_btn()
        self.scan.input_file_name(w_const.TEST_TEXT.TEST_TEXT_00)
        self.scan.verify_file_has_been_saved_dialog()
        self.scan.click_dialog_close_btn()
        self.scan.dismiss_are_you_enjoy_dialog()
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.verify_password_protection_toggle_status(by_default=False)
        self.scan.enter_password('12345678 ')
        self.scan.click_save_dialog_save_btn()
        self.scan.verify_password_space_error_shows()
        self.scan.clear_password()
        self.scan.enter_password('123')
        self.scan.click_save_dialog_save_btn()
        self.scan.verify_password_tooshort_error_shows()
        self.scan.clear_password()
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
        self.scan.enter_password(random_string)
        self.scan.click_save_dialog_save_btn()
        self.scan.verify_password_toolong_error_shows()
        self.scan.clear_password()
        self.scan.enter_password('12 3')
        self.scan.click_save_dialog_save_btn()
        self.scan.verify_password_tooshortwithspace_error_shows()
        self.scan.clear_password()
        self.scan.enter_password(' {}'.format(random_string))
        self.scan.click_save_dialog_save_btn()
        self.scan.verify_password_toolongwithspace_error_shows()
        self.scan.click_dialog_close_btn()
        self.scan.click_share_btn()
        self.scan.verify_share_dialog()
        self.scan.verify_password_protection_toggle_status()
        self.scan.click_dialog_close_btn()
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.click_save_dialog_save_btn()
        self.scan.input_file_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.scan.verify_file_has_been_saved_dialog()
        flie_path = self.scan.verify_the_saved_file_name_is_correct(w_const.TEST_TEXT.TEST_TEXT_01)
        self.scan.click_dialog_close_btn()
        self.scan.dismiss_are_you_enjoy_dialog()
        ssh = SSH(self.ip_addr, "exec")
        ssh.send_command("del " + flie_path)
        self.scan.click_save_btn()
        self.scan.verify_save_dialog()
        self.scan.select_file_type_listitem('Searchable PDF')
        self.scan.find_password_protection_opt()
        self.scan.click_password_protection_toggle()
        self.driver.swipe()
        self.scan.enter_password('12345678')
        self.scan.click_save_dialog_save_btn()
        self.scan.input_file_name(w_const.TEST_TEXT.TEST_TEXT_00)
        self.scan.click_save_as_yes_btn()
        self.scan.verify_file_has_been_saved_dialog()
        flie_path = self.scan.verify_the_saved_file_name_is_correct(w_const.TEST_TEXT.TEST_TEXT_00)
        self.scan.click_dialog_close_btn()
        ssh = SSH(self.ip_addr, "exec")
        ssh.send_command("del " + flie_path)

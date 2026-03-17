import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"
 
@pytest.mark.usefixtures("function_setup_myhp_launch") 
class Test_Suite_01_Shortcuts(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
        cls.shortcuts_create_edit = cls.fc.fd["shortcuts_create_edit"]
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.devicesMFE.click_home_loggedin()
        cls.fc.sign_in(cls.user_name, cls.password, cls.web_driver, user_icon_click=False)
        cls.fc.add_a_printer(cls.p)


    @pytest.mark.regression
    def test_01_sign_in_to_cloud_account_C50837308(self):
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].win_scroll_element("shortcuts_tile", direction="down")
        assert self.fc.fd["devicesDetailsMFE"].verify_shortcuts_tile(), "Shortcuts tile is not displayed on printer details page."
        self.fc.fd["devicesDetailsMFE"].click_shortcuts_tile()
        assert self.fc.fd["shortcuts"].verify_add_new_shortcuts(), "Add new shortcuts screen is not displayed after clicking shortcuts tile."
        self.fc.fd["shortcuts"].click_add_new_shortcuts()
        assert self.fc.fd["shortcuts"].verify_create_your_own_shortcut(), "Create your own shortcut option is not displayed on add new shortcuts screen."
        self.fc.fd["shortcuts"].click_create_your_own_shortcut()
        self.fc.fd["shortcuts"].enter_shortcut_name("cloud")
        assert self.fc.fd["shortcuts"].verify_save_shortcut_btn(), "Save shortcut button is not displayed after entering shortcut name."
        self.fc.fd["shortcuts"].click_save_shortcut_btn()
        assert self.fc.fd["shortcuts"].verify_one_drive_signin_link(), "One drive sign in link is not displayed after clicking save shortcut button."
        self.fc.fd["shortcuts"].click_one_drive_signin_link()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.fc.fd["shortcuts"].sign_in_and_verify_account_listed(), "Failed to sign in to One Drive account."
 
    @pytest.mark.regression
    def test_02_verify_sign_in_page_not_shown_in_shortcut_C48457989(self):
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].win_scroll_element("shortcuts_tile", direction="down")
        assert self.fc.fd["devicesDetailsMFE"].verify_shortcuts_tile(), "Shortcuts tile is not shown on device details page"
        self.fc.fd["devicesDetailsMFE"].click_shortcuts_tile()
        assert self.fc.fd["shortcuts"].verify_sign_in_to_use_shortcuts_screen(), "Sign in to use shortcuts screen is not shown"

    @pytest.mark.regression
    def test_03_Accessing_shortcuts_newuser_C50837356(self):
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        assert self.fc.fd["devicesDetailsMFE"].verify_shortcuts_tile(),  "Shortcuts title not found"
        self.fc.fd["devicesDetailsMFE"].click_shortcuts_tile()
        assert self.fc.fd["shortcuts"].verify_shortcuts_screen(), "shortcuts page is not found"
        assert self.fc.fd["shortcuts"].verify_default_email(), "shortcut is not available"  

    @pytest.mark.regression
    def test_04_verify_shortcut_sent_screen_C50837350(self):
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].win_scroll_element("shortcuts_tile", direction="down")
        assert self.fc.fd["devicesDetailsMFE"].verify_scan_tile(), "Scan tile is not shown on device details page"
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)      
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        assert self.fc.fd["scan"].verify_shortcuts_btn_display(), "Shortcuts button is not displayed on scan result screen"
        self.fc.fd["scan"].click_shortcuts_btn()
        assert self.fc.fd["scan"].verify_shortcuts_screen_dialog(), "Shortcuts screen dialog is not displayed"
 
    @pytest.mark.regression
    def test_05_verify_more_than_one_email_not_accepted_C50837296(self):
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].win_scroll_element("shortcuts_tile", direction="down")
        self.fc.fd["devicesDetailsMFE"].verify_shortcuts_tile()
        self.fc.fd["devicesDetailsMFE"].click_shortcuts_tile()
        assert self.fc.fd["shortcuts"].verify_add_new_shortcuts(), "Add new shortcuts screen is not shown"
        self.fc.fd["shortcuts"].click_add_new_shortcuts()
        assert self.fc.fd["shortcuts"].verify_create_your_own_shortcut(), "Create your own shortcut option is not shown"
        self.fc.fd["shortcuts"].click_create_your_own_shortcut()
        assert self.fc.fd["shortcuts_create_edit"].verify_email_toggle(), "Email toggle button is not shown on create your own shortcut screen"
        self.fc.fd["shortcuts_create_edit"].click_email_toggle()
        self.fc.fd["shortcuts_create_edit"].enter_email_receiver("testqama24@gmail.com")
        self.fc.fd["shortcuts_create_edit"].enter_email_receiver("testqama24+shortcuts@gmail.com")
        assert self.fc.fd["shortcuts_create_edit"].verify_invalid_email_message_screen(), "Invalid email message is not shown when more than one email is entered"      

    @pytest.mark.regression
    def test_06_verify_shortcut_sent_screen_C50837351(self):
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].win_scroll_element("shortcuts_tile", direction="down")
        assert self.fc.fd["devicesDetailsMFE"].verify_scan_tile(), "Scan tile is not shown on device details page"
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)      
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        assert self.fc.fd["scan"].verify_shortcuts_btn_display(), "Shortcuts button is not displayed on scan result screen"
        self.fc.fd["scan"].click_shortcuts_btn()
        assert self.fc.fd["scan"].verify_shortcuts_screen_dialog(), "Shortcuts screen dialog is not displayed"
        self.fc.fd["scan"].click_shortcuts_screen_email()
        assert self.fc.fd["scan"].verify_shortcuts_screen_successfull(), "Shortcuts successfull screen is not displayed"


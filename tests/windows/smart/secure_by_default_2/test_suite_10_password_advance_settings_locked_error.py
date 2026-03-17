import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_10_password_advance_settings_locked_error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer = cls.fc.fd["printers"]
        cls.ews = cls.fc.fd["ews"]

        cls.setup_pw = "12345678"
        cls.stack = request.config.getoption("--stack")
   
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        if "DunePrinterInfo" in str(cls.p.p_obj):
            pytest.skip("Skip this test as Dune Printer can not door open")

    def test_01_go_to_ews_screen(self):
        """
        Go to Printer Settings
        Select "Advanced Settings" (EWS)
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)

    def test_02_setup_ews_password_protected(self):
        """
        Setup password if the printer has no one.
        """
        if not self.ews.verify_ews_sign_in_link(raise_e=False):
            if self.ews.verify_ews_login_state(raise_e=False):
                self.ews.click_sign_out_link()
                self.ews.verify_sign_out_successfuly_text()
                self.ews.click_ok_btn()
            self.ews.make_ews_to_password_modal(self.setup_pw)

    def test_03_check_secure_prompt_printer_error(self):
        """
        Install and launch app to main UI.
        Go to device picker to select the printer under test.
        Go to Printer Settings.
        Select "Advanced Settings" (EWS).
        Click on any tile with a lock sign on it (see below for an example of ews screen).
        Enter incorrect password on the secure prompt dialog and click Submit.
        Repeat step 6 several times.
        Verify secure prompt is dismissed.
        Verify the locked error message shows.
        Verify user access to Advanced Settings (EWS) will be blocked.
        Verify user can still access other pages in the app.
        Leave printer settings and then come back to it.
        Verify secure prompt is not displayed.
        Verify the locked error message still shows there.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25430556
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413201
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        self.ews.click_sign_in_link()
        if self.ews.verify_log_in_with_pin_dialog(raise_e=False):
            for _ in range(6):
                self.ews.input_pin("666666")
                self.ews.click_log_in_with_pin_dialog_submit_btn()
                if self.ews.verify_continuing_to_your_printer_settings_dialog(raise_e=False):
                    break
                self.ews.verify_log_in_with_pin_dialog()
            self.ews.click_ok_btn()
        else:
            self.ews.verify_sign_in_to_access_this_site_dialog()
            for _ in range(6):
                self.ews.input_username("admin")
                self.ews.input_password("666666")
                self.ews.click_sign_in_to_access_this_site_dialog_sign_in_btn()
                #GOTH-25980 Sometimes locked error message does not show when enter the incorrect password continuously on the secure prompt dialog.
                if self.ews.verify_incorrect_user_name_and_password_display(raise_e=False):
                    break
                self.ews.verify_sign_in_to_access_this_site_dialog()

    def test_04_remove_ews_password_protected(self):
        """
        remove ews password protected and Restore printer status
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        self.ews.remove_ews_password_modal(self.p.get_pin())
        self.home.select_navbar_back_btn()

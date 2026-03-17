import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_08_password_advance_settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.ews = cls.fc.fd["ews"]

        cls.setup_pw = "12345678"
        cls.stack = request.config.getoption("--stack")
   
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

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
        if not self.ews.verify_ews_sign_in_link(raise_e=False) and "DunePrinterInfo" not in str(self.p.p_obj):
            if self.ews.verify_ews_login_state(raise_e=False):
                self.ews.click_sign_out_link()
                self.ews.verify_sign_out_successfuly_text()
                self.ews.click_ok_btn()
            self.ews.make_ews_to_password_modal(self.setup_pw)

    def test_03_check_cancel_btn_on_secure_prompt_with_offline_printe(self):
        """
        Check ews screen with locked  
        Printer has password set (password needs to be set in printer EWS if Pin is still available)
        Go to Printer Settings
        Select "Advanced Settings" (EWS)
        Click on any tile with a lock sign on it (see below for an example of ews screen)
        Click Cancel button on the secure prompt.
        Verify the secure dialog dismisses.
        Verify locked feature cannot be accessed.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413192
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413200
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        try:
            self.ews.click_sign_in_link()
            if self.ews.verify_log_in_with_pin_dialog(raise_e=False):
                self.ews.click_log_in_with_pin_dialog_cancel_btn()
                assert self.ews.verify_log_in_with_pin_dialog(raise_e=False) is False
                self.ews.click_sign_in_link()
                self.ews.verify_log_in_with_pin_dialog()
                self.fc.trigger_printer_offline_status(self.p)
                self.ews.click_log_in_with_pin_dialog_cancel_btn()
                assert self.ews.verify_log_in_with_pin_dialog(raise_e=False) is False
                self.ews.verify_ews_sign_in_link()
            else:
                self.ews.verify_sign_in_to_access_this_site_dialog()
                self.ews.click_sign_in_to_access_this_site_dialog_cancel_btn()
                assert self.ews.verify_sign_in_to_access_this_site_dialog(raise_e=False) is False
                self.ews.click_sign_in_link()
                self.ews.verify_sign_in_to_access_this_site_dialog()
                self.fc.trigger_printer_offline_status(self.p)
                self.ews.click_sign_in_to_access_this_site_dialog_cancel_btn()
                assert self.ews.verify_sign_in_to_access_this_site_dialog(raise_e=False) is False
                self.ews.verify_ews_sign_in_link()
        finally: 
            self.fc.restore_printer_online_status(self.p)

    def test_04_check_secure_prompt_with_offline_printer(self):
        """
        Check ews screen with locked  
        Printer has password set (password needs to be set in printer EWS if Pin is still available)
        Go to Printer Settings
        Select "Advanced Settings" (EWS)
        Click on any tile with a lock sign on it (see below for an example of ews screen)
        Turn off printer after the Advanced Settings(EWS) secure prompt shows.
        Enter correct password and click Submit.
        Verify secure prompt is dismissed.
        Verify the locked feature is not open.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413198
        """
        user_name = "admin"
        try:
            self.ews.click_sign_in_link()
            if self.ews.verify_log_in_with_pin_dialog(raise_e=False):
                self.fc.trigger_printer_offline_status(self.p)
                self.ews.input_pin(self.setup_pw)
                self.ews.click_log_in_with_pin_dialog_submit_btn()
                assert self.ews.verify_log_in_with_pin_dialog(raise_e=False) is False
                self.ews.verify_ews_sign_in_link()
            else:
                self.ews.verify_sign_in_to_access_this_site_dialog()
                self.fc.trigger_printer_offline_status(self.p)
                self.ews.input_username(user_name)
                self.ews.input_password(self.p.get_pin())
                self.ews.click_sign_in_to_access_this_site_dialog_sign_in_btn()
                assert self.ews.verify_sign_in_to_access_this_site_dialog(raise_e=False) is False
                self.ews.verify_ews_sign_in_link()
        finally: 
            self.fc.restore_printer_online_status(self.p)

    def test_05_remove_ews_password_protected(self):
        """
        remove ews password protected
        """
        if "DunePrinterInfo" in str(self.p.p_obj):
            pytest.skip("Skip this test if a Dune printer selected")
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        self.ews.remove_ews_password_modal(self.p.get_pin())
        self.home.select_navbar_back_btn()

    def test_06_not_ews_password_protected(self):
        """
        Install and launch app to main UI.
        Go to device picker to select the printer under test.
        Go to Printer Settings.
        Select "Advanced Settings" (EWS).
        Click on any tile.
        Verify password prompt does not show.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413194
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973459 (03)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413195
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        self.ews.select_scan_menu()
        assert self.ews.verify_sign_in_to_access_this_site_dialog(raise_e=False) is False and self.ews.verify_log_in_with_pin_dialog(raise_e=False) is False

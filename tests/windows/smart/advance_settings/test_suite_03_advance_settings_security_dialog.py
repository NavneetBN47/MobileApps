import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_03_Advance_Settings_Security_Dialog(object):
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
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_add_printer(self):
        """
        Add a printers
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

        if self.printer.verify_pin_dialog(raise_e=False) is not False:
            if self.printer.input_pin(self.p.get_pin()) is True:
                self.printer.select_pin_dialog_submit_btn()

        self.home.select_printer_settings_tile(change_check={"wait_obj": "printer_settings_tile", "invisible": True})
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item()
        self.printer_settings.select_advanced_settings_item(change_check={"wait_obj": "advanced_settings_opt", "invisible": True})
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

    def test_03_check_security_dialog(self):
        """
        (+) Go to Advanced Settings with a password protected printer, verify Windows Security dialog pops up
        Enter incorrect user info on the OS Security dialog to access EWS, verify the dialog prompts again
        Enter correct user info on the OS Security dialog to access EWS, verify EWS content shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541112
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541113
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/15962713
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17855002
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413191
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/25413193
        """
        user_name = "admin"
        incorrect_pw = "abcdefgh"
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile(change_check={"wait_obj": "printer_settings_tile", "invisible": True})
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)

        self.ews.click_sign_in_link()
        if self.ews.verify_log_in_with_pin_dialog(raise_e=False):
            self.ews.input_pin(incorrect_pw)
            self.ews.click_log_in_with_pin_dialog_submit_btn()
            if self.ews.verify_unauthorized_dialog(raise_e=False):
                self.ews.click_sign_in_btn_on_unauthorized_dialog()
            self.ews.verify_log_in_with_pin_dialog()

            self.ews.input_pin(self.p.get_pin())
            self.ews.click_log_in_with_pin_dialog_submit_btn()
            if self.ews.verify_log_in_with_pin_dialog(raise_e=False):
                self.ews.input_pin(self.setup_pw)
                self.ews.click_log_in_with_pin_dialog_submit_btn()
            assert self.ews.verify_log_in_with_pin_dialog(raise_e=False) is False
        else:
            self.ews.verify_sign_in_to_access_this_site_dialog()
            self.ews.input_username(user_name)
            self.ews.input_password(incorrect_pw)
            self.ews.click_sign_in_to_access_this_site_dialog_sign_in_btn()
            self.ews.verify_sign_in_to_access_this_site_dialog()

            self.ews.input_username(user_name)
            self.ews.input_password(self.p.get_pin())
            self.ews.click_sign_in_to_access_this_site_dialog_sign_in_btn()
            assert self.ews.verify_sign_in_to_access_this_site_dialog(raise_e=False) is False

        self.ews.verify_advanced_settings_page(self.p)

    def test_04_remove_ews_password_protected(self):
        """
        Setup password if the printer has no one.
        (+) Modify some settings in the printer EWS webview, verify the settings can be saved 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541085

        """
        if "DunePrinterInfo" in str(self.p.p_obj):
            pytest.skip("Skip this test if a Dune printer selected")
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile(change_check={"wait_obj": "printer_settings_tile", "invisible": True})
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        
        self.ews.remove_ews_password_modal(self.p.get_pin())
        self.home.select_navbar_back_btn()

        
import pytest
from time import sleep

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "GOTHAM"
class Test_Suite_01_Smart_Security(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.smart_dashboard = cls.fc.fd["smart_dashboard"]
        cls.sf = SystemFlow(cls.driver)

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_add_remote_printer(self):
        """""
        Verify security badge icon status reflects correctly the status of the printer security as follows:
        a. Security monitored
        b. Needs attention
        c. Not monitored
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808909(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808884
        """""
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_status_text(timeout=120)
        self.home.verify_carousel_printer_security_text()
        if self.home.verify_print_anywhere_dialog(raise_e=False):
            self.home.select_paw_x_btn()

    def test_02_check_security_status_page(self):
        """
        Click on security badge icon (for security monitored) that show on printer card on main UI
        Check the toggle for smart security status in printer Setting -> Smart Security 
        verify toggle is On
        turn off monitoring
        verify toggle is Off
        Verify security badge icon on the printer card on main UI is changed from security monitored to Security Not monitored
        Verify smart security status on Printer Settings -> Security Status is changed from security monitored to Security Not monitored
        verify Printer Setting opens to "Security Status" -> (security not monitored) screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808895
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808896
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808891
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808898
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28174498
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808888
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28161417
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28174499
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808883
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808899
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27563167(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27985522
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28161419

        """
        self.home.click_security_badge_icon()
        self.printer_settings.verify_security_status_page()
        self.printer_settings.verify_smart_security_toggle_status()
        self.printer_settings.select_smart_security_toggle()
        self.printer_settings.verify_hp_smart_security_protects_dialog()
        self.printer_settings.select_remove_security_btn()
        self.printer_settings.verify_security_not_monitroed_text()
        self.printer_settings.verify_smart_security_toggle_status(by_default=False)
        self.home.select_navbar_back_btn()
        self.home.verify_carousel_printer_security_text()
        self.home.verify_security_not_monitroed_display()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_security_status_opt()
        self.printer_settings.verify_security_status_page()
        self.printer_settings.verify_smart_security_toggle_status(by_default=False)
        self.printer_settings.select_smart_security_toggle()
        self.printer_settings.verify_hp_smart_security_protects_dialog()
        self.printer_settings.select_get_protected_btn()
        self.printer_settings.verify_security_status_page()
        self.printer_settings.verify_security_monitroed_text()
        self.printer_settings.verify_smart_security_toggle_status()

    def test_03_check_security_status_for_Dashboard(self):
        """
        Click on person icon
        Select "My HP Account" from login flyout
        Check Smart Security on HP Smart Dashboard
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28189022

        """
        self.home.select_navbar_back_btn()
        self.home.verify_carousel_printer_security_text()
        self.home.verify_security_monitroed_display()
        self.home.select_manage_hp_account_btn()
        self.smart_dashboard.verify_my_account_page()
        self.smart_dashboard.select_solutions_btn()
        self.smart_dashboard.verify_smart_security_btn_display()
        self.home.select_navbar_back_btn()

    def test_04_check_security_status_for_not_sign_in_or_not_claimed(self):
        """
        Make sure account is not signed
        Verify "Smart Security" option is hidden.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731308
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808878
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808879
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27809326
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27808880

        """
        #not sign in
        self.fc.sign_out()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_security_text_not_display() 
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_security_status_opt_is_hidden()
        self.home.select_navbar_back_btn()
        #not claimed
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_carousel_printer_security_text_not_display()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_security_status_opt_is_hidden()

import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_Printer_Settings_Remote_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
     
        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_check_printer_settings_with_remote_printer(self):
        """
        Add a remote printer to the carousel
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_remote_printer()
        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_status_text(timeout=120)
        self.home.verify_carousel_printer_security_text()

    def test_02_check_printer_settings_with_remote_printer(self):
        """
        Add a remote printer to the carousel
        Navigate to Printer Settings and observe
        Verify Printer Status tab is hidden.
        Verify Supply Status tab is enabled
        Verify Printer Information tab is enabled.(IP address is hide, Printer Email Address is added)
        Verify Network Information tab is hidden.
        Verify the Advanced Setting tab is hidden.
        Verify Printer Anywhere tab is enabled for only GEN II printers 
        if the GEN I printer is selected, Printer anywhere tab is hidden.
        Verify Printer reports tab is hidden.
        Verify See what's printing tab is hidden.
        Verify Print Quality Tools tab is hidden.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25699101
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25699102
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25699103
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25699104
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25699105
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_status_tile(is_remote=True)
        self.printer_settings.verify_information_tile(is_remote=True)
        self.printer_settings.verify_advanced_settings_item_is_hidden()
        self.printer_settings.verify_print_anywhere_option_display()
        self.printer_settings.verify_printer_reports_is_hidden()
        self.printer_settings.verify_print_quality_tools_option_is_hidden()
        self.printer_settings.verify_see_what_printing_option_is_hidden()
        self.printer_settings.verify_manage_tile()
        
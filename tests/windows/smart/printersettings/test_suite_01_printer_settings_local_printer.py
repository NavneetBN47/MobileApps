import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_01_Printer_Settings_Local_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_check_printer_settings_option(self):
        """
        Click "Printer Settings" tile on the Main UI
        Observe Master detail page   
        Verify "Printer Information" is displayed and enabled.
        Verify "Network Information" is displayed and enabled.
        Verify "Print Anywhere" option is hidden.  
        Verify "Hide Printer" tab is displayed and enabled. 
        Verify "Print Reports" tab is displayed and enabled.
        Verify "Print Quality Tools" tab is displayed and enabled.
        Verify "See What's Printing" tab is displayed and enabled. (Win & OEM ONLY)
        Verify "Advanced Settings" tab is displayed and enabled.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731307
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787558(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787559(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787560(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16942831(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787561(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787562(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787563(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16989741(low)
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_status_tile()
        self.printer_settings.verify_information_tile()
        self.printer_settings.verify_settings_tile()
        self.printer_settings.verify_tools_tile()
        self.printer_settings.verify_manage_tile()
        self.printer_settings.verify_print_anywhere_option_is_hidden()

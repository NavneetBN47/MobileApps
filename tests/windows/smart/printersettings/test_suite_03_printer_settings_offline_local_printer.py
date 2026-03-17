import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_Printer_Settings_Offline_Local_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_check_printer_settings_with_offline_printer(self):
        """
        Trigger the offline status for printer.
        Verify "Printer settings" tile is enabled
        Click the Printer Settings tile on main UI.
        Verify "Printer Information" screen opens
        Verify Printer Status tab is enabled.
        Verify Supply Status tab is enabled 
        Verify Network Information tab is disabled.
        Verify Printer Information tab is enabled with minimum item
        Verify Advanced Settings is disable
        Verify Printer Reports tab is disabled
        Verify See What's Printing tab is disabled Note: Mac not support See What's Printing
        Verify Print Quality Tools tab is disabled
        1. Verify Print from other Devices tab is enabled. (Not applicable for OEM)
        2. Verify Forget this Printer tab is enabled.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787534
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787575
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787535
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16991854
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787536
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787537
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787538
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14063489
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16991853
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064100
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064101
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064102
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16991678
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.fc.trigger_printer_offline_status(self.p)
        self.home.verify_carousel_printer_offline_status()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_status_tile()
        self.printer_settings.verify_information_tile()
        self.printer_settings.verify_network_information_not_available()
        self.printer_settings.verify_print_anywhere_option_is_hidden()
        self.printer_settings.verify_settings_tile()
        self.printer_settings.verify_advanced_settings_not_available()
        self.printer_settings.verify_tools_tile()
        self.printer_settings.verify_all_the_opt_not_available_in_tools_tile()
        self.printer_settings.verify_manage_tile()
        self.home.select_navbar_back_btn()

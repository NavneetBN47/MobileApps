import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

class TileNotInOrderException(Exception):
    pass


pytest.app_info = "GOTHAM"
class Test_Suite_07_Home_Tiles_With_Printers(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.scan = cls.fc.fd["scan"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.print = cls.fc.fd["print"]
        cls.printer = cls.fc.fd["printers"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_nine_tiles_shows(self):
        """
        Verify the correct number of tiles show (9 tiles in total).
        Check shell title bar on the main UI, verify shell title bar is removed 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932420
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16977317
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

        if self.printer.verify_pin_dialog(raise_e=False) is not False:
            if self.printer.input_pin(self.p.get_pin()) is True:
                self.printer.select_pin_dialog_submit_btn()

        self.home.verify_main_page_tiles()
        self.home.verify_shell_title_bar_removed()
        
    def test_02_get_supplies_tile_correct_behavior(self):
        """
        Verify "Get Ink" / "Get Supplies" tile opens to correct page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732
        """
        self.home.select_get_supplies_tile()

        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn()
        else:
            self.web_driver.add_window("get_supplies")
            sleep(2)
            self.web_driver.switch_window("get_supplies")
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')

        self.home.verify_home_screen()

    def test_03_scan_tile_correct_behavior(self):
        """
        Verify "Scan" tile opens to scan intro page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732
        """
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()

        self.home.select_navbar_back_btn()

    def test_04_shortcuts_correct_behavior(self):
        """
        Verify correct Smart Tasks page shows.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16977318
        """
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()

        self.shortcuts.click_files_type_back_btn()

    def test_05_print_documents_tile_correct_behavior(self):
        """
        Verify "Print Documents" opens to "Supported Document File Types" dialog/ file picker.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732        
        """
        self.home.select_print_documents_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            if self.home.verify_success_printer_installed_dialog(timeout=120, raise_e=False):
                self.home.select_success_printer_installed_ok_btn()
                self.home.verify_home_screen()
                self.home.select_print_documents_tile()
            else:
                self.home.verify_printer_driver_installed_failed_dialog(timeout=300)
                self.home.select_printer_driver_installed_failed_later_btn()
                self.home.verify_home_screen()
                pytest.skip("Printer driver could not be installed successfully, so skip this test")

        self.print.verify_supported_document_file_types_dialog()

        self.home.select_navbar_back_btn()

    def test_06_mobile_fax_tile_correct_behavior(self):
        """
        Verify "Mobile Fax" tile opens to Mobile Fax get started screen.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27835409     
        """
        self.home.select_mobile_fax_tile()
        self.mobile_fax.verify_mobile_fax_home_screen()

        self.home.select_navbar_back_btn()

    def test_07_help_and_support_tile_correct_behavior(self):
        """
        Verify Help & Support webview opens within the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16977318                          
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_help_and_support_tile()
        self.home.verify_help_and_support_page()

        self.home.select_navbar_back_btn()

    def test_08_print_photos_tile_correct_behavior(self):
        """
        Verify "Print Photos" opens to file picker.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732        
        """
        self.home.select_print_photos_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            if self.home.verify_success_printer_installed_dialog(timeout=120, raise_e=False):
                self.home.select_success_printer_installed_ok_btn()
                self.home.verify_home_screen()
                self.home.select_print_photos_tile()
            else:
                self.home.verify_printer_driver_installed_failed_dialog(timeout=300)
                self.home.select_printer_driver_installed_failed_later_btn()
                self.home.verify_home_screen()
                pytest.skip("Printer driver could not be installed successfully, so skip this test")
        self.print.verify_file_picker_dialog()
        
        self.print.select_file_picker_dialog_cancel_btn()
        self.home.verify_home_screen()

    def test_09_printer_settings_correct_behavior(self):
        """
        Verify "Printer Settings" opens to printer information page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16977318        
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()

        self.home.select_navbar_back_btn()
    
    def test_10_verify_tile_order(self):
        """
        Observe the tile order on the Main UI.

        Verify Instant Ink tile shows on the 1st place. (If the printer is eligible for II)
        Verify Tile shows on the following order left to right:
            Get Ink/Get Supplies
            Scan
            Shortcuts
            Printables
            Print Documents
            Mobile Fax (If enabled)
            Help & Support
            Print Photos
            Printer Settings

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15962728
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212365
        """
        tile_order = ["Instant Ink", ["Get Ink", "Get Supplies"],\
            "Scan", "Shortcuts", "Printables", "Print Documents",\
            "Mobile Fax", "Help & Support", "Print Photos", "Printer Settings"]

        optional_tile_idx = [tile_order.index("Instant Ink"), tile_order.index("Mobile Fax")]
        idx = 0

        for tile_text in tile_order:
            el = self.home.verify_tile_by_index(idx + 1)

            if el.text not in tile_text:
                if idx in optional_tile_idx:
                    idx -= 1
                else:    
                    raise TileNotInOrderException()
            idx += 1

        self.fc.sign_out()
        assert self.home.verify_logged_in() is False

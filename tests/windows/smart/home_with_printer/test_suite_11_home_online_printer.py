import pytest
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_11_Home_Online_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer_status = cls.fc.fd["printer_status"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_check_printer_card_relaunch(self):
        """
        Close the app and reopen it, verify printer still shows on printer card 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14757434
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_offline_status(invisible=True)

    def test_02_click_printer_image(self):
        """
        Click the printer image on the main UI (local printer), verify user navigates to the "Printer Information" page 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890715
        """
        self.home.click_printer_image()
        if not self.printer_status.verify_printer_ioref_status_screen(raise_e=False):
            self.printer_settings.verify_printer_status_page()
        self.home.select_navbar_back_btn()

    def test_03_click_printer_status(self):
        """
        Click the printer status string on the main UI with local printer, verify user navigates to the "Printer Status" page 
        Click the printer status icon on the main UI with local printer, verify user navigates to the "Printer Status" page	
        Hover over printer status in printer card, verify no animation is exist 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890716
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890717
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266578
        """
        if not self.home.verify_carousel_finish_setup_btn(raise_e=False):
            self.home.click_carousel_printer_status_text()
            if not self.printer_status.verify_printer_ioref_status_screen(raise_e=False):
                self.printer_settings.verify_printer_status_page()
            self.home.select_navbar_back_btn()

            self.home.hover_carousel_printer_status_icon()
            sleep(1)
            self.home.click_carousel_printer_status_icon()
            if not self.printer_status.verify_printer_ioref_status_screen(raise_e=False):
                self.printer_settings.verify_printer_status_page()
            self.home.select_navbar_back_btn()

    def test_04_click_ink_level(self):
        """
        Click ink level icon on the main UI (local printer), verify user navigates to the "Supply Status" page
        Hover over supplies level icons in carousel card, verify no animation is exist

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890718
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266577

        """
        if self.home.verify_carousel_estimated_supply_image(raise_e=False):
            self.home.hover_carousel_estimated_supply_image()
            sleep(1)
            self.home.click_carousel_estimated_supply_levels()
            if self.printer_settings.verify_supply_status_page(raise_e=False) is not False:
                self.home.select_navbar_back_btn()
            else:
                self.web_driver.add_window("supply_status_page")
                if "supply_status_page" not in self.web_driver.session_data["window_table"].keys():
                    self.home.click_carousel_estimated_supply_levels()
                    self.web_driver.add_window("supply_status_page")
                self.web_driver.switch_window("supply_status_page")
                current_url = self.web_driver.get_current_url()
                assert "hp.com" in current_url
                self.web_driver.set_size('min')
        else:
            self.home.verify_carousel_finish_setup_btn()

            self.home.verify_home_screen()
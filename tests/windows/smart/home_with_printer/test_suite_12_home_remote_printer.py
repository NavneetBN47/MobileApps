import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

class LogStringFoundException(Exception):
    pass

pytest.app_info = "GOTHAM"
class Test_Suite_12_Home_Remote_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.print = cls.fc.fd["print"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_add_remote_printer(self):
        """
        Add a remote printer to main UI, verify printer is added and shows on main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266580
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()

    def test_02_check_gotham_log(self):
        """
        Add a remote Gen 2 printer to main UI, verify log does not contain "foreign-access"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17843695  
        """
        check_string = "foreign-access"
        sleep(3)
        with self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH) as f:
            data = f.read().decode("utf-8")
        if check_string not in data:
            return True
        raise LogStringFoundException("HP Smart should not call {} API".format(check_string))

    def test_03_restart_app(self):
        """
        Add remote printer on main UI, relaunch app, verify SMB printer still shows as remote 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30553850
        """
        self.fc.restart_hp_smart()
        self.home.verify_printer_add_to_carousel()

    def test_04_click_printer_image(self):
        """
        Click the printer image on the main UI (remote printer), verify user navigates to the "Printer Information" page 	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17843695
        """
        self.home.verify_carousel_printer_offline_status(invisible=True)
        self.home.click_printer_image()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()

    def test_05_click_printer_status_text(self):
        """
        Click the printer status string on the main UI (remote printer), verify user navigates to the "Printer Information" page 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890720
        """
        self.home.verify_carousel_printer_offline_status(invisible=True)
        self.home.click_carousel_printer_status_text()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()

    def test_06_click_printer_status_icon(self):
        """
        Click the printer status icon on the main UI (remote printer), verify user navigates to the "Printer Information" page 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890721
        """
        self.home.verify_carousel_printer_offline_status(invisible=True)
        self.home.click_carousel_printer_status_icon()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()

    def test_07_click_ink_level(self):
        """
        Click ink level icon on the main UI (remote printer), verify user navigates to the "Supply Status" page
        Check main UI ink levels, verify "Estimated supply levels" string and correct ink levels shows
        Add OfficeJet Pro printer to main UI (individual cartridges), verify "Estimated supply levels" string and correct ink level shows on printer card 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890722
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/24220327
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27426951
        """
        self.home.verify_carousel_printer_offline_status(invisible=True)
        if self.home.verify_carousel_estimated_supply_image(timeout=60, raise_e=False):
            assert self.home.verify_carousel_estimated_supply_text().text == "Estimated supply levels"
            self.home.click_carousel_estimated_supply_levels()
            if self.printer_settings.verify_supply_status_page(raise_e=False) is not False:
                self.home.select_navbar_back_btn()
            else:
                self.web_driver.add_window("supply_status_page")
                self.web_driver.switch_window("supply_status_page")
                current_url = self.web_driver.get_current_url()
                assert "hp.com" in current_url
                self.web_driver.set_size('min')

            self.home.verify_home_screen()

    def test_08_sign_out(self):
        """
        Log out from app (remote printer), verify printer is removed from main UI 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17843687
        """
        self.fc.sign_out()
        assert self.home.verify_logged_in() is False
        self.home.verify_setup_or_add_printer_card()

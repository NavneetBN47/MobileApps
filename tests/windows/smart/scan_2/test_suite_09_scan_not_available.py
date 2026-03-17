import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_09_Scan_Not_Available(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

    def test_01_click_add_button_on_preview_without_network(self):
        """
        Click on 'Scan' button
        Click "+Add" from the Preview to add more scanned page
        Repeat step 1 and 2 till you have more than 5 scanned images/pages
        While in Preview screen make the printer goes offline and click on '+Add"

        Verify "Scanning is currently unavailable" shows in Scan home screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639459  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639463 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639460
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639461
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.fc.trigger_printer_offline_status(self.p)
        self.scan.click_add_pages_btn()
        self.scan.verify_scanning_unavailable_screen()
        self.scan.click_return_home_btn()
        self.home.verify_home_screen()

    def test_02_connect_wifi(self):
        if "DunePrinterInfo" in str(self.p.p_obj):
            self.p.pp_module._power_on()
        else:
            self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)

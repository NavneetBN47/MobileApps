import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_03_Help_Support_Offline_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.help_support = cls.fc.fd["help_support"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]

        cls.stack = request.config.getoption("--stack")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_add_printer(self):
        """
        Add printer to Home page.  
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

    def test_02_check_diagnose_fix_link_offline_printer(self):
        """
        Click "Diagnose & Fix" link from Help & Support -> Print, Scan and Share -> Printing, verify "Diagnose and Fix" flow launched
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/42736316      
        """
        try:
            self.fc.trigger_printer_offline_status(self.p)             
            self.home.verify_carousel_printer_offline_status()

            self.home.select_help_and_support_tile()
            self.help_support.verify_help_center_screen()
            self.help_support.swipe_and_click_item(self.help_support.PRINTING_ITEM)
            self.help_support.click_item(self.help_support.DIAGNOSE_FIX_LINK)
            self.home.verify_connect_to_your_printer_screen()
            self.home.click_diagnose_and_fix_link()
            self.home.verify_diagnose_and_fix_screen()
            self.home.select_navbar_back_btn(return_home=False)
            self.home.verify_connect_to_your_printer_screen()
            self.home.select_navbar_back_btn()

        finally:
            self.fc.restore_printer_online_status(self.p)

        self.home.verify_carousel_printer_offline_status(timeout=60, invisible=True)
        self.home.select_help_and_support_tile()
        self.help_support.verify_help_center_screen()
        self.help_support.swipe_and_click_item(self.help_support.PRINTING_ITEM)
        self.help_support.click_item(self.help_support.DIAGNOSE_FIX_LINK)
        self.diagnose_fix.verify_diagnoseing_and_fixing_text_display()
        self.diagnose_fix.verify_diagnosis_complete_screen()


    
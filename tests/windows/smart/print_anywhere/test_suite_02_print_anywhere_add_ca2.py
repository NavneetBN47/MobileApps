import pytest
from time import sleep

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_Print_Anywhere_ca2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printers = cls.fc.fd["printers"]
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
        """
        Install app and launch app
        Sign in to the account that claimed the printer
        Make sure printer and computer are not on the same networks
        Add the remote printer from device picker
        Verify the remote printer shows in device picker
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24283697
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24287186 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17155849 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24287183(low Main ui)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24287184(low Main ui)
        """
        self.driver.terminate_app()
        self.printer_settings.enable_useca2()
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_status_text(timeout=120)
        self.home.verify_carousel_printer_security_text()
        if self.home.verify_print_anywhere_dialog(raise_e=False):
            self.home.select_paw_x_btn()

    def test_02_check_print_settings(self):
        """
        Click Print/Print Settings
        Verify Print Settings shows limited tabs
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24284717(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24287190(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24218229(low)
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_print_anywhere_option_display()
        
    def test_03_check_check_print_settings_with_non_hpc(self):
        """
        Computer is on non-HPC region.
        Printer is Gen2 printer.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064326(low)
        """
        self.driver.terminate_app()
        self.sf.change_pc_region_to_non_hpc_region()
        sleep(3)
        self.driver.launch_app()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_status_text(timeout=120)
        self.home.verify_carousel_printer_security_text()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_print_anywhere_option_is_hidden()
    
    def test_04_clean_env(self):
        self.driver.terminate_app()
        self.sf.change_pc_region_to_us_region()
        sleep(3)
        self.driver.launch_app()

    def test_05_check_dp_without_sign_in(self):
        """
        Sign out from main UI
        Go to device picker and observe
        Verify the remote printer does not show in device picker
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24283696
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24287187
        """
        self.home.verify_home_screen()
        self.fc.sign_out()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.verify_remote_printer_not_show()
        
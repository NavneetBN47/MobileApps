import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_03_Hide_Printer_Main_UI_Owner(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.smart_dashboard = cls.fc.fd["smart_dashboard"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_add_remote_printer(self):
        """
        Add a remote printer that claimed to the account to carousel
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_remote_printer()
        self.home.verify_printer_add_to_carousel()

    def test_02_check_hide_printer_btn_owner_version(self):
        """
        Hide a printer from main UI (Owner version), verify flow
        [Owner account]Click Hide printer option , verify confirmation modal "Hide this printer?" displays
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388305
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388309
        """
        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()

        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load(owner=True)

        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        assert self.home.verify_carousel_printer_image(timeout=5, raise_e=False) is False

    def test_03_check_go_to_dashboard_btn_owner_version(self):
        """
        [Owner account] Click "Go to Dashboard" button on the Hide printer dialog, verify user navigated to the portal printer page 	
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29458299
        """
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_remote_printer()
        self.home.verify_printer_add_to_carousel()

        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()

        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load(owner=True)

        self.home.click_hide_this_printer_dialog_go_to_dashboard_btn()

        self.smart_dashboard.verify_my_account_page()
        self.home.select_navbar_back_btn()
        assert self.home.verify_carousel_printer_image(timeout=5, raise_e=False) is False

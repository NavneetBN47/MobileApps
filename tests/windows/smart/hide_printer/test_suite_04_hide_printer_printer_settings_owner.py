import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_04_Hide_Printer_Printer_Settings_Owner(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
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

    def test_02_check_hide_this_printer_is_block_model(self):
        """
        Click Back arrow when "Hide this printer" dialog is up, verify user land on the Main UI
        Verify "Hide Printer" dialog is blocking model
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538524
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538514
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()

        self.printer_settings.select_hide_printer_item()
        self.printer_settings.verify_hide_this_printer_screen()

        self.printer_settings.select_hide_this_printer_btn()
        self.home.verify_hide_this_printer_dialog_load(owner=True)

        self.printer_settings.select_supply_status_option()
        self.home.verify_hide_this_printer_dialog_load(owner=True)

        self.home.select_navbar_back_btn()
        assert self.home.verify_hide_this_printer_dialog_load(owner=True, raise_e=False) is False
        self.home.verify_carousel_printer_image()

    def test_03_check_cancel_btn_owner_version(self):
        """
        Select "Cancel" button on confirmation modal "Hide Printer", verify this cancels the process
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538508
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()

        self.printer_settings.select_hide_printer_item()
        self.printer_settings.verify_hide_this_printer_screen()

        self.printer_settings.select_hide_this_printer_btn()
        self.home.verify_hide_this_printer_dialog_load(owner=True)
        self.home.click_hide_this_printer_dialog_cancel_btn()
        assert self.home.verify_hide_this_printer_dialog_load(owner=True, raise_e=False) is False

    def test_04_check_hide_printer_btn_owner_version(self):
        """
        Hide a printer from Printer settings (Owner version), verify flow
        Select the "Hide Printer" button on the confirmation modal , verify printer is removed from the printer card 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538503
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538507
        """
        self.printer_settings.verify_hide_this_printer_screen()

        self.printer_settings.select_hide_this_printer_btn()
        self.home.verify_hide_this_printer_dialog_load(owner=True)
        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        assert self.home.verify_hide_this_printer_dialog_load(owner=True, raise_e=False) is False
        assert self.home.verify_carousel_printer_image(timeout=5, raise_e=False) is False

    def test_05_check_go_to_dashboard_btn_owner_version(self):
        """
        [Owner account] Click "Go to Dashboard" button on the Hide printer dialog and remove the printer, verify user navigated to the portal printer page 	
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538513
        """
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_remote_printer()
        self.home.verify_printer_add_to_carousel()

        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()

        self.printer_settings.select_hide_printer_item()
        self.printer_settings.verify_hide_this_printer_screen()
        self.printer_settings.select_hide_this_printer_btn()

        self.home.verify_hide_this_printer_dialog_load(owner=True)
        self.home.click_hide_this_printer_dialog_go_to_dashboard_btn()

        self.smart_dashboard.verify_my_account_page()
        self.home.select_navbar_back_btn()
        assert self.home.verify_carousel_printer_image(timeout=5, raise_e=False) is False

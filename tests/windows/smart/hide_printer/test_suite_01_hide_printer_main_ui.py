import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_01_Hide_Printer_Main_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_check_hide_printer_option(self):
        """
        Right click on printer in printer card, verify "Hide Printer" option appears
        Right click for printer menu and then click outside menu, verify Hide printer option disappears
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388306
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388307
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()

        self.home.select_menu_btn()
        assert self.home.verify_hide_printer_list_item_load(raise_e=False) is False

    def test_02_check_hide_this_printer_dialog(self):
        """
        [non Owner account]Click Hide printer option , verify confirmation modal "Hide this printer?" displays
        Verify "Hide Printer" dialog is blocking model
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29458297
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538501
        """
        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()

        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load()

        self.home.select_my_hp_account_btn()
        assert self.home.verify_fly_out_sign_in_page(timeout=5, raise_e=False) is False

    def test_03_check_cancel_btn_on_hide_this_printer_dialog(self):
        """
        Select "Cancel" button on confirmation modal "Hide Printer", verify this cancels the process
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388312
        """    
        self.home.click_hide_this_printer_dialog_cancel_btn()
        assert self.home.verify_hide_this_printer_dialog_load(raise_e=False) is False

    def test_04_check_hide_printer_btn_on_hide_this_printer_dialog(self):
        """
        Select the "Hide Printer" button on the confirmation modal , verify printer is removed from the printer card
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388311
        """ 
        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()

        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load()

        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        assert self.home.verify_carousel_printer_image(timeout=10, raise_e=False) is False

    def test_05_check_same_printer_add_again(self):
        """
        Re add the hide printer from the device picker, verify Device picker shows the same printer
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538502
        """
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen(timeout=60)
        self.fc.select_a_printer(self.p)

    def test_06_hide_printer_flow_sign_in_non_owner(self):
        """
        Hide a printer from main UI (non- Owner version), verify flow
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388318
        """
        self.home.verify_carousel_printer_image(timeout=60)
        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()
        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load()

        self.home.click_hide_this_printer_dialog_cancel_btn()
        assert self.home.verify_hide_this_printer_dialog_load(raise_e=False) is False

        self.home.right_click_printer_carousel()
        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load()

        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        assert self.home.verify_carousel_printer_image(timeout=10, raise_e=False) is False
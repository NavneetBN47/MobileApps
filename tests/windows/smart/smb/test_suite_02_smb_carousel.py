import pytest

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_02_SMB_Device_Carousel(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup  
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.scan = cls.fc.fd["scan"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.stack = request.config.getoption("--stack")
        if cls.stack == "stage":
            login_info = ma_misc.get_smb_account_info("stage_journey_testing")
        else:
            login_info = ma_misc.get_smb_account_info(cls.stack)
        cls.username, cls.password = login_info["email"], login_info["password"]

    def test_01_check_carousel_with_my_printer_org(self):
        """
        Add a printer to the carousel via any available entry
        Select the personal org "My Printer" on Org Picker
        Verify all the tiles are available.
        Verify local printer is not removed from the carousel
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123433
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        local_printer_name=self.home.get_carousel_printer_model_name()
        self.fc.sign_in(self.username, self.password)
        self.home.verify_welcome_back_dialog()
        self.home.select_an_organization_list_item(4)
        self.home.select_welcome_back_continue_btn()
        self.home.verify_home_screen()
        assert self.home.get_carousel_printer_model_name() == local_printer_name
     

    def test_02_check_hide_printer_with_local_printer_carousel(self):
        """
        Verify correct Hide flow shows
        Verify Invited user can only hide the printer from HP Smart home page
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123442
        """
        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()
        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load()
        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        assert self.home.verify_carousel_printer_image(raise_e=False) is False

    def test_03_check_no_sign_in_with_local_printer_carousel(self):
        """
        Sign in using SMB account which has multiple Orgs with printers associated
        Select a business Org from Org Picker
        Add a could printer to the carousel
        Now sign out of the app
        Add a remote printer to the carousel via any available entry ( Printer and PC network must be the same. 
        As you are sign in as SMB account you will not see the printer as local printer in DP)
        Click on Scan tile
        Verify user is able to use the printer scan.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123434
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31268719
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123445
        """
        self.fc.select_a_printer(self.p)
        local_printer_name=self.home.get_carousel_printer_model_name()
        self.fc.sign_out()
        self.home.verify_home_screen()
        self.fc.sign_in(self.username, self.password)
        self.home.verify_welcome_back_dialog()
        self.home.select_an_organization_list_item(2)
        self.home.select_welcome_back_continue_btn()
        self.home.verify_home_screen()
        self.home.verify_carousel_add_printer_btn()
        self.home.select_left_add_printer_btn()
        self.printers.verify_smb_searching_screen()
        self.printers.verify_smb_device_picker_screen()
        printer = self.printers.search_printer('HP Office')
        printer.click()
        # self.printers.select_remote_printer()
        self.home.verify_home_screen()
        sleep(10)
        # self.home.select_scan_tile()
        # self.scan.verify_scan_intro_page(is_remote_printer=True)
        # self.scan.click_get_started_btn()
        # self.scan.click_scan_btn()
        # self.scan.verify_scan_result_screen()
        # self.home.select_navbar_back_btn(return_home=False)
        # self.scan.verify_exit_without_saving_dialog()
        # self.scan.click_yes_btn()
        # self.scan.verify_scanner_screen()
        # self.home.select_navbar_back_btn()
        assert self.home.get_carousel_printer_model_name() != local_printer_name
        self.fc.sign_out()
        self.home.verify_home_screen()
        assert self.home.get_carousel_printer_model_name() == local_printer_name
        
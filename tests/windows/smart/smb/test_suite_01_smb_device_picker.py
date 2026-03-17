import pytest

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_01_SMB_Device_Picker(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup  
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.stack = request.config.getoption("--stack")
        if cls.stack == "stage":
            login_info = ma_misc.get_smb_account_info("stage_journey_testing")
        elif cls.stack == "production":
            login_info = ma_misc.get_smb_account_info(cls.stack)
        else:
            pytest.skip("Skip this test as printer is offline with pie stack")
        cls.username, cls.password = login_info["email"], login_info["password"]

    def test_01_check_dp_with_no_printer_account(self):
        """
        Signin via with an SMB Account
        Select org1 that has no printers, check DP

        Verify DP screen shows with "No available printers found..." msg
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110406
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30717284
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100065
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100068(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100071
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100072(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100073
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100075(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110411(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110459
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29371528
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30717286
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30717283
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30774856(low)
        """
        self.fc.go_home()
        self.fc.sign_in(self.username, self.password)
        if self.home.verify_welcome_back_dialog(raise_e=False) is not False:
            if self.stack == "production":
                self.home.select_an_organization_list_item(3)
            else:
                self.home.select_an_organization_list_item(1)
            self.home.select_welcome_back_continue_btn()
        else:
            self.home.select_my_hp_account_btn()
            self.home.select_an_organization_list_item(1)
        sleep(5)
        self.home.select_left_add_printer_btn()
        self.printers.verify_smb_device_picker_screen(has_printer=False)
        self.printers.select_refresh_list_link()
        self.printers.verify_smb_device_picker_screen(has_printer=False)
        self.printers.search_printer(w_const.TEST_TEXT.INVALID_IP, value=False)
        self.printers.verify_warning_message_display(w_const.TEST_TEXT.WARNING_MSG_VALUE, w_const.TEST_TEXT.INVALID_IP)

    def test_02_check_dp_with_printer_account(self):
        """
        Switch to org2 that has printers, check DP

        Verify DP screen shows with org2 associated printers
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110406
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123436
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123444
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110414
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31099405
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100013(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100066(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31100067(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110412(since GOTH-22358 printer should displays)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110413
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110415
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30717294
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30717295
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30797474(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30794745
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123441
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123443
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31356579
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31864128  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30553849     
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29371536    
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29371535  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31747078
        """
        self.home.select_navbar_back_btn()
        self.home.select_my_hp_account_btn()
        self.home.select_an_organization_list_item(2)
        sleep(5)
        self.home.select_left_add_printer_btn()
        self.printers.verify_smb_searching_screen()
        self.printers.verify_smb_device_picker_screen()
        printer = self.printers.search_printer('HP Office')
        printer.click()
        # self.printers.select_remote_printer()
        self.home.verify_home_screen()
        printer_name=self.home.get_carousel_printer_model_name()
        if self.home.verify_print_anywhere_dialog(raise_e=False):
            self.home.select_paw_x_btn()
        self.home.click_carousel_estimated_supply_levels()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item_is_hidden()
        self.printer_settings.verify_printer_reports_is_hidden()
        self.printer_settings.verify_print_quality_tools_option_is_hidden()
        self.printer_settings.verify_see_what_printing_option_is_hidden()
        self.printer_settings.verify_print_quality_tools_option_is_hidden()
        self.printer_settings.verify_print_from_other_devices_is_hidden()
        self.printer_settings.verify_supply_status_opt_is_hidden()
        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()
        self.home.click_printer_image()
        self.printer_settings.verify_printer_settings_page()
        self.driver.restart_app()
        self.gotham_utility.click_maximize()
        self.home.verify_home_screen()
        self.home.verify_carousel_estimated_supply_image()
        self.home.select_my_hp_account_btn()
        self.home.verify_org_ltem_is_selected(2)
        self.home.select_navbar_back_btn()
        assert self.home.get_carousel_printer_model_name() in printer_name
        self.home.select_left_add_printer_btn()
        self.printers.verify_smb_device_picker_screen()
        self.home.select_navbar_back_btn()

    def test_03_switch_org_and_sign_out(self):
        """
        Switch to org

        Sign out from the SMB account when printer is in stable condition 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123447
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110449
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31089515
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31110410
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31164506
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31164914
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30797523(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30797525(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30797527(low)
                  
        """
        self.home.select_my_hp_account_btn()
        self.home.select_an_organization_list_item(4)
        sleep(5)
        self.driver.restart_app()
        self.gotham_utility.click_maximize()
        self.home.verify_home_screen()
        self.home.select_my_hp_account_btn()
        self.home.verify_org_ltem_is_selected(4)
        self.home.select_navbar_back_btn()
        self.home.verify_carousel_add_printer_btn()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.home.select_navbar_back_btn()
        self.home.select_my_hp_account_btn()
        if self.stack == "pie":
            self.home.select_an_organization_list_item(3)
        else:
            self.home.select_an_organization_list_item(2)
        sleep(5)
        self.fc.sign_out()
        self.home.verify_carousel_add_printer_btn()

    def test_04_re_sign_in(self):
        """
        Sign in as smb user => "My printer" org should shows along with other smb orgs
        Select "My Printer" from org picker in Home page (Navigation bar for win, Title bar for Mac)
        Open DP and select not claimed network printer  
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31164907
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123435
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123437
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123439
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31123446
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/44468135
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32757272
        """
        self.fc.sign_in(self.username, self.password)
        self.home.verify_welcome_back_dialog()
        self.home.select_an_organization_list_item(4)
        self.home.select_welcome_back_continue_btn()
        self.home.verify_home_screen()
        self.fc.select_a_printer(self.p)
        self.home.click_carousel_estimated_supply_levels()
        if self.printer_settings.verify_supply_status_page(raise_e=False):
            if self.home.verify_navbar_back_btn(raise_e=False):
                self.home.select_navbar_back_btn()
        else:
            if self.home.verify_navbar_back_btn(raise_e=False):
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

        self.home.verify_home_screen()
        self.fc.sign_out()
        self.home.verify_printer_still_displays()
        
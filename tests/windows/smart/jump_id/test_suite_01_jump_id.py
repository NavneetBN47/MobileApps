import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.common.exceptions import NoSuchElementException

pytest.app_info = "GOTHAM"
class Test_Suite_01_Jump_IDs(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.cec = cls.fc.fd["cec"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]
        cls.printer_status = cls.fc.fd["printer_status"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_to_main_ui_login_add_printer(self):
        """
        Printer must be II eligable
        Computer region must be set as II supported region
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    def test_02_check_jump_id_from_cec_tile(self):
        """
        Click on the II related CEC tile on the Main UI
        Close the app once you see the DSP page
        heck Gotham log        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29504565
        """
        if self.stack == 'pie':
            pytest.skip("Never Run out save CEC item is only available for Stage Stack")
        self.home.verify_cec_banner()
        self.home.verify_cec_engagement_list_items()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)

        # GOTH-25062:DSP related engagement "Never run out & save"" is missing in CEC Jweb area after sign in accounts (HP+ & ucde). 
        self.cec.verify_never_run_out_save_tile()
        self.cec.click_never_run_out_save_tile()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn()
        else:
            self.web_driver.wait_for_new_window(timeout=30)
            self.web_driver.add_window("get_supplies")
            sleep(2)
            self.web_driver.switch_window("get_supplies")
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')

        self.home.verify_home_screen()
        self.driver.terminate_app()
        check_string = 'in_r11549_ii2_winhpsmart_cec_03012021'
        self.fc.check_gotham_log(check_string)

    def test_03_check_jump_id_from_get_supplies_tile(self):
        """
        Click on the II (Get supplies) tile on the Main UI
        Close the app after DSP page is loaded
        Check the Gotham log           
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29504566
        """
        self.driver.launch_app()
        self.home.verify_home_screen()
        self.home.select_get_supplies_tile()
        if self.dedicated_supplies_page.verify_not_now_dialog():
            self.dedicated_supplies_page.select_not_now_btn()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn()
        else:
            self.web_driver.wait_for_new_window(timeout=15)
            self.web_driver.add_window("get_supplies")
            sleep(3)
            self.web_driver.switch_window("get_supplies")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                raise NoSuchElementException('Failed launch instant ink url')
            self.web_driver.close_window("get_supplies")
        self.home.verify_home_screen()
        self.driver.terminate_app()
        check_string = 'in_r11549_ii2_winhpsmart_tile_042919'
        self.fc.check_gotham_log(check_string)

    def test_04_check_jump_id_from_get_supplies_tile(self):
        """
        Click on the II (Get supplies) tile on the Main UI
        Close the app after DSP page is loaded
        Check the Gotham log           
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29504567
        """
        self.driver.launch_app()
        self.home.verify_home_screen()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        sleep(2)
        self.printer_settings.select_supply_status_option()
        if self.printer_settings.verify_supply_status_page():
            self.home.select_navbar_back_btn()
        else:
            self.web_driver.add_window("supply_status_page")
            sleep(3)
            self.web_driver.switch_window("supply_status_page")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')
        self.driver.terminate_app()\
        
        check_string = 'in_r11549_ii2_winhpsmart_supplystatus-pst_042919'
        self.fc.check_gotham_log(check_string)

    def test_05_check_jump_id_from_ink_icon_on_the_carousel(self):
        """
        Click Ink icon on the carousel
        Close the app after you see the DSP page
        Check the Gotham log           
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33137590
        """
        self.driver.launch_app()
        self.home.verify_home_screen()
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
        self.driver.terminate_app()
        check_string = 'in_r11549_ii2_winhpsmart_supplystatus-car_042919'
        self.fc.check_gotham_log(check_string)

    def test_06_check_jump_id_from_supply_related_status(self):
        """
        Generate supply related status
        CLick on the estimated supplys and start II flow
        Close the app once you see the DSP page
        check the Gotham log      
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29504570
        """
        self.driver.launch_app()
        self.home.verify_home_screen()
        self.fc.trigger_printer_status(self.serial_number, ["66378"])
        self.printer_status.click_ps_body_btn("Get Supplies")
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
        self.driver.terminate_app()
        check_string = 'in_r11549_ii2_winhpsmart_printerstatus_042919'
        self.fc.check_gotham_log(check_string)
        
import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_07_User_Onboarding_Tiles_Get_Supplies(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.printer = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        

    def test_01_add_printer(self):
        """
        Add printer
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_close_sign_in_up_dialog(self):
        """
        Click "X" button on the HPID Sign in/Create account dialog, verify user navigates to the Home page
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731495
        """
        self.home.select_get_supplies_tile()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            if self.dedicated_supplies_page.verify_try_instant_ink_free_link():
                self.dedicated_supplies_page.select_try_instant_ink_free_link()
                self.moobe.click_button_on_fp_from_printer(self.p)
                self.fc.enter_printer_pin_number(self.p.get_pin())    
                self.fc.verify_hp_id_sign_in_up_page(timeout=30, is_sign_up=True)

            elif self.dedicated_supplies_page.verify_get_started_now_link():
                self.dedicated_supplies_page.select_get_started_now_link()
                self.moobe.click_button_on_fp_from_printer(self.p)
                self.fc.enter_printer_pin_number(self.p.get_pin())
                self.fc.verify_hp_id_sign_in_up_page(timeout=30, is_sign_up=True)

            elif self.dedicated_supplies_page.verify_finish_setup_link():
                self.dedicated_supplies_page.select_finish_setup_link()
                self.moobe.click_button_on_fp_from_printer(self.p)
                self.fc.enter_printer_pin_number(self.p.get_pin())    
                self.fc.verify_hp_id_sign_in_up_page(timeout=30, is_sign_up=True)

            elif self.dedicated_supplies_page.verify_sign_in_link():
                self.dedicated_supplies_page.select_sign_in_link()
                self.fc.verify_hp_id_sign_in_up_page(timeout=30)
            else:
                self.dedicated_supplies_page.select_get_started_with_hp_instant_ink_link()
                self.moobe.click_button_on_fp_from_printer(self.p)
                self.fc.enter_printer_pin_number(self.p.get_pin())    
                self.fc.verify_hp_id_sign_in_up_page(timeout=30, is_sign_up=True)
            
            self.fc.close_hp_id_sign_in_up_page()
        else:
            logging.info("Link opens on extenal browser...")
            self.web_driver.add_window("get_supplies")
            self.web_driver.switch_window("get_supplies")
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')
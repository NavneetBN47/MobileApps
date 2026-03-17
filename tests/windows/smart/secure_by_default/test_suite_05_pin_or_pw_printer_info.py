import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.webdriver.common.keys import Keys
import logging
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_05_pin_or_pw_printer_info(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.printer_ip_address = cls.p.p_obj.ipAddress
    
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.stack = request.config.getoption("--stack")
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        cls.pin_num = cls.p.get_pin()
   
    def test_01_printer_oobe_reset_and_skip_push_dialog(self):
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Stack Reset for printer...")
        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")
        self.p.exit_oobe()
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        self.fc.go_home()
        self.home.click_carousel_add_printer_btn()
        self.printers.verify_device_picker_screen()
        printer = self.printers.search_printer(self.printer_ip_address)
        printer.click()
        self.moobe.verify_connected_printing_services_screen()
        self.moobe.select_accept_all_btn()
        self.moobe.verify_touch_checkmark_dialog(timeout=20)
        self.p.click_front_panel_btn("fb_allow")
        self.printers.verify_exit_setup_btn(timeout=20)
        self.printers.select_exit_setup()
        self.printers.select_pop_up_exit_setup()
        if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
            self.printers.select_pop_up_exit_setup()
        if self.printers.verify_install_success_dialog(raise_e=False):
            self.printers.click_install_success_dialog_continue_btn()
        self.home.verify_home_screen()
        self.fc.web_password_credential_delete()

    def test_02_check_pin_or_pw_prompt_dialog_with_change_country_language(self):
        """
        Add the test secure printer to main UI.
        Go to printer Information tab.
        Change country/language.
        Click Save button on Set Country/Language dialog.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628899
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628901
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628902
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628903
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628907
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628900
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628908
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628909
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628910
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628911
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628912
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628913
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628914
                  pw
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581534
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581949(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17451820
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581950
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581951
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581954
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581955
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581956
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17856582
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17856584
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24582342(GOTH-10651)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17433312(GOTH-10651)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24582056(GOTH-10651)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24582436
        """
        self.p.fake_action_door_open()
        sleep(3)
        self.home.select_printer_settings_tile()
        self.__change_printer_country_region()
        if self.printers.verify_pin_dialog(raise_e=False):
            self.printers.verify_pin_dialog()
            self.printers.verify_pin_dialog_submit_btn_not_enabled()
            self.printers.select_pin_cancel_btn()
            sleep(1)
            self.__change_printer_country_region()
            self.printers.input_pin("11111111")
            self.printers.select_pin_dialog_submit_btn()
            if self.printers.verify_sign_in_dialog_show(raise_e=False):
                self.printers.verify_incorrect_pw_dialog_show()
            else:
                self.printers.verify_incorrect_pin_dialog_show()
            self.printers.select_pin_cancel_btn()
            self.__change_printer_country_region()
            self.printers.verify_pin_dialog()
            try:
                self.fc.trigger_printer_offline_status(self.p)
                self.printers.input_pin(self.pin_num)
                self.printers.select_pin_dialog_submit_btn()
                self.printers.verify_network_error_pin_dialog_show()
                self.printers.select_pin_cancel_btn()
                self.__change_printer_country_region()
                assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False
            finally:
                self.fc.restore_printer_online_status(self.p)
            self.__change_printer_country_region()
            if not self.printers.verify_sign_in_dialog_show(raise_e=False):
                self.printers.input_pin("11111111")
                for _ in range(11):
                    self.printers.select_pin_dialog_submit_btn()
                self.printers.verify_incorrect_pin_enter_dialog_show()
                self.printers.click_ok_btn()
            self.__change_printer_country_region()
            self.printers.verify_pin_dialog()
            self.printers.input_pin(self.pin_num)
            self.printers.select_pin_dialog_submit_btn()
            assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False
        else:
            self.p.fake_action_door_close()
            pytest.skip("The printer PIN is not available or has not password set, can not do this test")

    def test_03_clear_env(self):
        self.p.fake_action_door_close()
        self.fc.restart_hp_smart()
        self.fc.restore_printer_info_country_language(self.pin_num)


     #****************PRIVATE FUNCTION****************
    def __change_printer_country_region(self):
        """
        Change printer country region 
        """
        sleep(1)
        self.printer_settings.verify_preference_country_part()
        select_item = self.printer_settings.get_country_region_text()
        self.printer_settings.click_country_dropdown()
        el = self.printer_settings.verify_country_select_item(select_item)
        el.send_keys(Keys.UP, Keys.ENTER)
        self.printer_settings.verify_set_country_or_language_dialog()
        self.printer_settings.click_set_save_btn()

import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import logging
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_02_pin_advanced_settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
    
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.printer_ip_address = cls.p.p_obj.ipAddress
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
  
    def test_02_check_ews_page_locked_with_pin_num(self):
        """
        Go to Printer Settings.
        Select "Advanced Settings" (EWS).
        Click on any tile with a lock sign on it (see below for an example of ews screen).
        Verify pin prompt shows.
        Enter incorrect pin on the Advanced Settings secure prompt.
        Enter correct Pin on the Access Secure Settings dialog.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17855001  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973458 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973457
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17856566
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973463
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973464
        """
        sleep(3)
        self.p.fake_action_door_open()
        self.__make_pin_dialog_displays()
        if self.printer_settings.verify_log_in_with_pin_dialog(raise_e=False):
            self.printer_settings.click_sign_in_cancel_btn()
            self.printer_settings.verify_log_in_with_pin_dialog(invisible=True)
            self.printer_settings.click_ews_home_title()
            self.printer_settings.click_network_summary_tile()
            self.printer_settings.verify_log_in_with_pin_dialog()
            self.printer_settings.enter_pin_num("11111111")
            self.printer_settings.click_submit_btn()
            self.printer_settings.verify_log_in_with_pin_dialog()
            self.printer_settings.incorrect_pin_text()
        else:
            self.p.fake_action_door_close()
            pytest.skip("The printer PIN is not available, can not do this test")

    def test_03_check_pin_num_dialog_with_turn_off_printer(self):
        """
        Turn off printer after the Advanced Settings(EWS) secure prompt shows.
        Enter correct Pin and click Submit.
        Click Cancel on the secure prompt.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973462
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973461
          
        """
        try:
            self.fc.trigger_printer_offline_status(self.p)
            self.printer_settings.click_sign_in_cancel_btn()
            self.printer_settings.verify_sign_in_text_display()
            self.home.select_navbar_back_btn()
        finally:
            self.fc.restore_printer_online_status(self.p)
        self.__go_to_the_log_in_with_pin_dialog_from_home_page()
        try:
            self.fc.trigger_printer_offline_status(self.p)
            self.printer_settings.enter_pin_num(self.pin_num)
            self.printer_settings.verify_sign_in_text_display()
            self.home.select_navbar_back_btn()
        finally:
            self.fc.restore_printer_online_status(self.p)

    def test_04_enter_correct_Pin(self):
        """
        Enter correct Pin on the Access Secure Settings dialog.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/26973456
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17856564
        
        """
        self.__go_to_the_log_in_with_pin_dialog_from_home_page()
        self.printer_settings.enter_pin_num(self.pin_num)
        self.printer_settings.verify_sign_out_text_display()

    def test_05_clear_env(self):
        self.p.fake_action_door_close()
 
    #****************PRIVATE FUNCTION****************
    def __go_to_the_log_in_with_pin_dialog_from_home_page(self):
        """
        go to the log in with pin dialog
        """
        self.__make_pin_dialog_displays()
        self.printer_settings.verify_log_in_with_pin_dialog()

    def __make_pin_dialog_displays(self):
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        if self.printer_settings.verify_continuing_to_your_printer_settings_dialog():
            self.printer_settings.click_the_pin_ok_btn()
        self.printer_settings.verify_ews_page()
        self.printer_settings.verify_tile_are_locked()
        self.printer_settings.click_network_summary_tile()
        
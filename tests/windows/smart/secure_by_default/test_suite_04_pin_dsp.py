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
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
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

    def test_02_check_pin_prompt_dialog_with_dsp_flow(self):
        """
        Add the test secure printer to main UI.
        Start DSP Enroll flow in any DSP entries. (Click "Get Ink" tile or ink levels on main UI or "Supply status" tab in printer settings ...etc)
        Generate any printer error (eg: Door open/ ink missing/ out of paper/...).
        Turn off printer before "Find the printer PIN" dialog shows.
        Continue the DSP enroll flow.
        Verify "Find the printer PIN" dialog shows during the flow.
        
        Click the "Cancel" button on the "Find the printer PIN" dialog.
        Verify "Submit" button does not show enabled until something is entered to the text box.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615989 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615991
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615992
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615993
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24616000
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615997
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615998
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615999
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24616002
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615990
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24616001
        """
        sleep(3)
        self.p.fake_action_door_open()
        self.home.select_get_supplies_tile()
        if self.dedicated_supplies_page.verify_try_instant_ink_free_link():
            self.dedicated_supplies_page.select_try_instant_ink_free_link()
        if self.dedicated_supplies_page.verify_finish_setup_link():
            self.dedicated_supplies_page.select_finish_setup_link()
        if self.printers.verify_pin_dialog(raise_e=False):
            self.printers.verify_pin_dialog()
            self.printers.verify_pin_dialog_submit_btn_not_enabled()
            self.printers.select_pin_cancel_btn()
            self.printers.verify_pin_dialog()
            self.printers.input_pin("11111111")
            self.printers.select_pin_dialog_submit_btn()
            self.printers.verify_incorrect_pin_dialog_show()
            self.printers.select_pin_cancel_btn()
            self.printers.verify_pin_dialog()
            try:
                self.fc.trigger_printer_offline_status(self.p)
                self.printers.input_pin(self.pin_num)
                self.printers.select_pin_dialog_submit_btn()
                self.printers.verify_network_error_pin_dialog_show()
                self.printers.select_pin_cancel_btn()
                self.printers.verify_sign_in_dialog_show()
            finally:
                self.fc.restore_printer_online_status(self.p)
            if self.printers.verify_sign_in_dialog_show(raise_e=False):
                    self.printers.select_pin_cancel_btn()
            for _ in range(11):
                self.printers.select_pin_dialog_submit_btn()
            self.printers.verify_incorrect_pin_enter_dialog_show()
            self.printers.click_ok_btn()
            self.printers.verify_pin_dialog()
            self.printers.input_pin(self.pin_num)
            self.printers.select_pin_dialog_submit_btn()
            self.moobe.verify_connected_printing_services_screen()
        else:
            logging.info("The printer PIN is not available, can not do this test")

    def test_03_clear_env(self):
        self.p.fake_action_door_close()

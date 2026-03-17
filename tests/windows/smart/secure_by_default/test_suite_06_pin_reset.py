import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import logging
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_06_pin_reset(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
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

    def test_02_check_pin_prompt_dialog_with_dsp_flow(self):
        """
        Add the test secure printer to main UI.
        Go to About screen or legacy Supply Status screen.
        Ctrl + Shift + right click on About screen or on top of the Legacy Status screen.
        Enter data in 41-45 text boxes on "Reset device region" screen.
        Click "Reset Device" button.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950659
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950661
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950662
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950663
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950667
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950668
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950669
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950671
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950672
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950673
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950674
        """
        sleep(3)
        self.fc.select_a_printer(self.p)
        self.p.fake_action_door_open()
        self.home.go_to_reset_device_screen()
        sleep(5)
        self.home.enter_reset_code("11111111111111111111")
        self.home.click_reset_device_btn()
        if self.printers.verify_pin_dialog(raise_e=False):
            self.printers.verify_pin_dialog()
            self.printers.verify_pin_dialog_submit_btn_not_enabled()
            self.printers.select_pin_cancel_btn()
            self.home.verify_exception_msg_dialog()
            self.home.click_exception_msg_dialog_ok_btn()
            self.home.click_reset_device_btn()
            self.printers.input_pin("11111111")
            self.printers.select_pin_dialog_submit_btn()
            self.printers.verify_incorrect_pin_dialog_show()
            self.printers.select_pin_cancel_btn()
            self.home.verify_exception_msg_dialog()
            self.home.click_exception_msg_dialog_ok_btn()
            self.home.click_reset_device_btn()
            self.printers.verify_pin_dialog()
            try:
                self.fc.trigger_printer_offline_status(self.p)
                self.printers.input_pin(self.pin_num)
                self.printers.select_pin_dialog_submit_btn()
                self.printers.verify_network_error_pin_dialog_show()
                self.printers.select_pin_cancel_btn()
                self.home.verify_exception_msg_dialog()
                self.home.click_exception_msg_dialog_ok_btn()
            finally:
                self.fc.restore_printer_online_status(self.p)
            if self.printers.verify_sign_in_dialog_show(raise_e=False):
                    self.printers.select_pin_cancel_btn()
            self.home.click_reset_device_btn()
            self.printers.input_pin("11111111")
            for _ in range(11):
                self.printers.select_pin_dialog_submit_btn()
            self.printers.verify_incorrect_pin_enter_dialog_show()
            self.printers.click_ok_btn()
            self.home.verify_exception_msg_dialog()
            self.home.click_exception_msg_dialog_ok_btn()
            # self.home.click_reset_device_btn()
            # self.printers.verify_pin_dialog()
            # self.printers.input_pin(self.pin_num)
            # self.printers.select_pin_dialog_submit_btn()
        else:
            self.p.fake_action_door_close()
            pytest.skip("The printer PIN is not available, can not do this test")

    def test_03_clear_env(self):
        self.p.fake_action_door_close()
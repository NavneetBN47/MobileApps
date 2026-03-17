import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import logging
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_01_pin_and_push_2n_oobe(object):
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

    def test_01_printer_oobe_reset(self):
        """
        Precondition: 
        *1 Clear printer data in Cloud 
        *2 Do an OOBE reset for printer
        *3 Connect printer wifi
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Stack Reset for printer...")
        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")
        self.p.exit_oobe()
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)

    def test_02_check_push_dialog(self):
        """
        Verify push button modal shows 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25437420
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26975703
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26975704
        """
        self.fc.go_home()
        self.home.click_carousel_add_printer_btn()
        self.printers.verify_device_picker_screen()
        printer = self.printers.search_printer(self.printer_ip_address)
        printer.click()
        self.moobe.verify_connected_printing_services_screen()
        self.moobe.select_accept_all_btn()
        self.moobe.verify_touch_checkmark_dialog(timeout=20)
        self.p.click_front_panel_btn("fb_cancel")
        self.moobe.verify_touch_checkmark_dialog()
        self.p.click_front_panel_btn("fb_allow")
        self.printers.verify_exit_setup_btn(timeout=20)
        self.printers.select_exit_setup()
        self.printers.select_pop_up_exit_setup()
        if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
            self.printers.select_pop_up_exit_setup()
        if self.printers.verify_install_success_dialog(raise_e=False):
            self.printers.click_install_success_dialog_continue_btn()
        self.home.verify_home_screen()
        #create pin dialog
        self.fc.web_password_credential_delete()
        self.home.right_click_printer_carousel()
        self.home.verify_hide_printer_list_item_load()
        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load()
        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        assert self.home.verify_carousel_printer_image(raise_e=False) is False

    def test_03_check_pin_prompt_dialog_with_2n_flow(self):
        """
        Go to Device Picker
        Select a network printer from the device picker
        Continue 2-N flow
        Verify "Find the printer PIN" dialog shows during the flow.
        Click the "Cancel" button on the "Find the printer PIN" dialog
        Enter incorrect pin on "Find the printer PIN" dialog when it shows.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24612802 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615690(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24612804
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24612805
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24612806
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24631907((low))
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615689
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615685
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615686
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615687(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615692
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24628881(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615693
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24612803
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24615688
                  No Beaconing Setup
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641204
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641205
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641206
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641207
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641208
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641212
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641213
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641214
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641215
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641216
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641217
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641218
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24641219
        """
        self.p.fake_action_door_open()
        self.home.click_carousel_add_printer_btn()
        self.printers.verify_device_picker_screen()
        printer = self.printers.search_printer(self.printer_ip_address)
        printer.click()
        if self.home.verify_home_screen(raise_e=False) is False:
            if self.printers.verify_pin_dialog(raise_e=False):
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
                self.printers.input_pin("11111111")
                for _ in range(11):
                    self.printers.select_pin_dialog_submit_btn()
                self.printers.verify_incorrect_pin_enter_dialog_show()
                self.printers.click_ok_btn()
                self.printers.verify_pin_dialog()
                self.printers.input_pin("11111111")
                self.printers.select_pin_dialog_submit_btn()
                self.printers.verify_incorrect_pin_dialog_show()
                self.driver.terminate_app()
                sleep(3)
                self.driver.launch_app()
                self.home.verify_home_screen()
                self.home.right_click_printer_carousel()
                self.home.click_hide_printer_list_item()
                self.home.click_hide_this_printer_dialog_hide_printer_btn()
                self.home.click_carousel_add_printer_btn()
                self.printers.verify_device_picker_screen()
                printer = self.printers.search_printer(self.printer_ip_address)
                printer.click()
                self.printers.verify_pin_dialog()
                if self.printers.input_pin(self.pin_num):
                    self.printers.select_pin_dialog_submit_btn()

                if self.printers.verify_printer_setup_webpage(raise_e=False):
                    self.printers.select_printer_setup_accept_all_btn()

                if self.printers.verify_exit_setup_btn(raise_e=False):
                    self.printers.select_exit_setup()
                self.printers.select_pop_up_exit_setup()
                if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
                    self.printers.select_pop_up_exit_setup()

                self.home.verify_home_screen()
                
                
            else:
                self.p.fake_action_door_close()
                pytest.skip("The printer PIN is not available, can not do this test")

    def test_03_clear_env(self):
        self.p.fake_action_door_close()

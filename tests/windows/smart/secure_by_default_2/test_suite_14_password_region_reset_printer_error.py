import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_13_password_region_reset(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.ews = cls.fc.fd["ews"]
        cls.printer_ip_address = cls.p.p_obj.ipAddress
        cls.setup_pw = "12345678"
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.stack = request.config.getoption("--stack")
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        cls.pin_num = cls.p.get_pin()
        if "DunePrinterInfo" in str(cls.p.p_obj):
            pytest.skip("Skip this test as Dune Printer can not door open")
   
   
    def test_01_go_to_ews_screen(self):
        """
        Go to Printer Settings
        Select "Advanced Settings" (EWS)
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item() 
        self.ews.verify_advanced_settings_page(self.p)

    def test_02_setup_ews_password_protected(self):
        """
        Setup password if the printer has no one.
        """
        if not self.ews.verify_ews_sign_in_link(raise_e=False):
            if self.ews.verify_ews_login_state(raise_e=False):
                self.ews.click_sign_out_link()
                self.ews.verify_sign_out_successfuly_text()
                self.ews.click_ok_btn()
            self.ews.make_ews_to_password_modal(self.setup_pw)

    def test_03_check_pin_prompt_dialog_with_dsp_flow_with_printer_error(self):
        """
        Add the test secure printer to main UI.
        Go to About screen or legacy Supply Status screen.
        Ctrl + Shift + right click on About screen or on top of the Legacy Status screen.
        Enter data in 41-45 text boxes on "Reset device region" screen.
        Generate any printer error (eg: Door open/ ink missing/ out of paper/...).
        Click "Reset Device" button.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950653
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.go_to_reset_device_screen()
        sleep(5)
        self.home.enter_reset_code("11111111111111111111")
        self.p.fake_action_door_open()
        self.home.click_reset_device_btn()
        self.printers.verify_sign_in_dialog_show()
        self.printers.verify_pin_dialog_submit_btn_not_enabled()
        self.printers.select_pin_cancel_btn()
        assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False
        self.home.verify_exception_msg_dialog()
        self.home.click_exception_msg_dialog_ok_btn()
       
    def test_04_remove_ews_password_protected(self):
        """
        remove ews password protected and Restore printer status
        """
        self.p.fake_action_door_close()
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        self.ews.remove_ews_password_modal(self.p.get_pin())
        self.home.select_navbar_back_btn()

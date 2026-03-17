import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.webdriver.common.keys import Keys
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_11_password_printer_info(object):
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
            pytest.skip("Skip this test as Dune Printer")
   
   
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

    def test_03_pw_prompt_dialog_with_change_country_language(self):
        """
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581534
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/17451820
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581950
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581951
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581954
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581955
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581956
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        language_1 = self.printer_settings.get_country_region_text()
        self.__change_printer_country_region()
        self.printers.verify_sign_in_dialog_show()
        self.printers.verify_pin_dialog_submit_btn_not_enabled()
        self.printers.select_pin_cancel_btn()
        assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False
        assert self.printer_settings.get_country_region_text() == language_1
        self.__change_printer_country_region()
        self.printers.verify_sign_in_dialog_show()
        self.printers.input_pin("11111111")
        self.printers.select_pin_dialog_submit_btn()
        self.printers.verify_incorrect_pw_dialog_show()
        #check pw prompt dialog with Turn off printer
        self.fc.trigger_printer_offline_status(self.p)
        self.printers.input_pin(self.setup_pw)
        self.printers.select_pin_dialog_submit_btn()
        self.printers.verify_network_error_pin_dialog_show()
        self.printers.select_pin_cancel_btn()
        assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False
        assert self.printer_settings.get_country_region_text() == language_1
        self.__change_printer_country_region()
        assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False

    def test_04_pw_prompt_dialog_with_change_country_language(self):
        """
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/24581949(high)
        """
        self.fc.restore_printer_online_status(self.p)
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        language_2 = self.printer_settings.get_country_region_text()
        self.__change_printer_country_region()
        self.printers.verify_sign_in_dialog_show()
        self.printers.input_pin(self.setup_pw)
        self.printers.select_pin_dialog_submit_btn()
        assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False
        assert self.printer_settings.get_country_region_text() != language_2

    def test_05_restore_language(self):
        self.fc.restart_hp_smart()
        self.fc.restore_printer_info_country_language(self.pin_num)

    def test_06_remove_ews_password_protected(self):
        """
        remove ews password protected
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=60)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_advanced_settings_page(self.p)
        self.ews.remove_ews_password_modal(self.p.get_pin())
        self.home.select_navbar_back_btn()


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

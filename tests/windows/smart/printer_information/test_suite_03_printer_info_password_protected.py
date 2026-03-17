import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_03_Printer_Info_Password_Protected(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.host_name = cls.p.get_printer_information()["host name"]
        cls.model_name = cls.p.get_printer_information()["model name"].strip()
        if 'HP' not in cls.model_name:
            cls.model_name = 'HP ' + cls.model_name
        cls.serial_number = cls.p.get_printer_information()["serial number"].strip()
        cls.firmware_version = cls.p.get_printer_information()["firmware version"].strip()
        cls.service_id = cls.p.get_printer_information()["service id"].strip()
        
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

    @pytest.fixture()
    def restore_printer_info(self, request):
        def restore():
            self.fc.restart_hp_smart()
            self.fc.restore_printer_info_country_language(self.p.get_pin())
        request.addfinalizer(restore)

    def test_01_add_a_printer(self):
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        
    def test_02_check_country_incorrect_password(self):
        """
        Click on "Country" or "Language" dropdown and select a different value to open the "Set Country" or "Set Language" dialog.
        Click "Save" button to open "Sign in to..." dialog.
        Enter Incorrect Username/Password then click Continue.

        Verify the "Sign in to..." dialog does not dismiss and it shows error message and will not continue.
        Verify the country and language settings are enabled.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078923
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078918
        https://hp-testrail.external.hp.com/index.php?/cases/view/24628915
        """
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())
        self.printer_settings.verify_preference_country_part()
        select_item = self.printer_settings.get_country_region_text()
        self.printer_settings.click_country_dropdown()
        el = self.printer_settings.verify_country_select_item(select_item)
        el.send_keys(Keys.UP, Keys.ENTER)
        self.printer_settings.verify_set_country_or_language_dialog()
        self.printer_settings.click_set_save_btn()
        if self.printer_settings.verify_sign_in_to_dialog(raise_e=False):
            self.printer_settings.edit_sign_in_password('11111111')
            self.printer_settings.click_sign_in_submit_btn()
            self.printer_settings.verify_sign_in_to_dialog()
            self.printer_settings.verify_invalid_pin_code_text()
            self.printer_settings.click_sign_in_cancel_btn()
            assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False
        
    def test_03_check_language_incorrect_password(self):
        self.printer_settings.verify_preference_language_part()
        select_item = self.printer_settings.get_language_text()
        self.printer_settings.click_language_dropdown()
        el = self.printer_settings.verify_language_select_item(select_item)
        el.send_keys(Keys.DOWN, Keys.ENTER)
        self.printer_settings.verify_set_country_or_language_dialog()
        self.printer_settings.click_set_save_btn()
        if self.printer_settings.verify_sign_in_to_dialog(raise_e=False):
            self.printer_settings.edit_sign_in_password('11111111')
            self.printer_settings.click_sign_in_submit_btn()
            self.printer_settings.verify_sign_in_to_dialog()
            self.printer_settings.verify_invalid_pin_code_text()
            self.printer_settings.click_sign_in_cancel_btn()
            assert self.printer_settings.verify_sign_in_to_dialog(raise_e=False) is False

    def test_04_change_language_first(self):
        """
        Click on "Country" or "Language" dropdown and select a different value to open the "Set Country" or "Set Language" dialog.
        Click "Save" button and check.

        Verify "Sign in to [printer name]" modal pops up.
        Verify the "Sign in to [printer name]" modal is dismissed and settings is saved

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078919
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078920
        """
        select_item = self.printer_settings.get_language_text()
        self.printer_settings.click_language_dropdown()
        el = self.printer_settings.verify_language_select_item(select_item)
        el.send_keys(Keys.DOWN, Keys.ENTER)
        self.printer_settings.verify_set_country_or_language_dialog()
        self.printer_settings.click_set_save_btn()
        if self.printer_settings.verify_sign_in_to_dialog(raise_e=False):
            self.printer_settings.edit_sign_in_password(self.p.get_pin())
            self.printer_settings.click_sign_in_submit_btn()
            assert self.printer_settings.verify_language_select_item(select_item, raise_e=False) is False
    
    def test_05_change_language_second(self, restore_printer_info):
        """
        Click on "Country" or "Language" dropdown and select a different value to open the "Set Country" or "Set Language" dialog.
        Click "Save" button and check.

        Verify the "Sign in to..." dialog is no longer displayed and the settings saved successfully.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078921
        """
        select_item = self.printer_settings.get_language_text()
        self.printer_settings.click_language_dropdown()
        el = self.printer_settings.verify_language_select_item(select_item)
        el.send_keys(Keys.DOWN, Keys.ENTER)
        self.printer_settings.verify_set_country_or_language_dialog()
        self.printer_settings.click_set_save_btn()
        assert self.printer_settings.verify_language_select_item(select_item, raise_e=False) is False

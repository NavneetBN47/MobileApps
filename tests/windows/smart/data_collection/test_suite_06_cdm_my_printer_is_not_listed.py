import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_06_Cdm_My_Printer_Is_Not_Listed(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, check_bluetooth_network):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]
        cls.printers = cls.fc.fd["printers"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

    def test_01_generate_turn_on_screen(self):
        """
        Click "My Printer isn't listed" button on the Device Picker
        Generate "Turn on Bluetooth or Wi-Fi screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/36047323
        https://hp-testrail.external.hp.com/index.php?/cases/view/36047333
        """ 
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.driver.ssh.send_command("netsh wlan disconnect")
        sleep(2)
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_turn_on_ble_or_wifi_screen()

    def test_03_enable_wifi_and_click_continue_button(self):
        """
        enable one type of settings and click "Continue" button on the Bluetooth or Wi-Fi screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/36047337
        """ 
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        sleep(2)
        self.printers.click_continue_btn(check_kibana=True)
        self.printers.verify_device_picker_screen()

    def test_04_disable_wifi_and_click_continue_button(self):
        """
        Click "Continue" button on the Bluetooth or Wi-Fi screen without enabling any network,

        https://hp-testrail.external.hp.com/index.php?/cases/view/36047339
        """
        self.driver.ssh.send_command("netsh wlan disconnect")
        sleep(2)
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_turn_on_ble_or_wifi_screen()
        self.printers.click_continue_btn(check_kibana=True)
        self.printers.verify_turn_on_ble_or_wifi_dialog()
        
    def test_05_click_no_bluetooth_or_wifi_button(self):
        """
        Click "No Bluetooth or Wi-Fi" button on the "Turn on Bluetooth or Wi-Fi" model

        https://hp-testrail.external.hp.com/index.php?/cases/view/36047340
        """
        self.printers.click_no_bluetooth_or_wifi_btn()
        self.printers.verify_what_type_of_printer_screen(wifi_connect=False)

    def test_05_click_try_button(self):
        """
        Click "Try" button on the "Turn on Bluetooth or Wi-Fi" model

        https://hp-testrail.external.hp.com/index.php?/cases/view/36047341
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.printers.verify_device_picker_screen()
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_turn_on_ble_or_wifi_screen()
        self.printers.click_continue_btn(check_kibana=True)
        self.printers.verify_turn_on_ble_or_wifi_dialog()
        self.printers.click_try_again_btn()
        self.printers.verify_turn_on_ble_or_wifi_dialog()
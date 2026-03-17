import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"

class Test_Suite_09_OOBE_No_beaconing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

    def test_01_click_setup_mode_printer_on_connection_choice_screen(self):
        """
        Click on the Wi-Fi set up mode button
        "Let's find your new printer" appears
        Follow the page instruction and proceed through the flow
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28328351
        """
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_what_type_of_printer_screen() 
        self.printers.select_setup_mode_printer_btn()
        self.printers.verify_let_us_find_your_new_printer_screen()
        self.printers.select_search_again_btn()
        self.printers.verify_device_picker_screen()

    def test_02_click_network_printer_on_connection_choice_screen(self):
        """
        Click the "Network printer" button on the "Connection choice" screen
        omplete the flow
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28328348
        """
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_what_type_of_printer_screen()  
        self.printers.select_network_printer_btn()
        self.printers.verify_let_us_find_your_network_screen()  
        self.printers.select_search_again_btn()
        self.printers.verify_device_picker_screen()

    def test_03_click_usb_printer_on_connection_choice_screen(self):
        """
        Click on the USB printer button
        Let's find your USB printer" appears
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28328357
                   > https://hp-testrail.external.hp.com/index.php?/cases/view/28328349
        """
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_what_type_of_printer_screen()
        self.printers.select_usb_printer_btn()
        self.printers.verify_let_us_find_your_usb_printer_screen()
        self.printers.select_search_again_btn()
        self.printers.verify_device_picker_screen()

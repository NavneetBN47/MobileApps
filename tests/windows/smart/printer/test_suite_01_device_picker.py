import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_01_Device_Picker(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_search_again_link(self):
        """
        Connect multi printer via USB/Network, verify information displays in Device Picker
        Verify device picker list gets refreshed after clicking search again link.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12494942
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29870253
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12494940
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13258918
        """
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_search_again_link()

        # There's no search box while refreshing.
        assert self.printers.verify_search_box(raise_e=False, timeout=3) is False

        self.printers.verify_device_picker_screen()

    def test_02_search_by_hostname(self):
        """
        Input a hostname of a on-subnet printer in search box, verify printer is found.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13251413
        """
        self.printers.search_printer(self.hostname)

    def test_03_search_by_invalid_hostname_or_ip(self):
        """
        Input invalid IP or hostname in search box, verify no printer is found

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12577950
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16942924
        """
        self.printers.select_search_again_link()
        self.printers.verify_device_picker_screen()
        self.printers.search_printer(w_const.TEST_TEXT.INVALID_IP, value=False)
        self.printers.verify_warning_message_display(w_const.TEST_TEXT.WARNING_MSG_VALUE, w_const.TEST_TEXT.INVALID_IP)
        self.printers.select_search_again_link()
        self.printers.verify_device_picker_screen()
        self.printers.search_printer(w_const.TEST_TEXT.TEST_TEXT_00, value=False)
        self.printers.verify_warning_message_display(w_const.TEST_TEXT.WARNING_MSG_VALUE, w_const.TEST_TEXT.INVALID_IP)
        self.home.select_navbar_back_btn()

    def test_04_search_by_ip(self):
        """
        Input an IP of a on-subnet printer in search box, verify printer can be found.
        Add USB/Network connected printer to carousel, verify it shows on DP
        Add USB/Network connected printer to carousel, verify the printer can be found in DP after searching the IP address of the printer 
        Add USB/Network connected printer to carousel, verify the printer can be found in DP after searching the name of the printer 
        Add USB/Network connected printer to carousel (OOBE not complete), verify the flow goes to OWS after selecting the printer from DP
        Add USB/Network connected printer to carousel (OOBE is complete), verify the flow goes to main UI after selecting the printer from DP 
        Select USB/Network printer from DP that is already added in carousel, verify no other printer instances are added to carouse 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13251414 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29718806
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550560
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550561
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550562
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550563
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550564
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550565

        """
        printer_ip = self.fc.select_a_printer(self.p)

        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.check_network_printer_show(printer_ip)
        self.printers.search_printer(printer_ip)
        printer = self.printers.search_printer(self.hostname)
        printer.click()
        if self.p.is_oobe_mode():
            self.fc.enter_printer_pin_number(self.p.get_pin())
            if self.printers.verify_printer_setup_webpage(raise_e=False):
                self.printers.select_printer_setup_accept_all_btn()
            elif self.printers.verify_exit_setup_btn(raise_e=False):
                self.printers.select_exit_setup()
                self.printers.select_pop_up_exit_setup()
                if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
                    self.printers.select_pop_up_exit_setup()
                if self.printers.verify_install_success_dialog(raise_e=False):
                    self.printers.click_install_success_dialog_continue_btn()
        else:
            self.home.verify_home_screen()

        self.home.verify_carousel_printer_image()
        assert self.home.verify_pagination_text(raise_e=False) is False


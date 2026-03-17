import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_01_Entry_Link_Ethernet(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, clear_printer_data, check_bluetooth_network):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.p = load_printers_session
        
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.print = cls.fc.fd["print"]

        cls.printer_ows_type = cls.p.get_printer_information()['firmware version'][:3]

        cls.stack = request.config.getoption("--stack")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"

    def test_01_printer_oobe_reset(self):
        """
        Precondition: 
        *1 Clear printer data in Cloud 
        *2 Do an OOBE reset for printer
        *3 Connect printer wifi
        *4 Change printer stack to the one that app is
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Stack Reset for printer...")
        self.p.exit_oobe()
        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")
        self.p.connect_to_wifi(self.ssid, self.password)

    def test_02_go_through_turn_on_buletooth_or_wifi_flow(self):
        """
        Click big "+" on the Main UI.
        Click "My printer isn't listed " link on the Device picker screen.
        Follow and finish the flow with the testing printer.
        
        Verify Gotham app directs to OOBE flow where a user can install the not discovered printer in Device Picker via USB/Ethernet/Wireless.
        Verify setup is successful.
        Verify printer is added to main UI after flow completed.
        "Turn on Bluetooth or Wi-Fi" screen UI - (DP Phase 2)
        "Turn on Bluetooth or Wi-Fi" modal screen UI - (DP Phase 2)
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/12797861
        https://hp-testrail.external.hp.com/index.php?/cases/view/29870952
        https://hp-testrail.external.hp.com/index.php?/cases/view/29870959
        https://hp-testrail.external.hp.com/index.php?/cases/view/12612365
        """
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.driver.ssh.send_command("netsh wlan disconnect")
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_turn_on_ble_or_wifi_screen()
        self.printers.click_continue_btn()
        self.printers.verify_turn_on_ble_or_wifi_dialog()
        self.printers.click_no_bluetooth_or_wifi_btn()
        self.printers.verify_what_type_of_printer_screen(wifi_connect=False)
        
    def test_03_check_let_us_find_your_network_screen(self):
        """
        The computer is connected to a network via Ethernet
        BT/WiFi adapter is not present
        Start OOBE flow from "Turn on Bluetooth or Wi-Fi" screen
        Check all strings for the screen

        Check UI layout, form and fit against the attached screen shot.
        Re-size app to check UI form and fit.
        Click on 'I' buttons verify layout
        Verify strings are translated correctly and matching string table
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/29884894
        https://hp-testrail.external.hp.com/index.php?/cases/view/33357059
        """
        self.printers.select_network_i_icon()
        self.printers.verify_check_for_network_connection_dialog()
        self.printers.click_ok_btn()
        assert self.printers.verify_check_for_network_connection_dialog(raise_e=False) is False
        self.printers.select_network_printer_btn()
        self.printers.verify_let_us_find_your_network_screen()

    def test_04_check_buttons_in_dialog(self):
        """
        Click on the "Exit Setup" link on this screen for Win
        Click the Back on this screen (Win)

        Verify "Back" button dismisses the dialog.
        Verify "Exit Setup" button exit the OOBE flow to main UI with no printer on card added (if the printer is not connected via Ethernet cable yet), and with printer added if printer is connected via Ethernet cable.

        https://hp-testrail.external.hp.com/index.php?/cases/view/12797957
        https://hp-testrail.external.hp.com/index.php?/cases/view/33321131
        """
        self.printers.select_exit_setup()
        self.printers.verify_printer_setup_is_incomplete_dialog_1()
        self.printers.select_popup_back_btn()
        assert self.printers.verify_printer_setup_is_incomplete_dialog_1(raise_e=False) is False
        self.printers.select_exit_setup()
        self.printers.verify_printer_setup_is_incomplete_dialog_1()
        self.printers.select_exit_setup_btn_on_dialog()
        self.home.verify_setup_or_add_printer_card()

    def test_05_click_search_again_button(self):
        """
        Click the "Search Again button on this screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/12797545
        """
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_turn_on_ble_or_wifi_screen()
        self.printers.click_continue_btn()
        self.printers.verify_turn_on_ble_or_wifi_dialog()
        self.printers.click_no_bluetooth_or_wifi_btn()
        self.printers.verify_what_type_of_printer_screen(wifi_connect=False)
        self.printers.select_network_printer_btn()
        self.printers.verify_let_us_find_your_network_screen()
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        sleep(2)
        self.printers.select_search_again_btn()
        self.printers.verify_device_picker_screen()

    def test_06_selcect_a_printer_to_finish_ows_flow(self):
        """
        Select the test printer from Device Picker.
        OWS flow starts and then "Let's print" screen shows
        """
        self.fc.search_network_printer(self.p)
        self.ows_flow.go_through_ows_flow(self.printer_ows_type, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()

    def test_07_print_photos_flow(self):
        """
        Send a print job to the printer

        Verify the flow
        Verify printer is added to main UI after the flow
        Verify print is successful.

        https://hp-testrail.external.hp.com/index.php?/cases/view/19526490
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()

        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.print.verify_simple_print_dialog()

        hostname = self.p.get_printer_information()["host name"]
        self.print.select_printer(hostname)
        
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    

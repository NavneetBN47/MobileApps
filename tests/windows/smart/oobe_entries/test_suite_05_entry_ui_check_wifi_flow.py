import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "GOTHAM"
class Test_Suite_05_Entry_Ui_Check_Wifi_flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        # Initializing Printer1
        cls.p = load_printers_session
        # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.p2.set_mech_mode(mech=False)
        
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        
        cls.stack = request.config.getoption("--stack")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"

    def test_01_printer_oobe_reset(self):
        """
        Precondition: 
        Do an OOBE reset for printer
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer_1 = self.p.oobe_reset_printer()
        oobe_reset_printer_2 = self.p2.oobe_reset_printer()
        if not oobe_reset_printer_1 or not oobe_reset_printer_2:
            raise Exception("Printer OOBE reset failed")
        logging.info("Stack Reset for printer...")
        self.p.exit_oobe()
        self.p2.exit_oobe()
    
    def test_01_go_through_choose_a_printer_to_set_up_flow(self):
        """
        Click the "Set up a new printer" button on the UCDE value prop.

        Verify Device picker is launched after clicking the "Set up a new printer" button
        """
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_choose_a_printer_to_set_up_screen()
        self.printers.click_refresh_link()
        self.printers.verify_choose_a_printer_to_set_up_screen()

    def test_02_check_what_type_of_printer_screen(self):
        """
        Click on 'I' buttons verify layout
        Check all strings for the screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/29884892
        """
        self.printers.click_printer_not_listed_link()
        self.printers.verify_what_type_of_printer_screen()
        self.printers.select_wifi_mode_i_icon()
        self.printers.verify_check_for_wifi_setup_mode_dialog()
        self.printers.click_ok_btn()
        assert self.printers.verify_check_for_wifi_setup_mode_dialog(raise_e=False) is False
        self.printers.select_network_i_icon()
        self.printers.verify_check_for_network_connection_dialog()
        self.printers.click_ok_btn()
        assert self.printers.verify_check_for_network_connection_dialog(raise_e=False) is False

    def test_03_check_let_us_find_your_new_printer_screen(self):
        """
        Click on the Wi-Fi set up mode button
        "Let's find your new printer" appears

        Check all strings for the screen
        Verify "HP Support website" link shows in the description and opens to
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/29884896
        """
        self.printers.select_setup_mode_printer_btn()
        self.printers.verify_let_us_find_your_new_printer_screen()
        self.printers.click_hp_support_website_link()
        self.web_driver.add_window("hp_support")
        sleep(3)
        self.web_driver.switch_window("hp_support")
        sleep(3)
        current_url = self.web_driver.get_current_url()
        assert 'support.hp.com' in current_url
        self.web_driver.close_window("hp_support")

    def test_04_check_let_us_find_your_usb_printer_screen(self):
        """
        Click on the USB printer button
        "Let's find your USB printer" appears

        Check all strings for the screen
        Click on "Show me how" validate UI and all the strings
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/29884897
        https://hp-testrail.external.hp.com/index.php?/cases/view/27176694
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.printers.select_usb_printer_btn()
        self.printers.verify_let_us_find_your_usb_printer_screen()
        self.printers.click_show_me_how_link(index=1)
        self.printers.verify_check_for_windows_update_screen()
        self.printers.click_x_button_to_close_dialog()

        self.printers.click_show_me_how_link(index=2)
        self.printers.verify_check_the_status_of_screen()
        self.printers.click_x_button_to_close_dialog()

        self.printers.click_show_me_how_link(index=3)
        self.printers.verify_connect_using_usb_screen()
        self.printers.click_x_button_to_close_dialog()

    def test_05_check_let_us_find_your_network_connected_printer_screen(self):
        """
        Click on the Network printer button
        "Let's find your network connected printer" appears

        Check all strings for the screen
        Click on "Show me how" validate UI and all the strings
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/29884898
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.printers.select_network_printer_btn()
        self.printers.verify_let_us_find_your_network_screen()
        self.printers.click_show_me_how_link()
        self.printers.verify_connect_printer_to_router_screen()
        self.printers.click_x_button_to_close_dialog()

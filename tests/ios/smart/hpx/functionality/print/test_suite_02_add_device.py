import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_Add_Device:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.printers = cls.fc.fd["printers"]
        cls.fc.hpx = True

    def test_01_verify_set_up_new_printer_option_C66289887(self):
        """
        Description: C66289887
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Set up a new printer' option on Add Device screen
                5. Observe the screen
            Expected Result:
                5.  Verify that the user is taken to existing new printer setup flow.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.click_set_up_new_printer_option()
        self.printers.verify_connect_this_printer_option()

    def test_02_verify_choose_an_available_printer_option_C66289888(self):
        """
        Description: C66289888
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Choose an available printer' option on Add Device screen
                5. Observe the screen
            Expected Result:
                5.  Verify that the user is taken to existing new printer setup flow.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.select_add_printer_btn()
        self.printers.verify_printers_nav()

    def test_03_verify_search_by_serial_printer_option_C66289889(self):
        """
        Description: C66289889
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Choose an available printer' option on Add Device screen
                5. Observe
                6. Tap on Back arrow button.
                7. Observe
            Expected Result:
                5. Verify the user is navigated to 'Search by serial number' screen.
                7. Verify back button from search by serial number screen should navigate back to add device screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.click_search_by_serial_number_option()
        self.printers.verify_search_by_serial_number_screen()

    def test_04_verify_close_button_add_printer_screen_C66289890(self):
        """
        Description: C66289890
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Close' button on Add Device screen
                5. Observe
            Expected Result:
                5. Verify the Add a device screen is closed and user is taken back to rootview.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.home.close_print_anywhere_pop_up()
        self.home.verify_hpx_home()

    def test_05_verify_search_by_serial_number_screen_ui(self):
        """
        Description: C56537453
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Search by serial number' option on Add Device screen
                5. Observe
            Expected Result:
                5. Verify the 'Search by serial number' screen UI is as per figma.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.click_search_by_serial_number_option()
        self.printers.verify_search_by_serial_number_screen()
        self.printers.verify_help_link_for_search_by_serial_number_screen()

    def test_06_click_help_link_screen_for_serial_number_screen_ui(self):
        """
        Description: C56537458
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Search by serial number' option on Add Device screen
                5. Tap on the link 'Need help finding your serial number?'
                6. Observe
            Expected Result:
                6. Verify the user is navigated to https://support.hp.come/us-en/document/ish2039298-1862169-16
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.click_search_by_serial_number_option()
        self.printers.verify_search_by_serial_number_screen()
        self.printers.click_and_verify_help_link_for_search_by_serial_number_screen()

    def test_07_click_back_arrow_and_verify_add_device_screen(self):
        """
        Description: C56537457
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Search by serial number' option on Add Device screen
                5. Tap on 'Add a device' button on the top
                6. Observe
            Expected Result:
                6. Verify the user is taken back to "Add a device" screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.click_search_by_serial_number_option()
        self.printers.verify_search_by_serial_number_screen()
        self.printers.click_on_back_arrow_on_add_device_button()
        self.printers.verify_add_device_page()

    def test_08_verify_add_device_screen_ui_C66289808(self):
        """
        Description: C66289808
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Observe the Add Device UI
            Expected Result:
                6. Verify the "Add a device" screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.verify_add_device_page()
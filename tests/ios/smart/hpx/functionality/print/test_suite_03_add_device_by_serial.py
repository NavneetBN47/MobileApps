import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_03_Add_Device_By_Serial:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_num = cls.p.get_printer_information()["serial number"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.printers = cls.fc.fd["printers"]
        cls.fc.hpx = True

    def test_01_verify_add_printer_by_serial_num_C66289878(self):
        """
        Description: C66289878
                1. Install and launch app.
                2. Accept consents and navigate to rootview
                3. Tap '+' button on top bar
                4. Tap "Search by serial number' option on Add Device screen
                5. Enter serial number of the test printer in valid format and hit search
                6. Observe
            Expected Result:
                4. Verify the user is able to enter the serial number at the search bar
                6. Verify the search returned with a device corresponding to the serial number
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_printer_plus_button_from_topbar()
        self.printers.click_search_by_serial_number_option()
        self.printers.verify_search_by_serial_number_screen()
        self.printers.search_for_printer_using_serial_num(serialnum=self.p.get_printer_information()["serial number"])
        self.printers.verify_listed_printer_using_serial_num()

    def test_02_click_to_connect_printer_by_serial_num_C66289877(self):
        """
        Description: C66289877
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
        self.printers.search_for_printer_using_serial_num(serialnum=self.p.get_printer_information()["serial number"])
        self.printers.click_on_add_device_using_serial_num()
        self.home.verify_hpx_home()
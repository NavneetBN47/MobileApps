import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_Print:

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
        cls.photos = cls.fc.fd["photos"]
        cls.fc.hpx = True

    def test_01_add_printer(self):
        """
        Description: C52683913
                1. Launch MyHP App
                2. Click onPrinter Device section.
            Expected Result:
                2. Printer Device page should be displayed with proper device name.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])

    def test_02_print_tiles(self):
        """
        Description: 
                1. Launch MyHP App
                2. Click onPrinter Device section.
            Expected Result:
                2. Below Tiles should be displayed properly
                    Scan
                    Print photos
                    Print PDFs
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"]) 
        self.home.click_sign_btn_hpx()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.wait_for_object(i_const.HOME_TILES.TILE_SCAN)
        self.driver.wait_for_object(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        self.driver.swipe()
        self.driver.wait_for_object(i_const.HOME_TILES.TILE_PRINT_PHOTOS)

    def test_03_device_page_to_home(self):
        """
        Description: 
                1. Launch MyHP App
                2. Click onPrinter Device section.
                3. Click on Back button on the top left side
            Expected Result:
                3. App should be navigated back to Home screen
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.click_hpx_devices_btn()
        self.home.verify_hpx_home()
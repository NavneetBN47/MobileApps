import pytest
from MobileApps.libs.ma_misc import ma_misc
import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_05_Home_Carousel_Printer_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.stack = request.config.getoption("--stack")
        cls.db_info = cls.sys_config.get("database_info", None)
    
    @pytest.fixture(scope="function", autouse=True)
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)

    def test_01_printer_info(self):
        """
        IOS & MAC:
        Requirement:
            C31297438 - Verify Printer information from long tap on ONLINE PRINTER available on carousel.
        Preconditions:
            1.Clear Cache, Clear Storage *of the previous App from the Phone Settings
            2.Uninstall the previous App
            3.Fresh install the app/ upgrade to the latest version of HP Smart
            4.Launch the App
            5.Go to Home Screen
            6. Add online local/cloud printers to the Carousel in Home Screen            
        Steps:
            1.Add online local printers to the Carousel in Home Screen
            2.Launch the Smart App
            3.Login to the HPID account and proceed to home screen
            4.Long tap on the printer that displays in the card in the carousel
            5. You will see two options: "Forget This Printer" & "Printer Information"
            6.Tap on 'Printer Information'
        Expected results:
            1.Printer information are shown
        """
        if self.home.verify_finish_setup_warning(timeout=10, raise_e=False) or not self.home.verify_estimated_cartridge_levels(timeout=10, raise_e=False):
            pytest.skip(f"The printer {self.p.get_printer_information()['bonjour name']} has a problem and the test can not continue. Skipping...")
        self.home.verify_printer_dropdown_options()
        self.home.select_printer_information_from_menu()
        self.home.verify_printer_information_screen()

    def test_02_hide_printer(self):
        """
        IOS & MAC:
        Requirements:   
            C31297434 - Verify Long tap on ONLINE PRINTER for pop-up menu to Forget and My Printer Info
            C31297435 - Verify "FORGET THIS PRINTER" functionality.
        Preconditions:
            1.Clear Cache, Clear Storage *of the previous App from the Phone Settings
            2.Uninstall the previous App
            3.Fresh install the app/ upgrade to the latest version of HP Smart
            4.Launch the App
            5.Go to Home Screen
            6. Add online local/cloud printers to the Carousel in Home Screen     
        Steps:
            1.Add online local printers to the Carousel in Home Screen
            2.Launch the Smart App
            3.Login to the HPID account and proceed to home screen
        Expected result:
            1.On online printer, long tap
            2.tap on 'Hide This Printer'
            3.Tap on CANCEL
            4.Again long tap on printer
            5.tap on 'Hide This Printer'
            6.Tap on 'Hide'
        """
        self.home.verify_printer_dropdown_options()
        self.home.select_hide_printer_from_menu()
        self.home.verify_hide_printer_popup()
        self.home.select_forget_printer_cancel_btn()
        assert not self.home.verify_add_your_first_printer(raise_e=False)
        self.home.verify_printer_dropdown_options()
        self.home.select_hide_printer_from_menu()
        self.home.verify_hide_printer_popup()
        self.home.select_hide_printer_confirmation_btn()
        assert self.home.verify_add_printer_on_carousel()

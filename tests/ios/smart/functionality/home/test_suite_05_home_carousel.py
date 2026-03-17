import pytest
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.ma_misc import ma_misc
from SPL.driver.reg_printer import PrinterNotReady
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_05_Home_Carousel(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.supply_levels = cls.fc.fd["dedicated_supply_levels"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.stack = request.config.getoption("--stack")
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        if pytest.platform == "MAC":
            cls.mac_browser_popup_flow = cls.fc.fd["mac_browser_popup_flow"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_home(self):
        self.fc.go_home(reset=True, stack=self.stack)
      
    def test_01_empty_carousel(self):
        """
        IOS & MAC:
        Requirement:
            C38414681, C31297428 - Verify 'ADD YOUR FIRST PRINTER' card when there is no printer added to the carousel
            C31297429 - Verify Tap on "ADD YOUR FIRST PRINTER" from Carousel on the Home Screen.
        Preconditions:
            1.Clear Cache, Clear Storage *of the previous App from the Phone Settings
            2.Uninstall the previous App
            3.Fresh install the app/ upgrade to the latest version of HP Smart
            4.Launch the App
            5.Make sure there is no printer added to the carousel
        Script steps:
            1. Reach Home screen
            2. Verify "Add Your First Printer" card on the carousel
            3. Tap on "Add Your First Printer" 
            4. Verify if action was successfull
        """
        self.fc.dismiss_tap_here_to_start()
        self.home.verify_empty_carousel()
        assert self.home.verify_add_your_first_printer(raise_e=False), "'Add Your First Printer' Card is not present on HomeScreen"
        self.home.select_add_your_first_printer()
        self.printers.verify_printer_options_screen()
        
    def test_02_add_printer_to_carousel(self):
        """
        IOS & MAC:
        Requirement:
            C31297430 Verify "ADD YOUR FIRST PRINTER" allows to add a printer To the Carousel
            C31297447 - Verify Printer with LONG NAME in the Carousel
        Preconditions:
            1.Clear Cache, Clear Storage of the previous App from the Phone Settings
            2.Uninstall the previous App
            3.Fresh install the app/ upgrade to the latest version of HP Smart
            4.Launch the Smart app
            5.Accept GA consent
            6."Create your Hp Account" from the OU Value Prop Screen
            7.Accept App T&Cs consent
            8.Load Home screen
            9.Make sure there is no printer added to the carousel
        Steps:
            1.Tap on "Add Your First Printer" from Carousel
            2.The Printers List is displayed
            3.Select any available printer
        """
        self.fc.dismiss_tap_here_to_start()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        if self.home.verify_finish_setup_warning(timeout=5, raise_e=False) or not self.home.verify_estimated_cartridge_levels(timeout=5, raise_e=False):
            pytest.skip(f"The printer {self.printer_name} has a problem and the test can not continue. Skipping...")
        assert not self.home.verify_add_your_first_printer(raise_e=False)
        self.home.verify_loaded_printer(self.printer_name, raise_e=False)

    def test_03_tap_on_printer(self):
        """
        IOS & MAC:
        Requirement:
            C31297433 - Verify Options when Tap on Printer's icon For ONLINE PRINTERS in Carousel
            C31297439 - Verify behavior when Single tap on Left area of card view for ONLINE PRINTER
        Preconditions:
            1.Fresh Install or Upgrade the app to the latest version
            2.Launch the app
            3. Navigate to the Home Screen
        Steps:    	
            1.Add Targeted printer to the carousel
            2.Tap on Printer's icon (on the left-side of the card) in the Carousel
        """
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_on_printer_icon()
        self.printer_settings.verify_printer_settings_screen(raise_e=True)

    def test_05_verify_hp_smart_nav_bar(self):
        """
        IOS & MAC:
        Requirements:
            C31297445 - Verify '+' FROM NAVIGATION BAR on the Home Screen 
        Preconditions:
            1.Clear Cache, Clear Storage *of the previous App from the Phone Settings
            2.Uninstall the previous App
            3.Fresh install the app/ upgrade to the latest version of HP Smart
            4.Launch the App
        Steps:
            1.Navigate to Home screen
            2.Click on '+' from the Navigation Bar.
        """
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.verify_hp_smart_nav_bar()
        self.home.verify_add_printer_nav_bar()
        self.home.select_add_printer_nav_bar()
        self.printers.verify_printer_options_screen()
        
    def test_06_verify_homescreen_carousel_card(self):
        """
        Requirements:
            C31297432 - Verify Carousel Card for ONLINE PRINTER 
            C31297441 - Verify behavior when single tap on Right side (Ink section) of card view for ONLINE PRINTER
        Preconditions:
            1.Clear Cache, Clear Storage of the previous App from the Phone Settings
            2.Uninstall the previous App
            3.Fresh install the app/ upgrade to the latest version of HP Smart
            4.Launch the Smart app
            5.Accept GA consent
            6."Create your Hp Account" from the OU Value Prop Screen
            7.Accept App T&Cs consent
            8.Load Home screen
            9.Make sure there at least one printer added to the carousel
        Steps:
            1. Add printer if no printer is added.
            2. Verify printer icon
            3. Verify alert status icon
            4. Verify setimated cartridge levels
            5. Select estimated supply levels
        """
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.verify_printer_icon()
        if self.home.verify_finish_setup_warning(timeout=5, raise_e=False) or not self.home.verify_estimated_cartridge_levels(timeout=5, raise_e=False):
            pytest.skip(f"The printer {self.printer_name} has a problem and the test can not continue. Skipping...")
        self.home.verify_alert_status_icon(timeout=15)
        self.home.verify_alert_status_icon_text()
        assert self.home.verify_estimated_cartridge_levels(timeout=5)
        self.home.select_estimated_supply_levels()
        if pytest.platform == "IOS":
            if self.home.verify_your_privacy_title(raise_e=False):
                self.home.close_privacy_web_alert_dialog(timeout=20)
                assert self.home.verify_arrow_back_to_home()
            else:
                self.supply_levels.verify_hp_instant_ink_page()
        else:
            if not self.supply_levels.verify_try_instant_ink_free_link() or not self.supply_levels.verify_your_privacy_popup():
                self.fc.switch_window_and_modify_wn("mac_browser_popup_flow", "hp_ink_page", wait_for_new_window=False)
                assert self.mac_browser_popup_flow.verify_an_element_and_click("hp_ink_page_privacy_popup", raise_e=False) or\
                    self.mac_browser_popup_flow.verify_an_element_and_click("hp_ink_title", raise_e=False),\
                    "HP Instant Ink page didn't show up neither in the app nor in the browser."
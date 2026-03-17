"""
Home flow and functionality smoke test suite for iOS
"""
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import pytest

pytest.app_info = "SMART"


class Test_Suite_Smoke_02_Home:
    """
    Home flow class for smoke testing for iOS
    """
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.personalize = cls.fc.fd["personalize"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printers = cls.fc.fd["printers"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_home(self):
        """
        Verify navigation to home page after:
        1. App installation on the mobile device
        2. Clicking on Sign In on the ows screen and navigating to home page
        """
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_empty_carousel_home(self):
        """
        IOS & MAC:
        Requirement:
            C38414681, C31297428 - Verify 'ADD YOUR FIRST PRINTER' card when
            there is no printer added to the carousel
            C31297429 - Verify Tap on "ADD YOUR FIRST PRINTER" from Carousel on the Home Screen.
        Preconditions:
            1.Clear Cache, Clear Storage *of the previous App from the Phone Settings
            2.Uninstall the previous App
            3.Fresh install the app/ upgrade to the latest version of HP Smart
            4.Launch the App
            5.Make sure there is no printer added to the carousel
        Script steps:
            1.Reach Home screen
            2.Verify "Add Your First Printer" card on the carousel
            3.Tap on "Add Your First Printer"
            4.Verify if action was successfull
        """
        self.fc.dismiss_tap_here_to_start()
        self.home.verify_empty_carousel()
        self.home.verify_add_your_first_printer(raise_e=False)
        self.home.select_add_your_first_printer()
        self.printers.verify_printer_options_screen()

    def test_02_tap_on_printer_icon(self):
        """
        IOS & MAC:
        Requirement:
            C31297433 - Verify Options when Tap on Printer's icon For ONLINE PRINTERS in Carousel
            C31297439 - Verify behavior when Single tap on Left area of card view for ONLINE PRINTER
        Preconditions:
            1.Fresh Install or Upgrade the app to the latest version
            2.Launch the app
            3.Navigate to the Home Screen
        Steps:
            1.Add Targeted printer to the carousel
            2.Tap on Printer's icon (on the left-side of the card) in the Carousel
        """
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(
                printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_on_printer_icon()
        self.printer_settings.verify_printer_settings_screen(raise_e=True)

    def test_03_verify_notification_bell_icon_and_hp_smart_title(self):
        """
        Verify Notification bell is present on the home page navigation bar
        """
        self.home.verify_hp_smart_nav_bar()
        self.home.verify_notification_bell()

    def test_04_verify_personalize_tile_btn(self):
        """
        TESTRAIL: IOS & MAC
        C31297057, C31298227 - Verify Personalize Tiles screen
        """
        self.home.select_personalize_btn()
        self.personalize.verify_personalize_screen()
        self.personalize.verify_personalize_tiles_and_switches()
        self.personalize.select_done()
        self.home.verify_home()

    def test_05_verify_all_tiles(self):
        """
        Verify all tiles are present on the home page:
        1. Get the count of the switches in the personalize screen
        2. Verify the count of the switches and the number of tiles present on home page are same
        """
        self.home.select_personalize_btn()
        self.personalize.verify_personalize_screen()
        self.personalize.toggle_all_tiles()
        tiles_on_personalize_screen = self.personalize.get_tile_names()
        if pytest.platform == "MAC":
            self.personalize.select_done()
        tiles_on_home_screen = self.home.get_all_tiles_titles()
        assert_text = "The number of tiles toggled on and tiles on the home screen is different"
        assert (len(set(tiles_on_personalize_screen)) ==
                len(set(tiles_on_home_screen))), assert_text

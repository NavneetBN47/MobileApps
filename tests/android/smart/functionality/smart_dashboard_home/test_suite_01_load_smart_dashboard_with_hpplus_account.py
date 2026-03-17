from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import *
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Load_Smart_Dashboard_With_Hpplus_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]
        cls.hp_connect_account = cls.fc.flow[FLOW_NAMES.HP_CONNECT_ACCOUNT]

        # Define the variable
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True, force_reset=True)

    def test_01_load_smart_dashboard_by_hp_plus_account_with_printer(self):
        """
        Description: C28340770, C28340773, C28340778
          1. Load to Home screen without user onboarding account
          2. Click on Account button on navigation bar of Home screen
          3. Click on Back button from mobile device

        Expected Result:
          2. Verify Smart Dashboard screen with HP+Member displays
          3. App should direct into Smart app home screen
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_smart_dashboard()
        self.driver.press_key_back()
        self.home.verify_home_nav(timeout=20)

    def test_02_close_button(self):
        """
        Description: C28340772
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Close button on Smart Dashboard screen

        Expected Result:
          2. App should direct into Smart app home screen
        """
        self.fc.flow_home_smart_dashboard()
        self.hp_connect.click_close_btn()
        self.home.verify_home_nav(timeout=20)

    def test_03_wireless_print_center(self):
        """
        Description: C28340774
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Help Center
          3. Click on About HP Smart
          4. Click on Wireless Print Center

        Expected Result:
          3. App should direct into Wireless Print Center page
        """
        self.__load_link_from_about_hp_smart_screen(self.hp_connect.WIRELESS_PRINT_CENTER_LINK)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    def test_04_hp_smart_terms_of_use_link(self):
        """
        Description: C28340775
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Help Center
          3. CLick on About HP Smart
          4. Click on HP Smart Terms of Use link on Smart Dashboard screen

        Expected Result:
          4. App should direct into Terms of Use page
        """
        self.__load_link_from_about_hp_smart_screen(self.hp_connect.HP_SMART_TERMS_OF_USE_LINK)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    def test_05_hp_privacy(self):
        """
        Description: C28340776
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Help Center
          3. CLick on About HP Smart
          4. Click on HP Privacy link

        Expected Result:
          4. App should direct into HP Privacy page
        """
        self.__load_link_from_about_hp_smart_screen(self.hp_connect.HP_PRIVACY_LINK)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"
  
    ######################################################################
    #                        PRIVATE FUNCTIONS                           #
    ######################################################################
    def __load_link_from_about_hp_smart_screen(self, link_name):
        """
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Toogle menu / Users item
          3. Type each link on this screen
        """
        self.fc.load_smart_dashboard_help_center_about_hp_smart()
        self.hp_connect.click_link(link=link_name)
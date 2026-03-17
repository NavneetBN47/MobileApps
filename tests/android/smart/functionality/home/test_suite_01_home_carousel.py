from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import PACKAGE

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_01_Home_Carousel(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]

        # Define the variable
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_home_without_printer_connected(self):
        """
        Description: C31297428
         1. Load Home screen without printer connected (Use app reset to make sure no printer connected)
         2. Verify Printer section on Home screen
        Expected Results:
         2. Verify below points:
           + No small "+" button on nav bar
           + message "Add Your First Printer" display under big "+" icon
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.verify_add_new_printer()
        self.home.verify_home_nav_add_printer_icon(invisible=True)

    def test_02_home_with_printer_connected(self):
        """
        Description: C31297429, C31297430, C31297432, C31297447
         1. Load Home screen
         2. Click on Add Printer button on Home screen
         3. Select target printer from printer lists
        Expected Results:
         3. Verify Home screen with below points:
           + No "Add Your First Printer" icon on Home screen
           + small "+" button on nav bar
        """
        self.__load_home_screen_connected_printer()
        self.home.verify_add_new_printer(invisible=True)
        self.home.verify_home_nav_add_printer_icon()

    def test_03_home_nav_add_btn(self):
        """
        Description:C31297445
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Click on small "+" button on Home top navigation bar
         3. Select Add Printer
        Expected Results:
         3. Verify Printer screen
        """
        self.__load_home_screen_connected_printer()
        self.home.select_nav_add_icon()
        self.printers.select_printer_option_add_printer()
        self.printers.verify_printers_screen()

    def test_04_printer_information(self):
        """
        Description: C31297434, C31297438
         1. Load Home screen with printer connected
         2. Long press Printer icon
         3. Click on Printer Information button
        Expected Results:
         3. Verify My Printer screen
        """
        self.__load_home_screen_connected_printer()
        self.home.long_press_printer()
        self.home.verify_long_press_printer_popup()
        self.home.select_printer_information()
        self.printer_settings.verify_my_printer(self.bonjour_name)

    def test_05_forget_this_printer(self):
        """
        Description: C31297435
         1. Load Home screen with printer connected
         2. Long press Printer icon
         3. Click on Forget This Printer button
         4. Click "FORGET" btn
        Expected Results:
         3. Verify Forget This Printer popup with:
            - Popup message "Forget this...."
            - CANCEL button
            - FORGET button
         4. Verify Home screen with printer is removed success with:
        """
        self.__load_home_screen_connected_printer()
        self.home.long_press_printer()
        self.home.select_forget_this_printer()
        self.home.verify_home_nav()
        self.home.verify_printer_model_name(self.bonjour_name, invisible=True)

    def test_06_estimated_supply_levels(self):
        """
        Description: C31297440, C31297441
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Click on Estimated Supply Levels
        Expected Results:
         2. Verify Estimated Supply screen
        """
        self.__load_home_screen_connected_printer()
        self.home.select_estimated_supply_levels()
        if self.app_settings.verify_accept_cookies_popup(raise_e=False):
            self.app_settings.dismiss_accept_cookies_popup()
        if self.printer_settings.verify_pin_dialog(raise_e=False):
            pin_code = self.p.get_pin()
            self.printer_settings.select_and_submit_pin_code(pin_code)
        assert (self.home.verify_supply_status_screen() or (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME)), "Estimated ink level screen isn't launched success"

    def test_07_printer_carousel_btn(self):
        """
        Description: C31297433, C31297439
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Click on Printer area on top of screen
        Expected Results:
         2. Verify My Printer screen
        """
        self.__load_home_screen_connected_printer()
        self.home.load_printer_info()
        self.printer_settings.verify_my_printer(self.bonjour_name)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_home_screen_connected_printer(self):
        """
        If current screen is not Home screen, load to Home screen.
        - If there is no connected printer, select a target printer
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        if self.home.verify_printer_model_name(self.bonjour_name, raise_e=False, timeout=15):
            self.fc.flow_home_select_network_printer(self.p, is_searched=True)
            self.home.dismiss_print_anywhere_popup()
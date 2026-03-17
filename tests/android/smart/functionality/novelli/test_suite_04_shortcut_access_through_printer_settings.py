from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from selenium.common.exceptions import TimeoutException

pytest.app_info = "SMART"

class Test_Suite_04_Shortcut_Access_Through_Printer_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Novelli printer is unavailable for testing this time")

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]

        #Define the variable
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_verify_shortcut_function_on_printer_settings(self):
        """
         Description:
         C29093827, C29172108, C29093838, C29093843, C29093887
         1. Load to Home screen with HP+ account login
         2. Select a novelli printer from printer list
         3. Click on Printer icon on Home screen
         4. Click on Shortcuts option from Printer settings screen
         5. Click on Help icon next to Shortcuts
         6. Click on Back button

         Expected Result:
         3. Verify Shortcuts under Options screen
         4. Verify app goes to Shortcuts screen
         5. Verify Shortcuts Help screen
         6. Verify Shortcuts screen
        """
        self.fc.flow_home_load_shortcuts_access_screen(self.bonjour_name, self.p)
        self.shortcuts.click_help_btn()
        self.shortcuts.verify_shortcuts_help_screen()
        self.shortcuts.click_back_btn()
        self.shortcuts.verify_shortcuts_screen(timeout=20)

    def test_02_enable_disable_shortcut_access_function(self):
        """
         Description:
         C29093848, C29093844, C29093866, C29093892, C29093893, C29093890, C29093891, C29093892
          1. Load to Home screen with HP+ account login
         2. Select a Novelli printer from printer list
         3. Click on Printer icon on Home screen
         4. Click on Shortcuts option from Printer settings screen
         5. Click on Printer Access item on Shortcuts screen
         6. Click on Access Off button
         7. Click on More Option button
         8. Click on 1 year-Most convenient option, and click on Save button
         9. Click on OK button
         10. Click on Access expires in 365 days 
         11. Click on Access Off, then save button
         12. Click on Ok button

         Expected Result:
         5. Verify Access Shortcuts screen
         7. Verify below options display:
            - 1 day--Most secure
            - 1 year--Most convenient
            - Custom
        8. Verify Shortuct access enabled screen
        11. Verify Shortcut access disabled screen
        12. Verify Shortcuts screen
        """
        self.fc.flow_home_load_shortcuts_access_screen(self.bonjour_name, self.p)
        self.shortcuts.click_printer_access_arrow_btn()
        self.shortcuts.verify_access_shortcuts_screen()
        self.shortcuts.click_more_options_btn()
        self.shortcuts.verify_one_day_most_secure_option()
        self.shortcuts.verify_custom_option()
        self.shortcuts.click_one_year_most_convenient_option()
        self.shortcuts.click_edit_save_btn()
        self.shortcuts.verify_shortcuts_access_enabled_screen()
        self.shortcuts.click_back_btn()
        self.shortcuts.verify_access_shortcuts_screen()
        self.shortcuts.click_access_off_option()
        self.shortcuts.click_edit_save_btn()
        self.shortcuts.verify_shortcuts_access_disabled_screen()
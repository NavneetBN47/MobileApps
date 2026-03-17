from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_05_Shortcut_Access_Through_Shortcuts(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Novelli printer is unavailable for testing this time")

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]

        #Define the variable
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_verify_shortcut_access_through_shortcuts_tile(self):
        """
         Description:
         C29093873, C29093876, C29093889
         1. Load to Home screen with HP+ account login
         2. Select a novelli printer from printer list
         3. Click on Shortcut tile from Home screen
         4. Click on X button next to Shortcuts Access Off item

         Expected Result:
         3. Verify Shortcuts Access Off item displays on shortcuts screen
         4. Verify Shortcuts Access Off message is disappeared
        """
        self.fc.flow_home_load_shortcuts_screen(create_acc=False, printer_obj=self.p)
        self.shortcuts.verify_shortcuts_access_off_item()
        self.shortcuts.click_close_btn()
        self.shortcuts.verify_shortcuts_access_off_item(invisible=True)

    def test_02_verify_enable_shortcut_access_function(self):
        """
         Description:
         C29093875
          1. Load to Home screen with HP+ account login
         2. Select a novelli printer from printer list
         3. Click on Shortcut tile from Home screen
         4. Click on Enable item Shortcuts Access Off
         5. Click on More Option button
         6. Click on 1 year--Most convenient option
         7. Click on Save button

         Expected Result:
         4. Verify Access Shortcuts screen
         7. Verify Access Shortcuts enabled screen
        """
        self.fc.flow_home_load_shortcuts_screen(create_acc=False, printer_obj=self.p)
        self.shortcuts.verify_shortcuts_access_off_item()
        self.shortcuts.click_enable_btn()
        self.shortcuts.verify_access_shortcuts_screen()
        self.shortcuts.verify_one_day_most_secure_option(invisible=True)
        self.shortcuts.verify_custom_option(invisible=True)
        self.shortcuts.click_one_year_most_convenient_option()
        self.shortcuts.click_edit_save_btn()
        self.shortcuts.verify_shortcuts_access_enabled_screen()
    
    def test_03_verify_access_expiring_message_screen(self):
        """
         Description:
         C29093848, C29093878
         1. Load to Home screen with HP+ account login
         2. Select a novelli printer from printer list
         3. Click on Shortcut tile from Home screen
         4. Click on Settings icon
         5. Click on Access expires in 365 days
         6. Click on Access Off button
         7. Click on Save button

         Expected Result:
         4. Verify Access expires in message
         8. Verify Access Shortcuts disabled message
        """
        self.fc.flow_home_load_shortcuts_screen(create_acc=False, printer_obj=self.p)
        self.shortcuts.verify_shortcuts_access_off_item(invisible=True)
        self.shortcuts.click_settings_btn()
        self.shortcuts.verify_access_expiring_message_with_one_year_option()
        self.shortcuts.click_printer_access_arrow_btn()
        self.shortcuts.verify_access_shortcuts_screen()
        self.shortcuts.click_access_off_option()
        self.shortcuts.click_edit_save_btn()
        self.shortcuts.verify_shortcuts_access_disabled_screen()
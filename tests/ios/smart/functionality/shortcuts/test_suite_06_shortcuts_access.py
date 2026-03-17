import pytest
import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_06_Shortcuts_Access(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.stack = request.config.getoption("--stack")
        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Novelli printer is unavailable for testing this time")
        ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True, driver=cls.driver)
        cls.fc.go_home(stack=cls.stack)

    def test_01_toggle_shortcuts_access(self):
        """
        Requirements:
         1.C31461895 - Verify 'Access Shortcuts' screen 
         2.C31461896 - Verify 'Shortcuts Access' screen
         3.C31461897 - Verify 'Access Off' option
         4.C31461898 - Verify '1 year-Most convenient' option
         5.C31461899 - Verify '1 day - Most secure' option
         6.C31461900 - Verify 'custom' option 
        Steps:
         1. Launch Smart app
         2. Load Printer
         3. Tap on Printer Icon
         4. Select Shortcuts
         5. Select Printer Access
         6. Select 1 Year duration
         7. Select Save
         8. Select Ok Button
         9. Select Printer Access
         10. Select More Options11. Select 1 day 
         12. Select Save
         13. Select Ok Button
         14. Select Printer Access
         15. Select Access Off
         16. Select Save
         17. Select Ok Button
        Expected Results:
         4. Verify Shortcuts title
         5. Verify Shortcuts Access screen
         7. Verify Shortcuts Access Enabled screen
         8. Verify Shortcuts title
         9. Verify Shortcuts Access screen
         12. Verify Shortcuts Access Enabled screen
         13. Verify Shortcuts title
         14. Verify Shortcuts Access screen
         16. Verify Shortcuts Access Disabled screen         
         17. Verify Shortcuts title
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(self.printer_settings.PS_SHORTCUTS, verify_nav=False)
        for option in ["one_year", "one_day", "custom", "access_off"]:
            logging.info(f'Testing option "{option}"')
            self.shortcuts.verify_shortcuts_title(timeout=30)
            self.shortcuts.click_printer_access_arrow_btn()
            self.shortcuts.verify_access_shortcuts_screen()
            if option == "one_year":
                self.shortcuts.click_one_year_most_convenient_option()
            elif option == "one_day":
                self.shortcuts.click_more_access_options_btn()
                self.shortcuts.click_one_day_most_secure_option()
            elif option == "custom":
                self.shortcuts.click_more_access_options_btn()
                self.shortcuts.pick_custom_date()
            else:
                self.shortcuts.click_access_off_option()
            self.shortcuts.click_edit_save_btn()
            if option == "access_off":
                self.shortcuts.verify_shortcuts_access_disabled_screen()
            else:
                self.shortcuts.verify_shortcuts_access_enabled_screen()
            self.shortcuts.click_ok_btn()
            self.shortcuts.verify_shortcuts_title(timeout=30)

    def test_02_shortcuts_access_from_tile(self):
        """
        Requirements:
         1. C31461888 - Verify 'Shortcuts Access Off' message
         2. C31461890 - Verify X button on 'Shortcuts Access Off' message
         3. C31461889 - Enable Access from 'Shortcuts Access Off' message
         4. C31461892 - Change Access from 'Shortcuts Access Expiring ' message 
        Steps
         1. Launch Smart App
         2. Load Printer
         3. Select Shortcuts Tile
         4. Select x Button on Shortcuts Access Off message
         5. Select Back button
         6. Select Shortcuts Tile
         7. Select Enable on Shortcuts Access Off message
         8. Select 1 day
         9. Select Save
         10. Select OK button
         11. Select Renew
         12. Select Access Off
         13. Select Save
        Expected Results:
         4. Verify Shortcuts Access Off message is invisible
         7. Verify Shortcuts Access screen
         9. Verify Shortcut Access Enabled screen
         10. Verify Shortcuts screen
         11. Verify Shortcuts Access screen
         13. Verify Shortcut Access Disabled screen
        """
        self.fc.go_to_home_screen()
        self.home.select_tile_by_name(self.home.SHORTCUTS_BTN)
        self.home.close_smart_task_awareness_popup()
        self.shortcuts.verify_shortcuts_screen(timeout=30)
        self.shortcuts.verify_shortcuts_access_off_item()
        self.shortcuts.click_close_btn()
        self.shortcuts.verify_shortcuts_access_off_item(invisible=True)
        self.shortcuts.click_back_btn()
        self.home.close_smart_task_awareness_popup()
        self.home.select_tile_by_name(self.home.SHORTCUTS_BTN)
        self.shortcuts.verify_shortcuts_screen(timeout=30)
        self.shortcuts.click_enable_btn()
        self.shortcuts.verify_access_shortcuts_screen()
        self.shortcuts.click_access_off_option()
        self.shortcuts.click_edit_save_btn()
        self.shortcuts.verify_shortcuts_access_disabled_screen()
        self.shortcuts.click_ok_btn()
        self.shortcuts.verify_shortcuts_title(timeout=30)
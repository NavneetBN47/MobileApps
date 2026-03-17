from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_03_Invalid_Shortcuts_Name(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_shortcuts_name_starts_with_invalid_special_characters(self):
        """
        Description:
          1. Load to Home screen with HPID account login
          2. Click on Smart Tasks tile
          3. Click on Add Shortcut button
          4. Click on Create your own Shortcut
          5. Click on Print item
          6. Click on Continue button, and type shortcut name which starts/ middle/end with special character, or end with period

        Expected Result:
          6. Verify the error message "invalid shortcut name format"
        """
        shortcut_names = ["%12e", "12=e", "12e@", "12e."]
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.verify_add_print_screen()
        self.shortcuts.click_add_to_shortcut_btn()
        self.shortcuts.click_continue_btn()
        for name in shortcut_names:
            self.shortcuts.enter_shortcut_name(name)
            self.shortcuts.verify_invalid_shortcut_name_text()
            self.shortcuts.clear_shortcut_name()
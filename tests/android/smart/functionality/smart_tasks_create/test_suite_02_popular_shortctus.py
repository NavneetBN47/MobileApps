from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
import datetime

pytest.app_info = "SMART"


class Test_Suite_02_Popular_Shortcuts(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define the variable
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)


    def test_01_print_email_save_screen(self):
        """
        Requirements:
          1. C31461694	"Subject" section can be modified
          2. C31461695	"Body" section can be modified
          3. C31461708	Verify file type options for Unsupported printer
          4. C31461711	Verify settings page for shortcut with all options together (Supported printer) 
          5. C31461736	"X" button behavior on source selection dialog
          6. C31461703	[Print,Email, and Save] Redirection 
          7. C31461704	Test print,email, and save flow to the end 
          
        Description:
          1. Load to Shortcuts screen
          2. Click on Print, Email, and Save button
          3. Select Short edge option
          4. Click on Add to Shortcut button
          5. Type the email address
          6. Type the subject and Body
          7. Click on Add to Shortcut button
          8. Click on Save to google drive
          9. Click on Add to Shortcut button
          10. Click on Continue button
          11.Type Shortcut Name
          12. Click on Save Shortcut screen
          13. Click on Start Shortcut button
          14. Click on X button from source page screen

        Expected Result:
          2. Verify Add Print screen
          12. Shortcuts save success
          13. Verify Source page screen
          14. Verify Shortcuts save success

        """
        shortcuts_name = "{}_{:%H_%M_%S}".format("print_save_email",(datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_print_email_and_save_btn()
        self.shortcuts.verify_add_print_screen()
        self.shortcuts.select_two_sided(self.shortcuts.SHORT_EDGE_BTN)
        self.shortcuts.click_add_to_shortcut_btn()
        self.shortcuts.verify_add_email_screen()
        self.shortcuts.enter_email_receiver(self.email_address)
        self.shortcuts.enter_subject_receiver("Files for testing")
        self.shortcuts.enter_body_receiver("The attached file have been sent to your")
        self.shortcuts.click_add_to_shortcut_btn()
        self.shortcuts.verify_add_save_screen()
        self.shortcuts.click_google_drive_checkbox()
        self.shortcuts.click_add_to_shortcut_btn()
        self.shortcuts.verify_settings_screen(invisible=False)
        self.shortcuts.click_file_type_btn()
        self.shortcuts.verify_file_type_screen()
        self.shortcuts.click_files_type_back_btn()
        self.shortcuts.verify_settings_screen(invisible=False)
        self.shortcuts.enter_shortcut_name(shortcuts_name)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(timeout=15)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_x_btn()
        self.shortcuts.verify_shortcut_saved_screen(timeout=15)

    def test_02_save_to_google_drive(self):
        """
        Requirements:
          1. C31461802	[Save to Google Drive] Redirection
          
        Description:
          1. Load to Shortcuts screen
          2. Click on Save to Google Drive button

        Expected Result:
          2. Verify Add Save screen
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_save_to_google_drive_btn()
        self.shortcuts.verify_add_save_screen()

    def test_03_verify_back_button_from_shortcuts_screen(self):
        """
        Requirements:
          1. 	C31461664	Shortcuts Screen : Back button functionality 
          
        Description:
          1. Load to Shortcuts screen
          2. Click on Back button

        Expected Result:
          2. Verify Home screen
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.shortcuts.click_back_btn()
        self.home.verify_home_nav()
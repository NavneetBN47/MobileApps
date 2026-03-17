import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_04_Verify_Edit_Shortcuts(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.camera = cls.fc.fd["camera"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.preview = cls.fc.fd["preview"]
        cls.app_settings = cls.fc.fd["app_settings"]
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(button_index=1, stack=cls.stack)

    def test_01_verify_three_button_menu_shortcut(self):
        """
        Requirements:
            C31461841 - Verify 3 dot menu on 'Edit Shortcut' screen
            C31461839 - Verify 'Start' functionality from 3 dot menu
            C31461836 - Verify 3 button menu items for shortcut 
            C31461737 - "X" button behavior from Shortcuts page already created shortcut
        Preconditions:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.User will see a list of shortcuts
            5.Tap on the 3 button menu next to any shortcut
            6.Tap on the Start option
            7. Verify source select screen
            9. Press "X" Button
            10. Verifly shortcuts screen present
        Expected result:
            1. Source select popup appears
            2. "X" button is successfully pressed and shortcuts screen is present
        """
        shortcuts_name = f"Email_{self.test_01_verify_three_button_menu_shortcut.__name__}_{ma_misc.get_random_str()}"
        self.create_a_shortcut(shortcuts_name)
        self._navigate_to_shortcuts_verify_screen_menu(shortcuts_name)
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_x_btn()
        self.shortcuts.verify_shortcuts_screen()
    
    def test_02_verify_cancel_edit_option(self):
        """
        Requirements:
            C31461840 - Verify 'Edit Shortcut' screen
            C31461853 - Verify cancel shortcut functionality under Edit Shortcuts screen
            C31461667 - Verify Cancel button functionality on Add shortcut screen
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Tap on the 3 button menu next to any shortcut
            5.Tap on the Cancel option
            6.Tap on "No, Continue Edits" option on confirmation popup screen
            7.Tap on Cancel button again
            8.Tap on "Yes, Cancel Edits" button on confirmation popup screen
        Expected results:
            1. Edit cancel popup shows up
            2. Shortcuts screen appears after clicking 'yes' button
        """
        shortcuts_name = f"Email_{self.test_02_verify_cancel_edit_option.__name__}_{ma_misc.get_random_str()}"
        self.create_a_shortcut(shortcuts_name)
        self._navigate_to_shortcuts_verify_screen_menu(shortcuts_name)
        self.shortcuts.click_edit_btn()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.click_edits_cancel_popup_no_btn()
        self.shortcuts.verify_edit_shortcut_screen()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.click_edits_cancel_popup_yes_btn()
        self.shortcuts.verify_shortcuts_screen()

    def test_03_verify_edit_email_shortcut_screen(self):
        """"
        Requirements:
            C31461845 - Verify 'Edit Email' screen
            C31461849 - Tap Remove button on 'Edit Email' screen
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.User will see a list of shortcuts
            5.Tap on the 3 button menu next Email shortcut
            6.Tap on the Edit option
            7.On the Edit Shortcut screen, tap on the 3 dot menu next to Email and then tap Edit
        Expected results:
            1. Edit email screen appears after clicking edit email button
            2. Remove edits popup appears after taping on remove email button
        """
        shortcuts_name = f"Email_{self.test_03_verify_edit_email_shortcut_screen.__name__}_{ma_misc.get_random_str()}"
        self.create_a_shortcut(shortcuts_name)
        self._navigate_to_shortcuts_verify_screen_menu(shortcuts_name)
        self.shortcuts.click_edit_btn()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_edit_btn()
        self.shortcuts.verify_edit_email_screen()
        self.shortcuts.click_remove_btn()
        self.shortcuts.verify_shortcut_remove_edits_popup()
    
    def test_04_verify_print_edit_screen(self):
        """
        Requirements:
            C31461842 - Verify 'Edit Print' screen
            C31461847 - Tap Remove button on 'Edit Print' screen
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.User will see a list of shortcuts
            5.Tap on the 3 button menu next print shortcut
            6.ap on the Edit option
            7.On the Edit Shortcut screen, tap on the 3 dot menu next to Print and then tap Edit
        Expected results:
            1. Edit print screen appears
            2. Verify shortcuts after pressing remove button
        """
        shortcuts_name = f"Print_test_{self.test_04_verify_print_edit_screen.__name__}_{ma_misc.get_random_str()}"
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.fc.save_shortcut(shortcuts_name, invisible=True)
        self._navigate_to_shortcuts_verify_screen_menu(shortcuts_name)
        self.shortcuts.click_edit_btn()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_edit_btn()
        self.shortcuts.verify_edit_print_screen()
        self.shortcuts.click_remove_btn()
        self.shortcuts.verify_shortcut_remove_edits_popup()
    
    def test_05_verify_edit_email_save_option(self):
        """
        Requirements:
            C31461846 - Verify 'Edit Save' screen
            C31461850 - Tap Save button on 'Edit Email' screen
            C31461852 - Tap Save button on 'Edit Save' screen
            C31461727 - Run already created shortcut (Email)
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.User will see a list of shortcuts
            5.Tap on the 3 button menu next to the Save shortcut
            6.Tap on the Edit option
            7.On the Edit Shortcut screen, tap on the 3 dot menu next to Save and then tap Edit
            8.On the Edit Save screen, make some changes to save settings and tap Save
        Expected result:
            1. Verify edit save screen as appears
        """
        shortcuts_name = f"Email_{self.test_05_verify_edit_email_save_option.__name__}_{ma_misc.get_random_str()}"
        self.create_a_shortcut(shortcuts_name)        
        self._navigate_to_shortcuts_verify_screen_menu(shortcuts_name)
        self.shortcuts.click_edit_btn()
        self.shortcuts.click_continue_btn()
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen()

    def test_06_verify_edit_print_save_option(self):
        """
        Requirements:
            C31461848 - Tap Save button on 'Edit Print' screen
            C31461851 - Tap Save button on 'Edit Save' scree
            C31461844 - Tap 'Continue' button on Edit Shortcut screen
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.User will see a list of shortcuts
            5.Tap on the 3 button menu next print shortcut
            6.Tap on the Edit option
            7.On the Edit Shortcut screen, tap on the 3 dot menu next to Print and then tap Edit
            8.On the Edit Print screen, make some changes to print settings and tap Save
        Expected result:
            1. User is back to Edit Shortcut screen and the Print setting changes are reflected in the Shortcut
        """
        shortcuts_name = f"Print_test_{self.test_06_verify_edit_print_save_option.__name__}_{ma_misc.get_random_str()}"
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.fc.save_shortcut(shortcuts_name, invisible=True)
        self._navigate_to_shortcuts_verify_screen_menu(shortcuts_name)
        self.shortcuts.click_edit_btn()
        self.shortcuts.click_continue_btn()
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen()

    @pytest.mark.parametrize("quick_run", [True, False])
    def test_07_verify_processing_file_popup_print(self, quick_run):
        """
        Requirements:
            C31461725 - "Your file is processing" pop up when "Quick Run" is enabled
            C31461726 - "Your file is processing" pop up when "Quick Run" is enabled with print
            C31461728 - Run already created shortcut (Print) (Quick Run Disabled)
            C31461730 - Run already created shortcut (Print) (Quick Run Enabled)
        Steps: 
            1.Launch HP Smart app
            2.Sign In to your account
            3.Get to home page
            4.Tap on Shortcuts
            5.Tap on 3 vertical dots next to created shortcut
            6.Select "Start" option
            7.Capture a file
            8.Tap on "Next" on detect edges page
            9.Tap on 'Start(shortcut name)' button
            10.Tap on "Finish Shortcut" button
        Expected results:
            1. Your file is being uploaded popup appears with Quick Run Enabled/Disabled
            2. User is redirected to Finish Shortcut
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password, remove_default_printer=False)
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        shortcuts_name = f"Print_test_{self.test_07_verify_processing_file_popup_print.__name__}_{ma_misc.get_random_str()}"
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.fc.save_shortcut(shortcuts_name, invisible=True)
        self._navigate_to_shortcuts_verify_screen_menu(shortcuts_name)
        
        if quick_run:
            self.shortcuts.click_edit_btn()
            self.shortcuts.click_continue_btn()
            self.shortcuts.click_quick_run_checkbox()
            self.shortcuts.click_save_shortcut_btn()
            self.shortcuts.click_start_shortcut_btn()
        else:
            self.shortcuts.click_start_btn()
        self.shortcuts.click_scanner_btn()
        self.camera.clear_tips_pop_up()
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next(timeout=40)
        
    def create_a_shortcut(self, shortcuts_name):
        email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_email_btn()
        self.shortcuts.verify_add_email_screen()
        self.shortcuts.enter_email_receiver(email_address)
        self.shortcuts.change_email_subject_text("Testing - Email Shortcuts")
        self.fc.save_shortcut(shortcuts_name, invisible=False)

    def _navigate_to_shortcuts_verify_screen_menu(self, shortcuts_name):
        self.fc.navigate_to_shortcuts_screen()
        self.shortcuts.open_shortcuts_menu(shortcuts_name)
        self.shortcuts.verify_shortcuts_option_menu()
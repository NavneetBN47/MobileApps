import pytest
import datetime
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA, WEBVIEW_URL

pytest.app_info = "SMART"

class Test_Suite_02_Create_Own_Shortcuts(object):

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
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.notifications = cls.fc.fd["notifications"]
        cls.camera = cls.fc.fd["camera"]
        cls.preview = cls.fc.fd["preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.photos = cls.fc.fd["photos"]
        cls.files = cls.fc.fd["files"]
        cls.fc.go_home(button_index=1, stack=cls.stack)

    
    @pytest.mark.parametrize("print_option",["two_sided_off,color,single_copies", "short_edge,black,single_copies",
                                             "long_edge,color,multi_copies"])
    def test_01_verify_create_your_own_shortcut(self, print_option):
        """
        Requirements:
            C31461698 - End to end flow of creating new shortcut 
            C31461676 - Print "+" button redirection
            C31461679 - Back "Cancel" button behavior on Add Print page
            C31461687 - Two-sided option can be changed
            C31461688 - "Add to Shortcut" button behavior from Add Print page:
            C31461689 - "Add Shortcut" button behavior after changes have been made:
            C31461685 -  Copies option can be changed 
            C31461686 - Color option can be changed
            C31461703 -	[Print,Email, and Save] Redirection 
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Tap on "Create your own Shortcuts" option
            5.Tap on "+" button next to Print section
            6.Expand the 'Copies' dropdown
            7.Select any other option
        Expected results:
            1.User is redirected to "Add Print" screen after pressing "+" button
            2.User is redirected back to Add Shortcut page after tapping cancel
            3.Verify that list of other options can be shown and other option can be selected
            4.User is redirected to Add Shortcut page with saved default info from Add Print page
            5.User is redirected to Add Shortcut page with saved modified info from Add Print page
            6.Verify that list of other options can be shown and other option can be selected
            7.Verify that list of other options can be shown and other option can be selected
        """
        print_option = print_option.split(",")
        shortcuts_name = self.generate_shortcut_name(print_option[0] + "_" + print_option[1])
        sides_option = {
            "two_sided_off": self.shortcuts.OFF_BTN,
            "short_edge": self.shortcuts.SHORT_EDGE_BTN,
            "long_edge": self.shortcuts.LONG_EDGE_BTN}
        color_option = {
            "color": self.shortcuts.COLOR_BTN,
            "black": self.shortcuts.GRAYSCALE_BTN}
        copies_num = {"single_copies": self.shortcuts.SINGLE_COPIES_BTN,
                      "multi_copies": self.shortcuts.MULTIPLE_COPIES_BTN}
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=copies_num[print_option[2]])
        self.shortcuts.select_color(color_btn=color_option[print_option[1]])
        self.shortcuts.select_two_sided(two_sided_option=sides_option[print_option[0]])
        self.fc.save_shortcut(shortcuts_name, invisible=True)
    
    @pytest.mark.parametrize("email_option", ["valid_email", "invalid_email"])
    def test_02_verify_email_shortcut(self, email_option):
        """
        Requirements:
            C31461677 - Email "+" button redirection
            C31461690 - Enter valid email address in "To" section
            C31461691 - Enter invalid email address in "To" section 
            C31461704 - Test print,email, and save flow to the end
            C31461680 - Cancel button behavior on Add Email page
            C31461694 - "Subject" section can be modified
            C31461695 - "Body" section can be modified
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Tap on "Create your own Shortcuts" option
            5.Tap on "+" button next to Email section
        Expected results:
            1.Verify user is redirected to "Add Email" page after taping on "+" button.
            2.User is redirected to Add Shortcut page with saved info from Add Email page if valid email adress is used in "To" section
            3.Verify error message occur and user is not able to move forward if invalid email adress is used in "To" section
        """
        shortcuts_name = self.generate_shortcut_name(email_option)
        email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_email_btn()
        self.shortcuts.verify_add_email_screen()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.click_email_btn()
        if email_option == "valid_email":
            self.shortcuts.enter_body_receiver("body_works")
            self.shortcuts.enter_email_receiver(email_address)
            self.shortcuts.change_email_subject_text("Testing - Email Shortcuts")
            self.fc.save_shortcut(shortcuts_name, invisible=False)
            
        else:
            self.shortcuts.enter_email_receiver("qa.mobiautotest")
            self.shortcuts.click_add_to_shortcut_btn()
            self.shortcuts.verify_invalid_email_message_screen()
    
    @pytest.mark.parametrize("option", ["yes", "no"])
    def test_03_verify_shortcut_cancel_btn(self, option):
        """
        Requirements:
            C31461697 - Cancel created shortcut and then continue it
            C33559184 - Verify Cancel button functionality on Add shortcut screen
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Tap on "Create your own Shortcuts" option
            5.Tap on "Cancel" button from top left corner
            6.Tap on "No, Continue Shortcut" button
        Expected results:
            1.User stays at Add Shortcut page
        """
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.verify_shortcuts_cancel_popup(timeout=15)
        if option == "yes":
            self.shortcuts.click_yes_cancel_shortcut_btn()
            self.shortcuts.verify_add_shortcuts_screen()
        else:
            self.shortcuts.click_no_continue_shortcut_btn()
            self.shortcuts.verify_add_your_own_shortcut_screen()
    
    @pytest.mark.parametrize("from_page", ["print", "email", "save"])
    def test_04_verify_shortcut_help(self, from_page):
        """
        Requirements:
            C31461682 - Question "?" button behavior on Add Print page
            C31461683 - Question "?" button behavior on Add Email page
            C31461684 - Question "?" button behavior on Add Save page
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Tap on "Create your own Shortcuts" option
            5.Tap on "+" button next to Print/Email/Save section
            6.Tap on "?" button from top right corner
        Expected result:
            1.Users should see content of Shortcuts Help when expanded
        """
        self.fc.navigate_to_add_shortcuts_screen()
        if from_page == "print":
            self.shortcuts.click_print_btn()
        elif from_page == "email":
            self.shortcuts.click_email_btn()  
        else:
            self.shortcuts.click_save_btn()
        self.click_and_verify_help_shortcut()
    
    @pytest.mark.parametrize("save_option", ["google_drive", "dropbox"])
    def test_05_verify_save_shortcuts_screen(self, save_option):
        """
        Requirements:
            C31461678 - Save "+" button redirection
            C31461681 - Back "<" button behavior on Add Save page ? duplicated case           
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Tap on "Create your own Shortcuts" option
            5.Tap on "+" button next to Save section
        Expected results:
            1.User is redirected to "Add Save" screen
        """
        shortcuts_name = self.generate_shortcut_name(save_option)
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_save_btn()
        self.shortcuts.verify_add_save_screen()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.click_save_btn()
        if save_option == "google_drive":
            self.shortcuts.click_checkbox_for_saving(index=0)
        else:
            self.shortcuts.click_checkbox_for_saving(index=1)
        self.fc.save_shortcut(invisible=False, shortcuts_name=shortcuts_name, click_home=False)

    @pytest.mark.parametrize("btn_option", ["activity_center", "continue", "home"])
    def test_06_verify_start_shortcut_btn_behavior(self, btn_option):
        """
        Requirements:
            C31461712 - "Start Shortcut" button behavior after creating a shortcut for 1-st time
            C31461717 - 'Camera' button redirection from Select a Source pop-up
            C31461721 - "Your file is being uploaded for processing" pop up
            C31461738 - "Your file is processing" pop up
            C31461722 - "Continue" button behavior from Your file is processing pop up
            C31461723 - "Home" button behavior from Your file is processing pop up
            C31461724 - "Activity" button behavior from Your file is processing pop up
            C31461729 - Run already created shortcut (Save)
            C31461734 - Source selection dialog when Printer is selected
        Steps:
            1.Launch the app
            2.Sign In to your account
            3.Create a new shortcut and navigate to "Settings" page
            4.Give a name to shortcut
            5.Tap on "Save Shortcut" button
            6.Tap on "Start Shortcut" on shortcut saved page
            7.Get to "Select Source" page
            8.Select any source and get to 'Adjust Boundaries/Detect Edges' page
            9.Tap on "Next" button
            10.Get to page where selected file is located
                O1-11Tap on "Activity" button on pop up
                O2-11.Tap on "Continue" button on pop up
                O3-11.Tap on "Home" button on pop up
            12.Tap on 'Start (shortcut name)' button
            13.Wait for some time on "Your file is being uploaded for processing" screen
        Expected results:
            1. User is redirected to select source page.
            2.Tapping on the Start Button should displays the Source Selection Dialog.
            3.Pop up is dismissed and user stays on the same page
            4."Your file is being uploaded for processing" screen is shown
            5."Your file is processing" screen is shown with 3 options:
        """
        shortcuts_name = self.generate_shortcut_name("DropBox_Test")
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_save_btn()
        self.shortcuts.verify_add_save_screen()
        self.shortcuts.click_checkbox_for_saving(index=1)
        self.fc.save_shortcut(invisible=False, shortcuts_name=shortcuts_name, click_home=False)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_camera_btn()
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()
        self.scan.select_scan_job_button(change_check={"wait_obj": "adjust_boundaries_title", "flow_change": "preview"})
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        if self.preview.verify_second_close_btn():
            self.preview.select_second_close_btn()
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_file_is_being_uploaded_popup()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen()
        if btn_option == "activity_center":
            self.shortcuts.click_activity_btn()
            self.notifications.verify_notifications_screen()
        elif btn_option == "continue":
            self.home.select_continue()
            self.preview.verify_preview_screen()
        elif btn_option == "home":
            self.shortcuts.click_shortcuts_home_btn()
            self.home.close_organize_documents_pop_up()
            self.home.verify_home()
    
    def test_07_verify_printer_scan_redirection(self):
        """
        Requirements:
            C31461718 - 'Printer Scan' button redirection from Select a Source pop-up
        Steps:
            1.Launch the app
            2.Sign In to your account
            3.Create a new shortcut and navigate to "Settings" page
            4.Give a name to shortcut
            5.Tap on "Save Shortcut" button
            6.Tap on "Start Shortcut" on shortcut saved page
            7.Get to "Select Source" page
            8.Tap on Printer Scan optionrinter scan option
        Expected result:
            1.Verify user is redirected to printer scan page
        """
        shortcuts_name = self.generate_shortcut_name("DropBox_Test")
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.fc.save_shortcut(shortcuts_name, invisible=True, click_home=False)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_scanner_btn()
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.verify_scanner_screen()
    
    def test_08_verify_files_n_photos_redirection(self):
        """
        Requirements:
            C31461719 - 'Files&Photos' button redirection from Select a Source pop-up
            C31461736 - "X" button behavior on source selection dialog
        Steps:
            1.Launch the app
            2.Sign In to your account
            3.Create a new shortcut and navigate to "Settings" page
            4.Give a name to shortcut
            5.Tap on "Save Shortcut" button
            6.Tap on "Start Shortcut" on shortcut saved page
            7.Get to "Select Source" page
            8.Tap on Files&Photos option
        Expected results:
            1.Verify pop up is dismissed and Shortcut Saved page is shown again
            2.User is redirected to Files&Photos page
        """
        shortcuts_name = "{}_{:%Y_%m_%d_%H_%M_%S}".format("DropBox_Test", (datetime.datetime.now()))
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.fc.save_shortcut(shortcuts_name, invisible=True, click_home=False)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_x_btn()
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_files_photo_btn()
        self.camera.select_allow_access_to_camera_on_popup()
        self.photos.select_allow_access_to_photos_popup()
        self.files.verify_files_screen()

    @pytest.mark.parametrize("btn_option", ["start_shortcut_btn", "my_shortcuts_btn", "home_btn"])
    def test_09_shortcut_saved_screen(self, btn_option):
        """
        Requirements:
            C31461716 - "Home" button behavior after creating a shortcut not for a 1-st time
            C31461714 - "Start Shortcut" button behavior after creating a shortcut not for a 1-st time
            C31461715 - "My Shortcut" button behavior after creating a shortcut not for a 1-st time
        Steps:
            1.Launch the app
            2.Sign In to your account
            3.Get to "Settings" page
            4.Give a name to shortcut
            5.Tap on "Save Shortcut" button
            6.Tap on "Start Shortcut" on shortcut saved page
            8.Get to "Shortcut Saved" page
            9.Tap on "Home" button
        Expected results:
            1.User is redirected to select source page
            2."Shortcut Saved" page is shown
            3.User is redirected to home page
        """
        shortcuts_name = self.generate_shortcut_name("email_test")
        email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_email_btn()
        self.shortcuts.verify_add_email_screen()
        self.shortcuts.enter_email_receiver(email_address)
        self.shortcuts.change_email_subject_text("Testing - Email Shortcuts")
        self.fc.save_shortcut(shortcuts_name, invisible=False, click_home=False)
        if btn_option == "my_shortcuts_btn":
            self.shortcuts.click_my_shortcuts_btn()
            self.shortcuts.verify_shortcuts_screen()
        elif btn_option == "home_btn":
            self.shortcuts.click_home_btn()
            self.home.close_organize_documents_pop_up()
            self.home.verify_home()
        elif btn_option == "start_shortcut_btn":
            self.shortcuts.click_start_shortcut_btn()
            self.shortcuts.verify_source_select_popup()

    def generate_shortcut_name(self, name):
        return "{}_{:%Y_%m_%d_%H_%M_%S}".format(name, (datetime.datetime.now()))

    def click_and_verify_help_shortcut(self):
        self.shortcuts.click_help_btn()
        self.driver.wait_for_context(WEBVIEW_URL.SHORTCUTS)
        self.shortcuts.click_shortcuts_help_expand_page_btn()
        self.shortcuts.verify_shortcuts_help_screen()
"""
Shortcuts flow and functionality smoke test suite for iOS
"""
import datetime
import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_Smoke_05_Shortcuts:
    """
    Shortcuts flow class for smoke testing for iOS
    """
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        """
        Necessary modules and resources are defined in this setup function
        """
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.home = cls.fc.fd["home"]
        login_info = ma_misc.get_hpid_account_info(
            stack=cls.stack, a_type="ucde", instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.p = load_printers_session

    @pytest.mark.parametrize("shortcut_type", ["save", "email"])
    def test_01_shortcut_settings_page_print_option(self, shortcut_type):
        """
        Requirements:
            C31461708 - Verify file type options for Unsupported printer
            C31461709 - Settings page for shortcut with only email option (Supported printer)
            C31461710 - Verify settings page for shortcut with only save option (Supported printer)
            C31461711 - Verify settings page for shortcut
                        with all options together (Supported printer)
            C31461705 - Settings page for shortcut with only print option
        Steps:
            1.Launch the app
            2.Sign In to account
            3.Add printer to carousal
            4.Tap on Shortcuts tile
            5.Tap on "Add Shortcut"
            6.Get to page with 3 options of creating shortcut
            7.Tap on "Create your own Shortcuts" option
            8.Tap on "+" button next to Print section
            9.Tap on "Add to Shortcut" button
            10.Get to Add Shortcut page
            11.Tap on "Continue" button
            12.Get to Settings page
            13.Tap on file type button
            14.Get to the File Type screen
        Expected results:
            1.Settings screen contains the required fields
            2.File type screen contains the required fields

        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username,
                        password=self.password, remove_default_printer=False)
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(
                printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.navigate_to_add_shortcuts_screen()
        if shortcut_type == "save":
            self.shortcuts.click_save_btn()
            self.shortcuts.verify_add_save_screen()
            self.shortcuts.click_checkbox_for_saving(index=1)
        else:
            email_address = saf_misc.load_json(ma_misc.get_abs_path(
                TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
            self.shortcuts.click_email_btn()
            self.shortcuts.verify_add_email_screen()
            self.shortcuts.enter_email_receiver(email_address)
            self.shortcuts.change_email_subject_text(
                "Testing - Email Shortcuts")
        self.shortcuts.click_add_to_shortcut_btn()
        self.shortcuts.click_continue_btn()
        self.shortcuts.verify_settings_screen(False)
        self.shortcuts.click_file_type_btn()
        self.shortcuts.verify_file_type_screen()

    @pytest.mark.parametrize("print_option", ["two_sided_off,color,single_copies",
                                              "short_edge,black,single_copies", "long_edge,color,multi_copies"])
    def test_02_verify_create_your_own_shortcut(self, print_option):
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
        shortcuts_name = self.generate_shortcut_name(
            print_option[0] + "_" + print_option[1])
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
        self.shortcuts.select_two_sided(
            two_sided_option=sides_option[print_option[0]])
        self.fc.save_shortcut(shortcuts_name, invisible=True)

    def generate_shortcut_name(self, name):
        """
        Function for generating a shortcut name by implementing datetime module
        """
        return "{}_{:%Y_%m_%d_%H_%M_%S}".format(name, (datetime.datetime.now()))

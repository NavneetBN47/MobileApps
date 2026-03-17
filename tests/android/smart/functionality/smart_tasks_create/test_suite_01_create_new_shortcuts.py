from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
import datetime
from time import sleep

pytest.app_info = "SMART"


class Test_Suite_01_Create_New_Shortcuts(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.ows_value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.web_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]
        cls.smb = cls.fc.flow[FLOW_NAMES.SMB]

        # Define the variable
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.smart_context = cls.fc.smart_context
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)


    def test_01_shortcuts_login_by_creating_account_via_tile(self):
        """
        Description: C31461808
          1. Load to Home screen
          2. Click on Smart Tasks tile
          3. Click on Create Account button
          4. Create a new HPID account

        Expected Result:
          4. Verify Smart Tasks empty lists screen
        """
        self.__load_hpid_sign_in_screen()
        # Handle for welcome screen of Google Chrome
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        if not self.hpid.verify_hp_id_sign_up(raise_e=False):
            self.hpid.click_create_account_link()
        self.hpid.verify_hp_id_sign_up()
        self.hpid.create_account()
        #After click on create account button, it take some time to load to Shortcuts screen
        self.home.check_run_time_permission(accept=True, timeout=30)
        self.shortcuts.dismiss_coachmark()
        self.shortcuts.verify_shortcuts_screen(timeout=15)

    def test_02_shortcuts_login_via_tile(self):
        """
        Description: C31461810, C33559181, C31461663
          1. Load to Home screen
          2. Go to App Setting to logout HPID account
          3. Click on Back button
          4. Click on Smart Tasks tile
          5. Click on Sign In button
          6. Login HPID account

        Expected Result:
          6. Verify Smart Tasks screen:
             - Title
             - "+" button
        """
        self.__load_hpid_sign_in_screen(index=1)
        # Handle for welcome screen of Google Chrome
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        #Todo: From HPID login to Smart Tasks screen will take to 20s. And has CR GDG-1768 for tracking this issue
        self.home.check_run_time_permission(accept=True, timeout=20)
        if self.smb.select_my_printers(raise_e=False):
            self.smb.select_continue()
        self.driver.wait_for_context(self.smart_context, timeout=15)
        self.shortcuts.verify_shortcuts_screen(timeout=15)

    def test_03_shortcuts_help_screen(self):
        """
        Description: C31297216, C33559182, C31461665
          1. Load to Shortcuts screen
          2. Click on Help button
          3.Click on Back button

        Expected Result:
          2. Verify Help screen via:
             + Title
             + Help Message
          3. Verify Shortcuts screen
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.shortcuts.click_help_btn()
        # This is a super long page, and takes around 50s to scroll to Shortcuts help section
        self.shortcuts.click_shortcuts_help_expand_page_btn()
        self.shortcuts.click_connecting_to_your_printer_expand_page_btn(clickable=False)
        self.shortcuts.click_shortcuts_help_expand_page_btn()
        self.shortcuts.verify_shortcuts_help_screen(timeout=15)
        self.driver.press_key_back()
        self.shortcuts.verify_shortcuts_screen(timeout=15)


    @pytest.mark.parametrize("print_option",["two_sided_off,color,single_copies",
                                             "short_edge,black,single_copies",
                                             "long_edge,color,multi_copies"
                                             ])
    def test_04_create_your_own_shortcuts_for_print(self, print_option):
        """
        Description: C31461676, C31461685, C31461686, C31461687, C31461688, C31461689, C31461705, C31461698, C28299209
          1. Load to Shortcuts screen
          2. Click on Add Shortcuts button
          3. Click on Create your own Shortcut button
          4. click on Print button
          5. For print type:
             - color_two_sided_off: Click on Two-sided / Color / single copies
             - color_long_edge: Click on long edge / Color / Multi copies
             - black_short_edge: Click on Grayscale / short edge / single copies
          7. Click on Add to Shortcut button
          8. Click on Continue button
          9.Type Shortcut Name
          10. Click on Save Shortcut screen

        Expected Result:
          3. Verify Add Shortcut screen
          4. Verify Add Print screen
          8.  Verify Settings screen
          10. Verify Shortcut Saved screen
        """
        print_option = print_option.split(",")
        shortcuts_name = "{}_{}_{:%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], print_option[1], (datetime.datetime.now()))
        sides_option = {
            "two_sided_off": self.shortcuts.OFF_BTN,
            "short_edge": self.shortcuts.SHORT_EDGE_BTN,
            "long_edge": self.shortcuts.LONG_EDGE_BTN}
        color_option = {
            "color": self.shortcuts.COLOR_BTN,
            "black": self.shortcuts.GRAYSCALE_BTN}
        copies_num = {"single_copies": self.shortcuts.SINGLE_COPIES_BTN,
                      "multi_copies": self.shortcuts.MULTIPLE_COPIES_BTN}
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.verify_add_print_screen()
        self.shortcuts.select_copies(copies_num=copies_num[print_option[2]])
        self.shortcuts.select_color(color_btn=color_option[print_option[1]])
        self.shortcuts.select_two_sided(two_sided_option=sides_option[print_option[0]])
        self.fc.flow_save_shortcuts(invisible=True, shortcuts_name=shortcuts_name)

    @pytest.mark.parametrize("email_option", ["valid_email", "invalid_email"])
    def test_05_create_your_own_shortcut_for_email(self, email_option):
        """
        Description:C31461677, C31461690, C31461691, C31461709
          1. Load to Shortcuts screen
          2. Click on Add Shortcuts button
          3. Click on Create your own Shortcut button
          4. Click on Email item
          5. Type email address
             - valid_email: type valid email address
             - invalid_email: type invalid email address
          6. Click on Add to Shortcut button
          7. Click on Continue button
          8.Type Shortcut Name
          9. Click on Save Shortcut screen

        Expected Result:
          4. Verify Add Email screen
          5. If invalid recipient from step 5, then verify invalid recipient popup:
                - Message
            If valid recipient from step 6, then click on Add to Shortcut button
          9. Verify Shortcut Saved screen
        """
        shortcuts_name = "{}_{}_{:%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], email_option, (datetime.datetime.now()))
        email_options = {
            "valid_email": self.email_address,
            "invalid_email": "qa.mobiautotest"}
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_email(email_options[email_option])
        if email_option == "invalid_email":
            self.shortcuts.click_add_to_shortcut_btn()
            self.shortcuts.verify_invalid_email_message_screen()
        else:
            self.fc.flow_save_shortcuts(invisible=False, shortcuts_name=shortcuts_name)

    @pytest.mark.parametrize("save_option", ["google_drive", "dropbox"])
    def test_06_create_your_own_shortcuts_for_save(self, save_option):
        """
        Description: C31461678, C31461710
          1. Load to Shortcuts screen
          2. Click on Add Shortcuts button
          3. Click on Create your own Shortcut button
          4. Click on Save item
          5. Select Google Drive option and Dropbox option
          6. Click on Add to Shortcut button
          7. Click on Continue button
          8.Type Shortcut Name
          9. Click on Save Shortcut screen

        Expected Result:
          4. Verify "Add Save screen
          9. Verify Shortcut Saved screen
        """
        shortcuts_name = "{}_{}_{:%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], save_option, (datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.shortcuts.click_save_btn()
        self.shortcuts.verify_add_save_screen()
        if save_option == "google_drive":
            self.shortcuts.click_google_drive_checkbox()
        else:
            self.shortcuts.click_dropbox_checkbox()
        self.fc.flow_save_shortcuts(invisible=False, shortcuts_name=shortcuts_name)

    @pytest.mark.parametrize("cancel_option", ["yes", "no"])
    def test_07_add_shortcut_cancel(self, cancel_option):
        """
        Description: C33559184, C31461667, C31461679, C31461680, C31461696, C31461697
          1. Load to Shortcuts screen
          2. Click on Add Shortcuts button
          3. Click on Create your own Shortcut button
          4. Click on Cancel button
          5. Click on Yes, Cancel Shortcut button
             Or Click on No, Continue Shortcut button

        Expected Result:
          4. Verify Cancel popup
          5. if cancel_option is Yes, then verify Add Shortcut screen
             if can_option is No, then verify Add Shortcuts screen
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.verify_shortcuts_cancel_popup(timeout=15)
        if cancel_option == "yes":
            self.shortcuts.click_yes_cancel_shortcut_btn()
            self.shortcuts.verify_add_shortcuts_screen()
            self.shortcuts.click_create_your_own_shortcut_btn()
            self.shortcuts.click_print_btn()
            self.shortcuts.click_cancel_btn()
            self.shortcuts.verify_add_your_own_shortcut_screen()
            self.shortcuts.click_email_btn()
            self.shortcuts.click_cancel_btn()
            self.shortcuts.verify_add_your_own_shortcut_screen()
        else:
            self.shortcuts.click_no_continue_shortcut_btn()
            self.shortcuts.verify_add_your_own_shortcut_screen()

    def test_08_add_shortcut_help(self):
        """
        Description: C33559185, C31461668, C31461683
          1. Load to Shortcuts screen
          2. Click on Add Shortcuts button
          3. Click on Create your own Shortcut button
          4. Click on Help button
          5. Click on Yes, Cancel Shortcut button
             Or Click on No, Continue Shortcut button

        Expected Result:
          4. Verify Help message
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.shortcuts.click_help_btn()
        #This is a super long page, and takes around 50s to scroll to Shortcuts help section
        self.shortcuts.click_connecting_to_your_printer_expand_page_btn(clickable=False)
        self.shortcuts.click_shortcuts_help_expand_page_btn()
        self.shortcuts.verify_shortcuts_help_screen(timeout=15)

    @pytest.mark.parametrize("btn_option", ["my_shortcuts_btn", "home_btn"])
    def test_09_shortcut_saved_screen(self, btn_option):
        """
        Description: C31461700, C31461713, C31461715, C31461716
          1. Load to Shortcuts screen
          2. Create your own shorcut to lead to Shortcut Saved screen
          3. Click on each button to lead to different screen:
             - my_shortcuts_btn
             - home_btn

        Expected Result:
          3. - my_shortcuts_btn: verify My shortcuts screen
             - home_btn: verify Home screen
        """
        shortcuts_name = "{}_{}_{:%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], btn_option, (datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_email(self.email_address)
        self.fc.flow_save_shortcuts(invisible=False, shortcuts_name=shortcuts_name)
        if btn_option == "my_shortcuts_btn":
            self.shortcuts.click_my_shortcuts_btn()
            self.shortcuts.verify_shortcuts_screen()
        else:
            self.shortcuts.click_home_btn()
            self.home.verify_home_nav()

    def test_10_add_save_help(self):
        """
        Description: C31461684
          1. Load to Shortcuts screen
          2. Click on Add Shortcuts button
          3. Click on Create your own Shortcut button
          4. Click on Add Save option
          5. Click on Help button

        Expected Result:
          5. Verify Help message
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.shortcuts.click_save_btn()
        self.shortcuts.verify_add_save_screen()
        self.shortcuts.click_help_btn()
        # This is a super long page, and takes around 50s to scroll to Shortcuts help section
        self.shortcuts.click_connecting_to_your_printer_expand_page_btn(clickable=False)
        self.shortcuts.click_shortcuts_help_expand_page_btn()
        self.shortcuts.verify_shortcuts_help_screen(timeout=15)

    def test_11_verify_add_save_back_function(self):
        """
        Description: C31461681
          1. Load to Shortcuts screen
          2. Click on Add Shortcuts button
          3. Click on Create your own Shortcut button
          4. Click on Add Save option
          5. Click on Cancel button

        Expected Result:
          5. Verify Add Shortcut screen
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.shortcuts.click_save_btn()
        self.shortcuts.verify_add_save_screen()
        self.shortcuts.click_cancel_btn()
        self.shortcuts.verify_add_your_own_shortcut_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_hpid_sign_in_screen(self, index=0):
        """
        1. Logout HPID if HPID still login
        2. Load to Home screen
        3. Click on Smart Tasks tile, and click on get started button
        """
        self.fc.reset_app()
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.SMART_TASKS))
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
        self.ows_value_prop.select_value_prop_buttons(index=index)
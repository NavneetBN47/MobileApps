import datetime
import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA
 
pytest.app_info = "SMART"

class Test_Suite_01_Shortcuts_Ui(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.home = cls.fc.fd["home"]
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.p = load_printers_session

    def test_01_help_and_back_btn(self):
        '''
        Requirements:
            1.C33559181 - Add Shortcut screen- prebuilt shortcuts
            2.C33559182 - Verify help and back button functionality on Add Shortcut screen
            3.C33559185	- Verify help button functionality on Add shortcut screen
            4.C31461665 - Verify help and back button functionality on Add Shortcut screen
            5.C31461668 - Verify help button functionality on Add shortcut screen
            6.C31461664 - Shortcuts Screen : Back button functionality
            
        Steps:
            1-Launch HP Smart, login & go home
            2-Select the Shortcuts tile
            3-Tap on Add shortcuts button
            4-Tap on the help icon (to verify shortcuts info in the help center menu) & then close it
            5-Tap on the back arrow in the top left corner (Verify user is redirected to Shortcuts screen)
            
        Expected results:
            1.Verify prebuilt shortcuts present after tapping Shortcuts tile
            2.Check back button functionality
            3.Verify create your own shortcout functionality
        '''
        self.fc.go_home(reset=False, stack=self.stack, create_account=False)
        self.fc.navigate_to_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.home.select_navigate_back()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_help_btn()
        sleep(5)
        self.shortcuts.click_shortcuts_help_expand_page_btn()
        self.shortcuts.verify_shortcuts_help_screen()

    def test_02_default_shortcuts(self):
        '''
        Requirements:
            C31461660 - Shortcuts Screen : No Shortcuts- Default email shortcut
            C31461661 - Shortcuts Screen : User Deletes default email shortcut 
            C31461808 - Accessing shortcuts as a new user
            C31461837 - Verify delete shortcut confirmation pop up
            C31461838 - Verify delete shortcut functionality
            C31461843 - Tap 'Delete' button on Edit Shortcut screen
        
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Select default shortcut
            5.Delete default shortcut
         
        Expected results:
            1.Verify default e-mail shortcut presence
            2.Delete default shortcut
            3.Verify empty shortcut screen
        '''
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.fc.navigate_to_shortcuts_screen()
        self.shortcuts.dismiss_coachmark()
        default_shortcut_name = "Email {}".format(self.driver.session_data["hpid_user"].split("@")[0].replace("+", "_").replace(".", "_"))
        self.shortcuts.select_shortcut(default_shortcut_name, click_obj=False)
        self.shortcuts.delete_single_shortcut(default_shortcut_name, is_delete=True)
        self.shortcuts.verify_empty_shortcuts_screen()
        
    def test_03_add_shortcuts_as_user(self):
        """
        Requirements:
            1.C31461810 - Accessing shortcuts as a user with shortcuts
            2.C31461835 - Verify shortcut list user experience
            3.C33559183 - Add shortcut screen after tapping create your own shortcuts
            4.C31461663 - Add Shortcut screen- prebuilt shortcuts
            5.C31461662 - Shortcuts Screen : Existing shortcuts
            6.C31461666 - Add shortcut screen after tapping create your own shortcuts
            7.C31461700 - Cloud destination is showing as signed in
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.Tap on Add Shortcut button
            5.Add new shortcut
            6.Go to home
            7.Access shortcut as user when shortcut present
        Expected result:
            1.Shortcut can be accessed as user with shortcuts
            2.Pre built shortcuts are present when accesing shortcuts
            3.Shortcuts are present after tapping on Shortcuts on home screen
            4.'Add Shortcut' screen opens up with Print, Email and Save Destinations
            5.Shortcut is present on shortcuts screen after creation
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password, remove_default_printer=False)
        shortcuts_name = self.generate_shortcut_name("test_ui_shortcut")
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_save_btn()
        self.shortcuts.verify_add_save_screen()
        self.shortcuts.click_checkbox_for_saving(index=1)
        self.fc.save_shortcut(invisible=False, shortcuts_name=shortcuts_name, click_home=True)
        self.fc.navigate_to_shortcuts_screen()
        assert self.shortcuts.select_shortcut(shortcuts_name, click_obj=False)
    
    @pytest.mark.parametrize("shortcut_type", ["save", "email"])
    def test_04_shortcut_settings_page_print_option(self, shortcut_type):
        """
        Requirements:
            C31461708 - Verify file type options for Unsupported printer
            C31461709 - Settings page for shortcut with only email option (Supported printer)
            C31461710 - Verify settings page for shortcut with only save option (Supported printer)
            C31461711 - Verify settings page for shortcut with all options together (Supported printer)
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
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password, remove_default_printer=False)
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.navigate_to_add_shortcuts_screen()
        if shortcut_type == "save":
            self.shortcuts.click_save_btn()
            self.shortcuts.verify_add_save_screen()
            self.shortcuts.click_checkbox_for_saving(index=1)
        else:
            email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
            self.shortcuts.click_email_btn()
            self.shortcuts.verify_add_email_screen()
            self.shortcuts.enter_email_receiver(email_address)
            self.shortcuts.change_email_subject_text("Testing - Email Shortcuts")
        self.shortcuts.click_add_to_shortcut_btn()
        self.shortcuts.click_continue_btn()
        self.shortcuts.verify_settings_screen(False)
        self.shortcuts.click_file_type_btn()
        self.shortcuts.verify_file_type_screen()

    def generate_shortcut_name(self, name):
        return "{}_{:%Y_%m_%d_%H_%M_%S}".format(name, (datetime.datetime.now()))
    
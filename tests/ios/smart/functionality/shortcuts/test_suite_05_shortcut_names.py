import pytest
from random import choice
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_05_Shortcut_Names(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.fc.go_home(stack=cls.stack)
    
    def test_01_invalid_shortcut_names(self):
        """
        Requirements:
            C33559172 - New shortcuts invalid name starts with special characters
            C33559173 - New Shortcuts invalid name with Special characters in the middle 
            C33559174 - New Shortcuts invalid name ends with period
            C33559175 - New Shortcuts invalid name ends with Special characters
            C33559176 - New Shortcuts without a name
        Steps:
            1.Launch the Smart App
            2.Login to the HPID account and proceed to home screen
            3.Tap on Shortcuts tile
            4.On the Shortcuts screen click on Add Shortcut button
            5.Click on Create your own Shortcut item
            6. Enable Print item
            7. Click on Continue button
            8. Input a shortcut name starts/contains/ends with any special charater, like "%12d" or no shortcut name.
        Expected results:
            1.The error message "Shortcut name is invalid" displays on the screen
        """
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_add_to_shortcut_btn()
        self.shortcuts.click_continue_btn()
        self.shortcuts.verify_settings_screen(invisible=True)
        names = self.generate_invalid_names()
        for shortcut_name in names:
            self.shortcuts.enter_shortcut_name(shortcut_name)
            self.shortcuts.verify_invalid_shortcut_name_text()
            self.shortcuts.clear_shortcut_name()

    def generate_invalid_names(self):
        '''
        invalid cases:
        starts with special characters (exclude "-", "_")
        ends with special characters
        ends with .
        without a name
        '''
        names = []
        middle_invalid = "#$%&()*+/:<=>?@[]^`{|}~"
        special_chars = middle_invalid + "."
        for _ in range(5):
            names.append(choice(special_chars) + self.fc.get_random_str())
            names.append(self.fc.get_random_str() + choice(middle_invalid) + self.fc.get_random_str())
            names.append(self.fc.get_random_str() + choice(special_chars))
        return names
import datetime
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_07_Shortcuts:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.fc.go_home(button_index=1, stack=cls.stack)

    @pytest.mark.parametrize("print_option",["two_sided_off,color,single_copies", "short_edge,black,single_copies",
                                             "long_edge,color,multi_copies"])
    def test_01_verify_create_your_own_shortcut(self, print_option):
        """
        Requirements:
            C50698994: "Add Shortcut" button behavior after changes have been made
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

    def generate_shortcut_name(self, name):
        return "{}_{:%Y_%m_%d_%H_%M_%S}".format(name, (datetime.datetime.now()))
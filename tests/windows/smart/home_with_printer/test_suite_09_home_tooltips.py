import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import logging


pytest.app_info = "GOTHAM"
class Test_Suite_09_Home_Tooltips(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_check_tooltips_nav_pane_close(self):
        """
        Hover over navigation pane icon (open & close), verify correct tooltip shows
        Home page Tooltips UI 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28189019  (GOTH-22394)
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28189020
        """    
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_printer(self.p)

        assert self.home.navbar_menu_expand() is False

        self.home.hover_home_icon()
        self.home.verify_home_tooltip()

        self.home.hover_activity_icon()
        self.home.verify_activity_tooltip()

        self.home.hover_add_setup_printer_icon()
        self.home.verify_add_setup_printer_tooltip()

        self.home.hover_diagnose_and_fix_icon()
        self.home.verify_diagnose_and_fix_tooltip()

        self.home.hover_app_settings_icon()
        self.home.verify_app_settings_tooltip()

    def test_02_check_tooltips_nav_pane_open(self):
        """
        Check Home page tooltips when navigation pane opens.
        """   
        self.home.menu_expansion(expand=True)
        assert self.home.navbar_menu_expand() is True

        self.home.hover_home_icon()
        self.home.verify_home_tooltip()

        self.home.hover_activity_icon(expand=True)
        self.home.verify_activity_tooltip()

        self.home.hover_add_setup_printer_icon()
        self.home.verify_add_setup_printer_tooltip()

        self.home.hover_diagnose_and_fix_icon(expand=True)
        self.home.verify_diagnose_and_fix_tooltip()

        self.home.hover_app_settings_icon(expand=True)
        self.home.verify_app_settings_tooltip()

    def test_03_check_activity_center_listitem(self):
        """
        Hover the "Print" and "Shortcuts" options o the AC flyout.
        Press the "Print" and "Shortcuts" options o the AC flyout.
        Hover the "Accounts" options o the AC flyout.
        Press the "Accounts" options o the AC flyout.
        Hover the "Supplies" options o the AC flyout.
        Press the "Supplies" options o the AC flyout.

        Verify hover is a light gray.
        Verify press is a little darker gray than hover state.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14099914
        https://hp-testrail.external.hp.com/index.php?/cases/view/27997742
        https://hp-testrail.external.hp.com/index.php?/cases/view/27803556
        """   
        hover_list = ["print_listview", "shortcuts_listview", "supplies_listview", "account_listview"]
        png_list = ["hover_print.png", "hover_shortcuts.png", "hover_supplies.png", "hover_account.png"]
        self.home.menu_expansion(expand=False)    
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_activity_title()
        value_org = self.fc.check_element_background("left_side_menu_pane", 'activity_center', "org.png")
        logging.info("org vs org: {}".format(value_org))
        assert value_org < 0.05
        sleep(2)
        for i in range(4):
            self.home.hover_activity_item(hover_list[i])
            value_org = self.fc.check_element_background("left_side_menu_pane", 'activity_center', "org.png")
            logging.info("hover vs org: {}".format(value_org))
            assert value_org > 0.02
            value_hover = self.fc.check_element_background("left_side_menu_pane", 'activity_center', png_list[i])
            logging.info("hover vs hover: {}".format(value_hover))
            assert value_hover < 0.05
            sleep(2)


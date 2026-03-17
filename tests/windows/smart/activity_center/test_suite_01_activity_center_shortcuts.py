import pytest
import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_01_Activity_Center_Shortcuts(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.p = load_printers_session

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]
        cls.activity_center = cls.fc.fd["activity_center"]

        cls.shortcut_time={}

        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        time.sleep(3)

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        if self.home.verify_smart_driver_dialog(raise_e=False):
            self.home.click_smart_driver_x_btn()
        self.home.select_print_documents_tile()
        if not self.print.verify_supported_document_file_types_dialog(raise_e=False):
            self.home.verify_install_to_print_dialog()
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=180)
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
            self.home.verify_home_screen()
        else:
            self.fc.restart_hp_smart()

    def test_02_create_a_shortcut(self):
        """
        Create a shortcut     
        """
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        if self.shortcuts.verify_file_already_exists_dialog():
            self.shortcuts.click_already_exists_no_btn()
        self.shortcuts.click_home_btn()
         
    def test_03_verify_shortcut_running_status_shows(self):
        """
        Go to Shortcuts Activity Center window with a ongoing Shortcuts execution.
        Verify "Shortcut Running" status shows with correct information.  

        https://hp-testrail.external.hp.com/index.php?/cases/view/14099933
        """
        self.__delete_shortcut()
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog()
        if self.scan.click_shortcuts_order_for_email(raise_e=False):
            self.scan.verify_your_shortcut_dialog()
            self.scan.click_activity_btn()
            self.activity_center.verify_shortcut_running_item_display()
            time.sleep(45)#wait for job completed
            self.activity_center.click_shortcut_completed_item()
            self.activity_center.click_del_btn()
            self.activity_center.click_close_btn()
            self.activity_center.verify_shortcuts_flyout_disappear()

    def test_04_create_a_shortcut(self):
        """
        Create a shortcut     
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        if self.shortcuts.verify_file_already_exists_dialog():
            self.shortcuts.click_already_exists_no_btn()

    def test_05_check_shortcut_from_activity_btn(self):
        """
        "Activity" button on the "Your Shortcut is on it's way!" dialog.

        Verify it shows with Shortcuts activities.
        Verify the Shortcut current status shows.
        Verify the Shortcut execution date shows.
        Verify the Shortcut name shows for the executed Shortcuts(the text is offscreen, so can not be found).

        https://hp-testrail.external.hp.com/index.php?/cases/view/14099920 
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099926
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099934
        """
        self.shortcuts.click_start_shortcut_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_start_btn()
        self.scan.click_start_btn()
        self.print.verify_simple_print_dialog()
        hostname = self.p.get_printer_information()["host name"][:-1]
        self.print.select_printer(hostname)
        self.print.select_print_dialog_print_btn()
        self.scan.verify_your_shortcut_dialog()
        time.sleep(5)

    def test_06_click_close_btn_on_shortcut_flyout(self):
        """
        Click exit icons on the Shortcuts Activity Center windows (has Shortcuts activity).

        https://hp-testrail.external.hp.com/index.php?/cases/view/14099931
        """
        self.scan.click_activity_btn()
        self.activity_center.verify_shortcuts_item_added()
        self.activity_center.click_close_btn()
        self.activity_center.verify_shortcuts_flyout_disappear()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.click_yes_btn()
        self.home.select_navbar_back_btn()

    def test_07_click_back_arrow_on_shortcut_flyout(self):
        self.home.select_activity_btn()
        self.home.click_shortcuts_listview()
        self.activity_center.verify_shortcuts_item_added()
        self.activity_center.click_shortcut_completed_item()
        self.activity_center.verify_shortcut_completed_dialog()
        self.activity_center.click_print_item()
        time.sleep(2)
        for _ in range(3):
            self.activity_center.click_back_arrow()
        self.activity_center.verify_shortcuts_flyout_disappear()

    def test_08_check_shortcut_from_activity_center_bell(self):
        """
        "Shortcuts" from the Activity Center bell icon.
        Click back arrow on the Shortcuts job status (master view) in Activity Center windows.

        Verify it shows with Shortcuts activities.
        Verify the Shortcut current status shows.
        Verify the Shortcut execution date shows.
        Verify the Shortcut name shows for the executed Shortcuts.
        Go to Shortcuts Activity Center window with a completed Shortcut execution

        https://hp-testrail.external.hp.com/index.php?/cases/view/14099920 
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099926
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099917
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099934
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099929
        https://hp-testrail.external.hp.com/index.php?/cases/view/17155840
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099927
        """
        self.home.select_activity_btn()
        self.home.click_shortcuts_listview()
        self.activity_center.verify_shortcuts_item_added()
        self.activity_center.click_shortcut_completed_item()
        self.activity_center.verify_shortcut_completed_dialog()
        self.activity_center.click_print_item()
        time.sleep(2)
        self.activity_center.click_back_arrow()
        self.activity_center.click_del_btn()
        self.activity_center.click_back_arrow()
        self.activity_center.verify_shortcuts_flyout_disappear()

    def test_09_no_shortcut_activity_center_screen(self):
        """
        Go to Shortcuts Activity Center with an account that has not executed any Shortcut before.
        Click back arrow on the ST Activity Center windows (no Smart Task activity).

        Verify No Shortcut activity information shows in Shortcuts Activity Center window.
        Verify the window is closed and app main UI shows.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14099921
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099924
        """  
        self.home.select_activity_btn()
        self.home.click_shortcuts_listview()
        self.activity_center.verify_shortcuts_dialog()
        for _ in range(5):
            if self.activity_center.click_shortcut_completed_item(raise_e=False):
                self.activity_center.click_del_btn()
            else:
                break
        self.activity_center.click_back_arrow()
        self.driver.ssh.send_command('Stop-Process -Name "*chrome*"')
        self.activity_center.verify_shortcuts_flyout_disappear()
        self.home.verify_home_screen()

    def test_10_click_close_btn_on_empty_shortcut(self):
        """
        Click exit icons on the ST Activity Center windows (no Smart Task activity).

        Verify the window can be exited.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14099925
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099922
        """
        self.home.select_activity_btn()
        self.home.click_shortcuts_listview()
        self.activity_center.verify_shortcuts_dialog()
        self.activity_center.click_close_btn()
        self.activity_center.verify_shortcuts_flyout_disappear()

    def test_11_delete_shortcut(self):
        """
        Delete jobs to prepare for the next test    
        """  
        self.__delete_shortcut()

    def __delete_shortcut(self):
        """
        Delete jobs to prepare for the next test    
        """  
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        for _ in range(5):
            if self.shortcuts.click_dynamic_three_dot(w_const.TEST_TEXT.TEST_TEXT_01):
                self.shortcuts.click_delete_btn()
                self.shortcuts.click_delete_popup_delete_btn(is_win=True)
                self.shortcuts.verify_shortcuts_screen()
            else:
                break
        assert self.shortcuts.verify_dynamic_shortcuts_item(w_const.TEST_TEXT.TEST_TEXT_01) is False
 

"""
Description: This is a smoke test for app. In the smoke test, it include install printer,
welcome flow, post OOBE flow, main UI checking, print flow and scan flow.
"""
import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException
import logging


pytest.app_info = "GOTHAM"
class Test_Suite_01_Smoke(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.softfax_home = cls.fc.fd["softfax_home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.account = cls.fc.fd["account"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.result = {"add_printer": False}

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "ucde")
        
        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_go_home_and_add_a_printer(self):
        """
        User onboarding sign in flow
        *Add a local printer to main UI, verify printer shows on main UI card

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997915
                     https://hp-testrail.external.hp.com/index.php?/cases/view/27266563
        
        """
        self.fc.go_home(self.login_info["email"], self.login_info["password"])
        self.home.verify_navigation_pane_split_view(login=True, printer=False)
        self.home.verify_setup_or_add_printer_card()
        self.home.verify_main_page_tiles()
        self.home.verify_shell_title_bar_removed()
        self.fc.select_a_printer(self.p)
        self.result["add_printer"] = True
        
    def test_02_check_main_ui_sign_in_with_printer(self):
        """
        Observe each tile on the main UI (with a printer), verify correct order shows 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15962728
        """
        if self.result["add_printer"]:
            assert self.home.verify_logged_in() is True
            self.home.verify_navigation_pane_split_view(login=True, printer=True)
            self.home.verify_carousel_printer_image()
            self.home.verify_main_page_tiles()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_03_mobile_fax_flow(self):
        """
        Click "Mobile Fax" tile on the Main UI (Signed in) first time, verify mobile fax landing page shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861532
        """
        if self.result["add_printer"]:
            self.home.select_mobile_fax_tile()
            self.softfax_home.verify_mobile_fax_home_screen()
            self.home.select_navbar_back_btn()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_04_print_settings_flow(self):
        """
        Click "Printer Settings" tile on main UI, verify "Printer Information" screen opens

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14787559
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_printer_settings_tile()
            self.printer_settings.verify_printer_settings_page()
            self.home.select_navbar_back_btn()
        else:
            raise NoSuchElementException('Failed to add printer!')    

    def test_05_print_documents_flow(self):
        """
        Click "Print Documents" tile to print, verify native dialog shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585792
        """
        if self.result["add_printer"]:
            if not self.home.verify_home_screen(raise_e=False):
                self.home.select_navbar_back_btn()
                sleep(2)
            self.home.select_print_documents_tile()
            if not self.print.verify_supported_document_file_types_dialog(raise_e=False):
                self.home.verify_install_to_print_dialog()
                self.home.select_install_printer_btn()
                self.home.verify_installing_printer_dialog()
                self.home.verify_success_printer_installed_dialog(timeout=180)
                self.home.select_success_printer_installed_ok_btn()
                assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
                self.home.verify_home_screen()
                self.home.select_print_documents_tile()
                self.print.verify_supported_document_file_types_dialog()
            self.print.select_do_not_show_this_message_checkbox()
            self.print.select_supported_document_file_types_dialog_ok_btn()
            self.print.verify_file_picker_dialog()
            self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
            self.print.verify_simple_print_dialog()
            
            self.print.select_printer(self.hostname)
            self.print.select_print_dialog_print_btn()
            self.home.verify_home_screen()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_06_scan_scanner_flow(self):
        """
        Click on Scan tile the first time (signed in), verify Scan welcome modal shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572534
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()   
            self.home.select_scan_tile()
            self.scan.verify_scan_intro_page()
            self.scan.click_get_started_btn()
            self.__check_printer_job_status()
            self.scan.click_scan_btn()
            self.scan.verify_scan_result_screen()
            self.scan.click_print_btn()
            self.print.verify_simple_print_dialog()

            self.print.select_printer(self.hostname)
            self.print.select_print_dialog_print_btn()
            self.print.verify_simple_print_dialog(invisible=True)
            self.scan.verify_scan_result_screen()

            self.home.select_navbar_back_btn(return_home=False)
            self.scan.verify_exit_without_saving_dialog()
            self.scan.click_yes_btn()
            self.scan.verify_scanner_screen()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_07_scan_import_flow(self):
        """
        (+) Import a scan local, verify flow

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961733
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_scan_tile()
            self.scan.verify_scanner_screen()
            self.scan.select_import_btn()
            self.scan.verify_import_dialog()
            self.scan.click_import_dialog_get_started_btn()
            self.print.verify_file_picker_dialog()
            self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
            self.scan.verify_import_screen()
            self.scan.click_import_apply_btn()
            self.scan.verify_scan_result_screen()
            self.scan.click_save_btn()
            self.scan.verify_save_dialog()
            self.scan.click_save_dialog_save_btn()
            sleep(3)
            self.scan.click_save_as_dialog_save_btn()
            self.scan.verify_file_has_been_saved_dialog()
            file_path = self.scan.get_the_saved_file_path()
                                
            self.scan.click_dialog_close_btn()
            self.driver.ssh.send_command("del " + file_path)
            sleep(1)
            self.home.select_navbar_back_btn(return_home=False)
            sleep(2)
            self.home.select_navbar_back_btn()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_08_print_photos_flow(self):
        """
        Click "Print Photo" tile on main UI, verify native dialog shows 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585496
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_print_photos_tile()
            self.print.verify_file_picker_dialog()

            self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
            self.print.verify_simple_print_dialog()

            self.print.select_printer(self.hostname)
            self.print.select_print_dialog_print_btn()
            self.home.verify_home_screen()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_09_shortcuts_flow(self):
        """
        Observe each tile on the main UI (with a printer), verify correct behavior shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890732
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_shortcuts_tile()
            self.shortcuts.verify_shortcuts_screen()
            self.home.select_navbar_back_btn()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_10_get_supplies_tile_correct_behavior(self):
        """
        Click "Get Supplies" tile (II eligible), verify II related DSP content shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17117702
        """  
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_get_supplies_tile()
            if self.dedicated_supplies_page.verify_not_now_dialog():
                self.dedicated_supplies_page.select_not_now_btn()
            if self.dedicated_supplies_page.verify_hp_instant_ink_page():
                self.dedicated_supplies_page.select_back_btn()
            else:
                self.web_driver.wait_for_new_window(timeout=15)
                self.web_driver.add_window("get_supplies")
                sleep(3)
                self.web_driver.switch_window("get_supplies")
                sleep(3)
                current_url = self.web_driver.get_current_url()
                if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                    raise NoSuchElementException('Failed launch instant ink url')
                self.web_driver.close_window("get_supplies")
            self.home.verify_home_screen()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_11_help_and_support_tile_correct_behavior(self):
        """
        Click "Help & Support" Tile on the Main UI, Verify the help center web view opens within the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15991975
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_help_and_support_tile()
            self.home.verify_help_and_support_page()
            self.home.select_navbar_back_btn()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_12_printables_tile_flow(self):
        """
        (*)Click on the "Printables" tile, verify correct website opens 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24809585
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_printables_tile()
            self.web_driver.wait_for_new_window(timeout=15)
            self.web_driver.add_window("printables")
            sleep(3)
            self.web_driver.switch_window("printables")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.close_window("printables")
            self.home.verify_home_screen()
        else:
            raise NoSuchElementException('Failed to add printer!')

    def test_13_check_sign_out_dialog_shows(self):
        """
        Sign out via app settings (Win) / person icon (Mac) on Main UI, verify user can sign out without issue

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715859
        """
        if self.result["add_printer"]:
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.fc.sign_out()
            assert self.home.verify_logged_in() is False
        else:
            raise NoSuchElementException('Failed to add printer!')

    def __check_printer_job_status(self):
        cur_id = self.p.get_newest_job_id()
        job_status = self.p.check_print_job_status(cur_id)
        logging.info("Printer status {}".format(job_status))
        if job_status['printer_status'] != 'ready':
            sleep(30)

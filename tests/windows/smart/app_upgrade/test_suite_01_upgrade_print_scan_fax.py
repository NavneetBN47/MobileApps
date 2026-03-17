import pytest
from time import sleep
import logging
from SAF.misc import saf_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.resources.const.ios.const import TEST_DATA


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_01_Upgrade_Print_Scan_Fax(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.sf = SystemFlow(cls.driver)
        cls.install_app_path = install_app
        cls.search_app = 'HP Smart'

        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]

        cls.login_info = ma_misc.get_hpid_account_info(stack="production", a_type="ucde")
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_06"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        
        cls.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(2)
        cls.driver.ssh.send_command('start-process "ms-windows-store://home"')

        cls.version_info = {}
        cls.version_info["expected_app_version"] = cls.install_app_path[-10:]

    def test_01_install_ms_store_hp_smart(self):
        """
        Upgrade app to the latest live version, verify basic functions on the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541029
        """    
        self.sf.search_app_on_mircosoft_store(self.search_app)
        self.sf.launch_app_on_mircosoft_store()
        self.welcome.verify_welcome_screen()

        self.version_info["store_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Live build Version - {}'.format(self.version_info["store_app_version"]))
        
    def test_02_install_latest_hp_smart(self):
        """
        Upgrade app to the latest live version, verify basic functions on the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541029
        """
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        launch_activity, close_activity = self.fc.get_activity_parameter()   
        self.driver.terminate_app(close_activity)
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.fc.change_stack_server(stack='production', restart=False)
        self.driver.launch_app(launch_activity)
        self.fc.go_home()
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()

        self.version_info["actual_app_version"] = self.fc.get_installed_hp_smart_version()
        logging.info('Installed Test build Version after upgrade - {}'.format(self.version_info["actual_app_version"]))

        assert self.version_info["actual_app_version"] > self.version_info["store_app_version"]
        assert self.version_info["actual_app_version"] == self.version_info["expected_app_version"]

    def test_03_login_and_add_printer(self):
        """
        Sign in HP account and add printer for testing
        """
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

    def test_04_check_print_function(self):
        """
        Upgrade app to the latest live version, verify basic functions on the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541029
        """
        printer = self.driver.ssh.send_command('Get-Printer -Name "*hp*"')
        if not printer["stdout"]:
            self.home.select_print_documents_tile()
            self.home.verify_install_to_print_dialog()
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=120)
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False

        self.home.select_print_documents_tile()
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()
        hostname = self.p.get_printer_information()["host name"][:-1]
        self.print.select_printer(hostname)
        self.print.verify_simple_pdf_print_dialog()
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_05_check_scan_function(self):
        """
        Upgrade app to the latest live version, verify basic functions on the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541029
        """
        self.home.select_scan_tile()
        self.scan.verify_new_scan_auto_enhancements_dialog()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.home.select_navbar_back_btn()

    def test_06_check_mobile_fax_function(self):
        """
        Upgrade app to the latest live version, verify basic functions on the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541029
        """
        self.home.select_mobile_fax_tile()
        self.mobile_fax.verify_mobile_fax_home_screen()
        self.mobile_fax.select_compose_fax_menu()
        self.mobile_fax.enter_recipient_information(self.recipient_info["phone"])
        self.mobile_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.mobile_fax.click_add_files_option_btn(self.mobile_fax.FILES_PHOTOS_BTN)
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.mobile_fax.verify_add_files_successfully()
        self.mobile_fax.click_send_fax()
        self.mobile_fax.verify_job_sent_successfully()
        self.home.select_navbar_back_btn()

    def test_07_check_behavior_after_logout(self):
        """
        App update: Local printing/scanning becomes permanently available for logged in users after app update

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550539
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.fc.sign_out()
        self.home.select_print_documents_tile()
        self.print.verify_supported_document_file_types_dialog()
        self.home.select_navbar_back_btn()

        self.home.select_scan_tile()
        self.scan.verify_scanner_screen()
        self.home.select_navbar_back_btn()

        self.home.select_shortcuts_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

        self.home.select_mobile_fax_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()








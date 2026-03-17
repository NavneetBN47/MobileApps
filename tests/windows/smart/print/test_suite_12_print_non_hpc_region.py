import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_12_Print_Non_HPC_Region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.sf = SystemFlow(cls.driver)

        cls.host_name = cls.p.get_printer_information()['host name']

        cls.home = cls.fc.fd["home"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        # cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_go_to_home_page(self):
        """
        Verify Supported Document File Types dialog shows after clicking Print Document tile with printer (printer driver installed)
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12341708
        """
        self.sf.change_pc_region_to_non_hpc_region()
        self.fc.go_home()
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        if self.host_name not in self.driver.ssh.send_command("Get-Printer")["stdout"]:
            launch_activity, close_activity = self.fc.get_activity_parameter() 
            self.driver.terminate_app(close_activity)
            self.driver.ssh.send_command('Start-Process "ms-settings:printers" -windowstyle Maximized')
            self.sf.select_printer_on_win_settings(self.host_name.split("HP")[1])
            self.driver.launch_app(launch_activity)

    def test_02_check_print_documents(self):
        """
        Print document locally (non HPC region), verify output and that Simple PDF Print dialogue is received
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072363
        """
        self.home.select_print_documents_tile()
        # OWS-68809
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        self.print.verify_supported_document_file_types_dialog(timeout=60)

        self.print.select_supported_document_file_types_dialog_ok_btn()

        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.host_name)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_03_check_print_photos(self):
        """
        Print photo locally (non HPC region), verify output and that Simple photo Print dialog is received
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064336
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()

        self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.host_name)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_04_check_print_on_scan_preview(self):
        """
        Print photo from local printer (non HPC region), verify Simple Photo Print screen shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064129
        """
        self.home.select_scan_tile()
        self.scan.verify_new_scan_auto_enhancements_dialog()

        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.host_name)
        self.print.select_print_dialog_print_btn()
        self.scan.verify_scan_result_screen()

    def test_05_restore_region(self):
        self.sf.change_pc_region_to_us_region()

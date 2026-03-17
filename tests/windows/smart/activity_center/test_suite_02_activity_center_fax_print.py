import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.resources.const.ios.const import TEST_DATA
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_02_Activity_Center_Fax_Print(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]
        cls.print = cls.fc.fd["print"]
        cls.activity_center = cls.fc.fd["activity_center"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_06"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        
    def test_01_go_home_without_a_printer(self):
        """
        Verify the Print option is not available when no printer is added on the Main UI.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/26973394
        https://hp-testrail.external.hp.com/index.php?/cases/view/25701886
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.select_activity_btn()
        self.home.verify_activity_pane(add_printer=False)
        self.home.select_navbar_back_btn()

    def test_02_send_mobile_fax(self):
        """
        Finish send Mobile Fax flow.
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
        self.mobile_fax.verify_job_is_sending()

        sleep(10)
        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

    def test_03_check_fax_from_activity_center_bell(self):
        """
        Click bell icon
        Click "Mobile Fax" option under the bell 

        Verify correct fax history shows under "Sent" page'

        https://hp-testrail.external.hp.com/index.php?/cases/view/17320211
        https://hp-testrail.external.hp.com/index.php?/cases/view/17361143
        https://hp-testrail.external.hp.com/index.php?/cases/view/16932012
        https://hp-testrail.external.hp.com/index.php?/cases/view/19429269
        https://hp-testrail.external.hp.com/index.php?/cases/view/26973390
        """
        if not self.home.verify_home_screen(raise_e=False):
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
        self.home.select_activity_btn()
        self.home.verify_activity_pane(add_printer=False)
        self.home.click_mobile_fax_listview()
        self.mobile_fax.verify_mobile_fax_home_screen()
   
    def test_04_delete_mobile_fax_job(self):
        """
        clear the job
        """
        self.mobile_fax.click_delete_this_fax_btn()
        self.mobile_fax.verify_are_you_sure_dialog()
        self.mobile_fax.click_delete_btn()
        sleep(5)
        self.home.select_navbar_back_btn()

    def test_05_send_print_job(self):
        """
        Send print job for the local printer.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14061838
        """
        self.fc.select_a_printer(self.p)
        self.home.select_print_documents_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=300)
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

        hostname = self.p.get_printer_information()["host name"][:-1]
        self.print.select_printer(hostname)

        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_06_check_print_from_activity_center_bell(self):
        """
        Click bell icon
        Click "Print" option under the bell 

        Verify the print job status does not appear in the Activity Center.
        Verify Remote Print Activity Center opens.
        Verify the Activity Center shows with "No Print activity available"

        https://hp-testrail.external.hp.com/index.php?/cases/view/14061838
        https://hp-testrail.external.hp.com/index.php?/cases/view/17212350
        https://hp-testrail.external.hp.com/index.php?/cases/view/17212323
        https://hp-testrail.external.hp.com/index.php?/cases/view/13891868
        https://hp-testrail.external.hp.com/index.php?/cases/view/14061886
        """
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_print_listview()
        self.activity_center.verify_print_flyout_without_job()

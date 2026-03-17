import pytest
from time import sleep
import random

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_08_Print_From_Scan_Remote(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.scan = cls.fc.fd["scan"]
        cls.activity_center = cls.fc.fd["activity_center"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    @pytest.fixture()
    def restore_remote_printer_state(self):
        launch_activity, close_activity = self.fc.get_activity_parameter() 
        self.driver.restart_app(launch_activity, close_activity)
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_status_text(timeout=120)
        self.home.verify_carousel_printer_security_text()

    def test_01_add_remote_printer(self):
        """
        Precondition - Login in HP Account and add the claimed remote printer to Main Page.
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()

    def test_02_print_from_scan_result_screen_remote(self):
        """
        In App Print Dialog(IPP)_Print in Scan Happy Path 
        [POTG not enable, PA enabled] Send a print job to a remote printer, verify legacy remote print experience is seen	
        Import an image from Scan screen and print, verify functionality
        

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064063
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27894527
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064107
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064109
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064119
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064123
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13849421
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27959505
        """
        self.home.select_scan_tile()
        self.scan.verify_new_scan_auto_enhancements_dialog()
        self.scan.click_get_started_btn()
        self.scan.verify_couldnt_connect_to_scanner_screen()

        self.scan.select_import_btn()
        self.scan.verify_import_dialog()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()

        self.scan.click_print_btn()
        self.print.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.print.verify_creating_preview_text(timeout=45, invisible=True)

        quality_list = ['normal', 'best', 'draft']
        self.print.change_ipp_print_quality(random.choice(quality_list))
        self.print.verify_ipp_print_screen_print_btn()
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()

        self.print.verify_sending_file_dialog()
        self.print.verify_file_send_dialog(timeout=300)
        self.print.select_file_sent_dialog_job_status_btn()
        self.activity_center.verify_print_flyout_with_job()
        self.activity_center.click_close_btn()
        self.scan.verify_scan_result_screen()

    def test_03_cancel_on_sending_file_screen(self, restore_remote_printer_state):
        """
        (+) Start a cloud print job from Print Documents, verify 'Getting Remote Printer Status' with loading icon
        Click Print button from Print Documents screen, verify 'Sending File' dialogue appears	
        Click Cancel Print button on "Sending File" dialog, verify "Print job canceled" dialog shows
        Click Cancel Print button on "Sending File" dialog, verify "Print job canceled" dialog shows	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064111
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064115
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064117
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/22484591
        """
        self.home.select_scan_tile()
        self.scan.verify_couldnt_connect_to_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)

        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()

        self.scan.click_print_btn()
        self.print.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.print.verify_creating_preview_text(timeout=45, invisible=True)
        self.print.verify_ipp_print_screen_print_btn()
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()

        self.print.verify_sending_file_dialog()
        self.print.select_dialog_cancel_btn()
        self.print.verify_print_job_canceled_dialog()
        self.print.select_dialog_ok_btn()
        self.print.verify_ipp_print_screen()


            
        


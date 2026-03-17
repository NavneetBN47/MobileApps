import pytest
from time import sleep
import random

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_07_Print_Photos_Remote(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
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
        self.fc.restart_hp_smart()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_status_text(timeout=120)
        self.home.verify_carousel_printer_security_text()


    def test_01_add_remote_printer(self):
        """
        In App Print Dialog(IPP)_Print Photo Happy Path
        [POTG not enable, PA enabled] Send a print job to a remote printer, verify legacy remote print experience is seen	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064114
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27894527
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()

    def test_02_check_back_flow(self):
        """
        Click the back arrow from print photo preview, verify user returns to Main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064120
        """
        self.__start_a_remote_print_via_print_photos(w_const.TEST_DATA.WOMAN_BMP)
        self.home.select_navbar_back_btn()

    def test_03_check_sending_file_dialog(self, restore_remote_printer_state):
        """
        Click Print button from Photo Preview screen, verify 'sending file' dialogue appears
        Click Cancel print button from Photo Preview screen, verify "Print job canceled" dialog displays
        Click "OK" button on "Print job canceled" dialog, verify user returns to print screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064127
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064131
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/24409845
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064606
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/24409843
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27959505
        """
        self.__start_a_remote_print_via_print_photos(w_const.TEST_DATA.AUTUMN_JPG)

        self.print.verify_ipp_print_screen_print_btn()
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(timeout=3, raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()

        self.print.verify_sending_file_dialog()
        self.print.select_dialog_cancel_btn()
        self.print.verify_print_job_canceled_dialog()
        self.print.select_dialog_ok_btn()
        self.print.verify_ipp_print_screen_photo_preview_image()

    @pytest.mark.parametrize("buttons", ["OK", "JOB_STATUS"])
    def test_04_check_file_sent_dialog(self, buttons, restore_remote_printer_state):
        """
        Click "OK" button on file sent dialogue, verify user returns to Main UI
        Click job status on file sent dialogue, verify notification center opens with correct print job status
        (+) Toggle Printer settings on Photo preview screen, verify functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064130
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064128
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064121
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064608
        """
        self.__start_a_remote_print_via_print_photos(w_const.TEST_DATA.FISH_PNG)
        quality_list = ['normal', 'best', 'draft']
        self.print.change_ipp_print_quality(random.choice(quality_list))
        self.print.verify_ipp_print_screen_print_btn()
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(timeout=3, raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()
        self.print.verify_sending_file_dialog()
         # Print Job failed dialog is handeled here : Unable to complete the print job.
        if self.print.verify_print_job_failed_dialog(raise_e=False):
            self.print.select_dialog_ok_btn()
            self.home.verify_home_screen()
        self.print.verify_file_send_dialog(timeout=120)
        if buttons == "OK":
            self.print.select_dialog_ok_btn()
        else:
            self.print.select_file_sent_dialog_job_status_btn()
            self.activity_center.verify_print_flyout_with_job()
            self.activity_center.click_close_btn()
        self.home.verify_home_screen()
        
    def test_05_print_format_error_photo(self, restore_remote_printer_state):
        """
        Print a format error photo, verify error dialogue indicating that photo format error 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14102987
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064615
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.CORRUPTED_JPEG)

        self.print.verify_file_format_error_dialog(remote_printer=True, file_path=w_const.TEST_DATA.CORRUPTED_JPEG)
        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __start_a_remote_print_via_print_photos(self, file_name):
        """
        Start a cloud print job, verify generic preview while loading file 
        (+) Start a cloud print job from Print Photo screen, verify 'Getting Remote Printer Status' with loading icon should go away within 45 seconds 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064116
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064122
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064364
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072366
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064337
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064358
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(file_name)
        self.print.verify_ipp_print_screen_no_preview_image(raise_e=False)
        self.print.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.print.verify_creating_preview_text(timeout=45, invisible=True)
        self.print.verify_ipp_print_screen_photo_preview_image()



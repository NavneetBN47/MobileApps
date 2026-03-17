import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_04_Activity_Center_Print_Remote(object):
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

        cls.file_name = w_const.TEST_DATA.ONE_PAGE_DOC

    def test_01_add_remote_printer(self):
        """
        Add a remote printer to Main UI.
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()
        if self.home.verify_smart_driver_dialog(raise_e=False):
            self.home.click_smart_driver_x_btn()

    def test_02_click_back_arrow_on_shortcut_flyout(self):
        """
        Click back arrow on the Shortcuts job status (list view) in Shortcuts Activity Center windows.
        
        Verify main UI shows.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099930
        """
        self.home.select_activity_btn()
        self.home.click_shortcuts_listview()
        self.activity_center.verify_shortcuts_dialog()
        self.activity_center.click_back_arrow()
        self.activity_center.verify_shortcuts_flyout_disappear()
        self.home.verify_home_screen()

    def test_03_check_bell_icon_print_item(self):
        """
        Click the Bell icon to open the overlay.
        Click "Print" item and check.

        Verify Activity center screen shows with "No Print activity available".

        https://hp-testrail.external.hp.com/index.php?/cases/view/13905043
        """
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_print_listview()
        self.activity_center.verify_print_flyout_without_job()
        self.activity_center.click_close_btn()
        self.home.verify_home_screen()
        assert self.activity_center.verify_connected_remote_jobs_file_created() is not False
        
    def test_04_send_a_print_job(self):
        """
        Send a print job to the remote printer.
        """
        self.__start_a_remote_print_via_print_documents(self.file_name)
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(timeout=3, raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()
        self.print.verify_sending_file_dialog()
        self.print.verify_file_send_dialog(timeout=120)
        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()

    def test_05_check_bell_icon_print_item(self):
        """
        Click the Bell icon to open the overlay.
        Click the "Print" item and check.

        Verify Activity center screen shows with the Print job status details.
        Verify the Job Printed status shown for this job on the AC.
        Verify the Print Job Processing status shows on the Activity Center for this print job.

        https://hp-testrail.external.hp.com/index.php?/cases/view/13905044
        https://hp-testrail.external.hp.com/index.php?/cases/view/14590935
        https://hp-testrail.external.hp.com/index.php?/cases/view/14590936
        """
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_print_listview()
        self.activity_center.verify_print_flyout_with_job()
        self.activity_center.verify_print_job_processing()
        self.activity_center.select_first_print_item()
        self.activity_center.verify_print_job_detail_screen(num=1)
        self.activity_center.click_close_btn()
        self.home.verify_home_screen()

    def test_06_simulate_all_print_job_status(self):
        """
        Simulate all the Job Printed status in the Activity Center.
        """
        self.activity_center.simulate_all_print_job_status()
        self.home.verify_home_screen()
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_print_listview()
        self.activity_center.verify_print_flyout_with_job(all_jobs=True)

    def test_07_select_job_printed_item(self):
        """
        Simulate a Job Printed status in the Activity Center.
        Click Bell icon and select print option to navigate to the Activity Center.
        Click on the Job Printed status to show the detais panel.

        Check UI layout, form

        https://hp-testrail.external.hp.com/index.php?/cases/view/14063522
        """
        compare_str = 'has successfully printed.'
        self.__check_each_print_job_item(5, compare_str)

    def test_08_select_error_printing_item(self):
        """
        Simulate a Error Printing status in the Activity Center.
        Click Bell icon and select print option to navigate to the Activity Center.
        Click on the Error Printing status to show the detais panel.

        Check UI layout, form

        https://hp-testrail.external.hp.com/index.php?/cases/view/14064049
        https://hp-testrail.external.hp.com/index.php?/cases/view/13905074('X with circle' icon can not check)
        """
        compare_str = 'There was an error printing'
        left_str = 'Error Printing'
        self.activity_center.verify_error_message_of_left_title(left_str, 4) 
        self.__check_each_print_job_item(4, compare_str)

    def test_09_select_job_processing_item(self):
        """
        Simulate a Print Job Processing status in the Activity Center.
        Click Bell icon and select print option to navigate to the Activity Center.
        Click on the Print Job Processing status to show the detais panel.

        Check UI layout, form

        https://hp-testrail.external.hp.com/index.php?/cases/view/14063491
        """
        compare_str = 'is being processed.  Please wait...'
        self.__check_each_print_job_item(1, compare_str)

    def test_10_select_status_unknown_item(self):
        """
        Simulate a Status Unknown status in the Activity Center.
        Click Bell icon and select print option to navigate to the Activity Center.
        Click on the Status Unknown status to show the detais panel.

        Check UI layout, form

        https://hp-testrail.external.hp.com/index.php?/cases/view/14064051
        https://hp-testrail.external.hp.com/index.php?/cases/view/14061822
        """
        compare_str = 'Status is unavailable.'
        left_str = 'Status Unknown'
        self.activity_center.verify_error_message_of_left_title(left_str, 6) 
        self.__check_each_print_job_item(6, compare_str)

    def test_11_select_job_canceled_item(self):
        """
        Simulate a Print job Canceled status in the Activity Center.
        Click Bell icon and select print option to navigate to the Activity Center.
        Click on the Print job Canceled status to show the detais panel.

        Check UI layout, form

        https://hp-testrail.external.hp.com/index.php?/cases/view/14064053
        """
        compare_str = 'was canceled.'
        self.__check_each_print_job_item(3, compare_str)

    def test_12_click_clear_notification_btn_on_each_status(self):
        """
        Click "Clear Notification" button on the details screen for
        each status (Error Printing/Status Unknown/Job Printed/Print Job Canceled).
        https://hp-testrail.external.hp.com/index.php?/cases/view/14061830 
        """       
        for _ in range(10):
            if self.activity_center.select_print_job_item(3, raise_e=False):
                self.activity_center.click_clear_notification_btn()
                sleep(2)
        assert self.activity_center.select_print_job_item(3, raise_e=False) is False

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __start_a_remote_print_via_print_documents(self, file_name):
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(file_name)
        self.print.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.print.verify_creating_preview_text(timeout=45, invisible=True)
        self.print.verify_ipp_print_screen_document_preview_image()

    def __check_each_print_job_item(self, num, compare_str):
        self.activity_center.select_print_job_item(num)
        self.activity_center.verify_print_job_detail_screen(num)
        detail_text = self.activity_center.get_detail_job_text()
        assert compare_str in detail_text
        if num not in [1, 3]:
            detail_text_2 = self.activity_center.get_detail_job_text_2()       
            assert 'day' in detail_text_2
        self.activity_center.click_detail_back_arrow()
        self.activity_center.verify_print_flyout_with_job(all_jobs=True)
        
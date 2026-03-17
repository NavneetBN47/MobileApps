import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_05_Activity_Center_Background(object):
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

    def test_02_create_and_edit_connected_remote_jobs_file(self):
        """
        Create ConnectedRemoteJobs.xml in LocalState folder
        """
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_print_listview()
        self.activity_center.verify_print_flyout_without_job()
        self.activity_center.click_back_arrow()
        self.home.verify_home_screen()
        assert self.activity_center.verify_connected_remote_jobs_file_created() is not False
        
    def test_03_simulate_all_print_job_status(self):
        """
        Simulate all the Job Printed status in the Activity Center.
        """
        self.activity_center.simulate_all_print_job_status()
        self.home.verify_home_screen()
        sleep(3)
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_print_listview()
        self.activity_center.verify_print_flyout_with_job(all_jobs=True)

    def test_04_check_each_item_different_states(self):
        """
        Print status:
            Print Job Processing status
            Job Printed status
            Error Printing status
            Status Unknown status
            Print job Canceled status
        
        Check each list view when not selected/hover/selected/selected with hover.

        Verify there will be no background color and Font color is black when not selected.
        Verify Icon background was changed to grey and font color was black when hover. (not covered)
        Verify Icon background was changed to dark grey and font color was black when hover and select. (not covered)
        Verify icon background changes to darker blue when selected.
        Verify "X" icon doesn't shows for "Print Job Processing" and shows for "Job Printed"/"Error Printing"/"Status Unknown"/"Print job Canceled" when selected.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14590937
        https://hp-testrail.external.hp.com/index.php?/cases/view/17212324
        """
        sel_list = ["s_job_pro.png", "s_job_can.png", "s_error_pri.png", "s_job_pri.png", "s_status_unk.png"]
        value_org = self.fc.check_element_background("status_list_view", 'activity_center', "print_org.png", value=0.3)
        logging.info("hover vs org: {}".format(value_org))
        assert value_org < 0.01
        
        for i in range(2, 7):
            self.activity_center.select_print_job_item(i)
            sleep(1)
            self.activity_center.click_back_arrow()
            sleep(1)
            value_org = self.fc.check_element_background("status_list_view", 'activity_center', "print_org.png", value=0.3)
            logging.info("select vs org: {}".format(value_org))
            assert value_org > 0.05
            value_sel = self.fc.check_element_background("status_list_view", 'activity_center', sel_list[i-2], value=0.3)
            logging.info("select vs select: {}".format(value_sel))
            assert value_sel < 0.015
            sleep(2)

    def test_05_check_date_info_on_job_status(self):
        """
        Verify the day information display in list view when job was sent and retain for 1 week after being sent from app. Dates are: Today, Day, Yesterday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
        Verify if the status pass 1 week than it should disappear from the list

        https://hp-testrail.external.hp.com/index.php?/cases/view/13905054
        """
        day_list = ["Today", "Yesterday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Thursday", "7 days ago"]
        for i in range(1, 10):
            day_text = self.activity_center.get_job_day_info(i)
            assert day_text in day_list


            

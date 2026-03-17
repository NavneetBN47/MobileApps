from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
import MobileApps.resources.const.windows.const as w_const
import time
import re
import pytest

class SignInRequiredException(Exception):
    pass


class ActivityCenter(GothamFlow):
    flow_name = "activity_center"
    connected_remote_jobs_file = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\\ConnectedRemoteJobs.xml'

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_shortcut_completed_item(self, num=1, raise_e=True):
        return self.driver.click("dynamic_shortcut_completed_item", format_specifier=[num], raise_e=raise_e)

    def click_print_item(self):
        self.driver.click("print_item")

    def click_back_arrow(self):
        self.driver.click("back_btn")

    def click_del_btn(self):
        return self.driver.click("delete_button", raise_e=False)

    def click_close_btn(self):
        self.driver.click("close_btn")

    def click_clear_notification_btn(self):
        self.driver.click("clear_notification")

    def select_first_print_item(self):
        self.driver.click("first_print_item")

    def select_print_job_item(self, job_count, raise_e=True):
        """
        - 1: Print Job Processing...
        - 2: Print Job Processing...
        - 3: Print Job Canceled
        - 4: Error Printing
        - 5: Job Printed
        - 6: Status Unknown
        - 7: Error Printing
        - 8: Error Printing
        - 9: Error Printing
        """
        return self.driver.click("dynamic_print_job_status_item", format_specifier=[job_count], raise_e=raise_e)

    def get_job_day_info(self, num):
        """
        Verify the print job status appears in the Activity Center.

        - 1: Print Job Processing...
        - 2: Print Job Processing...
        - 3: Print Job Canceled
        - 4: Error Printing
        - 5: Job Printed
        - 6: Status Unknown
        - 7: Error Printing
        - 8: Error Printing
        - 9: Error Printing
        """
        if num == 6:
            return self.driver.get_attribute("dynamic_job_status_day_text_2", format_specifier=[num], attribute="Name")
        else:
            return self.driver.get_attribute("dynamic_job_status_day_text", format_specifier=[num], attribute="Name")
   
    def click_detail_back_arrow(self):
        self.driver.click("job_detail_back_button")

    def get_detail_job_text(self):
        return self.driver.get_attribute("print_job_detail_text", attribute="Name")
    
    def get_detail_job_text_2(self):
        return self.driver.get_attribute("print_job_detail_text_2", attribute="Name")
            
    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_shortcuts_dialog(self):
        self.driver.wait_for_object("back_btn", timeout=20)
    
    def verify_shortcuts_flyout_disappear(self):
        """
        Verify shortcuts flyout does not appear.
        """
        assert self.driver.wait_for_object("shortcuts_dialog", raise_e=False) is False

    def verify_shortcuts_item_added(self):
        self.driver.wait_for_object("back_btn", timeout=20)
        self.driver.wait_for_object("shortcut_completed_today_item")

    def verify_no_shortcut_item_added(self, timeout=5, raise_e=False):
        return self.driver.wait_for_object("no_shortcut_text", timeout=timeout, raise_e=raise_e)

    def verify_shortcut_completed_dialog(self):
        self.driver.wait_for_object("delete_button")

    def verify_print_sent_dialog(self):
        self.driver.wait_for_object("print_sent_title")

    def verify_shortcuts_deleted(self):
        return self.driver.wait_for_object("delete_button", raise_e=False)

    def verify_my_account_screen(self):
        """
        My Account screen: View Notifications
        """
        self.driver.wait_for_object("my_account_title", timeout=25)
        self.driver.wait_for_object("view_notifications_text", timeout=25)

    def verify_print_activity_center_flyout(self, timeout=20, raise_e=True):
        """
        Verify Print Activity Center flyout load
        """
        return self.driver.wait_for_object("print_activity_center_flyout_title", timeout=timeout, raise_e=raise_e)

    def verify_print_flyout_without_job(self):
        """
        Verify the print job status does not appear in the Activity Center.
        """
        self.verify_print_activity_center_flyout()
        self.driver.wait_for_object("print_image")
        self.driver.wait_for_object("no_print_activity_available_text")
        self.driver.wait_for_object("send_a_file_text")

    def verify_print_flyout_with_job(self, all_jobs=False):
        """
        Verify the print job status appears in the Activity Center.

        - 1: Print Job Processing...
        - 2: Print Job Processing...
        - 3: Print Job Canceled
        - 4: Error Printing
        - 5: Job Printed
        - 6: Status Unknown
        - 7: Error Printing
        - 8: Error Printing
        - 9: Error Printing
        """
        self.verify_print_activity_center_flyout()
        self.driver.wait_for_object("status_list_view")
        if all_jobs:
            for i in range (1,10):
                self.driver.wait_for_object("dynamic_print_job_status_item", format_specifier=[i])

    def verify_print_job_processing(self, raise_e=True, timeout=30):
        """
        Verify the Print Job Processing status shows on the Activity Center for this print job.
        """
        self.driver.wait_for_object("print_job_processing_status_text", raise_e=raise_e, timeout=timeout)

    def verify_print_job_detail_screen(self, num):
        """
        Verify the print job status appears in the Activity Center.

        - 1: Print Job Processing... (no Clear Notification button)
        - 2: Print Job Processing... (no Clear Notification button)
        - 3: Print Job Canceled
        - 4: Error Printing
        - 5: Job Printed
        - 6: Status Unknown
        - 7: Error Printing
        - 8: Error Printing
        - 9: Error Printing
        """
        self.driver.wait_for_object("print_job_detail_image")
        if num in [1,2]:
            assert self.driver.wait_for_object("clear_notification", raise_e=False) is False
        else:
            self.driver.wait_for_object("clear_notification")

    def verify_shortcut_running_item_display(self, timeout=30):
        self.driver.wait_for_object("shortcut_running_item", timeout=timeout)

    # ***********************************************************************************************
    #              find all supported remote printing message notifications                                      *
    # ***********************************************************************************************
    def verify_connected_remote_jobs_file_created(self):
        return self.driver.ssh.send_command('Test-Path -path "{}"'.format(self.connected_remote_jobs_file), raise_e=False)

    def simulate_all_print_job_status(self):
        if pytest.app_info != "DESKTOP":
            launch_activity = close_activity = None
        else:
            launch_activity = eval("w_const.LAUNCH_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
            close_activity = eval("w_const.CLOSE_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
        if (fh := self.driver.ssh.remote_open(self.connected_remote_jobs_file, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            data = re.sub("<Flags>0</Flags>", "<Flags>7</Flags>", data)
            fh = self.driver.ssh.remote_open(self.connected_remote_jobs_file, mode="w")
            fh.write(data)
            fh.close()
            time.sleep(1)
            self.driver.terminate_app(close_activity)
            time.sleep(3)
            self.driver.launch_app(launch_activity)
            time.sleep(3)

    def verify_error_message_of_left_title(self, str, num):
        assert str in self.driver.get_attribute("dynamic_print_job_status_item", format_specifier=[num], attribute="Name")
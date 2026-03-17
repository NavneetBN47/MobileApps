import pytest
from datetime import datetime
from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow


class ShortcutsNotification(SmartFlow):
    flow_name = "shortcuts_notification"

    def verify_shortcuts_list_from_notification(self, timeout=15):
        """
        Verify current screen is Shortcuts list screen
        """
        self.driver.wait_for_object("shortcuts_title", timeout=timeout)
        self.driver.wait_for_object("shortcuts_list")

    def verify_no_shortcut_activity_available_msg(self, timeout=15):
        """
        Verify current screen is Shortcuts empty list screen
        """
        self.driver.wait_for_object("no_shortcut_activity_available_msg", timeout=timeout)
    
    def verify_job_status(self, job_number, job_status, raise_e=True):
        """
        Verify job status by job number
        """
        try:
            if pytest.platform == "MAC":
                assert self.driver.get_attribute("job_status_by_number", "text", format_specifier=[(job_number - 1) * 5 + 2]) == job_status
            else:
                assert self.driver.get_attribute("job_status_by_number", "text", format_specifier=[job_number]) == job_status
        except AssertionError:
            if raise_e:
                raise AssertionError(f"Job status '{job_status}' is not matched.")
            return False
        return True

    def verify_job_name(self, job_number, job_name):
        """
        Verify job name by job number
        """
        if pytest.platform == "MAC":
            assert self.driver.get_attribute("job_name_by_number", "text", format_specifier=[job_number * 5]) == job_name
        else:
            assert self.driver.get_attribute("job_name_by_number", "text", format_specifier=[job_number]) == job_name
    
    def verify_job_date(self, job_number, job_name):
        """
        Verify job name by job number
        """
        if pytest.platform == "MAC":
            assert self.driver.get_attribute("job_date_by_number", "text", format_specifier=[(job_number - 1) * 5 + 3]) == job_name
        else:
            assert self.driver.get_attribute("job_date_by_number", "text", format_specifier=[job_number]) == job_name
    
    def verify_job_status_date_and_name_by_number(self, job_number, job_status, job_name, job_date):
        """
        Verify job status and name by job number
        """
        self.verify_job_name(job_number, job_name)
        self.verify_job_status(job_number, job_status)
        self.verify_job_date(job_number, job_date)

    def verify_shortcut_complete_screen(self):
        """
        Verify current screen is Shortcuts complete screen
        """
        self.driver.wait_for_object("shortcut_completed_screen_title")
        self.driver.wait_for_object("shortcut_completed_screen_delete_btn")
    
    def verify_email_sent_screen(self):
        """
        Verify current screen is Email sent screen
        """
        self.driver.wait_for_object("email_sent_screen_title")
        self.driver.wait_for_object("email_sent_screen_success_message")

    def verify_print_sent_screen(self):
        """
        Verify current screen is Print sent screen
        """
        self.driver.wait_for_object("print_sent_screen_title")
    
    def verify_job_name_and_date_on_print_sent_screen(self, job_name):
        """
        Verify job name and date on Print sent screen
        """
        assert self.driver.get_attribute("job_name_on_print_sent_screen", "text") == job_name
        assert f"{datetime.now().strftime('%B')} {datetime.now().day}" in self.driver.get_attribute("job_date_on_print_sent_screen", "text")

    def navigate_back(self):
        """
        Navigate back to Notification screen
        """
        self.driver.click("navigate_back_btn")
    
    def select_job_by_number(self, job_number):
        """
        Select job by job number
        """
        if pytest.platform == "MAC":
            self.driver.click("job_name_by_number", format_specifier=[job_number * 5])
        else:
            self.driver.click("job_name_by_number", format_specifier=[job_number])
    
    def select_email_completed_item(self):
        """
        Select Email Completed item
        """
        self.driver.click("shortcut_completed_screen_email_item")
    
    def select_print_completed_item(self):
        """
        Select Email Completed item
        """
        self.driver.click("shortcut_completed_screen_print_item")
    
    def select_delete_button(self):
        """
        Select Delete button on Shortcut Complete screen
        """
        self.driver.click("shortcut_completed_screen_delete_btn")

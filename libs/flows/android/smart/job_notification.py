from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow

class JobNotification(SmartFlow):

    flow_name = "job_notification"

    ###################################################################
    #                  Action Flows                                   #
    ###################################################################

    def select_print_notification_by_printer_name(self, printer_name, timeout=20):
        """
        selects the job notification by pritner name
        :param printer_name:
        """
        if self.driver.wait_for_object("print_job_notification", format_specifier=[printer_name], timeout=timeout, raise_e=False):
            self.driver.click("print_job_notification", format_specifier=[printer_name])
        else:
            # Sometimes, only Printing message shows on notification list
            self.driver.click("printing_notification", format_specifier=[self.get_text_from_str_id("printing_txt")])

    def verify_print_job_on_the_list(self):
        """
        Verify print job shows on Print Jobs list screen
        """
        self.driver.wait_for_object("job_cell")
        self.driver.wait_for_object("file_name")

    def select_cancel_btn(self):
        """
        click the Cancel button to cancel the jobs that are selected
        """
        self.driver.click("cancel_btn")

    def select_delete_btn(self):
        """
        click the Delete button to delete the jobs that are selected
        """
        self.driver.click("delete_btn")

    ###################################################################
    #                  Action Flows                                   #
    ###################################################################

    def verify_print_jobs_screen(self):
        """
        verify print jobs screen is displayed
        :return:
        """
        self.driver.wait_for_object("print_jobs_title")
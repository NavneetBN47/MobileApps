from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow


class TextNotifications(SmartFlow):
    flow_name = "text_notifications"

    def verify_text_file_job(self, file_name=None, invisible=False, timeout=30):
        """
        Verifies that the specified file_name appears in the Text File notifications screen
        :param file_name: The file name of the text job to verify. If none the first text file job will be selected.
        :param invisible: True -> Verify the text job does not exist. False -> Verify the text job exists and wait for completion.
        :param timeout: Seconds to wait for job to complete(status text appears)
        :return: The text job's id. returns -1 if invisible==True
        """
        text_job = self.driver.wait_for_object("text_file_job_txt", format_specifier=[] if file_name is None else [file_name], invisible=invisible)
        if invisible == False:
            job_number = text_job.get_attribute("id").replace("jobName", "")
            self.driver.wait_for_object("text_file_job_status_txt", format_specifier=[job_number], timeout=timeout)
            return job_number
        return -1

    def verify_text_file_job_options(self):
        """
        Verifies the options from a text file job's 3-dot menu
         - share button
         - download button
         - delete button
        """
        self.driver.wait_for_object("text_file_job_share_btn")
        self.driver.wait_for_object("text_file_job_download_btn")
        self.driver.wait_for_object("text_file_job_delete_btn")

    def verify_text_files_screen(self):
        """
        Verifies the text files screen with
         - title
         - "files are accessible for 30 days" sub header
        """
        self.driver.wait_for_object("text_files_title_txt")
        self.driver.wait_for_object("text_files_accessibility_txt")

class TextNotificationsAndroid(TextNotifications):

    def select_text_file_job_3dot_button(self, file_name=None, timeout=40):
        """
        Selects the 3-dots button on a text file job
        :param file_name: The name of the text file job to select the 3-dot button on. If unspecified selects the first text file 
            job's button.
        :param timeout: Time in seconds to find 3dot button.
        """
        job_number = self.verify_text_file_job(file_name=file_name)
        self.driver.click("text_file_job_btn", format_specifier=[job_number], timeout=timeout)

    def select_text_file_job_button(self, btn):
        """
        Selects the a button on a text file job's 3-dots menu.
        :param btn: The button on the text file job's 3-dots menu to select. Possible values: "share", "download", "delete"
        """
        self.driver.click("text_file_job_{}_btn".format(btn))

    def verify_errored_text_file_job(self):
        """
        Verifies an errored text file job if any are present on the screen
         - error status text
         - failure image
        """
        if self.driver.wait_for_object("text_file_job_status_txt", raise_e=False) is False:
            return False
        error_str = self.driver.return_str_id_value_from_id("status_msg_error")
        text_jobs = [e for e in self.driver.find_object("text_file_job_status_txt", multiple=True) if e.text.startswith(error_str)]
        if len(text_jobs) == 0:
            return False
        errored_job_id = text_jobs[0].get_attribute("id").replace("jobStatus", "")
        self.driver.find_object("text_file_job_failure_icon", format_specifier=[errored_job_id])
        return True

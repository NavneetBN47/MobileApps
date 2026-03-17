from datetime import datetime
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Notifications(SmartFlow):
    flow_name = "notifications"

########################################################################################################################                                                                                                                 #
#                                              ACTION  FLOWS                                                           #                                                                                                                   #
########################################################################################################################

    def select_first_notification(self):
        """
        Click on the first notification
        End of flow: Notification Details
        Device: Phone, Tablet
        """
        self.driver.click("first_notification_btn")

    def select_notifications_by_title(self, notification_title):
        """
        Select the notification from the Notifications list
        """
        self.driver.click(notification_title)

    def select_settings_icon(self):
        """
        Click on Settings button from Notification screen
        """
        self.driver.click("settings_opt")

    def select_print_button(self):
        """
        Click on Print button from Notification screen
        """
        self.driver.click("print_btn")

    def select_mobile_fax_button(self):
        """
        Click on Mobile Fax button from Notification screen
        """
        self.driver.click("mobile_fax_btn")

    def select_account_button(self):
        """
        Click on Account button from Notification screen
        """
        self.driver.click("account_btn")

    def select_supplies_button(self):
        """
        Click on Supplies button from Notification screen
        """
        self.driver.click("supplies_btn")

    def select_shortcuts_button(self):
        """
        Click on Shortcuts button from Notification screen
        """
        self.driver.click("shortcuts_btn")

    def select_print_job_by_number(self, job_number=1):
        """
        Click on Print job by number
        """
        self.driver.click("print_job_by_number", format_specifier=[job_number])
    
    def select_clear_notification_btn(self):
        """
        Click on Clear Notification button on Job Printed screen
        """
        self.driver.click("clear_notification_button")
    
    def get_printed_file_name(self):
        """
        Get the name of the printed file
        """
        return self.driver.get_attribute("printed_job_name", "text")
    ########################################################################################################################                                                                                                                #
    #                                                  Verification Flows                                                                                                                    #
    ########################################################################################################################

    def verify_notifications_screen(self):
        """
        Verify Notification Screen via:
            - Notification title
        """
        self.driver.wait_for_object("notifications_title")

    def verify_no_printer_selected_screen(self):
        """
        Verify No printer selected Screen via:
            - No printer selected title
            - Add printer to get current information on print job message
        """
        self.driver.wait_for_object("no_printer_selected")
        self.driver.wait_for_object("add_printer_message")

    def verify_no_print_activity_available_screen(self):
        """
        Verify No Print activity available Screen via:
            - title
            - Send a file to your printer messag
        """
        self.driver.wait_for_object("no_printer_activity_title")
        self.driver.wait_for_object("send_file_to_your_printer_message")
    
    def verify_completed_status_on_print_screen(self, timeout=10, raise_e=True):
        """
        Verify Completed status on Print Screen via:
            - Job Printed status
        """
        return self.driver.wait_for_object("job_printed_status", timeout=timeout, raise_e=raise_e)
    
    def verify_job_completed_on_print_screen(self, timeout=10):
        """
        Verify Job Completed on Print Screen via:
            - Job Printed status
            - Green Checkmark
        """
        self.verify_completed_status_on_print_screen(timeout=timeout)
        self.driver.wait_for_object("print_job_completed_checkmark")
    
    def verify_job_printed_screen(self):
        """
        Verify Job Printed Screen via:
            - Job Printed title
        """
        self.driver.wait_for_object("job_printed_screen_title")
    
    def verify_job_printed_screen_date_and_job_name(self, job_name):
        """
        Verify Job Printed screen shows with correct info:
            - Name of the printed file
            - Correct date
        """
        text = self.driver.get_attribute("job_date_and_name_on_job_printed_screen", "text")
        assert job_name in text
        assert f"{datetime.now().strftime('%B')} {datetime.now().day}" in text
    
    def hpx_notification_close_btn(self):
        """
        Click on Close button on Notification screen
        """
        self.driver.click("close_btn")
    
    def verify_hpx_notification_screen(self):
        """
        Verify HPX Notification Screen via:
            - HPX Notification title
        """
        return self.driver.wait_for_object("hpx_notification_title")
    
    def verify_hpx_notification_print_txt(self):
        """
        Verifies the print text
        """
        return self.driver.wait_for_object("hpx_print",timeout=5)
    
    def verify_hpx_notification_mobile_fax_txt(self):
        """
        Verifies the mobile fax text
        """
        return self.driver.wait_for_object("hpx_mobile_fax",timeout=5)
    
    def verify_hpx_notification_shortcuts_txt(self):
        """
        Verifies the shortcuts text
        """
        return self.driver.wait_for_object("hpx_shortcuts",timeout=5)
    
    def verify_hpx_notification_supplies_txt(self):
        """
        Verifies the supplies text
        """
        return self.driver.wait_for_object("hpx_supplies",timeout=5)
    
    def verify_hpx_notification_account_txt(self):
        """
        Verifies the account text
        """
        return self.driver.wait_for_object("hpx_account",timeout=5)
    
    def verify_hpx_mobilefax_draft_txt(self):
        """
        Verifies the draft notification text
        """
        return self.driver.wait_for_object("hpx_draft_notification",timeout=5)

    def verify_hpx_mobilefax_sent_txt(self):
        """
        Verifies the sent notification text
        """
        return self.driver.wait_for_object("hpx_sent_notification",timeout=5)

    def verify_hpx_fax_history_notification_screen_title(self):
        """
        Verify HPX Notification Screen via:
            - HPX Mobile fax Notification title
        """
        return self.driver.wait_for_object("hpx_fax_history_notification_title")

    def verify_hpx_on_supplies_notification_screen_title(self):
        """
        Verify HPX Notification Screen via:
            - HPX Supplies Notification title
        """
        return self.driver.wait_for_object("hpx_on_supplies_page")

    def verify_hpx_on_supplies_page_close_btn(self):
        """
        Verify HPX Notification Screen via:
            - HPX supplies Notification title
        """
        return self.driver.wait_for_object("hpx_on_supplies_page_close_btn")

    def verify_hpx_on_printer_page(self):
        """
        Verify HPX Notification Screen via:
            - HPX Printer Notification title
        """
        return self.driver.wait_for_object("hpx_on_printer_page")

    def verify_hpx_on_printer_page_no_printer_selected(self):
        """
        Verify HPX Notification Screen via:
            - HPX Printer Notification title
        """
        return self.driver.wait_for_object("hpx_on_printer_page_no_printer_selected")

    def verify_hpx_page_on_product_information_card(self):
        """
        Verify HPX Notification Screen via:
            - HPX Product Information Card title
        """
        return self.driver.wait_for_object("hpx_product_information_card")
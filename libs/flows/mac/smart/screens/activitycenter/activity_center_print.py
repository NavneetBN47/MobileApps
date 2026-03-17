# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for Activity Center Fly-out.

@author: Ivan
@create_date: Jan 20, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ActivityCenterPrint(SmartScreens):

    folder_name = "activitycenter"
    flow_name = "activity_center_print"

    def __init__(self, driver):
        super(ActivityCenterPrint, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Activity Center Print page shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_activity_center_print_status", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_status_unknown(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Activity Center Print page shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[wait_for_screen_load_status_unknown]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_activity_center_print_status_status_unknown", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_error_printing(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Activity Center Print page shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[wait_for_screen_load_error_printing]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_activity_center_print_status_error_printing", timeout=timeout, raise_e=raise_e)

    def wait_for_no_print_activity_available_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait No Print Activity Available page shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[wait_for_no_print_activity_available_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_print_activity_available_image", timeout=timeout, raise_e=raise_e)

    def wait_for_print_activity_center_status_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Print Activity Center Status screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[wait_for_print_activity_center_status_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("status_image", timeout=timeout, raise_e=raise_e)

    def click_print_activity_center_close_btn(self):
        '''
        This is a method to click Close button on Print Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_no_print_activity_available_close_btn]-Click Close button... ")

        self.driver.click("print_activity_center_close_btn", is_native_event=True)

    def click_print_activity_center_minimize_btn(self):
        '''
        This is a method to click Minimize button on Print Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_minimize_btn]-Click Minimize button... ")

        self.driver.click("print_activity_center_minimize_btn", is_native_event=True)

    def click_print_activity_center_cancel_btn(self):
        '''
        This is a method to click Cancel button on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_cancel_btn]-Click Cancel button... ")

        self.driver.click("status_cancel_btn", is_native_event=True)

    def click_print_activity_center_clear_noticification_btn(self):
        '''
        This is a method to click Clear Notification button on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_clear_noticification_btn]-Click Clear Notification button... ")

        self.driver.click("status_clear_notification_btn", is_native_event=True)

    def click_print_activity_center_delete_btn(self):
        '''
        This is a method to click Delete button on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_delete_btn]-Click Delete button... ")

        self.driver.click("print_activity_center_delete_btn", is_native_event=True)

    def click_print_activity_center_print_status(self):
        '''
        This is a method to click Status Text on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_print_status]-Click Status Text... ")

        self.driver.click("print_activity_center_print_status", is_native_event=True)

    def click_print_activity_center_print_status_job_printed(self):
        '''
        This is a method to click Job Printed Text on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_print_status__job_printed]-Click Status Text... ")

        self.driver.click("print_activity_center_print_status_job_printed", is_native_event=True)

    def click_print_activity_center_print_status_status_unknown(self):
        '''
        This is a method to click Status Unknown Text on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_print_status_status_unknown]-Click Status Text... ")

        self.driver.click("print_activity_center_print_status_status_unknown", is_native_event=True)

    def click_print_activity_center_print_status_error_printing(self):
        '''
        This is a method to click Error Printing Text on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_print_activity_center_print_status_error_printing]-Click Status Text... ")

        self.driver.click("print_activity_center_print_status_error_printing", is_native_event=True)

    def get_value_of_no_print_activity_available_title(self):
        '''
        This is a method to get value of title for No Print Activity Available page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_no_print_activity_available_title]-Get the value of title ...  ")

        return self.driver.get_value("no_print_activity_available_title")

    def get_value_of_no_print_activity_available_content_1(self):
        '''
        This is a method to get value of content - 1 for No Print Activity Available page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_no_print_activity_available_content_1]-Get the value of content - 1 ...  ")

        return self.driver.get_value("no_print_activity_available_content_1")

    def get_value_of_no_print_activity_available_content_2(self):
        '''
        This is a method to get value of content - 2 for No Print Activity Available page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_no_print_activity_available_content_2]-Get the value of content - 2 ...  ")

        return self.driver.get_value("no_print_activity_available_content_2")

    def get_value_of_print_activity_center_print_status(self):
        '''
        This is a method to get value of Status on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_print_status]-Get the value of Status ...  ")

        return self.driver.get_value("print_activity_center_print_status")

    def get_value_of_print_activity_center_file_name(self):
        '''
        This is a method to get value of File Name on Status page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_file_name]-Get the value of File Name ...  ")

        return self.driver.get_value("print_activity_center_file_name")

    def get_value_of_print_activity_center_date(self):
        '''
        This is a method to get value of Date on Status page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_date]-Get the value of Date ...  ")

        return self.driver.get_value("print_activity_center_date")

    def get_value_of_print_activity_center_print_status_job_printed(self):
        '''
        This is a method to get value of Status on Print Activity Center page - Job Printed.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_print_status_job_printed]-Get the value of Status ...  ")

        return self.driver.get_value("print_activity_center_print_status_job_printed")

    def get_value_of_print_activity_center_file_name_job_printed(self):
        '''
        This is a method to get value of File Name on Status page - Job Printed.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_file_name_job_printed]-Get the value of File Name ...  ")

        return self.driver.get_value("print_activity_center_file_name_job_printed")

    def get_value_of_print_activity_center_date_job_printed(self):
        '''
        This is a method to get value of Date on Status page - Job Printed.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_date_job_printed]-Get the value of Date ...  ")

        return self.driver.get_value("print_activity_center_date_job_printed")

    def get_value_of_print_activity_center_print_status_status_unknown(self):
        '''
        This is a method to get value of Status on Print Activity Center page - Status Unknown.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_print_status_status_unknown]-Get the value of Status ...  ")

        return self.driver.get_value("print_activity_center_print_status_status_unknown")

    def get_value_of_print_activity_center_file_name_status_unknown(self):
        '''
        This is a method to get value of File Name on Status page - Status Unknown.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_file_name_status_unknown]-Get the value of File Name ...  ")

        return self.driver.get_value("print_activity_center_file_name_status_unknown")

    def get_value_of_print_activity_center_date_status_unknown(self):
        '''
        This is a method to get value of Date on Status page - Status Unknown.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_date_status_unknown]-Get the value of Date ...  ")

        return self.driver.get_value("print_activity_center_date_status_unknown")

    def get_value_of_print_activity_center_print_status_error_printing(self):
        '''
        This is a method to get value of Status on Print Activity Center page - Error Printing.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_print_status_error_printing]-Get the value of Status ...  ")

        return self.driver.get_value("print_activity_center_print_status_error_printing")

    def get_value_of_print_activity_center_file_name_error_printing(self):
        '''
        This is a method to get value of File Name on Status page - Error Printing.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_file_name_error_printing]-Get the value of File Name ...  ")

        return self.driver.get_value("print_activity_center_file_name_error_printing")

    def get_value_of_print_activity_center_date_error_printing(self):
        '''
        This is a method to get value of Date on Status page - Error Printing.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_print_activity_center_date_error_printing]-Get the value of Date ...  ")

        return self.driver.get_value("print_activity_center_date_error_printing")

    def get_value_of_status_content_1(self):
        '''
        This is a method to get value of content - 1 for Status on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_content_1]-Get the value of content - 1 ...  ")

        return self.driver.get_value("status_content_1")

    def get_value_of_status_content_2(self):
        '''
        This is a method to get value of content - 2 for Status on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_content_2]-Get the value of content - 2 ...  ")

        return self.driver.get_value("status_content_2")

    def get_value_of_status_content_3(self):
        '''
        This is a method to get value of content - 3 for Status on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_content_3]-Get the value of content - 3 ...  ")

        return self.driver.get_value("status_content_3")

    def get_value_of_status_content_4(self):
        '''
        This is a method to get value of content - 4 for Status on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_content_4]-Get the value of content - 4 ...  ")

        return self.driver.get_value("status_content_4")

    def get_value_of_status_content_5(self):
        '''
        This is a method to get value of content - 5 for Status on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_content_5]-Get the value of content - 5 ...  ")

        return self.driver.get_value("status_content_5")

    def get_value_of_status_details_date(self):
        '''
        This is a method to get value of Details Date text on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_details_date]-Get the value of Details Date text ...  ")

        return self.driver.get_title("status_details_date")

    def get_value_of_status_cancel_btn(self):
        '''
        This is a method to get value of Cancel button on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_cancel_btn]-Get the value of Cancel button ...  ")

        return self.driver.get_title("status_cancel_btn")

    def get_value_of_status_clear_notification_btn(self):
        '''
        This is a method to get value of Clear Notification button on Print Activity Center page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_status_clear_notification_btn]-Get the value of Clear Notification button ...  ")

        return self.driver.get_title("status_clear_notification_btn")

    def click_activity_center_print_close_btn(self):
        '''
        This is a method to click Close button on Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_activity_center_print_close_btn]-Click Close button... ")

        self.driver.click("activity_center_print_close_btn", is_native_event=True)

    def click_activity_center_print_minimize_btn(self):
        '''
        This is a method to click Minimize button on Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_activity_center_print_minimize_btn]-Click Minimize button... ")

        self.driver.click("activity_center_print_minimize_btn", is_native_event=True)

    def get_value_of_activity_center_print_title(self):
        '''
        This is a method to get value of title for Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_activity_center_print_title]-Get the value of title ...  ")

        return self.driver.get_value("activity_center_print_title")

    def get_value_of_activity_center_print_content_1(self):
        '''
        This is a method to get value of content - 1 for Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_activity_center_print_content_1]-Get the value of content - 1 ...  ")

        return self.driver.get_value("activity_center_print_content_1")

    def get_value_of_activity_center_print_content_2(self):
        '''
        This is a method to get value of content - 2 for Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_activity_center_print_content_2]-Get the value of content - 2 ...  ")

        return self.driver.get_value("activity_center_print_content_2")

# -------------------------------Verification Methods-------------------------------
    def verify_activity_center_print_page(self):
        '''
        This is a verification method to check UI strings of Activity Center Print Page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Activity Center Print Page")
#         assert self.get_value_of_activity_center_print_title() == u""
#         assert self.get_value_of_activity_center_print_content_1() == u""
#         assert self.get_value_of_activity_center_print_content_2() == u""

    def verify_no_print_activity_available_screen(self):
        '''
        This is a verification method to check UI strings of No Print Activity Available screen.
        :parameter:
        :return:
        '''
        self.wait_for_no_print_activity_available_screen_load()
        logging.debug("Start to check UI strings of No Print Activity Available screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='no_print_activity_available_screen')
        assert self.get_value_of_no_print_activity_available_content_1() == test_strings['no_print_activity_available_content_1']
        assert self.get_value_of_no_print_activity_available_content_2() == test_strings['no_print_activity_available_content_2']

    def verify_job_printed_status(self):
        '''
        This is a verification method to check UI strings of Job Printed Status screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Job Printed Status screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status() == test_strings['job_printed_status']
#         assert self.get_value_of_print_activity_center_file_name() == u""
#         assert self.get_value_of_print_activity_center_date() == u""

    def verify_print_job_canceled_status(self):
        '''
        This is a verification method to check UI strings of Print Job Canceled Status screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Print Job Canceled Status screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status() == test_strings['print_job_canceled_status']
#         assert self.get_value_of_print_activity_center_file_name() == u""
#         assert self.get_value_of_print_activity_center_date() == u""

    def verify_status_unknown_status(self):
        '''
        This is a verification method to check UI strings of Status Unknown Status screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load_status_unknown()
        logging.debug("Start to check UI strings of Status Unknown Status screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status_status_unknown() == test_strings['status_unknown_status']
#         assert self.get_value_of_print_activity_center_file_name_status_unknown() == u""
#         assert self.get_value_of_print_activity_center_date_status_unknown() == u""

    def verify_error_printing_status(self):
        '''
        This is a verification method to check UI strings of Print Job Canceled Status screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load_error_printing()
        logging.debug("Start to check UI strings of Error Printing Status screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status_error_printing() == test_strings['error_printing_status']
#         assert self.get_value_of_print_activity_center_file_name_error_printing() == u""
#         assert self.get_value_of_print_activity_center_date_error_printing() == u""

    def verify_print_activity_center_status_screen_print_job_processing(self):
        '''
        This is a verification method to check UI strings of Print Activity Center Status - Print Job Processing screen.
        :parameter:
        :return:
        '''
        self.wait_for_print_activity_center_status_screen_load()
        logging.debug("Start to check UI strings of Print Activity Center Status - Print Job Processing screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status() == test_strings['job_processing_status']
        assert self.get_value_of_status_content_1() == test_strings['job_processing_your_file_text']
#         assert self.get_value_of_status_content_2() == u""
        assert self.get_value_of_status_content_3() == test_strings['job_processing_is_being_processed_text']
        assert self.get_value_of_status_cancel_btn() == test_strings['job_processing_cancel_btn']

    def verify_print_activity_center_status_screen_job_printed(self):
        '''
        This is a verification method to check UI strings of Print Activity Center Status - Job Printed screen.
        :parameter:
        :return:
        '''
        self.wait_for_print_activity_center_status_screen_load()
        logging.debug("Start to check UI strings of Print Activity Center Status - Job Printed screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status() == test_strings['job_printed_status']
        assert self.get_value_of_status_content_1() == test_strings['job_printed_your_file_text']
#         assert self.get_value_of_status_content_2() == u""
        assert self.get_value_of_status_content_3() == test_strings['job_printed_has_successfully_printed_text']
#         assert self.get_value_of_status_details_date() == u""
        assert self.get_value_of_status_clear_notification_btn() == test_strings['clear_notification_btn']

    def verify_print_activity_center_status_screen_print_job_canceled(self):
        '''
        This is a verification method to check UI strings of Print Activity Center Status - Print Job Canceled screen.
        :parameter:
        :return:
        '''
        self.wait_for_print_activity_center_status_screen_load()
        logging.debug("Start to check UI strings of Print Activity Center Status - Print Job Canceled screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status() == test_strings['print_job_canceled_status']
        assert self.get_value_of_status_content_1() == test_strings['print_job_canceled_the_printing_of_the_file_text']
#         assert self.get_value_of_status_content_2() == u""
        assert self.get_value_of_status_content_3() == test_strings['print_job_canceled_was_canceled_text']
        assert self.get_value_of_status_clear_notification_btn() == test_strings['clear_notification_btn']

    def verify_print_activity_center_status_screen_status_unknown(self):
        '''
        This is a verification method to check UI strings of Print Activity Center Status - Status Unknown screen.
        :parameter:
        :return:
        '''
        self.wait_for_print_activity_center_status_screen_load()
        logging.debug("Start to check UI strings of Print Activity Center Status - Status Unknown screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status_status_unknown() == test_strings['status_unknown_status']
        assert self.get_value_of_status_content_1() == test_strings['status_unknown_status_is_unavailable_text']
#         assert self.get_value_of_status_content_2() == u""
        assert self.get_value_of_status_content_3() == test_strings['status_unknown_did_not_print_text']
#         assert self.get_value_of_status_details_date() == u""
        assert self.get_value_of_status_clear_notification_btn() == test_strings['clear_notification_btn']

    def verify_print_activity_center_status_screen_error_printing(self):
        '''
        This is a verification method to check UI strings of Print Activity Center Status - Error Printing screen.
        :parameter:
        :return:
        '''
        self.wait_for_print_activity_center_status_screen_load()
        logging.debug("Start to check UI strings of Print Activity Center Status - Error Printing screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='print_activity_center_status_screen')
        assert self.get_value_of_print_activity_center_print_status_error_printing() == test_strings['error_printing_status']
        assert self.get_value_of_status_content_1() == test_strings['error_printing_this_pdf_text']
#         assert self.get_value_of_status_content_2() == u""
        assert self.get_value_of_status_content_3() == test_strings['error_printing_is_password_protected_text']
#         assert self.get_value_of_status_details_date() == u""
        assert self.get_value_of_status_clear_notification_btn() == test_strings['clear_notification_btn']

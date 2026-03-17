# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for Activity Center Text Files.

@author: Ivan
@create_date: Sep 28, 2021
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ActivityCenterTextFiles(SmartScreens):

    folder_name = "activitycenter"
    flow_name = "activity_center_text_files"

    def __init__(self, driver):
        super(ActivityCenterTextFiles, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Text Files Activity Center screen shows correctly after clicking Text Files item on Activity Center flyout.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("files_are_accessible_for_30_days_text", timeout=timeout, raise_e=raise_e)

    def wait_for_job_ellipsis_horizontal_sharp_btn_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for the first text files completed on Text Files Activity Center screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]:[wait_for_job_ellipsis_horizontal_sharp_btn_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("job_ellipsis_horizontal_sharp_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_text_files_activity_center_screen_title(self):
        '''
        This is a method to get value of Text Files Activity Center screen title
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]:[get_value_of_text_files_activity_center_screen_title]-Get the value of Text Files Activity Center screen title...  ")

        return self.driver.get_value("text_files_activity_center_screen_title")

    def get_value_of_files_are_accessible_for_30_days_text(self):
        '''
        This is a method to get value of Files are accessible for 30 days text on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]:[get_value_of_files_are_accessible_for_30_days_text]-Get the value of View all your recent account notifications text...  ")

        return self.driver.get_value("files_are_accessible_for_30_days_text")

    def get_value_of_job_name(self):
        '''
        This is a method to get value of the first job name on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]:[get_value_of_job_name]-Get the value of the first job name...  ")

        return self.driver.get_value("job_name")

    def get_value_of_job_status_date(self):
        '''
        This is a method to get value of the first job status date on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]:[get_value_of_job_status_date]-Get the value of the first job name...  ")

        return self.driver.get_value("job_status_date")

    def click_text_files_activity_center_screen_close_btn(self):
        '''
        This is a method to Click Close button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]]:[click_text_files_activity_center_screen_close_btn]-Click Close button... ")

        self.driver.click("text_files_activity_center_screen_close_btn", is_native_event=True)

    def click_text_files_activity_center_screen_back_btn(self):
        '''
        This is a method to Click Back button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]]:[click_text_files_activity_center_screen_back_btn]-Click Back button... ")

        self.driver.click("text_files_activity_center_screen_back_btn", is_native_event=True)

    def click_job_ellipsis_horizontal_sharp_btn(self):
        '''
        This is a method to Click Ellipsis horizontal sharp button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]]:[click_job_ellipsis_horizontal_sharp_btn]-Click Ellipsis horizontal sharp button... ")

        self.driver.click("job_ellipsis_horizontal_sharp_btn", is_native_event=True)

    def click_download_btn(self):
        '''
        This is a method to Click Download button on after clicking Ellipsis horizontal sharp button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]]:[click_download_btn]-Click Download button... ")

        self.driver.click("download_btn", is_native_event=True)

    def click_share_btn(self):
        '''
        This is a method to Click Share button on after clicking Ellipsis horizontal sharp button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]]:[click_share_btn]-Click Share button... ")

        self.driver.click("share_btn", is_native_event=True)

    def click_delete_btn(self):
        '''
        This is a method to Click Delete button on after clicking Ellipsis horizontal sharp button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]]:[click_delete_btn]-Click Delete button... ")

        self.driver.click("delete_btn", is_native_event=True)

    def wait_for_share_service_selected_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Share service selected dialog shows correctly after clicking Share button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]:[wait_for_share_service_selected_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("share_email_item", timeout=timeout, raise_e=raise_e)

    def click_share_more_item(self):
        '''
        This is a method to Click Delete button on after clicking Ellipsis horizontal sharp button on Text Files Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterTextFiles]]:[click_share_more_item]-Click Delete button... ")

        self.driver.click("share_more_item", is_native_event=True)

# -------------------------------Verification Methods-------------------------------
    def verify_text_files_activity_center_screen(self):
        '''
        This is a verification method to check UI strings of Text Files Activity Center screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to check UI strings of Text Files Activity Center screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='text_files_activity_center_screen')
        assert self.get_value_of_text_files_activity_center_screen_title() == test_strings['text_files_activity_center_screen_title']
        assert self.get_value_of_files_are_accessible_for_30_days_text() == test_strings['files_are_accessible_for_30_days_text']

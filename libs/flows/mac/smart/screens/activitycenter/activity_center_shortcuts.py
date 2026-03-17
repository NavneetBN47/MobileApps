# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for Activity Center Fly-out.

@author: Ivan
@create_date: Jan 20, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ActivityCenterShortcuts(SmartScreens):

    folder_name = "activitycenter"
    flow_name = "activity_center_shortcuts"

    def __init__(self, driver):
        super(ActivityCenterShortcuts, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Activity Center Fly-out shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("st_activity_center_title", timeout=timeout, raise_e=raise_e)

    def wait_for_no_st_activity_available_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait No Smart Task Activity Available page shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[wait_for_no_st_activity_available_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_st_activity_availbale_content_1", timeout=timeout, raise_e=raise_e)

    def wait_for_has_st_activity_center_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait ST Activity Center with st activity screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[wait_for_has_st_activity_center_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("smart_task_completed_title", timeout=timeout, raise_e=raise_e)

    def wait_for_has_st_activity_center_details_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait ST Activity Center with st activity details screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[wait_for_has_st_activity_center_details_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("smart_task_completed_details_title", timeout=timeout, raise_e=raise_e)

    def click_st_activity_center_back_btn(self):
        '''
        This is a method to click Back button on Shortcuts Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[click_st_activity_center_back_btn]-Click Back button... ")

        self.driver.click("st_activity_center_back_btn", is_native_event=True)

    def click_st_activity_center_close_btn(self):
        '''
        This is a method to click Close button on Shortcuts Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[click_st_activity_center_close_btn]-Click Close button... ")

        self.driver.click("st_activity_center_close_btn", is_native_event=True)

    def click_smart_task_completed_title(self):
        '''
        This is a method to click Smart Task Completed title on Shortcuts Activity Center screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[click_smart_task_completed_title]-Click Smart Task Completed title... ")

        self.driver.click("smart_task_completed_title", is_native_event=True)

    def click_smart_task_completed_details_delete_btn(self):
        '''
        This is a method to click Delete button on Shortcuts Activity Center details screen.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[click_smart_task_completed_details_delete_btn]-Click Delete button... ")

        self.driver.click("smart_task_completed_details_delete_btn", is_native_event=True)

    def get_value_of_no_st_activity_availbale_title(self):
        '''
        This is a method to get value of No Smart Task Activity Available Page title
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_no_st_activity_availbale_title]-Get the value of No Smart Task Activity Available Page title ...  ")

        return self.driver.get_value("st_activity_center_title")

    def get_value_of_no_st_activity_availbale_content_1(self):
        '''
        This is a method to get value of No Smart Task Activity Available Page content - 1
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_no_st_activity_availbale_content_1]-Get the value of No Smart Task Activity Available Page content - 1 ...  ")

        return self.driver.get_value("no_st_activity_availbale_content_1")

    def get_value_of_no_st_activity_availbale_content_2(self):
        '''
        This is a method to get value of No Smart Task Activity Available Page content - 2
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_no_st_activity_availbale_content_2]-Get the value of No Smart Task Activity Available Page content - 2 ...  ")

        return self.driver.get_value("no_st_activity_availbale_content_2")

    def get_value_of_smart_task_completed_title(self):
        '''
        This is a method to get value of Tasks title on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_title]-Get the value of Tasks title ...  ")

        return self.driver.get_value("smart_task_completed_title")

    def get_value_of_smart_task_completed_name(self):
        '''
        This is a method to get value of Tasks name on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_name]-Get the value of Tasks name ...  ")

        return self.driver.get_value("smart_task_completed_name")

    def get_value_of_smart_task_completed_date(self):
        '''
        This is a method to get value of Tasks date on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_date]-Get the value of Tasks date ...  ")

        return self.driver.get_value("smart_task_completed_date")

    def get_value_of_smart_task_completed_details_title(self):
        '''
        This is a method to get value of Details page title on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_details_title]-Get the value of Details page title ...  ")

        return self.driver.get_value("smart_task_completed_details_title")

    def get_value_of_smart_task_completed_details_content_1(self):
        '''
        This is a method to get value of Details page content - 1 on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_details_content_1]-Get the value of Details page content - 1 ...  ")

        return self.driver.get_value("smart_task_completed_details_content_1")

    def get_value_of_smart_task_completed_details_content_2(self):
        '''
        This is a method to get value of Details page content - 2 on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_details_content_2]-Get the value of Details page content - 2 ...  ")

        return self.driver.get_value("smart_task_completed_details_content_2")

    def get_value_of_smart_task_completed_details_content_3(self):
        '''
        This is a method to get value of Details page content - 3 on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_details_content_3]-Get the value of Details page content - 3 ...  ")

        return self.driver.get_value("smart_task_completed_details_content_3")

    def get_value_of_smart_task_completed_details_date(self):
        '''
        This is a method to get value of Details page date on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_details_date]-Get the value of Details page date ...  ")

        return self.driver.get_value("smart_task_completed_details_date")

    def get_value_of_smart_task_completed_details_delete_btn(self):
        '''
        This is a method to get value of Details page delete button on Smart Task Activity Center screen - With ST Activity
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterShortcuts]:[get_value_of_smart_task_completed_details_delete_btn]-Get the value of Details page delete button ...  ")

        return self.driver.get_title("smart_task_completed_details_delete_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_no_st_activity_available_screen(self):
        '''
        This is a verification method to check UI strings of No Shortcuts Activity Available screen
        :parameter:
        :return:
        '''
        self.wait_for_no_st_activity_available_load()
        logging.debug("Start to check UI strings of No Shortcuts Activity Available screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='shortcuts_activity_center_screen')
        assert self.get_value_of_no_st_activity_availbale_title() == test_strings['st_activity_center_title']
        assert self.get_value_of_no_st_activity_availbale_content_1() == test_strings['no_st_activity_availbale_content_1']
        assert self.get_value_of_no_st_activity_availbale_content_2() == test_strings['no_st_activity_availbale_content_2']

    def verify_st_activity_center_screen_disappear(self, timeout=10):
        '''
        verify No Shortcuts Activity Center screen disappear after click Back/Close button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("st_activity_center_title", timeout=timeout, raise_e=False)

    def verify_has_st_activity_center_screen(self):
        '''
        This is a verification method to check UI strings of Smart Task Completed on Activity Center screen.
        :parameter:
        :return:
        '''
        self.wait_for_has_st_activity_center_screen_load()
        logging.debug("Start to check UI strings of Smart Task Completed on Activity Center screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='shortcuts_activity_center_screen')
        assert self.get_value_of_smart_task_completed_title() == test_strings['smart_task_completed_title']
#         assert self.get_value_of_smart_task_completed_name() == u""
        assert self.get_value_of_smart_task_completed_date() == test_strings['smart_task_completed_date']

    def verify_has_st_activity_center_details_screen(self):
        '''
        This is a verification method to check UI strings of Smart Task Completed details page on Activity Center screen.
        :parameter:
        :return:
        '''
        self.wait_for_has_st_activity_center_details_screen_load()
        logging.debug("Start to check UI strings of Smart Task Completed details page on Activity Center screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='shortcuts_activity_center_screen')
        assert self.get_value_of_smart_task_completed_details_title() == test_strings['smart_task_completed_title']
        assert self.get_value_of_smart_task_completed_details_content_1() == test_strings['smart_task_completed_details_your_smart_task_text']
#         assert self.get_value_of_smart_task_completed_details_content_2() == test_strings['']
        assert self.get_value_of_smart_task_completed_details_content_3() == test_strings['smart_task_completed_details_has_successfully_text']
#         assert self.get_value_of_smart_task_completed_details_date() == test_strings['']
        assert self.get_value_of_smart_task_completed_details_delete_btn() == test_strings['smart_task_completed_details_delete_btn']

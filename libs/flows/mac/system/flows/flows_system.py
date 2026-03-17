# encoding: utf-8
'''
Description: It defines system flows in the MAC OS.

@author: Sophia
@create_date: May 9, 2019
'''
from MobileApps.libs.flows.mac.smart.utility import smart_utilities
from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences
from MobileApps.resources.const.mac import const as m_const


class SystemFlows(object):

    def __init__(self, driver, append=False):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver
        self.system_preferences = SystemPreferences(self.driver, append=append)

    def allow_hp_smart_app_notifications(self):
        self.driver.launch_app(m_const.BUNDLE_ID.SYSTEM_SETTINGS)
        smart_utilities.clear_mac_popups(self.driver.session_data["ssh"])
        self.system_preferences.click_notifications_settings_option()
        self.system_preferences.click_application_notifications_hp_smart_opt()
        self.system_preferences.allow_hp_smart_notifications()
        self.driver.terminate_app(m_const.BUNDLE_ID.SYSTEM_SETTINGS)
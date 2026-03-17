import logging
from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.base_flow import BaseFlow
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class AndroidFlow(BaseFlow):
    __metaclass__ = ABCMeta
    system = "android"

    def __init__(self, driver):
        super(AndroidFlow, self).__init__(driver)
        self.load_android_system_ui()

    def load_android_system_ui(self):
        ui_map = self.load_ui_map(system="ANDROID", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map)
        return True

    def handle_allow_popup(self):
        if self.driver.wait_for_object("_system_app_permission_allow_btn", timeout=25, raise_e=False):
            logging.info("Permission popup is present")
            self.driver.click("_system_app_permission_allow_btn", timeout=25)

    def check_run_time_permission(self, accept=True, consent_type=None, location_precision=None, timeout=5):
        """
        Allow App Permission alert if it displays on the screen for Marshmallow or N device
        :param accept: True or False depending on whether the permission should be approved or denied
        :param consent_type: The type of consent that should be granted(ignored for accept=False). "one_time" or "foreground_only".
        :param location_precision: The location precision to select for android 12+. "precise" or "approximate"
        """
        if popup := self.driver.wait_for_object("_system_app_permission_popup", timeout=timeout, interval=1, raise_e=False) and \
            ((accept and self.driver.wait_for_object("_system_app_permission_allow_btn", raise_e=False)) or (not accept and self.driver.wait_for_object("_system_app_permission_deny_btn", raise_e=False))):
            logging.info("Permission popup found with text: " + popup.text)
            if location_precision != None:
                if int(self.driver.platform_version) < 12:
                    logging.warning("location_precision param does not apply for android 11 and below")
                else:
                    self.driver.click("_system_app_permission_{}_location_rb".format(location_precision))
            if not accept:
                self.driver.click("_system_app_permission_deny_btn")
            elif consent_type != None:
                self.driver.click("_system_app_permission_allow_{}_btn".format(consent_type))
            else:
                self.driver.click("_system_app_permission_allow_btn")

    def is_app_permission_popup(self):
        try:
            self.driver.wait_for_object("_system_app_permission_popup", timeout=5)
            is_displayed = True
        except (TimeoutException, NoSuchElementException):
            is_displayed = False
            logging.info("Popup about App Permission is not displayed")
        return is_displayed        

class android_system_ui_flow(AndroidFlow):
    project="system"
    flow_name = "system_ui"

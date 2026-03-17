from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class FirmwareUpdateChoice(OWSFlow):
    """
    url: https://oss.hpconnectedpie.com//firmware-update-choice
    """
    flow_name = "firmware_update_choice"


    def verify_firmware_update_choice_page(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("fw_update_choice_page", raise_e=raise_e, timeout=timeout)

    def click_auto_update_button(self):
        self.driver.wait_for_object("auto_update_button")

    def click_notify_button(self):
        self.driver.wait_for_object("notify_button")

    def click_apply_button(self):
        self.driver.wait_for_object("apply_button")

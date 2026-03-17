import json

from MobileApps.libs.flows.mac.jweb.jweb_flow import JwebFlow

class DevicePlugin(JwebFlow):
    project = "jweb"
    flow_name = "device_plugin"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def press_device_info_test_btn(self):
        """
        presses the test button under Device.getInfo()
        """
        self.driver.click("device_info_test_btn")

    def press_language_test_btn(self):
        """
        presses the test button under Device.getLanguageCode()
        """
        self.driver.click("language_code_test_btn")

    def return_device_info(self):
        """
        :return: text result text under Device.getInfo() 
        """
        return json.loads(self.driver.wait_for_object("device_info_test_result", displayed=False).get_attribute('value'))

    def return_language_test_result(self):
        """
        :return: text result text under Device.getLanguageCode() 
        """
        return json.loads(self.driver.wait_for_object("language_test_result", displayed=False).get_attribute('value'))

    # *********************************************************************************
    #                             VERIFICATION FLOWS                                  *
    # *********************************************************************************

    def verify_at_device_plugin(self):
        """
        Verify that we are currently on the device plugin page
        :return: bool
        """
        return self.driver.wait_for_object("device_info_test_btn", raise_e=False, timeout=1) is not False
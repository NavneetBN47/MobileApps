from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow
import json

class EventingPlugin(JwebFlow):
    project = "jweb"
    flow_name = "eventing_plugin"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################


    def select_eventing_plugin_test(self):
        """
        clicks the eventing plugin test btn
        """
        self.driver.swipe(direction="up")
        self.driver.click("eventing_test_button")

    def eventing_test_result(self):
        """
        :return: the eventing test result text
        """
        return self.driver.wait_for_object("eventing_test_result_txt", raise_e=False, displayed=False).text

    def select_jarvis_event_option_test(self):
        """
        clicks the send jarvis event test btn
        """
        self.driver.swipe(direction="down")
        self.driver.click("eventing_send_event_test_btn")

    def jarvis_event_option_test_result(self):
        """
        :return: text after clicking jarvis event option test btn
        """
        return self.driver.find_object("eventing_jarvis_options_test_result").text.lstrip()

    def enter_add_listener_event(self, option):
        """
        sends name of event listener in Eventing.addListener() tab
        :param: option
        """
        self.driver.send_keys("eventing_native_element_listener_field", option)

    def select_add_listener_test_btn(self):
        """
        clicks the add listener test btn
        """
        self.driver.swipe(direction="down")
        self.driver.click("eventing_add_listener_btn")

    def add_listener_test_result(self):
        """
        :return: add listener test result text
        """
        return self.driver.wait_for_object("add_listener_test_result_text", displayed=False).text

    def get_add_listener_pop_up_toast_text(self):
        """
        :return: text found from the toast pop up notification
        """
        return json.loads(self.driver.wait_for_object("pop_up_toast_text", displayed=False).text)

    def add_listener_event_result(self):
        """
        :return: add listener event result text
        """
        return json.loads(self.driver.wait_for_object("add_listener_event_result_text", displayed=False).text)

    def close_all_toast_notification(self):
        """
        Continue closing all toast notifications until no more notifications are present
        """
        while self.verify_toast_is_present():
            self.driver.click("toast_close_btn")
            

    # *********************************************************************************
    #                             VERIFICATION FLOWS                                  *
    # *********************************************************************************

    def verify_toast_is_present(self):
        """
        verifies that a toast message is present
        :return: bool
        """
        return self.driver.wait_for_object("toast_close_btn", raise_e=False, timeout=2) is not False

    def verify_at_eventing_plugin(self):
        """
        Verify that we are currently on the eventing plugin page
        :return: bool
        """
        return self.driver.wait_for_object("eventing_test_button", raise_e=False, timeout=3, displayed=False) is not False
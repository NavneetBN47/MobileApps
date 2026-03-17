import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class NoEmailAccount(Exception):
    pass

class SpecificEmailAccountDoesNotExist(Exception):
    pass

class Gmail(SmartFlow):
    flow_name = "gmail"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def compose_and_send_email(self, to_email, subject_text="", body_text=""):
        self.driver.wait_for_object("to_field", displayed=False)
        self.driver.click("to_field", displayed=False)
        self.driver.send_keys("to_field", to_email, press_enter=True)
        if subject_text:
            try:
                self.driver.click("subject_field")
                self.driver.send_keys("subject_field", subject_text)
            except NoSuchElementException:
                logging.info("subject field is empty")
        self.driver.click("send_btn")
        if (self.handle_send_email_popup() or self.verify_reduce_message_displayed()) is not False:
            self.click_on_btn('actual size')

    def handle_send_email_popup(self):
        return self.driver.wait_for_object("continue_btn", timeout=20, raise_e=False) is not False

    def verify_reduce_message_displayed(self):
        return self.driver.wait_for_object("reduce_message_size_title_txt", timeout=20, raise_e=False) is not False

    def click_on_btn(self, btn_name):
        all_btn_on_page = len(self.driver.find_object("all_btn_in_page", multiple=True))
        for button_index in range(all_btn_on_page):
            if btn_name.lower() in self.driver.find_object("all_btn_in_page", index=button_index).text.lower():
                return self.driver.click("all_btn_in_page", index=button_index)

    def get_email_subject_text(self):
        return self.driver.get_attribute("subject_field", attribute="value")
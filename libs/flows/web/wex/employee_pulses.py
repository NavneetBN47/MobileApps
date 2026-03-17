from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from selenium.webdriver.common.keys import Keys
from time import sleep

class EmployeePulses(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "employee_pulses"

    ######################## Main Menu ########################

    def verify_pulses_page(self):
        return self.driver.wait_for_object("pulses_page_breadcrumb", timeout=30, raise_e=False)

    def get_pulses_page(self):
        return self.driver.wait_for_object("pulses_page_breadcrumb", timeout=30, raise_e=False).text

    def click_pulses_page_breadcrumb(self):
        return self.driver.click("custom_pulse_page_pulses_breadcrumb")

    def verify_pulses_page_create_pulse_button(self, displayed=True):
        return self.driver.wait_for_object("pulses_page_create_pulse_button", invisible=not displayed, raise_e=False)

    def click_pulses_page_create_pulse_button(self):
        return self.driver.click("pulses_page_create_pulse_button")

    def click_create_pulse_from_scratch_button(self):
        return self.driver.click("pulses_page_create_pulse_from_scratch_button",timeout=30)

    def verify_pulses_page_sentiment_pulse_button(self, displayed=True):
        return self.driver.wait_for_object("pulses_page_sentiment_pulse_button", invisible=not displayed, raise_e=False)

    def verify_pulses_page_pulses_table_checkbox(self, displayed=True):
        return self.driver.wait_for_object("pulses_page_pulses_table_checkbox", invisible=not displayed, raise_e=False)
   
    def click_pulses_page_pulses_table_checkbox(self):
        return self.driver.click("pulses_page_pulses_table_checkbox")

    def verify_pulses_page_create_custom_pulse_button(self):
        return self.driver.wait_for_object("pulses_page_create_custom_pulse_button", raise_e=False)
    
    def verify_pulses_page_create_sentiment_pulse_button(self):
        return self.driver.wait_for_object("pulses_page_create_sentiment_pulse_button", raise_e=False)
    
    def click_create_custom_pulse_button(self):
        return self.driver.click("pulses_page_create_custom_pulse_button")
    
    def click_create_sentiment_pulse_button(self):
        return self.driver.click("pulses_page_create_sentiment_pulse_button")

    def click_pulses_page_custom_pulses_table_checkbox(self, pulse_name):
        return self.driver.click("pulses_page_custom_pulses_table_checkbox",format_specifier =[pulse_name])
    
    def click_pulses_page_sentiment_pulses_table_checkbox(self, pulse_name):
        return self.driver.click("pulses_page_sentiment_pulses_table_checkbox", format_specifier=[pulse_name])

    ############################### Pulses Page - Custom Pulse Page ######################

    def verify_pulses_page_create_pulse_custom_pulse_page(self, displayed=True):
        return self.driver.wait_for_object("pulses_page_create_pulse_custom_pulse_page", invisible=not displayed, raise_e=False)

    def get_pulses_page_create_pulse_custom_pulse_header(self):
        return self.driver.wait_for_object("pulses_page_create_pulse_custom_pulse_header").text

    def click_pulses_page_leave_page_popup_leave_button(self):
        return self.driver.click("pulses_page_leave_page_popup_leave_button")

    def verify_create_custom_pulse_page_content_tab(self):
        return self.driver.wait_for_object("create_custom_pulse_page_content_tab", raise_e=False)
    
    def verify_create_custom_pulse_page_schedule_tab(self):
        return self.driver.wait_for_object("create_custom_pulse_page_schedule_tab", raise_e=False)
    
    def verify_create_custom_pulse_page_audience_tab(self):
        return self.driver.wait_for_object("create_custom_pulse_page_audience_tab", raise_e=False)

    def click_create_custom_pulse_page_edit_button(self):
        return self.driver.click("create_custom_pulse_page_edit_button")

    def edit_create_custom_pulse_page_pulse_name(self, pulse_name):
        # # obj = self.driver.find_object("create_custom_pulse_page_pulse_name_input")
        # # obj.send_keys(Keys.CONTROL + "a")
        # sleep(3)  # Wait for the input to be cleared
        return self.driver.send_keys("create_custom_pulse_page_pulse_name_input", pulse_name)

    ######################### Pulses Page - Edit Pulse Popup ########################

    def verify_pulses_page_edit_pulse_button(self, displayed=True):
        return self.driver.wait_for_object("pulses_page_edit_pulse_button", invisible=not displayed, raise_e=False)

    ######################## Pulses Page - Duplicate Pulse Popup ######################

    def verify_pulses_page_duplicate_pulse_button(self, displayed=True):
        return self.driver.wait_for_object("pulses_page_duplicate_pulse_button", invisible=not displayed, raise_e=False)
   
    def click_pulses_page_duplicate_pulse_button(self):
        return self.driver.click("pulses_page_duplicate_pulse_button")

    def get_pulses_page_duplicate_pulse_popup_title(self):
        return self.driver.wait_for_object("pulses_page_duplicate_pulse_popup_title", timeout=30).text

    def verify_pulses_page_duplicate_pulse_popup_cancel_button(self):
        return self.driver.wait_for_object("pulses_page_duplicate_pulse_popup_cancel_button", raise_e=False)

    def click_pulses_page_duplicate_pulse_popup_cancel_button(self):
        return self.driver.click("pulses_page_duplicate_pulse_popup_cancel_button")

    ######################## Pulses Page - Delete Pulse Popup ######################

    def verify_pulses_page_delete_pulse_button(self, displayed=True):
        return self.driver.wait_for_object("pulses_page_delete_pulse_button", invisible=not displayed, raise_e=False)

    def click_pulses_page_delete_pulse_button(self):
        return self.driver.click("pulses_page_delete_pulse_button")
   
    def get_pulses_page_delete_pulse_popup_title(self):
        return self.driver.wait_for_object("pulses_page_delete_pulse_popup_title").text

    def verify_pulses_page_delete_pulse_popup_cancel_button(self):
        return self.driver.wait_for_object("pulses_page_delete_pulse_popup_cancel_button", raise_e=False)

    def click_pulses_page_delete_pulse_popup_cancel_button(self):
        return self.driver.click("pulses_page_delete_pulse_popup_cancel_button")

    def verify_pulses_page_delete_pulse_popup_delete_button(self):
        return self.driver.wait_for_object("pulses_page_delete_pulse_popup_delete_button", raise_e=False)
    
    def click_pulses_page_delete_pulse_popup_delete_button(self):
        return self.driver.click("pulses_page_delete_pulse_popup_delete_button")
    
    def get_pulse_deleted_toast_msg(self):
        return self.driver.wait_for_object("pulse_deleted_toast_msg", timeout=30, raise_e=False).text

    ######################## Pulses Page - Sentiment Pulse Page ######################
     
    def verify_pulses_page_create_pulse_sentiment_pulse_page(self):
        return self.driver.wait_for_object("pulses_page_create_pulse_sentiment_pulse_page", raise_e=False, timeout =30)
 
    def verify_create_sentiment_pulse_page_content_tab(self):
        return self.driver.wait_for_object("create_sentiment_pulse_page_content_tab", raise_e=False)
    
    def verify_create_sentiment_pulse_page_schedule_tab(self):
        return self.driver.wait_for_object("create_sentiment_pulse_page_schedule_tab", raise_e=False)

    def verify_create_sentiment_pulse_page_audience_tab(self):
        return self.driver.wait_for_object("create_sentiment_pulse_page_audience_tab", raise_e=False)

    def click_create_sentiment_pulse_page_edit_button(self):
        return self.driver.click("create_sentiment_pulse_page_edit_button")
    
    def edit_create_sentiment_pulse_page_pulse_name(self, pulse_name):
        self.driver.clear_text("create_sentiment_pulse_page_pulse_name_input")
        sleep(3)
        return self.driver.send_keys("create_sentiment_pulse_page_pulse_name_input", pulse_name)
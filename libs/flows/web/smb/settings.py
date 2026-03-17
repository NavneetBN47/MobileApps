from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow

class UnexpectedItemPresentException(Exception):
    pass

class Settings(SMBFlow):

    flow_name = "settings"

    ############################ Preferences ############################

    def click_preferences_tab(self):
        return self.driver.click("preferences_tab",timeout=20)

    ##################### Notification Tab #######################
    def verify_preferences_screen_title(self):
        return self.driver.verify_object_string("preferences_title", timeout=20)
    
    def verify_preferences_screen_description(self):
        return self.driver.verify_object_string("preferences_title_desc")

    def verify_notifications_tab_title(self):
        return self.driver.verify_object_string("notifications_tab_title")
    
    def verify_privacy_tab_title(self):
        return self.driver.verify_object_string("privacy_tab_title")
        
    def verify_language_tab_title(self):
        return self.driver.verify_object_string("language_tab_title")

    def verify_notifications_tab_description(self):
        return self.driver.verify_object_string("notifications_tab_title_desc")
    
    def verify_notification_type_printer_and_service_status(self):
        return self.driver.verify_object_string("printer_type_title")
    
    def verify_notification_type_account_and_billing(self):
        return self.driver.verify_object_string("billing_type_title")
    
    def verify_notification_type_promotions(self):
        return self.driver.verify_object_string("promotions_type_title")

    def verify_notification_type_feature_awareness(self):
        return self.driver.verify_object_string("feature_type_title")

    def verify_notification_type_printer_and_service_status_description(self):
        return self.driver.verify_object_string("printer_type_title_desc")
    
    def verify_notification_type_account_and_billing_description(self):
        return self.driver.verify_object_string("billing_type_title_desc")

    def verify_notification_type_promotions_type_description(self):
       return self.driver.verify_object_string("promotions_type_title_desc")

    def verify_notification_type_feature_awareness_type_description(self):
        return self.driver.verify_object_string("feature_type_title_desc")
    
    def click_notification_type_printer_and_service_status_toggle_button(self):
        return self.driver.click("printer_type_toggle",timeout=5)
    
    def click_notification_type_account_and_billing_toggle_button(self):
        return self.driver.click("billing_type_toggle",timeout=5)
    
    def click_notification_type_promotions_toggle_button(self):
        return self.driver.click("promotions_type_toggle",timeout=5)
    
    def click_notification_type_feature_awarenesss_toggle_button(self):
        return self.driver.click("feature_type_toggle",timeout=5)
        
    def get_notification_type_printer_and_service_toggle_button_status(self):
        return self.driver.get_text("printer_type_status")

    def get_notification_type_account_and_billing_toggle_button_status(self):
        return self.driver.get_text("billing_type_status")

    def get_notification_type_promotions_toggle_button_status(self):
        return self.driver.get_text("promotions_type_status")
    
    def get_notification_type_feature_awareness_toggle_button_status(self):
        return self.driver.get_text("feature_type_status")
    
    def verify_positive_toast_notification(self):
        return self.driver.verify_object_string("positive_toast_notification")
    
    def verify_negative_toast_notification(self):
        return self.driver.verify_object_string("negative_toast_notification")

    def get_notifications_table_headers(self):
        notifications_table_headers = []
        headers = self.driver.find_object("notification_table_headers", multiple = True)
        for header in headers:
            notifications_table_headers.append(header.text)
        return notifications_table_headers

from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
from SAF.decorator.saf_decorator import string_validation

class HelpCenter(SMBFlow):
    flow_name = "helpcenter"
    
    def verify_help_center_title(self):
        return self.driver.verify_object_string("helpcenter_title", timeout=40)
    
    @string_validation("sideMenuContent_title")
    def verify_about_help_center_title(self):
        return self.driver.wait_for_object("sideMenuContent_title")
    
    @string_validation("sideMenuContent_text")
    def verify_about_help_center_description(self):
        return self.driver.wait_for_object("sideMenuContent_text")

    def verify_help_center_printing_title(self):
        return self.driver.verify_object_string("printing_title", timeout=20)
    
    def verify_help_center_help_and_support_title(self):
        return self.driver.verify_object_string("help_and_support_title", timeout=20)
    
    def verify_help_center_account_title(self):
        return self.driver.verify_object_string("account_title", timeout=20)
    
    def verify_help_center_scan_and_fax_settings_title(self):
        return self.driver.verify_object_string("scan_and_fax_settings_title", timeout=20)
    
    def verify_help_center_sustainability_title(self):
        return self.driver.verify_object_string("sustainability_title", timeout=20)
    
    def verify_help_center_solutions_title(self):
        return self.driver.verify_object_string("solutions_title", timeout=20)
    
    def verify_help_center_hp_instant_ink_title(self):
        return self.driver.verify_object_string("hp_instant_ink_title", timeout=20)
    
    def verify_help_center_managing_users_title(self):
        return self.driver.verify_object_string("managing_users_title", timeout=20)
    
    def verify_help_center_managing_printers_title(self):
        return self.driver.verify_object_string("managing_printers_title", timeout=20)
    
    def verify_help_center_hp_smart_admin_dashboard_title(self):
        return self.driver.verify_object_string("hp_smart_admin_dashboard_title", timeout=20)
    
    @string_validation("breadcrumb_helpCenter")
    def verify_helpcenter_breadcrumb_helpcenter_text(self):
        return self.driver.wait_for_object("breadcrumb_helpCenter")

    @string_validation("breadcrumb_home")
    def verify_helpcenter_breadcrumb_home_text(self):
        return self.driver.wait_for_object("breadcrumb_home")
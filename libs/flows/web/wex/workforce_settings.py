from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class WorkforceSettings(WEXFlow):
    """
        Settings flow for WEX.
    """
    flow_name = "workforce_settings"

   ############################ Main Menu verifys ############################

    def verify_settings_page(self):
        return self.driver.wait_for_object("settings_page_breadcrumb", timeout=20, raise_e=False)

    def get_settings_page_breadcrumb(self):
        return self.driver.wait_for_object("settings_page_breadcrumb", timeout=20, raise_e=False).text
    
    def verify_settings_locations_tab(self):
        return self.driver.wait_for_object("settings_locations_tab", timeout=20, raise_e=False)
    
    def get_settings_locations_tab(self):
        return self.driver.wait_for_object("settings_locations_tab", timeout=20, raise_e=False).text
    
    def click_settings_locations_tab(self):
        return self.driver.click("settings_locations_tab")
    
    def get_locations_tab_title(self):
        self.driver.wait_for_object("settings_locations_tab_title", timeout=20)
        return self.driver.get_text("settings_locations_tab_title")
    
    def verify_settings_preferences_tab(self):
        return self.driver.wait_for_object("settings_preferences_tab", timeout=20, raise_e=False)

    def get_settings_preferences_tab(self):
        return self.driver.wait_for_object("settings_preferences_tab", timeout=20, raise_e=False).text
    
    def click_settings_preferences_tab(self):
        return self.driver.click("settings_preferences_tab")
    
    def get_preferences_tab_title(self):
        return self.driver.wait_for_object("settings_preferences_tab_title", timeout=20, raise_e=False).text
    
    def verify_settings_roles_and_permissions_tab(self):
        return self.driver.wait_for_object("settings_roles_and_permissions_tab", timeout=20, raise_e=False)
    
    def click_settings_roles_and_permissions_tab(self):
        return self.driver.click("settings_roles_and_permissions_tab")
    
    def get_roles_and_permissions_tab_title(self):
        self.driver.wait_for_object("settings_roles_and_permissions_tab_title", timeout=20)
        return self.driver.get_text("settings_roles_and_permissions_tab_title")
    
    def verify_settings_end_user_notifications_tab(self):
        return self.driver.wait_for_object("settings_end_user_notifications_tab", timeout=20, raise_e=False)
    
    def click_settings_end_user_notifications_tab(self):
        return self.driver.click("settings_end_user_notifications_tab")
    
    def get_end_user_notifications_tab_title(self):
        self.driver.wait_for_object("settings_end_user_notifications_tab_title", timeout=20)
        return self.driver.get_text("settings_end_user_notifications_tab_title")
    
    def verify_settings_logs_tab(self):
        return self.driver.wait_for_object("settings_logs_tab", timeout=20, raise_e=False)  
    
    def click_settings_logs_tab(self):
        return self.driver.click("settings_logs_tab")
    
    def get_logs_tab_title(self):
        self.driver.wait_for_object("settings_logs_tab_title", timeout=20)
        return self.driver.get_text("settings_logs_tab_title")
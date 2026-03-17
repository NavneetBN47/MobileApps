from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class RemediationsActivity(WEXFlow):
    """
        Remediations Activity flow for WEX.
    """
    flow_name = "remediations_activity"

    ############################ Main Menu verifys ############################
 
    def verify_remediations_activity_page(self):
        return self.driver.wait_for_object("remediations_activity_page_breadcrumb", timeout=30, raise_e=False)
    
    def get_remediations_activity_page(self):
        return self.driver.wait_for_object("remediations_activity_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_remediations_activity_add_button(self):
        return self.driver.wait_for_object("remediations_activity_add_button", timeout=20, raise_e=False)
    
    def click_remediations_activity_add_button(self):
        return self.driver.click("remediations_activity_add_button")
    
    def verify_add_activity_page_title(self):
        return self.driver.verify_object_string("add_activity_page_title", timeout=30)
    
    def click_add_activity_page_cancel_button(self):
        return self.driver.click("add_activity_page_cancel_button")

    def get_first_entry_link_text(self):
        return self.driver.get_text("_shared_table_entries_with_link")
    
    def get_activity_page_title(self):
        self.driver.wait_for_object("activity_page_title", timeout=30)
        return self.driver.get_text("activity_page_title")
    
    def get_activity_page_activity_name(self):
        return self.driver.get_text("activity_page_activity_name")
    
    def verify_activity_page_edit_button(self):
        return self.driver.wait_for_object("activity_page_edit_button", timeout=20, raise_e=False)
    
    def verify_activity_page_delete_button(self):
        return self.driver.wait_for_object("activity_page_delete_button", timeout=20, raise_e=False)
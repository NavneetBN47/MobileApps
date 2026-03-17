from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class Groups(WEXFlow):
    """
        Groups flow for WEX.
    """
    flow_name = "groups"

   ############################ Main Menu verifys ############################

    def verify_pcs_groups_page(self):
        return self.driver.verify_object_string("groups_page_breadcrumb", timeout=30)
    
    def verify_pcs_groups_add_button(self):
        return self.driver.wait_for_object("groups_add_button", timeout=20, raise_e=False)
    
    def verify_pcs_groups_delete_button(self):
        return self.driver.wait_for_object("groups_delete_button", timeout=20, raise_e=False)
    
    def verify_pcs_groups_export_button(self):
        return self.driver.wait_for_object("groups_export_button", timeout=20, raise_e=False)
    
    def verify_pcs_groups_edit_button(self):
        return self.driver.wait_for_object("groups_edit_button", timeout=20, raise_e=False)

    def click_pcs_groups_add_button(self):
        return self.driver.click("groups_add_button")
    
    def verify_add_groups_page_title(self):
        return self.driver.verify_object_string("add_groups_page_title", timeout=30)

    def click_add_groups_page_cancel_button(self):
        return self.driver.click("add_groups_page_cancel_button")
    
    def click_pcs_groups_edit_button(self):
        return self.driver.click("groups_edit_button")
    
    def verify_edit_groups_page_title(self):
        return self.driver.verify_object_string("edit_groups_page_title", timeout=30)
    
from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class PolciesPCS(WEXFlow): 
    """
        Remediations Policies PC's flow for WEX.
    """
    flow_name = "policies_pcs"

   ############################ Main Menu verifys ############################
        
    def verify_remediations_policies_pcs_page(self):
        return self.driver.wait_for_object("remediations_policies_pcs_page_breadcrumb", timeout=30, raise_e=False)

    def get_remediations_policies_pcs_page(self):
        return self.driver.wait_for_object("remediations_policies_pcs_page_breadcrumb", timeout=20, raise_e=False).text

    def verify_remediations_policies_pcs_tab(self):
        return self.driver.wait_for_object("remediations_policies_pcs_tab", timeout=20, raise_e=False)

    def get_remediations_policies_pcs_tab(self):
        return self.driver.wait_for_object("remediations_policies_pcs_tab", timeout=20, raise_e=False).text
    
    def verify_remediations_policies_pcs_add_button(self):
        return self.driver.wait_for_object("remediations_policies_pcs_add_button", timeout=20, raise_e=False)
    
    def verify_remediations_policies_pcs_delete_button(self):
        return self.driver.wait_for_object("remediations_policies_pcs_delete_button", timeout=20, raise_e=False)
    
    def click_remediations_policies_pcs_add_button(self):
        return self.driver.click("remediations_policies_pcs_add_button")
    
    def verify_add_pcs_policies_page_title(self):
        return self.driver.verify_object_string("add_pcs_policies_page_title", timeout=30)
    
    def click_add_pcs_policies_page_cancel_button(self):
        return self.driver.click("add_pcs_policies_page_cancel_button")
    
    def click_first_entry_policy_link(self):
        self.driver.wait_for_object("policies_pc_first_link", timeout=30)
        return self.driver.click("policies_pc_first_link")

    def get_first_entry_link_text(self):
        return self.driver.get_text("policies_pc_first_link")

    def get_pcs_policies_page_title(self):
        self.driver.wait_for_object("pcs_policies_page_title", timeout=30)
        return self.driver.get_text("pcs_policies_page_title")
    
    def get_pcs_policies_page_policy_name(self):
        return self.driver.get_text("pcs_policies_page_policy_name")
    
    def verify_pcs_policies_edit_button(self):
        return self.driver.wait_for_object("pcs_policies_edit_button", timeout=20, raise_e=False)
    
    def verify_pcs_policies_delete_button(self):
        return self.driver.wait_for_object("pcs_policies_delete_button", timeout=20, raise_e=False)
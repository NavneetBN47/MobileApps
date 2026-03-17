from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class RemediationsSecrets(WEXFlow):
    """
        Remediations Secrets flow for WEX.
    """
    flow_name = "remediations_secrets"

   ############################ Main Menu verifys ############################

    def verify_remediations_secrets_page(self):
        return self.driver.wait_for_object("remediations_secrets_page_breadcrumb", timeout=30, raise_e=False)
    
    def get_remediations_secrets_page(self):
        return self.driver.wait_for_object("remediations_secrets_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_remediations_secrets_add_button(self):
        return self.driver.wait_for_object("remediations_secrets_add_button", timeout=20, raise_e=False)
    
    def click_remediations_secrets_add_button(self):
        return self.driver.click("remediations_secrets_add_button")
    
    def verify_add_secrets_page_title(self):
        return self.driver.verify_object_string("add_secrets_page_title", timeout=30)
    
    def click_add_secrets_page_cancel_button(self):
        return self.driver.click("add_secrets_page_cancel_button")

    def get_first_entry_link_text(self):
        return self.driver.get_text("_shared_table_entries_with_link")

    def get_secrets_page_title(self):
        self.driver.wait_for_object("secrets_page_title", timeout=30)
        return self.driver.get_text("secrets_page_title")
    
    def get_secrets_page_secret_name(self):
        return self.driver.get_text("secrets_page_secret_name")
    
    def verify_secrets_page_edit_button(self):
        return self.driver.wait_for_object("secrets_page_edit_button", timeout=20, raise_e=False)
    
    def verify_secrets_page_delete_button(self):
        return self.driver.wait_for_object("secrets_page_delete_button", timeout=20, raise_e=False)
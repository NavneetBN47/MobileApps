from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class UpgradesScripts(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "upgrades_scripts"

    #################################### Main Menu - Scripts ####################################

    def verify_scripts_page_breadcrumb(self):
        return self.driver.wait_for_object("scripts_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_scripts_page_title(self):
        return self.driver.wait_for_object("scripts_page_title", timeout=30, raise_e=False).text

    ############################### Remediations - Scripts ####################################

    def verify_remediations_scripts_page(self):
        return self.driver.wait_for_object("remediations_scripts_page_breadcrumb", timeout=30, raise_e=False)
    
    def get_remediations_scripts_page(self):
        return self.driver.wait_for_object("remediations_scripts_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_remediations_scripts_page_library_tab(self):
        return self.driver.wait_for_object("remediations_scripts_page_library_tab", timeout=30, raise_e=False)
    
    def verify_remediations_scripts_page_assignments_tab(self):
        return self.driver.wait_for_object("remediations_scripts_page_assignments_tab", timeout=30, raise_e=False)
    
    def verify_remediations_scripts_page_gallery_tab(self):
        return self.driver.wait_for_object("remediations_scripts_page_gallery_tab", timeout=30, raise_e=False)

    def verify_remediations_scripts_add_button(self):
        return self.driver.wait_for_object("remediations_scripts_add_button", timeout=30, raise_e=False)
    
    def click_remediations_scripts_add_button(self):
        self.driver.click("remediations_scripts_add_button", timeout=30)
        
    def get_add_scripts_page_title(self):
        return self.driver.wait_for_object("add_scripts_page_title", timeout=30, raise_e=False).text

    def click_add_scripts_page_cancel_button(self):
        self.driver.click("add_scripts_page_cancel_button", timeout=30)

    def get_first_entry_link_text(self):
        return self.driver.wait_for_object("_shared_table_entries_with_link", timeout=30, raise_e=False).text
    
    def get_scripts_details_page_title(self):
        return self.driver.wait_for_object("scripts_details_page_title", timeout=30, raise_e=False).text
    
    def get_scripts_details_page_breadcrumb(self):
        return self.driver.wait_for_object("scripts_deatils_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_scripts_page_delete_button(self):
        return self.driver.wait_for_object("scripts_page_delete_button", timeout=20, raise_e=False)
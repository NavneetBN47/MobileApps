from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class UpgradesAlerts(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "upgrades_alerts"

    ################################# Main Menu - Alerts ###################################3333

    def verify_alerts_page_breadcrumb(self):
        return self.driver.wait_for_object("alerts_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_alerts_page_title(self):
        return self.driver.wait_for_object("alerts_page_title", timeout=30, raise_e=False).text

    def verify_active_alerts_page_breadcrumb(self):
        return self.driver.wait_for_object("active_alerts_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_active_alerts_page_alerts_table(self):
        # It verifies active alerts table is loaded and has lists of alerts entry.
        if self.driver.wait_for_object("active_alerts_page_alerts_table", timeout=30, raise_e=False):
            return True
        else:
            return self.verify_active_alerts_page_alerts_table_is_empty_msg()
    
    def verify_active_alerts_page_alerts_table_is_empty_msg(self):
        return self.driver.wait_for_object("active_alerts_page_alerts_table_empty_msg", timeout=30, raise_e=False)

    def verify_alerts_management_page_breadcrumb(self):
        return self.driver.wait_for_object("alerts_management_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_alerts_management_page_alerts_table(self):
        return self.driver.wait_for_object("alerts_management_page_alerts_table", timeout=30, raise_e=False)

    def click_first_checkbox(self):
        return self.driver.click("alerts_management_page_first_checkbox", timeout=30)
    
    def verify_alerts_management_page_enable_alerts_button(self):
        return self.driver.wait_for_object("alerts_management_page_enable_alerts_button", timeout=30, raise_e=False)
    
    def verify_alerts_management_page_disable_alerts_button(self):
        return self.driver.wait_for_object("alerts_management_page_disable_alerts_button", timeout=30, raise_e=False)
    
    def verify_alerts_management_page_delete_alerts_button(self):
        return self.driver.wait_for_object("alerts_management_page_delete_alerts_button", timeout=30, raise_e=False)
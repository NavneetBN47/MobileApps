from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow

class UpgradesLabs(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "upgrades_labs"

    ################################# Main Menu - Labs ###################################3333

    def verify_labs_page_breadcrumb(self):
        return self.driver.wait_for_object("labs_page_breadcrumb", timeout=30, raise_e=False).text
    
    def verify_labs_page_title(self):
        return self.driver.wait_for_object("labs_page_title", timeout=30, raise_e=False).text

    def get_welcome_to_labs_page_title(self):
        return self.driver.wait_for_object("welcome_to_labs_page_title", timeout=30, raise_e=False).text
    
    def get_labs_page_description(self):
        return self.driver.wait_for_object("labs_page_description", timeout=30, raise_e=False).text
    
    def verify_labs_page_fleet_explorer_card(self):
        return self.driver.wait_for_object("labs_page_fleet_explorer_card", timeout=30, raise_e=False)
    
    def get_labs_page_fleet_explorer_card_title(self):
        return self.driver.wait_for_object("labs_page_fleet_explorer_card_title", timeout=30, raise_e=False).text
    
    def verify_labs_page_fleet_explorer_card_try_now_button(self):
        return self.driver.wait_for_object("labs_page_fleet_explorer_card_try_now_button", timeout=30, raise_e=False)
    
    def verify_labs_page_smart_refresh_card(self):
        return self.driver.wait_for_object("labs_page_smart_refresh_card", timeout=30, raise_e=False)
    
    def get_labs_page_smart_refresh_card_title(self):
        return self.driver.wait_for_object("labs_page_smart_refresh_card_title", timeout=30, raise_e=False).text
    
    def verify_labs_page_smart_refresh_card_try_now_button(self):
        return self.driver.wait_for_object("labs_page_smart_refresh_card_try_now_button", timeout=30, raise_e=False)
    
    def verify_labs_page_request_features_card(self):
        return self.driver.wait_for_object("labs_page_request_features_card", timeout=30, raise_e=False)
    
    def get_labs_page_request_features_card_title(self):
        return self.driver.wait_for_object("labs_page_request_features_card_title", timeout=30, raise_e=False).text
    
    def get_labs_page_request_features_card_description(self):
        return self.driver.wait_for_object("labs_page_request_features_card_description", timeout=30, raise_e=False).text
    
    def verify_labs_page_request_features_card_request_button(self):
        return self.driver.wait_for_object("labs_page_request_features_card_request_button", timeout=30, raise_e=False)
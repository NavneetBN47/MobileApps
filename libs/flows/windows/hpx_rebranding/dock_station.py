from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import logging
from SAF.decorator.saf_decorator import screenshot_compare
 
class DockStation(HPXRebrandingFlow):
    flow_name = "dock_station"
 
    def verify_dock_station_icon_show_up(self):
        return self.driver.wait_for_object("dock_station_icon", raise_e = False, timeout = 10)
 
    def verify_contact_us_txt_show_up(self):
        return self.driver.wait_for_object("contact_us_txt", raise_e = False, timeout = 10)

    def verify_product_information_txt_show_up(self):
        return self.driver.wait_for_object("product_information_title", raise_e = False, timeout = 10)
    
    def verify_serial_number_value_show_up(self):
        return self.driver.wait_for_object("serial_number_value", raise_e = False, timeout = 10)
    
    def verify_firewall_version_show_up(self):
        return self.driver.wait_for_object("firewall_version", raise_e = False, timeout = 10)

    def swipe_down_to_product_information_section(self):
        self.scroll_down_to_element("product_information_title")
    
    def hover_over_product_information_section(self):
        self.driver.hover("product_information_title")
    
    def click_copy_serial_number_button(self):
        self.driver.click("copy_serial_number_button", timeout = 10)
        
    def swipe_down_to_contact_us_button(self):
        self.scroll_down_to_element("contact_us_button")
    
    def click_contact_us_button(self): 
        self.driver.click("contact_us_button")

    @screenshot_compare(include_param=["mode"])
    def verify_get_help_card_show_up(self, mode):
        return self.driver.wait_for_object("get_help_card", raise_e = False, timeout = 10)
    
    def swipe_down_to_product_warranty_details(self):
        self.scroll_down_to_element("get_warranty_status_button")
        
    @screenshot_compare(include_param=["mode"])
    def verify_get_warranty_details_show_up(self, mode):
        return self.driver.wait_for_object("get_warranty_status_button", raise_e = False, timeout = 10)

from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time

class PcConnect(HPXFlow):
    flow_name = "pc_connect"

    def verify_5G_module_on_pcdevice_page(self):
        return self.driver.get_attribute("5G_module_from_pc_device_page","Name")

    def click_5G_module_on_pcdevice_page(self):
        return self.driver.click("5G_module_from_pc_device_page")    

    def verify_5G_header(self):
        return self.driver.get_attribute("5G_header","Name")  

    def verify_5G_connectivity_text(self):
        return self.driver.get_attribute("5G_connectivity_text","Name")  

    def verify_esim_text(self):
        return self.driver.get_attribute("esim_text","Name") 

    def verify_tmobile_text(self):
        return self.driver.get_attribute("t_mobile_text","Name")     

    def verify_sim_number_text(self):
        return self.driver.get_attribute("sim_number_text","Name")  

    def verify_usage_data_text(self):
        return self.driver.get_attribute("usage_data_text","Name")   
    
    def verify_usage_datain_last_30_days_text(self):
        return self.driver.get_attribute("usage_data_description","Name")

    def verify_coverage_map_text(self):
        return self.driver.get_attribute("coverage_map_text","Name")

    def verify_network_and_internet_settings_text(self):
        return self.driver.get_attribute("network_and_internet_settings","Name")     

    def click_network_and_internet_settings(self):
        return self.driver.click("network_and_internet_settings")             

    def click_usage_data(self):
        return self.driver.click("usage_data_tooltip")
        return self.driver.get_attribute("usage_data_tooltip","Name") 
       
    def click_coverage_map(self):
        return self.driver.click("coverage_map_tooltip")
        return self.driver.get_attribute("coverage_map_tooltip","Name")
    
    def click_toggle_5G_connectivity(self):
        self.driver.click("5G_connectivity_toggle")

    def get_toggle_notification_state(self):
        return self.driver.get_attribute("5G_connectivity_toggle","Toggle.ToggleState")    

    def verify_5g_network_connection_alert(self):
        return self.driver.get_attribute("5G_network_connection_popup","Name",timeout=60)

    def verify_5g_network_disconnected_alert(self):
        return self.driver.get_attribute("5G_network_disconnect_popup","Name",timeout=60)
   
    def verify_system_network_and_internet_page(self):
        return self.driver.get_attribute("system_network_and_internet","Name")

    def click_system_close_button(self):
        self.driver.click("close_system_network_and_internet_page")
    
    def click_system_tray_icon(self):
        self.driver.click("system_tray_icon")   
    
    def click_cellular_icon_arrow(self):
        self.driver.click("cellular_icon_arrow")   

    def click_cellular_network_bar(self):
        self.driver.click("cellular_network_bar")   

    def click_system_cellular_network_toggle(self):
        self.driver.click("system_cellular_network_toggle")   

    def system_cellular_network_toggle_state(self):
        return self.driver.get_attribute("system_cellular_network_toggle","Toggle.ToggleState")
    
    def verify_cellular_text(self):
        return self.driver.get_attribute("cellular_text","Name")
    
    def verify_cellular_connection(self):
        return self.driver.get_attribute("network_settings_system_cellular_status_text","Name")
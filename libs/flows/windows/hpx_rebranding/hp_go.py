from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from SAF.decorator.saf_decorator import screenshot_compare

class HPGo(HPXRebrandingFlow):
    flow_name = "hp_go"

    def verify_hp_go_title_on_hp_go_page(self):
        return self.driver.wait_for_object("hp_go_title", timeout=10, raise_e=False)
    
    def verify_hp_go_information_txt_on_hp_go_page(self):
        return self.driver.wait_for_object("hp_go_information_txt", timeout=10, raise_e=False)

    def verify_hp_go_connection_txt_on_hp_go_page(self):
        return self.driver.wait_for_object("connection_txt", timeout=10, raise_e=False)
    
    def verify_hpgo_card_show_up(self):
        return self.driver.wait_for_object("hpgo_card", timeout=10, raise_e=False)
    
    def click_hpgo_card(self):
        self.driver.click("hpgo_card", timeout=10)
    
    def get_hp_go_title(self):
        return self.driver.get_attribute("hp_go_title", "Name", timeout=10)
    
    def get_hp_go_information_txt(self):
        return self.driver.get_attribute("hp_go_information_txt", "Name", timeout=10)

    def get_connection_txt(self):
        return self.driver.get_attribute("connection_txt", "Name", timeout=10)

    def get_connection_hp_go(self):
        return self.driver.get_attribute("connection_hp_go", "Name", timeout=10)
    
    def get_hp_go_status_text(self):
        return self.driver.get_attribute("hp_go_status_text", "Name", timeout=10)
    
    def get_hp_go_usage_text(self):
        return self.driver.get_attribute("hp_go_usage_text", "Name", timeout=10)

    def verify_eid_number(self):
        return self.driver.wait_for_object("eid_number", timeout=10, raise_e=False)

    def verify_eid_copy_btn(self):
        return self.driver.wait_for_object("eid_copy_btn", timeout=10, raise_e=False)

    def click_eid_copy_btn(self):
        self.driver.click("eid_copy_btn", timeout=10)
    
    def get_eid_number(self):
        return self.driver.get_attribute("eid_number", "Name", timeout=10)

    def verify_hp_go_in_system_tray(self):
        self.driver.click("system_tray_icon", timeout=10)
        return self.driver.wait_for_object("system_tray_hp_go_tile", timeout=10, raise_e=False)
    
    @screenshot_compare(root_obj="hp_go_module_image",include_param=["machine_type"],pass_ratio=0.01)
    def verify_hp_go_image(self,machine_type,raise_e=True):
        element = self.driver.wait_for_object("hp_go_module_image", timeout=10, raise_e=raise_e)
        return self.driver.wait_for_object("eid_number", raise_e=raise_e, timeout=10)
        
    def verify_hp_go_status_text(self):
        return self.driver.wait_for_object("hp_go_status_text", timeout=10, raise_e=False)
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow


class PresenceSensing(HPXRebrandingFlow):
    flow_name = "presence_sensing"


    def verify_turn_off_my_screen_btn_show(self):
        return self.driver.wait_for_object("turn_off_my_screen_btn",raise_e=False, timeout = 10)
    
    def verify_wake_my_device_btn_show(self):
        return self.driver.wait_for_object("wake_my_device_btn",raise_e=False, timeout = 10)
    
    def verify_dim_my_screen_btn_show(self):
        return self.driver.wait_for_object("dim_my_screen_btn",raise_e=False, timeout = 10)
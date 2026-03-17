from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow

class InstantInkSMB(InstantinkFlow):
    flow_name="instantink_smb"
    
    def verify_promotional_banner(self):
        return self.driver.wait_for_object("instantink_vulcan_banner")
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow

class DevicesDetailsPCMFE(SmartFlow):
    flow_name = "devices_details_pc_mfe"

# *********************************************************************************
#                                VERIFICATION FLOWS                               *
# *********************************************************************************

    def verify_audio_card_show_up(self):
        return self.driver.wait_for_object("audio_card")
    


# *********************************************************************************
#                                ACTION FLOWS                                     *
# *********************************************************************************

    def click_audio_card(self):
        return self.driver.click("audio_card")

import time
import random
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class Filltanks(OWSFlow):
    flow_name = "fill_tanks"
    flow_url = "fill-ink-tanks"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def select_ink_bottle_type(self):
        bottle_type = ["screw_cap", "flip_cap"]
        bottle = random.choice(bottle_type)
        self.driver.click(bottle)
        self.driver.click("_shared_carousel_screen_continue_or_skip_btn")
        return bottle
    
    def verify_ink_tank_installed_popup(self, bottle):
        if bottle == "flip_cap":
            self.driver.wait_for_object("continue_btn", displayed=False)
            self.driver.click("continue_btn")
        return self.driver.wait_for_object("fill_ink_tanks_popup")
    
    @screenshot_compare(root_obj="fill_ink_tanks_popup",at_end=False)
    def fill_tanks_click_continue(self):
        self.driver.wait_for_object("fill_ink_tanks_popup_continue_btn")
        return self.driver.click("fill_ink_tanks_popup_continue_btn")
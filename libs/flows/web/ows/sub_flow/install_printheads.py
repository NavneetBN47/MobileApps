import time
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class Printheads(OWSFlow):
    flow_name = "print_heads"
    flow_url = "install-pha"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project)  
    
    def verify_install_printheads_popup(self):
        return self.driver.wait_for_object("install_printheads_popup")
    
    @screenshot_compare(root_obj="install_printheads_popup",at_end=False)
    def pha_click_continue(self):
        self.driver.wait_for_object("install_printheads_popup_continue_btn")
        return self.driver.click("install_printheads_popup_continue_btn")
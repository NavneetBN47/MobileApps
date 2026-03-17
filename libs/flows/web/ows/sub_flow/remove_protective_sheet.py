from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class RemoveProtectiveSheet(OWSFlow):
    flow_name = "remove_protective_sheet"
    flow_url = "remove-protective-sheet"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project)   
    
    def click_continue(self):
        return self.driver.click("remove_protective_sheet_continue")
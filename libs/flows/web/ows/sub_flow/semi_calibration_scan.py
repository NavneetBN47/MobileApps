import time
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow, AndroidOWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class SemiCalibrationScan(OWSFlow):
    flow_name = "semi_calibration_scan"
    flow_url = "scan-alignment"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def navigate_semi_calibration_scan(self):
        for _ in self.get_total_carousel_pages():
            self.scroll_carousel()
            time.sleep(3)
            
    def verify_success_popup(self, timeout=10):
        self.driver.wait_for_object("scan_success_popup")
        self.driver.wait_for_object("scan_success_ok_btn", timeout=timeout)
        return True
    
    @screenshot_compare(root_obj="scan_success_popup",at_end=False)
    def click_success_popup_ok(self):
        return self.driver.click("scan_success_ok_btn")

class AndroidSemiCalibrationScan(SemiCalibrationScan, AndroidOWSFlow):
    """
    Create this class for using functions in AndroidOWSFlow, not from base OWS flow.
    For example: scroll_carousel()
    """
    platform = "android"
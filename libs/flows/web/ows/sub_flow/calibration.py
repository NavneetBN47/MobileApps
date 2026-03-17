from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class Calibration(OWSFlow):
    flow_name = "calibration"
    flow_url = "auto-calibration"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_calibration(self):
        return self.driver.wait_for_object("calibration_title", timeout=15)
    
    @screenshot_compare(root_obj="skip_alignment_link")
    def click_skip_alignment(self, raise_e=False):
        return self.driver.click("skip_alignment_link", timeout=60, raise_e=raise_e)
    
    @screenshot_compare(at_end=False)
    def click_start_calibration(self):
        return self.driver.click("start_calibration_btn")
    
    def verify_failure_screen(self):
        return self.driver.wait_for_object("full_screen_error_obj")

    def skip_calibration(self, timeout=180):
        """
        Wait 180s or more for skip alignment btn then click it
        """
        self.driver.wait_for_object("skip_installing_btn", timeout=timeout)
        return self.driver.click("skip_installing_btn")

class Calibration2_0(Calibration):
    flow_url="offer-calibration"
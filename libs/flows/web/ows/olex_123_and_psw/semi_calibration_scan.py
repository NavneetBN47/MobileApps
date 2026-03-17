import time
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class ScanCalibrationTrafficDirector(OWSFlow):
    flow_name = "td_scan_calibration"
    flow_url = "scan-alignment"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_scan_alignment_step(self):
        """
        Verify Print Alignement step.
        """
        self.driver.wait_for_object("title_header")

    def verify_animation_card_step(self, carousal):
        """
        Verify Animation Step.
        """
        self.driver.wait_for_object("animation_card_step_{}".format(carousal))

    def verify_card_instructions(self, instruction):
        """
        Verify Instruction on every card of Alignement step.
        """
        self.driver.wait_for_object("animation_card_instruction_{}".format(instruction))
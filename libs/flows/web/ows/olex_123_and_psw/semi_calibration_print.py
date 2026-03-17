from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class PrintCalibrationTrafficDirector(OWSFlow):
    flow_name = "td_calibration"
    file_path = __file__
    flow_url = "alignment"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_print_alignment_step(self):
        """
        Verify Print Alignement step.
        """
        self.driver.wait_for_object("title_header")

    def verify_alignment_card_image(self, image_number):
        self.driver.click(f"alignment_card_image_{image_number}")
        self.driver.process_screenshot(self.file_path, (f"alignment_card_image_{image_number}_{self.get_printer_profile()}"), 
                                       root_obj="alignment_card_image_{}".format(image_number))

    def verify_alignment_card_instruction(self, instruction):
        self.driver.wait_for_object("alignment_card_instruction_{}".format(instruction))

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
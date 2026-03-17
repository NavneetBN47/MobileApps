from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path

class InstallInkTrafficDirector(OWSFlow):
    flow_name = "td_install_ink"
    flow_url = "install-ink"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_install_ink_step_td(self, displayed=False):
        """
        Verify Install Ink step for Traffic Director Marconi.
        """
        self.driver.wait_for_object("header", displayed=displayed)

    def verify_install_ink_card_image(self, image_number):
        self.driver.click(f"install_ink_card_image_{image_number}")
        self.driver.process_screenshot(self.file_path, (f"install_ink_card_image_{image_number}_{self.get_printer_profile()}"), 
                                       root_obj=f"install_ink_card_image_{image_number}")

    def verify_install_ink_card_instruction(self, instruction):
        self.driver.wait_for_object("install_ink_card_instruction_{}".format(instruction))
    
    def verify_animation_card_step(self, carousal):
        """
        Verify Animation in cards showsing visual of the Instruction.
        """
        self.driver.wait_for_object("animation_card_step_{}".format(carousal))

    def verify_card_instructions(self, instruction):
        """
        Verify Instruction on every card of install ink step.
        """
        self.driver.wait_for_object("animation_card_instruction_{}".format(instruction))

    def verify_already_install_ink_button(self):
        self.driver.wait_for_object("skip_button_text")
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path


class LoadPaperTrafficDrector(OWSFlow):
    flow_name = "td_load_paper"
    flow_url = "load-paper"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_td_load_paper_step(self):
        """
        Verify Load Paper step.
        """
        self.driver.wait_for_object("load_paper_card")

    def verify_card_slider(self):
        """
        verify carousaul card.
        """
        self.driver.wait_for_object("card_slider_content")

    def click_view_anumations_button(self):
        self.driver.click("view_animations_button")

    def verify_load_paper_card_image(self, image_number):
        self.driver.click(f"load_paper_card_image_{image_number}")
        self.driver.process_screenshot(self.file_path, (f"load_paper_card_image_{image_number}_{self.get_printer_profile()}"), 
                                       root_obj=f"load_paper_card_image_{image_number}")

    def verify_load_paper_card_instruction(self, instruction):
        self.driver.wait_for_object("load_paper_card_instruction_{}".format(instruction))
    
    def verify_animation_card_step(self, carousal):
        self.driver.wait_for_object("animation_card_step_{}".format(carousal))
    
    def verify_animation_card_instruction(self, instruction):
        """
        Verify animation card instruction.
        """
        self.driver.wait_for_object("animation_card_instruction_{}".format(instruction))

    def verify_skip_load_paper_step(self):
        self.driver.wait_for_object("skip_button_text")
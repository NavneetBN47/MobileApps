import time
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow, AndroidOWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.ma_misc import ma_misc

class LoadPaper(OWSFlow):
    flow_name = "load_paper"
    flow_url = "load-paper"
    file_path = __file__
    folder_name = get_subfolder_path(__file__, OWSFlow.project) 

    def navigate_load_paper(self):
        for _ in range(self.get_total_carousel_pages()-1):
            self.scroll_carousel()
            time.sleep(3)
        self.paper_click_continue()
    
    def paper_click_continue(self):
        return self.driver.click("paper_continue_btn", timeout=10)


class LoadPaperTrafficDrector(LoadPaper):
    flow_name = "td_load_paper"
    flow_url = "load-paper"

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
        self.driver.wait_for_object("load_paper_card_image_{}".format(image_number))
        self.driver.process_screenshot(self.file_path, ("load_paper_card_image_{}").format(image_number), root_obj="load_paper_card_image_{}".format(image_number))

    def verify_load_paper_card_instruction(self, instruction):
        self.driver.wait_for_object("load_paper_card_instruction_{}".format(instruction))
    
    def verify_animation_card_step(self, carousal):
        """
        Verify animation card instruction.
        """
        self.driver.wait_for_object(f"animation_card_step_{carousal}")
    
    def verify_animation_card_instruction(self, instruction):
        """
        Verify animation card instruction.
        """
        self.driver.wait_for_object("animation_card_instruction_{}".format(instruction))

    def verify_skip_load_paper_step(self):
        self.driver.wait_for_object("skip_button_text")

class AndroidLoadPaper(LoadPaper, AndroidOWSFlow):
    """
    Create this class for using functions in AndroidOWSFlow, not from base OWS flow.
    For example: scroll_carousel()
    """
    platform = "android"
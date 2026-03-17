from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time
from SAF.decorator.saf_decorator import screenshot_compare

class VideoControl(HPXRebrandingFlow):
    flow_name = "video_control"

    def verify_camera_pop_up(self):
        return self.driver.wait_for_object("camera_pop_up", raise_e=False, timeout=10)
    
    def verify_camera_description_text(self):
        return self.driver.wait_for_object("camera_pop_up_description", timeout=10)
    
    def verify_camera_header_text(self):
        return self.driver.wait_for_object("camera_pop_up_header", timeout=10)
    
    def get_camera_pop_up_header(self):
        return self.driver.get_attribute("camera_pop_up_header", "Name", timeout = 20)
    
    def verify_camera_pop_up_cancel_button(self):
        return self.driver.wait_for_object("camera_pop_up_cancel_button", timeout=10)
    
    def click_camera_pop_up_cancel_button(self):
        self.driver.click("camera_pop_up_cancel_button", timeout=10)
    
    def verify_camera_pop_up_continue_button(self):
        return self.driver.wait_for_object("camera_pop_up_continue_button", raise_e=False, timeout=10)
    
    def click_camera_pop_up_continue_button(self):
        self.driver.click("camera_pop_up_continue_button", timeout=10)

    def verify_hp_presence_window_pop_up(self):
        return self.driver.wait_for_object("hp_presence_window_pop_up", raise_e=False, timeout=10) is not False
    
    def click_camera_pop_up_yes_button(self):
        self.driver.click("poly_camera_yes_button", timeout=10)
    
    def verify_poly_camera_window_pop_up(self):
        return self.driver.wait_for_object("poly_camera_window_pop_up", raise_e=False, timeout=10) is not False
    
    def get_poly_camera_contextual_text(self):
        return self.driver.get_attribute("poly_camera_contextual_text", "Name", timeout = 20)# this may fail, if it happens will have to use name property

    def verify_auto_frame_title_show_up(self):
        return self.driver.wait_for_object("auto_frame_title", raise_e=False,  timeout=20)
    
    def verify_tutorial_next_button_show(self):
        return self.driver.wait_for_object("tutorial_next_button", raise_e=False, timeout=10)

    def click_tutorial_next_button(self):
        self.driver.click("tutorial_next_button", timeout=10)

    def verify_video_card_show_up(self):
        return self.driver.wait_for_object("video_card", raise_e=False, timeout=10)

    def click_video_card(self):
        self.driver.click("video_card", timeout=10)
        
    def click_cancel_button_on_video_dialog(self):
        self.driver.click("cancel_button_on_video_dialog", timeout=10)

    def get_hp_presence_video_contextual_text(self):
        return self.driver.get_attribute("hp_presence_video_contextual_text", "Name", timeout = 20)# this may fail, if it happens will have to use name property    
    
    @screenshot_compare(include_param=["machine_name", "page_number","mode"], pass_ratio=0.01)
    def verify_video_control_page(self, machine_name, page_number, element, mode, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)

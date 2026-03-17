import logging
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time
from SAF.decorator.saf_decorator import screenshot_compare
from selenium.webdriver.common.keys import Keys

class TaskGroup(HPXRebrandingFlow):
    flow_name = "task_group"

    def verify_task_group_create_new_show(self):
        return self.driver.wait_for_object("task_group_create_new_button", raise_e=False, timeout=20)
    
    def verify_task_group_title_show(self):
        return self.driver.wait_for_object("task_group_title", raise_e=False, timeout=30)

    def verify_task_group_description_show(self):
        return self.driver.wait_for_object("task_group_description", raise_e=False, timeout=20)

    def verify_task_group_video_container_show(self):
        return self.driver.wait_for_object("task_group_video_container", raise_e=False, timeout=20)

    def click_task_group_create_new_button(self):
        self.driver.click("task_group_create_new_button")
        if self.verify_privacy_pop_window_agree_button_show():
            time.sleep(2)
            self.click_privacy_pop_window_agree_button()
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_task_group_create_new_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("task_group_create_new_button", raise_e=False, timeout=20)

    @screenshot_compare(include_param=["machine_name", "page_number", "color"])
    def verify_create_new_button__show_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_task_group_create_new_show_scale(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    
    def verify_privacy_pop_window_title_show(self):
        return self.driver.wait_for_object("privacy_pop_windows_title", raise_e=False, timeout=10)
    
    def verify_privacy_pop_window_desc_show(self):
        return self.driver.wait_for_object("privacy_pop_windows_desc", raise_e=False, timeout=10)

    def verify_privacy_pop_window_decline_button_show(self):
        return self.driver.wait_for_object("privacy_pop_windows_decline_button", raise_e=False, timeout=10)

    def verify_privacy_pop_window_agree_button_show(self):
        return self.driver.wait_for_object("privacy_pop_windows_agree_button", raise_e=False, timeout=10)

    def click_edit_task_group_save_button(self):
        self.driver.click("edit_task_group_save_button")

    def verify_edit_task_group_save_button_show(self):
        return self.driver.wait_for_object("edit_task_group_save_button", raise_e=False, timeout=10)

    def click_privacy_pop_windows_decline_button(self):
        self.driver.click("privacy_pop_windows_decline_button")
    
    def click_privacy_pop_window_agree_button(self):
        self.driver.click("privacy_pop_windows_agree_button")
    
    def input_short_key_name(self, name):
        self.driver.click("shortkey_name_text_box")
        self.driver.clear_text("shortkey_name_text_box")
        self.driver.send_keys("shortkey_name_text_box", name)
    
    def click_shortkey_dropdown(self):
        self.driver.click("shortkey_dropdown")
    
    def select_shortkey_shift12(self):
        self.driver.click("shortkey_shift12")
    
    def verify_task_arrow_icon_show(self):
        return self.driver.wait_for_object("task_arrow_icon", raise_e=False, timeout=10)   
    
    def click_task_arrow_icon(self):
        self.driver.click("task_arrow_icon")

    def click_delete_task_button(self):
        self.driver.click("task_delete_icon")

    def verify_delete_pop_window_checkbox_show(self):
        return self.driver.wait_for_object("delete_pop_window_checkbox", raise_e=False, timeout=10)
    
    def click_delete_pop_window_continue_button(self):
        self.driver.click("delete_pop_window_continue_button")
    
    def select_shortkey_ctrl12(self):
        self.driver.click("shortkey_ctrl12")
    
    def select_shortkey_alt12(self):
        self.driver.click("shortkey_alt12")
    
    def verify_delete_task_button_show(self):
        return self.driver.wait_for_object("task_delete_icon", raise_e=False, timeout=10)
    
    def verify_delete_pop_window_cancel_button_show(self):
        return self.driver.wait_for_object("delete_pop_window_cancel_button", raise_e=False, timeout=10)

    def verify_delete_pop_window_continue_button_show(self):
        return self.driver.wait_for_object("delete_pop_window_continue_button", raise_e=False, timeout=10)
    
    def select_delete_pop_window_checkbox(self):
        self.driver.click("delete_pop_window_checkbox")
    
    def verify_ms_store_delete_icon_show(self):
        return self.driver.wait_for_object("ms_store_delete_icon", raise_e=False, timeout=10)
    
    def click_ms_store_delete_icon(self):
        self.driver.click("ms_store_delete_icon")

    def click_task_arrow_terminal_icon(self):
        self.driver.click("task_arrow_terminal_icon")
    
    def verify_task_arrow_terminal_icon_show(self):
        return self.driver.wait_for_object("task_arrow_terminal_icon", raise_e=False, timeout=10)
    
    def verify_how_it_works_link_show(self):
        return self.driver.wait_for_object("how_it_works_link", raise_e=False, timeout=10)
    
    def click_how_it_works_link(self):
        self.driver.click("how_it_works_link")
    
    def verify_how_to_use_task_group_title_show(self):
        return self.driver.wait_for_object("how_to_use_task_group_title", raise_e=False, timeout=10)
    
    def verify_how_to_use_task_group_desc_show(self):
        return self.driver.wait_for_object("how_to_use_task_group_desc", raise_e=False, timeout=10)
    
    def click_how_to_use_task_group_understand_button(self):
        self.driver.click("how_to_use_task_group_understand_button")
    
    def click_task_group_create_new_button_with_app(self):
        self.driver.click("task_group_create_new_button_with_app")

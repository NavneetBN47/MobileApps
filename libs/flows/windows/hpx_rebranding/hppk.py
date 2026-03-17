from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys
import time
from SAF.decorator.saf_decorator import screenshot_compare

class HPPK(HPXRebrandingFlow):
    flow_name = "hppk"

    def verify_programmabe_header_visible(self):
        return self.driver.wait_for_object("programmable_key_header", raise_e=False, timeout = 20) is not False

    def verify_programmabe_card_visible(self):
        return self.driver.wait_for_object("progkey_menu_card", raise_e=False, timeout = 5) is not False

    def verify_support_key_card_visible(self):
        return self.driver.wait_for_object("supportkey_menu_card", raise_e=False, timeout = 5) is not False

    def verify_pc_device_key_card_visible(self):
        return self.driver.wait_for_object("pcdevicekey_menu_card", raise_e=False, timeout = 5) is not False

    def verify_programmabe_header_text(self):
        return self.driver.get_attribute("programmable_key_header","Name", timeout = 20)

    def verify_progkey_menucard_shift_visible(self):
        return self.driver.wait_for_object("progkey_menucard_shift", raise_e=False, timeout = 10) is not False

    def verify_progkey_menucard_ctl_visible(self):
        return self.driver.wait_for_object("progkey_menucard_ctl", raise_e=False, timeout = 10) is not False

    def verify_progkey_menucard_alt_visible(self):
        return self.driver.wait_for_object("progkey_menucard_alt", raise_e=False, timeout = 10) is not False

    def verify_progkey_info_icon_visible(self):
        return self.driver.wait_for_object("title_info_icon", raise_e=False, timeout = 10) is not False

    def click_progkey_menucard_arrow_btn(self):
        self.driver.click("progkey_menucard_arrow_btn", timeout=20)

    def click_progkey_menucard_shift_arrow_btn(self):
        self.driver.click("progkey_menucard_shift_arrow_btn", timeout=20)

    def click_progkey_menucard_ctl_arrow_btn(self):
        self.driver.click("progkey_menucard_ctl_arrow_btn", timeout = 20)

    def click_progkey_menucard_alt_arrow_btn(self):
        self.driver.click("progkey_menucard_alt_arrow_btn", timeout=20)

    def verify_assign_programmable_header_text(self):
        return self.driver.get_attribute("assign_prog_key_header","Name", timeout = 20)

    def verify_automation_text(self):
        return self.driver.get_attribute("automation_title","Name", timeout = 20)

    def verify_key_sequence_text(self):
        return self.driver.get_attribute("key_sequence_title","Name", timeout = 20)

    def verify_text_input_text(self):
        return self.driver.get_attribute("text_input_title","Name", timeout = 20)

    def verify_programmable_key_text(self):
        return self.driver.get_attribute("hp_prog_key_title","Name", timeout = 20)

    def verify_automation_radio_btn_visible(self):
        return self.driver.wait_for_object("automation_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_key_sequence_radio_btn_visible(self):
        return self.driver.wait_for_object("key_sequence_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_text_input_radio_btn_visible(self):
        return self.driver.wait_for_object("text_input_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_programmable_key_radio_button_is_selected(self):
        return self.driver.get_attribute("hp_prog_key_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_key_sequence_text(self):
        return self.driver.get_attribute("key_sequence_title","Name", timeout = 20)

    def verify_text_input_text(self):
        return self.driver.get_attribute("text_input_title","Name", timeout = 20)

    def verify_shift_key_header_text(self):
        return self.driver.get_attribute("prog_shift_key_header","Name", timeout = 20)

    def verify_shift_automation_radio_btn_visible(self):
        return self.driver.wait_for_object("shift_automation_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_shift_key_sequence_radio_btn_visible(self):
        return self.driver.wait_for_object("shift_sequence_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_shift_text_input_radio_btn_visible(self):
        return self.driver.wait_for_object("shift_text_input_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_shift_not_assigned_radio_button_is_selected(self):
        return self.driver.get_attribute("shift_not_assigned_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_ctl_key_header_text(self):
        return self.driver.get_attribute("prog_ctl_key_header","Name", timeout = 20)

    def verify_ctl_automation_radio_btn_visible(self):
        return self.driver.wait_for_object("ctl_automation_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_ctl_key_sequence_radio_btn_visible(self):
        return self.driver.wait_for_object("ctl_sequence_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_ctl_text_input_radio_btn_visible(self):
        return self.driver.wait_for_object("ctl_text_input_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_ctl_not_assigned_radio_button_is_selected(self):
        return self.driver.get_attribute("ctl_not_assigned_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_alt_key_header_text(self):
        return self.driver.get_attribute("prog_alt_key_header","Name", timeout = 20)

    def verify_alt_automation_radio_btn_visible(self):
        return self.driver.wait_for_object("alt_automation_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_alt_key_sequence_radio_btn_visible(self):
        return self.driver.wait_for_object("alt_sequence_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_alt_text_input_radio_btn_visible(self):
        return self.driver.wait_for_object("alt_text_input_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_alt_not_assigned_radio_button_is_selected(self):
        return self.driver.get_attribute("alt_not_assigned_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def click_hpone_progkey_menucard_arrow_btn(self):
        self.driver.click("hpone_progkey_menucard_arrow_btn", timeout = 20)

    def click_hpone_pc_device_menucard_arrow_btn(self):
        self.driver.click("hpone_pc_device_menucard_arrow_btn", timeout = 20)

    def click_hpone_support_key_menucard_arrow_btn(self):
        self.driver.click("hpone_support_key_menucard_arrow_btn", timeout = 20)

    def verify_pc_device_key_header_text(self):
        return self.driver.get_attribute("pc_device_key_header","Name", timeout = 20)

    def verify_pc_device_automation_radio_btn_visible(self):
        return self.driver.wait_for_object("pc_device_key_automation_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_pc_device_sequence_radio_btn_visible(self):
        return self.driver.wait_for_object("pc_device_key_sequence_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_pc_device_text_input_radio_btn_visible(self):
        return self.driver.wait_for_object("pc_device_key_text_input_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_hp_pc_device_radio_button_is_selected(self):
        return self.driver.get_attribute("hp_pc_device_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_support_key_header_text(self):
        return self.driver.get_attribute("prog_support_key_header","Name", timeout = 20)

    def verify_support_key_automation_radio_btn_visible(self):
        return self.driver.wait_for_object("support_key_automation_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_support_key_sequence_radio_btn_visible(self):
        return self.driver.wait_for_object("support_key_sequence_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_support_key_text_input_radio_btn_visible(self):
        return self.driver.wait_for_object("support_key_text_input_radio_btn", raise_e=False, timeout = 10) is not False

    def verify_hp_support_radio_button_is_selected(self):
        return self.driver.get_attribute("hp_support_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def click_prog_key_back_btn(self):
        self.driver.click("prog_key_back_btn", timeout=10)

    def click_automation_radio_btn(self):
        self.driver.click("automation_radio_btn", timeout = 20)

    def click_automation_dropbox_btn(self):
        self.driver.click("automation_dropbox", timeout = 20)

    def verify_add_action_text_visible(self):
        return self.driver.wait_for_object("automation_add_action_title", raise_e=False, timeout = 10) is not False

    def verify_automation_dropdown_visible(self):
        return self.driver.wait_for_object("automation_dropbox", raise_e=False, timeout = 10) is not False

    def verify_automation_dropbox_value_application(self):
        return self.driver.get_attribute("automation_dropbox_value_application","Name", timeout = 20)

    def verify_automation_dropbox_value_website(self):
        return self.driver.get_attribute("automation_dropbox_value_website","Name", timeout = 20)

    def verify_automation_dropbox_value_folder(self):
        return self.driver.get_attribute("automation_dropbox_value_folder","Name", timeout = 20)

    def verify_automation_dropbox_value_file(self):
        return self.driver.get_attribute("automation_dropbox_value_file","Name", timeout = 20)

    def click_prog_key_detail_back_btn(self):
        self.driver.click("prog_key_detail_back_btn", timeout=10)

    def click_application_from_dropdown(self):
        self.driver.click("automation_dropbox_value_application", timeout = 20)

    def select_admin_tool_from_application_dropdown(self):
        self.driver.click("prog_key_detail_admin_app", timeout = 20)

    def click_enter_key(self,element):
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.ENTER)

    def click_esc_key(self,element):
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.ESCAPE)

    def verify_app_delete_btn_visible(self):
        return self.driver.wait_for_object("automation_list_delete_btn", raise_e=False, timeout = 10) is not False

    def click_app_delete_btn(self):
        self.driver.click("automation_list_delete_btn", timeout = 20)

    def verify_admin_tool_app_visible(self):
        return self.driver.wait_for_object("automation_list_admin_tool_app", raise_e=False, timeout = 10) is not False
    
    def run_command_to_launch_hppk(self,command):
        self.driver.send_keys("run_text_box",command)
        self.driver.send_keys("search_bar_on_windows", Keys.ENTER)
    
    def click_search_bar_on_windows(self):
        self.driver.click("search_bar_on_windows")

    def search_bar_on_windows(self,app_name):
        self.driver.clear_text("search_bar_on_windows")
        self.driver.send_keys("search_bar_on_windows", app_name)
        self.driver.send_keys("search_bar_on_windows", Keys.ENTER)
    
    def click_website_from_dropdown(self):
        self.driver.click("automation_dropbox_value_website", timeout = 20)
    
    def add_website(self,website):
        self.driver.clear_text("website_text_field")
        self.driver.send_keys("website_text_field",website)

    def verify_website_icon_visible(self):
        return self.driver.wait_for_object("website_icon", raise_e=False, timeout = 10)
    
    def click_website_cancel_button(self):
        self.driver.click("website_cancel_button", timeout = 20)
    
    def verify_assign_programmable_header(self):
        return self.driver.wait_for_object("assign_prog_key_header", raise_e=False, timeout = 10)
    
    def input_key_sequence(self,key_sequence):
        self.driver.clear_text("key_sequence_text_field")
        self.driver.send_keys("key_sequence_text_field", key_sequence)
    
    def click_key_sequence_save_button(self):
        self.driver.click("key_sequence_save_button", timeout = 20)
    
    def get_key_sequence_config_value(self):
        return self.driver.get_attribute("progkey_menu_card_value","Name", raise_e = False, timeout = 20)
    
    def click_key_sequence_radio_btn(self):
        self.driver.click("key_sequence_radio_btn", timeout = 10)
    
    def click_application_list_cancel_button(self):
        self.driver.click("prog_key_detail_app_cancel_btn", timeout = 10)
    
    def delete_key_sequence(self):
        self.driver.click("delete_key_sequence_button", timeout = 10)
    
    def verify_key_sequence_delete_icon_show(self):
        return self.driver.wait_for_object("delete_key_sequence_button", raise_e=False, timeout = 10)
    
    def click_text_input_radio_btn(self):
        self.driver.click("text_input_radio_btn", timeout = 10)
    
    def input_text_input(self,text_input):
        self.driver.click("text_input_area", timeout = 20)
        self.driver.clear_text("text_input_area")
        self.driver.send_keys("text_input_area", text_input)
    
    def click_key_text_input_save_button(self):
        self.driver.click("text_input_save_button", timeout = 20)

    def click_hp_support_key_automation_radio_btn(self):
        self.driver.click("support_key_automation_radio_btn", timeout = 20)

    def click_automation_pcpk_radio_btn(self):
        self.driver.click("pc_device_key_automation_radio_btn", timeout = 20)        
    
    def click_hp_prog_key_radio_btn(self):
        self.driver.click("hp_prog_key_radio_btn", timeout = 20)

    def click_hp_support_spk_radio_btn(self):
        self.driver.click("hp_support_radio_btn", timeout = 20)

    def click_text_input_spk_radio_btn(self):
        self.driver.click("support_key_text_input_radio_btn", timeout = 20)

    def click_key_sequence_spk_radio_btn(self):
        self.driver.click("support_key_sequence_radio_btn", timeout = 20)

    def click_key_sequence_pcpk_radio_btn(self):
        self.driver.click("pc_device_key_sequence_radio_btn", timeout = 20)

    def click_text_input_pcpk_radio_btn(self):
        self.driver.click("pc_device_key_text_input_radio_btn", timeout = 20)

    def click_hp_pc_device_radio_btn(self):
        self.driver.click("hp_pc_device_radio_btn", timeout = 20)

    def click_shift_plus_pk_automation_radio_btn(self):
        self.driver.click("shift_automation_radio_btn", timeout = 20)

    def click_shift_plus_pk_key_sequence_radio_btn(self):
        self.driver.click("shift_sequence_radio_btn", timeout = 20)

    def click_shift_plus_pk_text_input_radio_btn(self):
        self.driver.click("shift_text_input_radio_btn", timeout = 20)

    def click_shift_plus_pk_not_assigned_default_radio_btn(self):
        self.driver.click("shift_not_assigned_radio_btn", timeout = 20)

    def click_ctrl_plus_pk_automation_radio_btn(self):
        self.driver.click("ctl_automation_radio_btn", timeout = 20)

    def click_ctrl_plus_pk_key_sequence_radio_btn(self):
        self.driver.click("ctl_sequence_radio_btn", timeout = 20)

    def click_ctrl_plus_pk_text_input_radio_btn(self):
        self.driver.click("ctl_text_input_radio_btn", timeout = 20)

    def click_ctrl_plus_pk_not_assigned_default_radio_btn(self):
        self.driver.click("ctl_not_assigned_radio_btn", timeout = 20)

    def click_alt_plus_pk_automation_radio_btn(self):
        self.driver.click("alt_automation_radio_btn", timeout = 20)

    def click_alt_plus_pk_key_sequence_radio_btn(self):
        self.driver.click("alt_sequence_radio_btn", timeout = 20)

    def click_alt_plus_pk_text_input_radio_btn(self):
        self.driver.click("alt_text_input_radio_btn", timeout = 20)

    def click_alt_plus_pk_not_assigned_default_radio_btn(self):
        self.driver.click("alt_not_assigned_radio_btn", timeout = 20)

    def click_automation_dropbox_value_folder(self):
        self.driver.click("automation_dropbox_value_folder")  

    def click_automation_dropbox_value_file(self):
        self.driver.click("automation_dropbox_value_file")                    
    
    def click_folder_file_cancel_button(self):
        self.driver.click("select_windows_folder_file_cancel_button", timeout = 20)

    def select_website_for_programable_key(self, url):
        self.driver.click("automation_dropbox")
        self.driver.click("automation_dropbox_value_website")
        self.driver.click("website_text_field_box", timeout = 20)
        self.driver.send_keys("website_text_field_box", url)

    def click_add_application_continue_button(self):
        self.driver.click("prog_key_detail_app_continue_btn", timeout = 20)

    def click_add_website_continue_button(self):
        self.driver.click("website_continue_button", timeout = 20)

    def select_application_for_programable_key(self,app_name,locator):
        self.driver.click("automation_dropbox")
        self.driver.click("automation_dropbox_value_application")
        self.driver.click("search_application_box_to_add_application_list", timeout = 20)
        self.driver.send_keys("search_application_box_to_add_application_list",app_name)
        self.driver.click(locator, timeout = 10)

    def delete_application_list(self,locator):
        self.driver.click(locator, timeout = 10)

    def key_sequence_text_input(self,keys):
        self.driver.click("keysquence_text_field_box", timeout = 20)
        time.sleep(10)
        self.driver.send_keys("keysquence_text_field_box", keys)
        #need to ad 10 sec as it is very inconsistant to send keys
        time.sleep(10)
        self.driver.click("key_sequence_save_button", timeout = 20)
        #need to ad 10 sec as it is very inconsistant to save and delete keys
        time.sleep(10)
        self.delete_key_sequence()
    
    def clear_text_input(self,text_input):
        self.driver.clear_text(text_input)

    def verify_support_card_visible(self):
        return self.driver.wait_for_object("support_card", raise_e=False, timeout = 1015)
    
    def verify_key_sequence_text_field_show(self):
        return self.driver.wait_for_object("key_sequence_text_field", raise_e=False, timeout = 10)

    @screenshot_compare()
    def verify_color_filter(self):
        return self.driver.wait_for_object("programmable_key_header", raise_e=False, timeout=10)
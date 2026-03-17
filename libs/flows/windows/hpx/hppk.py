import re
from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.keys import Keys

class Hppk(HPXFlow):
    flow_name = "hppk"

    def verify_assign_description(self):
        return self.driver.wait_for_object("assign_description", raise_e=False, timeout=20)

    def verify_programmable_key_heading(self):
       return self.driver.get_attribute("programmable_key_heading","Name", timeout = 10)

    def verify_hppk_icon(self):
        return self.driver.wait_for_object("hppk_icon", raise_e=False, timeout=20)

    def verify_add_action(self):
        return self.driver.wait_for_object("add_action", raise_e=False, timeout=20)

    def verify_add_another(self):
        return self.driver.wait_for_object("add_another", raise_e=False, timeout=20)

    def verify_save(self):
        return self.driver.wait_for_object("save", raise_e=False, timeout=20)

    def verify_circular_1(self):
        return self.driver.wait_for_object("circularbutton1", raise_e=False, timeout=20)

    def verify_circular_2(self):
        return self.driver.wait_for_object("circularbutton2", raise_e=False, timeout=20)

    def verify_circular_3(self):
        return self.driver.wait_for_object("circularbutton3", raise_e=False, timeout=20)

    def verify_circular_4(self):
        return self.driver.wait_for_object("circularbutton4", raise_e=False, timeout=20)

    def verify_circular_5(self):
        return self.driver.wait_for_object("circularbutton5", raise_e=False, timeout=20)

    def verify_application(self):
        return self.driver.wait_for_object("application", raise_e=False, timeout=20)

    def verify_close_app_button(self):
        return self.driver.wait_for_object("close_app_button", raise_e=False, timeout=20)

    def verify_cancel_app_button(self):
        return self.driver.wait_for_object("cancel_app_button", raise_e=False, timeout=20)

    def verify_add_app_button(self):
        return self.driver.wait_for_object("add_app_button", raise_e=False, timeout=20)

    def verify_save_button(self):
        return self.driver.wait_for_object("save_button", raise_e=False, timeout=20)

    def verify_delete1(self):
        return self.driver.wait_for_object("delete1", raise_e=False, timeout=20)

    def verify_delete2(self):
        return self.driver.wait_for_object("delete2", raise_e=False, timeout=20)

    def verify_delete3(self):
        return self.driver.wait_for_object("delete3", raise_e=False, timeout=20)

    def verify_delete4(self):
        return self.driver.wait_for_object("delete4", raise_e=False, timeout=20)

    def verify_delete5(self):
        return self.driver.wait_for_object("delete5", raise_e=False, timeout=20)

    def verify_calculator(self):
        return self.driver.wait_for_object("calculator", raise_e=False, timeout=20)

    def verify_website(self):
        return self.driver.wait_for_object("website", raise_e=False, timeout=20)

    def verify_file(self):
        return self.driver.wait_for_object("file", raise_e=False, timeout=20)

    def verify_folder(self):
        return self.driver.wait_for_object("folder", raise_e=False, timeout=20)

    def verify_website_header(self):
        return self.driver.wait_for_object("website_header", raise_e=False, timeout=20)

    def verify_website_description(self):
        return self.driver.wait_for_object("website_description", raise_e=False, timeout=20)

    def verify_website_close(self):
        return self.driver.wait_for_object("website_close", raise_e=False, timeout=20)

    def verify_website_add(self):
        return self.driver.wait_for_object("website_add", raise_e=False, timeout=20)

    def verify_website_cancel(self):
        return self.driver.wait_for_object("website_cancel", raise_e=False, timeout=20)

    def verify_website_input(self):
        return self.driver.wait_for_object("website_input", raise_e=False, timeout=20)

    def verify_website_invalid_url_warning_text(self):
        return self.driver.wait_for_object("website_invalid_url_warning_text", raise_e=False, timeout=20)

    def click_add_action(self):
        self.driver.click("add_action" , timeout = 10)

    def verify_add_action_2(self):
        return self.driver.wait_for_object("add_action_2", raise_e=False, timeout=20)

    def verify_add_action_3(self):
        return self.driver.wait_for_object("add_action_3", raise_e=False, timeout=20)

    def verify_add_action_4(self):
        return self.driver.wait_for_object("add_action_4", raise_e=False, timeout=20)

    def verify_add_action_5(self):
        return self.driver.wait_for_object("add_action_5", raise_e=False, timeout=20)

    def verify_action_content_box(self):
        return self.driver.wait_for_object("action_content_box", raise_e=False, timeout=20)

    def click_applicationsearch(self):
        self.driver.click("applicationsearch", timeout = 20)

    def click_calculator(self):
        self.driver.click("calculator")

    def click_add_app_button(self):
        self.driver.click("add_app_button")

    def click_close_app_button(self):
        self.driver.click("close_app_button")

    def click_cancel_app_button(self):
        self.driver.click("cancel_app_button")

    def click_add_another(self):
        self.driver.click("add_another")

    def click_save_button(self):
        self.driver.click("save_button")

    def click_delete1(self):
        self.driver.click("delete1")

    def click_website(self):
        self.driver.click("website")

    def click_website_input(self):
        self.driver.click("website_input")

    def click_website_close(self):
        self.driver.click("website_close")

    def click_website_add(self):
        self.driver.click("website_add")

    def click_website_cancel(self):
        self.driver.click("website_cancel", timeout=10)

    def get_prog_key_nav_text(self):
        return self.driver.get_attribute("prog_key_nav_text","Name", timeout = 10)

    def get_assign_description(self):
        return self.driver.get_attribute("assign_description","Name")

    def get_personalized_text(self):
        return self.driver.get_attribute("personalized_text","Name")

    def get_add_action_text(self):
        return self.driver.get_attribute("add_action_text","Name")
    
    def get_application_text(self):
        return self.driver.get_attribute("application_text","Name", timeout = 10)
    
    def click_application(self):
        self.driver.click("application_text", timeout = 20)

    def get_app_text(self):
        return self.driver.get_attribute("app_title_text","Name")
    
    def get_search_text(self):
        return self.driver.get_attribute("applicationsearch","Name")
    
    def get_cancel_text(self):
        return self.driver.get_attribute("cancel_app_button","Name")
    
    def get_add_app_text(self):
        return self.driver.get_attribute("add_app_button","Name")

    def get_textbox_text(self):
        return self.driver.get_attribute("website_input","Name")

    def get_website_header(self):
        return self.driver.get_attribute("website_header","Name")
    
    def get_website_description_text(self):
        return self.driver.get_attribute("website_description","Name")

    def get_website_cancel_text(self):
        return self.driver.get_attribute("website_cancel","Name")

    def get_website_add_text(self):
        return self.driver.get_attribute("website_add","Name")
    
    def get_file_text(self):
        return self.driver.get_attribute("file","Name")
    
    def get_folder_text(self):
        return self.driver.get_attribute("folder","Name")

    def get_save_text(self):
        return self.driver.get_attribute("save_button","Name")

    def get_website_invalid_url_warning_text(self):
        return self.driver.get_attribute("website_invalid_url_warning_text","Name")
    
    def click_msaccess_app_applist(self):
        self.driver.click("msaccess_app_applist")
    
    def verify_default_support_page(self):
        return self.driver.wait_for_object("default_support_page", raise_e=False, timeout=20)
    
    def verify_supportkey_icon(self):
        return self.driver.wait_for_object("supportkey_icon", raise_e=False, timeout=20)
    
    def click_supportkey_icon(self):
        self.driver.click("supportkey_icon")
    
    def search_application(self,app_name):
        self.driver.send_keys("applicationsearch",app_name)
    
    def input_url(self,url):
        self.driver.send_keys("website_input",url)

    def mouse_hover_on_app(self):
        self.driver.click("assign_description")

    def click_delete_icon(self):
        self.driver.click("delete_icon", raise_e=False, timeout=10)

    def click_hppk_icon(self):
        self.driver.click("hppk_icon")

    def click_pcpkprogrammablekey_icon(self):
        self.driver.click("pcpkprogrammablekey")

    def click_automation_radio_button(self):
        self.driver.click("automation_radio_btn")

    def get_automation_text(self):
        return self.driver.get_attribute("automation_text","Name")
    
    def get_key_sequence_text(self):
        return self.driver.get_attribute("key_sequence_text","Name")
    
    def get_text_input_text(self):
        return self.driver.get_attribute("text_input_text","Name")
    
    def get_my_hp_pc_device_text(self):
        return self.driver.get_attribute("my_hp_pc_device_text","Name")
    
    def get_assign_text(self):
        return self.driver.get_attribute("assign_text","Name")
    
    def get_add_action_text_in_list(self):
        return self.driver.get_attribute("add_action_text_in_list","Name")
    
    def click_automation_radio_btn(self):
        self.driver.click("automation_radio_btn", timeout = 10)
    
    def click_key_sequence_radio_btn(self):
        self.driver.click("key_sequence_radio_btn", timeout = 10)
    
    def get_add_action_text_in_key_sequence(self):
        return self.driver.get_attribute("key_sequence_input_box","Name", timeout = 10)
    
    def enter_keys_in_key_sequence_textbox(self,keys):
        self.driver.click("key_sequence_input_box")
        self.driver.send_keys("key_sequence_input_box",keys)
    
    def get_save_text_key_sequence(self):#please do not change xpath of "key_sequence_save_button" coz it's break localization
        return self.driver.get_attribute("key_sequence_save_button","Name")
    
    def click_text_input_radio_btn(self):
        self.driver.click("text_input_radio_btn", timeout = 10)
    
    def get_add_text_in_text_input(self):
        return self.driver.get_attribute("text_input_text_box","Name")
    
    def get_char_left_text(self):
        return self.driver.get_attribute("char_left_text","Name")
    
    def enter_char_in_text_input(self,charac):
        self.driver.click("text_input_text_box")
        self.driver.send_keys("text_input_text_box",charac)
    
    def click_myhp_image(self):
        self.driver.click("hppk_icon")
    
    def get_my_programmable_key_text(self):
        return self.driver.get_attribute("my_programmable_key_text","Name")
    
    def get_my_support_key_text(self):
        return self.driver.get_attribute("my_support_key_text","Name")
    
    def click_pcpk_prog_key_image(self):
        self.driver.click("pcpkprogrammablekey")
    
    def get_save_in_text_input(self):#please do not change xpath of "text_input_save_button" coz it's break localization
        return self.driver.get_attribute("text_input_save_button","Name")

    def click_hppk_icon(self):
        self.driver.click("hppk_icon")

    def click_pcpkprogrammablekey_icon(self):
        self.driver.click("pcpkprogrammablekey")

    def click_automation_radio_button(self):
        self.driver.click("automation_radio_btn")

    def verify_automation_radio_btn(self):
       return self.driver.get_attribute("automation_radio_btn","Name")
    
    def verify_key_sequence_radio_btn(self):
       return self.driver.get_attribute("key_sequence_radio_btn","Name")
    
    def verify_text_input_radio_btn(self):
       return self.driver.get_attribute("text_input_radio_btn","Name")
    
    def verify_myhp_programmable_key_radio_btn(self):
       return self.driver.get_attribute("myHP_programmable_radio_btn","Name")
    
    def filter_char_left_text(self,char_left):
        ch=re.search("([^a-z\s]{1,})",char_left).group(1)
        ch1=char_left.replace(ch," ")
        ch2=ch1.strip()
        return ch2

    def click_key_sequence_input_box(self):
        self.driver.click("key_sequence_input_box", timeout = 10)

    def input_text_keysequence(self,text):
        self.driver.send_keys("key_sequence_input_box",text)

    def click_key_sequence_save_button(self):
        self.driver.click("key_sequence_save_button")

    def click_key_sequence_close_button(self):
        self.driver.click("key_sequence_close_button", timeout = 5)

    def click_text_input_text_box(self):
        self.driver.click("text_input_text_box")

    def input_text_text_input(self,text):
        self.driver.send_keys("text_input_text_box",text)

    def click_text_input_save_button(self):
        self.driver.click("text_input_save_button")

    def click_text_input_close_button(self):
        self.driver.click("text_input_close_button")

    def click_myhp_programmablekey_radio_btn(self):
        self.driver.click("myHP_programmable_radio_btn")

    def click_continue_button_on_change_shortcut_pop_up(self):
        self.driver.click("continue_button_on_change_shortcut_pop_up")

    def click_myhp_support_radio_btn(self):
        self.driver.click("myHP_hpsupport_radio_btn")

    def click_myHP_pcdevice_radio_btn(self):
        self.driver.click("myHP_pcdevice_radio_btn")
    
    def get_website_text(self):
        return self.driver.get_attribute("website","Name")

    def enter_char_in_key_sequence_textbox_save(self,charac):
        self.driver.click("key_sequence_input_box")
        self.driver.send_keys("key_sequence_input_box",charac)
        self.driver.click("key_sequence_save_button")

    def verify_pc_prog_key_icon(self):
        return self.driver.wait_for_object("pcpkprogrammablekey", raise_e=False, timeout=20)

    def verify_pcdevice_radio_button_is_selected(self):
        return self.driver.get_attribute("myHP_pcdevice_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_programmable_key_radio_button_is_selected(self):
        return self.driver.get_attribute("myHP_programmable_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_hpsupport_key_radio_button_is_selected(self):
        return self.driver.get_attribute("myHP_hpsupport_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_hp_support_key_radio_btn(self):
       return self.driver.get_attribute("myHP_hpsupport_radio_btn","Name", timeout = 10)

    def verify_pc_device_key_radio_btn(self):
       return self.driver.get_attribute("myHP_pcdevice_radio_btn","Name", timeout = 10)
    
    def get_saved_text_key_sequence(self):
        return self.driver.get_attribute("saved_text_key_sequence","Name", timeout = 10)
    
    def verify_change_shortcut_modal_title(self):
        return self.driver.wait_for_object("change_shortcut_modal_title", raise_e=False, timeout=10)
    
    def get_change_shortcut_modal_title(self):
        return self.driver.get_attribute("change_shortcut_modal_title","Name")
    
    def get_change_shortcut_modal_subtitle(self):
        return self.driver.get_attribute("change_shortcut_modal_subtitle","Name")
    
    def get_continue_btn_modal(self):
        return self.driver.get_attribute("continue_button_on_change_shortcut_pop_up","Name")
    
    def get_cancel_btn_modal(self):
        return self.driver.get_attribute("cancel_btn_modal","Name")
    
    def click_cancel_btn_modal(self):
        self.driver.click("cancel_btn_modal")
    
    def verify_key_sequence_close_button(self):
        return self.driver.wait_for_object("key_sequence_close_button", raise_e=False, timeout=10)
    
    def verify_saved_text_key_sequence(self):
        return self.driver.wait_for_object("saved_text_key_sequence", raise_e=False, timeout=10)

    def click_enter_key(self,element):
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.ENTER)

    def verify_delete_icon(self):
        return self.driver.wait_for_object("delete_icon", raise_e=False, timeout=10)

    def verify_action_content_box_value(self):
        return self.driver.get_attribute("action_content_box","Name", timeout = 10)

    def click_command_prompt_app(self):
        self.driver.click("command_prompt_app", timeout = 10)

    def click_esc_key(self,element):
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.ESCAPE)
    
    def verify_automation_radio_button_is_selected(self):
        return self.driver.get_attribute("automation_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def input_appname_appication_search(self,app_name):
        el = self.driver.wait_for_object("applicationsearch", raise_e=False, timeout=20)
        if el is not False:
            self.driver.send_keys("applicationsearch",app_name)

    def verify_applications_header_visible(self):
        return self.driver.wait_for_object("app_title_text", raise_e=False, timeout=10)

    def verify_website_header_visible(self):
        return self.driver.wait_for_object("website_header", raise_e=False, timeout=10)

    def verify_text_input_radio_button_is_selected(self):
        return self.driver.get_attribute("text_input_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_text_input_textbox_visible(self):
        return self.driver.wait_for_object("text_input_text_box", raise_e=False, timeout=20)

    def verify_input_text_save_button_visible(self):
        return self.driver.wait_for_object("text_input_save_button", raise_e=False, timeout=20)

    def verify_input_text_close_button_visible(self):
        return self.driver.wait_for_object("text_input_close_button", raise_e=False, timeout=20)

    def verify_text_input_radio_button_is_selected(self):
        return self.driver.get_attribute("text_input_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_key_sequence_radio_button_is_selected(self):
        return self.driver.get_attribute("key_sequence_radio_btn", "SelectionItem.IsSelected", timeout = 10)

    def verify_sequence_text_box_visible(self):
        return self.driver.wait_for_object("key_sequence_input_box", raise_e=False, timeout=20)

    def click_back_arrow(self):
        self.driver.click("back_arrow")

    def verify_key_sequence_textbox_text_value(self):
        return self.driver.get_attribute("key_sequence_input_box", "Value.Value", timeout = 10)

    def verify_text_input_textbox_text_value(self):
        return self.driver.get_attribute("text_input_text_box", "Value.Value", timeout = 10)

    def verify_continue_btn_modal_visible(self):
        return self.driver.wait_for_object("continue_button_on_change_shortcut_pop_up", raise_e=False, timeout=10)

    def verify_cancel_btn_modal_visible(self):
        return self.driver.wait_for_object("cancel_btn_modal", raise_e=False, timeout=10)

    def verify_shift_hppk_icon(self):
        return self.driver.wait_for_object("shift_hppk_icon", raise_e=False, timeout=20)

    def verify_ctrl_hppk_icon(self):
        return self.driver.wait_for_object("ctrl_hppk_icon", raise_e=False, timeout=20)

    def verify_alt_hppk_icon(self):
        return self.driver.wait_for_object("alt_hppk_icon", raise_e=False, timeout=20)

    def click_alt_hppk_btn(self):
        self.driver.click("alt_hppk_icon", timeout = 10)

    def click_ctrl_hppk_btn(self):
        self.driver.click("ctrl_hppk_icon", timeout = 10)

    def click_shift_hppk_btn(self):
        self.driver.click("shift_hppk_icon", timeout = 10)

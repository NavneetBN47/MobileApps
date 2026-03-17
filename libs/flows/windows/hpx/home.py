from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class Home(HPXFlow):
    flow_name = "home"

    def verify_welcome_message_on_homepage(self):
        return self.driver.wait_for_object("Welcome_to_hp_text").get_attribute("Name")

    def verify_audio_control(self):
        return self.driver.wait_for_object("Audio_Control_Display").get_attribute("Name")   

    def verify_video_control(self):
        return self.driver.wait_for_object("Video_Control_Display").get_attribute("Name")

    def click_view_all_controls(self):
        self.driver.click("View_All_Controls_Link")
            
    def verify_view_all_controls(self):
        return self.driver.wait_for_object("View_All_Controls_Link").get_attribute("Name")
    
    def verify_support_icon(self):
        return self.driver.wait_for_object("Support_Icon").get_attribute("Name")

    def verify_network_booster_item(self):
        return self.driver.wait_for_object("Network_Booster_Item").get_attribute("Name")

    def verify_programmable_key(self):
        return self.driver.wait_for_object("Programmable_Key").get_attribute("Name")

    def verify_take_action(self):
        return self.driver.wait_for_object("Take_Action").get_attribute("Name")

    def verify_minimize_button_visible(self):
        return self.driver.wait_for_object("Minimize_Button", raise_e=False, timeout=10) is not False

    def verify_maximize_button_visible(self):
        return self.driver.wait_for_object("Maximize_Button", raise_e=False, timeout=10) is not False

    def verify_close_button_visible(self):
        return self.driver.wait_for_object("Close_Button", raise_e=False, timeout=10) is not False
    
    def click_audio_control_card(self):
        return self.driver.click("AudioControl_card")
    
    def click_programmable_key_card(self):
        return self.driver.click("Programmable_Key_card")

    def click_support_control_card(self):
        self.driver.click("support_control_card", timeout=20)
    
    def get_view_all_controls_text(self):
        return self.driver.wait_for_object("view_all_controls_text").get_attribute("Name")
    
    def get_audio_control_text(self):
        return self.driver.wait_for_object("audio_control_text").get_attribute("Name")
    
    def get_configure_to_optimize_audio_text(self):
        return self.driver.wait_for_object("Configure_to_optimize_audio_text").get_attribute("Name")  
    
    def get_video_control_text(self):
        return self.driver.wait_for_object("video_control_text").get_attribute("Name")
    
    def get_optimize_conference_streaming_text(self):
        return self.driver.wait_for_object("optimize_conference_streaming_text").get_attribute("Name")
    
    def get_prog_key_text(self):
        return self.driver.wait_for_object("prog_key_text").get_attribute("Name")
    
    def get_create_short_cut_text(self):
        return self.driver.wait_for_object("create_short_cut_text").get_attribute("Name")
    
    def get_display_control_title_text(self):
        return self.driver.wait_for_object("display_control_title").get_attribute("Name")
    
    def get_manage_display_setting_text(self):
        return self.driver.wait_for_object("manage_display_setting_text").get_attribute("Name")
    
    def verify_get_most_put_of_hp(self):
        return self.driver.get_attribute("get_most_put_of_hp","Name", raise_e=False, timeout=20)

    def verify_programmable_keyNavTitle(self):
        return self.driver.wait_for_object("Program_Key_Nav").get_attribute("Name")

    def verify_support_card_title(self):
        return self.driver.wait_for_object("support_card_title").get_attribute("Name")
        
    def verify_display_control_card_visible(self):
        return self.driver.wait_for_object("display_control_card", raise_e=False, timeout=2)
   
    def verify_video_control_card_visible(self):
        return self.driver.wait_for_object("video_control_card",raise_e=False, timeout=5)
    
    def verify_AudioControl_card_visible(self):
        return self.driver.wait_for_object("AudioControl_card", raise_e=False, timeout=2) 
    
    def verify_Programmable_Key_card_visible(self):
        return self.driver.wait_for_object("Programmable_Key_card", raise_e=False, timeout=2)

    def verify_support_detail_page_title(self):
        return self.driver.wait_for_object("support_screen_detail_page_title").get_attribute("Name")
    
    def verify_support_card_visible(self):
        return self.driver.wait_for_object("support_control_card", raise_e=False, timeout=2)

    def click_content_card(self):
        self.driver.click("home_content_card")

    def verify_maybe_later_btn_show(self):
        return self.driver.wait_for_object("maybe_later_btn", raise_e=False, timeout=10)

    def click_back_arrow(self):
        self.driver.click("back_arrow")

    def verify_home_title_show(self):
        return self.driver.wait_for_object("home_title", raise_e=False, timeout=10)

    def verify_home_audio_title_show(self):
        return self.driver.wait_for_object("home_audio_title", raise_e=False, timeout=10)
    
    def verify_pc_diagtools_card_show(self):
        return self.driver.wait_for_object("pc_diagtools_card", raise_e=False, timeout=10) is not False
    
    def click_pc_diagtools_card(self):
        self.driver.click("pc_diagtools_card")

    def click_pc_visit_support_btn(self):
        self.driver.click("visit_support_btn")
    
    def verify_take_action_btn_show(self):
        return self.driver.wait_for_object("Take_Action", raise_e=False, timeout=10)
    
    def verify_prog_key_card(self):
        return self.driver.wait_for_object("prog_key_card", raise_e=False, timeout=10)
    
    def click_display_control_card(self):
        self.driver.click("display_control_card")
        
    def verify_home_module_show_on_global_navigation_panel(self):
        return self.driver.wait_for_object("home_module", raise_e=False, timeout = 20)
    
    def click_system_control_card(self):
        self.driver.click("system_control_card")

    def verify_get_help_anytime_card_show(self):
        return self.driver.wait_for_object("get_help_anytime_card", raise_e=False, timeout=10) is not False

    def click_get_help_anytime_card(self):
        self.driver.click("get_help_anytime_card")

    def verify_gesture_card_show_on_home_page(self):
        return self.driver.wait_for_object("gesture_card", raise_e=False, timeout=10) is not False

    def verify_wifi_card_show_on_home_page(self):
        return self.driver.wait_for_object("wifi_sharing_card", raise_e=False, timeout=10) is not False
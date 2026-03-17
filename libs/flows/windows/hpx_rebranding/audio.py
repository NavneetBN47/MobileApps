import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from selenium.webdriver.common.keys import Keys
from SAF.misc.ssh_utils import SSH
from SAF.misc import windows_utils
from SAF.decorator.saf_decorator import screenshot_compare

class Audio(HPXRebrandingFlow):
    flow_name = "audio"

    def verify_audio_control_card_show_up(self):
        return self.driver.wait_for_object("audio_card_on_home_page", raise_e=False, timeout=10) is not False

    def click_audio_control_card(self):
        self.driver.click("audio_card_on_home_page")
    
    def verify_audio_presets_title_show_up(self):
        if self.driver.wait_for_object("eq_title", raise_e=False, timeout=20) is False:
            try:
                self.driver.scroll_element(direction="down", distance=10, time_out=20)
            except Exception:
                pass  
        return self.driver.wait_for_object("audio_presets_title", raise_e=False, timeout=20) is not False

    def verify_audio_presets_music_txt_show_up(self):
        return self.driver.wait_for_object("audio_presets_music_txt", raise_e=False, timeout=10) is not False

    def verify_audio_presets_movie_txt_show_up(self):
        return self.driver.wait_for_object("audio_presets_movie_txt", raise_e=False, timeout=10) is not False

    def verify_audio_presets_voice_txt_show_up(self):
        return self.driver.wait_for_object("audio_presets_voice_txt", raise_e=False, timeout=10) is not False

    def verify_audio_presets_music_button_show_up(self):
        return self.driver.wait_for_object("audio_presets_music_button", raise_e=False, timeout=10) is not False

    def verify_audio_presets_movie_button_show_up(self):
        return self.driver.wait_for_object("audio_presets_movie_button", raise_e=False, timeout=10) is not False

    def verify_audio_presets_voice_button_show_up(self):
        if self.driver.wait_for_object("audio_presets_voice_button", raise_e=False, timeout=10) is False:
            try:
                self.driver.scroll_element("audio_presets_voice_button", direction="up", distance=20, time_out=20)
                self.driver.scroll_element("audio_presets_voice_button", direction="down", distance=10, time_out=20)
            except Exception:
                pass  
        return self.driver.wait_for_object("audio_presets_voice_button", raise_e=False, timeout=10) is not False

    def verify_ai_noise_removal_title_show_up(self):
        return self.driver.wait_for_object("ai_noise_removal_title", raise_e=False, timeout=10) is not False

    def verify_ai_noise_removal_tooltip_show_up(self):
        return self.driver.wait_for_object("ai_noise_removal_tooltip", raise_e=False, timeout=10) is not False

    def verify_ai_noise_removal_toggle_show_up(self):
        return self.driver.wait_for_object("ai_noise_removal_toggle_off", raise_e=False, timeout=10) is not False

    def verify_ai_noise_reduction_title_show_up(self):
        if self.driver.wait_for_object("ai_noise_reduction_title", raise_e=False, timeout=20) is False:
            try:
                self.driver.scroll_element("ai_noise_reduction_title", direction="up", distance=18, time_out=20)
                self.driver.scroll_element("ai_noise_reduction_title", direction="down", distance=6, time_out=20)
            except Exception:
                pass
        return self.driver.wait_for_object("ai_noise_reduction_title", raise_e=False, timeout=10) is not False

    def verify_ai_noise_reduction_tooltip_show_up(self):
        return self.driver.wait_for_object("noise_reduction_tooltip", raise_e=False, timeout=10) is not False

    def verify_ai_noise_reduction_toggle_show_up(self):
        return self.driver.wait_for_object("ai_noise_reduction_toggle_on", raise_e=False, timeout=10) is not False
    
    def verify_output_title_show_up(self):
        return self.driver.wait_for_object("output_title", raise_e=False, timeout=10) is not False
    
    def verify_output_source_title_show_up(self):
        return self.driver.wait_for_object("output_source_title", raise_e=False, timeout=10) is not False
    
    def verify_output_combobox_show_up(self):
        return self.driver.wait_for_object("output_combobox", raise_e=False, timeout=20) is not False
    
    def verify_output_combobox_open_button_show_up(self):
        return self.driver.wait_for_object("output_combobox_open_button", raise_e=False, timeout=10) is not False

    def verify_output_volume_title_show_up(self):
        return self.driver.wait_for_object("output_volume_title", raise_e=False, timeout=10) is not False

    def verify_output_volume_0_show_up(self):
        return self.driver.wait_for_object("output_volume_0", raise_e=False, timeout=10) is not False

    def verify_output_volume_slider_show_up(self):
        return self.driver.wait_for_object("output_volume_slider", raise_e=False, timeout=10) is not False

    def verify_output_volume_100_show_up(self):
        return self.driver.wait_for_object("output_volume_100", raise_e=False, timeout=10) is not False

    def verify_input_title_show_up(self):
        return self.driver.wait_for_object("input_title", raise_e=False, timeout=10) is not False

    def verify_input_source_title_show_up(self):
        return self.driver.wait_for_object("input_source_title", raise_e=False, timeout=10) is not False

    def verify_input_combobox_show_up(self):
        return self.driver.wait_for_object("input_combobox", raise_e=False, timeout=10) is not False
    
    def verify_input_combobox_open_button_show_up(self):
        return self.driver.wait_for_object("input_combobox_open_button", raise_e=False, timeout=10) is not False

    def verify_input_volume_title_show_up(self):
        return self.driver.wait_for_object("input_volume_title", raise_e=False, timeout=10) is not False

    def verify_input_volume_0_show_up(self):
        return self.driver.wait_for_object("input_volume_0", raise_e=False, timeout=10) is not False

    def verify_input_volume_slider_show_up(self):
        return self.driver.wait_for_object("input_volume_slider", raise_e=False, timeout=10) is not False

    def verify_input_volume_100_show_up(self):
        return self.driver.wait_for_object("input_volume_100", raise_e=False, timeout=10) is not False
    
    def get_restore_default_button_text(self):
        return self.driver.get_attribute("restore_defaults_button", "Name")

    def verify_audio_presets_RPG_txt_show_up(self):
        return self.driver.wait_for_object("audio_presets_RPG_txt", raise_e=False, timeout=10) is not False
 
    def verify_audio_presets_shooter_txt_show_up(self):
        return self.driver.wait_for_object("audio_presets_shooter_txt", raise_e=False, timeout=10) is not False
 
    def verify_audio_presets_strategy_txt_show_up(self):
        return self.driver.wait_for_object("audio_presets_strategy_txt", raise_e=False, timeout=10) is not False
 
    def verify_audio_presets_RPG_button_show_up(self):
        return self.driver.wait_for_object("audio_presets_RPG_button", raise_e=False, timeout=10) is not False
 
    def verify_audio_presets_shooter_button_show_up(self):
        return self.driver.wait_for_object("audio_presets_shooter_button", raise_e=False, timeout=10) is not False
 
    def verify_audio_presets_strategy_button_show_up(self):
        return self.driver.wait_for_object("audio_presets_strategy_button", raise_e=False, timeout=10) is not False
 
    def verify_mic_mode_title_show_up(self):
        return self.driver.wait_for_object("mic_mode_title", raise_e=False, timeout=10) is not False
 
    def verify_mic_mode_tooltip_show_up(self):
        return self.driver.wait_for_object("mic_mode_tooltip", raise_e=False, timeout=10) is not False
 
    def verify_mic_mode_combobox_show_up(self):
        return self.driver.wait_for_object("mic_mode_combobox", raise_e=False, timeout=10) is not False
 
    def verify_mic_mode_combobox_open_button_show_up(self):
        return self.driver.wait_for_object("mic_mode_combobox_open_button", raise_e=False, timeout=10) is not False
 
    def verify_conference_show_up(self):
        return self.driver.wait_for_object("conference", raise_e=False, timeout=10) is not False
 
    def verify_personal_show_up(self):
        return self.driver.wait_for_object("personal", raise_e=False, timeout=10) is not False
   
    def verify_studio_recording_mode_show_up(self):
        return self.driver.wait_for_object("studio_recording_mode", raise_e=False, timeout=10) is not False
 
    def verify_output_device_headphone_show_up(self):
        return self.driver.wait_for_object("output_device_3.5mm_headphone", raise_e=False, timeout=10) is not False
 
    def verify_output_device_internal_speaker_dropbox_show_up_willie_robotics(self):
        return self.driver.wait_for_object("output_device_internal_speaker_willie_robotics", raise_e=False, timeout=10) is not False
 
    def click_output_combobox_open_button(self):
        self.driver.click("output_combobox_open_button")
 
    def click_output_device_headphone(self):
        self.driver.click("output_device_3.5mm_headphone")
 
    def click_output_device_internal_speaker_on_arti(self):
        self.driver.click("output_device_internal_speaker")

    def verify_eq_title_show_up(self):
        if self.driver.wait_for_object("run_audio_check_button", raise_e=False, timeout=20) is False:
            try:
                self.driver.scroll_element(direction="up", distance=20, time_out=20)
                self.driver.scroll_element(direction="down", distance=15, time_out=20)
            except Exception:
                pass  
        return self.driver.wait_for_object("eq_title", raise_e=False, timeout=20) is not False

    def verify_eq_slider_show_up(self):
        return self.driver.wait_for_object("eq_slider", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_32_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_32", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_64_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_64", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_125_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_125", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_250_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_250", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_500_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_500", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_1k_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_1k", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_2k_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_2k", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_4k_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_4k", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_8k_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_8k", raise_e=False, timeout=10) is not False

    def verify_horizontal_axis_16k_show_up(self):
        return self.driver.wait_for_object("horizontal_axis_16k", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_6_show_up(self):
        return self.driver.wait_for_object("vertical_axis_6", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_3_show_up(self):
        return self.driver.wait_for_object("vertical_axis_3", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_0_show_up(self):
        return self.driver.wait_for_object("vertical_axis_0", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_minus_3_show_up(self):
        return self.driver.wait_for_object("vertical_axis_minus_3", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_minus_6_show_up(self):
        return self.driver.wait_for_object("vertical_axis_minus_6", raise_e=False, timeout=10) is not False
    
    def verify_global_icon_show_up(self):
        return self.driver.wait_for_object("global_icon", raise_e=False, timeout=10) is not False
    
    def verify_add_application_button_show_up(self):
        return self.driver.wait_for_object("add_application_button", raise_e=False, timeout=10) is not False

    def verify_add_application_button_text_show_up(self):
        return self.driver.wait_for_object("add_application_button_text", raise_e=False, timeout=10) is not False
    
    def verify_for_all_applications_text_show_up(self):
        return self.driver.wait_for_object("for_all_applications_text", raise_e=False, timeout=10) is not False

    def verify_advanced_audio_settings_title_show_up(self):
        if self.driver.wait_for_object("advanced_audio_settings_title", raise_e=False, timeout=10) is False:
            try:
                self.driver.scroll_element("advanced_audio_settings_title", direction="down", distance=6, time_out=50)
            except Exception:
                pass  
        return self.driver.wait_for_object("advanced_audio_settings_title", raise_e=False, timeout=10) is not False
            
    def verify_advanced_audio_settings_arrow_show_up(self):
        return self.driver.wait_for_object("advanced_audio_settings_arrow", raise_e=False, timeout=10) is not False

    def click_advanced_audio_settings_arrow(self):
        self.driver.click("advanced_audio_settings_arrow")

    def verify_audio_title_show_on_advanced_audio_setting_page(self):
        return self.driver.wait_for_object("audio_title_on_advanced_audio_settings_page", raise_e=False, timeout=10) is not False

    def verify_speaker_swap_title_show_up(self):
        return self.driver.wait_for_object("speaker_swap_title", raise_e=False, timeout=10) is not False

    def verify_speaker_swap_toggle_show_up(self):
        if self.driver.wait_for_object("speaker_swap_toggle", raise_e=False, timeout=10) is not False:
            return True
        elif self.driver.wait_for_object("speaker_swap_toggle_on", raise_e=False, timeout=10) is not False:
            return True 
        else:
            return False

    def get_speaker_swap_toggle_status(self):
        if self.driver.wait_for_object("speaker_swap_toggle", raise_e=False, timeout=5) is not False:
            return self.driver.get_attribute("speaker_swap_toggle", "Toggle.ToggleState")
        else:
            return self.driver.get_attribute("speaker_swap_toggle_on", "Toggle.ToggleState")
    
    def click_speaker_swap_toggle(self):
        if self.driver.wait_for_object("speaker_swap_toggle", raise_e=False, timeout=5) is not False:
            self.driver.click("speaker_swap_toggle")
        else:
            self.driver.click("speaker_swap_toggle_on")

    def scroll_window_locator(self):
        return self.driver.wait_for_object("scroll_window", timeout=10)

    def get_presets_music_button_status(self):
        return self.driver.get_attribute("audio_presets_music_button", "SelectionItem.IsSelected", raise_e=False, timeout=10)
   
    def click_audio_presets_music_button(self):
        self.driver.click("audio_presets_music_button")
 
    def get_presets_movie_button_status(self):
        return self.driver.get_attribute("audio_presets_movie_button", "SelectionItem.IsSelected", raise_e=False, timeout=10)
   
    def click_audio_presets_movie_button(self):
        self.driver.click("audio_presets_movie_button")
 
    def get_presets_voice_button_status(self):
        return self.driver.get_attribute("audio_presets_voice_button", "SelectionItem.IsSelected", raise_e=False, timeout=10)
   
    def click_audio_presets_voice_button(self):
        self.driver.click("audio_presets_voice_button")
 
    def click_back_button_on_audio_page(self):
        self.driver.click("back_button_on_audio_page")

    def verify_mute_txt_for_output_show_up(self):
        return self.driver.wait_for_object("mute_txt_for_output", raise_e=False, timeout=10) is not False
    
    def verify_mute_toggle_for_output_show_up(self):
        return self.driver.wait_for_object("mute_toggle_for_output", raise_e=False, timeout=10) is not False
    
    def get_mute_toggle_for_output_status(self):
        return self.driver.get_attribute("mute_toggle_for_output", "Toggle.ToggleState", raise_e=False, timeout=10)

    def click_mute_toggle_for_output(self):
        return self.driver.click("mute_toggle_for_output")

    def verify_mute_txt_for_input_show_up(self):
        return self.driver.wait_for_object("mute_txt_for_input", raise_e=False, timeout=10) is not False
    
    def verify_mute_toggle_for_input_show_up(self):
        return self.driver.wait_for_object("mute_toggle_for_input", raise_e=False, timeout=10) is not False
    
    def get_mute_toggle_for_input_status(self):
        return self.driver.get_attribute("mute_toggle_for_input", "Toggle.ToggleState", timeout = 10)

    def click_mute_toggle_for_input(self):
        self.driver.click("mute_toggle_for_input")

    def get_input_slider_value(self):
        time.sleep(5)
        return self.driver.get_attribute("input_volume_slider", "Value.Value",  timeout = 20)
    
    def get_output_slider_value(self):
        time.sleep(5)
        return self.driver.get_attribute("output_volume_slider", "Value.Value",  timeout = 20)
    
    def set_audio_output_slider_value_decrease(self, value):
        slider = self.driver.wait_for_object("output_volume_slider", timeout = 10)
        self.driver.click("output_volume_slider", timeout = 10)
        output_value = int(float(self.get_output_slider_value()))
        for _ in range(output_value - value):
            time.sleep(2)  
            slider.send_keys(Keys.LEFT)
        
    def set_audio_output_slider_value_increase(self, value):
        slider = self.driver.wait_for_object("output_volume_slider", timeout = 10)
        self.driver.click("output_volume_slider", timeout = 10)
        output_value = int(float(self.get_output_slider_value()))
        for _ in range(value - output_value):
            time.sleep(2)
            slider.send_keys(Keys.RIGHT)
    
    def set_audio_input_slider_value_decrease(self, value):
        slider = self.driver.wait_for_object("input_volume_slider", timeout = 10)
        self.driver.click("input_volume_slider", timeout = 10)
        input_value = int(float(self.get_input_slider_value()))
        for _ in range(input_value - value):
            time.sleep(2)
            slider.send_keys(Keys.LEFT)
        
    def set_audio_input_slider_value_increase(self, value):
        slider = self.driver.wait_for_object("input_volume_slider", timeout = 10)
        self.driver.click("input_volume_slider", timeout = 10)
        input_value = int(float(self.get_input_slider_value()))
        for _ in range(value - input_value):
            time.sleep(2)
            slider.send_keys(Keys.RIGHT)
    
    def click_on_system_settings_maximize_button(self):
        self.driver.click("maximize_system_settings")
    
    def verify_system_settings_window_maximize(self):
        return self.driver.get_attribute("maximize_system_settings","Name")
    
    def get_windows_system_sound_output_volume_tab(self):
        return self.driver.get_attribute("windows_system_sound_output_volume_tab","RangeValue.Value")
    
    def verify_restore_defaults_button_show_up(self):
        try:
            self.driver.scroll_element("restore_defaults_button", direction="down", distance=18, time_out=30)
        except Exception:
            pass  
        return self.driver.wait_for_object("restore_defaults_button", raise_e=False, timeout=10) is not False

    def click_restore_defaults_button(self):
        self.driver.click("restore_defaults_button")
        time.sleep(5)
        
    def click_advanced_settings_restore_defaults_button(self):
        self.driver.click("advanced_settings_restore_defaults_button")
    
    def get_windows_system_sound_input_volume_tab(self):
        return self.driver.get_attribute("windows_system_sound_input_volume_tab","RangeValue.Value")

    def verify_aiqiyi_app_show_on_application_list(self):
        return self.driver.wait_for_object("aiqiyi_on_application_list", raise_e=False, timeout=10)
    
    def verify_tencent_app_show_on_application_list(self):
        return self.driver.wait_for_object("tencent_on_application_list", raise_e=False, timeout=10)

    def verify_disney_app_show_on_application_list(self):
        return self.driver.wait_for_object("disney+_on_application_list", raise_e=False, timeout=10)
    
    def verify_access_app_show_on_application_list(self):
        return self.driver.wait_for_object("access_on_application_list", raise_e=False, timeout=10)

    def click_access_app_on_application_list(self):
        self.driver.click("access_on_application_list")
   
    def click_add_application_button(self):
        self.driver.click("add_application_button")

    def verify_add_application_txt_on_dialog_show_up(self):
        return self.driver.wait_for_object("add_application_txt_on_dialog", raise_e=False, timeout=10)
    
    def verify_search_application_txt_on_search_frame_show_up(self):
        return self.driver.wait_for_object("search_application_txt_on_search_frame", raise_e=False, timeout=10)
    
    def verify_search_application_frame_show_up(self):
        return self.driver.wait_for_object("search_application_frame", raise_e=False, timeout=10)
    
    def click_search_application_frame(self):
        self.driver.click("search_application_frame")

    def verify_search_application_frame_show_up(self):
        return self.driver.wait_for_object("search_application_frame")
    
    def verify_application_list_on_dialog_show_up(self):
        return self.driver.wait_for_object("application_list_on_dialog", raise_e=False, timeout=10)

    def verify_cancel_button_on_dialog_show_up(self):
        return self.driver.wait_for_object("cancel_button_on_dialog", raise_e=False, timeout=10)
    
    def click_cancel_button_on_dialog(self):
        self.driver.click("cancel_button_on_dialog")

    def verify_continue_button_on_dialog_show_up(self):
        return self.driver.wait_for_object("continue_button_on_dialog", raise_e=False, timeout=10)

    def click_continue_button_on_dialog(self):
        self.driver.click("continue_button_on_dialog")

    def search_apps_on_search_frame(self, app_name):
        self.driver.click("search_application_frame")
        self.driver.send_keys("search_application_frame", app_name)
        
    def click_access_on_application_list_dialog(self):
        self.driver.click("search_access_on_application_list")

    def verify_serached_app_is_be_selected(self):
        return self.driver.wait_for_object("searched_app", raise_e=False, timeout=10)

    def verify_delete_button_show_up(self):
        return self.driver.wait_for_object("delete_button", raise_e=False, timeout=10)

    def click_delete_button(self):
        self.driver.click("delete_button")
    
    def verify_delete_profile_txt_on_dialog_show_up(self):
        return self.driver.wait_for_object("delete_profile_txt_on_dialog", raise_e=False, timeout=10)
    
    def verify_continue_button_on_delete_app_dialog_show_up(self):
        return self.driver.wait_for_object("continue_button_on_delete_app_dialog", raise_e=False, timeout=10)

    def click_continue_button_on_delete_app_dialog(self):
        self.driver.click("continue_button_on_delete_app_dialog")

    def verify_audio_title_on_header_show_up(self):
        return self.driver.wait_for_object("audio_title_on_header", raise_e=False, timeout=10)
    
    def select_output_usb_external_device(self):
        self.driver.click("output_device_usb_headphone_gidget")
    
    def select_output_35mm_external_device(self):
        self.driver.click("output_device_3.5mm_headphone_gidget")
    
    def select_output_internal_device(self):
        self.driver.click("output_device_internal_speaker_gidget")
    
    def select_input_usb_external_device(self):
        self.driver.click("input_usb_external_headphone_gidget")
    
    def select_input_35mm_external_device(self):
        self.driver.click("input_35mm_external_headphone_gidget")
    
    def select_input_internal_device(self):
        self.driver.click("input_internal_headphone_gidget")
    
    def click_input_combobox_open_button(self):
        self.driver.click("input_combobox_open_button")
    
    def verify_input_internal_device_show(self):
        return self.driver.wait_for_object("input_internal_headphone_gidget", raise_e=False, timeout=10)
    
    def verify_input_35mm_external_device_show(self):
        return self.driver.wait_for_object("input_35mm_external_headphone_gidget", raise_e=False, timeout=10)
    
    def verify_output_internal_device_show(self):
        return self.driver.wait_for_object("output_device_internal_speaker_gidget", raise_e=False, timeout=10)
    
    def verify_output_35mm_external_device_show(self):
        return self.driver.wait_for_object("output_device_3.5mm_headphone_gidget", raise_e=False, timeout=10)
    
    def verify_noise_removal_toggle_on_state(self):
        return self.driver.get_attribute("ai_noise_removal_toggle_on", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def verify_noise_removal_toggle_off_state(self):
        return self.driver.get_attribute("ai_noise_removal_toggle_off", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def verify_noise_reduction_toggle_on_state(self):
        if self.driver.wait_for_object("ai_noise_reduction_toggle_on", raise_e=False, timeout=10) is False:
            try:
                self.driver.scroll_element("ai_noise_reduction_toggle_on", direction="up", distance=18, time_out=50)
                self.driver.scroll_element("ai_noise_reduction_toggle_on", direction="down", distance=4, time_out=50)
            except Exception:
                pass  
        return self.driver.get_attribute("ai_noise_reduction_toggle_on", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def verify_noise_reduction_toggle_off_state(self):
        return self.driver.get_attribute("ai_noise_reduction_toggle_off", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def turn_on_noise_removal(self):
        self.driver.click("ai_noise_removal_toggle_off")
    
    def turn_off_noise_removal(self):
        self.driver.click("ai_noise_removal_toggle_on")
    
    def turn_on_noise_reduction(self):
        self.driver.click("ai_noise_reduction_toggle_off")
    
    def turn_off_noise_reduction(self):
        self.driver.click("ai_noise_reduction_toggle_on", timeout = 15)
    
    def click_mic_mode_combobox_open_button(self):
        self.driver.click("mic_mode_combobox_open_button")
    
    def selected_conferenece_mode(self):
        self.driver.click("conference")
    
    def selected_personal_mode(self):
        self.driver.click("personal")
    
    def selected_studio_recording_mode(self):
        self.driver.click("studio_recording_mode")
    
    def click_conference_items(self):
        self.driver.click("conference_selected")
 
    def click_personal_items(self):
        self.driver.click("personal_selected")
   
    def click_studio_recording_items(self):
        self.driver.click("studio_recording_mode")
    
    def set_eq_slider_value_decrease(self, element, value):
        slider = self.driver.wait_for_object(element, timeout = 10)
        self.driver.click(element, timeout = 10)
        eq_value = int(float(self.get_output_slider_value()))
        for _ in range(eq_value - value):
            time.sleep(2)  
            slider.send_keys(Keys.DOWN)
        
    def set_eq_slider_value_increase(self, element, value):
        slider = self.driver.wait_for_object(element, timeout = 10)
        self.driver.click(element, timeout = 10)
        eq_value = int(float(self.get_eq_slider_value(element)))
        for _ in range(value - eq_value):
            time.sleep(2)
            slider.send_keys(Keys.UP)
    
    def get_eq_slider_value(self, element):
        time.sleep(5)
        return self.driver.get_attribute(element, "Value.Value",  timeout = 20)
    
    def verify_arrow_next_on_application_list(self):
        return self.driver.wait_for_object("arrow_next_on_application_list", raise_e=False, timeout = 40) is not False

    def click_arrow_next_on_application_list(self):
        self.driver.click("arrow_next_on_application_list")

    def click_searched_app_on_search_frame(self):
        self.driver.click("searched_app")

    def verify_searched_app_is_be_selected(self):
        return self.driver.get_attribute("searched_app", "name")

    def click_global_icon(self):
        self.driver.click("global_icon")

    def click_tencent_app_on_application_list(self):
        self.driver.click("tencent_on_application_list")

    def click_aiqiyi_app_on_application_list(self):
        self.driver.click("aiqiyi_on_application_list")

    def click_disney_app_on_application_list(self):
        self.driver.click("disney+_on_application_list")
    
    def verify_immersive_title_show_up(self):
        return self.driver.wait_for_object("immersive_title", raise_e=False, timeout=10) is not False
    
    def turn_on_immersive_button(self):
        self.driver.click("immersive_toggle_off")
    
    def turn_off_immersive_button(self):
        self.driver.click("immersive_toggle_on")
    
    def verify_immersive_toggle_on_state(self):
        return self.driver.get_attribute("immersive_toggle_on", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def verify_immersive_toggle_off_state(self):
        return self.driver.get_attribute("immersive_toggle_off", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def verify_usb_headphone_input_selected_willie_robotics(self):
        return self.driver.wait_for_object("usb_headphone_input_selected_willie_robotics", raise_e=False, timeout=10)
    
    def verify_output_usb_headphone_show(self):
        return self.driver.wait_for_object("output_device_usb_headphone_gidget", raise_e=False, timeout=10) is not False
    
    def verify_speaker_selected_willie_robotics(self):
        return self.driver.wait_for_object("speaker_selected_willie_robotics", raise_e=False, timeout=10) is not False
    
    def verify_microphone_array_selected_willie_robotics(self):
        return self.driver.wait_for_object("microphone_array_selected_willie_robotics", raise_e=False, timeout=10) is not False
    
    def verify_3_5_headphone_input_selected_willie_robotics(self):
        return self.driver.wait_for_object("3_5_headphone_input_selected_willie_robotics", raise_e=False, timeout=10) is not False
    
    def verify_3_5_headphone_output_selected_willie_robotics(self):
        return self.driver.wait_for_object("3_5_headphone_output_selected_willie_robotics", raise_e=False, timeout=10) is not False
    
    def verify_3_5_headphone_input_dropbox_show_up_willie_robotics(self):
        return self.driver.wait_for_object("3_5_headphone_input_dropbox_show_up_willie_robotics", raise_e=False, timeout=10) is not False
    
    def verify_usb_headphone_input_dropbox_show_up_willie_robotics(self):
        return self.driver.wait_for_object("usb_headphone_input_dropbox_show_up_willie_robotics", raise_e=False, timeout=10) is not False
    
    def verify_usb_headphone_output_dropbox_show_up_willie_robotics(self):
        return self.driver.wait_for_object("usb_headphone_output_dropbox_show_up_willie_robotics", raise_e=False, timeout=10) is not False
    
    def verify_microphone_array_dropbox_show_up_willie_robotics(self):
        return self.driver.wait_for_object("microphone_array_dropbox_show_up_willie_robotics", raise_e=False, timeout=15) is not False

    def launch_windows_app(self, app_name):
        self.driver.click("search_bar_on_windows", timeout = 20)
        time.sleep(3)
        self.driver.send_keys("search_bar_on_windows", app_name)
        time.sleep(5)
        el = self.driver.wait_for_object("search_bar_on_windows", displayed=False, timeout=10)
        el.send_keys(Keys.ENTER)
        time.sleep(5)
        el.send_keys(Keys.ENTER)
        time.sleep(5)
 
    def click_myhp_on_taskbar(self):
        if(self.driver.wait_for_object("myhp_on_task_bar", raise_e=False, timeout=10) is True):
            self.driver.click("myhp_on_task_bar", timeout= 20)

    def verify_calculator_app_show_on_application_list(self):
        return self.driver.wait_for_object("calculator_on_application_list", raise_e=False, timeout=10) 

    def verify_privacy_app_show_on_application_list(self):
        return self.driver.wait_for_object("privacy_on_application_list", raise_e=False, timeout=10)    

    def verify_error_icon_on_application_list(self):
        return self.driver.wait_for_object("error_icon_on_application_list", raise_e=False, timeout=10)
    
    def verify_retask_notification_toast_show(self):
        return self.driver.wait_for_object("retask_notification_toast", raise_e=False, timeout=10)  

    def verify_retask_notification_toast_select_options(self):
        return self.driver.get_attribute("retask_notification_toast_select_option", "Name", timeout=10)
    
    def click_retask_notification_toast_x_button(self):
        self.driver.click("retask_notification_toast_x_button", timeout=10)

    def click_retask_notification_settings_button(self):
        self.driver.click("retask_notification_settings_button", timeout=10)

    def click_retask_notification_turn_off_notifications(self):
        self.driver.click("retask_notification_turn_off_notifications", timeout=10)

    def click_retask_notification_combo_box(self):
        self.driver.click("retask_notification_combo_box", timeout=10)

    def click_retask_notification_toast_select_option_line_in(self):
        self.driver.click("retask_notification_toast_select_option_line_in", timeout=10)

    def verify_retask_notification_toast_select_option_line_in(self):
        return self.driver.get_attribute("retask_notification_toast_select_option_line_in", "Name", timeout=10)
    
    def click_retask_notification_toast_select_option_speaker(self):
        self.driver.click("retask_notification_toast_select_option", timeout=10)

    def click_retask_notification_toast_ok_button(self):
        self.driver.click("retask_notification_toast_ok_button", timeout=10)

    def get_retask_notification_turn_off_notifications(self):
        return self.driver.get_attribute("retask_notification_turn_off_notifications", "Name", timeout=10)
    
    def get_retask_notification_toast_go_to_notification(self):
        return self.driver.get_attribute("retask_notification_toast_go_to_notification", "Name", timeout=10)
    
    def click_retask_notification_toast_go_to_notification(self):
        self.driver.click("retask_notification_toast_go_to_notification", timeout=10)
    
    def set_audio_output_slider_value_decrease_for_analytics(self, value):
        slider = self.driver.wait_for_object("output_volume_slider", timeout = 10)
        self.driver.click("output_volume_slider", timeout = 10)
        output_value = int(float(self.get_output_slider_value()))
        for _ in range(value):
            time.sleep(2)  
            slider.send_keys(Keys.LEFT)
        
    def set_audio_output_slider_value_increase_for_analytics(self, value):
        slider = self.driver.wait_for_object("output_volume_slider", timeout = 10)
        self.driver.click("output_volume_slider", timeout = 10)
        for _ in range(value):
            time.sleep(2)
            slider.send_keys(Keys.RIGHT)

    def click_noise_removal_button(self):
        if self.driver.wait_for_object("ai_noise_removal_toggle_on", raise_e=False, timeout=5) is not False:
            self.driver.click("ai_noise_removal_toggle_on")
        else:
            self.driver.click("ai_noise_removal_toggle_off")
    
    def click_noise_reduction_button(self):
        if self.driver.wait_for_object("ai_noise_reduction_toggle_on", raise_e=False, timeout=5) is not False:
            self.driver.click("ai_noise_reduction_toggle_on")
        else:
            self.driver.click("ai_noise_reduction_toggle_off")

    def set_audio_input_slider_value_decrease_for_analytics(self, value):
        slider = self.driver.wait_for_object("input_volume_slider", timeout = 10)
        self.driver.click("input_volume_slider", timeout = 10)
        output_value = int(float(self.get_output_slider_value()))
        for _ in range(value):
            time.sleep(2)  
            slider.send_keys(Keys.LEFT)
        
    def set_audio_input_slider_value_increase_for_analytics(self, value):
        slider = self.driver.wait_for_object("input_volume_slider", timeout = 10)
        self.driver.click("input_volume_slider", timeout = 10)
        for _ in range(value):
            time.sleep(2)
            slider.send_keys(Keys.RIGHT)

    def set_eq_slider_value_decrease_for_analytics(self, element, value):
        slider = self.driver.wait_for_object(element, timeout = 10)
        self.driver.click(element, timeout = 10)
        for _ in range(value):
            time.sleep(2)  
            slider.send_keys(Keys.DOWN)
        
    def set_eq_slider_value_increase_for_analytics(self, element, value):
        slider = self.driver.wait_for_object(element, timeout = 10)
        self.driver.click(element, timeout = 10)
        for _ in range(value):
            time.sleep(2)
            slider.send_keys(Keys.UP)
    
    def click_immersive_toggle(self):
        if self.driver.wait_for_object("immersive_toggle_on", raise_e=False, timeout=5) is not False:
            self.driver.click("immersive_toggle_on")
        else:
            self.driver.click("immersive_toggle_off")

    def click_play_all_button(self):
        self.driver.click("play_all_button")

    def get_access_name_on_application_list(self):
        return self.driver.get_attribute("access_txt", "Name", timeout=10)

    def get_disney_name_on_application_list(self):
        return self.driver.get_attribute("disney_txt", "Name", timeout=10)
    
    def get_for_all_application_name_on_application_list(self):
        return self.driver.get_attribute("for_all_applications_text", "Name", timeout=10)

    def get_output_slider_value(self):
        return self.driver.get_attribute("output_slider_value","RangeValue.Value", raise_e=False, timeout=20)
    
    def get_input_slider_value(self):
        return self.driver.get_attribute("input_slider_value","RangeValue.Value", raise_e=False, timeout=20)

    def get_output_mute_button_on_status(self):
        return self.driver.get_attribute("mute_toggle_for_output","Toggle.ToggleState", raise_e=False, timeout=10)
    
    def get_input_mute_button_status(self):
        return self.driver.get_attribute("mute_toggle_for_input","Toggle.ToggleState", raise_e=False, timeout=10)

    def get_output_mute_button_status(self):
        return self.driver.get_attribute("mute_toggle_for_output","Toggle.ToggleState", raise_e=False, timeout=10)

    def verify_input_title(self):
        return self.driver.wait_for_object("input_title", raise_e=False, timeout=10) is not False

    def verify_adaptive_audio_settings_title_on_detail_page_show_up(self):
        return self.driver.wait_for_object("advanced_audio_settings_title_on_detail_page", raise_e=False, timeout=10) is not False
    
    def verify_adaptive_audio_title_show_up(self):
        return self.driver.wait_for_object("adaptive_audio_title", raise_e=False, timeout=10) is not False
    
    def verify_adaptive_audio_toggle_show_up(self):
        return self.driver.wait_for_object("adaptive_audio_toggle", raise_e=False, timeout=10) is not False

    def get_adaptive_audio_toggle_status(self):
        return self.driver.wait_for_object("adaptive_audio_toggle").is_enabled()
    
    def click_adaptive_audio_toggle(self):
        self.driver.click("adaptive_audio_toggle", timeout=10)

    def verify_automatic_title_show_up(self):
        return self.driver.wait_for_object("automatic_title", raise_e=False, timeout=10) is not False

    def verify_automatic_toggle_show_up(self):
        return self.driver.wait_for_object("automatic_toggle", raise_e=False, timeout=10) is not False
    
    def get_automatic_toggle_status(self):
        return self.driver.get_attribute("automatic_toggle", "SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def click_automatic_toggle(self):
        self.driver.click("automatic_toggle", timeout=10)

    def verify_near_to_display_title_show_up(self):
        return self.driver.wait_for_object("near_to_display_title", raise_e=False, timeout=10) is not False
    
    def verify_near_to_display_toggle_show_up(self):
        return self.driver.wait_for_object("near_to_display_toggle", raise_e=False, timeout=10) is not False
    
    def get_near_to_display_toggle_status(self):
        return self.driver.get_attribute("near_to_display_toggle", "SelectionItem.IsSelected", raise_e=False, timeout=10)

    def click_near_to_display_toggle(self):
        self.driver.click("near_to_display_toggle", timeout=15)

    def verify_far_from_display_title_show_up(self):
        return self.driver.wait_for_object("far_from_display_title", raise_e=False, timeout=10) is not False
    
    def verify_far_from_display_toggle_show_up(self):
        return self.driver.wait_for_object("far_from_display_toggle", raise_e=False, timeout=10) is not False

    def get_far_from_display_toggle_status(self):
        return self.driver.get_attribute("far_from_display_toggle", "SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def click_far_from_display_toggle(self):
        self.driver.click("far_from_display_toggle", timeout=10)

    def click_immersive_audio_toggle(self):
        self.driver.click("immersive_toggle", timeout=10)

    def verify_usb_headphone_is_be_selected(self):
        return self.driver.wait_for_object("output_usb_external_headphone", raise_e=False, timeout=10) is not False

    def get_retask_notification_toast_select_options_line_in(self):
        return self.driver.wait_for_object("retask_notification_toast_select_option_line_in", raise_e=False, timeout=10)

    def verify_adaptive_audio_toggle_status_not_on(self):
        return self.driver.get_attribute("adaptive_toggle_on", "Toggle.ToggleState", raise_e=False, timeout=10)
    
    def verify_adaptive_audio_toggle_status_on(self):
        return self.driver.get_attribute("adaptive_toggle_off", "Toggle.ToggleState", raise_e=False, timeout=10)

    def verify_input_usb_external_device_show_up(self):
        return self.driver.wait_for_object("input_usb_external_headphone_gidget", raise_e=False, timeout=10)

    def verify_apm_mode_title_show(self):
        return self.driver.wait_for_object("apm_mode_title", raise_e=False, timeout=10)
   
    def verify_apm_mode_toggle_show(self):
        return self.driver.wait_for_object("apm_mode_toggle", raise_e=False, timeout=10)
   
    def verify_apm_mode_tips_show(self):
        return self.driver.wait_for_object("apm_mode_tips", raise_e=False, timeout=10)
    
    def select_output_usb_external_device_arti(self):
        self.driver.click("output_device_usb_headphone_arti",timeout=10)

    def select_input_usb_external_device_arti(self):
        self.driver.click("input_usb_external_headphone_arti",timeout=10)

    def select_input_35mm_external_device_arti(self):
        self.driver.click("input_35mm_external_headphone_arti",timeout=10)

    def select_output_35mm_external_device_arti(self):
        self.driver.click("output_device_35mm_headphone_arti",timeout=10)

    def verify_output_usb_external_device_arti_show(self):
        return self.driver.wait_for_object("output_device_usb_headphone_arti", raise_e=False, timeout=10) is not False

    def verify_input_usb_external_device_arti_show(self):
        return self.driver.wait_for_object("input_usb_external_headphone_arti", raise_e=False, timeout=10) is not False

    def verify_output_35mm_external_device_arti_show(self):
        return self.driver.wait_for_object("output_device_35mm_headphone_arti", raise_e=False, timeout=10) is not False

    def verify_input_35mm_external_device_arti_show(self):
        return self.driver.wait_for_object("input_35mm_external_headphone_arti", raise_e=False, timeout=10) is not False

    def verify_apm_mode_toggle_status(self):
        return self.driver.get_attribute("apm_mode_toggle", "Toggle.ToggleState", raise_e=False, timeout=10)
   
    def click_apm_mode_toggle(self):
        self.driver.click("apm_mode_toggle", timeout=10)

    def verify_close_button_on_windows_settings_show_up(self):
        return self.driver.wait_for_object("close_button_on_windows_settings",raise_e=False, timeout=10)

    def verify_output_internal_device_show_on_london(self):
        return self.driver.wait_for_object("output_internal_device_london",raise_e=False, timeout=10)

    def select_output_internal_device_london(self):
        self.driver.click("output_internal_device_london")
    
    def verify_input_internal_device_show_on_thompson(self):
        return self.driver.wait_for_object("input_internal_device_thompson",raise_e=False, timeout=10)

    def select_input_internal_device_thompson(self):
        self.driver.click("input_internal_device_thompson")

    def verify_input_35mm_headphone_show_thompson(self):
        return self.driver.wait_for_object("input_35mm_headphone_thompson",raise_e=False, timeout=10)

    def select_input_35mm_headphone_thompson(self):
        self.driver.click("input_35mm_headphone_thompson")

    def verify_usb_headphone_output_selected_willie_robotics(self):
        return self.driver.wait_for_object("usb_headphone_output_selected_willie_robotics", raise_e=False, timeout=10)

    def click_noise_reduction_tooltip(self):
        self.driver.click("noise_reduction_tooltip", timeout=10)

    def click_ai_noise_removal_tooltip(self):
        self.driver.click("ai_noise_removal_tooltip", timeout=10)

    def get_ai_noise_removal_tooltip_text(self):
        return self.driver.get_attribute("ai_noise_removal_tooltip", "Name", timeout=10)
    
    def get_noise_reduction_tooltip_text(self):
        return self.driver.get_attribute("noise_reduction_tooltip", "Name", timeout=10)

    def verify_audio_standalone_app_on_application_list(self):
        return self.driver.wait_for_object("audio_standalone_app", raise_e=False, timeout=10) is not False

    def verify_back_button_on_audio_page(self):
        return self.driver.wait_for_object("back_button_on_audio_page",raise_e=False, timeout=10) is not False

    def click_mic_mode_tooltip_contents(self):
        self.driver.click("mic_mode_tooltip_contents", timeout=10)

    def get_mic_mode_tooltip_contents(self):
        return self.driver.get_attribute("mic_mode_tooltip_contents", "Name", timeout=10)

    def click_APM_tooltip_contents(self):
        self.driver.click("apm_tooltip_contents", timeout=10)

    def get_APM_tooltip_contents(self):
        return self.driver.get_attribute("apm_tooltip_contents", "Name", timeout=10)

    def verify_output_device_headphone_show_up_willie_robotics(self):
        return self.driver.wait_for_object("output_device_3.5mm_headphone_willie_robotics", raise_e=False, timeout=10) is not False

    def verify_external_speaker_settings_title_show_up(self):
        return self.driver.wait_for_object("external_speaker_settings_title", raise_e=False, timeout=10) is not False
    
    def verify_arrow_right_on_external_speaker_settings_show_up(self):
        return self.driver.wait_for_object("arrow_right_on_external_speaker_settings", raise_e=False, timeout=10) is not False
    
    def click_arrow_right_on_external_speaker_settings(self):
        self.driver.click("arrow_right_on_external_speaker_settings", timeout=10)

    def verify_output_internal_speaker_show_up_on_arti(self):
        return self.driver.wait_for_object("output_device_internal_speaker", raise_e=False, timeout=10) is not False

    def verify_output_internal_device_show_on_arti(self):
        return self.driver.wait_for_object("output_internal_speaker_on_arti",raise_e=False, timeout=10) is not False
 
    def click_output_combobox_open_button(self):
        self.driver.click("output_combobox_open_button", timeout=10)
 
    def verify_output_internal_device_arti_show(self):
        return self.driver.wait_for_object("output_internal_device_arti", raise_e=False, timeout=10) is not False
    
    def select_output_internal_device_arti(self):
        self.driver.click("output_internal_device_arti", timeout=10)
 
    def verify_external_speaker_settings_show_up(self):
        if self.driver.wait_for_object("external_speaker_settings_title", raise_e=False, timeout=10) is False:
            try:
                self.driver.scroll_element("external_speaker_settings_title", direction="down", distance=15, time_out=20)
            except Exception:
                pass 
        return self.driver.wait_for_object("external_speaker_settings_title", raise_e=False, timeout=10) is not False
 
    def click_external_speaker_settings(self):
        self.driver.click("advanced_audio_settings_arrow", timeout=10)
 
    def verify_external_speaker_settings_text_show_up(self):
        return self.driver.wait_for_object("external_speaker_settings_title", raise_e=False, timeout=10) is not False
    
    def verify_speaker_configuration_text_show_up(self):
        return self.driver.wait_for_object("speaker_configuration_text", raise_e=False, timeout=10) is not False
    
    def verify_speaker_configuration_option_surround_combox_show_up(self):
        return self.driver.wait_for_object("speaker_configuration_drop_down_list_option_surround", raise_e=False, timeout=10) is not False
    
    def click_speaker_configuration_open_option(self):
        self.driver.click("speaker_configuration_option", timeout=10)
 
    def verify_speaker_configuration_option_surround_show_up(self):
        return self.driver.wait_for_object("speaker_configuration_drop_down_list_option_surround", raise_e=False, timeout=10) is not False
    
    def select_speaker_configuration_option_surround(self):
        self.driver.click("speaker_configuration_drop_down_list_option_surround", timeout=10)
 
    def verify_front_left_speaker_distance(self):
        return self.driver.get_attribute("front_left_speaker_distance", "Name", raise_e=False, timeout=10) 
    
    def verify_front_left_speaker_distance_combobox_14_9_ft_show_up(self):
        return self.driver.wait_for_object("front_left_speaker_distance_14.9", raise_e=False, timeout=10) is not False

    def select_front_left_speaker_distance_combobox_14_9_ft(self):
        self.driver.click("front_left_speaker_distance_14.9", timeout=10)
 
    def verify_front_left_speaker_volume(self):
        return self.driver.get_attribute("front_left_speaker_volume", "Name", raise_e=False, timeout=10)
 
    def verify_front_left_speaker_volume_combobox_1_db_show_up(self):
        return self.driver.wait_for_object("front_left_speaker_volume_-1", raise_e=False, timeout=10) is not False

    def select_front_left_speaker_volume_combobox_1_db(self):
        self.driver.click("front_left_speaker_volume_-1", timeout=10)

    def is_for_all_application_button_selected(self):
        return self.driver.get_attribute("global_icon", "SelectionItem.IsSelected", raise_e=False, timeout=10)

    def get_presets_RPG_button_status(self):
        return self.driver.get_attribute("audio_presets_RPG_button", "SelectionItem.IsSelected", raise_e=False, timeout=10)

    def get_presets_shooter_button_status(self):
        return self.driver.get_attribute("audio_presets_shooter_button", "SelectionItem.IsSelected", raise_e=False, timeout=10)

    def get_presets_strategy_button_status(self):
        return self.driver.get_attribute("audio_presets_strategy_button", "SelectionItem.IsSelected", raise_e=False, timeout=10)

    def click_audio_presets_RPG_button(self):
        self.driver.click("audio_presets_RPG_button", timeout=10)
    
    def click_audio_presets_shooter_button(self):
        self.driver.click("audio_presets_shooter_button", timeout=10)
        
    def click_audio_presets_strategy_button(self):
        self.driver.click("audio_presets_strategy_button", timeout=10)

    def verify_audio_presets_auto_txt_show_up(self):
        return self.driver.wait_for_object("audio_presets_auto_txt", raise_e=False, timeout=10) is not False

    def verify_audio_presets_auto_button_show_up(self):
        return self.driver.wait_for_object("audio_presets_auto_button", raise_e=False, timeout=10) is not False
    
    def click_audio_presets_auto_button(self):
        self.driver.click("audio_presets_auto_button", timeout=10)

    def get_audio_presets_auto_button_status(self):
        return self.driver.get_attribute("audio_presets_auto_button", "SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def verify_output_internal_speaker_commercial_show_up(self):
        return self.driver.wait_for_object("output_internal_speaker_commercial", raise_e=False, timeout=10) is not False

    def verify_input_internal_mic_commercial_show_up(self):
        return self.driver.wait_for_object("input_internal_mic_commercial", raise_e=False, timeout=10) is not False

    def verify_input_35mm_headphone_commercial_show_up(self):
        return self.driver.wait_for_object("input_35mm_headphone_commercial", raise_e=False, timeout=10) is not False
    
    def verify_output_35mm_headphone_commercial_show_up(self):
        return self.driver.wait_for_object("output_35mm_headphone_commercial", raise_e=False, timeout=10) is not False
    
    def verify_input_usb_headphone_commercial_show_up(self):
        return self.driver.wait_for_object("input_usb_headphone_commercial", raise_e=False, timeout=10) is not False

    def verify_output_usb_headphone_commercial_show_up(self):
        return self.driver.wait_for_object("output_usb_headphone_commercial", raise_e=False, timeout=10) is not False

    def click_output_internal_speaker_commercial(self):
        self.driver.click("output_internal_speaker_commercial", timeout=10)

    def click_input_internal_mic_commercial(self):
        self.driver.click("input_internal_mic_commercial", timeout=10)

    def click_input_35mm_headphone_commercial(self):
        self.driver.click("input_35mm_headphone_commercial", timeout=10)

    def click_output_35mm_headphone_commercial(self):
        self.driver.click("output_35mm_headphone_commercial", timeout=10)

    def click_input_usb_headphone_commercial(self):
        self.driver.click("input_usb_headphone_commercial", timeout=10)

    def click_output_usb_headphone_commercial(self):
        self.driver.click("output_usb_headphone_commercial", timeout=10)

    def install_audio_standalone_app_by_task_scheduler(self):
        app_path = "C:\\build\HPAudioControl_19H1_2.51.339.99_Test\\Install.ps1"      
        if "HPAudioControl" in app_path:
            self.driver.ssh.send_command(f'schtasks /create /tn "InstallAppNow" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File {app_path} -Force" /sc once /st 00:00 /f', timeout=60)   
            self.driver.ssh.send_command('schtasks /run /tn "InstallAppNow"', timeout=240)
            time.sleep(10)
            file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\RealtekSemiconductorCorp.HPAudioControl_dt26b99r8h8gj\\LocalCache"'
            file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            max_attempts = 5
            for _ in range(max_attempts):
                if file_exist:
                    break
                time.sleep(10)
                file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
            time.sleep(10)
            self.driver.ssh.send_command('schtasks /delete /tn "InstallAppNow" /f', timeout=60)

    def verify_vertical_value_0_show_up(self):
        return self.driver.wait_for_object("vertical_value_0", raise_e=False, timeout=10) is not False

    def verify_vertical_value_20_show_up(self):
        return self.driver.wait_for_object("vertical_value_20", raise_e=False, timeout=10) is not False

    def verify_vertical_value_40_show_up(self):
        return self.driver.wait_for_object("vertical_value_40", raise_e=False, timeout=10) is not False
    
    def verify_vertical_value_60_show_up(self):
        return self.driver.wait_for_object("vertical_value_60", raise_e=False, timeout=10) is not False

    def verify_vertical_value_80_show_up(self):
        return self.driver.wait_for_object("vertical_value_80", raise_e=False, timeout=10) is not False

    def verify_vertical_value_100_show_up(self):
        return self.driver.wait_for_object("vertical_value_100", raise_e=False, timeout=10) is not False

    def verify_input_mic_on_windows_show_up(self):
        return self.driver.wait_for_object("input_mic_on_windows", raise_e=False, timeout=10) is not False
    
    def click_input_mic_on_windows(self):
        self.driver.click("input_mic_on_windows", timeout=10)

    def verify_audio_enhancements_on_windows_show_up(self):
        return self.driver.wait_for_object("audio_enhancements_on_windows", raise_e=False, timeout=10) is not False

    def click_audio_enhancements_combobox_on_windows(self):
        self.driver.click("audio_enhancements_combobox_on_windows", timeout=10)

    def verify_audio_enhancements_combobox_on_windows_show_up(self):
        return self.driver.wait_for_object("audio_enhancements_combobox_on_windows",raise_e=False, timeout=10) is not False

    def verify_mep_option_on_windows_show_up(self):
        return self.driver.wait_for_object("mep_option_on_windows",raise_e=False, timeout=10) is not False

    def click_mep_option_on_windows(self):
        self.driver.click("mep_option_on_windows", timeout=10)

    def verify_non_mep_option_on_windows_show_up(self):
        return self.driver.wait_for_object("non_mep_option_on_windows",raise_e=False, timeout=10) is not False
    
    def click_non_mep_option_on_windows(self):
        self.driver.click("non_mep_option_on_windows", timeout=10)

    def verify_mep_notification_toast_show_up(self):
        return self.driver.wait_for_object("mep_notification_toast", raise_e=False, timeout=10) is not False

    def verify_mep_ui_show_up(self):
        return self.driver.wait_for_object("mep_ui", raise_e=False, timeout=10) is not False

    def verify_windows_sound_settings_mep_show_up(self):
        return self.driver.wait_for_object("windows_sound_settings_mep", raise_e=False, timeout=10) is not False
    
    def verify_learn_more_link_title_on_mep_show_up(self):
        return self.driver.wait_for_object("learn_more_link_on_mep", raise_e=False, timeout=10) is not False

    def verify_sound_title_on_windows_show_up(self):
        return self.driver.wait_for_object("sound_title_on_windows", raise_e=False, timeout=10)

    def verify_settings_on_taskbar_show_up(self):
        return self.driver.wait_for_object("settings_on_taskbar", raise_e=False, timeout=10) is not False

    def click_settings_on_taskbar(self):
        self.driver.click("settings_on_taskbar", timeout=10)

    def verify_mep_contents_on_myhp_show_up(self):
        return self.driver.wait_for_object("mep_contents_on_myhp", raise_e=False, timeout=10) is not False

    def click_learn_more_link_on_mep(self):
        self.driver.click("learn_more_link_on_mep", timeout=10)

    def verify_mep_pop_up_dialog_title_show_up(self):
        return self.driver.wait_for_object("mep_pop_up_dialog_title", raise_e=False, timeout=10) is not False
    
    def verify_mep_pop_up_dialog_second_title_show_up(self):
        return self.driver.wait_for_object("mep_pop_up_dialog_second_title", raise_e=False, timeout=10) is not False

    def verify_noise_reduction_contents_on_mep_pop_up_dialog_show_up(self):
        return self.driver.wait_for_object("noise_reduction_contents_on_mep_pop_up_dialog", raise_e=False, timeout=10) is not False
    
    def verify_conference_mode_contents_on_mep_pop_up_dialog_show_up(self):
        return self.driver.wait_for_object("conference_mode_contents_on_mep_pop_up_dialog", raise_e=False, timeout=10) is not False
    
    def verify_personal_mode_contents_on_mep_pop_up_dialog_show_up(self):
        return self.driver.wait_for_object("personal_mode_contents_on_mep_pop_up_dialog", raise_e=False, timeout=10) is not False

    def verify_studio_recording_mode_contents_on_mep_pop_up_dialog_show_up(self):
        return self.driver.wait_for_object("studio_recording_mode_contents_on_mep_pop_up_dialog", raise_e=False, timeout=10) is not False

    def verify_cancel_button_on_mep_pop_up_dialog_show_up(self):
        return self.driver.wait_for_object("cancel_button_on_mep_pop_up_dialog", raise_e=False, timeout=10) is not False

    def verify_go_to_windows_sound_settings_button_on_mep_pop_up_dialog_show_up(self):
        return self.driver.wait_for_object("go_to_windows_sound_settings_button_on_mep_pop_up_dialog", raise_e=False, timeout=10) is not False

    def click_cancel_button_on_mep_pop_up_dialog(self):
        self.driver.click("cancel_button_on_mep_pop_up_dialog", timeout=10)

    def verify_input_device_show_up(self):
        return self.driver.wait_for_object("input_device_on_windows", raise_e=False, timeout=10) is not False

    def click_input_device_on_windows(self):
        self.driver.click("input_device_on_windows", timeout=10)

    def verify_system_button_on_windows_show_up(self):
        return self.driver.wait_for_object("system_button_on_windows", raise_e=False, timeout=10) is not False
    
    def click_system_button_on_windows(self):
        self.driver.click("system_button_on_windows", timeout=10)

    def verify_sound_button_on_windows_show_up(self):
        return self.driver.wait_for_object("sound_button_on_windows",raise_e=False, timeout=10) is not False
    
    def click_sound_button_on_windows(self):
        self.driver.click("sound_button_on_windows", timeout=10)

    def is_enabled_ai_noise_removal_toggle(self):
        if self.driver.wait_for_object("ai_noise_removal_toggle_off",raise_e=False, timeout=10):
            return self.driver.get_attribute("ai_noise_removal_toggle_off", "IsEnabled", raise_e=False, timeout=10)
        else:
            self.driver.wait_for_object("ai_noise_removal_toggle_on",raise_e=False, timeout=10)
            return self.driver.get_attribute("ai_noise_removal_toggle_on", "IsEnabled", raise_e=False, timeout=10)

    def is_enabled_noise_reduction_toggle(self):
        if self.driver.wait_for_object("ai_noise_reduction_toggle_on",raise_e=False, timeout=10):
            return self.driver.get_attribute("ai_noise_reduction_toggle_on", "IsEnabled", raise_e=False, timeout=10)
        else:
            self.driver.wait_for_object("ai_noise_reduction_toggle_off",raise_e=False, timeout=10)
            return self.driver.get_attribute("ai_noise_reduction_toggle_off", "IsEnabled", raise_e=False, timeout=10)

    def is_enabled_mic_mode_toggle(self):
        self.driver.wait_for_object("mic_mode_combobox_status",raise_e=False, timeout=10)
        return self.driver.get_attribute("mic_mode_combobox_status", "IsEnabled", raise_e=False, timeout=10)

    def verify_off_option_on_windows_input_side_show_up(self):
        return self.driver.wait_for_object("off_option_on_windows_input_side", raise_e=False, timeout=10) is not False
    
    def click_off_option_on_windows_input_side(self):
        self.driver.click("off_option_on_windows_input_side", timeout=10)

    def swipe_to_restore_defaults_button(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to restore_defaults_button
        try:
            self.driver.scroll_element("restore_defaults_button", direction="down", distance=12, time_out=20)
        except Exception:
            pass  
        return self.driver.wait_for_object("restore_defaults_button", raise_e=False, timeout = 5)

    def verify_35mm_headphone_for_divinity_output_device_show_up(self):
        return self.driver.wait_for_object("35mm_headphone_for_divinity_output_device", raise_e=False, timeout=10) is not False

    def click_35mm_headphone_for_divinity_output_device(self):
        self.driver.click("35mm_headphone_for_divinity_output_device", timeout=10)

    def verify_35mm_headphone_for_divinity_input_device_show_up(self):
        return self.driver.wait_for_object("35mm_headphone_for_divinity_input_device", raise_e=False, timeout=10) is not False

    def click_35mm_headphone_for_divinity_input_device(self):
        self.driver.click("35mm_headphone_for_divinity_input_device", timeout=10)

    def click_learn_more_link_on_mep(self):
        self.driver.click("learn_more_link_on_mep", timeout=10)

    def click_go_to_windows_sound_settings_button_on_mep_pop_up_dialog(self):
        self.driver.click("go_to_windows_sound_settings_button_on_mep_pop_up_dialog", timeout=10)

    def verify_mep_notification_windows_toast_show_up(self):
        return self.driver.wait_for_object("mep_notification_windows_toast", raise_e=False, timeout=10) is not False
    
    def verify_mep_notification_hp_title_show_up(self):
        return self.driver.wait_for_object("mep_notification_hp_title", raise_e=False, timeout=10) is not False

    def verify_settings_for_this_notification_show_up(self):
        return self.driver.wait_for_object("settings_for_this_notification", raise_e=False, timeout=10) is not False

    def verify_move_this_notification_to_notification_center_show_up(self):
        return self.driver.wait_for_object("move_this_notification_to_notification_center", raise_e=False, timeout=10) is not False

    def verify_audio_effects_switch_show_up(self):
        return self.driver.wait_for_object("audio_effects_switch", raise_e=False, timeout=10) is not False

    def verify_mep_notification_switch_back_button_show_up(self):
        return self.driver.wait_for_object("mep_notification_switch_back_button", raise_e=False, timeout=10) is not False

    def verify_mep_notification_dismiss_button_show_up(self):
        return self.driver.wait_for_object("mep_notification_dismiss_button", raise_e=False, timeout=10) is not False

    def click_mep_notification_dismiss_button(self):
        self.driver.click("mep_notification_dismiss_button", timeout=10)

    def click_mep_notification_switch_back_button(self):
        self.driver.click("mep_notification_switch_back_button", timeout=10)

    def click_settings_for_this_notification(self):
        self.driver.click("settings_for_this_notification", timeout=10)

    def click_move_this_notification_to_notification_center(self):
        self.driver.click("move_this_notification_to_notification_center", timeout=10)

    def verify_all_sounds_devices_on_windows_show_up(self):
        return self.driver.wait_for_object("all_sounds_devices_on_windows", raise_e=False, timeout=10) is not False
    
    def verify_internal_speaker_for_divinity_output_device_show_up(self):
        return self.driver.wait_for_object("internal_speaker_for_divinity_output_device", raise_e=False, timeout=10) is not False
    
    def click_internal_speaker_for_divinity_output_device(self):
        self.driver.click("internal_speaker_for_divinity_output_device", timeout=10)

    def verify_internal_mic_for_divinity_input_device_show_up(self):
        return self.driver.wait_for_object("internal_mic_for_divinity_input_device", raise_e=False, timeout=10) is not False

    def click_internal_mic_for_divinity_input_device(self):
        self.driver.click("internal_mic_for_divinity_input_device", timeout=10)

    def verify_usbheadphone_for_divinity_output_device_show_up(self):
        return self.driver.wait_for_object("usb_headphone_for_divinity_output_device", raise_e=False, timeout=10) is not False

    def click_usb_headphone_for_divinity_output_device(self):
        self.driver.click("usb_headphone_for_divinity_output_device", timeout=10)

    def verify_usb_headphone_for_divinity_input_device_show_up(self):
        return self.driver.wait_for_object("usb_headphone_for_divinity_input_device", raise_e=False, timeout=10) is not False

    def click_usb_headphone_for_divinity_input_device(self):
        self.driver.click("usb_headphone_for_divinity_input_device", timeout=10)

    def verify_audio_standalone_app_in_app_list(self):
        return self.driver.wait_for_object("audio_standalone_app_in_app_list", raise_e=False, timeout=10)

    def verify_dts_sound_unbound_link_on_myhp_show_up(self):
        return self.driver.wait_for_object("dts_sound_unbound_link_on_myhp", raise_e=False, timeout=10) is not False

    def click_dts_sound_unbound_link_on_myhp(self):
        self.driver.click("dts_sound_unbound_link_on_myhp", timeout=10)

    def verify_dts_sound_unbound_dialog_privacy_page_title_show_up(self):
        return self.driver.wait_for_object("dts_sound_unbound_dialog_privacy_page_title", raise_e=False, timeout=10) is not False

    def verify_dts_sound_unbound_dialog_title_show_up(self):
        return self.driver.wait_for_object("dts_sound_unbound_dialog_title", raise_e=False, timeout=10) is not False

    def verify_cancel_button_on_dts_sound_unbound_dialog_show_up(self):
        return self.driver.wait_for_object("cancel_button_on_dts_sound_unbound_dialog", raise_e=False, timeout=10) is not False
    
    def click_cancel_button_on_dts_sound_unbound_dialog(self):
        self.driver.click("cancel_button_on_dts_sound_unbound_dialog", timeout=10)

    def verify_multistreaming_toggle_show_up(self):
        return self.driver.wait_for_object("multistreaming_toggle_on_state", raise_e=False, timeout=10) is not False
 
    def get_multistreaming_toggle_on_state(self):
        return self.driver.get_attribute("multistreaming_toggle_on_state", "Toggle.ToggleState", raise_e=False, timeout=10)
   
    def click_multistreaming_toggle_on_state(self):
        self.driver.click("multistreaming_toggle_on_state", timeout=10)
 
    def get_multistreaming_toggle_off_state(self):
        return self.driver.get_attribute("multistreaming_toggle_off_state", "Toggle.ToggleState", raise_e=False, timeout=10)
   
    def click_multistreaming_toggle_off_state(self):
        self.driver.click("multistreaming_toggle_off_state", timeout=10)
 
    def verify_output_external_speaker_headphone_show(self):
        return self.driver.wait_for_object("output_device_external_speaker_headphone", raise_e=False, timeout=10) is not False

    def click_front_left_speaker_distance_combobox(self):
        self.driver.click("front_left_speaker_distance", timeout=10)

    def click_front_left_speaker_volume_combobox(self):
        self.driver.click("front_left_speaker_volume", timeout=10)

    def verify_speaker_not_support_dialog_pop_up(self):
        return self.driver.wait_for_object("speaker_not_support_dialog_pop_up", raise_e=False, timeout=10) is not False

    def click_continue_button_on_speaker_not_support_dialog(self):
        self.driver.click("continue_button_on_speaker_not_support_dialog", timeout=10)

    def verify_dts_unbound_link_show_up(self):
        if self.driver.wait_for_object("dts_sound_unbound_link_on_myhp", raise_e=False, timeout=20) is False:
            try:
                self.driver.scroll_element("dts_sound_unbound_link_on_myhp", direction="down", distance=11, time_out=50)
            except Exception:
                pass
        return self.driver.wait_for_object("dts_sound_unbound_link_on_myhp", raise_e=False, timeout=10)

    def verify_tooltips_for_app_on_the_application_list_show_up(self):
        return self.driver.wait_for_object("tooltips_for_app_on_the_application_list", raise_e=False, timeout=10) is not False

    def verify_settings_on_MEP_notification_show_up(self):
        return self.driver.wait_for_object("settings_on_MEP_notification", raise_e=False, timeout=10) is not False
    
    def click_settings_on_MEP_notification(self):
        self.driver.click("settings_on_MEP_notification", timeout=10)

    def verify_go_to_notification_settings_button_on_MEP_notification_show_up(self):
        return self.driver.wait_for_object("go_to_notification_settings_button_on_MEP_notification", raise_e=False, timeout=10) is not False

    def click_go_to_notification_settings_button_on_MEP_notification(self):
        self.driver.click("go_to_notification_settings_button_on_MEP_notification", timeout=10)

    def verify_notification_toggle_on_windows_settings_page_show_up(self):
        return self.driver.wait_for_object("notification_toggle_on_windows_settings_page", raise_e=False, timeout=10) is not False

    def click_notification_toggle_on_windows_settings_page(self):
        self.driver.click("notification_toggle_on_windows_settings_page", timeout=10)

    def verify_turn_off_notifications_for_hp_button_on_MEP_notification_show_up(self):
        return self.driver.wait_for_object("turn_off_notifications_for_hp_button_on_MEP_notification", raise_e=False, timeout=10) is not False

    def click_turn_off_notifications_for_hp_button_on_MEP_notification(self):
        self.driver.click("turn_off_notifications_for_hp_button_on_MEP_notification", timeout=10)

    def verify_audio_card_show_up(self):
        return self.driver.wait_for_object("audio_card_on_home_page", raise_e=False, timeout=10) is not False

    def verify_open_myhp_button_show_up(self):
        return self.driver.wait_for_object("open_myhp_button", raise_e=False, timeout=20) is not False

    def click_open_myhp_button(self):
        self.driver.click("open_myhp_button")

    def verify_not_now_button_show_up(self):
        return self.driver.wait_for_object("not_now_button", raise_e=False, timeout=10) is not False

    def click_not_now_button(self):
        self.driver.click("not_now_button")

    def verify_close_audio_standalone_app_button_show_up(self):
        return self.driver.wait_for_object("close_audio_standalone_app_button", raise_e=False, timeout=10) is not False

    def click_close_audio_standalone_app_button(self):
        self.driver.click("close_audio_standalone_app_button")

    
    def swipe_to_external_speaker_settings_restore_defaults_button(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to restore_defaults_button
        try:
            self.driver.scroll_element("external_speaker_settings_restore_default", direction="down", distance=12, time_out=20)
        except Exception:
            pass  
        return self.driver.wait_for_object("external_speaker_settings_restore_default", raise_e=False, timeout = 5)
 
    def click_external_speaker_settings_restore_default(self):
        self.driver.click("external_speaker_settings_restore_default", timeout=10)
 
    def select_output_external_speaker_headphone(self):
        self.driver.click("output_device_external_speaker_headphone", timeout=10)
    def get_output_drop_down_list_name(self):
        return self.driver.get_attribute("output_device_external_speaker_headphone", "Name", raise_e=False, timeout=10)
 
    def get_speaker_configuration_option(self):
        return self.driver.get_attribute("speaker_configuration_option", "Name", raise_e=False, timeout=10)
 
    def verify_continue_button_on_speaker_not_support_dialog(self):
        return self.driver.wait_for_object("continue_button_on_speaker_not_support_dialog", raise_e=False, timeout=10) is not False
 
    def click_continue_button_on_speaker_not_support_dialog(self):
        self.driver.click("continue_button_on_speaker_not_support_dialog", timeout=10)
 
    def verify_multistreaming_toggle_off_show_up(self):
        return self.driver.wait_for_object("multistreaming_toggle_off_state", raise_e=False, timeout=10) is not False
 
    def verify_multistreaming_toggle_on_show_up(self):
        return self.driver.wait_for_object("multistreaming_toggle_on_state", raise_e=False, timeout=10) is not False

    def verify_turn_off_notification_from_myhp_side_show_up(self):
        return self.driver.wait_for_object("turn_off_notification_from_myhp_side", raise_e=False, timeout=10) is not False
    
    def click_turn_off_notification_from_myhp_side(self):
        self.driver.click("turn_off_notification_from_myhp_side", timeout=10)

    def is_hp_notification_toggle_enabled(self):
        return self.driver.get_attribute("hp_notification_toggle_on_windows_settings_page", "Toggle.ToggleState", raise_e=False, timeout=10)

    def verify_hp_notification_toggle_on_windows_settings_page_show_up(self):
        if self.driver.wait_for_object("hp_notification_toggle_on_windows_settings_page", raise_e=False, timeout=20) is False:
            try:
                self.driver.scroll_element("hp_notification_toggle_on_windows_settings_page", direction="down", distance=2, time_out=50)
            except Exception:
                pass  
        return self.driver.wait_for_object("hp_notification_toggle_on_windows_settings_page", raise_e=False, timeout=10) is not False

    def click_hp_notification_toggle_on_windows_settings_page(self):
        self.driver.click("hp_notification_toggle_on_windows_settings_page", timeout=10)

    def select_speaker_configuration_option_stereo(self):
        self.driver.click("speaker_configuration_drop_down_list_option_stereo", timeout=10)

    def select_speaker_configuration_option_quad(self):
        self.driver.click("speaker_configuration_drop_down_list_option_quad", timeout=10)

    def verify_speaker_configuration_option_stereo_show_up(self):
        return self.driver.wait_for_object("speaker_configuration_drop_down_list_option_stereo", raise_e=False, timeout=10) is not False

    def verify_speaker_configuration_option_quad_show_up(self):
        return self.driver.wait_for_object("speaker_configuration_drop_down_list_option_quad", raise_e=False, timeout=10) is not False

    def verify_combine_headphone_for_speaker_configuration_show_up(self):
        return self.driver.wait_for_object("combine_headphone_for_speaker_configuration", raise_e=False, timeout=10) is not False

    def select_combine_headphone_for_speaker_configuration(self):
        self.driver.click("combine_headphone_for_speaker_configuration", timeout=10)

    def verify_front_left_speaker_title_show_up(self):
        return self.driver.wait_for_object("front_left_speaker_title", raise_e=False, timeout=10) is not False

    def verify_front_left_speaker_play_button_show_up(self):
        return self.driver.wait_for_object("front_left_speaker_play_button", raise_e=False, timeout=10) is not False

    def click_front_left_speaker_play_button(self):
        self.driver.click("front_left_speaker_play_button", timeout=10)

    def verify_front_right_speaker_title_show_up(self):
        return self.driver.wait_for_object("front_right_speaker_title", raise_e=False, timeout=10) is not False

    def verify_front_right_speaker_play_button_show_up(self):
        return self.driver.wait_for_object("front_right_speaker_play_button", raise_e=False, timeout=10) is not False

    def click_front_right_speaker_play_button(self):
        self.driver.click("front_right_speaker_play_button", timeout=10)

    def verify_back_left_speaker_title_show_up(self):
        return self.driver.wait_for_object("back_left_speaker_title", raise_e=False, timeout=10) is not False

    def verify_back_left_speaker_play_button_show_up(self):
        return self.driver.wait_for_object("back_left_speaker_play_button", raise_e=False, timeout=10) is not False

    def click_back_left_speaker_play_button(self):
        self.driver.click("back_left_speaker_play_button", timeout=10)

    def verify_back_right_speaker_title_show_up(self):
        return self.driver.wait_for_object("back_right_speaker_title", raise_e=False, timeout=10) is not False

    def verify_back_right_speaker_play_button_show_up(self):
        return self.driver.wait_for_object("back_right_speaker_play_button", raise_e=False, timeout=10) is not False

    def click_back_right_speaker_play_button(self):
        self.driver.click("back_right_speaker_play_button", timeout=10)

    def verify_subwoofer_speaker_title_show_up(self):
        return self.driver.wait_for_object("subwoofer_speaker_title", raise_e=False, timeout=10) is not False
    
    def verify_subwoofer_speaker_play_button_show_up(self):
        return self.driver.wait_for_object("subwoofer_speaker_play_button", raise_e=False, timeout=10) is not False

    def click_subwoofer_speaker_play_button(self):
        self.driver.click("subwoofer_speaker_play_button", timeout=10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_output_title_show_up_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("output_title", raise_e=False, timeout=10) is not False

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_input_title_show_up_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("input_title", raise_e=False, timeout=10) is not False

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_audio_presets_movie_txt_show_up_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("audio_presets_movie_txt", raise_e=False, timeout=10) is not False

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_advanced_audio_settings_title_show_up_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        if self.driver.wait_for_object("advanced_audio_settings_title", raise_e=False, timeout=10) is False:
            self.driver.scroll_element("advanced_audio_settings_title", direction="down", distance=6, time_out=50)
        return self.driver.wait_for_object("advanced_audio_settings_title", raise_e=False, timeout=10) is not False

    @screenshot_compare(include_param=["machine_name", "page_number", "color"])
    def verify_output_title_show_up_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "color"])
    def verify_input_title_show_up_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "color"])
    def verify_audio_presets_movie_txt_show_up_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    

    @screenshot_compare(include_param=["mode"])
    def verify_output_title_show_up_system_mode(self, mode):
        return self.driver.wait_for_object("output_title", raise_e = False, timeout = 10)

    @screenshot_compare(include_param=["mode"])
    def verify_input_title_show_up_system_mode(self, mode):
        return self.driver.wait_for_object("input_title", raise_e = False, timeout = 10)

    @screenshot_compare(include_param=["mode"])
    def verify_audio_presets_movie_txt_show_up_system_mode(self, mode):
        return self.driver.wait_for_object("audio_presets_movie_txt", raise_e = False, timeout = 10)

    def verify_subwofer_speaker_title_show_up(self):
        return self.driver.wait_for_object("subwoofer_speaker_title", raise_e=False, timeout=10) is not False

    def verify_subwofer_speaker_play_button_show_up(self):
        return self.driver.wait_for_object("subwoofer_speaker_play_button", raise_e=False, timeout=10) is not False

    def click_subwofer_speaker_play_button(self):
        self.driver.click("subwoofer_speaker_play_button", timeout=10)

    def verify_center_speaker_title_show_up(self):
        return self.driver.wait_for_object("center_speaker_title", raise_e=False, timeout=10) is not False

    def verify_center_speaker_play_button_show_up(self):
        return self.driver.wait_for_object("center_speaker_play_button", raise_e=False, timeout=10) is not False

    def click_center_speaker_play_button(self):
        self.driver.click("center_speaker_play_button", timeout=10)

    def verify_front_left_speaker_distance_open_button_show_up(self):
        return self.driver.wait_for_object("front_left_speaker_distance_open_button", raise_e=False, timeout=10) is not False

    def click_front_left_speaker_distance_open_button(self):
        self.driver.click("front_left_speaker_distance_open_button", timeout=10)

    def verify_front_left_speaker_volume_open_button_show_up(self):
        return self.driver.wait_for_object("front_left_speaker_volume_open_button", raise_e=False, timeout=10) is not False

    def click_front_left_speaker_volume_open_button(self):
        self.driver.click("front_left_speaker_volume_open_button", timeout=10)

    def verify_vertical_axis_15_show_up(self):
        return self.driver.wait_for_object("vertical_axis_15", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_7_show_up(self):
        return self.driver.wait_for_object("vertical_axis_7", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_minus_7_show_up(self):
        return self.driver.wait_for_object("vertical_axis_minus_7", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_minus_15_show_up(self):
        return self.driver.wait_for_object("vertical_axis_minus_15", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_12_show_up(self):
        return self.driver.wait_for_object("vertical_axis_12", raise_e=False, timeout=10) is not False

    def verify_vertical_axis_minus_12_show_up(self):
        return self.driver.wait_for_object("vertical_axis_minus_12", raise_e=False, timeout=10) is not False

    def verify_output_internal_speaker_show_up(self):
        return self.driver.wait_for_object("output_device_internal_speaker", raise_e=False, timeout=10) is not False

    def click_output_internal_speaker(self):
        self.driver.click("output_device_internal_speaker", timeout=10)

    def verify_35mm_headphone_show_on_output_device(self):
        return self.driver.wait_for_object("output_device_3.5mm_headphone_on_DTS", raise_e=False, timeout=10) is not False

    def click_35mm_headphone_on_output_device(self):
        self.driver.click("output_device_3.5mm_headphone_on_DTS", timeout=10)

    def verify_internal_speaker_on_output_device(self):
        return self.driver.wait_for_object("output_device_internal_speaker_on_DTS", raise_e=False, timeout=10) is not False

    def click_internal_speaker_on_output_device(self):
        self.driver.click("output_device_internal_speaker_on_DTS", timeout=10)

    def verify_input_mic_on_quardo_show_up(self):
        return self.driver.wait_for_object("input_mic_on_quardo", raise_e=False, timeout=10) is not False

    def click_input_mic_on_quardo(self):
        self.driver.click("input_mic_on_quardo", timeout=10)

    def verify_output_internal_speaker_on_snowball_show_up(self):
        return self.driver.wait_for_object("output_internal_speaker_on_snowball", raise_e=False, timeout=10) is not False

    def click_output_internal_speaker_on_snowball(self):
        self.driver.click("output_internal_speaker_on_snowball", timeout=10)

    def verify_new_mep_option_on_windows_show_up(self):
        return self.driver.wait_for_object("new_mep_option_on_windows",raise_e=False, timeout=10) is not False

    def click_new_mep_option_on_windows(self):
        self.driver.click("new_mep_option_on_windows", timeout=10)

    def verify_output_device_35mm_headphone_on_snowball_show_up(self):
        return self.driver.wait_for_object("output_device_35mm_headphone_on_snowball", raise_e=False, timeout=10) is not False

    def click_output_device_35mm_headphone_on_snowball(self):
        self.driver.click("output_device_35mm_headphone_on_snowball", timeout=10)

    def verify_output_device_usb_headphone_on_snowball_show_up(self):
        return self.driver.wait_for_object("output_device_usb_headphone_on_snowball", raise_e=False, timeout=10) is not False

    def click_output_device_usb_headphone_on_snowball(self):
        self.driver.click("output_device_usb_headphone_on_snowball", timeout=10)

    def verify_input_device_35mm_headphone_on_snowball_show_up(self):
        return self.driver.wait_for_object("input_device_35mm_headphone_on_snowball", raise_e=False, timeout=10) is not False

    def click_input_device_35mm_headphone_on_snowball(self):
        self.driver.click("input_device_35mm_headphone_on_snowball", timeout=10)
    
    def verify_input_device_usb_headphone_on_snowball_show_up(self):
        return self.driver.wait_for_object("input_device_usb_headphone_on_snowball", raise_e=False, timeout=10) is not False

    def click_input_device_usb_headphone_on_snowball(self):
        self.driver.click("input_device_usb_headphone_on_snowball", timeout=10)

    def verify_output_device_usb_headphone_on_DTS_show_up(self):
        return self.driver.wait_for_object("output_device_usb_headphone_on_DTS", raise_e=False, timeout=10) is not False

    def click_output_device_usb_headphone_on_DTS(self):
        self.driver.click("output_device_usb_headphone_on_DTS", timeout=10)

    def verify_output_combobox_unavailable_show_up(self):
        return self.driver.wait_for_object("output_combobox_unavailable", raise_e=False, timeout=10) is not False
    
    @screenshot_compare(include_param=["machine_name"], root_obj="dts_logo_on_tower", pass_ratio=0.2)
    def wait_and_verify_dts_logo_on_tower(self, machine_name, raise_e=True):
        return self.driver.wait_for_object("dts_logo_on_tower", raise_e=raise_e, timeout=10)
    
    def verify_dts_logo_on_tower_show_up(self):
        return self.driver.wait_for_object("dts_logo_on_tower", raise_e=False, timeout=10) is not False

    def verify_navigate_to_mep_page_all_sounds_devices_show_up(self):
        return self.driver.wait_for_object("navigate_to_mep_page_all_sounds_devices", raise_e=False, timeout=10) is not False

    def click_navigate_to_mep_page_all_sounds_devices(self):
        self.driver.click("navigate_to_mep_page_all_sounds_devices", timeout=10)

    def verify_mic_on_all_sounds_devices_page_show_up(self):
        return self.driver.wait_for_object("mic_on_all_sounds_devices_page", raise_e=False, timeout=10) is not False

    def click_mic_on_all_sounds_devices_page(self):
        self.driver.click("mic_on_all_sounds_devices_page", timeout=10)
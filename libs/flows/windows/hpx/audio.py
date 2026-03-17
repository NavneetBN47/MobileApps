from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.keys import Keys
import time
import logging

class Audio(HPXFlow):
    flow_name = "audio"

    def click_equalizer_toggle(self):
        self.driver.click("preset_toggle")

    def click_preset_movie(self):
        self.driver.click("preset_movie_text")

    def click_preset_music(self):
        self.driver.click("preset_music_text")

    def click_preset_voice(self):
        self.driver.click("voice_preset", timeout = 40)

    def click_immersive_audio_toggle(self):
        self.driver.click("immersive_audio_toggle")

    def click_speaker_swap_toggle(self):
        self.driver.click("speaker_swap_toggle")

    def click_dynamic_audio_toggle(self):
        self.driver.click("dynamic_audio_toggle")

    def click_speaker_swap_tooltip(self):
        self.driver.click("speaker_swap_tooltip")

    def click_equalizer_tooltip(self):
        self.driver.click("sound_tooltip")

    def verify_output_title(self):
        return self.driver.wait_for_object("output_title", timeout=20) is not False

    def verify_output_icon(self):
        return self.driver.wait_for_object("input_mute") is not False
    
    def verify_input_icon(self):
        return self.driver.wait_for_object("output_title") is not False

    def verify_audio_header_displayed(self):
        return self.driver.wait_for_object("audio_header") is not False

    def is_preset_toggle_status_selected(self):
        return self.driver.get_attribute("preset_toggle", "SelectionItem.IsSelected")

    def is_music_status_selected(self):
        return self.driver.get_attribute("preset_music_text", "Toggle.ToggleState", timeout=50)

    def is_movie_status_selected(self):
        return self.driver.get_attribute("preset_movie_text", "Toggle.ToggleState", timeout=50)

    def is_voice_status_selected(self):
        return self.driver.get_attribute("preset_voice_text", "Toggle.ToggleState", timeout=50)
    
    def is_auto_status_selected(self):
        return self.driver.get_attribute("preset_auto_text", "Toggle.ToggleState")

    def verify_speakerswap_toggle_status(self):
        return self.driver.get_attribute("speaker_swap_toggle", "Toggle.ToggleState")
    
    def get_speakerswap_toggle_text(self):
        return self.driver.get_attribute("speaker_swap_tooltip_text", "Name")

    def click_microphone_AI_noise_removal_toggle(self):
        self.driver.click("microphone_noise_removal_btn")

    def verify_microphone_AI_noise_removal_toggle(self):
        return self.driver.get_attribute("microphone_noise_removal_btn", "Toggle.ToggleState")

    def click_noise_removal_toggle(self):
        self.driver.click("noise_removal_btn")
    
    def click_noise_removal_ontoggle(self):
        self.driver.click("noise_removal_btn_on")

    def click_noise_removal_offtoggle(self):
        self.driver.click("noise_removal_btn_off")

    def verify_noise_removal_toggle(self):
        return self.driver.get_attribute("noise_removal_btn", "Toggle.ToggleState")
    
    def wait_noise_removal_toggle_on(self):
        return self.driver.wait_for_object("noise_removal_btn_on", raise_e=False, timeout=10) is not False
    
    def click_noise_reduction_toggle(self):
        self.driver.click("noise_reduction_btn")

    def click_noise_reduction_ontoggle(self):
        self.driver.click("noise_reduction_toggle_on")

    def click_noise_reduction_offtoggle(self):
        self.driver.click("noise_reduction_btn_off")

    def verify_noise_reduction_toggle(self):
        return self.driver.get_attribute("noise_reduction_btn", "Toggle.ToggleState")
    
    def wait_noise_reduction_toggle_on(self):
        return self.driver.wait_for_object("noise_reduction_toggle_on", raise_e=False, timeout=10) is not False
        
    def click_eq_sound_tooltip_icon(self):
        self.driver.click("eq_sound_tootip")

    def get_eq_sound_tooltip_text(self):
        return self.driver.get_attribute("eq_sound_tooltip_message", "Name")

    def get_slider_value(self,slider_name):
        return self.driver.get_attribute(slider_name, "RangeValue.Value", timeout = 10)
           
    def set_slider_value_increase(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            time.sleep(5)
            slider.send_keys(Keys.RIGHT)

    def set_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            time.sleep(5)
            slider.send_keys(Keys.LEFT)

    def set_slider_value(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        width, height = slider.rect["width"], slider.rect["height"]
        self.driver.click_by_coordinates(slider, width * value * 0.01, height * 0.5)

    def set_EQ_slider_value(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        width, height = slider.rect["width"], slider.rect["height"]
        self.driver.click_by_coordinates(slider, width * 0.5, height * value * 0.01)

    def set_equalizer_slider_value_increase(self,value, slider_name):
        slider = self.driver.wait_for_object(slider_name, timeout = 10)
        for _ in range(value):
            slider.send_keys(Keys.UP)
    
    def set_equalizer_slider_value_decrease(self,value, slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.DOWN)

    def get_advanced_slider_value(self,slider_name):
        return self.driver.get_attribute(slider_name, "RangeValue.Value")

    def set_advanced_slider_value(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.UP)

    def verify_noise_removal_show(self):
        return self.driver.wait_for_object("noise_removal_text", raise_e=False) is not False
    
    def verify_noise_eduction_show(self):
        return self.driver.wait_for_object("noise_eduction_text") is not False

    def verify_output_speaker_show(self):
        return self.driver.wait_for_object("output_speaker") is not False
    
    def verify_input_microphone_array_show(self):
        return self.driver.wait_for_object("input_microphone_array") is not False
    
    def verify_mic_mode_text_show(self):
        return self.driver.wait_for_object("mic_mode_text", raise_e=False) is not False

    def verify_conference_text_show(self):
        return self.driver.wait_for_object("conference_text", raise_e=False) is not False
    
    def verify_personal_text_show(self):
        return self.driver.wait_for_object("personal_text", raise_e=False) is not False
    
    def verify_presets_text_show(self):
        return self.driver.wait_for_object("presets_text", raise_e=False, timeout=30) is not False
    
    def verify_movie_checkbox_show(self):
        return self.driver.wait_for_object("preset_movie_text", raise_e=False) is not False
    
    def verify_voice_checkbox_show(self):
        return self.driver.wait_for_object("preset_voice_text", raise_e=False) is not False
    
    def verify_music_checkbox_show(self):
        return self.driver.wait_for_object("preset_music_text", raise_e=False) is not False
    
    def verify_sound_text_show(self):
        return self.driver.wait_for_object("sound_text", raise_e=False) is not False
    
    def verify_sound_tooltips_btn_show(self):
        return self.driver.wait_for_object("sound_tooltips_btn") is not False
    
    def click_sound_tooltips_btn(self):
        self.driver.click("sound_tooltips_btn")
        
    def get_sound_tooltips_text(self):
        return self.driver.get_attribute("sound_tooltips_btn", "Name")
    
    def verify_bass_text_show(self):
        return self.driver.wait_for_object("bass_text", raise_e=False, timeout=10) is not False
    
    def verify_treble_text_show(self):
        return self.driver.wait_for_object("treble_text", raise_e=False) is not False
    
    def verify_width_text_show(self):
        return self.driver.wait_for_object("width_text", raise_e=False) is not False

    def verify_equalizer_text_show(self):
        return self.driver.wait_for_object("equalizer_text", raise_e=False) is not False

    def verify_equalizer_tooltip_icon_show(self):
        return self.driver.wait_for_object("equalizer_tooltip", raise_e=False) is not False

    def verify_equalizer_slider_volume_show(self):
        return self.driver.wait_for_object("equalizer_slider_32volume", raise_e=False) is not False
    
    def click_equalizer_tootip_icon(self):
        self.driver.click("equalizer_tooltip")
    
    def get_equalizer_tootip_txt(self):
        return self.driver.get_attribute("equalizer_tooltip_txt", "Name")
    
    def click_noise_removal_tootip_icon(self):
        self.driver.click("noiseremoval_tooltip")
    
    def get_noise_removal_tootip_txt(self):
        return self.driver.get_attribute("noiseremoval_tooltip", "Name")
    
    def click_noise_reduction_tootip_icon(self):
        self.driver.click("noisereduction_tooltip")
    
    def get_noise_reduction_tootip_txt(self):
        return self.driver.get_attribute("noisereduction_tooltip", "Name")
    
    def click_restore_button(self):
        self.driver.click("restore_defaults_btn")

    def verify_restore_defaults_button_show(self):
        return self.driver.wait_for_object("restore_defaults_btn", raise_e=False, timeout=30)
        
    def verify_restore_defaults_header_show(self):
        return self.driver.wait_for_object("restore_default_dialog_header", raise_e=False, timeout=30)
    
    def verify_restore_defaults_content_1_show(self):
        return self.driver.wait_for_object("restore_default_dialog_content_1", raise_e=False, timeout=30)
    
    def get_restore_defaults_content_1_txt(self):
        return self.driver.get_attribute("restore_default_dialog_content_1", "Name")
    
    def verify_restore_defaults_content_2_show(self):
        return self.driver.wait_for_object("restore_default_dialog_content_2", raise_e=False, timeout=30)
    
    def verify_restore_defaults_content_2_checkbox_show(self):
        return self.driver.wait_for_object("restore_default_dialog_content_2_checkbox", raise_e=False, timeout=30)
    
    def click_restore_defaults_content_2_checkbox(self):
        self.driver.click("restore_default_dialog_content_2_checkbox")
    
    def verify_restore_defaults_cancel_button_show(self):
        return self.driver.wait_for_object("restore_default_dialog_cancel_button", raise_e=False, timeout=30)
    
    def click_cancel_button_on_restore_defaults_dialog(self):
        self.driver.click("restore_default_dialog_cancel_button")
    
    def verify_restore_defaults_x_button_show(self):
        return self.driver.wait_for_object("restore_default_dialog_x_button", raise_e=False, timeout=30)
    
    def click_x_button_on_restore_defaults_dialog(self):
        self.driver.click("restore_default_dialog_x_button")
        
    def click_continue_button(self):
        self.driver.click("continue_button")
        time.sleep(5)
    
    def click_conference_checkbox(self):
        self.driver.click("conference_checkbox")

    def click_personal_checkbox(self):
        self.driver.click("personal_checkbox")
    
    def verify_conference_checkbox_is_selected(self):
        return self.driver.get_attribute("conference_checkbox", "Toggle.ToggleState")
    
    def verify_personal_checkbox_is_selected(self):
        return self.driver.get_attribute("personal_checkbox", "Toggle.ToggleState")

    def verify_home_audio_show(self):
        return self.driver.wait_for_object("home_audio", raise_e=False, timeout=30)

    def verify_audio_show(self):
        return self.driver.wait_for_object("navigate_pc_audio_module_from_pc_device", raise_e=False, timeout=30)
    
    def verify_auto_preset_show(self):
        return self.driver.wait_for_object("preset_auto_text", raise_e=False, timeout=30)

    def verify_auto_preset_selected(self):
        return self.driver.get_attribute("preset_auto_text", "SelectionItem.IsSelected")
    
    def verify_music_preset_selected(self):
        return self.driver.get_attribute("preset_music_text", "SelectionItem.IsSelected")
      
    def click_preset_auto(self):
        self.driver.click("preset_auto_text")

    def click_settings_audio(self):
        self.driver.click("settings_audio")
    
    def verify_immersive_on_settings(self):
        return self.driver.wait_for_object("immersive_on_settings", raise_e=False, timeout=30)
      
    def click_audio_settings_btn(self):
        self.driver.click("audio_settings_button", timeout=10)

    def verify_speak_swap_show(self):
        return self.driver.wait_for_object("speak_swap_title", raise_e=False, timeout=30)

    def verify_speak_swap_btn_status_on(self):
        return self.driver.get_attribute("speak_swap_button_on", "Toggle.ToggleState")

    def verify_speak_swap_btn_on_show(self):
        return self.driver.wait_for_object("speak_swap_button_on", raise_e=False, timeout=30)

    def click_speak_swap_btn_on(self):
        self.driver.click("speak_swap_button_on")

    def verify_speak_swap_btn_status_off(self):
        return self.driver.get_attribute("speak_swap_button_off", "Toggle.ToggleState")

    def click_speak_swap_btn_off(self):
        self.driver.click("speak_swap_button_off")    

    def close_audio_settings(self):
        self.driver.click("audio_settings_close")
    
    def verify_strategy_checkbox_show(self):
        return self.driver.wait_for_object("preset_strategy", raise_e=False, timeout=10) is not False
    
    def verify_rpg_checkbox_show(self):
        return self.driver.wait_for_object("preset_rpg", raise_e=False, timeout=10) is not False
    
    def verify_shooter_checkbox_show(self):
        return self.driver.wait_for_object("audio_shooter", raise_e=False, timeout=10) is not False

    def click_strategy_checkbox(self):
        self.driver.click("preset_strategy")
    
    def click_rpg_checkbox(self):
        self.driver.click("preset_rpg")
    
    def click_shooter_checkbox(self):
        self.driver.click("audio_shooter")

    def is_strategy_status_selected(self):
        return self.driver.get_attribute("preset_strategy", "Toggle.ToggleState")

    def is_rpg_status_selected(self):
        return self.driver.get_attribute("preset_rpg", "Toggle.ToggleState")

    def is_shooter_status_selected(self):
        return self.driver.get_attribute("audio_shooter", "Toggle.ToggleState")

    def turn_on_immersive_audio_toggle(self):
        self.driver.click("immersive_toggle_off")

    def is_immersive_toggle_status_on_status(self):
        return self.driver.get_attribute("immersive_toggle_on", "Toggle.ToggleState")

    def click_close_button_on_settings(self):
        self.driver.click("close_button_on_settings")
       
    def verify_External_Speaker_Settings_text_show(self):
        return self.driver.wait_for_object("external_speaker_settings")

    def verify_Speaker_Configuration_text_show(self):
        return self.driver.wait_for_object("speaker_configuration")

    def verify_Stereo_btn_show(self):
        return self.driver.wait_for_object("stereo_btn")

    def verify_Quad_btn_show(self):
        return self.driver.wait_for_object("quad_btn")
    
    def click_Quad_btn(self):
        self.driver.click("quad_btn")

    def is_Quad_btn_selected(self):
        return self.driver.wait_for_object("quad_btn")

    def verify_5_1_btn_show(self):
        return self.driver.wait_for_object("5.1_btn")

    def verify_Setup_Test_Sound_text_show(self):
        return self.driver.wait_for_object("setup_test_sound")

    def verify_Sound_hide_text_show(self):
        return self.driver.wait_for_object("Sound_hide_text")

    def click_Setup_Test_Sound_hide_caret_custom_icon(self):
        self.driver.click("Sound_hide_caret")

    def verify_Multi_Streaming_text_show(self):
        return self.driver.wait_for_object("Multi-Streaming_text") is not False

    def verify_Play_Test_btn_show(self):
        return self.driver.wait_for_object("Play_Test_btn")

    def verify_Front_Left_checkbox_show(self):
        return self.driver.wait_for_object("Front_Left_checkbox")

    def verify_Front_Left_text_show(self):
        return self.driver.wait_for_object("Front_Left_text")
    
    def verify_Front_Right_checkbox_show(self):
        return self.driver.wait_for_object("Front_Right_checkbox")
    
    def verify_Front_Right_text_show(self):
        return self.driver.wait_for_object("Front_Right_text")
    
    def get_output_text(self):
       return self.driver.wait_for_object("output_title").get_attribute("Name")
       
    def get_noice_removal_text(self):
        return self.driver.wait_for_object("noice_removal_text").get_attribute("Name")
    
    def get_input_text(self):
        return self.driver.wait_for_object("input_title").get_attribute("Name")
    
    def get_noice_reduction_text(self):
        return self.driver.wait_for_object("noice_reduction_text").get_attribute("Name")
    
    def get_mice_mode_text(self):
        return self.driver.wait_for_object("mic_mode_text").get_attribute("Name")
    
    def get_conference_text(self):
        return self.driver.wait_for_object("conference_checkbox").get_attribute("Name")
    
    def get_personal_text(self):
        return self.driver.wait_for_object("personal_checkbox",timeout=30).get_attribute("Name")
    
    def get_preset_text(self):
        return self.driver.wait_for_object("presets_text").get_attribute("Name")
    
    def get_music_text(self):
        return self.driver.wait_for_object("preset_music_text").get_attribute("Name")
    
    def get_voice_text(self):
        return self.driver.wait_for_object("preset_voice_text").get_attribute("Name")
    
    def get_movie_text(self):
        return self.driver.wait_for_object("preset_movie_text").get_attribute("Name")
    
    def get_sound_text(self):
        return self.driver.wait_for_object("sound_text").get_attribute("Name")
    
    def get_bass_text(self):
        return self.driver.wait_for_object("bass_text").get_attribute("Name")
    
    def get_treble_text(self):
        return self.driver.wait_for_object("treble_text").get_attribute("Name")
    
    def get_width_text(self):
        return self.driver.wait_for_object("width_text").get_attribute("Name")
    
    def get_equilizer_text(self):
        return self.driver.wait_for_object("equalizer_text",timeout=10).get_attribute("Name")
    
    def get_external_speaker_setting_text(self):
        return self.driver.wait_for_object("external_speaker_settings").get_attribute("Name")
    
    def get_speaker_config_text(self):
        return self.driver.wait_for_object("speaker_configuration").get_attribute("Name")
    
    def get_stereo_text(self):
        return self.driver.wait_for_object("stereo_text").get_attribute("Name")
    
    def get_setup_test_sound_text(self):
        return self.driver.wait_for_object("setup_test_sound").get_attribute("Name")
    
    def get_sound_calibration_text(self):
        return self.driver.wait_for_object("sound_calibration",timeout=20).get_attribute("Name")
    
    def get_my_profle_text(self):
        return self.driver.wait_for_object("my_Profile_text").get_attribute("Name")
    
    def get_notify_text(self):
        return self.driver.wait_for_object("notify_text").get_attribute("Name")
    
    def get_intensity_text(self):
        return self.driver.wait_for_object("intensity_text").get_attribute("Name")
    
    def get_sound_test_text(self):
        return self.driver.wait_for_object("sound_test_text").get_attribute("Name")
    
    def get_profile_output_text(self):
        return self.driver.wait_for_object("output_text").get_attribute("Name")
    
    def get_balance_text(self):
        return self.driver.wait_for_object("balance_text").get_attribute("Name")
    
    def get_min_text(self):
        return self.driver.wait_for_object("min_text").get_attribute("Name")
    
    def get_max_text(self):
        return self.driver.wait_for_object("max_text").get_attribute("Name")
    
    def get_left_text(self):
        return self.driver.wait_for_object("left_text").get_attribute("Name")
    
    def get_right_text(self):
        return self.driver.wait_for_object("right_text").get_attribute("Name")
    
    def get_reset_text(self):
        return self.driver.wait_for_object("reset_btn").get_attribute("Name")
    
    def get_customize_manually_text(self):
        return self.driver.wait_for_object("customize_manually_btn").get_attribute("Name")
    
    def get_start_test_text(self):
        return self.driver.wait_for_object("start_test_btn").get_attribute("Name")

    def verify_Sound_hide_text_show(self):
        return self.driver.wait_for_object("Sound_hide_text")
    
    def click_Setup_Test_Sound_hide_caret_custom_icon(self):
        self.driver.click("Sound_hide_caret")

    def verify_switchSetMultiStreamOn_toggle_show(self):
         return self.driver.wait_for_object("switchSetMultiStreamOn", timeout = 10)
    
    def click_switchSetMultiStreamOn_toggle(self):
         self.driver.click("switchSetMultiStreamOn")

    def verify_Sound_hide_text_show(self):
        return self.driver.wait_for_object("Sound_hide_text")
    
    def click_Setup_Test_Sound_hide_caret_custom_icon(self):
        self.driver.click("Sound_hide_caret", timeout = 10)

    def verify_switchSetMultiStreamOff_toggle_show(self):
         return self.driver.wait_for_object("switchSetMultiStreamOff")

    def click_switchSetMultiStreamOff_toggle(self):
         self.driver.click("switchSetMultiStreamOff")

    def get_external_speaker_setting_text(self):
        return self.driver.wait_for_object("external_speaker_settings").get_attribute("Name")
    
    def get_stereo_text(self):
        return self.driver.wait_for_object("stereo_btn").get_attribute("Name")

    def click_Front_left_ft_combobox(self):
        self.driver.click("Front_left_ft_combobox")

    def click_Front_left_db_combobox(self):
        self.driver.click("Front_left_db_combobox")

    def is_Front_left_checkbox_selected(self):
        return self.driver.get_attribute("Front_left_checkbox", "Toggle.ToggleState")

    def is_Front_right_checkbox_selected(self):
        return self.driver.get_attribute("Front_right_checkbox", "Toggle.ToggleState")

    def is_Back_left_checkbox_selected(self):
        return self.driver.get_attribute("Back_left_checkbox", "Toggle.ToggleState")

    def is_Back_right_checkbox_selected(self):
        return self.driver.get_attribute("Back_right_checkbox", "Toggle.ToggleState")
    
    def click_Front_left_checkbox(self):
        self.driver.click("Front_left_checkbox")

    def click_Front_right_checkbox(self):
        self.driver.click("Front_right_checkbox")

    def click_Back_left_checkbox(self):
        self.driver.click("Back_left_checkbox")

    def click_Back_right_checkbox(self):
        self.driver.click("Back_right_checkbox")

    def click_Front_left_ft_dropdown(self):
        self.driver.click("Front_left_ft_dropdown")

    def click_Front_right_db_dropdown(self):
        self.driver.click("Front_left_db_dropdown")

    def click_Front_left_ft_30(self):
        self.driver.click("Front_left_ft_30")

    def click_Front_left_db_1(self):
        self.driver.click("Front_left_db_1")

    def verify_movie_preset(self):
        return self.driver.wait_for_object("preset_movie_text", raise_e=False, timeout=10)

    def verify_auto_preset(self):
        return self.driver.wait_for_object("auto_preset_text", raise_e=False, timeout=10)

    def get_auto_text(self):
        return self.driver.wait_for_object("preset_auto_text").get_attribute("Name")
    
    def get_restore_button_text(self):
        return self.driver.wait_for_object("restore_defaults_btn").get_attribute("Name")
    
    def verify_restore_button_text(self):
        return self.driver.wait_for_object("restore_defaults_btn", raise_e=False, timeout=2)
    
    def search_text(self,element,direction="down"):
        max_time=20
        for time in range(0,max_time) :
            if(self.driver.wait_for_object(element,invisible=False,raise_e=False)):
                break
            else:
                self.driver.swipe(direction=direction)
                continue
    
    def get_settings_text(self):
        return self.driver.wait_for_object("audio_setting_text").get_attribute("Name")
    
    def get_general_features_text(self):
        return self.driver.wait_for_object("general_features_text").get_attribute("Name")
    
    def get_immersive_audio_text(self):
        return self.driver.wait_for_object("immersive_audio_text").get_attribute("Name")
    
    def get_speaker_swap_text(self):
        return self.driver.wait_for_object("speaker_swap_text").get_attribute("Name")
    
    def get_quad_text(self):
        return self.driver.wait_for_object("quad_btn").get_attribute("Name")

    def get_fiftyone_text(self):
        return self.driver.wait_for_object("5.1_btn").get_attribute("Name")
    
    def click_setup_and_test_soundhide_caret(self):
        self.driver.click("to_expand_caret",timeout=60)

    def click_stereo_tab(self):
        self.driver.click("stereo_btn")

    def click_quad_tab(self):
        self.driver.click("quad_btn")

    def click_fifty_one_tab(self):
        self.driver.click("5.1_btn")

    def get_multistreaming_text(self):
        return self.driver.wait_for_object("multi_streaming_text",timeout=30).get_attribute("Name")
    
    def get_play_test_text(self):
        return self.driver.wait_for_object("Play_Test_btn").get_attribute("Name")
    
    def get_front_left_text(self):
        return self.driver.wait_for_object("Front_Left_text").get_attribute("Name")
    
    def get_front_right_text(self):
        return self.driver.wait_for_object("Front_Right_text").get_attribute("Name")
    
    def get_back_right_text(self):
        return self.driver.wait_for_object("back_right_text").get_attribute("Name")
    
    def get_back_left_text(self):
        return self.driver.wait_for_object("back_left_text").get_attribute("Name")
    
    def get_subwoofer_text(self):
        return self.driver.wait_for_object("subwoofer_text").get_attribute("Name")
    
    def get_center_text(self):
        return self.driver.wait_for_object("center_text").get_attribute("Name")
    
    def click_to_expand_caret(self):
        max_time=20
        for time in range(0,max_time) :
            if(self.driver.wait_for_object("to_collapse_caret",invisible=False,raise_e=False)):
                break
            else:
                self.driver.click("to_expand_caret",timeout=60)
                break

    def click_to_collapse_caret(self):
        self.driver.click("to_collapse_caret",timeout=60)

    def get_settings_text_with_id(self):
        return self.driver.wait_for_object("audio_setting_text_id").get_attribute("Name")
    
    def get_general_features_text_with_id(self):
        return self.driver.wait_for_object("general_features_text_id").get_attribute("Name")
    
    def get_immersive_audio_text_with_id(self):
        return self.driver.wait_for_object("immersive_audio_text_id").get_attribute("Name")
    
    def get_speaker_swap_text_with_id(self):
        return self.driver.wait_for_object("speaker_swap_text_id").get_attribute("Name")
    
    def get_music_text_with_id(self):
        return self.driver.wait_for_object("preset_music_text",timeout=30).get_attribute("Name")
    
    def get_voice_text_with_id(self):
        return self.driver.wait_for_object("preset_voice_text",timeout=30).get_attribute("Name")
    
    def get_movie_text_with_id(self):
        return self.driver.wait_for_object("preset_movie_text",timeout=30).get_attribute("Name")
    
    def get_auto_text_with_id(self):
        return self.driver.wait_for_object("preset_auto_text",timeout=30).get_attribute("Name")
    
    def get_noise_removal_tool_tip_text(self):
        return self.driver.wait_for_object("noise_removal_tool_tip_text",timeout=30).get_attribute("Name")
    
    def get_noise_reduction_tooltip_text(self):
        return self.driver.wait_for_object("noise_reduction_tooltip_text",timeout=30).get_attribute("Name")
    
    def get_preset_tooltip_text(self):
        return self.driver.wait_for_object("preset_tooltip_text",timeout=30).get_attribute("Name")
    
    def verify_presets_tooltips_btn_show(self):
        return self.driver.wait_for_object("preset_tooltip_text") is not False
    
    def get_basic_eq_tooltip_text(self):
        return self.driver.wait_for_object("basic_eq_tooltip_text",timeout=30).get_attribute("Name")
    
    def get_band_eq_tooltip_text(self):
        return self.driver.wait_for_object("band_eq_tooltip_text",timeout=30).get_attribute("Name")
    
    def click_noise_removal_tool_tip(self):
        self.driver.click("noise_removal_tool_tip_text")
    
    def click_noise_reduction_tooltip(self):
        self.driver.click("noise_reduction_tooltip_text")
    
    def click_preset_tooltip(self):
        self.driver.click("preset_tooltip_text")
    
    def click_basic_eq_tooltip(self):
        self.driver.click("basic_eq_tooltip_text")
    
    def click_band_eq_tooltip(self):
        self.driver.click("band_eq_tooltip_text")

    def click_preset_movie_button(self):
        self.driver.click("preset_movie_text")
    
    def verify_preset_music_show(self):
        return self.driver.wait_for_object("preset_music_text",raise_e=False, timeout=2)
    
    def verify_bass_slider_show(self):
        return self.driver.wait_for_object("bass_slider",raise_e=False, timeout=2)
    
    def verify_trible_slider_show(self):
        return self.driver.wait_for_object("treble_slider",raise_e=False, timeout=2)
    
    def verify_width_slider_show(self):
        return self.driver.wait_for_object("width_slider",raise_e=False, timeout=2)
    
    def click_windows_speaker_icon(self):
        self.driver.click("windows_speaker_icon")
        return self.driver.get_attribute("windows_speaker_icon","Name")

    def verify_width_slider_show(self):
        return self.driver.wait_for_object("width_slider",raise_e=False, timeout=2)
    
    def verify_audio_control_module_on_pcdevice_page(self):
        return self.driver.get_attribute("navigate_pc_audio_module_from_pc_device","Name")
    
    def click_to_pc_audio_from_pc_device(self):
        self.driver.click("navigate_pc_audio_module_from_pc_device")

    def get_system_volume(self):
        return self.driver.get_attribute("windows_speaker_volume_tray","RangeValue.Value")
    
    def set_system_tray_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.LEFT)

    def click_windows_system_sound_tab(self):
        self.driver.click("windows_system_sound_tab")

    def click_windows_system_sound_more_sound_settings_tab(self):
        self.driver.click("windows_system_sound_more_sound_settings_tab")

    def click_system_sound_recording_tab(self):
        self.driver.click("system_sound_recording_tab")

    def click_sound_microphone_array_tab(self):
        self.driver.click("sound_microphone_array_tab")

    def click_sound_microphone_array_properties_tab(self):
        self.driver.click("sound_microphone_array_properties_tab")

    def click_sound_microphone_array_properties_levels_tab(self):
        self.driver.click("sound_microphone_array_properties_levels_tab")

    def set_system_sound_microphone_value_decrease(self,value):
        slider = self.driver.wait_for_object("sound_microphone_array_properties_levels_arrow_tab")
        for _ in range(value):
            slider.send_keys(Keys.LEFT)
        return self.driver.get_attribute("system_microphone_slider_level_value","Name")

    def set_windows_system_sound_input_volume_tab_decrease(self,value):
        self.driver.swipe(direction="down", distance=1)
        slider = self.driver.wait_for_object("windows_system_sound_input_volume_tab")
        for _ in range(value):
            slider.send_keys(Keys.LEFT)
        return self.driver.get_attribute("windows_system_sound_input_volume_tab","RangeValue.Value")
    
    def click_on_system_settings_maximize_button(self):
        self.driver.click("maximize_system_settings")

    def verify_system_settings_window_maximize(self):
        return self.driver.get_attribute("maximize_system_settings","Name")

    def click_close_microphone_array_properties_window(self):
        self.driver.click("close_microphone_array_properties_window") 

    def click_close_sound_window(self):
        self.driver.click("close_sound_window")

    def click_close_system_settings_window(self):
        self.driver.click("close_settings_window", timeout = 20)

    def click_mute_button_on_input_slider(self):
        self.driver.click("system_mute_button_on_input_slider")

    def click_mute_unmute_input_mic_button(self):
        self.driver.click("input_mute", timeout = 30)

    def get_mute_unmute_status_on_input_mic(self):
        return self.driver.get_attribute("input_mute","Name", timeout = 30)
        
    def get_unmute_button_on_input_slider(self):
        return self.driver.get_attribute("system_unmute_button_on_input_slider","Name")
    
    def click_unmute_button_on_input_slider(self):
        self.driver.click("system_unmute_button_on_input_slider")
         
    def get_mute_button_on_input_slider(self):
        return self.driver.get_attribute("system_mute_button_on_input_slider","Name")

    def click_output_mute_button(self):
        self.driver.click("output_mute")

    def get_output_mute_button_name(self):
        return self.driver.get_attribute("output_mute","Name")
    
    def click_input_mute_button(self):
        self.driver.click("input_mute")

    def get_input_mute_button_name(self):
        return self.driver.get_attribute("input_mute","Name")
    
    def click_app_mute_button_on_input_slider(self):
        self.driver.click("mute_button_on_input_slider_app")
        
    def get_app_unmute_button_on_input_slider(self):
        return self.driver.get_attribute("mute_button_on_input_slider_app","Name")
    
    def click_output_device_speaker(self):
        self.driver.click("speaker_device")
        
    def select_headphone_input_device(self):
        self.driver.click("3.5mm_headphone_input_device")
        
    def select_usb_headphone_output_device(self):
        self.driver.click("usb_headphone_output_device")

    def verify_standalone_app_header_show(self):
        return self.driver.wait_for_object("standalone_app_header",raise_e=False, timeout = 30)
    
    def verify_standalone_app_contents_one_show(self):
        return self.driver.wait_for_object("standalone_app_contents_one") is not False
    
    def verify_standalone_app_contents_two_title_show(self):
        return self.driver.wait_for_object("standalone_app_contents_two_title") is not False
    
    def verify_standalone_app_contents_two_text1_show(self):
        return self.driver.wait_for_object("standalone_app_contents_two_text1") is not False
    
    def verify_standalone_app_contents_two_text2_show(self):
        return self.driver.wait_for_object("standalone_app_contents_two_text2") is not False
    
    def verify_standalone_app_contents_two_text3_show(self):
        return self.driver.wait_for_object("standalone_app_contents_two_text3") is not False
    
    def verify_open_myhp_show(self):
        return self.driver.wait_for_object("open_myHP_button") is not False
    
    def verify_not_now_show(self):
        return self.driver.wait_for_object("not_now_button", timeout = 30)
    
    def click_standalone_app_close_button(self):
        self.driver.click("standalone_app_close_button", timeout = 20)
        
    def click_not_now_button(self):
        self.driver.click("not_now_button", timeout = 30)
        
    def launch_standalone_app(self, Audio):
        self.driver.click("search_bar_on_windows")
        time.sleep(3)
        self.driver.send_keys("search_bar_on_windows", Audio)
        time.sleep(5)
        self.driver.wait_for_object("search_bar_on_windows", displayed=False, timeout=10)
        self.driver.click("privacy_settings_open_button", timeout = 20)
        
    
    def press_down_arrow_key(self, locator):
        self.driver.send_keys(locator, Keys.DOWN)
        el = self.driver.wait_for_object(locator, displayed=False, timeout=3)
        el.send_keys(Keys.ENTER)
        
    
    def launch_IMAX_apps(self, IMAX):
        self.driver.click("search_bar_on_windows")
        time.sleep(3)
        self.driver.send_keys("search_bar_on_windows", IMAX)
        time.sleep(5)
        el = self.driver.wait_for_object("search_bar_on_windows", displayed=False, timeout=10)
        el.send_keys(Keys.ENTER)
        time.sleep(5)
        el.send_keys(Keys.ENTER)    
    
    def launch_common_apps(self, commonapps):
        self.driver.click("search_bar_on_windows", timeout = 20)
        time.sleep(3)
        self.driver.send_keys("search_bar_on_windows", commonapps)
        time.sleep(5)
        el = self.driver.wait_for_object("search_bar_on_windows", displayed=False, timeout=10)
        el.send_keys(Keys.ENTER)
        time.sleep(5)
        el.send_keys(Keys.ENTER)     
        
    def verify_hp_privacy_settings_exist_on_windows(self):
        return self.driver.wait_for_object("privacy_settings_open_button",invisible=False,raise_e=False)        
        
    def search_hp_privacy_settings(self, privacy):
        self.driver.click("search_bar_on_windows")
        time.sleep(3)
        self.driver.send_keys("search_bar_on_windows", privacy)
        time.sleep(2)    
        
    def click_on_dropdown(self,locator):
        self.driver.click(locator)
              
    def click_subwoofer_db_value_from_dropdown(self):
        self.driver.click("subwoofer_db_dropdown_item")
       
    def click_center_db_value_from_dropdown(self):
        self.driver.click("center_db_dropdown_item")

    def click_front_left_db_value_from_dropdown(self):
        self.driver.click("leftNextSelect_db_dropdown_item",timeout=5)

    def click_front_right_db_value_from_dropdown(self):
        self.driver.click("rightNextSelect_db_dropdown_item",timeout=5)

    def click_bottom_left_db_value_from_dropdown(self):
        self.driver.click("leftBottomNextSelect_db_dropdown_item",timeout=5)

    def click_bottom_right_db_value_from_dropdown(self):
        self.driver.click("rightBottomNextSelect_db_dropdown_item",timeout=5)

    def click_center_ft_value_from_dropdown(self):
        self.driver.click("center_ft_dropdown_item")

    def click_front_left_ft_value_from_dropdown(self):
        self.driver.click("leftSelect_ft_dropdown_item")

    def click_front_right_ft_value_from_dropdown(self):
        self.driver.click("rightSelect_ft_dropdown_item")

    def click_bottom_left_ft_value_from_dropdown(self):
        self.driver.click("leftBottomSelect_ft_dropdown_item")

    def click_bottom_right_ft_value_from_dropdown(self) :
        self.driver.click("rightBottomSelect_ft_dropdown_item")

    def click_speaker_tab(self):
        self.driver.click("speaker_device")

    def verify_subwoofer_db_value(self):
        return self.driver.get_attribute("subwoofer_db_dropdown", "Name")

    def verify_center_db_value(self):
        return self.driver.get_attribute("center_db_dropdown", "Name")

    def verify_front_left_db_value(self):
        return self.driver.get_attribute("Front_left_db_dropdown", "Name")

    def verify_front_right_db_value(self):
        return self.driver.get_attribute("rightNextSelect_db_dropdown", "Name")

    def verify_bottom_left_db_value(self):
        return self.driver.get_attribute("leftBottomNextSelect_db_dropdown", "Name")
    
    def verify_bottom_right_db_value(self):
        return self.driver.get_attribute("rightBottomNextSelect_db_dropdown", "Name")
    
    def verify_center_ft_value(self):
        return self.driver.get_attribute("center_ft_dropdown", "Name")
    
    def verify_front_left_ft_value(self):
        return self.driver.get_attribute("Front_left_ft_dropdown", "Name")
    
    def verify_front_right_ft_value(self):
        return self.driver.get_attribute("rightSelect_ft_dropdown", "Name")
    
    def verify_bottom_left_ft_value(self):
        return self.driver.get_attribute("leftBottomSelect_ft_dropdown", "Name")
    
    def verify_bottom_right_ft_value(self):
        return self.driver.get_attribute("rightBottomSelect_ft_dropdown", "Name")
    
    def open_windows_camera(self):
        self.driver.ssh.send_command('powershell start microsoft.windows.camera:')

    def close_windows_camera(self):
        if "WindowsCamera.exe" in self.driver.ssh.send_command("tasklist.exe")["stdout"]:
            self.driver.ssh.send_command('powershell taskkill /im WindowsCamera.exe /t /f')
            
    def get_adaptive_audio_text(self):
        return self.driver.get_attribute("adaptive_audio_text", "Name")
    
    def get_adaptive_audio_auto_radio_button_text(self):
        return self.driver.get_attribute("adaptive_audio_auto_radio_button", "Name")
    
    def click_adaptive_audio_auto_tooltip_text(self):
        self.driver.click("adaptive_audio_auto_tooltip")
    
    def get_adaptive_audio_auto_tooltip_text(self):
        return self.driver.get_attribute("adaptive_audio_auto_tooltip", "Name")
    
    def click_adaptive_audio_toggle_button(self):
        self.driver.click("adaptive_audio_toggle_switch_on", timeout = 20)

    def get_adaptive_audio_toggle_button_state(self):
        return self.driver.get_attribute("adaptive_audio_toggle_switch_on","Toggle.ToggleState")
    
    def get_adaptive_audio_far_from_display_radio_button_text(self):
        return self.driver.get_attribute("adaptive_audio_far_from_display", "Name")
    
    def get_adaptive_audio_far_from_display_radio_button_status(self):
        return self.driver.get_attribute("adaptive_audio_far_from_display", "Toggle.ToggleState")
    
    def get_adaptive_audio_auto_radio_button_status(self):
        return self.driver.get_attribute("adaptive_audio_auto_radio_button", "Toggle.ToggleState")

    def get_adaptive_audio_near_to_display_radio_button_text(self):
        return self.driver.get_attribute("adaptive_audio_near_to_display", "Name")

    def click_near_to_display_radio_button(self):
        self.driver.click("adaptive_audio_near_to_display")
 
    def get_near_to_display_radio_button_state(self):
        return self.driver.get_attribute("adaptive_audio_near_to_display","Toggle.ToggleState")

    def get_music_default_state(self):
        return self.driver.get_attribute("preset_music_text","Toggle.ToggleState")
    
    def get_adaptive_audio_auto_radio_button(self):
        auto_radio_button = self.driver.find_object("adaptive_audio_auto_radio_button")
        if auto_radio_button.is_enabled():
            return True
        else:
            return False
        
    def get_adaptive_audio_far_from_display_radio_button(self):
        auto_radio_button = self.driver.find_object("adaptive_audio_far_from_display")
        if auto_radio_button.is_enabled():
            return True
        else:
            return False 

    def get_adaptive_audio_near_to_display_radio_button(self):
        auto_radio_button = self.driver.find_object("adaptive_audio_near_to_display")
        if auto_radio_button.is_enabled():
            return True
        else:
            return False
        
    def click_manage_camera_tab(self) :
        self.driver.click("system__manage_camera_tab") 

    def expand_manage_camera_disable_tab(self) :
        logging.info("manage camera disable tab")
        if self.driver.wait_for_object("system_manage_camera_enable_tab", raise_e=False, timeout=5) is False:
            logging.info("click manage camera disable tab")
            self.click_manage_camera_tab() 
        else:
            logging.info("click manage camera enable tab")
            self.driver.click("system_manage_camera_enable_tab")
            self.click_manage_camera_tab()

    def click_manage_camera_disable_button(self) :
        self.driver.click("system__manage_camera_disable_tab")

    def click_yes_option_to_disable(self) :
        self.driver.click("system__manage_camera_disable_tab")

    def click_manage_camera_enable_tab(self) :
        self.driver.click("system_manage_camera_enable_tab")

    def click_settings_tab_on_camera(self) :
        self.driver.click("system_camera_settings_button")

    def click_camera_settings_dropdown_on_settings(self) :
        self.driver.click("camera_settings_dropdown")

    def click_open_camera_system_settings(self) :
        self.driver.click("open_camera_system_settings")

    def click_yes_to_open_camera_system_settings(self) :
        self.driver.click("yes_button_to_open_camera_system_settings")

    def click_open_camera_system_settings_window(self) :
        self.driver.click("manage_camera_settings_window")

    def click_to_open_my_hp_window(self) :
        self.driver.click("my_hp_window")

    def click_to_open_my_hp_button(self) :
        self.driver.click("open_myHP_button")

    def get_standalone_app_header_text(self):
        return self.driver.get_attribute("standalone_app_header","Name")

    def verify_home_audio_control(self):
        return self.driver.get_attribute("audio_control_header_on_home_page","Name")
    
    def verify_pc_device_page_and_audio_control(self):
        return self.driver.get_attribute("pc_device_page_and_audio_control","Name")
    
    def verify_home_page_and_audio_control(self):
        return self.driver.get_attribute("home_page_and_audio_control","Name")
    
    def verify_pc_device_audio_control(self):
        return self.driver.get_attribute("audio_control_page_from_pc_device","Name")
    
    def click_headset_tab(self):
        self.driver.click("headset_device")

    def click_output_speaker_radio_button(self):
        self.driver.click("audio_control_speaker_default_output_radio_button")

    def click_output_headset_earphone_radio_button(self):
        self.driver.click("audio_control_headset_earphone_default_radio_button")

    def click_audio_control_restore_button(self):
        self.driver.click("audio_control_restore_button")

    def get_headset_tab(self):
        return self.driver.get_attribute("headset_device", "Name")
 
    def set_equalizer_slider_value(self, value, slider_name):
        slider = self.driver.wait_for_object(slider_name)
        height, width  = slider.rect["height"], slider.rect["width"]
        self.driver.click_by_coordinates(slider, height * value * 0.01, width * 0.5)

    def click_equalizer_32slider(self):
        self.driver.click("equalizer_slider_32volume")

    def click_equalizer_64slider(self):
        self.driver.click("equalizer_slider_64volume")

    def click_equalizer_125slider(self):
        self.driver.click("equalizer_slider_125volume")

    def click_equalizer_250slider(self):
        self.driver.click("equalizer_slider_250volume")

    def click_equalizer_500slider(self):
        self.driver.click("equalizer_slider_500volume")

    def click_equalizer_1kslider(self):
        self.driver.click("equalizer_slider_1kvolume")

    def click_equalizer_2kslider(self):
        self.driver.click("equalizer_slider_2kvolume")

    def click_equalizer_4kslider(self):
        self.driver.click("equalizer_slider_4kvolume")

    def click_equalizer_8kslider(self):
        self.driver.click("equalizer_slider_8kvolume")

    def click_equalizer_16kslider(self):
        self.driver.click("equalizer_slider_16kvolume")

    def click_auto_radio_button(self):
        self.driver.click("adaptive_audio_auto_radio_button")

    def click_far_from_display_radio_button(self):
        self.driver.click("adaptive_audio_far_from_display")

    def click_near_to_display_radio_button(self):
        self.driver.click("adaptive_audio_near_to_display")
    
    def select_microphone_usb_audio_external_device(self):
        self.driver.click("microphone_usb_audio_external_input_device", timeout = 40)

    def click_input_mic_icon_input_device(self):
        self.driver.click("internal_microphone_input_device")

    def is_input_mic_input_device_selected(self):
        return self.driver.get_attribute("internal_microphone_input_device", "Toggle.ToggleState")

    def verify_noise_removal_toggle_off(self):
        return self.driver.get_attribute("noise_removal_toggle_off","Toggle.ToggleState")
    
    def verify_noise_reduction_toggle_on_state(self):
        return self.driver.get_attribute("noise_reduction_toggle_on","Toggle.ToggleState")
    
    def click_noise_removal_toggle_to_on(self):
        self.driver.click("noise_removal_toggle_off")
    
    def click_noise_reduction_toggle_to_off(self):
        self.driver.click("noise_reduction_toggle_on")
    
    def hover_noise_removal_tool_tip(self):
        self.driver.click("noise_removal_tool_tip", timeout = 10)
    
    def get_noise_removal_tool_tip(self):
        return self.driver.get_attribute("noise_removal_tool_tip","Name")
    
    def hover_noise_reduction_tool_tip(self):
        self.driver.click("noise_reduction_tool_tip", timeout = 10)
    
    def get_noise_reduction_tool_tip(self):
        return self.driver.get_attribute("noise_reduction_tool_tip","Name")
    
    def verify_noise_removal_toggle_on_state(self):
        return self.driver.get_attribute("noise_removal_toggle_on","Toggle.ToggleState")
    
    def click_noise_removal_toggle_to_off(self):
        self.driver.click("noise_removal_toggle_on")
    
    def verify_noise_reduction_toggle_off(self):
        return self.driver.get_attribute("noise_reduction_btn_off","Toggle.ToggleState")
    
    def verify_usb_headset_input_device(self):
        return self.driver.wait_for_object("usb_headset_input_device",invisible=False,raise_e=False) is not False
    
    def select_usb_headset_input_device(self):
        self.driver.click("usb_headset_input_device")
    
    def get_windows_system_sound_input_volume_tab(self):
        return self.driver.get_attribute("windows_system_sound_input_volume_tab","RangeValue.Value")
    
    def verify_3_5mm_headphone_input_device(self):
        return self.driver.wait_for_object("3.5mm_headphone_input_device",raise_e=False, timeout=20)
    
    def click_play_test_button(self):
        self.driver.click("Play_Test_btn")
    
    def verify_settings_btn_show(self):
        return self.driver.wait_for_object("settings_audio", raise_e=False, timeout=20)
    
    def verify_studio_recording_show(self):
        return self.driver.wait_for_object("studio_recording_text", raise_e=False, timeout=10)
    
    def verify_studio_recording_checkbox_show(self):
        return self.driver.wait_for_object("studio_recording_checkbox", raise_e=False, timeout=10)
    
    def click_studio_recording_btn(self):
        self.driver.click("studio_recording_checkbox")
    
    def get_studio_recording_text(self):
        return self.driver.get_attribute("studio_recording_text","Name", raise_e=False, timeout=10)
    
    def select_studio_recording(self):
        self.driver.click("studio_recording_checkbox")

    def is_studio_recording_btn_selected(self):
        return self.driver.get_attribute("studio_recording_checkbox", "Toggle.ToggleState")
    
    def check_noise_reduction_btn_status(self):
        noise_reduction_toggle_status = self.driver.wait_for_object("noise_reduction_toggle_on")
        noise_reduction_toggle_status.is_enabled()
        
    def verify_context_aware_show(self):
        return self.driver.wait_for_object("add_Application_button", raise_e=False, timeout=10)
    
    def verify_all_application_icon_show(self):
        return self.driver.wait_for_object("all_Application_icon", raise_e=False, timeout=10)
    
    def click_all_application_icon(self):
        self.driver.click("all_Application_icon")
    
    def click_add_application_btn(self):
        self.driver.click("add_Application_button")
        
    def verify_application_page_header_pop_up(self):
        return self.driver.wait_for_object("Application_page_header", raise_e=False, timeout=10)
    
    def verify_search_bar_show(self):
        return self.driver.wait_for_object("search_frame_on_application_page", raise_e=False, timeout=10)
    
    def click_search_bar_on_application_page(self):
        self.driver.click("search_frame_on_application_page")
    
    def verify_application_page_list(self):
        return self.driver.wait_for_object("application_items_on_application_page", raise_e=False, timeout=10)
    
    def verify_access_app_show(self):
        return self.driver.wait_for_object("access_app_under_application_items", raise_e=False, timeout=10)
    
    def verify_cancel_button_on_application_page_show(self):
        return self.driver.wait_for_object("cancel_button_on_application_page", raise_e=False, timeout=10)
    
    def click_cancel_button_on_application_page(self):
        self.driver.click("cancel_button_on_application_page")
    
    def verify_add_button_on_application_page_show(self):
        return self.driver.wait_for_object("add_button_on_application_page_disabled", raise_e=False, timeout=10)
    
    def click_access_app_under_application_items(self):
        self.driver.click("access_app_under_application_items")
        
    def click_calculator_app_under_application_items(self):
        self.driver.click("calculator_under_application_items")
        
    def verify_calculator_app_under_application_items(self):
        return self.driver.wait_for_object("calculator_under_application_items", raise_e=False, timeout=10)
        
    def verify_calendar_app_under_application_items(self):
        return self.driver.wait_for_object("calendar_under_application_items", raise_e=False, timeout=10)
    
    def click_add_button_on_application_page(self):
        self.driver.click("add_button_on_application_page")
        
    def verify_add_button_enabled_on_application_page(self):
        return self.driver.wait_for_object("add_button_on_application_page").is_enabled()
        
    def verify_access_app_show_on_application_list(self):
        return self.driver.wait_for_object("added_app_on_application_list", raise_e=False, timeout=10)
    
    def verify_calculator_app_show_on_application_list(self):
        return self.driver.wait_for_object("calculator_on_application_list", raise_e=False, timeout=10)
        
    def hover_on_access_app(self):
        self.driver.click("added_app_on_application_list", timeout = 10)
        
    def click_access_app_on_application_list(self):
        self.driver.click("added_app_on_application_list")
        
    def verify_delete_btn_show_on_access_app(self):
        return self.driver.wait_for_object("delete_button_on_apps", raise_e=False, timeout=10)
    
    def click_myhp_on_task_bar(self):
        if(self.driver.wait_for_object("myhp_on_task_bar", raise_e=False, timeout=10) is True):
            self.driver.click("myhp_on_task_bar", timeout= 20)
        
    def click_tencent_on_task_bar(self):
        self.driver.click("tencent_on_task_bar", timeout= 10)
        
    def click_aiqiyi_on_task_bar(self):
        self.driver.click("aiqiyi_on_task_bar")
        
    def click_delete_btn_on_access_app(self):
        self.driver.click("delete_button_on_apps")
        
    def verify_delete_page_header_show(self):
        return self.driver.wait_for_object("delete_dialog_header", raise_e=False, timeout=10)
    
    def verify_delete_page_description_show(self):
        return self.driver.wait_for_object("delete_dialog_description", raise_e=False, timeout=10)
    
    def verify_delete_page_cancel_btn_show(self):
        return self.driver.wait_for_object("cancel_button_on_delete_dialog", raise_e=False, timeout=10)
    
    def verify_delete_page_continue_btn_show(self):
        return self.driver.wait_for_object("continue_button_on_delete_dialog", raise_e=False, timeout=10)
    
    def click_cancel_btn_on_delete_page(self):
        self.driver.click("cancel_button_on_delete_dialog")
        
    def click_continue_btn_on_delete_page(self):
        self.driver.click("continue_button_on_delete_dialog")
          
    def click_hp_privacy_settings_app_under_application_items(self):
        self.driver.click("hp_privacy_settings_app_under_application_items")
       
    def verify_hp_privacy_settings_show_on_application_list(self):
        return self.driver.wait_for_object("hp_privacy_settings_app_on_application_list", raise_e=False, timeout=10)
        
    def click_clock_app_under_application_items(self):
        self.driver.click("clock_under_application_items")
        
    def click_camera_app_under_application_items(self):
        self.driver.click("camera_under_application_items")
        
    def click_myhp_app_under_application_items(self):
        self.driver.click("myhp_under_application_items")
        
    def click_hpSmart_app_under_application_items(self):
        self.driver.click("hpSmart_under_application_items")
    
    def click_application_under_application_items(self):
        self.driver.click("application_items_on_application_page")
        
    def verify_hp_privacy_settings_app_under_application_page(self):
        return self.driver.wait_for_object("application_items_on_application_page", raise_e=False, timeout=10)
        
    def click_left_arrow_on_application_list(self):
        self.driver.click("left_arrow_on_application_list")
        
    def click_right_arrow_on_application_list(self):
        self.driver.click("right_arrow_on_application_list")
        
    def verify_left_arrow_on_application_list_show(self):
        return self.driver.wait_for_object("left_arrow_on_application_list", raise_e=False, timeout=10)

    def input_search_bar_on_application_page(self, text):
        self.driver.send_keys("search_frame_on_application_page", text)
    
    def verify_disney_app_show_on_application_list(self):
        return self.driver.wait_for_object("disney+_on_application_list", raise_e=False, timeout=10)
    
    def click_internal_speaker_on_thompson(self):
        self.driver.click("internal_speaker_on_thompson", timeout = 30)

    def is_internal_speaker_on_thompson_selected(self):
        return self.driver.get_attribute("internal_speaker_on_thompson", "Toggle.ToggleState")

    def click_internal_speaker_on_arti_a(self):
        self.driver.click("internal_speaker_on_arti-a", timeout = 20)

    def is_internal_speaker_on_arti_a_selected(self):
        return self.driver.get_attribute("internal_speaker_on_arti-a", "Toggle.ToggleState")
        
    def click_headphone_plugin_pc(self):
        self.driver.click("headphone_plugin_pc", timeout = 40)

    def is_headphone_on_pc_selected(self):
        return self.driver.get_attribute("headphone_plugin_pc", "Toggle.ToggleState")
    
    def is_headphone_plugin_pc_selected(self):
        return self.driver.get_attribute("headphone_plugin_pc", "Toggle.ToggleState")
        
    def verify_right_arrow_on_application_list_show(self):
        return self.driver.wait_for_object("right_arrow_on_application_list", raise_e=False, timeout=10)
    
    def verify_aiqiyi_app_show_on_application_list(self):
        return self.driver.wait_for_object("aiqiyi_on_application_list", raise_e=False, timeout=10)
    
    def click_aiqiyi_app_on_application_list(self):
        self.driver.click("aiqiyi_on_application_list")
    
    def verify_tencent_app_show_on_application_list(self):
        return self.driver.wait_for_object("tencent_on_application_list", raise_e=False, timeout=10)
    
    def click_tencent_app_on_application_list(self):
        self.driver.click("tencent_on_application_list")
    
    def turn_off_immersive_audio_toggle(self):
        self.driver.click("immersive_toggle_on")

    def is_immersive_toggle_status_off_status(self):
        return self.driver.get_attribute("immersive_toggle_off", "Toggle.ToggleState")

    def click_close_warranty(self):
        self.driver.click("close_btn_warranty")
    
    def is_speak_swap_button_on_visible(self):
        return self.driver.wait_for_object("speak_swap_button_on", raise_e=False, timeout=10)
    
    def click_disney_plus_on_application_list(self):
        self.driver.click("disney+_on_application_list")
    
    def click_all_Application_icon(self):
        self.driver.click("all_Application_icon")
    
    def verify_hp_privacy_settings_app_under_application_items(self):
        return self.driver.wait_for_object("hp_privacy_settings_app_under_application_items", raise_e=False, timeout=10)
    
    def click_adaptive_audio_toggle_off_button(self):
        self.driver.click("adaptive_audio_toggle_switch_off")

    def get_adaptive_audio_toggle_button_off_state(self):
        return self.driver.get_attribute("adaptive_audio_toggle_switch_off","Toggle.ToggleState")
    
    def close_calculator_app(self):
        self.driver.click("close_calculator_app_button")

    def click_restore_default_continue_button(self):
        self.driver.click("restore_default_continue_button", timeout = 40)

    def click_continue_on_restore_dialog(self):
        self.driver.click("continue_button")

    def click_headset_output_for_mm(self):
        self.driver.click("headset_output_for_mm")

    def is_headset_input_mm_device_selected(self):
        return self.driver.get_attribute("headset_output_for_mm", "Toggle.ToggleState")

    def click_headset_usb(self):
        self.driver.click("headset_usb")

    def is_headset_usb_device_selected(self):
        return self.driver.get_attribute("headset_usb", "Toggle.ToggleState")

    def click_headset_usb_output(self):
        self.driver.click("headset_usb_output")

    def is_usb_headphone_selected(self):
        return self.driver.get_attribute("headset_usb_output","Toggle.ToggleState")
    
    def click_speaker_on_bopeep(self):
        self.driver.click("speaker_on_bopeep")

    def click_headset_usb_input(self):
        self.driver.click("headset_usb_input")

    def verify_internal_speaker_output_device(self):
        return self.driver.wait_for_object("internal_speaker_on_arti-a", raise_e=False, timeout=10)

    def verify_internal_mic_input_device(self):
        return self.driver.wait_for_object("internal_microphone_input_device", raise_e=False, timeout=10)
      
    def click_output_mic_icon_to_mute_unmute(self):
        self.driver.click("output_mic_icon")

    def get_output_mic_mute_unmute_status(self):
        return self.driver.get_attribute("output_mic_icon","Name")

    def scroll_window_locator(self):
        return self.driver.wait_for_object("scroll_window", timeout=10)    

    def click_headphones_realtek_arti(self):
        self.driver.click("headphones_plugin_pc_arti")
    
    def get_clock_under_application_items(self):
        return self.driver.get_attribute("clock_under_application_items","Name")

    def click_to_select_calculator_app(self):
        self.driver.click("calculator_on_application_list")

    def click_speaker_on_device(self):
        self.driver.click("click_on_speaker", timeout = 10)

    def verify_usb_headphone_input_device(self):
        return self.driver.wait_for_object("usb_headphone_input_device", raise_e=False, timeout=30)

    def verify_speaker_on_device(self):
        return self.driver.wait_for_object("click_on_speaker", raise_e=False, timeout = 10)
    
    def verify_microphone_usb_audio_external_device(self):
        return self.driver.wait_for_object("microphone_usb_audio_external_input_device", raise_e=False, timeout = 10)
    
    def verify_microphone_array_amd_input_device(self):
        return self.driver.wait_for_object("microphone_array_amd_input_device", raise_e=False, timeout = 10)
    
    def click_microphone_array_amd_input_device(self):
        self.driver.click("microphone_array_amd_input_device")

    def verify_usb_headphone_output_device_grogu_show(self):
        return self.driver.wait_for_object("usb_headphone_output_device_grogu", raise_e=False, timeout=10) is not False
    
    def click_usb_headphone_output_device_grogu(self):
        self.driver.click("usb_headphone_output_device_grogu")

    def click_internal_speaker_output_device_grogu(self):
        self.driver.click("internal_speaker_output_device_grogu", timeout = 40)

    def get_windows_system_sound_output_volume_tab(self):
        return self.driver.get_attribute("windows_system_sound_output_volume_tab","RangeValue.Value")

    def click_internal_speaker_output_device_thompson(self):
        self.driver.click("internal_speaker_output_device_thompson", timeout = 40)

    def is_internal_speaker_output_device_thompson_selected(self):
        return self.driver.get_attribute("internal_speaker_output_device_thompson", "Toggle.ToggleState")

    def verify_internal_speaker_output_device(self):
        return self.driver.wait_for_object("internal_speaker_output_device_grogu", raise_e=False, timeout = 10)
    
    def is_calculator_on_application_list_selected(self):
        return self.driver.get_attribute("calculator_on_application_list","Toggle.ToggleState")
    
    def click_mic_mode_tooltip(self):
        self.driver.click("mic_mode_tooltip")
    
    def get_mic_mode_tooltip(self):
        return self.driver.get_attribute("mic_mode_tooltip","Name")
    
    def click_headset_usb_input_rameses(self):
        self.driver.click("usb_speaker_output_device", timeout = 40)

    def click_headset_bt_output_rameses(self):
        self.driver.click("bluetooth_speaker_output_device")

    def click_microphone_array_in_all_devices(self):
        self.driver.click("microphone_array")

    def click_headset_usb_mic(self):
        self.driver.click("headset_usb_mic")

    def verify_headset_tab_starts(self):
        return self.driver.wait_for_object("headset_usb_starts", raise_e=False, timeout = 40) is not False
    
    def verify_headset_device(self):
        return self.driver.wait_for_object("headset_device", raise_e=False, timeout = 40) is not False

    def click_headset_bt_output(self):
        self.driver.click("headphone_plugin_pc")

    def verify_headphones_plugin_pc_arti(self):
        return self.driver.wait_for_object("headphones_plugin_pc_arti", raise_e=False, timeout = 40) is not False
    
    def verify_bang_and_olufsen_logo(self):
        return self.driver.wait_for_object("bang_and_olufsen_logo", raise_e=False, timeout = 40) is not False

    def verify_dts_logo_less_than_24c1(self):
        return self.driver.wait_for_object("dts_logo_less_than_24c1", raise_e=False, timeout = 40) is not False
    
    def verify_hyperx_logo(self):
        return self.driver.wait_for_object("hyperx_logo", raise_e=False, timeout = 40) is not False
    
    def verify_dtsx_logo_24c1_and_above(self):
        return self.driver.wait_for_object("dtsx_logo_24c1_and_above", raise_e=False, timeout = 40) is not False
    
    def verify_bo_logo(self):
        return self.driver.wait_for_object("bo_logo", raise_e=False, timeout = 40) is not False
    
    def is_headset_usb_input_selected(self):
        return self.driver.get_attribute("headset_usb_input","Toggle.ToggleState")
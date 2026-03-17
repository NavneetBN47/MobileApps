import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
import logging


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_oobe")
#This suite should be run on keelung27 platform
class Test_Suite_Audio_Accessibility(object):


    def verify_images(self, image_compare_result, image_name, percentage):
        logging.info(f"Image comparison result at {percentage}% text size: {image_compare_result}")
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_check_audio_contents_will_be_focused_by_keyboard_keys_C50723568(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        # check audio card is displayed
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # check audio context aware
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"
        # Focus on Audio context aware by Tab KEY
        self.fc.fd["audio"].press_tab("global_icon")
        assert self.fc.fd["audio"].is_focus_on_element("global_icon"), "Global icon is not focused"
        self.fc.fd["audio"].press_tab("disney+_on_application_list") 
        assert self.fc.fd["audio"].is_focus_on_element("disney+_on_application_list"), "Disney app is not focused"
        self.fc.fd["audio"].press_tab("aiqiyi_on_application_list") 
        assert self.fc.fd["audio"].is_focus_on_element("aiqiyi_on_application_list"), "Aiqiyi app is not focused"
        self.fc.fd["audio"].press_tab("tencent_on_application_list") 
        assert self.fc.fd["audio"].is_focus_on_element("tencent_on_application_list"), "Tencent app is not focused"
        self.fc.fd["audio"].press_tab("add_application_button")
        assert self.fc.fd["audio"].is_focus_on_element("add_application_button"), "Add application button is not focused"
        # check audio level-Output
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        assert self.fc.fd["audio"].verify_output_volume_slider_show_up(), "Output volume slider is not displayed"
        assert self.fc.fd["audio"].verify_mute_toggle_for_output_show_up(), "Output mute toggle is not displayed"
        if self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1":
            time.sleep(2)
            self.fc.fd["audio"].turn_off_noise_removal()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
            time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up(), "AI Noise Removal toggle is not displayed"
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        assert self.fc.fd["audio"].verify_input_volume_slider_show_up(), "Input volume slider is not displayed"
        assert self.fc.fd["audio"].verify_mute_toggle_for_input_show_up(), "Input mute toggle is not displayed"
        if self.fc.fd["audio"].verify_noise_reduction_toggle_off_state() == "1":
            time.sleep(2)
            self.fc.fd["audio"].turn_on_noise_reduction()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_off_state() == "0", "Noise Reduction toggle is not turned off"
            time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up(), "AI Noise Reduction toggle is not displayed"
        # Focus on Audio level-Output by Tab KEY
        self.fc.fd["audio"].press_tab("for_all_applications_text")
        self.fc.fd["audio"].press_tab("output_combobox")
        assert self.fc.fd["audio"].is_focus_on_element("output_combobox"), "Output combobox is not focused"
        self.fc.fd["audio"].press_tab("output_volume_slider")
        assert self.fc.fd["audio"].is_focus_on_element("output_volume_slider"), "Output volume slider is not focused"
        self.fc.fd["audio"].press_tab("mute_toggle_for_output")
        assert self.fc.fd["audio"].is_focus_on_element("mute_toggle_for_output"), "Output mute toggle is not focused"
        if self.fc.fd["audio"].get_mute_toggle_for_output_status() == "0":
            self.fc.fd["audio"].press_enter("mute_toggle_for_output")
        Op = self.fc.fd["audio"].get_mute_toggle_for_output_status()
        assert Op == "1", "Output mute toggle is not on"
        self.fc.fd["audio"].press_tab("ai_noise_removal_toggle_off")
        assert self.fc.fd["audio"].is_focus_on_element("ai_noise_removal_toggle_on"), "AI Noise Removal toggle is not focused"
        self.fc.fd["audio"].press_enter("ai_noise_removal_toggle_on")
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is not turned on"
        time.sleep(2)
        # Focus on Audio level-Input by Tab KEY
        self.fc.fd["audio"].press_tab("input_combobox")
        assert self.fc.fd["audio"].is_focus_on_element("input_combobox"), "Input combobox is not focused"
        self.fc.fd["audio"].press_tab("input_volume_slider")
        assert self.fc.fd["audio"].is_focus_on_element("input_volume_slider"), "Input volume slider is not focused"
        self.fc.fd["audio"].press_tab("mute_toggle_for_input")
        assert self.fc.fd["audio"].is_focus_on_element("mute_toggle_for_input"), "Input mute toggle is not focused"
        if self.fc.fd["audio"].get_mute_toggle_for_input_status() == "0":
            self.fc.fd["audio"].press_enter("mute_toggle_for_input")
        Ip = self.fc.fd["audio"].get_mute_toggle_for_input_status()
        assert Ip == "1", "Input mute toggle is not on"
        self.fc.fd["audio"].press_tab("ai_noise_reduction_toggle_on")
        assert self.fc.fd["audio"].is_focus_on_element("ai_noise_reduction_toggle_off"), "AI Noise reduction toggle is not focused"
        self.fc.fd["audio"].press_enter("ai_noise_reduction_toggle_off")
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "0", "AI Noise reduction toggle is not turned off"
        time.sleep(2)
        # check Presets
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_voice_button_show_up(), "Audio presets voice button is not displayed"
        # Focus on Presets by Tab KEY
        self.fc.fd["audio"].press_tab("audio_presets_music_button")
        assert self.fc.fd["audio"].is_focus_on_element("audio_presets_music_button"), "Audio presets music button is not focused"
        self.fc.fd["audio"].press_tab("audio_presets_movie_button")
        assert self.fc.fd["audio"].is_focus_on_element("audio_presets_movie_button"), "Audio presets movie button is not focused"
        self.fc.fd["audio"].press_tab("audio_presets_voice_button")
        assert self.fc.fd["audio"].is_focus_on_element("audio_presets_voice_button"), "Audio presets voice button is not focused"
        self.fc.fd["audio"].press_enter("audio_presets_voice_button")
        time.sleep(2)
        assert self.fc.fd["audio"].verify_voice_button_is_selected_state() == "1", "Voice button is not selected"
        time.sleep(2)
        # check Equalizer
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_125_show_up(), "horizontal axis 125 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_250_show_up(), "horizontal axis 250 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_500_show_up(), "horizontal axis 500 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_1k_show_up(), "horizontal axis 1k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_2k_show_up(), "horizontal axis 2k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_4k_show_up(), "horizontal axis 4k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_8k_show_up(), "horizontal axis 8k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_16k_show_up(), "horizontal axis 16k is not displayed"
        # Focus on EQ by Tab KEY
        self.fc.fd["audio"].press_tab("horizontal_axis_32")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_32"), "EQ 32 is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_64")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_64"), "EQ 64 is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_125")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_125"), "EQ 125 is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_250")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_250"), "EQ 250 is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_500")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_500"), "EQ 500 is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_1k")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_1k"), "EQ 1k is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_2k")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_2k"), "EQ 2k is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_4k")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_4k"), "EQ 4k is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_8k")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_8k"), "EQ 8k is not focused"
        self.fc.fd["audio"].press_tab("horizontal_axis_16k")
        assert self.fc.fd["audio"].is_focus_on_element("horizontal_axis_16k"), "EQ 16k is not focused"
        # check restore defaults button
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "restore defaults button is not displayed"
        # Focus on restore defaults button by Tab KEY
        self.fc.fd["audio"].press_tab("restore_defaults_button")
        assert self.fc.fd["audio"].is_focus_on_element("restore_defaults_button"), "restore defaults button is not focused"
        self.fc.fd["audio"].press_enter("restore_defaults_button")
        time.sleep(2)


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_check_myhp_will_be_closed_automatically_with_ALT_F4_C50723577(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        # check audio card is displayed
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        # close app by ALT + F4
        self.fc.fd["audio"].press_alt_f4_to_close_app()
        time.sleep(2)
        # verify myHP app is closed
        assert self.fc.fd["audio"].verify_global_icon_show_up() is False, "global icon is displayed since app is not be closed by ALT+F4"


    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.require_platform(["not available"])
    def test_03_verify_audio_control_module_increase_text_size_C50723570(self):
        try: 
            platform=self.platform.lower()
            self.fc.close_myHP()
            self.fc.fd["audio"].update_text_size_in_system_settings(225)

            self.fc.launch_myHP()

            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_output_title_show_up_image, machine_name=platform, page_number=1, element="output_title", text_size=225)
            self.verify_images(image_compare_result, "output title", 225)

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(3)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_input_title_show_up_image, machine_name=platform, page_number=2, element="input_title", text_size=225)
            self.verify_images(image_compare_result, "input title", 225)

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(3)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_audio_presets_movie_txt_show_up_image, machine_name=platform, page_number=3, element="audio_presets_movie_txt", text_size=225)
            self.verify_images(image_compare_result, "audio presets movie text", 225)

            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(3)

            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up_image, machine_name=platform, page_number=4, element="advanced_audio_settings_title", text_size=225)
            self.verify_images(image_compare_result, "advanced audio settings title", 225)

        finally: 
            self.fc.fd["audio"].update_text_size_in_system_settings(100)
import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert

pytest.app_info = "HPX"
language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')



@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["audio_common_screenshot"])
def screenshot_folder_name(request):
    return request.param
    

class Test_Suite_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        time.sleep(5)
        cls.attachment_path = conftest_misc.get_attachment_folder()
    
    def test_01_audiocontrol_module_C33045040(self,language, publish_hpx_localization_screenshot, screenshot_folder_name):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/audiocontrolLocalization.json", language, "pcAudio")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["devices"].verify_audio_card_pcdevice()) is True, "Audio card not available"
        logging.info("Audio card available")
        self.fc.fd["devices"].click_audio_card_on_pcdevice()
        assert bool(self.fc.fd["audio"].verify_output_title()) is True, "Output title not available"
        # Output string verify
        expected_output_text = lang_settings["audioLevels"]["outputCard"]["output"]
        actual_output_text = self.fc.fd["audio"].get_output_text()
        ma_misc.create_localization_screenshot_folder("audio_common_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_audio_common_homepage01.png".format(language))
        soft_assertion.assert_equal(actual_output_text, expected_output_text, f"Output text is not matching, expected string text is {expected_output_text}, but got {actual_output_text}. ")
        # noice removal
        expected_noice_removal_text = lang_settings["noiseCancellation"]["output"]["header"]
        actual_noice_removal_text = self.fc.fd["audio"].get_noice_removal_text()
        soft_assertion.assert_equal(actual_noice_removal_text, expected_noice_removal_text, f"Noice removal text is not matching, expected string text is {expected_noice_removal_text}, but got {actual_noice_removal_text}. ")
        # noise removal tool tip, not avialable now due to missing AUID
        self.fc.fd["audio"].click_noise_removal_tool_tip()
        expected_noice_removal_tooltip_text = lang_settings["noiseCancellation"]["output"]["toolTip"]
        actual_noice_removal_tooltip_text = self.fc.fd["audio"].get_noise_removal_tool_tip_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_noise_removal_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_noice_removal_tooltip_text, expected_noice_removal_tooltip_text, f"Noice removal tooltip text is not matching, expected string text is {expected_noice_removal_tooltip_text}, but got {actual_noice_removal_tooltip_text}. ")
        # input
        expected_input_text = lang_settings["audioLevels"]["inputCard"]["input"]
        actual_input_text = self.fc.fd["audio"].get_input_text()
        soft_assertion.assert_equal(actual_input_text, expected_input_text, f"Input text is not matching, expected string text is {expected_input_text}, but got {actual_input_text}. ")
        # noice reduction
        expected_noice_reduction_text = lang_settings["noiseCancellation"]["input"]["header"]
        actual_noice_reduction_text = self.fc.fd["audio"].get_noice_reduction_text()
        soft_assertion.assert_equal(actual_noice_reduction_text, expected_noice_reduction_text, f"Noice reduction text is not matching, expected string text is {expected_noice_reduction_text}, but got {actual_noice_reduction_text}. ")
        # noise reduction toot tip, not avialable now due to missing AUID
        self.fc.fd["audio"].click_noise_reduction_tooltip()
        expected_noice_reduction_tooltip_text = lang_settings["noiseCancellation"]["input"]["toolTip"]
        actual_noice_reduction_tooltip_text = self.fc.fd["audio"].get_noise_reduction_tooltip_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_noise_reduction_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_noice_reduction_tooltip_text, expected_noice_reduction_tooltip_text, f"Noice reduction tooltip text is not matching, expected string text is {expected_noice_reduction_tooltip_text}, but got {actual_noice_reduction_tooltip_text}. ")
        # mice mode
        expected_mice_mode_text = lang_settings["micMode"]["header"]
        actual_mice_mode_text = self.fc.fd["audio"].get_mice_mode_text()
        soft_assertion.assert_equal(actual_mice_mode_text, expected_mice_mode_text, f"Mice mode text is not matching, expected string text is {expected_mice_mode_text}, but got {actual_mice_mode_text}. ")
        # mic mode tooltip        
        if bool(self.fc.fd["audio"].verify_studio_recording_show()) is False:
            self.fc.fd["audio"].click_mic_mode_tooltip()
            expected_conference_text = lang_settings["micMode"]["toolTip"]["conference"]
            expected_personal_text = lang_settings["micMode"]["toolTip"]["personal"]
            expected_mic_mode_tooltip_text = expected_conference_text+expected_personal_text
            actual_mic_mode_tooltip_text = self.fc.fd["audio"].get_mic_mode_tooltip()
            ac=actual_mic_mode_tooltip_text.replace('\n','')
            soft_assertion.assert_contains(ac, expected_mic_mode_tooltip_text, f"Mic mode tooltip text is not matching, expected string text is {expected_mic_mode_tooltip_text}, but got {ac}. ")
        if bool(self.fc.fd["audio"].verify_studio_recording_show()) is True:
            self.fc.fd["audio"].click_mic_mode_tooltip()
            expected_conference_text = lang_settings["micMode"]["toolTip"]["conference"]
            expected_personal_text = lang_settings["micMode"]["toolTip"]["personal"]
            expected_studio_text = lang_settings["micMode"]["toolTip"]["studioRecording"]
            expected_mic_mode_tooltip_text = expected_conference_text+expected_personal_text+"  "+expected_studio_text
            actual_mic_mode_tooltip_text = self.fc.fd["audio"].get_mic_mode_tooltip()
            ac=actual_mic_mode_tooltip_text.replace('\n','')
            soft_assertion.assert_contains(ac, expected_mic_mode_tooltip_text, f"Mic mode tooltip text is not matching, expected string text is {expected_mic_mode_tooltip_text}, but got {ac}. ")
        # conference
        expected_conference_text = lang_settings["micMode"]["radioOptions"]["conference"]
        actual_conference_text = self.fc.fd["audio"].get_conference_text()
        soft_assertion.assert_equal(actual_conference_text, expected_conference_text, f"Conference text is not matching, expected string text is {expected_conference_text}, but got {actual_conference_text}. ")
        # preset
        expected_preset_text = lang_settings["presets"]["title"]
        actual_preset_text = self.fc.fd["audio"].get_preset_text()
        soft_assertion.assert_equal(actual_preset_text, expected_preset_text, f"Preset text is not matching, expected string text is {expected_preset_text}, but got {actual_preset_text}. ")
        # preset tool tip
        self.fc.fd["audio"].click_preset_tooltip()
        expected_preset_tooltip_text = lang_settings["presets"]["tooltip"]
        actual_preset_tooltip_text = self.fc.fd["audio"].get_preset_tooltip_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_preset_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_preset_tooltip_text, expected_preset_tooltip_text, f"Preset tooltip text is not matching, expected string text is {expected_preset_tooltip_text}, but got {actual_preset_tooltip_text}. ")
        # music
        expected_music_text = lang_settings["presets"]["radioOptions"]["music"]
        actual_music_text = self.fc.fd["audio"].get_music_text_with_id()
        logging.info("checking music" + str(actual_music_text))
        soft_assertion.assert_equal(actual_music_text, expected_music_text, f"Music text is not matching, expected string text is {expected_music_text}, but got {actual_music_text}. ")
        # voice
        expected_voice_text = lang_settings["presets"]["radioOptions"]["voice"]
        actual_voice_text = self.fc.fd["audio"].get_voice_text_with_id()
        soft_assertion.assert_equal(actual_voice_text, expected_voice_text, f"Voice text is not matching, expected string text is {expected_voice_text}, but got {actual_voice_text}. ")
        # movie
        if bool(self.fc.fd["audio"].verify_movie_preset()):
            expected_movie_text = lang_settings["presets"]["radioOptions"]["movie"]
            actual_movie_text = self.fc.fd["audio"].get_movie_text_with_id()
            soft_assertion.assert_equal(actual_movie_text, expected_movie_text, f"Movie text is not matching, expected string text is {expected_movie_text}, but got {actual_movie_text}. ")
        else:
            logging.info("movie preset not available")
        # Auto
        if bool(self.fc.fd["audio"].verify_auto_preset()):
            expected_auto_text = lang_settings["presets"]["radioOptions"]["auto"]
            actual_auto_text = self.fc.fd["audio"].get_auto_text_with_id()
            soft_assertion.assert_equal(actual_auto_text, expected_auto_text, f"Auto text is not matching, expected string text is {expected_auto_text}, but got {actual_auto_text}. ")
        else:
            logging.info("Auto preset not available")
        if bool(self.fc.fd["audio"].verify_studio_recording_show()) is False:
            # equilizer
            expected_equilizer_text = lang_settings["equalizer"]["title"]
            actual_equilizer_text = self.fc.fd["audio"].get_equilizer_text()
            soft_assertion.assert_equal(actual_equilizer_text, expected_equilizer_text, f"Equilizer text is not matching, expected string text is {expected_equilizer_text}, but got {actual_equilizer_text}. ")
            # equlilizer tooltip, not avialable now due to missing AUID
            self.fc.fd["audio"].click_band_eq_tooltip()
            expected_eq_tooltip_text = lang_settings["equalizer"]["tooltip"]
            actual_eq_tooltip_text = self.fc.fd["audio"].get_band_eq_tooltip_text()
            soft_assertion.assert_equal(actual_eq_tooltip_text, expected_eq_tooltip_text, f"Equilizer tooltip text is not matching, expected string text is {expected_eq_tooltip_text}, but got {actual_eq_tooltip_text}. ")
            # sound
            expected_sound_text = lang_settings["eq"]["header"]["title"]
            actual_sound_text = self.fc.fd["audio"].get_sound_text()
            soft_assertion.assert_equal(actual_sound_text, expected_sound_text, f"Sound text is not matching, expected string text is {expected_sound_text}, but got {actual_sound_text}. ")
            # sound tooltip, not avialable now due to missing AUID
            self.fc.fd["audio"].click_basic_eq_tooltip()
            expected_sound_tooltip_text = lang_settings["eq"]["header"]["tooltip"]
            actual_sound_tooltip_text = self.fc.fd["audio"].get_basic_eq_tooltip_text()
            soft_assertion.assert_equal(actual_sound_tooltip_text, expected_sound_tooltip_text, f"Sound tooltip text is not matching, expected string text is {expected_sound_tooltip_text}, but got {actual_sound_tooltip_text}. ")
            self.fc.swipe_window(direction="down", distance=7) 
            # Bass
            expected_bass_text = lang_settings["eq"]["sliders"]["bass"]
            actual_bass_text = self.fc.fd["audio"].get_bass_text()
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_audio_common_homepage02.png".format(language))
            soft_assertion.assert_equal(actual_bass_text, expected_bass_text, f"Bass text is not matching, expected string text is {expected_bass_text}, but got {actual_bass_text}. ")
            # treble
            expected_treble_text = lang_settings["eq"]["sliders"]["treble"]
            actual_treble_text = self.fc.fd["audio"].get_treble_text()
            soft_assertion.assert_equal(actual_treble_text, expected_treble_text, f"Treble text is not matching, expected string text is {expected_treble_text}, but got {actual_treble_text}. ")
            # width
            expected_width_text = lang_settings["eq"]["sliders"]["width"]
            actual_width_text = self.fc.fd["audio"].get_width_text()
            soft_assertion.assert_equal(actual_width_text, expected_width_text, f"Width text is not matching, expected string text is {expected_width_text}, but got {actual_width_text}. ")
        # sound collibration
        # self.fc.fd["audio"].search_text("sound_calibration")
        # expected_sound_calibration_text = lang_settings["soundCalibration"]["header"]
        # actual_sound_calibration_text = self.fc.fd["audio"].get_sound_calibration_text()
        # assert actual_sound_calibration_text == expected_sound_calibration_text, "Sound calibration text not matched"
        # self.driver.swipe(direction="down", distance=2)
        # # my profile
        # expected_my_profile_text = lang_settings["soundCalibration"]["myProfile"]
        # actual_my_profile_text = self.fc.fd["audio"].get_my_profle_text()
        # self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_my_profile.png".format(language))
        # assert actual_my_profile_text == expected_my_profile_text, "My profile text not matched"
        # self.driver.swipe(direction="down", distance=2)
        # # Notify_text
        # expected_notify_text = lang_settings["soundCalibration"]["checkboxText"]
        # actual_notify_text = self.fc.fd["audio"].get_notify_text()
        # self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_audio_common_homepage03.png".format(language))
        # assert actual_notify_text == expected_notify_text, "Notify text not matched"
        # # intensity
        # expected_intensity_text = lang_settings["soundCalibration"]["intensitySliderHeader"]
        # actual_intensity_text = self.fc.fd["audio"].get_intensity_text()
        # assert actual_intensity_text == expected_intensity_text, "Intensity text not matched"
        # # sound test
        # expected_sound_test_text = lang_settings["soundCalibration"]["soundTestText"]
        # actual_sound_test_text = self.fc.fd["audio"].get_sound_test_text()
        # assert actual_sound_test_text == expected_sound_test_text, "Sound test text not matched"
        # self.driver.swipe(direction="down", distance=2)
        # # output
        # expected_output_text = lang_settings["audioLevels"]["outputCard"]["output"]
        # actual_output_text = self.fc.fd["audio"].get_profile_output_text()
        # assert actual_output_text == expected_output_text, "Output text not matched"
        # # balance
        # expected_balance_text = lang_settings["soundCalibration"]["balanceSliderHeader"]
        # actual_balance_text = self.fc.fd["audio"].get_balance_text()
        # self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_audio_common_homepage04.png".format(language))
        # assert actual_balance_text == expected_balance_text, "Balance text not matched"
        # self.driver.swipe(direction="down", distance=2)
        # # Min
        # expected_min_text = lang_settings["soundCalibration"]["minText"]
        # actual_min_text = self.fc.fd["audio"].get_min_text()
        # self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_screenshot/{}_audio_common_homepage05.png".format(language))
        # assert actual_min_text == expected_min_text, "Min text not matched"
        # # Max
        # expected_max_text = lang_settings["soundCalibration"]["maxText"]
        # actual_max_text = self.fc.fd["audio"].get_max_text()
        # assert actual_max_text == expected_max_text, "Max text not matched"
        # # left
        # expected_left_text = lang_settings["soundCalibration"]["leftText"]
        # actual_left_text = self.fc.fd["audio"].get_left_text()
        # assert actual_left_text == expected_left_text, "Left text not matched"
        # # right
        # expected_right_text = lang_settings["soundCalibration"]["rightText"]
        # actual_right_text = self.fc.fd["audio"].get_right_text()
        # assert actual_right_text == expected_right_text, "Right text not matched"
        # #  reset
        # expected_reset_text = lang_settings["soundCalibration"]["reset"]
        # actual_reset_text = self.fc.fd["audio"].get_reset_text()
        # assert actual_reset_text == expected_reset_text, "Reset text not matched"
        # # customize Manually
        # expected_customize_manually_text = lang_settings["soundCalibration"]["buttonText1"]
        # actual_customize_manually_text = self.fc.fd["audio"].get_customize_manually_text()
        # assert actual_customize_manually_text == expected_customize_manually_text, "Customize manually text not matched"
        # # start test
        # expected_start_test_text = lang_settings["soundCalibration"]["buttonText2"]
        # actual_start_test_text = self.fc.fd["audio"].get_start_test_text()
        # assert actual_start_test_text == expected_start_test_text, "Start test text not matched"
        #restore defaults
        if bool(self.fc.fd["audio"].verify_restore_button_text()):
            expected_restore_defaults_text = lang_settings["restoreDefaultsButton"]
            actual_restore_defaults_text = self.fc.fd["audio"].get_restore_button_text()
            soft_assertion.assert_equal(actual_restore_defaults_text, expected_restore_defaults_text, f"Restore defaults text is not matching, expected string text is {expected_restore_defaults_text}, but got {actual_restore_defaults_text}. ")
        else:
            logging.info("Restore Defaults not available")

        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()    
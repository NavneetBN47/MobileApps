import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc

pytest.app_info = "HPX"
language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')




@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["audio_speakconfiguration_screenshot"])
def screenshot_folder_name(request):
    return request.param

class Test_Suite_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.attachment_path = conftest_misc.get_attachment_folder()


    def test_04_audiocontrol_module_speaker_configuration_C34715026(self, language, publish_hpx_localization_screenshot, screenshot_folder_name):
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/audiocontrolLocalization.json", language, "pcAudio")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["devices"].verify_audio_card_pcdevice())is True, "Audio card is not available"
        logging.info("Audio card available")
        self.fc.fd["devices"].click_audio_card_on_pcdevice()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_speaker()
        time.sleep(1)
        self.fc.swipe_window(direction="down", distance=2)
        # external speaker setting
        expected_external_speaker_setting_text = lang_settings["externalSpeakerSettings"]["title"]
        actual_external_speaker_setting_text = self.fc.fd["audio"].get_external_speaker_setting_text()
        ma_misc.create_localization_screenshot_folder("audio_speakconfiguration_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_speakconfiguration_screenshot/{}_audio_speakconfiguration01.png".format(language))
        assert actual_external_speaker_setting_text == expected_external_speaker_setting_text, "External Speaker Setting text is not matched"
        # speaker configuration
        time.sleep(5)
        expected_speaker_config_text = lang_settings["externalSpeakerSettings"]["subtitle"]
        actual_speaker_config_text = self.fc.fd["audio"].get_speaker_config_text()
        assert actual_speaker_config_text == expected_speaker_config_text, "Speaker Configuration text is not matched"
        # stereo
        expected_stereo_text = lang_settings["externalSpeakerSettings"]["stereo"]
        actual_stereo_text = self.fc.fd["audio"].get_stereo_text()
        assert actual_stereo_text == expected_stereo_text, "Stereo text is not matched"
        #Quad
        expected_quad_text = lang_settings["externalSpeakerSettings"]["quad"]
        actual_quad_text = self.fc.fd["audio"].get_quad_text()
        assert actual_quad_text == expected_quad_text, "Quad text is not matched"
        #5.1
        expected_fiftyone_text = lang_settings["externalSpeakerSettings"]["fiftyOne"]
        actual_fiftyone_text = self.fc.fd["audio"].get_fiftyone_text()
        assert actual_fiftyone_text == expected_fiftyone_text, "5.1 text is not matched"
        # setup & test sound
        time.sleep(5)
        self.driver.swipe(direction="down", distance=2)
        expected_setup_test_sound_text = lang_settings["externalSpeakerSettings"]["setupTestSound"]
        actual_setup_test_sound_text = self.fc.fd["audio"].get_setup_test_sound_text()
        assert actual_setup_test_sound_text == expected_setup_test_sound_text, "Setup & Test Sound text is not matched"
        #expand setup & test sound carat and verify content in stereo
        time.sleep(15)
        self.fc.fd["audio"].click_to_expand_caret()
        self.fc.fd["audio"].click_stereo_tab()
        #multi-streaming
        self.driver.swipe(direction="down", distance=3)
        expected_multistreaming_text = lang_settings["externalSpeakerSettings"]["multiStreaming"]
        actual_multistreaming_text = self.fc.fd["audio"].get_multistreaming_text()
        assert actual_multistreaming_text == expected_multistreaming_text, "Multi Streaming text is not matched"
        #play test
        expected_playtest_text = lang_settings["externalSpeakerSettings"]["playTest"]
        actual_playtest_text = self.fc.fd["audio"].get_play_test_text()
        assert actual_playtest_text == expected_playtest_text, "Play Test text is not matched"
        #front left
        expected_frontleft_text = lang_settings["externalSpeakerSettings"]["frontLeft"]
        actual_frontleft_text = self.fc.fd["audio"].get_front_left_text()
        assert actual_frontleft_text == expected_frontleft_text, "Front Left text is not matched"
        #front right
        expected_frontright_text = lang_settings["externalSpeakerSettings"]["frontRight"]
        actual_frontright_text = self.fc.fd["audio"].get_front_right_text()
        assert actual_frontright_text == expected_frontright_text, "Front Right text is not matched"
        #Quad
        self.fc.swipe_window(direction="up", distance=2)
        self.fc.fd["audio"].click_quad_tab()
        self.fc.swipe_window(direction="down", distance=2)
        #multi-streaming
        expected_multistreaming_text = lang_settings["externalSpeakerSettings"]["multiStreaming"]
        actual_multistreaming_text = self.fc.fd["audio"].get_multistreaming_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_speakconfiguration_screenshot/{}_audio_speakconfiguration02.png".format(language))
        assert actual_multistreaming_text == expected_multistreaming_text, "Multi Streaming text is not matched"
        #play test
        expected_playtest_text = lang_settings["externalSpeakerSettings"]["playTest"]
        actual_playtest_text = self.fc.fd["audio"].get_play_test_text()
        assert actual_playtest_text == expected_playtest_text, "Play Test text is not matched"
        #front left
        expected_frontleft_text = lang_settings["externalSpeakerSettings"]["frontLeft"]
        actual_frontleft_text = self.fc.fd["audio"].get_front_left_text()
        assert actual_frontleft_text == expected_frontleft_text, "Front Left text is not matched"
        #front right
        expected_frontright_text = lang_settings["externalSpeakerSettings"]["frontRight"]
        actual_frontright_text = self.fc.fd["audio"].get_front_right_text()
        assert actual_frontright_text == expected_frontright_text, "Front Right text is not matched"
        #back left
        expected_backleft_text = lang_settings["externalSpeakerSettings"]["backLeft"]
        actual_backleft_text = self.fc.fd["audio"].get_back_left_text()
        assert actual_backleft_text == expected_backleft_text, "Back Left text is not matched"
        #back right
        expected_backright_text = lang_settings["externalSpeakerSettings"]["backRight"]
        actual_backright_text = self.fc.fd["audio"].get_back_right_text()
        assert actual_backright_text == expected_backright_text, "Back Right text is not matched"
        # #5.1
        self.fc.swipe_window(direction="up", distance=2)
        self.fc.fd["audio"].click_fifty_one_tab()
        self.fc.swipe_window(direction="down", distance=2)
        #multi-streaming
        expected_multistreaming_text = lang_settings["externalSpeakerSettings"]["multiStreaming"]
        actual_multistreaming_text = self.fc.fd["audio"].get_multistreaming_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_speakconfiguration_screenshot/{}_audio_speakconfiguration03.png".format(language))
        assert actual_multistreaming_text == expected_multistreaming_text, "Multi Streaming text is not matched"
        #play test
        expected_playtest_text = lang_settings["externalSpeakerSettings"]["playTest"]
        actual_playtest_text = self.fc.fd["audio"].get_play_test_text()
        assert actual_playtest_text == expected_playtest_text, "Play Test text is not matched"
        #front left
        expected_frontleft_text = lang_settings["externalSpeakerSettings"]["frontLeft"]
        actual_frontleft_text = self.fc.fd["audio"].get_front_left_text()
        assert actual_frontleft_text == expected_frontleft_text, "Front Left text is not matched"
        #front right
        expected_frontright_text = lang_settings["externalSpeakerSettings"]["frontRight"]
        actual_frontright_text = self.fc.fd["audio"].get_front_right_text()
        assert actual_frontright_text == expected_frontright_text, "Front Right text is not matched"
        #back left
        expected_backleft_text = lang_settings["externalSpeakerSettings"]["backLeft"]
        actual_backleft_text = self.fc.fd["audio"].get_back_left_text()
        assert actual_backleft_text == expected_backleft_text, "Back Left text is not matched"
        #back right
        expected_backright_text = lang_settings["externalSpeakerSettings"]["backRight"]
        actual_backright_text = self.fc.fd["audio"].get_back_right_text()
        assert actual_backright_text == expected_backright_text, "Back Right text is not matched"
        #subwoofer
        expected_subwoofer_text = lang_settings["externalSpeakerSettings"]["subwoofer"]
        actual_subwoofer_text = self.fc.fd["audio"].get_subwoofer_text()
        assert actual_subwoofer_text == expected_subwoofer_text, "Subwoofer text is not matched"
        #center
        expected_center_text = lang_settings["externalSpeakerSettings"]["center"]
        actual_center_text = self.fc.fd["audio"].get_center_text()
        assert actual_center_text == expected_center_text, "Center text is not matched"
        self.fc.swipe_window(direction="up", distance=2)
        self.fc.fd["audio"].click_to_collapse_caret()
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")            
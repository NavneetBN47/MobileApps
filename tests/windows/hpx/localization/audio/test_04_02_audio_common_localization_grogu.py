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

@pytest.fixture(scope="session", params=["audio_common_grogu_screenshot"])
def screenshot_folder_name(request):
    return request.param
    

class Test_Suite_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.attachment_path = conftest_misc.get_attachment_folder()
    
    def test_01_audiocontrol_module_C35437863(self,language, publish_hpx_localization_screenshot, screenshot_folder_name):
        self.fc.myhp_login_startup_for_localization_scripts(language)
        time.sleep(2)
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/audiocontrolLocalization.json", language, "pcAudio")
        assert bool(self.fc.fd["devices"].verify_audio_card_pcdevice()) is True
        logging.info("Audio card available")
        self.fc.fd["devices"].click_audio_card_on_pcdevice()
        self.fc.fd["audio"].click_output_device_speaker()
        # preset
        expected_preset_text = lang_settings["presets"]["title"]
        actual_preset_text = self.fc.fd["audio"].get_preset_text()
        ma_misc.create_localization_screenshot_folder("audio_common_grogu_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_grogu_screenshot/{}_audio_common_grogu_preset01.png".format(language))
        assert actual_preset_text == expected_preset_text, "Preset text is not matched"
        # music
        expected_music_text = lang_settings["presets"]["radioOptions"]["music"]
        actual_music_text = self.fc.fd["audio"].get_music_text_with_id()
        logging.info("checking music" + str(actual_music_text))
        assert actual_music_text == expected_music_text, "Music text is not matched"
        # voice
        expected_voice_text = lang_settings["presets"]["radioOptions"]["voice"]
        actual_voice_text = self.fc.fd["audio"].get_voice_text_with_id()
        assert actual_voice_text == expected_voice_text, "Voice text is not matched"
        # Auto
        expected_auto_text = lang_settings["presets"]["radioOptions"]["auto"]
        actual_auto_text = self.fc.fd["audio"].get_auto_text_with_id()
        assert actual_auto_text == expected_auto_text, "Auto text is not matched"
        # equilizer
        self.fc.fd["audio"].search_text("equalizer_text")
        expected_equilizer_text = lang_settings["equalizer"]["title"]
        actual_equilizer_text = self.fc.fd["audio"].get_equilizer_text()
        assert actual_equilizer_text == expected_equilizer_text, "Equilizer text is not matched"
        self.fc.swipe_window(direction="down", distance=4)
        # Bass
        self.fc.fd["audio"].search_text("bass_text")
        expected_bass_text = lang_settings["eq"]["sliders"]["bass"]
        actual_bass_text = self.fc.fd["audio"].get_bass_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_grogu_screenshot/{}_audio_common_grogu_preset02.png".format(language))
        assert actual_bass_text == expected_bass_text, "Bass text is not matched"
        # treble
        self.fc.fd["audio"].search_text("treble_text")
        expected_treble_text = lang_settings["eq"]["sliders"]["treble"]
        actual_treble_text = self.fc.fd["audio"].get_treble_text()
        assert actual_treble_text == expected_treble_text, "Treble text is not matched"
        # width
        self.fc.fd["audio"].search_text("width_text")
        expected_width_text = lang_settings["eq"]["sliders"]["width"]
        actual_width_text = self.fc.fd["audio"].get_width_text()
        assert actual_width_text == expected_width_text, "Width text is not matched"
        self.fc.swipe_window(direction="down", distance=12)
        #restore defaults
        if self.stack != "production":
            expected_restore_defaults_text = lang_settings["restoreDefaultsButton"]
            actual_restore_defaults_text = self.fc.fd["audio"].get_restore_button_text()
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_common_grogu_screenshot/{}_audio_common_grogu_restore_button.png".format(language))
            assert actual_restore_defaults_text == expected_restore_defaults_text, "Restore defaults text is not matched"
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")        
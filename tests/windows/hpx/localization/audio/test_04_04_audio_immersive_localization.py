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

@pytest.fixture(scope="session", params=["audio_immersive_screenshot"])
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
    

    def test_02_audiocontrol_module_immersive_audio_C34715023(self, language, publish_hpx_localization_screenshot, screenshot_folder_name):
       lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/audiocontrolLocalization.json", language, "pcAudio")
       self.fc.myhp_login_startup_for_localization_scripts(language)
       time.sleep(6)
       assert bool(self.fc.fd["devices"].verify_audio_card_pcdevice()) is True, "Audio card is not available"
       logging.info("Audio card not available")
       self.fc.fd["devices"].click_audio_card_on_pcdevice()       
       self.fc.fd["audio"].verify_movie_preset()
       time.sleep(2)

       self.fc.fd["audio"].click_preset_movie_button()
       self.fc.fd["audio"].click_audio_settings_btn()
       #settings
       expected_settings_text = lang_settings["settings"]["title"]
       actual_setting_text = self.fc.fd["audio"].get_settings_text_with_id()
       ma_misc.create_localization_screenshot_folder("audio_immersive_screenshot", self.attachment_path)
       self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "audio_immersive_screenshot/{}_audio_immersive.png".format(language))
       assert expected_settings_text == actual_setting_text, "Settings text is not matched"
       #General Features
       expected_general_feature_text = lang_settings["settings"]["group"]
       actual_general_features_text= self.fc.fd["audio"].get_general_features_text_with_id()
       assert expected_general_feature_text == actual_general_features_text, "General Features text is not matched"
       #Immersive Audio
       expected_immersive_text = lang_settings["settings"]["radioOptions"]["immersiveAudio"]
       actual_immersive_audio_text = self.fc.fd["audio"].get_immersive_audio_text_with_id()
       assert expected_immersive_text == actual_immersive_audio_text, "Immersive Audio text is not matched"
       
       self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
       self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
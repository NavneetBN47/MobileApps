import logging
import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
from MobileApps.libs.ma_misc import conftest_misc
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert

pytest.app_info = "HPX"

language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')

@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["vision_ai_screenshot"])
def screenshot_folder_name(request):
    return request.param


class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, publish_hpx_localization_screenshot, screenshot_folder_name):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.attachment_path = conftest_misc.get_attachment_folder()

    def test_01_vision_ai_localization_C51179197(self, language):
        soft_assertion = SoftAssert()
        self.fc.myhp_login_startup_for_localization_scripts(language)
        time.sleep(2)
        try:
            lang_settings = ma_misc.load_json_file("resources/test_data/hpx/smartexperienceLocalization.json")[language]["translation"]["smartExperiences"]
        except KeyError:
            try:
                language = language[0:2]
                lang_settings = ma_misc.load_json_file("resources/test_data/hpx/smartexperienceLocalization.json")[language]["translation"]["smartExperiences"]
            except KeyError:
                language = "sr-Latn-RS"
                lang_settings = ma_misc.load_json_file("resources/test_data/hpx/smartexperienceLocalization.json")[language]["translation"]["smartExperiences"]    

        #Top title
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_presence_detection()
        expected_top_title_text=lang_settings["cameraAndPresenceDetection"]["title"]
        actual_top_title_text= self.fc.fd["vision_ai"].get_top_title_text()
        ma_misc.create_localization_screenshot_folder("vision_ai_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "vision_ai_screenshot/{}_vision_ai_01.png".format(language))
        soft_assertion.assert_equal(actual_top_title_text, expected_top_title_text, f"Top title text is not matching. expected string text is {expected_top_title_text}, but got {actual_top_title_text}. ")

        # Auto HDR
        time.sleep(3)
        expected_auto_hdr_text=lang_settings["cameraAndPresenceDetection"]["features"]["autoHDR"]["title"]
        actual_auto_hdr_text= self.fc.fd["vision_ai"].get_auto_hdr_text()
        soft_assertion.assert_equal(actual_auto_hdr_text, expected_auto_hdr_text, f"Auto HDR text is not matching. expected string text is {expected_auto_hdr_text}, but got {actual_auto_hdr_text}. ")

        # Auto HDR description
        time.sleep(3)
        expected_auto_hdr_description_text=lang_settings["cameraAndPresenceDetection"]["features"]["autoHDR"]["description"]
        actual_auto_hdr_description_text= self.fc.fd["vision_ai"].get_auto_hdr_description_text()
        soft_assertion.assert_equal(actual_auto_hdr_description_text, expected_auto_hdr_description_text, f"Auto HDR description text is not matching. expected string text is {expected_auto_hdr_description_text}, but got {actual_auto_hdr_description_text}. ")

        # Intelligent dynamic contrast
        time.sleep(3)
        expected_IDC_text=lang_settings["cameraAndPresenceDetection"]["features"]["intelligentDynamicContrast"]["title"]
        actual_IDC_text= self.fc.fd["vision_ai"].get_intelligent_dynamic_contrast_text()
        soft_assertion.assert_equal(actual_IDC_text, expected_IDC_text, f"Intelligent dynamic contrast text is not matching. expected string text is {expected_IDC_text}, but got {actual_IDC_text}. ")

        # Intelligent dynamic contrast description 
        time.sleep(3)
        expected_IDC_description_text=lang_settings["cameraAndPresenceDetection"]["features"]["intelligentDynamicContrast"]["description"]
        actual_IDC_description_text= self.fc.fd["vision_ai"].get_intelligent_dynamic_contrast_description_text()
        soft_assertion.assert_equal(actual_IDC_description_text, expected_IDC_description_text, f"Intelligent dynamic contrast description text is not matching. expected string text is {expected_IDC_description_text}, but got {actual_IDC_description_text}. ")

        # Attention focus 
        time.sleep(3)
        expected_attention_fous_text=lang_settings["cameraAndPresenceDetection"]["features"]["attentionFocus"]["title"]
        actual_attention_fous_text= self.fc.fd["vision_ai"].get_attention_focus_text()
        soft_assertion.assert_equal(actual_attention_fous_text, expected_attention_fous_text, f"Attention focus  text is not matching. expected string text is {expected_attention_fous_text}, but got {actual_attention_fous_text}. ")

        # Intelligent dynamic description 
        time.sleep(3)
        expected_attention_fous_description_text=lang_settings["cameraAndPresenceDetection"]["features"]["attentionFocus"]["description"]
        actual_attention_fous_description_text= self.fc.fd["vision_ai"].get_attention_focus_description_text()
        soft_assertion.assert_equal(actual_attention_fous_description_text, expected_attention_fous_description_text, f"Attention focus description text is not matching. expected string text is {expected_attention_fous_description_text}, but got {actual_attention_fous_description_text}. ")

        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=9)

        # Onlooker detection
        time.sleep(3)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "vision_ai_screenshot/{}_vision_ai_02.png".format(language))
        expected_on_looker_detection_text=lang_settings["cameraAndPresenceDetection"]["features"]["onlookerDetection"]["title"]
        actual_on_looker_detection_text= self.fc.fd["vision_ai"].get_on_looker_detection_text()
        soft_assertion.assert_equal(actual_on_looker_detection_text, expected_on_looker_detection_text, f"Onlooker detection text is not matching. expected string text is {expected_on_looker_detection_text}, but got {actual_on_looker_detection_text}. ")

        # Onlooker detection description 
        time.sleep(3)
        expected_on_looker_detection_description_text=lang_settings["cameraAndPresenceDetection"]["features"]["onlookerDetection"]["description"]
        actual_on_looker_detection_description_text= self.fc.fd["vision_ai"].get_on_looker_detection_description_text()
        soft_assertion.assert_equal(actual_on_looker_detection_description_text, expected_on_looker_detection_description_text, f"Onlooker detection description text is not matching. expected string text is {expected_on_looker_detection_description_text}, but got {actual_on_looker_detection_description_text}. ")

        # Enable screen blur
        expected_enable_screen_blur_text=lang_settings["cameraAndPresenceDetection"]["features"]["onlookerDetection"]["screenBlur"]["title"]
        actual_enable_screen_blur_text= self.fc.fd["vision_ai"].get_enable_screen_blur_text()
        soft_assertion.assert_equal(actual_enable_screen_blur_text, expected_enable_screen_blur_text, f"Enable screen blur text is not matching. expected string text is {expected_enable_screen_blur_text}, but got {actual_enable_screen_blur_text}. ")

        # Enable screen blur tooltip
        expected_enable_screen_blur_tooltip_text=lang_settings["cameraAndPresenceDetection"]["features"]["onlookerDetection"]["screenBlur"]["tooltipContent"]
        actual_enable_screen_blur_tooltip_text= self.fc.fd["vision_ai"].get_enable_screen_blur_tooltips()
        soft_assertion.assert_equal(actual_enable_screen_blur_tooltip_text, expected_enable_screen_blur_tooltip_text, f"Enable screen blur tooltip text is not matching. expected string text is {expected_enable_screen_blur_tooltip_text}, but got {actual_enable_screen_blur_tooltip_text}. ")


        # Restore default settings
        time.sleep(3)
        expected_restore_default_text=lang_settings["cameraAndPresenceDetection"]["restoreDefaults"]["title"]
        actual_restore_default_text= self.fc.fd["vision_ai"].get_restore_default_button_text()
        soft_assertion.assert_equal(actual_restore_default_text, expected_restore_default_text, f"Restore default settings text is not matching. expected string text is {expected_restore_default_text}, but got {actual_restore_default_text}. ")

        soft_assertion.raise_assertion_errors()

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

@pytest.fixture(scope="session", params=["screen_distance_screenshot"])
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

    def test_14_screen_distance_localization_C42873645(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/screendistanceLocalization.json", language, "pCScreenDistance")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["devices"].verify_screen_distance_card_on_pcdevice_page()) is True, "Screen distance card not available."
        logging.info("screen distance module available")
        self.fc.fd["devices"].click_screen_distance_card()

        #Screen Distance nav title
        expected_screen_distance_nav_title_text=lang_settings["title"]
        actual_screen_distance_nav_title_text=self.fc.fd["screen_distance"].get_screen_distance_nav_title()
        ma_misc.create_localization_screenshot_folder("screen_distance_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_homepage.png".format(language))
        soft_assertion.assert_equal(actual_screen_distance_nav_title_text, expected_screen_distance_nav_title_text, f"Screen distance nav title text is not matching, expected string text is {expected_screen_distance_nav_title_text}, but got {actual_screen_distance_nav_title_text}. ")

        #Screen Distance title
        expected_screen_distance_title_text=lang_settings["title"]
        actual_screen_distance_title_text=self.fc.fd["screen_distance"].verify_screen_distance_title_show()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_title.png".format(language))
        soft_assertion.assert_equal(actual_screen_distance_title_text, expected_screen_distance_title_text, f"Screen distance title text is not matching, expected string text is {expected_screen_distance_title_text}, but got {actual_screen_distance_title_text}. ")

        #screen distance tool tips
        self.fc.fd["screen_distance"].click_screen_distance_tootlips()
        expected_screen_distance_tooltips_text=lang_settings["tooltipsDescription"]
        actual_screen_distance_tooltips_text=self.fc.fd["screen_distance"].verify_screen_distance_tootlips()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_screen_distance_tooltips_text, expected_screen_distance_tooltips_text, f"Screen distance tool tips text is not matching, expected string text is {expected_screen_distance_tooltips_text}, but got {actual_screen_distance_tooltips_text}. ")

        if self.fc.fd["screen_distance"].verify_screen_distance_button_status() == "Off":
            expected_toggle_text=lang_settings["featureOff"]
            actual_toggle_text=self.fc.fd["screen_distance"].get_toggle_text()
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_toggle_off.png".format(language))
            soft_assertion.assert_equal(actual_toggle_text, expected_toggle_text, f"Screen distance toggle text is not matching, expected string text is {expected_toggle_text}, but got {actual_toggle_text}. ")
        else:
            expected_toggle_text=lang_settings["featureOn"]
            actual_toggle_text=self.fc.fd["screen_distance"].get_toggle_text()
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_toggle_on.png".format(language))
            soft_assertion.assert_equal(actual_toggle_text, expected_toggle_text, f"Screen distance toggle text is not matching, expected string text is {expected_toggle_text}, but got {actual_toggle_text}. ")
        
        #sitting to close subtitle text
        expected_subtitle_text=lang_settings["introDescription"]
        actual_subtitle_text=self.fc.fd["screen_distance"].verify_screen_distance_subtitle_show()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_subtitle.png".format(language))
        soft_assertion.assert_equal(actual_subtitle_text, expected_subtitle_text, f"Screen distance subtitle text is not matching, expected string text is {expected_subtitle_text}, but got {actual_subtitle_text}. ")
        
        #set toggle on
        if self.fc.fd["screen_distance"].verify_screen_distance_button_status() == "Off":
           self.fc.fs["screen_distance"].click_screen_distance_button()

        #Alert options title
        expected_alert_options_text=lang_settings["alertOptionsHeading"]
        actual_alert_options_text=self.fc.fd["screen_distance"].verify_alert_option_title_show()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_alert_options_title.png".format(language))
        soft_assertion.assert_equal(actual_alert_options_text, expected_alert_options_text, f"Alert options title text is not matching, expected string text is {expected_alert_options_text}, but got {actual_alert_options_text}. ")

        #Set Preferred distance text
        expected_set_preferred_distance_text=lang_settings["setDistanceHeading"]
        actual_set_preferred_distance_text=self.fc.fd["screen_distance"].verify_set_preferred_title_show()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_set_preferred_distance_title.png".format(language))
        soft_assertion.assert_equal(actual_set_preferred_distance_text, expected_set_preferred_distance_text, f"Set Preferred distance title text is not matching, expected string text is {expected_set_preferred_distance_text}, but got {actual_set_preferred_distance_text}. ")

        #set custom threshhold text
        expected_custom_threshhold_text=lang_settings["setDistanceDescription"]
        actual_custom_threshhold_text=self.fc.fd["screen_distance"].verify_set_preferred_subtitle_show()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_set_preferred_distance_subtitle.png".format(language))
        soft_assertion.assert_equal(actual_custom_threshhold_text, expected_custom_threshhold_text, f"Set custom threshhold text is not matching, expected string text is {expected_custom_threshhold_text}, but got {actual_custom_threshhold_text}. ")

        self.fc.swipe_window(direction="down", distance=4)
        #restore defaults settings text
        expected_restore_defaults_text=lang_settings["restoreText"]
        actual_restore_defaults_text=self.fc.fd["screen_distance"].verify_restore_button_show()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_restore_defaults.png".format(language))
        soft_assertion.assert_equal(actual_restore_defaults_text, expected_restore_defaults_text, f"Restore defaults settings text is not matching, expected string text is {expected_restore_defaults_text}, but got {actual_restore_defaults_text}. ")

        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/screendistanceLocalization.json", language, "pCSetScreenDistance")
        #change distance
        expected_change_distance_text=lang_settings["changeDistanceButton"]
        actual_change_distance_text=self.fc.fd["screen_distance"].verify_change_button_show()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_change_distance.png".format(language))
        soft_assertion.assert_equal(actual_change_distance_text, expected_change_distance_text, f"Change distance text is not matching, expected string text is {expected_change_distance_text}, but got {actual_change_distance_text}. ")

        #click on change distance
        self.fc.fd["screen_distance"].click_change_button()
        #Cancel
        expected_cancel_text=lang_settings["cancelButton"]
        actual_cancel_text=self.fc.fd["screen_distance"].get_cancel_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_cancel.png".format(language))
        soft_assertion.assert_equal(actual_cancel_text, expected_cancel_text, f"Cancel text is not matching, expected string text is {expected_cancel_text}, but got {actual_cancel_text}. ")

        #Save
        expected_save_text=lang_settings["saveButton"]
        actual_save_text=self.fc.fd["screen_distance"].get_save_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_save.png".format(language))
        soft_assertion.assert_equal(actual_save_text, expected_save_text, f"Save text is not matching, expected string text is {expected_save_text}, but got {actual_save_text}. ")

        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/screendistanceLocalization.json", language, "pCScreenDistanceAlertOptions")

        #Nudge card
        expected_nudge_card_text=lang_settings["nudgeMe"]
        actual_nudge_card_text=self.fc.fd["screen_distance"].get_nudge_text_on_card()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "screen_distance_screenshot/{}_screen_distance_nudge_card.png".format(language))
        soft_assertion.assert_equal(actual_nudge_card_text, expected_nudge_card_text, f"Nudge card text is not matching, expected string text is {expected_nudge_card_text}, but got {actual_nudge_card_text}. ")

        #nudge subtitle
        expected_nudge_subtitle_text=lang_settings["nudgeMeDescription"]
        actual_nudge_subtitle_text=self.fc.fd["screen_distance"].get_nudge_card_subtitle_text()
        soft_assertion.assert_equal(actual_nudge_subtitle_text, expected_nudge_subtitle_text, f"Nudge subtitle text is not matching, expected string text is {expected_nudge_subtitle_text}, but got {actual_nudge_subtitle_text}. ")

        #Alert card
        expected_alert_card_text=lang_settings["fullNotification"]
        actual_alert_card_text=self.fc.fd["screen_distance"].get_alert_text_on_card()
        soft_assertion.assert_equal(actual_alert_card_text, expected_alert_card_text, f"Alert card text is not matching, expected string text is {expected_alert_card_text}, but got {actual_alert_card_text}. ")

        #alert subtitle
        expected_alert_subtitle_text=lang_settings["fullNotificationDescription"]
        actual_alert_subtitle_text=self.fc.fd["screen_distance"].get_alert_card_subtitle_text()
        soft_assertion.assert_equal(actual_alert_subtitle_text, expected_alert_subtitle_text, f"Alert subtitle text is not matching, expected string text is {expected_alert_subtitle_text}, but got {actual_alert_subtitle_text}. ")

        #Blur card
        expected_blur_card_text=lang_settings["blurMyDisplay"]
        actual_blur_card_text=self.fc.fd["screen_distance"].get_blur_text_on_card()
        soft_assertion.assert_equal(actual_blur_card_text, expected_blur_card_text, f"Blur card text is not matching, expected string text is {expected_blur_card_text}, but got {actual_blur_card_text}. ")

        #Blur subtitle
        expected_blur_subtitle_text=lang_settings["blurMyDisplayDescription"]
        actual_blur_subtitle_text=self.fc.fd["screen_distance"].get_blur_card_subtitle_text()
        soft_assertion.assert_equal(actual_blur_subtitle_text, expected_blur_subtitle_text, f"Blur subtitle text is not matching, expected string text is {expected_blur_subtitle_text}, but got {actual_blur_subtitle_text}. ")

        #current set distance : inch ---remaining
        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()

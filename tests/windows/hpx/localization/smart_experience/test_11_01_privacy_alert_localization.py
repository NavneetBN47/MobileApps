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

@pytest.fixture(scope="session", params=["smartexp_privacy_alert_screenshot"])
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

    def test_01_smart_experience_privacy_alert_module_C34746740(self, language):
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

        #privacy alert card
        assert bool(self.fc.fd["devices"].verify_privacy_alert()) is True, "privacy alert card is not displayed."
        logging.info("privacy alert available")
        self.fc.fd["devices"].click_privacy_alert()
        soft_assertion.assert_true(bool(self.fc.fd["smart_experience"].verify_privacy_alert_title_visible()), "Privacy alert title is not displayed. ")
        #Privacy alert nav text
        expected_privacy_alert_nav_text=lang_settings["moduleTitlePA"]
        actual_privacy_alert_nav_text=self.fc.fd["smart_experience"].get_privacy_alert_nav_text()
        ma_misc.create_localization_screenshot_folder("smart_exp_privacy_alert_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "smart_exp_privacy_alert_screenshot/{}_smart_exp_privacy_alert_homepage.png".format(language))
        soft_assertion.assert_equal(actual_privacy_alert_nav_text, expected_privacy_alert_nav_text, f"Privacy alert nav text is not matching. expected string text is {expected_privacy_alert_nav_text}, but got {actual_privacy_alert_nav_text}. ")
        #please enable your camera to use HP smart
        if bool(self.fc.fd["smart_experience"].verify_please_text_visible()) is True:
            expected_please_enable_text=lang_settings["about"]["cameraObscured"]
            actual_please_enable_text=self.fc.fd["smart_experience"].get_please_text()
            soft_assertion.assert_equal(actual_please_enable_text, expected_please_enable_text, f"Please enable text is not matching. expected string text is {expected_please_enable_text}, but got {actual_please_enable_text}. ")
        else:
            logging.info("please enable text not displayed")
        #Privacy Alert title
        expected_privacy_alert_title_text=lang_settings["shoulderSurf"]["title"]
        actual_privacy_alert_title_text=self.fc.fd["smart_experience"].verify_privacy_alert_title()
        soft_assertion.assert_equal(actual_privacy_alert_title_text, expected_privacy_alert_title_text, f"Privacy alert title text is not matching. expected string text is {expected_privacy_alert_title_text}, but got {actual_privacy_alert_title_text}. ")
        #privacy alert tool tip
        self.fc.fd["smart_experience"].click_privacy_alert_tool_tip()
        expected_tool_tip_text=lang_settings["toolTipMessage"]
        actual_tool_tip_text=self.fc.fd["smart_experience"].get_privacy_alert_tool_tip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "smart_exp_privacy_alert_screenshot/{}_smart_exp_privacy_alert_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_tool_tip_text, expected_tool_tip_text, f"Tooltips text is not matching. expected string text is {expected_tool_tip_text}, but got {actual_tool_tip_text}. ") 
        #toggle on in privacy alert title
        state=self.fc.fd["smart_experience"].verify_privacy_alert_btn_status()
        if (state=='1'):
            self.fc.fd["smart_experience"].click_privacy_alert_toggle_on()
            self.fc.fd["smart_experience"].click_privacy_alert_toggle_on()
        else:
            self.fc.fd["smart_experience"].click_privacy_alert_toggle_on()
        #privacy alert title
        expected_privacy_alert_title=lang_settings["shoulderSurf"]["title"]
        actual_privacy_alert_title=self.fc.fd["smart_experience"].get_privacy_alert_popup_title_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "smart_exp_privacy_alert_screenshot/{}_smart_exp_privacy_alert_pop_window.png".format(language))
        soft_assertion.assert_equal(actual_privacy_alert_title, expected_privacy_alert_title, f"Privacy alert title is not matching. expected string text is {expected_privacy_alert_title}, but got {actual_privacy_alert_title}. ")
        #privacy alert description text on popup
        expected_privacy_popup_des_text=lang_settings["cameraAccessModal"]["description"]
        actual_privacy_popup_des_text=self.fc.fd["smart_experience"].get_privacy_alert_description_on_popup()
        soft_assertion.assert_equal(actual_privacy_popup_des_text, expected_privacy_popup_des_text, f"Popup des text is not matching. expected string text is {expected_privacy_popup_des_text}, but got {actual_privacy_popup_des_text}. ")
        self.fc.fd["smart_experience"].click_do_not_show_privacy_chkbox()
        #Do not show again
        expected_do_not_show_again_text=lang_settings["cameraAccessModal"]["checkMessage"]
        actual_do_not_show_again_text=self.fc.fd["smart_experience"].get_do_not_show_text()
        soft_assertion.assert_equal(actual_do_not_show_again_text, expected_do_not_show_again_text, f"Show again text is not matching. expected string text is {expected_do_not_show_again_text}, but got {actual_do_not_show_again_text}. ")
        #hp privacy statement
        expected_hp_privacy_statement_text=lang_settings["cameraAccessModal"]["privacyStatement"]
        hp_privacy_statement_text=self.fc.fd["smart_experience"].get_hp_privacy_statement_text()
        actual_hp_privacy_statement_text=hp_privacy_statement_text.strip()
        logging.info("ac="+str(actual_hp_privacy_statement_text))
        soft_assertion.assert_equal(actual_hp_privacy_statement_text, expected_hp_privacy_statement_text, f"Hp privacy statement text is not matching. expected string text is {expected_hp_privacy_statement_text}, but got {actual_hp_privacy_statement_text}. ")
        #cancel
        expected_cancel_text=lang_settings["cameraAccessModal"]["cancel"]
        actual_cancel_text=self.fc.fd["smart_experience"].get_cancle_btn_on_popup()
        soft_assertion.assert_equal(actual_cancel_text, expected_cancel_text, f"Cancel text is not matching. expected string text is {expected_cancel_text}, but got {actual_cancel_text}. ")
        #continue
        expected_continue_text=lang_settings["welcomeModal"]["continue"]
        actual_continue_text=self.fc.fd["smart_experience"].get_continue_btn_on_popup()
        soft_assertion.assert_equal(actual_continue_text, expected_continue_text, f"Continue text is not matching. expected string text is {expected_continue_text}, but got {actual_continue_text}. ")
        #click continue
        self.fc.fd["smart_experience"].click_continue_on_popup()
        #privacy description text
        expected_description_text=lang_settings["shoulderSurf"]["description"]
        actual_description_text=self.fc.fd["smart_experience"].verify_privacy_alert_subtitle()
        soft_assertion.assert_equal(actual_description_text, expected_description_text, f"Privacy description text is not matching. expected string text is {expected_description_text}, but got {actual_description_text}. ")
        #snooze duration
        expected_snooze_duration=lang_settings["shoulderSurf"]["snoozeDuration"]
        actual_snooze_duration=self.fc.fd["smart_experience"].verify_snooze_duration_title()
        soft_assertion.assert_equal(actual_snooze_duration, expected_snooze_duration, f"Snooze duration text is not matching. expected string text is {expected_snooze_duration}, but got {actual_snooze_duration}. ")
        #click dd on snooze duration
        self.fc.fd["smart_experience"].click_snooze_duration_dd()
        #5 min
        expected_5_min_text=lang_settings["snoozeOptions"]["fiveMins"]
        actual_5_min_text=self.fc.fd["smart_experience"].get_five_minutes()
        logging.info("actual_5_min_text: {}".format(actual_5_min_text))
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "smart_exp_privacy_alert_screenshot/{}_smart_exp_privacy_alert_snooze_duration.png".format(language))
        if language == "lv":
            actual_5_min_text = actual_5_min_text.replace("5 minūtes","5 minūtes")
        logging.info("actual_5_min_text if lang lv: {}".format(actual_5_min_text))
        logging.info("expected_5_min_text: {}".format(expected_5_min_text))
        soft_assertion.assert_equal(actual_5_min_text, expected_5_min_text, f"5 minutes text is not matching. expected string text is {expected_5_min_text}, but got {actual_5_min_text}. ")
        #10 min
        expected_10_min_text=lang_settings["snoozeOptions"]["tenMins"]
        actual_10_min_text=self.fc.fd["smart_experience"].get_ten_minutes()
        soft_assertion.assert_equal(actual_10_min_text, expected_10_min_text, f"10 minutes text is not matching. expected string text is {expected_10_min_text}, but got {actual_10_min_text}. ")
        #30 min
        expected_30_min_text=lang_settings["snoozeOptions"]["thirtyMins"]
        actual_30_min_text=self.fc.fd["smart_experience"].get_thirty_minutes()
        soft_assertion.assert_equal(actual_30_min_text, expected_30_min_text, f"30 minutes text is not matching. expected string text is {expected_30_min_text}, but got {actual_30_min_text}. ")
        #1 hour
        expected_1_hour_text=lang_settings["snoozeOptions"]["oneHour"]
        actual_1_hour_text=self.fc.fd["smart_experience"].get_one_hour()
        soft_assertion.assert_equal(actual_1_hour_text, expected_1_hour_text, f"1 hour text is not matching. expected string text is {expected_1_hour_text}, but got {actual_1_hour_text}. ")
        #end of the day
        expected_end_of_the_day_text=lang_settings["snoozeOptions"]["endOfTheDay"]
        actual_end_of_the_day_text=self.fc.fd["smart_experience"].get_end_of_day()
        soft_assertion.assert_equal(actual_end_of_the_day_text, expected_end_of_the_day_text, f"End of day text is not matching. expected string text is {expected_end_of_the_day_text}, but got {actual_end_of_the_day_text}. ")
        self.fc.fd["smart_experience"].click_snooze_duration_dd()
        #restore default settings
        expected_restore_default_settings_text=lang_settings["resetToDefaultButton"]["title"]
        actual_restore_default_settings_text=self.fc.fd["smart_experience"].verify_privacy_alert_restoreBtn()
        soft_assertion.assert_equal(actual_restore_default_settings_text, expected_restore_default_settings_text, f"Restore default settings text is not matching. expected string text is {expected_restore_default_settings_text}, but got {actual_restore_default_settings_text}. ")
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        soft_assertion.raise_assertion_errors()

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

@pytest.fixture(scope="session", params=["smartexp_auto_dimming_screenshot"])
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
        
    def test_02_smart_experience_auto_screen_dimming_module_C34746741(self, language):
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

        #Auto screen dimming card
        assert bool(self.fc.fd["devices"].verify_auto_screen_dimming()) is True, "auto screen dimming card is not displayed."
        logging.info("Auto screen dimming available")
        self.fc.fd["devices"].click_auto_screen_dimming()
        #Auto screen dimming nav title
        expected_auto_screen_dimming_nav_title_text=lang_settings["moduleTitleASD"]
        actual_auto_screen_dimming_nav_title_text=self.fc.fd["smart_experience"].get_auto_screen_dimming_nav_title()
        ma_misc.create_localization_screenshot_folder("smart_exp_auto_dimming_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "smart_exp_auto_dimming_screenshot/{}_smart_exp_auto_dimming_homepage.png".format(language))
        soft_assertion.assert_equal(actual_auto_screen_dimming_nav_title_text, expected_auto_screen_dimming_nav_title_text, f"Auto screen dimming nav title is not matching. expected string text is {expected_auto_screen_dimming_nav_title_text}, but got {actual_auto_screen_dimming_nav_title_text}. ")
        #Auto Screen Dimming title
        expected_auto_screen_dimming_text=lang_settings["attentionDim"]["title"]
        actual_auto_screen_dimming_text=self.fc.fd["smart_experience"].get_auto_screen_dimming_text()
        soft_assertion.assert_equal(actual_auto_screen_dimming_text, expected_auto_screen_dimming_text, f"Auto screen dimming title is not matching. expected string text is {expected_auto_screen_dimming_text}, but got {actual_auto_screen_dimming_text}. ")
        #Auto screen dimming tool tip
        self.fc.fd["smart_experience"].click_on_auto_screen_dimming_tooltip()
        expected_tooltip_text=lang_settings["toolTipMessage"]
        actual_tooltip_text=self.fc.fd["smart_experience"].get_auto_screen_dimming_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "smart_exp_auto_dimming_screenshot/{}_smart_exp_auto_dimming_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_tooltip_text, expected_tooltip_text, f"Tooltips title is not matching. expected string text is {expected_tooltip_text}, but got {actual_tooltip_text}. ")
        #toggle on in privacy alert title
        state=self.fc.fd["smart_experience"].verify_auto_screen_dimming_btn_status()
        if(state=='1'):
            self.fc.fd["smart_experience"].click_toggle_switch_auto_dimming_popup()
            self.fc.fd["smart_experience"].click_toggle_switch_auto_dimming_popup()
        else:
            self.fc.fd["smart_experience"].click_toggle_switch_auto_dimming_popup()
        #Auto screen Dimming popup
        #Auto screen Dimming title
        expected_auto_screen_dimming_title=lang_settings["attentionDim"]["title"]
        actual_auto_screen_dimming_title=self.fc.fd["smart_experience"].get_privacy_alert_popup_title_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "smart_exp_auto_dimming_screenshot/{}_smart_exp_auto_dimming_pop_window.png".format(language))
        soft_assertion.assert_equal(actual_auto_screen_dimming_title, expected_auto_screen_dimming_title, f"Auto screen dimming title is not matching. expected string text is {expected_auto_screen_dimming_title}, but got {actual_auto_screen_dimming_title}. ")
        #des text on popup
        expected_des_text=lang_settings["cameraAccessModal"]["description"]
        actual_des_text=self.fc.fd["smart_experience"].get_privacy_alert_description_on_popup()
        soft_assertion.assert_equal(actual_des_text, expected_des_text, f"Auto screen dimming des text is not matching. expected string text is {expected_des_text}, but got {actual_des_text}. ")
        self.fc.fd["smart_experience"].click_do_not_show_dimming_chkbox()
        #Do not show again
        expected_do_not_show_text=lang_settings["cameraAccessModal"]["checkMessage"]
        actual_do_not_show_text=self.fc.fd["smart_experience"].get_do_not_show_text()
        soft_assertion.assert_equal(actual_do_not_show_text, expected_do_not_show_text, f"Do not show text is not matching. expected string text is {expected_do_not_show_text}, but got {actual_do_not_show_text}. ")
        #hp privacy link
        expected_privacy_link_text=lang_settings["cameraAccessModal"]["privacyStatement"]
        privacy_link_text=self.fc.fd["smart_experience"].get_hp_privacy_link_btn_on_popup()
        actual_privacy_link_text=privacy_link_text.strip()
        soft_assertion.assert_equal(actual_privacy_link_text, expected_privacy_link_text, f"Privacy link text is not matching. expected string text is {expected_privacy_link_text}, but got {actual_privacy_link_text}. ")
        #cancel
        expected_cancel_text=lang_settings["cameraAccessModal"]["cancel"]
        actual_cancel_text=self.fc.fd["smart_experience"].get_cancel_btn_auto_screen_dimming_popup()
        soft_assertion.assert_equal(actual_cancel_text, expected_cancel_text, f"Cancel text is not matching. expected string text is {expected_cancel_text}, but got {actual_cancel_text}. ")
        #continue
        expected_continue_text=lang_settings["welcomeModal"]["continue"]
        actual_continue_text=self.fc.fd["smart_experience"].get_continue_btn_auto_screen_dimming_popup()
        soft_assertion.assert_equal(actual_continue_text, expected_continue_text, f"Continue text is not matching. expected string text is {expected_continue_text}, but got {actual_continue_text}. ")
        #click cancel btn
        self.fc.fd["smart_experience"].click_auto_screen_dimming_dialogue_cancel_btn()
        #Description text
        expected_des_text=lang_settings["attentionDim"]["description"]
        actual_des_text=self.fc.fd["smart_experience"].get_auto_screen_dimming_des_text()
        soft_assertion.assert_equal(actual_des_text, expected_des_text, f"Description text is not matching. expected string text is {expected_des_text}, but got {actual_des_text}. ")
        #Disable when connected to an external
        expected_disable_checkbox_text=lang_settings["txtExternalMonitor"]
        actual_disable_checkbox_text=self.fc.fd["smart_experience"].get_disable_checkbox_text()
        soft_assertion.assert_equal(actual_disable_checkbox_text, expected_disable_checkbox_text, f"Disable checkbox text is not matching. expected string text is {expected_disable_checkbox_text}, but got {actual_disable_checkbox_text}. ")
        #restore defaults
        expected_restore_defaults_text=lang_settings["resetToDefaultButton"]["title"]
        actual_restore_default_text=self.fc.fd["smart_experience"].get_auto_screen_dimming_restore_btn()
        soft_assertion.assert_equal(actual_restore_default_text, expected_restore_defaults_text, f"Restore defaults text is not matching. expected string text is {expected_restore_defaults_text}, but got {actual_restore_default_text}. ")
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        soft_assertion.raise_assertion_errors()

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

@pytest.fixture(scope="session", params=["display_control_screenshot"])
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


    # only support on willie and grogu
    def test_06_displaycontrol_module_C33045042(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/displaycontrolLocalization.json", language, "pCDisplay")
        general_lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/generalLocalization.json", language, "installedapps")
        display_context_aware_lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/displaycontrolcontextawareLocalization.json", language, "appBarSetting")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        self.fc.fd["devices"].click_display_control_card_pcdevice()
        # display
        expected_display_title_text = lang_settings["moduleTitle"]
        actual_display_title_text = self.fc.fd["display_control"].get_display_title_text()
        ma_misc.create_localization_screenshot_folder("display_control_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_homepage01.png".format(language))
        soft_assertion.assert_equal(actual_display_title_text, expected_display_title_text, f"Display control title text is not matching, expected string text is {expected_display_title_text}, but got {actual_display_title_text}. ")
       # Brightness & Contrast
        expected_brightness_text = lang_settings["brightnesscontrast"]
        actual_brightness_text = self.fc.fd["display_control"].verify_brightness_contrast_label()
        soft_assertion.assert_equal(actual_brightness_text, expected_brightness_text, f"Brightness & contrast text is not matching, expected string text is {expected_brightness_text}, but got {actual_brightness_text}. ")
        # Display modes
        expected_display_modes_text = lang_settings["displaymodes"]
        actual_display_modes_text = self.fc.fd["display_control"].verify_display_modes_title()
        soft_assertion.assert_equal(actual_display_modes_text, expected_display_modes_text, f"Display modes text is not matching, expected string text is {expected_display_modes_text}, but got {actual_display_modes_text}. ")
        assert bool(self.fc.fd["display_control"].verify_standard_mode()) is True, "Standard mode not available."
        logging.info("Standard mode available")
        # Standard
        expected_stadard_text = lang_settings["standardmodes"]
        actual_standard_text = self.fc.fd["display_control"].verify_standard_title()
        soft_assertion.assert_equal(actual_standard_text, expected_stadard_text, f"Standard text is not matching, expected string text is {expected_stadard_text}, but got {actual_standard_text}. ")
        # Default
        assert bool(self.fc.fd["display_control"].verify_default_mode()) is True, "Default mode not available."
        logging.info("Default Mode available")
        expected_default_text = lang_settings["default"]
        actual_default_text = self.fc.fd["display_control"].verify_default_tile()
        soft_assertion.assert_equal(actual_default_text, expected_default_text, f"Default text is not matching, expected string text is {expected_default_text}, but got {actual_default_text}. ")
        # Work
        assert bool(self.fc.fd["display_control"].verify_work_mode()) is True, "Work mode not available."
        logging.info("Work mode available")
        expected_work_text = lang_settings["work"]
        actual_work_text = self.fc.fd["display_control"].verify_work_tile()
        soft_assertion.assert_equal(actual_work_text, expected_work_text, f"Work text is not matching, expected string text is {expected_work_text}, but got {actual_work_text}. ")
        self.driver.swipe(direction="down", distance=1)
        # Low Light
        assert bool(self.fc.fd["display_control"].verify_low_light_mode()) is True, "Low light mode not available."
        logging.info("light mode available")
        expected_low_light_text = lang_settings["lowlighing"]
        actual_low_light_text = self.fc.fd["display_control"].verify_low_light_tile()
        soft_assertion.assert_equal(actual_low_light_text, expected_low_light_text, f"Low Light text not matching, expected string text is {expected_low_light_text}, but got {actual_low_light_text}. ")
        # Entertainment
        assert bool(self.fc.fd["display_control"].verify_entertainment_mode()) is True, "Entertainment mode not availbale."
        logging.info("Enterainment mode available")
        expected_entertainment_text = lang_settings["entertainment"]
        actual_entertainment_text = self.fc.fd["display_control"].verify_entertainment_tile()
        soft_assertion.assert_equal(actual_entertainment_text, expected_entertainment_text, f"Entertaiment text is not matching, expected string text is {expected_entertainment_text}, but got {actual_entertainment_text}. ")
        # Low blue light
        assert bool(self.fc.fd["display_control"].verify_low_blue_light_mode()) is True, "Low blue light mode not available."
        logging.info("Low blue light Mode available")
        expected_low_blue_light_text = lang_settings["lowbluelight"]
        actual_low_blue_light = self.fc.fd["display_control"].verify_low_blue_light_tile()
        soft_assertion.assert_equal(actual_low_blue_light, expected_low_blue_light_text, f"Low blue light text is not matching, expected string text is {expected_low_blue_light_text}, but got {actual_low_blue_light}. ")
        # Advanced
        assert bool(self.fc.fd["display_control"].verify_advanced_mode()) is True, "Advanced mode not available."
        logging.info("Advanced mode available")
        expected_advanced_text = lang_settings["advancedmodes"]
        actual_advanced_text = self.fc.fd["display_control"].verify_advanced_title()
        soft_assertion.assert_equal(actual_advanced_text, expected_advanced_text, f"Advanced text is not matching, expected string text is {expected_advanced_text}, but got {actual_advanced_text}. ")
        # sRGB (Web)
        assert bool(self.fc.fd["display_control"].verify_sRGB_mode()) is True, "sRGB mode not available."
        logging.info("sRGB mode available")
        expected_srgb_text = lang_settings["srgb"]
        actual_srgb_text = self.fc.fd["display_control"].verify_sRGB_web_tile()
        soft_assertion.assert_equal(actual_srgb_text, expected_srgb_text, f"sRGB text is not matching, expected string text is {expected_srgb_text}, but got {actual_srgb_text}. ")
        # Adobe RGB(Printing and Imaging)
        assert bool(self.fc.fd["display_control"].verify_adobe_RGB_mode()) is True, "Adobe RGB (Printing and Imaging) mode not available."
        logging.info("Adobe RGB mode available")
        expected_adobe_rgb_text = lang_settings["adobergb"]
        actual_adobe_rgb_text = self.fc.fd["display_control"].get_adobe_rgb_text()
        soft_assertion.assert_equal(actual_adobe_rgb_text, expected_adobe_rgb_text, f"Adobe RGB(Printing and Imaging) text is not matching, expected string text is {expected_adobe_rgb_text}, but got {actual_adobe_rgb_text}. ")
        # Display P3(Photo and Video)
        assert bool(self.fc.fd["display_control"].verify_display_p3_mode()) is True, "Display P3 (Photo and Video) mode not available."
        logging.info("Display P3 mode available")
        expected_display_p_text = lang_settings["displayp3"]
        actual_display_p_text = self.fc.fd["display_control"].verify_display_p3__tile()
        soft_assertion.assert_equal(actual_display_p_text, expected_display_p_text, f"Display P3(Photo and Video) text is not matching, expected string text is {expected_display_p_text}, but got {actual_display_p_text}. ")
        # Native
        self.driver.swipe(direction="down", distance=1)
        assert bool(self.fc.fd["display_control"].verify_native_mode_tile) is True, "Native mode not available."
        logging.info("Native mode tile available")
        expected_native_text = lang_settings["native"]
        actual_native_text = self.fc.fd["display_control"].verify_native_tile()
        soft_assertion.assert_equal(actual_native_text, expected_native_text, f"Display P3(Photo and Video) text is not matching, expected string text is {expected_native_text}, but got {actual_native_text}. ")
        # Restore defaults
        assert bool(self.fc.fd["display_control"].verify_restore_defaults_btn()) is True, "Restore Defaults button not available."
        expected_restore_defaults_text = lang_settings["restoreDefaultsButton"]
        actual_restore_defaults_text = self.fc.fd["display_control"].verify_restore_default_button()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_restoreToDefaultSettings.png".format(language))
        soft_assertion.assert_equal(actual_restore_defaults_text, expected_restore_defaults_text, f"Restore Defaults text is not matching, expected string text is {expected_restore_defaults_text}, but got {actual_restore_defaults_text}. ")
        self.driver.swipe(direction="up", distance=2)
        #verify advanced settings
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings not availble."
        logging.info("Advanced setting available")
        # click advanced setting on top right
        self.fc.fd["display_control"].click_advaced_setting()
        # Advanced setting title
        expected_advanced_setting_title_text = lang_settings["advancedSetting"]
        actual_advanced_setting_title_text = self.fc.fd["display_control"].verify_advanced_settings_title()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_advanced_setting.png".format(language))
        soft_assertion.assert_equal(actual_advanced_setting_title_text, expected_advanced_setting_title_text, f"Advanced setting title text is not matching, expected string text is {expected_advanced_setting_title_text}, but got {actual_advanced_setting_title_text}. ")
        # Low blue light text
        expected_low_blue_light_text = lang_settings["lowbluelight"]
        actual_low_blue_light_text = self.fc.fd["display_control"].verify_low_blue_light_text()
        soft_assertion.assert_equal(actual_low_blue_light_text, expected_low_blue_light_text, f"Low blue light text is not matching, expected string text is {expected_low_blue_light_text}, but got {actual_low_blue_light_text}. ")
        # low blue light toggle text
        self.fc.fd["display_control"].click_low_blue_light_toggle()
        expected_low_blue_light_toggle_text = lang_settings["lowBlueLightTooltip"]
        actual_low_blue_light_toggle_text = self.fc.fd["display_control"].verify_low_blue_light_toggle_text()
        soft_assertion.assert_equal(actual_low_blue_light_toggle_text, expected_low_blue_light_toggle_text, f"Low blue light toggle text is not matching, expected string text is {expected_low_blue_light_toggle_text}, but got {actual_low_blue_light_toggle_text}. ")
        #click toggle to set as on
        toggle_state=self.fc.fd["display_control"].get_toggle_of_low_blue_light()
        if (toggle_state == '0'):
            self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        # turn on text
        expected_turnon_text = lang_settings["turnon"]
        actual_turnon_text = self.fc.fd["display_control"].get_turn_on_advanced_settings()
        soft_assertion.assert_equal(actual_turnon_text, expected_turnon_text, f"Turn on text is not matching, expected string text is {expected_turnon_text}, but got {actual_turnon_text}. ")
        #click turn on am/pm combo text
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        #am text
        expected_turn_on_am_text=lang_settings["am"]
        actual_turn_on_am_text=self.fc.fd["display_control"].verify_turn_on_am_text()
        soft_assertion.assert_equal(actual_turn_on_am_text, expected_turn_on_am_text, f"am text is not matching, expected string text is {expected_turn_on_am_text}, but got {actual_turn_on_am_text}. ")
        #pm text
        expected_turn_on_pm_text=lang_settings["pm"]
        actual_turn_on_pm_text=self.fc.fd["display_control"].verify_turn_on_pm_text()
        soft_assertion.assert_equal(actual_turn_on_pm_text, expected_turn_on_pm_text, f"pm text is not matching, expected string text is {expected_turn_on_pm_text}, but got {actual_turn_on_pm_text}. ")
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        # turn off
        expected_turn_off_text = lang_settings["turnoff"]
        actual_turn_off_text = self.fc.fd["display_control"].get_turn_off_advanced_settings()
        soft_assertion.assert_equal(actual_turn_off_text, expected_turn_off_text, f"Turn off text is not matching, expected string text is {expected_turn_off_text}, but got {actual_turn_off_text}. ")
        #click turn off am/pm combo
        self.fc.fd["display_control"].click_turn_off_combo_advanced_settings()
        #turn off am text
        expected_turn_off_am_text=lang_settings["am"]
        actual_turn_off_am_text=self.fc.fd["display_control"].verify_turn_off_am_text()
        soft_assertion.assert_equal(actual_turn_off_am_text, expected_turn_off_am_text, f"Turn off am text is not matching, expected string text is {expected_turn_off_am_text}, but got {actual_turn_off_am_text}. ")
        #turn off pm text
        expected_turn_off_pm_text=lang_settings["pm"]
        actual_turn_off_pm_text=self.fc.fd["display_control"].verify_turn_off_pm_text()
        soft_assertion.assert_equal(actual_turn_off_pm_text, expected_turn_off_pm_text, f"Turn off pm text is not matching, expected string text is {expected_turn_off_pm_text}, but got {actual_turn_off_pm_text}. ")
        self.fc.fd["display_control"].click_turn_off_combo_advanced_settings()
        #click "x" to close advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        #add application
        expected_add_application_text=display_context_aware_lang_settings["addApplication"]
        actual_add_application_text=self.fc.fd["display_control"].verify_add_application_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_add_application_window.png".format(language))
        soft_assertion.assert_equal(actual_add_application_text, expected_add_application_text, f"Add application text is not matching, expected string text is {expected_add_application_text}, but got {actual_add_application_text}. ")
        #click add application btn
        self.fc.fd["display_control"].click_add_application_btn()
        time.sleep(2)
        #verify add application window display or not
        assert bool(self.fc.fd["display_control"].verify_applications_display()) is True, "Add Applications window not popup." 
        #Applications
        expected_applications_text=general_lang_settings["applications"]
        actual_applications_text=self.fc.fd["display_control"].verify_applications_text()
        soft_assertion.assert_equal(actual_applications_text,expected_applications_text,f"applications text is not matching, expected string text is {expected_applications_text}, but got {actual_applications_text}. ")
        #search application
        expected_search_application_text=general_lang_settings["searchApplication"]
        actual_search_application_text=self.fc.fd["display_control"].verify_search_application_text()
        soft_assertion.assert_equal(actual_search_application_text,expected_search_application_text,f"search applications text is not matching, expected string text is {expected_search_application_text}, but got {actual_search_application_text}. ")
        #cancel text
        expected_cancel_text=general_lang_settings["cancel"]
        actual_cancel_text=self.fc.fd["display_control"].verify_cancel_text()
        soft_assertion.assert_equal(actual_cancel_text,expected_cancel_text,f"cancel button text is not matching, expected string text is {expected_cancel_text}, but got {actual_cancel_text}. ")
        #select an application from list then add
        self.fc.fd["display_control"].click_app_in_app_list()
        #add button text
        expected_add_text=general_lang_settings["add"]
        actual_add_text=self.fc.fd["display_control"].verify_add_btn_text()
        soft_assertion.assert_equal(actual_add_text,expected_add_text,f"add button text is not matching, expected string text is {expected_add_text}, but got {actual_add_text}. ")
        #click add button
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_add_btn.png".format(language))
        self.fc.fd["display_control"].click_add_btn()
        self.driver.swipe(direction="down", distance=1)
        #restore to global settings
        # expected_restore_global_settings_text=lang_settings["restoreToGlobalSettings"]
        # actual_restore_global_text=self.fc.fd["display_control"].verify_restore_default_button()
        # self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_restore to global settings.png".format(language))
        # soft_assertion.assert_equal(actual_restore_global_text,expected_restore_global_settings_text,f"restore to global settings text is not matching, expected string text is {expected_restore_global_settings_text}, but got {actual_restore_global_text}. ")
        #click on added application
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_added_app_click.png".format(language))
        self.driver.swipe(direction="up", distance=1)
        self.fc.fd["display_control"].hover_added_app()
        #verify delete or "x" button displayed or not
        if (bool(self.fc.fd["display_control"].verify_delete_disney_plus_app_display()) is True):
            self.fc.fd["display_control"].click_delete_disney_plus_app()
        else:
            self.fc.fd["display_control"].click_access_app_delete_button()
        time.sleep(2)
        #verify delete app setting window display or not
        assert bool(self.fc.fd["display_control"].verify_delete_app_setting_window()) is True, "Delete app setting window not displayed"
        #delete app setting
        expected_delete_app_setting_text=display_context_aware_lang_settings["deleteModalTitle"]
        actual_delete_app_setting_text=self.fc.fd["display_control"].verify_delete_app_setting()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_delete_app_setting_window.png".format(language))
        soft_assertion.assert_equal(actual_delete_app_setting_text,expected_delete_app_setting_text,f"Delete app setting text is not matching, expected string text is {expected_delete_app_setting_text}, but got {actual_delete_app_setting_text}. ")
        #Are you sure you want to remove this app configuration?
        expected_delete_app_setting_sub_title_text=display_context_aware_lang_settings["deleteModalDescription"]
        actual_delete_app_setting_sub_title_text=self.fc.fd["display_control"].verify_delete_app_setting_sub_title()
        soft_assertion.assert_equal(actual_delete_app_setting_sub_title_text,expected_delete_app_setting_sub_title_text,f"Delete app setting sub title text is not matching, expected string text is {expected_delete_app_setting_sub_title_text}, but got {actual_delete_app_setting_sub_title_text}. ")
        #Do not show again text
        expected_do_not_show_again_text=display_context_aware_lang_settings["deleteModalCheckBoxText"]
        actual_do_not_show_again_text=self.fc.fd["display_control"].verify_do_not_show_again()
        soft_assertion.assert_equal(actual_do_not_show_again_text,expected_do_not_show_again_text,f"Do not show again text is not matching, expected string text is {expected_do_not_show_again_text}, but got {actual_do_not_show_again_text}. ")
        #cancel text on delete app setting window
        expected_cancel_on_delete_app_setting_text=lang_settings["cancel"]
        actual_cancel_on_delete_app_setting_text=self.fc.fd["display_control"].verify_cancel_on_delete_app_setting()
        soft_assertion.assert_equal(actual_cancel_on_delete_app_setting_text,expected_cancel_on_delete_app_setting_text,f"cancel on delete app setting text is not matching, expected string text is {expected_cancel_on_delete_app_setting_text}, but got {actual_cancel_on_delete_app_setting_text}. ")
        #continue text on delete app setting
        expected_continue_on_delete_app_setting=lang_settings["continue"]
        actual_continue_on_delete_app_setting_text=self.fc.fd["display_control"].verify_continue_on_delete_app_setting()
        soft_assertion.assert_equal(actual_continue_on_delete_app_setting_text,expected_continue_on_delete_app_setting,f"continue on delete app setting text is not matching, expected string text is {expected_continue_on_delete_app_setting}, but got {actual_continue_on_delete_app_setting_text}. ")
        #click "x" to close app setting window
        self.fc.fd["display_control"].click_cancel_on_delete_app_setting()
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
        soft_assertion.raise_assertion_errors()

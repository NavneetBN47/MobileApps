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


    def test_06_displaycontrol_module_C37210024(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/displaycontrolLocalization.json", language, "pCDisplay")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        time.sleep(4)
        self.fc.fd["devices"].click_display_control_card_pcdevice()
        #Display control nav text
        expected_display_title_text=lang_settings["moduleTitle"]
        actual_display_title_text = self.fc.fd["display_control"].get_display_title_text()
        ma_misc.create_localization_screenshot_folder("display_control_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_homepage01.png".format(language))
        assert actual_display_title_text == expected_display_title_text, "Display control title text is not matched"
        #Brightness & contrast
        expected_brightness_contrast_text=lang_settings["brightnesscontrast"]
        actual_brightness_text = self.fc.fd["display_control"].verify_brightness_contrast_label()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_homepage01.png".format(language))
        assert actual_brightness_text == expected_brightness_contrast_text, "Brightness & contrast text is not matched"
        #Display modes
        expected_display_modes_text=lang_settings["displaymodes"]
        actual_display_modes_text = self.fc.fd["display_control"].verify_display_modes_title()
        assert actual_display_modes_text == expected_display_modes_text, "Display modes text is not matched"
        #Neutral
        expected_neutral_text=lang_settings["neutralMode"]
        actual_neutral_text=self.fc.fd["display_control"].verify_natural_mode_title()
        actual_neutral_text == expected_neutral_text, "Neutral text is not matched"
        #Gaming
        expected_gaming_text=lang_settings["gaming"]
        actual_gaming_text=self.fc.fd["display_control"].verify_game_mode_title()
        actual_gaming_text == expected_gaming_text, "Gaming text is not matched"
        #Reading
        expected_reading_text=lang_settings["reading"]
        actual_reading_text=self.fc.fd["display_control"].verify_reading_mode_title()
        actual_reading_text == expected_reading_text, "Reading text is not matched"
        #Night
        expected_night_text=lang_settings["night"]
        actual_night_text=self.fc.fd["display_control"].verify_night_mode_title()
        actual_night_text == expected_night_text, "Night text is not matched"
        #Movie
        expected_movie_text=lang_settings["movie"]
        actual_movie_text=self.fc.fd["display_control"].verify_movie_mode_title()
        actual_movie_text == expected_movie_text, "Movie text is not matched"
        #HP Enhance+
        expected_hp_enhanced_text=lang_settings["hpenhanceplus"]
        actual_hp_enhanced_text=self.fc.fd["display_control"].verify_enhanceplus_mode_title()
        actual_hp_enhanced_text == expected_hp_enhanced_text, "HP Enhance+ text is not matched"
        #Native 
        expected_native_text=lang_settings["native"]
        actual_native_text = self.fc.fd["display_control"].get_native_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_homepage01.png".format(language))
        assert actual_native_text == expected_native_text, "Native text is not matched"
        #Restore Defaults
        expected_restore_defaults=lang_settings["restoreDefaultsButton"]
        actual_restore_defaults_text = self.fc.fd["display_control"].verify_restore_default_button()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_homepage02.png".format(language))
        assert actual_restore_defaults_text == expected_restore_defaults, "Restore Defaults text is not matched"
        #click enhance settings at top right corner
        self.fc.fd["display_control"].click_advaced_setting()
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced setting window is not available"
        logging.info("advanced setting window available")
        #Advanced Settings
        expected_advanced_settings_text=lang_settings["advancedSetting"]
        actual_advanced_setting_title_text = self.fc.fd["display_control"].verify_advanced_settings_title()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_advanced_setting.png".format(language))
        assert actual_advanced_setting_title_text == expected_advanced_settings_text, "Advanced setting title text is not matched"
        #Use HDMI Input
        expected_use_hdmi_input_text=lang_settings["useHdmiInput"]
        actual_use_hdmi_input_text=self.fc.fd["display_control"].get_use_hdmi_input()
        actual_use_hdmi_input_text == expected_use_hdmi_input_text, "Use HDMI Input text is not matched"
        #tool tip of use hdmi input
        self.fc.fd["display_control"].click_use_hdmi_input_tooltip()
        expected_tooltip_use_hdmi_input_text=lang_settings["useHdmiInputTooltip"]
        actual_tooltip_use_hdmi_input_text=self.fc.fd["display_control"].get_use_hdmi_input_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_use_hdmi_tooltip.png".format(language))
        actual_tooltip_use_hdmi_input_text == expected_tooltip_use_hdmi_input_text, "Use HDMI Input tooltip text is not matched"
        #Switch
        expected_switch_text=lang_settings["switch"]
        actual_switch_text=self.fc.fd["display_control"].get_switch_text()
        actual_switch_text == expected_switch_text, "Switch text is not matched"
        #Press Ctrl + Shift + S + D to switch back to the PC desktop.
        expected_keys_text=lang_settings["hdmiInputDescription"]
        actual_keys_text=self.fc.fd["display_control"].verify_hpmi_input_description()
        actual_keys_text==expected_keys_text, "Press Ctrl + Shift + S + D to switch back to the PC desktop text is not matched"
        #link-"HDMI Input OSD Help"
        expected_hdmi_input_osd_help_text=lang_settings["hdmiOsdHelpModelTitle"]
        actual_hdmi_input_osd_help_text=self.fc.fd["display_control"].get_hdmi_input_osd_help_text()
        actual_hdmi_input_osd_help_text==expected_hdmi_input_osd_help_text, "HDMI Input OSD Help text is not matched"
        #Color Adjustments
        expected_color_adjustments_text=lang_settings["colorAdjustments"]
        actual_color_adjustments_text=self.fc.fd["display_control"].get_color_adjestments()
        assert actual_color_adjustments_text == expected_color_adjustments_text, "Color Adjustments text is not matched"
        #R, G, B letter not translated in other languages
        #click switch button
        self.fc.fd["display_control"].click_switch_btn()
        #Back to PC Desktop window
        #title Back to PC Desktop
        expected_back_to_pc_desktop_text=lang_settings["backToPcDesktopModelTitle"]
        actual_back_to_pc_desktop_text=self.fc.fd["display_control"].get_back_to_pc_desktop_window_title()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_back_to_pc_desktop.png".format(language))
        assert actual_back_to_pc_desktop_text == expected_back_to_pc_desktop_text, "Back to PC Desktop title text is not matched"
        #While in  HDMI Input, use these keyboard keys to access and navigate the HDMI Input functions.
        expected_back_to_pc_desktop_sub_title_text=lang_settings["backToPcDesktopModelDescription"]
        actual_back_to_pc_desktop_sub_title_text=self.fc.fd["display_control"].get_back_to_pc_desktop_window_sub_title()
        assert actual_back_to_pc_desktop_sub_title_text == expected_back_to_pc_desktop_sub_title_text, "Back to PC Desktop sub title text is not matched"
        #Press Ctrl + Shift + S + D to stop using PC as a display
        expected_keys_to_stop_text=lang_settings["keysToStopUsingPCDisplay"]
        actual_keys_to_stop_text=self.fc.fd["display_control"].get_keys_to_stop_using_pcdesktop_text()
        assert actual_keys_to_stop_text==expected_keys_to_stop_text, "Press Ctrl + Shift + S + D to stop using PC as a display text is not matched"
        #Do not show again text
        expected_do_not_show_again_text=lang_settings["doNotShowAgain"]
        actual_do_not_show_again_text=self.fc.fd["display_control"].get_do_not_show_text_on_back_to_pc_desktop_window()
        assert actual_do_not_show_again_text==expected_do_not_show_again_text, "Do not show again text is not matched"
        #cancel button
        expected_cancel_btn_text=lang_settings["cancel"]
        actual_cancel_btn_text=self.fc.fd["display_control"].get_cancel_btn_on_back_to_pc_desktop_window()
        assert actual_cancel_btn_text==expected_cancel_btn_text, "Cancel button text is not matched"
        #continue button
        expected_continue_btn_text=lang_settings["continue"]
        actual_continue_btn_text=self.fc.fd["display_control"].get_continue_btn_on_back_to_pc_desktop_window()
        assert actual_continue_btn_text==expected_continue_btn_text, "Continue button text is not matched"
        #click continue button
        self.fc.fd["display_control"].click_continue_btn_on_back_to_pc_desktop_window()
        #click HDMi Input OSD Help link
        time.sleep(5)
        self.fc.fd["display_control"].click_hdmi_input_osd_help_link()
        time.sleep(10)
        #HDMi Input OSD Help link elements
        #HDMI input OSD Help title
        expected_hdmi_input_osd_help_link_title_text=lang_settings["hdmiOsdHelpModelTitle"]
        actual_hdmi_input_osd_help_link_title_text=self.fc.fd["display_control"].get_hdmi_input_osd_help_title_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "display_control_screenshot/{}_display_control_hdmi_input_osd_help.png".format(language))
        assert actual_hdmi_input_osd_help_link_title_text==expected_hdmi_input_osd_help_link_title_text, "HDMI input OSD Help title text is not matched"
        #While in  HDMI Input, use these keyboard keys to access and navigate the HDMI Input functions.
        expected_get_hdmi_input_osd_help_sub_title_text=lang_settings["hdmiOsdHelpModelDescription"]
        actual_get_hdmi_input_osd_help_sub_title_text=self.fc.fd["display_control"].get_hdmi_input_osd_help_sub_title_text()
        assert actual_get_hdmi_input_osd_help_sub_title_text==expected_get_hdmi_input_osd_help_sub_title_text, "While in  HDMI Input, use these keyboard keys to access and navigate the HDMI Input functions. text is not matched"
        #Up & Down Arrows
        expected_up_down_arrows_text=lang_settings["UpDownArrows"]
        actual_up_down_arrows_text=self.fc.fd["display_control"].get_up_down_arrows_text()
        assert actual_up_down_arrows_text==expected_up_down_arrows_text, "Up & Down Arrows text is not matched"
        #Enter
        expected_enter_text=lang_settings["enter"]
        actual_enter_text=self.fc.fd["display_control"].get_enter_text()
        assert actual_enter_text==expected_enter_text, "Enter text is not matched"
        #Navigate OSD Menu or change values of a selected function.
        expected_navigate_osd_menu_text=lang_settings["upDownArrowsDescription"]
        actual_navigate_osd_menu_text=self.fc.fd["display_control"].get_navigate_osd_menu_text()
        assert actual_navigate_osd_menu_text==expected_navigate_osd_menu_text, "Navigate OSD Menu or change values of a selected function. text is not matched"
        #Select function. Also opens the HDMI Input OSD (On-Screen Display) menu.
        expected_enter_description_text=lang_settings["enterDescription"]
        actual_enter_description_text=self.fc.fd["display_control"].get_enter_des_text()
        assert actual_enter_description_text==expected_enter_description_text, "Select function. Also opens the HDMI Input OSD (On-Screen Display) menu. text is not matched"
        #Close
        expected_close_text=lang_settings["close"]
        actual_close_text=self.fc.fd["display_control"].get_close_btn_on_hdmi_input_osd_help_window()
        assert actual_close_text==expected_close_text, "Close text is not matched"
        #click close button
        self.fc.fd["display_control"].click_close_btn_on_hdmi_input_osd_help_window()
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
        soft_assertion.raise_assertion_errors()
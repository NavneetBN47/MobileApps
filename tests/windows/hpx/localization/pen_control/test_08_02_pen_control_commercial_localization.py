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

@pytest.fixture(scope="session", params=["pen_control_commercial_screenshot"])
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

    @pytest.mark.commercial
    @pytest.mark.function
    def test_08_04_pen_module_C38121541(self, language):#for Commercial "Ultron"
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/pencontrolLocalization.json", language, "pencontrol")
        time.sleep(5)
        self.fc.restart_app()
         # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["navigation_panel"].verify_pen_control_visible()) is True, "Pen control module not available."
        logging.info("Pen module is available")
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        self.fc.fd["pen_control"].click_info_icon()
        time.sleep(5)
        actual_serial_num_value = self.fc.fd["pen_control"].get_pen_control_serail_number_value_commercial()
        self.fc.fd["pen_control"].click_info_icon()
        # Verify pen title and pen title tooltips
        if actual_serial_num_value == "NA":
            #HP Rechargeable Pen --  pen title
            expected_default_pen_name = lang_settings["officalPenName"]["commercialPenDefault"]
            actual_default_pen_name = self.fc.fd["pen_control"].get_pen_control_custom_name_show_commercial()
            ma_misc.create_localization_screenshot_folder("pen_control_commercial_screenshot", self.attachment_path)
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_pen_control_homepage01.png".format(language))
            soft_assertion.assert_equal(actual_default_pen_name, expected_default_pen_name, f"HP Rechargeable Active Pen G3 pen title is not matching, expected string text is {expected_default_pen_name}, but got {actual_default_pen_name}. ")

            #HP Rechargeable Pen --  pen title tooltips
            actual_default_pen_name_tooltip = self.fc.fd["pen_control"].get_device_name_tooltip_commercial()
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_pen_control_title_tooltip.png".format(language))
            soft_assertion.assert_equal(actual_default_pen_name_tooltip, expected_default_pen_name, f"HP Rechargeable Active Pen G3 pen title tooltips is not matching, expected string text is {expected_default_pen_name}, but got {actual_default_pen_name_tooltip}. ")
        else:
            #HP Rechargeable Active Pen G3 --  pen title
            expected_default_pen_name=lang_settings["officalPenName"]["commercialPen"]
            actual_default_pen_name=self.fc.fd["pen_control"].get_pen_control_custom_name_show_commercial()
            ma_misc.create_localization_screenshot_folder("pen_control_commercial_screenshot", self.attachment_path)
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_pen_control_homepage01.png".format(language))
            soft_assertion.assert_equal(actual_default_pen_name, expected_default_pen_name, f"HP Rechargeable Active Pen G3 pen title is not matching, expected string text is {expected_default_pen_name}, but got {actual_default_pen_name}. ")

            # HP Rechargeable Active Pen G3 --  pen title tooltips
            actual_default_pen_name_tooltip=self.fc.fd["pen_control"].get_device_name_tooltip_commercial()
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_pen_control_title_tooltip.png".format(language))
            soft_assertion.assert_equal(actual_default_pen_name_tooltip, expected_default_pen_name, f"HP Rechargeable Active Pen G3 pen title tooltips is not matching, expected string text is {expected_default_pen_name}, but got {actual_default_pen_name_tooltip}. ")

        #pen control texts on image 
        #Single press
        expected_single_press_text=lang_settings["topButton"]["buttonTitle"]["singlePress"]
        actual_single_press_text=self.fc.fd["pen_control"].get_single_press_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_single_press_text.png".format(language))
        soft_assertion.assert_equal(actual_single_press_text, expected_single_press_text, f"Single press text is not matching, expected string text is {expected_single_press_text}, but got {actual_single_press_text}. ")
        #MS whiteboard
        expected_ms_whiteboard_text=lang_settings["commonButtonAction"]["msWhiteBoard"]
        actual_ms_whiteboard_text=self.fc.fd["pen_control"].get_ms_whiteboard_commercial()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_ms_whiteboard_text.png".format(language))
        soft_assertion.assert_equal(actual_ms_whiteboard_text, expected_ms_whiteboard_text, f"MS whiteboard text is not matching, expected string text is {expected_ms_whiteboard_text}, but got {actual_ms_whiteboard_text}. ")
        #Double press
        expected_double_press_text=lang_settings["topButton"]["buttonTitle"]["doublePress"]
        actual_double_press_text=self.fc.fd["pen_control"].get_double_press_text()
        soft_assertion.assert_equal(actual_double_press_text, expected_double_press_text, f"Double press text is not matching, expected string text is {expected_double_press_text}, but got {actual_double_press_text}. ")
        #Screen snipping
        expected_screen_snipping_text=lang_settings["commonButtonAction"]["screenSnipping"]
        actual_screen_snipping_text=self.fc.fd["pen_control"].get_screen_snipping_commercial()
        soft_assertion.assert_equal(actual_screen_snipping_text, expected_screen_snipping_text, f"Screen snipping text is not matching, expected string text is {expected_screen_snipping_text}, but got {actual_screen_snipping_text}. ")
        #Long press
        expected_long_press_text=lang_settings["topButton"]["buttonTitle"]["longPress"]
        actual_long_press_text=self.fc.fd["pen_control"].get_long_press_text()
        soft_assertion.assert_equal(actual_long_press_text, expected_long_press_text, f"Long press text is not matching, expected string text is {expected_long_press_text}, but got {actual_long_press_text}. ")
        #Sticky notes
        expected_sticky_notes_text=lang_settings["commonButtonAction"]["stickyNote"]
        actual_sticky_notes_text=self.fc.fd["pen_control"].get_sticky_notes_commercial()
        soft_assertion.assert_equal(actual_sticky_notes_text, expected_sticky_notes_text, f"Sticky notes text is not matching, expected string text is {expected_sticky_notes_text}, but got {actual_sticky_notes_text}. ")
        #Restore defaults
        expected_restore_defaults_text=lang_settings["resetToDefaultButton"]["title"]
        actual_restore_defaults_text=self.fc.fd["pen_control"].get_restore_btn_text()
        soft_assertion.assert_equal(actual_restore_defaults_text, expected_restore_defaults_text, f"Restore defaults text is not matching, expected string text is {expected_restore_defaults_text}, but got {actual_restore_defaults_text}. ")
        #Universal Select
        time.sleep(2)
        expected_universal_btn_text=lang_settings["barrelButtonAction"]["universalSelect"]
        actual_universal_btn_text=self.fc.fd["pen_control"].get_universal_select_commercial()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_universal_select_button_text.png".format(language))
        soft_assertion.assert_equal(actual_universal_btn_text, expected_universal_btn_text, f"Universal select text is not matching, expected string text is {expected_universal_btn_text}, but got {actual_universal_btn_text}. ")
        #Erase
        expected_erase_btn_text=lang_settings["barrelButtonAction"]["erase"]
        actual_erase_btn_text=self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        soft_assertion.assert_equal(actual_erase_btn_text, expected_erase_btn_text, f"Erase button text is not matching, expected string text is {expected_erase_btn_text}, but got {actual_erase_btn_text}. ")
        #Pen sensitivity
        expected_pen_sensitivity_text=lang_settings["penSensitivity"]["title"]
        actual_pen_sensitivity_text=self.fc.fd["pen_control"].get_pen_sensitivity_commercial()
        soft_assertion.assert_equal(actual_pen_sensitivity_text, expected_pen_sensitivity_text, f"Pen sensitivity text is not matching, expected string text is {expected_pen_sensitivity_text}, but got {actual_pen_sensitivity_text}. ")
        #click on Pen sensitivity
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        #Pen sensitivity window elements
        #Pen sensitivity title
        expected_pen_sensitivity_title_text=lang_settings["penSensitivity"]["title"]
        actual_pen_sensitivity_title_text=self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_pen_sensitivity_window_elements_text.png".format(language))
        soft_assertion.assert_equal(actual_pen_sensitivity_title_text, expected_pen_sensitivity_title_text, f"Pen sensitivity title text is not matching, expected string text is {expected_pen_sensitivity_title_text}, but got {actual_pen_sensitivity_title_text}. ")
        #Pressure
        expected_pressure_text=lang_settings["penSensitivity"]["penTipSensitivity"]["pressure"]
        actual_pressure_text=self.fc.fd["pen_control"].get_pressure_title_text()
        soft_assertion.assert_equal(actual_pressure_text, expected_pressure_text, f"Pressure text is not matching, expected string text is {expected_pressure_text}, but got {actual_pressure_text}. ")
        #Tilt
        expected_tilt_text=lang_settings["penSensitivity"]["penTiltSensitivity"]["tilt"]
        actual_tilt_text=self.fc.fd["pen_control"].get_tilt_commercial()
        soft_assertion.assert_equal(actual_tilt_text, expected_tilt_text, f"Tilt text is not matching, expected string text is {expected_tilt_text}, but got {actual_tilt_text}. ")
        #click on Erase
        self.fc.fd["pen_control"].click_erase_btn_commercial()
        time.sleep(2)
        #Pen section elements
        #Lower barrel button
        expected_lower_barrel_button_text=lang_settings["lowerBarrelButton"]["title"]
        actual_lower_barrel_button_text=self.fc.fd["pen_control"].get_lower_barrel_btn()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_lower_barrel_button_text.png".format(language))
        soft_assertion.assert_equal(actual_lower_barrel_button_text, expected_lower_barrel_button_text, f"Lower barrel button text is not matching, expected string text is {expected_lower_barrel_button_text}, but got {actual_lower_barrel_button_text}. ")
        #Hover-click
        expected_hover_click_text=lang_settings["hoverToggle"]["title"]
        actual_hover_click_text=self.fc.fd["pen_control"].get_hover_click_lower_barrel_text()
        soft_assertion.assert_equal(actual_hover_click_text, expected_hover_click_text, f"Hover-click text is not matching, expected string text is {expected_hover_click_text}, but got {actual_hover_click_text}. ")
        #mouse hover tool tip on hover click
        self.fc.fd["pen_control"].click_lower_barrel_tooltip()
        expected_hover_click_tooltip_text=lang_settings["hoverToggle"]["tooltip"]
        actual_hover_click_tooltip_text=self.fc.fd["pen_control"].get_lower_barrel_tool_tip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_hover_click_tooltip_text.png".format(language))
        soft_assertion.assert_equal(actual_hover_click_tooltip_text, expected_hover_click_tooltip_text, f"Hover-click tooltip text is not matching, expected string text is {expected_hover_click_tooltip_text}, but got {actual_hover_click_tooltip_text}. ")
        
        time.sleep(2)
        #click on apps dd
        self.fc.fd["pen_control"].click_apps_dropdown()
        time.sleep(2)
        #click on media control dd
        self.fc.fd["pen_control"].click_media_control_dropdown()
        time.sleep(2)
        #click on pen dd
        self.fc.fd["pen_control"].click_pen_section_dd()
        time.sleep(2)
        
        #More text of productivity
        expected_more_text=lang_settings["actionsMenuHeader"]["moreItem"]
        actual_more_text=self.fc.fd["pen_control"].get_more_link_on_productivity()
        soft_assertion.assert_equal(actual_more_text, expected_more_text, f"More text is not matching, expected string text is {expected_more_text}, but got {actual_more_text}. ")
        
        #Productivity
        expected_productivity_text=lang_settings["actionsMenuHeader"]["productivity"]
        actual_productivity_text=self.fc.fd["pen_control"].get_productivity()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_Productivity_text.png".format(language))
        soft_assertion.assert_equal(actual_productivity_text, expected_productivity_text, f"Productivity text is not matching, expected string text is {expected_productivity_text}, but got {actual_productivity_text}. ")
        #----------------Productivity remaining elements----------------
        #Universal Select
        expected_universal_text=lang_settings["barrelButtonAction"]["universalSelect"]
        actual_universal_text=self.fc.fd["pen_control"].get_universal_select_text_commercial()
        soft_assertion.assert_equal(actual_universal_text, expected_universal_text, f"Universal select text is not matching, expected string text is {expected_universal_text}, but got {actual_universal_text}. ")
        #Copy
        expected_copy_text=lang_settings["barrelButtonAction"]["copy"]
        actual_copy_text=self.fc.fd["pen_control"].get_copy_commercial()
        soft_assertion.assert_equal(actual_copy_text, expected_copy_text, f"Copy text is not matching, expected string text is {expected_copy_text}, but got {actual_copy_text}. ")
        #Paste
        expected_paste_text=lang_settings["barrelButtonAction"]["paste"]
        actual_paste_text=self.fc.fd["pen_control"].get_paste_commercial()
        soft_assertion.assert_equal(actual_paste_text, expected_paste_text, f"Paste text is not matching, expected string text is {expected_paste_text}, but got {actual_paste_text}. ")
        #Undo
        expected_undo_text=lang_settings["barrelButtonAction"]["undo"]
        actual_undo_text=self.fc.fd["pen_control"].get_undo_commercial()
        soft_assertion.assert_equal(actual_undo_text, expected_undo_text, f"Undo text is not matching, expected string text is {expected_undo_text}, but got {actual_undo_text}. ")
        #Redo
        expected_redo_text=lang_settings["barrelButtonAction"]["redo"]
        actual_redo_text=self.fc.fd["pen_control"].get_redo_commercial()
        soft_assertion.assert_equal(actual_redo_text, expected_redo_text, f"Redo text is not matching, expected string text is {expected_redo_text}, but got {actual_redo_text}. ")
        
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        time.sleep(2)
        #Page up
        expected_page_up_text=lang_settings["commonButtonAction"]["pageUp"]
        actual_page_up_text=self.fc.fd["pen_control"].get_page_up_commercial()
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Page up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        #Page down
        expected_page_down_text=lang_settings["commonButtonAction"]["pageDown"]
        actual_page_down_text=self.fc.fd["pen_control"].get_page_down_commercial()
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"Page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        #Go back
        expected_go_back_text=lang_settings["barrelButtonAction"]["goBack"]
        actual_go_back_text=self.fc.fd["pen_control"].get_go_back_commercial()
        soft_assertion.assert_equal(actual_go_back_text, expected_go_back_text, f"Go back text is not matching, expected string text is {expected_go_back_text}, but got {actual_go_back_text}. ")
        #Go forward
        expected_go_forward_text=lang_settings["barrelButtonAction"]["goForward"]
        actual_go_forward_text=self.fc.fd["pen_control"].get_go_forward_commercial()
        soft_assertion.assert_equal(actual_go_forward_text, expected_go_forward_text, f"Go forward text is not matching, expected string text is {expected_go_forward_text}, but got {actual_go_forward_text}. ")
        
        #click on productivity drop down
        self.fc.fd["pen_control"].click_productivity_dd()
        
        #click on pen dd
        self.fc.fd["pen_control"].click_pen_dd()
        #------------------Pen section elements------------------
        #Pen title
        expected_pen_title_text=lang_settings["actionsMenuHeader"]["pen"]
        actual_pen_title_text=self.fc.fd["pen_control"].get_pen_title()
        soft_assertion.assert_equal(actual_pen_title_text, expected_pen_title_text, f"Pen title text is not matching, expected string text is {expected_pen_title_text}, but got {actual_pen_title_text}. ")
        #Erase
        expected_erase_btn_text=lang_settings["barrelButtonAction"]["erase"]
        actual_erase_text=self.fc.fd["pen_control"].get_erase_text_commercial()
        soft_assertion.assert_equal(actual_erase_text, expected_erase_btn_text, f"Erase text is not matching, expected string text is {expected_erase_btn_text}, but got {actual_erase_text}. ")
        #Right click
        expected_right_click_text=lang_settings["barrelButtonAction"]["rightClick"]
        actual_right_click_btn_text=self.fc.fd["pen_control"].get_right_click_pen_commercial()
        soft_assertion.assert_equal(actual_right_click_btn_text, expected_right_click_text, f"Right click text is not matching, expected string text is {expected_right_click_text}, but got {actual_right_click_btn_text}. ")
        #Touch On/Off
        expected_touch_on_off_text=lang_settings["commonButtonAction"]["touchOnOff"]
        actual_touch_on_off_text=self.fc.fd["pen_control"].get_touch_on_off_commercial()
        soft_assertion.assert_equal(actual_touch_on_off_text, expected_touch_on_off_text, f"Touch On/Off text is not matching, expected string text is {expected_touch_on_off_text}, but got {actual_touch_on_off_text}. ")
        #Left click
        expected_left_click_text=lang_settings["barrelButtonAction"]["leftClick"]
        actual_left_click_text=self.fc.fd["pen_control"].get_left_click_commercial()
        soft_assertion.assert_equal(actual_left_click_text, expected_left_click_text, f"Left click text is not matching, expected string text is {expected_left_click_text}, but got {actual_left_click_text}. ")
        #Middle click
        expected_middle_click_text=lang_settings["barrelButtonAction"]["middleClick"]
        actual_middle_click_text=self.fc.fd["pen_control"].get_middle_click_commercial()
        soft_assertion.assert_equal(actual_middle_click_text, expected_middle_click_text, f"Middle click text is not matching, expected string text is {expected_middle_click_text}, but got {actual_middle_click_text}. ")
        #click on more link of Pen
        self.fc.fd["pen_control"].click_more_link_on_pen()
        #Fourth click
        expected_fourth_click_text=lang_settings["barrelButtonAction"]["forthClick"]
        actual_fourth_click_text=self.fc.fd["pen_control"].get_fourth_click_commercial()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_Pen_section_elements_text.png".format(language))
        soft_assertion.assert_equal(actual_fourth_click_text, expected_fourth_click_text, f"Fourth click text is not matching, expected string text is {expected_fourth_click_text}, but got {actual_fourth_click_text}. ")
        #Fifth click
        expected_fifth_click_text=lang_settings["barrelButtonAction"]["fifthClick"]
        actual_fifth_click_text=self.fc.fd["pen_control"].get_fifth_click_commercial()
        soft_assertion.assert_equal(actual_fifth_click_text, expected_fifth_click_text, f"Fifth click text is not matching, expected string text is {expected_fifth_click_text}, but got {actual_fifth_click_text}. ")
        #Pen menu
        expected_pen_menu_text=lang_settings["commonButtonAction"]["penMenu"]
        actual_pen_menu_text=self.fc.fd["pen_control"].get_pen_menu_commercial()
        soft_assertion.assert_equal(actual_pen_menu_text, expected_pen_menu_text, f"Pen menu text is not matching, expected string text is {expected_pen_menu_text}, but got {actual_pen_menu_text}. ")
        #Disabled
        expected_disabled_text=lang_settings["commonButtonAction"]["disabled"]
        actual_disabled_text=self.fc.fd["pen_control"].get_disabled_commercial()
        soft_assertion.assert_equal(actual_disabled_text, expected_disabled_text, f"Disabled text is not matching, expected string text is {expected_disabled_text}, but got {actual_disabled_text}. ")
        #click on Pen drop down
        self.fc.fd["pen_control"].click_pen_dd()
        #click on Apps dd#click on Apps drop down
        self.fc.fd["pen_control"].click_apps_dropdown()
        #-------------Apps section elements----------------
        #Apps title
        expected_apps_text=lang_settings["actionsMenuHeader"]["apps"]
        actual_apps_text=self.fc.fd["pen_control"].get_apps()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_Apps_section_elements_text.png".format(language))
        soft_assertion.assert_equal(actual_apps_text, expected_apps_text, f"Apps title text is not matching, expected string text is {expected_apps_text}, but got {actual_apps_text}. ")
        #MS whiteboard
        expected_ms_whiteboard_text=lang_settings["commonButtonAction"]["msWhiteBoard"]
        actual_ms_whiteboard_text=self.fc.fd["pen_control"].get_ms_whiteboard_commercial_apps()
        soft_assertion.assert_equal(actual_ms_whiteboard_text, expected_ms_whiteboard_text, f"MS whiteboard text is not matching, expected string text is {expected_ms_whiteboard_text}, but got {actual_ms_whiteboard_text}. ")
        #Screen snipping
        expected_screen_snipping_text=lang_settings["commonButtonAction"]["screenSnipping"]
        actual_screen_snipping_text=self.fc.fd["pen_control"].get_screen_snipping_commercial_apps()
        soft_assertion.assert_equal(actual_screen_snipping_text, expected_screen_snipping_text, f"Screen snipping text is not matching, expected string text is {expected_screen_snipping_text}, but got {actual_screen_snipping_text}. ")
        #Switch application
        expected_switch_application_text=lang_settings["commonButtonAction"]["switchApp"]
        actual_switch_application_text=self.fc.fd["pen_control"].get_switch_application_commercial()
        soft_assertion.assert_equal(actual_switch_application_text, expected_switch_application_text, f"Switch application text is not matching, expected string text is {expected_switch_application_text}, but got {actual_switch_application_text}. ")
        #Web browser
        expected_web_browser_text=lang_settings["barrelButtonAction"]["openBrowser"]
        actual_web_browser_text=self.fc.fd["pen_control"].get_web_browser_commercial()
        soft_assertion.assert_equal(actual_web_browser_text, expected_web_browser_text, f"Web browser text is not matching, expected string text is {expected_web_browser_text}, but got {actual_web_browser_text}. ")
        #E-mail
        expected_e_mail_text=lang_settings["barrelButtonAction"]["openMail"]
        actual_e_mail_text=self.fc.fd["pen_control"].get_e_mail_commercial()
        soft_assertion.assert_equal(actual_e_mail_text, expected_e_mail_text, f"E-mail text is not matching, expected string text is {expected_e_mail_text}, but got {actual_e_mail_text}. ")
        #click on more of apps
        self.fc.fd["pen_control"].click_more_link_on_apps()
        time.sleep(2)
        #Windows search
        expected_windows_search_text=lang_settings["commonButtonAction"]["windowsSearch"]
        actual_windows_search_text=self.fc.fd["pen_control"].get_windows_search_commercial()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_Windows_search_text.png".format(language))
        soft_assertion.assert_equal(actual_windows_search_text, expected_windows_search_text, f"Windows search text is not matching, expected string text is {expected_windows_search_text}, but got {actual_windows_search_text}. ")
        #click on Apps drop down
        self.fc.fd["pen_control"].click_apps_dropdown()
        #click on media control dd
        self.fc.fd["pen_control"].click_media_control_dropdown()
        #------------------Media control section elements------------------
        #Media control title
        expected_media_control_text=lang_settings["actionsMenuHeader"]["mediaControl"]
        actual_media_control_text=self.fc.fd["pen_control"].get_media_control()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_Media_control_elements_texts.png".format(language))
        soft_assertion.assert_equal(actual_media_control_text, expected_media_control_text, f"Media control title text is not matching, expected string text is {expected_media_control_text}, but got {actual_media_control_text}. ")
        #Play/pause
        expected_play_pause_text=lang_settings["commonButtonAction"]["playPause"]
        actual_play_pause_text=self.fc.fd["pen_control"].get_play_pause_commercial()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play/pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        #Next track
        expected_next_track_text=lang_settings["commonButtonAction"]["nextTrack"]
        actual_next_track_text=self.fc.fd["pen_control"].get_next_track_commercial()
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"Next track text is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        #Previous track
        expected_previous_track_text=lang_settings["commonButtonAction"]["previousTrack"]
        actual_previous_track_text=self.fc.fd["pen_control"].get_previous_track_commercial()
        soft_assertion.assert_equal(actual_previous_track_text, expected_previous_track_text, f"Previous track text is not matching, expected string text is {expected_previous_track_text}, but got {actual_previous_track_text}. ")
        #Volume up
        expected_volume_up_text=lang_settings["commonButtonAction"]["volumeUp"]
        actual_volume_up_text=self.fc.fd["pen_control"].get_volume_up_commercial()
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        #volume down
        expected_volume_down_text=lang_settings["commonButtonAction"]["volumeDown"]
        actual_volume_down_text=self.fc.fd["pen_control"].get_volume_down_commercial()
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"Volume down text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        #Click MOre link of Media control
        self.fc.fd["pen_control"].click_more_link_on_media()
        #Mute audio
        expected_mute_audio_text=lang_settings["commonButtonAction"]["muteAudio"]
        actual_mute_audio_text=self.fc.fd["pen_control"].get_mute_audio_commercial()
        soft_assertion.assert_equal(actual_mute_audio_text, expected_mute_audio_text, f"Mute audio text is not matching, expected string text is {expected_mute_audio_text}, but got {actual_mute_audio_text}. ")
        #click on media control drop down
        self.fc.fd["pen_control"].click_media_control_dropdown()
        
        #click on Universal select button on pen
        self.fc.fd["pen_control"].click_universal_select_commercial()
        time.sleep(2)
        #Upper barrel button
        expected_upper_barrel_button_text=lang_settings["upperBarrelButton"]["title"]
        actual_upper_barrel_button_text=self.fc.fd["pen_control"].get_upper_barrel_btn_right_click()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_commercial_screenshot/{}_upper_barrel_button_text.png".format(language))
        soft_assertion.assert_equal(actual_upper_barrel_button_text, expected_upper_barrel_button_text, f"Upper barrel button text is not matching, expected string text is {expected_upper_barrel_button_text}, but got {actual_upper_barrel_button_text}. ")
        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        #self.fc.fd["devices"].restore_app()
        soft_assertion.raise_assertion_errors()

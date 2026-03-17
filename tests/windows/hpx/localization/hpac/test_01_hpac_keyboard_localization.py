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

@pytest.fixture(scope="session", params=["keyboard_screenshot"])
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

    def test_01_hpac_keyboard_C38194888(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/keyboardLocalization.json", language, "pCKeyboard")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        logging.info("keyboard module is available")
        
        #keyboard title--not changed if app language is changed
        self.fc.fd["external_keyboard"].click_restore_button()
        expected_keyboard_title_text=lang_settings["title"]
        actual_keyboard_title_text=self.fc.fd["external_keyboard"].get_title_tooltips_text()
        ma_misc.create_localization_screenshot_folder("keyboard_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_keyboard_homepage01.png".format(language))
        soft_assertion.assert_equal(actual_keyboard_title_text, expected_keyboard_title_text, f"keyboard title text is not matching, expected string text is {expected_keyboard_title_text}, but got {actual_keyboard_title_text}. ")
        #keyboard title tooltip--not changed if app language is changed
        expected_keyboard_title_tooltip_text=lang_settings["title"]
        actual_keyboard_title_tooltip_text=self.fc.fd["external_keyboard"].get_title_tooltips_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_keyboard_homepage01.png".format(language))
        soft_assertion.assert_equal(actual_keyboard_title_tooltip_text, expected_keyboard_title_tooltip_text, f"keyboard title tooltip text is not matching, expected string text is {expected_keyboard_title_tooltip_text}, but got {actual_keyboard_title_tooltip_text}. ")
        #keyboard name-HP 970/975 Series Keyboard--not found translation in win client repo--not changed if app language is changed
        #battery status-Battery 100%--not found translation in win client repo
        #Connection Bluetooth
        #hover over connection icon
        self.fc.fd["external_keyboard"].hover_usb_connection_tooltip()
        expected_connection_text=lang_settings["connection"]
        expected_usb_text=lang_settings["usb"]
        expected_connection_usb_tooltip_text=expected_connection_text + " " + expected_usb_text
        actual_connection_usb_tooltip_text=self.fc.fd["external_keyboard"].get_usb_connection_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_keyboard_connection_usb_tooltip.png".format(language))
        soft_assertion.assert_equal(actual_connection_usb_tooltip_text, expected_connection_usb_tooltip_text, f"connection usb tooltip text is not matching, expected string text is {expected_connection_usb_tooltip_text}, but got {actual_connection_usb_tooltip_text}. ")
        #Lighting setup
        expected_lighting_setup_text=lang_settings["lightingSetup"]
        actual_lighting_setup_text=self.fc.fd["external_keyboard"].get_lighting_setup_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_keyboard_homepage01.png".format(language))
        soft_assertion.assert_equal(actual_lighting_setup_text, expected_lighting_setup_text, f"lighting setup text is not matching, expected string text is {expected_lighting_setup_text}, but got {actual_lighting_setup_text}. ")
        #Proximity sensor
        expected_proximity_sensor_text=lang_settings["proximitySensor"]
        actual_proximity_sensor_text=self.fc.fd["external_keyboard"].get_proximity_sensor_text()
        soft_assertion.assert_equal(actual_proximity_sensor_text, expected_proximity_sensor_text, f"proximity sensor text is not matching, expected string text is {expected_proximity_sensor_text}, but got {actual_proximity_sensor_text}. ")
        #Proximity sensor tooltip--click over proximity sensor icon tooltip
        self.fc.fd["external_keyboard"].click_proximity_sensor_tootips_btn()
        #What is Smart Sensor
        expected_smart_text=lang_settings["WhatIsSmartSensor"]
        actual_smart_text=self.fc.fd["external_keyboard"].verify_proximity_sensor_tootips_message1()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_proximity_tooltip_message1.png".format(language))
        soft_assertion.assert_equal(actual_smart_text, expected_smart_text, f"proximity sensor tooltip text is not matching, expected string text is {expected_smart_text}, but got {actual_smart_text}. ")
        #Detects when you are near your keyboard and turns on the backlight.
        expected_sub_text=lang_settings["SmartSensorCard"]
        actual_sub_text=self.fc.fd["external_keyboard"].verify_proximity_sensor_tootips_message2()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_proximity_tooltip_message2.png".format(language))
        soft_assertion.assert_equal(actual_sub_text, expected_sub_text, f"proximity sensor tooltip sub text is not matching, expected string text is {expected_sub_text}, but got {actual_sub_text}. ")
        #close tooltip
        self.fc.fd["external_keyboard"].close_proximity_sensor_tootips()
        #Backlight auto adjust
        expected_backup_auto_adjust_text=lang_settings["backlightAuto"]
        actual_backup_auto_adjust_text=self.fc.fd["external_keyboard"].get_backlight_auto_adjust_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Backlight_auto_adjust.png".format(language))
        soft_assertion.assert_equal(actual_backup_auto_adjust_text, expected_backup_auto_adjust_text, f"backlight auto adjust text is not matching, expected string text is {expected_backup_auto_adjust_text}, but got {actual_backup_auto_adjust_text}. ")
        #backup auto adjust tooltip-----click over backup auto adjust icon tooltip
        self.fc.fd["external_keyboard"].click_backlight_adjust_tooltips_btn()
        self.fc.fd["external_keyboard"].click_backlight_adjust_tooltips_btn()
        #self.fc.fd["external_keyboard"].hover_backlight_adjust_tooltips_btn()
        time.sleep(2)
        #Backlight Auto Adjustment
        expected_backlight_auto_adjust_text=lang_settings["BacklightAutoAdjustment"]
        actual_backlight_auto_adjust=self.fc.fd["external_keyboard"].verify_backlight_adjust_tooltips_message1()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_backlight_auto_adjustment_tooltip_message1.png".format(language))
        soft_assertion.assert_equal(expected_backlight_auto_adjust_text, actual_backlight_auto_adjust, f"backlight auto adjust tooltip text is not matching, expected string text is {expected_backlight_auto_adjust_text}, but got {actual_backlight_auto_adjust}. ")
        #Automatically adjusts keyboard backlight based on ambient lighting.
        expected_sub_text=lang_settings["AutomaticallyAdjustskeyboardCard"]
        actual_sub_text=self.fc.fd["external_keyboard"].verify_backlight_adjust_tooltips_message2()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_backlight_auto_adjustment_tooltip_message2.png".format(language))
        soft_assertion.assert_equal(actual_sub_text, expected_sub_text, f"backlight auto adjust tooltip sub text is not matching, expected string text is {expected_sub_text}, but got {actual_sub_text}. ")
        self.fc.fd["external_keyboard"].close_proximity_sensor_tootips()
        #Restore defaults
        expected_restore_defaults_text=lang_settings["restoreDefault"]
        actual_restore_defaults_text=self.fc.fd["external_keyboard"].get_restore_button_text()
        soft_assertion.assert_equal(actual_restore_defaults_text, expected_restore_defaults_text, f"restore defaults text is not matching, expected string text is {expected_restore_defaults_text}, but got {actual_restore_defaults_text}. ")
        #keyboard keys hover
        #Mute
        self.fc.fd["external_keyboard"].hover_mute_key()
        expected_mute_text=lang_settings["mute"]
        actual_mute_text=self.fc.fd["external_keyboard"].get_mute_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_mute_key_text.png".format(language))
        soft_assertion.assert_equal(actual_mute_text, expected_mute_text, f"mute key text is not matching, expected string text is {expected_mute_text}, but got {actual_mute_text}. ")
        #Volume down
        self.fc.fd["external_keyboard"].hover_volume_down_key()
        expected_volume_down_text=lang_settings["volumeDown"]
        actual_volume_down_text=self.fc.fd["external_keyboard"].get_volume_down_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_volume_down_key_text.png".format(language))
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"volume down key text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        #Volume up
        self.fc.fd["external_keyboard"].hover_volume_up_key()
        expected_volume_up_text=lang_settings["volumeUp"]
        actual_volume_up_text=self.fc.fd["external_keyboard"].get_volume_up_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_volume_up_key_text.png".format(language))
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"volume up key text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        #Previous track
        self.fc.fd["external_keyboard"].hover_previous_track_key()
        expected_previous_track_text=lang_settings["prevTrack"]
        actual_previous_track_text=self.fc.fd["external_keyboard"].get_previous_track_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_previous_track_key_text.png".format(language))
        soft_assertion.assert_equal(actual_previous_track_text, expected_previous_track_text, f"previous track key text is not matching, expected string text is {expected_previous_track_text}, but got {actual_previous_track_text}. ")
        #Play/pause
        self.fc.fd["external_keyboard"].hover_play_pause_key()
        expected_play_pause_text=lang_settings["playPause"]
        actual_play_pause_text=self.fc.fd["external_keyboard"].get_play_pause_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_play_pause_key_text.png".format(language))
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"play pause key text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        #Next track
        self.fc.fd["external_keyboard"].hover_next_track_key()
        expected_next_track_text=lang_settings["nextTrack"]
        actual_next_track_text=self.fc.fd["external_keyboard"].get_next_track_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_next_track_key_text.png".format(language))
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"next track key text is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        #Screen brightness -
        self.fc.fd["external_keyboard"].hover_screen_brightness_down_key()
        expected_screen_brightness_down_text=lang_settings["brightnessDown"]
        actual_screen_brightness_down_text=self.fc.fd["external_keyboard"].get_screen_brightness_down_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_screen_brightness_down_key_text.png".format(language))
        soft_assertion.assert_equal(actual_screen_brightness_down_text, expected_screen_brightness_down_text, f"screen brightness down key text is not matching, expected string text is {expected_screen_brightness_down_text}, but got {actual_screen_brightness_down_text}. ")
        #Screen brightness +
        self.fc.fd["external_keyboard"].hover_screen_brightness_up_key()
        expected_screen_brightness_up_text=lang_settings["brightnessUp"]
        actual_screen_brightness_up_text=self.fc.fd["external_keyboard"].get_screen_brightness_up_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_screen_brightness_up_key_text.png".format(language))
        soft_assertion.assert_equal(actual_screen_brightness_up_text, expected_screen_brightness_up_text, f"screen brightness up key text is not matching, expected string text is {expected_screen_brightness_up_text}, but got {actual_screen_brightness_up_text}. ")
        #Print screen
        self.fc.fd["external_keyboard"].hover_new_window_key()
        expected_new_window_text=lang_settings["printScreen"]
        actual_new_window_text=self.fc.fd["external_keyboard"].get_new_window_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_new_window_key_text.png".format(language))
        soft_assertion.assert_equal(actual_new_window_text, expected_new_window_text, f"Print screen key text is not matching, expected string text is {expected_new_window_text}, but got {actual_new_window_text}. ")
        #Windows settings
        self.fc.fd["external_keyboard"].hover_window_settings_key()
        expected_window_settings_text=lang_settings["windowsSettings"]
        actual_window_settings_text=self.fc.fd["external_keyboard"].get_window_settings_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_window_settings_key_text.png".format(language))
        soft_assertion.assert_equal(actual_window_settings_text, expected_window_settings_text, f"window settings key text is not matching, expected string text is {expected_window_settings_text}, but got {actual_window_settings_text}. ")
        #Switch screen
        self.fc.fd["external_keyboard"].hover_switch_screen_key()
        expected_switch_screen_text=lang_settings["switchScreen"]
        actual_switch_screen_text=self.fc.fd["external_keyboard"].get_switch_screen_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_switch_screen_key_text.png".format(language))
        soft_assertion.assert_equal(actual_switch_screen_text, expected_switch_screen_text, f"switch screen key text is not matching, expected string text is {expected_switch_screen_text}, but got {actual_switch_screen_text}. ")
        #Windows search
        self.fc.fd["external_keyboard"].hover_windows_search_key()
        expected_windows_search_text=lang_settings["windowsSearch"]
        actual_widows_search_text=self.fc.fd["external_keyboard"].get_windows_search_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_windows_search_key_text.png".format(language))
        soft_assertion.assert_equal(actual_widows_search_text, expected_windows_search_text, f"windows search key text is not matching, expected string text is {expected_windows_search_text}, but got {actual_widows_search_text}. ")
        #Mic mute
        self.fc.fd["external_keyboard"].hover_mic_mute_key()
        expected_mic_mute_text=lang_settings["micMute"]
        actual_mic_mute_text=self.fc.fd["external_keyboard"].get_mic_mute_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_mic_mute_key_text.png".format(language))
        soft_assertion.assert_equal(actual_mic_mute_text.strip(), expected_mic_mute_text.strip(), f"Mic Mute text is not matching, expected string text is {expected_mic_mute_text}, but got {actual_mic_mute_text}. ")
        #Keyboard backlight
        self.fc.fd["external_keyboard"].hover_keyboard_backlight_key()
        expected_keyboard_backlight_text=lang_settings["keyboardLight"]
        actual_keyboard_backlight_text=self.fc.fd["external_keyboard"].get_keyboard_backlight_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_keyboard_backlight_key_text.png".format(language))
        soft_assertion.assert_equal(actual_keyboard_backlight_text, expected_keyboard_backlight_text, f"keyboard backlight key text is not matching, expected string text is {expected_keyboard_backlight_text}, but got {actual_keyboard_backlight_text}. ")
        #Desktop show/hide
        self.fc.fd["external_keyboard"].hover_desktop_show_hide_key()
        expected_desktop_show_hide_text=lang_settings["desktopShowHide"]
        actual_desktop_show_hide_text=self.fc.fd["external_keyboard"].get_desktop_show_hide_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_desktop_show_hide_key_text.png".format(language))
        soft_assertion.assert_equal(actual_desktop_show_hide_text, expected_desktop_show_hide_text, f"desktop show hide key text is not matching, expected string text is {expected_desktop_show_hide_text}, but got {actual_desktop_show_hide_text}. ")
        #Action center
        self.fc.fd["external_keyboard"].hover_action_center_key()
        expected_action_center_text=lang_settings["actionCenter"]
        actual_action_center_text=self.fc.fd["external_keyboard"].get_action_center_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_action_center_key_text.png".format(language))
        soft_assertion.assert_equal(actual_action_center_text, expected_action_center_text, f"action center key text is not matching, expected string text is {expected_action_center_text}, but got {actual_action_center_text}. ")
        #Lock
        self.fc.fd["external_keyboard"].hover_lock_key()
        expected_lock_text=lang_settings["lock"]
        actual_lock_text=self.fc.fd["external_keyboard"].get_lock_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_lock_key_text.png".format(language))
        soft_assertion.assert_equal(actual_lock_text, expected_lock_text, f"lock key text is not matching, expected string text is {expected_lock_text}, but got {actual_lock_text}. ")
        #Insert
        self.fc.fd["external_keyboard"].hover_insert_key()
        expected_insert_text=lang_settings["insert"]
        actual_insert_text=self.fc.fd["external_keyboard"].get_insert_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_insert_key_text.png".format(language))
        soft_assertion.assert_equal(actual_insert_text, expected_insert_text, f"insert key text is not matching, expected string text is {expected_insert_text}, but got {actual_insert_text}. ")
        #Home
        self.fc.fd["external_keyboard"].hover_home_key()
        expected_home_text=lang_settings["home"]
        actual_home_text=self.fc.fd["external_keyboard"].get_home_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_home_key_text.png".format(language))
        soft_assertion.assert_equal(actual_home_text, expected_home_text, f"home key text is not matching, expected string text is {expected_home_text}, but got {actual_home_text}. ")
        #Page up
        self.fc.fd["external_keyboard"].hover_page_up_key()
        expected_page_up_text=lang_settings["pgUp"]
        actual_page_up_text=self.fc.fd["external_keyboard"].get_page_up_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_page_up_key_text.png".format(language))
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"page up key text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        #delete
        self.fc.fd["external_keyboard"].hover_delete_key()
        expected_delete_text=lang_settings["delete"]
        actual_delete_text=self.fc.fd["external_keyboard"].get_delete_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_delete_key_text.png".format(language))
        soft_assertion.assert_equal(actual_delete_text, expected_delete_text, f"delete key text is not matching, expected string text is {expected_delete_text}, but got {actual_delete_text}. ")
        #end
        self.fc.fd["external_keyboard"].hover_end_key()
        expected_end_text=lang_settings["end"]
        actual_end_text=self.fc.fd["external_keyboard"].get_end_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_end_key_text.png".format(language))
        soft_assertion.assert_equal(actual_end_text, expected_end_text, f"end key text is not matching, expected string text is {expected_end_text}, but got {actual_end_text}. ")
        #pg down
        self.fc.fd["external_keyboard"].hover_page_down_key()
        expected_page_down_text=lang_settings["pgDown"]
        actual_page_down_text=self.fc.fd["external_keyboard"].get_page_down_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_page_down_key_text.png".format(language))
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"page down key text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        #click on fn key
        self.fc.fd["external_keyboard"].click_fn_key()
        #fn right side window
        #Fn Key
        expected_fn_key_text=lang_settings["fnKey"]
        actual_fn_key_text=self.fc.fd["external_keyboard"].get_fn_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_fn_key_text.png".format(language))
        soft_assertion.assert_equal(actual_fn_key_text, expected_fn_key_text, f"fn key text is not matching, expected string text is {expected_fn_key_text}, but got {actual_fn_key_text}. ")
        #fn_key tooltip
        self.fc.fd["external_keyboard"].click_fn_key_tooltip_icon()
        expected_fn_tooltip_text=lang_settings["useControlFnKey"]
        actual_fn_tooltip_text=self.fc.fd["external_keyboard"].get_fn_key_tooltip_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_fn_key_tooltip_text.png".format(language))
        soft_assertion.assert_equal(actual_fn_tooltip_text, expected_fn_tooltip_text, f"fn key tooltip text is not matching, expected string text is {expected_fn_tooltip_text}, but got {actual_fn_tooltip_text}. ")
        time.sleep(3)
        self.fc.fd["external_keyboard"].click_fn_key_tooltip_icon()
        #Function lock on start
        expected_function_lock_on_start_text=lang_settings["fnLockOnStart"]
        actual_function_lock_on_start_text=self.fc.fd["external_keyboard"].get_function_lock_on_start()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_function_lock_on_start_text.png".format(language))
        soft_assertion.assert_equal(actual_function_lock_on_start_text, expected_function_lock_on_start_text, f"function lock on start text is not matching, expected string text is {expected_function_lock_on_start_text}, but got {actual_function_lock_on_start_text}. ")
        #function tooltip icon
        self.fc.fd["external_keyboard"].click_function_lock_on_start_tooltip_icon()
        expected_lock_start_tooltip_text=lang_settings["setStateFnKey"]
        actual_lock_start_tooltip_text=self.fc.fd["external_keyboard"].get_function_lock_on_start_tooltip_icon()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_function_lock_on_start_tooltip_text.png".format(language))
        soft_assertion.assert_equal(actual_lock_start_tooltip_text, expected_lock_start_tooltip_text, f"function lock on start tooltip text is not matching, expected string text is {expected_lock_start_tooltip_text}, but got {actual_lock_start_tooltip_text}. ")
        self.fc.fd["external_keyboard"].click_function_lock_on_start_tooltip_icon()
        #Function lock
        expected_function_lock_text=lang_settings["functionLock"]
        actual_function_lock_text=self.fc.fd["external_keyboard"].get_function_lock()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_function_lock_text.png".format(language))
        soft_assertion.assert_equal(actual_function_lock_text, expected_function_lock_text, f"function lock text is not matching, expected string text is {expected_function_lock_text}, but got {actual_function_lock_text}. ")
        #Function lock tooltip icon
        self.fc.fd["external_keyboard"].click_function_lock_tooltip_icon()
        expected_current_tooltip_text=lang_settings["currentStateFn"]
        actual_current_tooltip_text=self.fc.fd["external_keyboard"].get_function_lock_tooltip_icon()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_function_lock_tooltip_text.png".format(language))
        soft_assertion.assert_equal(actual_current_tooltip_text, expected_current_tooltip_text, f"function lock tooltip text is not matching, expected string text is {expected_current_tooltip_text}, but got {actual_current_tooltip_text}. ")
        self.fc.fd["external_keyboard"].click_fn_key()
        
        #To open side panel
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_mute_key_to_open_side_panel()

        #Texts under Productivity
        #Productivity
        self.fc.fd["external_keyboard"].click_productivity_collapsed_button_to_expand_side_panel()
        actual_productivity_text = self.fc.fd["external_keyboard"].get_productivity_text_on_side_panel()
        expected_productivity_text = lang_settings["productivity"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Productivity_text.png".format(language))
        soft_assertion.assert_equal(actual_productivity_text, expected_productivity_text, f"Productivity text is not matching, expected string text is {expected_productivity_text}, but got {actual_productivity_text}. ")
        #Copy
        actual_copy_text = self.fc.fd["external_keyboard"].get_copy_text_on_side_panel()
        expected_copy_text = lang_settings["copy"]
        soft_assertion.assert_equal(actual_copy_text, expected_copy_text, f"Copy text is not matching, expected string text is {expected_copy_text}, but got {actual_copy_text}. ")
        #Cut
        actual_cut_text = self.fc.fd["external_keyboard"].get_cut_text_on_side_panel()
        expected_cut_text = lang_settings["cut"]
        soft_assertion.assert_equal(actual_cut_text, expected_cut_text, f"Cut text is not matching, expected string text is {expected_cut_text}, but got {actual_cut_text}. ")
        #Paste
        actual_paste_text = self.fc.fd["external_keyboard"].get_paste_text_on_side_panel()
        expected_paste_text = lang_settings["paste"]
        soft_assertion.assert_equal(actual_paste_text, expected_paste_text, f"Paste text is not matching, expected string text is {expected_paste_text}, but got {actual_paste_text}. ")
        #Undo
        actual_undo_text = self.fc.fd["external_keyboard"].get_undo_text_on_side_panel()
        expected_undo_text = lang_settings["undo"]
        soft_assertion.assert_equal(actual_undo_text, expected_undo_text, f"Undo text is not matching, expected string text is {expected_undo_text}, but got {actual_undo_text}. ")
        #Redo
        actual_redo_text = self.fc.fd["external_keyboard"].get_redo_text_on_side_panel()
        expected_redo_text = lang_settings["redo"]
        soft_assertion.assert_equal(actual_redo_text, expected_redo_text, f"Redo text is not matching, expected string text is {expected_redo_text}, but got {actual_redo_text}. ")
        #more
        actual_more_text = self.fc.fd["external_keyboard"].get_more_text_on_side_panel()
        expected_more_text = lang_settings["more"]
        soft_assertion.assert_equal(actual_more_text, expected_more_text, f"More text is not matching, expected string text is {expected_more_text}, but got {actual_more_text}. ")
        #click more     
        self.fc.fd["external_keyboard"].click_more_tab_on_side_panel()
        #select all
        actual_select_all_text = self.fc.fd["external_keyboard"].get_select_all_text_on_side_panel()
        expected_select_all_text = lang_settings["select"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Select_all_text.png".format(language))
        soft_assertion.assert_equal(actual_select_all_text, expected_select_all_text, f"Select all text is not matching, expected string text is {expected_select_all_text}, but got {actual_select_all_text}. ")
        #print
        actual_print_text = self.fc.fd["external_keyboard"].get_print_text_on_side_panel()
        expected_print_text = lang_settings["print"]
        soft_assertion.assert_equal(actual_print_text, expected_print_text, f"Print text is not matching, expected string text is {expected_print_text}, but got {actual_print_text}. ")
        #zoom in 
        actual_zoom_in_text = self.fc.fd["external_keyboard"].get_zoom_in_text_on_side_panel()
        expected_zoom_in_text = lang_settings["zoomIn"]
        soft_assertion.assert_equal(actual_zoom_in_text, expected_zoom_in_text, f"Zoom in text is not matching, expected string text is {expected_zoom_in_text}, but got {actual_zoom_in_text}. ")
        #zoom out 
        actual_zoom_out_text = self.fc.fd["external_keyboard"].get_zoom_out_text_on_side_panel()
        expected_zoom_out_text = lang_settings["zoomOut"]
        soft_assertion.assert_equal(actual_zoom_out_text, expected_zoom_out_text, f"Zoom Out text is not matching, expected string text is {expected_zoom_out_text}, but got {actual_zoom_out_text}. ")
        #page up 
        actual_page_up_text = self.fc.fd["external_keyboard"].get_page_up_text_on_side_panel()
        expected_page_up_text = lang_settings["pageUp"]
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Page Up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        #page down 
        actual_page_down_text = self.fc.fd["external_keyboard"].get_page_down_text_on_side_panel()
        expected_page_down_text = lang_settings["pageDown"]
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"Page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        #Find
        actual_find_text = self.fc.fd["external_keyboard"].get_find_text_on_side_panel()
        expected_find_text = lang_settings["find"]
        soft_assertion.assert_equal(actual_find_text, expected_find_text, f"Find text is not matching, expected string text is {expected_find_text}, but got {actual_find_text}. ")
        #To scroll down the side panel
        self.fc.fd["external_keyboard"].scroll_down_with_tab("action_center_text_on_side_panel")
        #Back
        actual_back_text = self.fc.fd["external_keyboard"].get_back_text_on_side_panel()
        expected_back_text = lang_settings["back"]
        soft_assertion.assert_equal(actual_back_text, expected_back_text, f"Back text is not matching, expected string text is {expected_back_text}, but got {actual_back_text}. ")
        #Forward
        actual_forward_text = self.fc.fd["external_keyboard"].get_forward_text_on_side_panel()
        expected_forward_text = lang_settings["forward"]
        soft_assertion.assert_equal(actual_forward_text, expected_forward_text, f"Forward text is not matching, expected string text is {expected_forward_text}, but got {actual_forward_text}. ")
        #Refresh/Reload
        actual_refresh_reload_text = self.fc.fd["external_keyboard"].get_refresh_reload_text_on_side_panel()
        expected_refresh_reload_text = lang_settings["refreshReload"]
        soft_assertion.assert_equal(actual_refresh_reload_text, expected_refresh_reload_text, f"Refresh/Reload text is not matching, expected string text is {expected_refresh_reload_text}, but got {actual_refresh_reload_text}. ")
        #Print Screen
        actual_print_screen_text = self.fc.fd["external_keyboard"].get_print_screen_text_on_side_panel()
        expected_print_screen_text = lang_settings["printScreen"]
        soft_assertion.assert_equal(actual_print_screen_text, expected_print_screen_text, f"Print Screen text is not matching, expected string text is {expected_print_screen_text}, but got {actual_print_screen_text}. ")
        #Action Center
        actual_action_center_text = self.fc.fd["external_keyboard"].get_action_center_text_on_side_panel()
        expected_action_center_text = lang_settings["actionCenter"]
        soft_assertion.assert_equal(actual_action_center_text, expected_action_center_text, f"Action Center text is not matching, expected string text is {expected_action_center_text}, but got {actual_action_center_text}. ")
        #To Scroll back up the side panel
        self.fc.fd["external_keyboard"].scroll_up_with_tab("productivity_text_on_side_panel")
        #to colapse productivity
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_productivity_expand_button_to_collapse_side_panel()

        #Texts under Media Control 
        self.fc.fd["external_keyboard"].click_media_control_collapsed_button_to_expand_side_panel()
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_more_tab_on_side_panel()
        #Media Control
        actual_media_control_text = self.fc.fd["external_keyboard"].get_media_control_text_on_side_panel()
        expected_media_control_text = lang_settings["mediaControls"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Media_Control_text.png".format(language))
        soft_assertion.assert_equal(actual_media_control_text, expected_media_control_text, f"Media Control text is not matching, expected string text is {expected_media_control_text}, but got {actual_media_control_text}. ")
        #Volume Up
        actual_volume_up_text = self.fc.fd["external_keyboard"].get_volume_up_text_on_side_panel()
        expected_volume_up_text = lang_settings["volumeUp"]
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        #Volume down
        actual_volume_down_text = self.fc.fd["external_keyboard"].get_volume_down_text_on_side_panel()
        expected_volume_down_text = lang_settings["volumeDown"]
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"Volume down text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        #Play/pause
        actual_play_pause_text = self.fc.fd["external_keyboard"].get_play_pause_text_on_side_panel()
        expected_play_pause_text = lang_settings["playPause"]
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play/Pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        #Previous Track
        actual_previous_track_text = self.fc.fd["external_keyboard"].get_previous_track_text_on_side_panel()
        expected_previous_track_text = lang_settings["prevTrack"]
        soft_assertion.assert_equal(actual_previous_track_text, expected_previous_track_text, f"Previous Track text is not matching, expected string text is {expected_previous_track_text}, but got {actual_previous_track_text}. ")
        #Next Track
        actual_next_track_text = self.fc.fd["external_keyboard"].get_next_track_text_on_side_panel()
        expected_next_track_text = lang_settings["nextTrack"]
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"Next Track text is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        #Mute
        actual_mute_text = self.fc.fd["external_keyboard"].get_mute_text_on_side_panel()
        expected_mute_text = lang_settings["mute"]
        soft_assertion.assert_equal(actual_mute_text, expected_mute_text, f"Mute text is not matching, expected string text is {expected_mute_text}, but got {actual_mute_text}. ")
        #Mic.Mute
        actual_mic_mute_text = self.fc.fd["external_keyboard"].get_mic_mute_text_on_side_panel()
        expected_mic_mute_text = lang_settings["micMute"]
        soft_assertion.assert_equal(actual_mic_mute_text.strip(), expected_mic_mute_text.strip(), f"Mic Mute text is not matching, expected string text is {expected_mic_mute_text}, but got {actual_mic_mute_text}. ")
        #to colapse media control
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_media_control_expand_button_to_collapse_side_panel()

        #Texts under Apps and File 
        self.fc.fd["external_keyboard"].click_app_and_files_collapsed_button_to_expand_side_panel()
        self.fc.fd["external_keyboard"].click_more_tab_on_side_panel()
        #Apps and Files
        actual_apps_and_files_text = self.fc.fd["external_keyboard"].get_app_and_file_text_on_side_panel()
        expected_apps_and_files_text = lang_settings["appsFilesTitle"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Apps_and_Files_text.png".format(language))
        soft_assertion.assert_equal(actual_apps_and_files_text, expected_apps_and_files_text, f"Apps and Files text is not matching, expected string text is {expected_apps_and_files_text}, but got {actual_apps_and_files_text}. ")
        #Open File 
        actual_open_file_text = self.fc.fd["external_keyboard"].get_open_file_text_on_side_panel()
        expected_open_file_text = lang_settings["openFile"]
        soft_assertion.assert_equal(actual_open_file_text, expected_open_file_text, f"Open File text is not matching, expected string text is {expected_open_file_text}, but got {actual_open_file_text}. ")
        #File save
        actual_file_save_text = self.fc.fd["external_keyboard"].get_file_save_text_on_side_panel()
        expected_file_save_text = lang_settings["fileSave"]
        soft_assertion.assert_equal(actual_file_save_text, expected_file_save_text, f"File save text is not matching, expected string text is {expected_file_save_text}, but got {actual_file_save_text}. ")
        #Open Folder
        actual_open_folder_text = self.fc.fd["external_keyboard"].get_open_folder_text_on_side_panel()
        expected_open_folder_text = lang_settings["openFolder"]
        soft_assertion.assert_equal(actual_open_folder_text, expected_open_folder_text, f"Open Folder text is not matching, expected string text is {expected_open_folder_text}, but got {actual_open_folder_text}. ")
        #Documents
        actual_documents_text = self.fc.fd["external_keyboard"].get_documents_text_on_side_panel()
        expected_documents_text = lang_settings["documents"]
        soft_assertion.assert_equal(actual_documents_text, expected_documents_text, f"Documents text is not matching, expected string text is {expected_documents_text}, but got {actual_documents_text}. ")
        #Download folder
        actual_download_folder_text = self.fc.fd["external_keyboard"].get_download_folder_text_on_side_panel()
        expected_download_folder_text = lang_settings["download"]
        soft_assertion.assert_equal(actual_download_folder_text, expected_download_folder_text, f"Download Folders text is not matching, expected string text is {expected_download_folder_text}, but got {actual_download_folder_text}. ")
        #Pictures
        actual_pictures_text = self.fc.fd["external_keyboard"].get_pictures_text_on_side_panel()
        expected_pictures_text = lang_settings["pictures"]
        soft_assertion.assert_equal(actual_pictures_text, expected_pictures_text, f"Pictures text is not matching, expected string text is {expected_pictures_text}, but got {actual_pictures_text}. ")
        #Videos
        actual_videos_text = self.fc.fd["external_keyboard"].get_videos_text_on_side_panel()
        expected_videos_text = lang_settings["videos"]
        soft_assertion.assert_equal(actual_videos_text, expected_videos_text, f"Videos text is not matching, expected string text is {expected_videos_text}, but got {actual_videos_text}. ")
        #Calculator
        actual_calculator_text = self.fc.fd["external_keyboard"].get_calculator_text_on_side_panel()
        expected_calculator_text = lang_settings["calculator"]
        soft_assertion.assert_equal(actual_calculator_text, expected_calculator_text, f"Calculator text is not matching, expected string text is {expected_calculator_text}, but got {actual_calculator_text}. ")
        #to colapse Apps and Files
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_app_and_files_expand_button_to_collapse_side_panel()

        #Texts under System 
        self.fc.fd["external_keyboard"].click_system_collapsed_button_to_expand_side_panel()
        self.fc.fd["external_keyboard"].click_more_tab_on_side_panel()
        #System
        actual_system_text = self.fc.fd["external_keyboard"].get_system_text_on_side_panel()
        expected_system_text = lang_settings["system"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_System_text.png".format(language))
        soft_assertion.assert_equal(actual_system_text, expected_system_text, f"System text is not matching, expected string text is {expected_system_text}, but got {actual_system_text}. ")
        #Lock
        actual_lock_text = self.fc.fd["external_keyboard"].get_lock_text_on_side_panel()
        expected_lock_text = lang_settings["lock"]
        soft_assertion.assert_equal(actual_lock_text, expected_lock_text, f"Lock text is not matching, expected string text is {expected_lock_text}, but got {actual_lock_text}. ")
        #Sleep
        actual_sleep_text = self.fc.fd["external_keyboard"].get_sleep_text_on_side_panel()
        expected_sleep_text = lang_settings["sleep"]
        soft_assertion.assert_equal(actual_sleep_text, expected_sleep_text, f"Sleep text is not matching, expected string text is {expected_sleep_text}, but got {actual_sleep_text}. ")
        #Shutdown
        actual_shutdown_text = self.fc.fd["external_keyboard"].get_shutdown_text_on_side_panel()
        expected_shutdown_text = lang_settings["shutdown"]
        soft_assertion.assert_equal(actual_shutdown_text, expected_shutdown_text, f"Shutdown text is not matching, expected string text is {expected_shutdown_text}, but got {actual_shutdown_text}. ")
        #Restart
        actual_restart_text = self.fc.fd["external_keyboard"].get_restart_text_on_side_panel()
        expected_restart_text = lang_settings["restart"]
        soft_assertion.assert_equal(actual_restart_text, expected_restart_text, f"Restart text is not matching, expected string text is {expected_restart_text}, but got {actual_restart_text}. ")
        #Sign out
        actual_sign_out_text = self.fc.fd["external_keyboard"].get_signout_text_on_side_panel()
        expected_sign_out_text = lang_settings["signOut"]
        soft_assertion.assert_equal(actual_sign_out_text, expected_sign_out_text, f"Sign out text is not matching, expected string text is {expected_sign_out_text}, but got {actual_sign_out_text}. ")
        #To scroll down the side panel
        self.fc.fd["external_keyboard"].scroll_down_with_tab("this_computer_text_on_side_panel")
        #Screen Brightness +
        actual_brightness_plus_text = self.fc.fd["external_keyboard"].get_screen_brightness_plus_text_on_side_panel()
        expected_brightness_plus_text = lang_settings["brightnessUp"]
        soft_assertion.assert_equal(actual_brightness_plus_text, expected_brightness_plus_text, f"Brightness + text is not matching, expected string text is {expected_brightness_plus_text}, but got {actual_brightness_plus_text}. ")
        #Screen Brightness -
        actual_brightness_minus_text = self.fc.fd["external_keyboard"].get_screen_brightness_minus_text_on_side_panel()
        expected_brightness_minus_text = lang_settings["brightnessDown"]
        soft_assertion.assert_equal(actual_brightness_minus_text, expected_brightness_minus_text, f"Brightness - text is not matching, expected string text is {expected_brightness_minus_text}, but got {actual_brightness_minus_text}. ")
        #Windows Search
        actual_windows_search_text = self.fc.fd["external_keyboard"].get_windows_search_text_on_side_panel()
        expected_windows_search_text = lang_settings["windowsSearch"]
        soft_assertion.assert_equal(actual_windows_search_text, expected_windows_search_text, f"Windows Search text is not matching, expected string text is {expected_windows_search_text}, but got {actual_windows_search_text}. ")
        #Windows Settings
        actual_windows_settings_text = self.fc.fd["external_keyboard"].get_windows_settings_text_on_side_panel()
        expected_windows_settings_text = lang_settings["windowsSettings"]
        soft_assertion.assert_equal(actual_windows_settings_text, expected_windows_settings_text, f"Windows Settings text is not matching, expected string text is {expected_windows_settings_text}, but got {actual_windows_settings_text}. ")
        #Switch Language
        actual_switch_language_text = self.fc.fd["external_keyboard"].get_switch_language_text_on_side_panel()
        expected_switch_language_text = lang_settings["switchLanguage"]
        soft_assertion.assert_equal(actual_switch_language_text, expected_switch_language_text, f"Switch Language text is not matching, expected string text is {expected_switch_language_text}, but got {actual_switch_language_text}. ")
        #This Computer
        actual_this_computer_text = self.fc.fd["external_keyboard"].get_this_computer_text_on_side_panel()
        expected_this_computer_text = lang_settings["myPC"]
        soft_assertion.assert_equal(actual_this_computer_text, expected_this_computer_text, f"This Computer text is not matching, expected string text is {expected_this_computer_text}, but got {actual_this_computer_text}. ")
        #To Scroll back up the side panel
        self.fc.fd["external_keyboard"].scroll_up_with_tab("system_text_on_side_panel")
        #to colapse System
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_system_expand_button_to_collapse_side_panel()

        #Texts under Windows Management
        self.fc.fd["external_keyboard"].click_windows_management_collapsed_button_to_expand_side_panel()
        self.fc.fd["external_keyboard"].click_more_tab_on_side_panel()
        #Windows Management
        actual_windows_management_text = self.fc.fd["external_keyboard"].get_windows_management_text_on_side_panel()
        expected_windows_management_text = lang_settings["windowMng"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Windows_Management_text.png".format(language))
        soft_assertion.assert_equal(actual_windows_management_text, expected_windows_management_text, f"Windows Management text is not matching, expected string text is {expected_windows_management_text}, but got {actual_windows_management_text}. ")
        #Maximize Window
        actual_maximize_window_text = self.fc.fd["external_keyboard"].get_maximize_window_text_on_side_panel()
        expected_maximize_window_text = lang_settings["maximizeWindows"]
        soft_assertion.assert_equal(actual_maximize_window_text, expected_maximize_window_text, f"Maximize Windows text is not matching, expected string text is {expected_maximize_window_text}, but got {actual_maximize_window_text}. ")
        #Minimize Window
        actual_minimize_window_text = self.fc.fd["external_keyboard"].get_minimize_window_text_on_side_panel()
        expected_minimize_window_text = lang_settings["minimizeWindows"]
        soft_assertion.assert_equal(actual_minimize_window_text, expected_minimize_window_text, f"Minimize Windows text is not matching, expected string text is {expected_minimize_window_text}, but got {actual_minimize_window_text}. ")
        #Close Window
        actual_close_window_text = self.fc.fd["external_keyboard"].get_close_window_text_on_side_panel()
        expected_close_window_text = lang_settings["closeWindow"]
        soft_assertion.assert_equal(actual_close_window_text, expected_close_window_text, f"Close Windows text is not matching, expected string text is {expected_close_window_text}, but got {actual_close_window_text}. ")
        #New Window
        actual_new_window_text = self.fc.fd["external_keyboard"].get_new_window_text_on_side_panel()
        expected_new_window_text = lang_settings["newWindows"]
        soft_assertion.assert_equal(actual_new_window_text, expected_new_window_text, f"New Window text is not matching, expected string text is {expected_new_window_text}, but got {actual_new_window_text}. ")
        #Snap Left
        actual_snap_left_text = self.fc.fd["external_keyboard"].get_snap_left_text_on_side_panel()
        expected_snap_left_text = lang_settings["snapLeft"]
        soft_assertion.assert_equal(actual_snap_left_text, expected_snap_left_text, f"Snap Left text is not matching, expected string text is {expected_snap_left_text}, but got {actual_snap_left_text}. ")
        #To scroll down the side panel
        self.fc.fd["external_keyboard"].scroll_down_with_tab("start_menu_text_on_side_panel")
        #Snap Right
        actual_snap_right_text = self.fc.fd["external_keyboard"].get_snap_right_text_on_side_panel()
        expected_snap_right_text = lang_settings["snapRight"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Snap_Right_text.png".format(language))
        soft_assertion.assert_equal(actual_snap_right_text, expected_snap_right_text, f"Snap Right text is not matching, expected string text is {expected_snap_right_text}, but got {actual_snap_right_text}. ")
        #Desktop Show/hide
        actual_desktop_show_hide_text = self.fc.fd["external_keyboard"].get_desktop_show_hide_text_on_side_panel()
        expected_desktop_show_hide_text = lang_settings["desktopShowHide"]
        soft_assertion.assert_equal(actual_desktop_show_hide_text, expected_desktop_show_hide_text, f"Desktop Show/hide text is not matching, expected string text is {expected_desktop_show_hide_text}, but got {actual_desktop_show_hide_text}. ")
        #Switch Apps
        actual_switch_apps_text = self.fc.fd["external_keyboard"].get_switch_apps_text_on_side_panel()
        expected_switch_apps_text = lang_settings["switchApps"]
        soft_assertion.assert_equal(actual_switch_apps_text, expected_switch_apps_text, f"Switch Apps text is not matching, expected string text is {expected_switch_apps_text}, but got {actual_switch_apps_text}. ")
        #Switch Screen
        actual_switch_screen_text = self.fc.fd["external_keyboard"].get_switch_screen_text_on_side_panel()
        expected_switch_screen_text = lang_settings["switchScreen"]
        soft_assertion.assert_equal(actual_switch_screen_text, expected_switch_screen_text, f"Switch Screen text is not matching, expected string text is {expected_switch_screen_text}, but got {actual_switch_screen_text}. ")
        #Task View
        actual_task_view_text = self.fc.fd["external_keyboard"].get_task_view_text_on_side_panel()
        expected_task_view_text = lang_settings["taskView"]
        soft_assertion.assert_equal(actual_task_view_text, expected_task_view_text, f"Task View text is not matching, expected string text is {expected_task_view_text}, but got {actual_task_view_text}. ")
        #Desktop next
        actual_desktop_next_text = self.fc.fd["external_keyboard"].get_desktop_next_text_on_side_panel()
        expected_desktop_next_text = lang_settings["desktopNext"]
        soft_assertion.assert_equal(actual_desktop_next_text, expected_desktop_next_text, f"Desktop next text is not matching, expected string text is {expected_desktop_next_text}, but got {actual_desktop_next_text}. ")
        #Desktop previous
        actual_desktop_previous_text = self.fc.fd["external_keyboard"].get_desktop_previous_text_on_side_panel()
        expected_desktop_previous_text = lang_settings["desktopPrevious"]
        soft_assertion.assert_equal(actual_desktop_previous_text, expected_desktop_previous_text, f"Desktop previous text is not matching, expected string text is {expected_desktop_previous_text}, but got {actual_desktop_previous_text}. ")
        #Start menu
        actual_start_menu_text = self.fc.fd["external_keyboard"].get_start_menu_text_on_side_panel()
        expected_start_menu_text = lang_settings["startMenu"]
        soft_assertion.assert_equal(actual_start_menu_text, expected_start_menu_text, f"Start menu text is not matching, expected string text is {expected_start_menu_text}, but got {actual_start_menu_text}. ")
        #To Scroll back up the side panel
        self.fc.fd["external_keyboard"].scroll_up_with_tab("windows_management_text_on_side_panel")
        #to colapse System
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_windows_management_expand_button_to_collapse_side_panel()
  
        #Texts under Web Browsing
        self.fc.fd["external_keyboard"].click_web_browsing_collapsed_button_to_expand_side_panel()
        self.fc.fd["external_keyboard"].click_more_tab_on_side_panel()
        #Web Browsing
        actual_web_browsing_text = self.fc.fd["external_keyboard"].get_web_browsing_text_on_side_panel()
        expected_web_browsing_text = lang_settings["webBrowsing"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Web_Browsing_text.png".format(language))
        soft_assertion.assert_equal(actual_web_browsing_text, expected_web_browsing_text, f"Web Browsing text is not matching, expected string text is {expected_web_browsing_text}, but got {actual_web_browsing_text}. ")
        #Home
        actual_web_browsing_home_text = self.fc.fd["external_keyboard"].get_web_browsing_home_text_on_side_panel()
        expected_web_browsing_home_text = lang_settings["home"]
        soft_assertion.assert_equal(actual_web_browsing_home_text, expected_web_browsing_home_text, f"Home text is not matching, expected string text is {expected_web_browsing_home_text}, but got {actual_web_browsing_home_text}. ")
        #Web Search
        actual_web_browsing_web_search_text = self.fc.fd["external_keyboard"].get_web_browsing_web_search_text_on_side_panel()
        expected_web_browsing_web_search_text = lang_settings["webSearch"]
        soft_assertion.assert_equal(actual_web_browsing_web_search_text, expected_web_browsing_web_search_text, f"Web Search text is not matching, expected string text is {expected_web_browsing_web_search_text}, but got {actual_web_browsing_web_search_text}. ")
        #Open new tab/page
        actual_web_browsing_open_new_tab_text = self.fc.fd["external_keyboard"].get_web_browsing_open_new_tab_text_on_side_panel()
        expected_web_browsing_open_new_tab_text = lang_settings["openNew"]
        soft_assertion.assert_equal(actual_web_browsing_open_new_tab_text, expected_web_browsing_open_new_tab_text, f"Open new tab/page text is not matching, expected string text is {expected_web_browsing_open_new_tab_text}, but got {actual_web_browsing_open_new_tab_text}. ")
        #Close tab/page
        actual_web_browsing_close_tab_text = self.fc.fd["external_keyboard"].get_web_browsing_close_tab_text_on_side_panel()
        expected_web_browsing_close_tab_text = lang_settings["closeTab"]
        soft_assertion.assert_equal(actual_web_browsing_close_tab_text, expected_web_browsing_close_tab_text, f"Close tab/page text is not matching, expected string text is {expected_web_browsing_close_tab_text}, but got {actual_web_browsing_close_tab_text}. ")
        #Switch between open tabs
        actual_web_browsing_switch_between_open_tabs_text = self.fc.fd["external_keyboard"].get_web_browsing_switch_between_open_tabs_text_on_side_panel()
        expected_web_browsing_switch_between_open_tabs_text = lang_settings["switchTabs"]
        soft_assertion.assert_equal(actual_web_browsing_switch_between_open_tabs_text, expected_web_browsing_switch_between_open_tabs_text, f"Switch between open tabs text is not matching, expected string text is {expected_web_browsing_switch_between_open_tabs_text}, but got {actual_web_browsing_switch_between_open_tabs_text}. ")
        #Toggle full screen/windowed
        actual_web_browsing_toggle_full_screen_tabs_text = self.fc.fd["external_keyboard"].get_web_browsing_toggle_full_screen_tabs_text_on_side_panel()
        expected_web_browsing_toggle_full_screen_tabs_text = lang_settings["toggleWindow"]
        soft_assertion.assert_equal(actual_web_browsing_toggle_full_screen_tabs_text, expected_web_browsing_toggle_full_screen_tabs_text, f"Toggle full screen/windowed text is not matching, expected string text is {expected_web_browsing_toggle_full_screen_tabs_text}, but got {actual_web_browsing_toggle_full_screen_tabs_text}. ")
        #Save page as bookmark
        actual_web_browsing_save_page_as_bookmark_text = self.fc.fd["external_keyboard"].get_web_browsing_save_page_as_bookmark_text_on_side_panel()
        expected_web_browsing_save_page_as_bookmark_text = lang_settings["bookmark"]
        soft_assertion.assert_equal(actual_web_browsing_save_page_as_bookmark_text, expected_web_browsing_save_page_as_bookmark_text, f"Save page as bookmark text is not matching, expected string text is {expected_web_browsing_save_page_as_bookmark_text}, but got {actual_web_browsing_save_page_as_bookmark_text}. ")
        #To Scroll back up the side panel
        self.fc.fd["external_keyboard"].scroll_up_with_tab("web_browsing_text_on_side_panel")
        #to colapse System
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_web_browsing_expand_button_to_collapse_side_panel()
      
       #Texts under Keyboard
        self.fc.fd["external_keyboard"].click_keyboard_collapsed_button_to_expand_side_panel()
        self.fc.fd["external_keyboard"].click_more_tab_on_side_panel()
        #Keyboard
        actual_keyboard_text = self.fc.fd["external_keyboard"].get_keyboard_text_on_side_panel()
        expected_keyboard_text = lang_settings["Keyboard"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Keyboard_text.png".format(language))
        soft_assertion.assert_equal(actual_keyboard_text, expected_keyboard_text, f"Keyboard text is not matching, expected string text is {expected_keyboard_text}, but got {actual_keyboard_text}. ")
        #Key:F1
        actual_key_f1_text = self.fc.fd["external_keyboard"].get_key_f1_text_on_side_panel()
        expected_key_f1_text = lang_settings["keyPrefix"] + lang_settings["f1Key"]
        soft_assertion.assert_equal(actual_key_f1_text, expected_key_f1_text, f"Key:F1 text is not matching, expected string text is {expected_key_f1_text}, but got {actual_key_f1_text}. ")
        #Key:F2
        actual_key_f2_text = self.fc.fd["external_keyboard"].get_key_f2_text_on_side_panel()
        expected_key_f2_text = lang_settings["keyPrefix"] + lang_settings["f2Key"]
        soft_assertion.assert_equal(actual_key_f2_text, expected_key_f2_text, f"Key:F2 text is not matching, expected string text is {expected_key_f2_text}, but got {actual_key_f2_text}. ")
        #Key:F3
        actual_key_f3_text = self.fc.fd["external_keyboard"].get_key_f3_text_on_side_panel()
        expected_key_f3_text = lang_settings["keyPrefix"] + lang_settings["f3Key"]
        soft_assertion.assert_equal(actual_key_f3_text, expected_key_f3_text, f"Key:F3 text is not matching, expected string text is {expected_key_f3_text}, but got {actual_key_f3_text}. ")
        #Key:F4
        actual_key_f4_text = self.fc.fd["external_keyboard"].get_key_f4_text_on_side_panel()
        expected_key_f4_text = lang_settings["keyPrefix"] + lang_settings["f4Key"]
        soft_assertion.assert_equal(actual_key_f4_text, expected_key_f4_text, f"Key:F4 text is not matching, expected string text is {expected_key_f4_text}, but got {actual_key_f4_text}. ")
        #Key:F5
        actual_key_f5_text = self.fc.fd["external_keyboard"].get_key_f5_text_on_side_panel()
        expected_key_f5_text = lang_settings["keyPrefix"] + lang_settings["f5Key"]
        soft_assertion.assert_equal(actual_key_f5_text, expected_key_f5_text, f"Key:F5 text is not matching, expected string text is {expected_key_f5_text}, but got {actual_key_f5_text}. ")
        #To scroll down the side panel 
        self.fc.fd["external_keyboard"].scroll_down_with_tab("key_scrlk_text_on_side_panel")
        #Key:F6
        actual_keyboard_text = self.fc.fd["external_keyboard"].get_key_f6_text_on_side_panel()
        expected_keyboard_text = lang_settings["keyPrefix"] + lang_settings["f6Key"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_key_f6_text.png".format(language))
        soft_assertion.assert_equal(actual_keyboard_text, expected_keyboard_text, f"Key:F6 text is not matching, expected string text is {expected_keyboard_text}, but got {actual_keyboard_text}. ")
        #Key:F7
        actual_keyboard_text = self.fc.fd["external_keyboard"].get_key_f7_text_on_side_panel()
        expected_keyboard_text = lang_settings["keyPrefix"] + lang_settings["f7Key"]
        soft_assertion.assert_equal(actual_keyboard_text, expected_keyboard_text, f"Key:F7 text is not matching, expected string text is {expected_keyboard_text}, but got {actual_keyboard_text}. ")
        #Key:F8
        actual_key_f8_text = self.fc.fd["external_keyboard"].get_key_f8_text_on_side_panel()
        expected_key_f8_text = lang_settings["keyPrefix"] + lang_settings["f8Key"]
        soft_assertion.assert_equal(actual_key_f8_text, expected_key_f8_text, f"Key:F8 text is not matching, expected string text is {expected_key_f8_text}, but got {actual_key_f8_text}. ")
        #Key:F9
        actual_key_f9_text = self.fc.fd["external_keyboard"].get_key_f9_text_on_side_panel()
        expected_key_f9_text = lang_settings["keyPrefix"] + lang_settings["f9Key"]
        soft_assertion.assert_equal(actual_key_f9_text, expected_key_f9_text, f"Key:F9 text is not matching, expected string text is {expected_key_f9_text}, but got {actual_key_f9_text}. ")
        #Key:F10
        actual_key_f10_text = self.fc.fd["external_keyboard"].get_key_f10_text_on_side_panel()
        expected_key_f10_text = lang_settings["keyPrefix"] + lang_settings["f10Key"]
        soft_assertion.assert_equal(actual_key_f10_text, expected_key_f10_text, f"Key:F10 text is not matching, expected string text is {expected_key_f10_text}, but got {actual_key_f10_text}. ")
        #Key:F11
        actual_key_f11_text = self.fc.fd["external_keyboard"].get_key_f11_text_on_side_panel()
        expected_key_f11_text = lang_settings["keyPrefix"] + lang_settings["f11Key"]
        soft_assertion.assert_equal(actual_key_f11_text, expected_key_f11_text, f"Key:F11 text is not matching, expected string text is {expected_key_f11_text}, but got {actual_key_f11_text}. ")
        #Key:F12
        actual_key_f12_text = self.fc.fd["external_keyboard"].get_key_f12_text_on_side_panel()
        expected_key_f12_text = lang_settings["keyPrefix"] + lang_settings["f12Key"]
        soft_assertion.assert_equal(actual_key_f12_text, expected_key_f12_text, f"Key:F12 text is not matching, expected string text is {expected_key_f12_text}, but got {actual_key_f12_text}. ")
        #Key:Insert
        actual_key_insert_text = self.fc.fd["external_keyboard"].get_key_insert_text_on_side_panel()
        expected_key_insert_text = lang_settings["keyPrefix"] + lang_settings["insert"]
        soft_assertion.assert_equal(actual_key_insert_text, expected_key_insert_text, f"Key:Insert text is not matching, expected string text is {expected_key_insert_text}, but got {actual_key_insert_text}. ")
        #Key:Home
        actual_home_text = self.fc.fd["external_keyboard"].get_key_home_text_on_side_panel()
        expected_home_text = lang_settings["keyPrefix"] + lang_settings["home"]
        soft_assertion.assert_equal(actual_home_text, expected_home_text, f"Key:Home text is not matching, expected string text is {expected_home_text}, but got {actual_home_text}. ")
        #Key:Page up
        actual_page_up_text = self.fc.fd["external_keyboard"].get_key_page_up_text_on_side_panel()
        expected_page_up_text = lang_settings["keyPrefix"] +  lang_settings["pageUp"]
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Key:Page up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        #Key:Delete
        actual_delete_text = self.fc.fd["external_keyboard"].get_key_delete_up_text_on_side_panel()
        expected_delete_text = lang_settings["keyPrefix"] + lang_settings["delete"]
        soft_assertion.assert_equal(actual_delete_text, expected_delete_text, f"Key:Delete text is not matching, expected string text is {expected_delete_text}, but got {actual_delete_text}. ")
        #Key:End
        actual_end_text = self.fc.fd["external_keyboard"].get_key_end_up_text_on_side_panel()
        expected_end_text = lang_settings["keyPrefix"] + lang_settings["end"]
        soft_assertion.assert_equal(actual_end_text, expected_end_text, f"Key:End text is not matching, expected string text is {expected_end_text}, but got {actual_end_text}. ")
        #Key:Page down
        actual_page_down_text = self.fc.fd["external_keyboard"].get_key_page_down_up_text_on_side_panel()
        expected_page_down_text = lang_settings["keyPrefix"] + lang_settings["pageDown"]
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"Key:Page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        #Key:Scrlk
        actual_scrlk_text = self.fc.fd["external_keyboard"].get_key_scrlk_text_on_side_panel()
        expected_scrlk_text = lang_settings["keyPrefix"] + lang_settings["scrLk"]
        soft_assertion.assert_equal(actual_scrlk_text, expected_scrlk_text, f"Key:Scrlk text is not matching, expected string text is {expected_scrlk_text}, but got {actual_scrlk_text}. ")
        #To Scroll back up the side panel
        self.fc.fd["external_keyboard"].scroll_up_with_tab("keyboard_text_on_side_panel")
        #to colapse System
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_keyboard_expand_button_to_collapse_side_panel()

        #Texts under Mouse
        self.fc.fd["external_keyboard"].click_mouse_collapsed_button_to_expand_side_panel()
        #Mouse
        actual_mouse_text = self.fc.fd["external_keyboard"].get_mouse_text_on_side_panel()
        expected_mouse_text = lang_settings["mouse"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "keyboard_screenshot/{}_Mouse_text.png".format(language))
        soft_assertion.assert_equal(actual_mouse_text, expected_mouse_text, f"Mouse text is not matching, expected string text is {expected_mouse_text}, but got {actual_mouse_text}. ")
        #Double click
        actual_double_click_text = self.fc.fd["external_keyboard"].get_double_click_text_on_side_panel()
        expected_double_click_text = lang_settings["doubleClick"]
        soft_assertion.assert_equal(actual_double_click_text, expected_double_click_text, f"Double Click text is not matching, expected string text is {expected_double_click_text}, but got {actual_double_click_text}. ")
        #Right click
        actual_right_click_text = self.fc.fd["external_keyboard"].get_right_click_text_on_side_panel()
        expected_right_click_text = lang_settings["rightClick"]
        soft_assertion.assert_equal(actual_right_click_text, expected_right_click_text, f"Right Click text is not matching, expected string text is {expected_right_click_text}, but got {actual_right_click_text}. ")
        #Middle click
        actual_middle_click_text = self.fc.fd["external_keyboard"].get_middle_click_text_on_side_panel()
        expected_middle_click_text = lang_settings["middleClick"]
        soft_assertion.assert_equal(actual_middle_click_text, expected_middle_click_text, f"Middle Click text is not matching, expected string text is {expected_middle_click_text}, but got {actual_middle_click_text}. ")
        #To scroll down the side panel 
        self.fc.fd["external_keyboard"].scroll_down_with_tab("mouse_scroll_right_text_side_panel")
        #Scroll left
        actual_scroll_left_text = self.fc.fd["external_keyboard"].get_scroll_left_text_on_side_panel()
        expected_scroll_left_text = lang_settings["scrollLeft"]
        soft_assertion.assert_equal(actual_scroll_left_text, expected_scroll_left_text, f"Scroll left text is not matching, expected string text is {expected_scroll_left_text}, but got {actual_scroll_left_text}. ")
        #Scroll right
        actual_scroll_right_text = self.fc.fd["external_keyboard"].get_scroll_right_text_on_side_panel()
        expected_scroll_right_text = lang_settings["scrollRight"]
        soft_assertion.assert_equal(actual_scroll_right_text, expected_scroll_right_text, f"Scroll right text is not matching, expected string text is {expected_scroll_right_text}, but got {actual_scroll_right_text}. ")
        #To Scroll back up the side panel
        self.fc.fd["external_keyboard"].scroll_up_with_tab("mouse_text_on_side_panel")
        #to colapse System
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_mouse_expand_button_to_collapse_side_panel()
        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
        soft_assertion.raise_assertion_errors()
    
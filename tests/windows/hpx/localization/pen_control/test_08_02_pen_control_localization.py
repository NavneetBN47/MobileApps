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

@pytest.fixture(scope="session", params=["pen_control_screenshot"])
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

    def test_08_02_pen_module_C36769633(self, language):#for Consumer
        soft_assertion = SoftAssert()
        lang_settings = ma_misc.load_json_file("resources/test_data/hpx/pencontrolLocalization.json")[language]["translation"]["pencontrol"]
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["navigation_panel"].verify_pen_control_visible()) is True, "Pen control module not available."
        logging.info("Pen module is available")
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        #HP Digital pen title
        expected_default_pen_name=lang_settings["officalPenName"]["consumer"]
        actual_default_pen_name=self.fc.fd["pen_control"].get_default_pen_name()
        ma_misc.create_localization_screenshot_folder("pen_control_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_homepage01.png".format(language))
        soft_assertion.assert_equal(actual_default_pen_name, expected_default_pen_name, f"HP Digital pen title text is not matching, expected string text is {expected_default_pen_name}, but got {actual_default_pen_name}. ")
        #HP Digital pen title tooltips
        expected_default_pen_name_tooltip=lang_settings["officalPenName"]["consumer"]
        actual_default_pen_name_tooltip=self.fc.fd["pen_control"].get_pen_name_tooltips()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_title_tooltip.png".format(language))
        soft_assertion.assert_equal(actual_default_pen_name_tooltip, expected_default_pen_name_tooltip, f"HP Digital pen title tooltips text is not matching, expected string text is {expected_default_pen_name_tooltip}, but got {actual_default_pen_name_tooltip}. ")
        #Battery status
        self.fc.fd["pen_control"].click_battery_status()
        battery_text=lang_settings["batteryTooltip"]["titleDisconnect"]
        press_text=lang_settings["batteryTooltip"]["commonDescription"]
        expected_battery_status_text=battery_text+" "+press_text
        actual_battery_status_text=self.fc.fd["pen_control"].get_battery_status_tool_tip_text()
        soft_assertion.assert_equal(actual_battery_status_text, expected_battery_status_text, f"Battery status tooltips text is not matching, expected string text is {expected_battery_status_text}, but got {actual_battery_status_text}. ")
        # Upper Barrel Button
        expected_upper_barrel_button_text = lang_settings["upperBarrelButton"]["title"]
        actual_upper_barrel_button_text = self.fc.fd["pen_control"].get_upper_barrel_text()
        soft_assertion.assert_equal(actual_upper_barrel_button_text, expected_upper_barrel_button_text, f"Upper Barel Button text is not matching, expected string text is {expected_upper_barrel_button_text}, but got {actual_upper_barrel_button_text}. ")
        self.driver.swipe(direction="down", distance=1)
        #upper barrel dd
        self.fc.fd["pen_control"].click_upper_barrel_dropdown()
        #upper barrel elements
        self.driver.swipe(direction="up", distance=2)
        
        expected_undo_text = lang_settings["consumerButtonAction"]["undo"]
        actual_undo_text = self.fc.fd["pen_control"].get_upper_barrel_cons_undo()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel01.png".format(language))
        soft_assertion.assert_equal(actual_undo_text, expected_undo_text, f"Undo text is not matching, expected string text is {expected_undo_text}, but got {actual_undo_text}. ")
       
        expected_shift_key_text = lang_settings["consumerButtonAction"]["shiftKey"]
        actual_shift_key_text = self.fc.fd["pen_control"].get_upper_barrel_cons_shift_key()
        soft_assertion.assert_equal(actual_shift_key_text, expected_shift_key_text, f"Shift key text is not matching, expected string text is {expected_shift_key_text}, but got {actual_shift_key_text}. ")
        
        expected_control_key_text = lang_settings["consumerButtonAction"]["controlKey"]
        actual_control_key_text = self.fc.fd["pen_control"].get_upper_barrel_cons_control_key()
        soft_assertion.assert_equal(actual_control_key_text, expected_control_key_text, f"Control key text is not matching, expected string text is {expected_control_key_text}, but got {actual_control_key_text}. ")
        
        expected_alt_key_text = lang_settings["consumerButtonAction"]["altKey"]
        actual_alt_key_text = self.fc.fd["pen_control"].get_upper_barrel_cons_alt_key()
        soft_assertion.assert_equal(actual_alt_key_text, expected_alt_key_text, f"Alt key text is not matching, expected string text is {expected_alt_key_text}, but got {actual_alt_key_text}. ")
       
        expected_windows_key_text = lang_settings["consumerButtonAction"]["windowsKey"]
        actual_windows_key_text = self.fc.fd["pen_control"].get_upper_barrel_cons_windows_key()
        soft_assertion.assert_equal(actual_windows_key_text, expected_windows_key_text, f"Windows key text is not matching, expected string text is {expected_windows_key_text}, but got {actual_windows_key_text}. ")
       
        expected_tab_key_text = lang_settings["consumerButtonAction"]["tabKey"]
        actual_tab_key_text = self.fc.fd["pen_control"].get_upper_barrel_cons_tab_key()
        soft_assertion.assert_equal(actual_tab_key_text, expected_tab_key_text, f"Tab key text is not matching, expected string text is {expected_tab_key_text}, but got {actual_tab_key_text}. ")
        
        expected_volume_up_text = lang_settings["consumerButtonAction"]["volumeUp"]
        actual_volume_up_text = self.fc.fd["pen_control"].get_upper_barrel_cons_volume_up()
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
       
        expected_volume_down_text = lang_settings["consumerButtonAction"]["volumeDown"]
        actual_volume_down_text = self.fc.fd["pen_control"].get_upper_barrel_cons_volume_down()
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"Volume down text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        
        expected_mute_unmute_text = lang_settings["consumerButtonAction"]["muteUnmute"]
        actual_mute_unmute_text = self.fc.fd["pen_control"].get_upper_barrel_cons_mute_unmute()
        soft_assertion.assert_equal(actual_mute_unmute_text, expected_mute_unmute_text, f"Mute/Unmute text is not matching, expected string text is {expected_mute_unmute_text}, but got {actual_mute_unmute_text}. ")
        
        expected_play_pause_text = lang_settings["consumerButtonAction"]["playPause"]
        actual_play_pause_text = self.fc.fd["pen_control"].get_upper_barrel_cons_play_pause()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play/Pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        
        expected_right_arrow_key_text = lang_settings["consumerButtonAction"]["rightArrowKey"]
        actual_right_arrow_key_text = self.fc.fd["pen_control"].get_upper_barrel_cons_right_arrow_key()
        soft_assertion.assert_equal(actual_right_arrow_key_text, expected_right_arrow_key_text, f"Right arrow key text is not matching, expected string text is {expected_right_arrow_key_text}, but got {actual_right_arrow_key_text}. ")
        self.driver.swipe(direction="down", distance=1)
        
        expected_left_arrow_key_text = lang_settings["consumerButtonAction"]["leftArrowKey"]
        actual_left_arrow_key_text = self.fc.fd["pen_control"].get_upper_barrel_cons_left_arrow_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel02.png".format(language))
        soft_assertion.assert_equal(actual_left_arrow_key_text, expected_left_arrow_key_text, f"Left arrow key is not matching, expected string text is {expected_left_arrow_key_text}, but got {actual_left_arrow_key_text}. ")
       
        expected_new_browser_tab_text = lang_settings["consumerButtonAction"]["newBrowserTab"]
        actual_new_browser_tab_text = self.fc.fd["pen_control"].get_upper_barrel_cons_new_browser_tab()
        soft_assertion.assert_equal(actual_new_browser_tab_text, expected_new_browser_tab_text, f"New browser tab text is not matching, expected string text is {expected_new_browser_tab_text}, but got {actual_new_browser_tab_text}. ")
        
        expected_previous_page_text = lang_settings["consumerButtonAction"]["previousPage"]
        actual_previous_page_text = self.fc.fd["pen_control"].get_upper_barrel_cons_previous_page()        
        soft_assertion.assert_equal(actual_previous_page_text, expected_previous_page_text, f"Previous page text is not matching, expected string text is {expected_previous_page_text}, but got {actual_previous_page_text}. ")
        
        expected_next_page_text = lang_settings["consumerButtonAction"]["nextPage"]
        actual_next_page_text = self.fc.fd["pen_control"].get_upper_barrel_cons_next_page()
        soft_assertion.assert_equal(actual_next_page_text, expected_next_page_text, f"Next page text is not matching, expected string text is {expected_next_page_text}, but got {actual_next_page_text}. ")
       
        expected_take_sceenshot_text = lang_settings["consumerButtonAction"]["takeScreenshot"]
        actual_take_sceenshot_text = self.fc.fd["pen_control"].get_upper_barrel_cons_take_screenshot()
        soft_assertion.assert_equal(actual_take_sceenshot_text, expected_take_sceenshot_text, f"Take screenshot text is not matching, expected string text is {expected_take_sceenshot_text}, but got {actual_take_sceenshot_text}. ")
        
        expected_launch_task_manager_text = lang_settings["consumerButtonAction"]["lanuchTaskManager"]
        actual_launch_task_manager_text = self.fc.fd["pen_control"].get_upper_barrel_cons_launch_task_manager()
        soft_assertion.assert_equal(actual_launch_task_manager_text, expected_launch_task_manager_text, f"Launch task manager text is not matching, expected string text is {expected_launch_task_manager_text}, but got {actual_launch_task_manager_text}. ")
        self.driver.swipe(direction="down", distance=1)
        
        expected_switch_between_apps_text = lang_settings["consumerButtonAction"]["switchBetweenApps"]
        actual_switch_between_apps_text = self.fc.fd["pen_control"].get_upper_barrel_cons_switch_between_apps()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel03.png".format(language))
        soft_assertion.assert_equal(actual_switch_between_apps_text, expected_switch_between_apps_text, f"Switch between apps text is not matching, expected string text is {expected_switch_between_apps_text}, but got {actual_switch_between_apps_text}. ")
        
        expected_show_the_desktop_text = lang_settings["consumerButtonAction"]["showTheDesktop"]
        actual_show_the_desktop_text = self.fc.fd["pen_control"].get_upper_barrel_cons_show_the_desktop()
        soft_assertion.assert_equal(actual_show_the_desktop_text, expected_show_the_desktop_text, f"Show the desktop text is not matching, expected string text is {expected_show_the_desktop_text}, but got {actual_show_the_desktop_text}. ")
       
        expected_right_click_text = lang_settings["consumerButtonAction"]["rightClick"]
        actual_right_click_text = self.fc.fd["pen_control"].get_upper_barrel_cons_right_click()
        soft_assertion.assert_equal(actual_right_click_text, expected_right_click_text, f"Right click text is not matching, expected string text is {expected_right_click_text}, but got {actual_right_click_text}. ")
       
        expected_disable_pen_buttons_text = lang_settings["consumerButtonAction"]["disablePenButtons"]
        actual_disable_pen_buttons_text = self.fc.fd["pen_control"].get_upper_barrel_cons_disable_pen_buttons()
        soft_assertion.assert_equal(actual_disable_pen_buttons_text, expected_disable_pen_buttons_text, f"Disable pen buttons text is not matching, expected string text is {expected_disable_pen_buttons_text}, but got {actual_disable_pen_buttons_text}. ")
        
        expected_scroll_text = lang_settings["consumerButtonAction"]["scroll"]
        actual_scroll_text = self.fc.fd["pen_control"].get_upper_barrel_cons_scroll()
        soft_assertion.assert_equal(actual_scroll_text, expected_scroll_text, f"Scroll text is not matching, expected string text is {expected_scroll_text}, but got {actual_scroll_text}. ")
        
        expected_erase_text = lang_settings["consumerButtonAction"]["erase"]
        actual_erase_text = self.fc.fd["pen_control"].get_upper_barrel_cons_erase()
        soft_assertion.assert_equal(actual_erase_text, expected_erase_text, f"Erase text is not matching, expected string text is {expected_erase_text}, but got {actual_erase_text}. ")
        
        self.fc.fd["pen_control"].click_upper_barrel_cons_right_click()
        
        # Lower Barrel Button
        expected_lower_barrel_button_text = lang_settings["lowerBarrelButton"]["title"]
        actual_lower_barrel_button_text = self.fc.fd["pen_control"].get_lower_barrel_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_homepage_01.png".format(language))
        soft_assertion.assert_equal(actual_lower_barrel_button_text, expected_lower_barrel_button_text, f"Lower Barrel Button text is not matching, expected string text is {expected_lower_barrel_button_text}, but got {actual_lower_barrel_button_text}. ")
        # click lower barrel dd elements
        self.fc.fd["pen_control"].click_lower_barrel_dropdown()
        self.driver.swipe(direction="up", distance=2)
        
        expected_undo_text = lang_settings["consumerButtonAction"]["undo"]
        actual_undo_text = self.fc.fd["pen_control"].get_lower_barrel_cons_undo()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_low_barrel_02.png".format(language))
        soft_assertion.assert_equal(actual_undo_text, expected_undo_text, f"Undo text is not matching, expected string text is {expected_undo_text}, but got {actual_undo_text}. ")
       
        expected_shift_key_text = lang_settings["consumerButtonAction"]["shiftKey"]
        actual_shift_key_text = self.fc.fd["pen_control"].get_lower_barrel_cons_shift_key()
        soft_assertion.assert_equal(actual_shift_key_text, expected_shift_key_text, f"Shift key text is not matching, expected string text is {expected_shift_key_text}, but got {actual_shift_key_text}. ")
        
        expected_control_key_text = lang_settings["consumerButtonAction"]["controlKey"]
        actual_control_key_text = self.fc.fd["pen_control"].get_lower_barrel_cons_control_key()
        soft_assertion.assert_equal(actual_control_key_text, expected_control_key_text, f"Control key text is not matching, expected string text is {expected_control_key_text}, but got {actual_control_key_text}. ")
        
        expected_alt_key_text = lang_settings["consumerButtonAction"]["altKey"]
        actual_alt_key_text = self.fc.fd["pen_control"].get_lower_barrel_cons_alt_key()
        soft_assertion.assert_equal(actual_alt_key_text, expected_alt_key_text, f"Alt key text is not matching, expected string text is {expected_alt_key_text}, but got {actual_alt_key_text}. ")
       
        expected_windows_key_text = lang_settings["consumerButtonAction"]["windowsKey"]
        actual_windows_key_text = self.fc.fd["pen_control"].get_lower_barrel_cons_windows_key()
        soft_assertion.assert_equal(actual_windows_key_text, expected_windows_key_text, f"Windows key text is not matching, expected string text is {expected_windows_key_text}, but got {actual_windows_key_text}. ")
       
        expected_tab_key_text = lang_settings["consumerButtonAction"]["tabKey"]
        actual_tab_key_text = self.fc.fd["pen_control"].get_lower_barrel_cons_tab_key()
        soft_assertion.assert_equal(actual_tab_key_text, expected_tab_key_text, f"Tab key text is not matching, expected string text is {expected_tab_key_text}, but got {actual_tab_key_text}. ")
        
        expected_volume_up_text = lang_settings["consumerButtonAction"]["volumeUp"]
        actual_volume_up_text = self.fc.fd["pen_control"].get_lower_barrel_cons_volume_up()
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
       
        expected_volume_down_text = lang_settings["consumerButtonAction"]["volumeDown"]
        actual_volume_down_text = self.fc.fd["pen_control"].get_lower_barrel_cons_volume_down()
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"Volume down text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        
        expected_mute_unmute_text = lang_settings["consumerButtonAction"]["muteUnmute"]
        actual_mute_unmute_text = self.fc.fd["pen_control"].get_lower_barrel_cons_mute_unmute()
        soft_assertion.assert_equal(actual_mute_unmute_text, expected_mute_unmute_text, f"Mute/Unmute text is not matching, expected string text is {expected_mute_unmute_text}, but got {actual_mute_unmute_text}. ")
        
        expected_play_pause_text = lang_settings["consumerButtonAction"]["playPause"]
        actual_play_pause_text = self.fc.fd["pen_control"].get_lower_barrel_cons_play_pause()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play/Pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        
        expected_right_arrow_key_text = lang_settings["consumerButtonAction"]["rightArrowKey"]
        actual_right_arrow_key_text = self.fc.fd["pen_control"].get_lower_barrel_cons_right_arrow_key()
        soft_assertion.assert_equal(actual_right_arrow_key_text, expected_right_arrow_key_text, f"Right arrow key text is not matching, expected string text is {expected_right_arrow_key_text}, but got {actual_right_arrow_key_text}. ")
        self.driver.swipe(direction="down", distance=1)
        
        expected_left_arrow_key_text = lang_settings["consumerButtonAction"]["leftArrowKey"]
        actual_left_arrow_key_text = self.fc.fd["pen_control"].get_lower_barrel_cons_left_arrow_key()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel02.png".format(language))
        soft_assertion.assert_equal(actual_left_arrow_key_text, expected_left_arrow_key_text, f"Left arrow key is not matching, expected string text is {expected_left_arrow_key_text}, but got {actual_left_arrow_key_text}. ")
       
        expected_new_browser_tab_text = lang_settings["consumerButtonAction"]["newBrowserTab"]
        actual_new_browser_tab_text = self.fc.fd["pen_control"].get_lower_barrel_cons_new_browser_tab()
        soft_assertion.assert_equal(actual_new_browser_tab_text, expected_new_browser_tab_text, f"New browser tab text is not matching, expected string text is {expected_new_browser_tab_text}, but got {actual_new_browser_tab_text}. ")
        
        expected_previous_page_text = lang_settings["consumerButtonAction"]["previousPage"]
        actual_previous_page_text = self.fc.fd["pen_control"].get_lower_barrel_cons_previous_page()        
        soft_assertion.assert_equal(actual_previous_page_text, expected_previous_page_text, f"Previous page text is not matching, expected string text is {expected_previous_page_text}, but got {actual_previous_page_text}. ")
        
        expected_next_page_text = lang_settings["consumerButtonAction"]["nextPage"]
        actual_next_page_text = self.fc.fd["pen_control"].get_lower_barrel_cons_next_page()
        soft_assertion.assert_equal(actual_next_page_text, expected_next_page_text, f"Next page text is not matching, expected string text is {expected_next_page_text}, but got {actual_next_page_text}. ")
       
        expected_take_sceenshot_text = lang_settings["consumerButtonAction"]["takeScreenshot"]
        actual_take_sceenshot_text = self.fc.fd["pen_control"].get_lower_barrel_cons_take_screenshot()
        soft_assertion.assert_equal(actual_take_sceenshot_text, expected_take_sceenshot_text, f"Take screenshot text is not matching, expected string text is {expected_take_sceenshot_text}, but got {actual_take_sceenshot_text}. ")
        
        expected_launch_task_manager_text = lang_settings["consumerButtonAction"]["lanuchTaskManager"]
        actual_launch_task_manager_text = self.fc.fd["pen_control"].get_lower_barrel_cons_launch_task_manager()
        soft_assertion.assert_equal(actual_launch_task_manager_text, expected_launch_task_manager_text, f"Launch task manager text is not matching, expected string text is {expected_launch_task_manager_text}, but got {actual_launch_task_manager_text}. ")
        self.driver.swipe(direction="down", distance=1)
        
        expected_switch_between_apps_text = lang_settings["consumerButtonAction"]["switchBetweenApps"]
        actual_switch_between_apps_text = self.fc.fd["pen_control"].get_lower_barrel_cons_switch_berween_apps()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel03.png".format(language))
        soft_assertion.assert_equal(actual_switch_between_apps_text, expected_switch_between_apps_text, f"Switch between apps text is not matching, expected string text is {expected_switch_between_apps_text}, but got {actual_switch_between_apps_text}. ")
        
        expected_show_the_desktop_text = lang_settings["consumerButtonAction"]["showTheDesktop"]
        actual_show_the_desktop_text = self.fc.fd["pen_control"].get_lower_barrel_cons_show_the_desktop()
        soft_assertion.assert_equal(actual_show_the_desktop_text, expected_show_the_desktop_text, f"Show the desktop text is not matching, expected string text is {expected_show_the_desktop_text}, but got {actual_show_the_desktop_text}. ")
       
        expected_right_click_text = lang_settings["consumerButtonAction"]["rightClick"]
        actual_right_click_text = self.fc.fd["pen_control"].get_lower_barrel_cons_right_click()
        soft_assertion.assert_equal(actual_right_click_text, expected_right_click_text, f"Right click text is not matching, expected string text is {expected_right_click_text}, but got {actual_right_click_text}. ")
       
        expected_disable_pen_buttons_text = lang_settings["consumerButtonAction"]["disablePenButtons"]
        actual_disable_pen_buttons_text = self.fc.fd["pen_control"].get_lower_barrel_cons_disable_pen_buttons()
        soft_assertion.assert_equal(actual_disable_pen_buttons_text, expected_disable_pen_buttons_text, f"Disable pen buttons text is not matching, expected string text is {expected_disable_pen_buttons_text}, but got {actual_disable_pen_buttons_text}. ")
        
        expected_scroll_text = lang_settings["consumerButtonAction"]["scroll"]
        actual_scroll_text = self.fc.fd["pen_control"].get_lower_barrel_cons_scroll()
        soft_assertion.assert_equal(actual_scroll_text, expected_scroll_text, f"Scroll text is not matching, expected string text is {expected_scroll_text}, but got {actual_scroll_text}. ")
        
        expected_erase_text = lang_settings["consumerButtonAction"]["erase"]
        actual_erase_text = self.fc.fd["pen_control"].get_lower_barrel_cons_erase()
        soft_assertion.assert_equal(actual_erase_text, expected_erase_text, f"Erase text is not matching, expected string text is {expected_erase_text}, but got {actual_erase_text}. ")
        
        self.fc.fd["pen_control"].click_lower_barrel_cons_right_click()
        
        # Restore Default Settings
        expected_restore_default_settings_text = lang_settings["resetToDefaultButton"]["title"]
        actual_restore_default_settings_text = self.fc.fd["pen_control"].get_restore_btn_text()
        soft_assertion.assert_equal(actual_restore_default_settings_text, expected_restore_default_settings_text, f"Restore Default Settings text is not matching, expected string text is {expected_restore_default_settings_text}, but got {actual_restore_default_settings_text}. ")
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
        soft_assertion.raise_assertion_errors()
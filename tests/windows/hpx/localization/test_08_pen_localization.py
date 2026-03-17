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

    def test_08_pen_module_C33053784(self, language):
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
        # click info icon
        self.fc.fd["pen_control"].click_info_icon()
        # product number
        expected_product_number_text = lang_settings["penHeader"]["productNumber"]
        self.fc.fd["pen_control"].click_product_number_stg()
        actual_product_number_text = self.fc.fd["pen_control"].get_product_number_stg_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_i_icon_info.png".format(language))
        soft_assertion.assert_equal(actual_product_number_text, expected_product_number_text, f"Product number text is not matching, expected string text is {expected_product_number_text}, but got {actual_product_number_text}. ")
        # serial number
        expected_serial_number_text = lang_settings["penHeader"]["serialNumber"]
        self.fc.fd["pen_control"].get_serial_number_stg_text()
        actual_serial_number_text = self.fc.fd["pen_control"].get_serial_number_text()
        soft_assertion.assert_equal(actual_serial_number_text, expected_serial_number_text, f"Serial number text is not matching, expected string text is {expected_serial_number_text}, but got {actual_serial_number_text}. ")
        # firmware version
        expected_firmware_version_text = lang_settings["penHeader"]["firmwareVersion"]
        self.fc.fd["pen_control"].click_firmware_version_stg()
        actual_firmware_version_text = self.fc.fd["pen_control"].get_firmware_version_text()
        soft_assertion.assert_equal(actual_firmware_version_text, expected_firmware_version_text, f"Firmware version text is not matching, expected string text is {expected_firmware_version_text}, but got {actual_firmware_version_text}. ")
        self.fc.fd["pen_control"].click_info_icon()
        # Top Button
        expected_top_button_text = lang_settings["topButton"]["title"]
        actual_top_button_text = self.fc.fd["pen_control"].get_top_btn_text()
        soft_assertion.assert_equal(actual_top_button_text, expected_top_button_text, f"Top button text is not matching, expected string text is {expected_top_button_text}, but got {actual_top_button_text}. ")
        # Single Press
        expected_single_press_text = lang_settings["topButton"]["subTitle"]["singlePress"]
        actual_single_press_text = self.fc.fd["pen_control"].get_single_press_text()
        soft_assertion.assert_equal(actual_single_press_text, expected_single_press_text, f"Single Press text is not matching, expected string text is {expected_single_press_text}, but got {actual_single_press_text}. ")
        # single press drop down elements
        self.fc.fd["pen_control"].click_single_press_dd()
        expected_touch_on_off_text = lang_settings["commonButtonAction"]["touchOnOff"]
        actual_touch_on_off_text = self.fc.fd["pen_control"].get_single_press_touch_on_off()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_single_press01.png".format(language))
        soft_assertion.assert_equal(actual_touch_on_off_text, expected_touch_on_off_text, f"Touch on off text is not matching, expected string text is {expected_touch_on_off_text}, but got {actual_touch_on_off_text}. ")
        expected_window_search_text = lang_settings["commonButtonAction"]["windowsSearch"]
        actual_window_search_text = self.fc.fd["pen_control"].get_single_press_window_search()
        soft_assertion.assert_equal(actual_window_search_text, expected_window_search_text, f"Window Search text is not matching, expected string text is {expected_window_search_text}, but got {actual_window_search_text}. ")
        expected_ms_white_board_text = lang_settings["commonButtonAction"]["msWhiteBoard"]
        actual_ms_white_board_text = self.fc.fd["pen_control"].get_single_press_ms_white_board()
        soft_assertion.assert_equal(actual_ms_white_board_text, expected_ms_white_board_text, f"MS White Board text is not matching, expected string text is {expected_ms_white_board_text}, but got {actual_window_search_text}. ")
        expected_screen_snip_text = lang_settings["commonButtonAction"]["screenSnipping"]
        actual_screen_snip_text = self.fc.fd["pen_control"].get_single_press_screen_snip()
        soft_assertion.assert_equal(actual_screen_snip_text, expected_screen_snip_text, f"Screen Snipping text is not matching, expected string text is {expected_screen_snip_text}, but got {actual_screen_snip_text}. ")
        expected_sticky_notes_text = lang_settings["commonButtonAction"]["stickyNote"]
        actual_sticky_notes_text = self.fc.fd["pen_control"].get_single_press_sticky_notes()
        soft_assertion.assert_equal(actual_sticky_notes_text, expected_sticky_notes_text, f"Sticky Note text is not matching, expected string text is {expected_sticky_notes_text}, but got {actual_sticky_notes_text}. ")
        expected_page_up_text = lang_settings["commonButtonAction"]["pageUp"]
        actual_page_up_text = self.fc.fd["pen_control"].get_single_press_page_up()
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Page up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        expected_page_down_text = lang_settings["commonButtonAction"]["pageDown"]
        actual_page_down_text = self.fc.fd["pen_control"].get_single_press_page_down()
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"Page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        expected_play_pause_text = lang_settings["commonButtonAction"]["playPause"]
        actual_play_pause_text = self.fc.fd["pen_control"].get_single_press_play_pause()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        expected_next_track_text = lang_settings["commonButtonAction"]["nextTrack"]
        actual_next_track_text = self.fc.fd["pen_control"].get_single_press_next_track()
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"Next Track text is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        expected_previus_track_text = lang_settings["commonButtonAction"]["previousTrack"]
        actual_previus_track_text = self.fc.fd["pen_control"].get_single_press_previus_track()
        soft_assertion.assert_equal(actual_previus_track_text, expected_previus_track_text, f"Previous track text is not matching, expected string text is {expected_previus_track_text}, but got {actual_previus_track_text}. ")
        self.driver.swipe(direction="down", distance=1)
        expected_volume_up_text = lang_settings["commonButtonAction"]["volumeUp"]
        actual_volume_up_text = self.fc.fd["pen_control"].get_single_press_volume_up()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_single_press02.png".format(language))
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        expected_volume_down_text = lang_settings["commonButtonAction"]["volumeDown"]
        actual_volume_down_text = self.fc.fd["pen_control"].get_single_press_volume_down()
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"Volume down text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        expected_mute_audio_text = lang_settings["commonButtonAction"]["muteAudio"]
        actual_mute_audio_text = self.fc.fd["pen_control"].get_single_press_mute_audio()
        soft_assertion.assert_equal(actual_mute_audio_text, expected_mute_audio_text, f"Mute audio text is not matching, expected string text is {expected_mute_audio_text}, but got {actual_mute_audio_text}. ")
        expected_disable_text = lang_settings["commonButtonAction"]["disabled"]
        actual_disable_text = self.fc.fd["pen_control"].get_single_press_disable()
        soft_assertion.assert_equal(actual_disable_text, expected_disable_text, f"Disable text is not matching, expected string text is {expected_disable_text}, but got {actual_disable_text}. ")
        expected_pen_menu=lang_settings["commonButtonAction"]["penMenu"]
        actual_pen_menu_text=self.fc.fd["pen_control"].get_single_press_pen_menu()
        soft_assertion.assert_equal(actual_pen_menu_text, expected_pen_menu, f"Pen menu text is not matching, expected string text is {expected_pen_menu}, but got {actual_pen_menu_text}. ")
        self.fc.fd["pen_control"].click_ms_white_board()
        time.sleep(2)
        # Double Press
        expected_double_press_text = lang_settings["topButton"]["subTitle"]["doublePress"]
        actual_double_press_text = self.fc.fd["pen_control"].get_double_press_text()
        soft_assertion.assert_equal(actual_double_press_text, expected_double_press_text, f"Double Press text is not matching, expected string text is {expected_double_press_text}, but got {actual_double_press_text}. ")
        # double press elements--
        self.fc.fd["pen_control"].click_double_press_dd()
        time.sleep(2)
        expected_touch_on_off_text = lang_settings["commonButtonAction"]["touchOnOff"]
        actual_touch_on_off_text = self.fc.fd["pen_control"].get_double_press_touch_on_off()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_double_press01.png".format(language))
        soft_assertion.assert_equal(actual_touch_on_off_text, expected_touch_on_off_text, f"Touch off text is not matching, expected string text is {expected_touch_on_off_text}, but got {actual_touch_on_off_text}. ")
        expected_window_search_text = lang_settings["commonButtonAction"]["windowsSearch"]
        actual_window_search_text = self.fc.fd["pen_control"].get_double_press_window_search()
        soft_assertion.assert_equal(actual_window_search_text, expected_window_search_text, f"Window Search text is not matching, expected string text is {expected_window_search_text}, but got {actual_window_search_text}. ")
        expected_ms_white_board_text = lang_settings["commonButtonAction"]["msWhiteBoard"]
        actual_ms_white_board_text = self.fc.fd["pen_control"].get_double_press_ms_white_board()
        soft_assertion.assert_equal(actual_ms_white_board_text, expected_ms_white_board_text, f"MS White board text is not matching, expected string text is {expected_ms_white_board_text}, but got {actual_ms_white_board_text}. ")
        expected_screen_snip_text = lang_settings["commonButtonAction"]["screenSnipping"]
        actual_screen_snip_text = self.fc.fd["pen_control"].get_double_press_screen_snip()
        soft_assertion.assert_equal(actual_screen_snip_text, expected_screen_snip_text, f"Screen snipping text is not matching., expected string text is {expected_screen_snip_text}, but got {actual_screen_snip_text}. ")
        expected_sticky_notes_text = lang_settings["commonButtonAction"]["stickyNote"]
        actual_sticky_notes_text = self.fc.fd["pen_control"].get_double_press_sticky_notes()
        soft_assertion.assert_equal(actual_sticky_notes_text, expected_sticky_notes_text, f"Sticky note text is not matching., expected string text is {expected_sticky_notes_text}, but got {actual_sticky_notes_text}. ")
        expected_page_up_text = lang_settings["commonButtonAction"]["pageUp"]
        actual_page_up_text = self.fc.fd["pen_control"].get_double_press_page_up()
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Page up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        expected_page_down_text = lang_settings["commonButtonAction"]["pageDown"]
        actual_page_down_text = self.fc.fd["pen_control"].get_double_press_page_down()
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"Page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        expected_play_pause_text = lang_settings["commonButtonAction"]["playPause"]
        actual_play_pause_text = self.fc.fd["pen_control"].get_double_press_play_pause()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        expected_next_track_text = lang_settings["commonButtonAction"]["nextTrack"]
        actual_next_track_text = self.fc.fd["pen_control"].get_double_press_next_track()
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"Next track is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        expected_previus_track_text = lang_settings["commonButtonAction"]["previousTrack"]
        actual_previus_track_text = self.fc.fd["pen_control"].get_double_press_previus_track()
        soft_assertion.assert_equal(actual_previus_track_text, expected_previus_track_text, f"Previous track text is not matching, expected string text is {expected_previus_track_text}, but got {actual_previus_track_text}. ")
        self.driver.swipe(direction="down", distance=1)
        expected_volume_up_text = lang_settings["commonButtonAction"]["volumeUp"]
        actual_volume_up_text = self.fc.fd["pen_control"].get_double_press_volume_up()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_double_press02.png".format(language))
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        expected_volume_down_text = lang_settings["commonButtonAction"]["volumeDown"]
        actual_volume_down_text = self.fc.fd["pen_control"].get_double_press_volume_down()
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"Volume down text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        expected_mute_audio_text = lang_settings["commonButtonAction"]["muteAudio"]
        actual_mute_audio_text = self.fc.fd["pen_control"].get_double_press_mute_audio()
        soft_assertion.assert_equal(actual_mute_audio_text, expected_mute_audio_text, f"Mute audio text is not matching, expected string text is {expected_mute_audio_text}, but got {actual_mute_audio_text}. ")
        expected_disable_text = lang_settings["commonButtonAction"]["disabled"]
        actual_disable_text = self.fc.fd["pen_control"].get_double_press_disable()
        soft_assertion.assert_equal(actual_disable_text, expected_disable_text, f"Disable text is not matching, expected string text is {expected_disable_text}, but got {actual_disable_text}. ")
        expected_pen_menu_text = lang_settings["commonButtonAction"]["penMenu"]
        actual_pen_mune_text = self.fc.fd["pen_control"].get_double_press_pen_menu()
        soft_assertion.assert_equal(actual_pen_mune_text, expected_pen_menu_text, f"Pen menu text is not matching, expected string text is {expected_pen_menu_text}, but got {actual_pen_mune_text}. ")
        self.fc.fd["pen_control"].click_double_press_ms_white_board()
        time.sleep(2)
        # Long Press
        expected_long_press_text = lang_settings["topButton"]["subTitle"]["longPress"]
        actual_long_press_text = self.fc.fd["pen_control"].get_long_press_text()
        soft_assertion.assert_equal(actual_long_press_text, expected_long_press_text, f"Long Press text is not matching, expected string text is {expected_long_press_text}, but got {actual_long_press_text}. ")
        # long press elements---
        self.fc.fd["pen_control"].click_long_press_dd()
        time.sleep(2)
        self.driver.swipe(direction="up", distance=2)
        expected_touch_on_off_text = lang_settings["commonButtonAction"]["touchOnOff"]
        actual_touch_on_off_text = self.fc.fd["pen_control"].get_long_press_touch_on_off()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_press01.png".format(language))
        soft_assertion.assert_equal(actual_touch_on_off_text, expected_touch_on_off_text, f"Touch on off text is not matching, expected string text is {expected_touch_on_off_text}, but got {actual_touch_on_off_text}. ")
        expected_window_search_text = lang_settings["commonButtonAction"]["windowsSearch"]
        actual_window_search_text = self.fc.fd["pen_control"].get_long_press_window_search()
        soft_assertion.assert_equal(actual_window_search_text, expected_window_search_text, f"Window Search is not matching, expected string text is {expected_window_search_text}, but got {actual_window_search_text}. ")
        expected_ms_white_board_text = lang_settings["commonButtonAction"]["msWhiteBoard"]
        actual_ms_white_board_text = self.fc.fd["pen_control"].get_long_press_ms_white_board()
        soft_assertion.assert_equal(actual_ms_white_board_text, expected_ms_white_board_text, f"MS White board text is not matching, expected string text is {expected_ms_white_board_text}, but got {actual_ms_white_board_text}. ")
        expected_screen_snip_text = lang_settings["commonButtonAction"]["screenSnipping"]
        actual_screen_snip_text = self.fc.fd["pen_control"].get_long_press_screen_snip()
        soft_assertion.assert_equal(actual_screen_snip_text, expected_screen_snip_text, f"Screen snipping text is not matching, expected string text is {expected_screen_snip_text}, but got {actual_screen_snip_text}. ")
        expected_sticky_notes_text = lang_settings["commonButtonAction"]["stickyNote"]
        actual_sticky_notes_text = self.fc.fd["pen_control"].get_long_press_sticky_notes()
        soft_assertion.assert_equal(actual_sticky_notes_text, expected_sticky_notes_text, f"Sticky note text is not matching, expected string text is {expected_sticky_notes_text}, but got {actual_sticky_notes_text}. ")
        expected_page_up_text = lang_settings["commonButtonAction"]["pageUp"]
        actual_page_up_text = self.fc.fd["pen_control"].get_long_press_page_up()
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Page up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        expected_page_down_text = lang_settings["commonButtonAction"]["pageDown"]
        actual_page_down_text = self.fc.fd["pen_control"].get_long_press_page_down()
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"Page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        expected_play_pause_text = lang_settings["commonButtonAction"]["playPause"]
        actual_play_pause_text = self.fc.fd["pen_control"].get_long_press_play_pause()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        expected_next_track_text = lang_settings["commonButtonAction"]["nextTrack"]
        actual_next_track_text = self.fc.fd["pen_control"].get_long_press_next_track()
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"Next track text is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        expected_previus_track_text = lang_settings["commonButtonAction"]["previousTrack"]
        actual_previus_track_text = self.fc.fd["pen_control"].get_long_press_previus_track()
        soft_assertion.assert_equal(actual_previus_track_text, expected_previus_track_text, f"Previous track text is not matching, expected string text is {expected_previus_track_text}, but got {actual_previus_track_text}. ")
        self.driver.swipe(direction="down", distance=1)
        expected_volume_up_text = lang_settings["commonButtonAction"]["volumeUp"]
        actual_volume_up_text = self.fc.fd["pen_control"].get_long_press_volume_up()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_press02.png".format(language))
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        expected_volume_down_text = lang_settings["commonButtonAction"]["volumeDown"]
        actual_volume_down_text = self.fc.fd["pen_control"].get_long_press_volume_down()
        soft_assertion.assert_equal(actual_volume_down_text, expected_volume_down_text, f"Volume down text is not matching, expected string text is {expected_volume_down_text}, but got {actual_volume_down_text}. ")
        expected_mute_audio_text = lang_settings["commonButtonAction"]["muteAudio"]
        actual_mute_audio_text = self.fc.fd["pen_control"].get_long_press_mute_audio()
        soft_assertion.assert_equal(actual_mute_audio_text, expected_mute_audio_text, f"Mute audio text is not matching, expected string text is {expected_mute_audio_text}, but got {actual_mute_audio_text}. ")
        expected_disable_text = lang_settings["commonButtonAction"]["disabled"]
        actual_disable_text = self.fc.fd["pen_control"].get_long_press_disable()
        soft_assertion.assert_equal(actual_disable_text, expected_disable_text, f"Disable text is not matching, expected string text is {expected_disable_text}, but got {actual_disable_text}. ")
        expected_pen_menu_text = lang_settings["commonButtonAction"]["penMenu"]
        actual_pen_menu_text = self.fc.fd["pen_control"].get_long_press_pen_menu()
        soft_assertion.assert_equal(actual_pen_menu_text, expected_pen_menu_text, f"Pen menu text is not matching, expected string text is {expected_pen_menu_text}, but got {actual_pen_menu_text}. ")
        self.fc.fd["pen_control"].click_long_press_ms_white_board()
        # Upper Barrel Button
        expected_upper_barrel_button_text = lang_settings["upperBarrelButton"]["title"]
        actual_upper_barrel_button_text = self.fc.fd["pen_control"].get_upper_barrel_text()
        soft_assertion.assert_equal(actual_upper_barrel_button_text, expected_upper_barrel_button_text, f"Upper Barel Button text is not matching, expected string text is {expected_upper_barrel_button_text}, but got {actual_upper_barrel_button_text}. ")
        self.driver.swipe(direction="down", distance=1)
        # Hover-Click under upper barrel button
        expected_hover_click_upper_barrel_button_hover_text = lang_settings["hoverToggle"]["title"]
        actual_hover_click_upper_barrel_button_hover_text = self.fc.fd["pen_control"].get_hover_click_upper_barrel_text()
        soft_assertion.assert_equal(actual_hover_click_upper_barrel_button_hover_text, expected_hover_click_upper_barrel_button_hover_text, f"Hover-Click  text is not matching, expected string text is {expected_hover_click_upper_barrel_button_hover_text}, but got {actual_hover_click_upper_barrel_button_hover_text}. ")
        self.fc.fd["pen_control"].click_upper_barrel_tool_tip()
        # upper barrel tool tip
        expected_upper_barrel_tool_tip_text = lang_settings["hoverToggle"]["tooltip"]
        actual_upper_barrel_tool_tip_text = self.fc.fd["pen_control"].get_upper_barrel_tool_tip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_upper_barrel_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_upper_barrel_tool_tip_text, expected_upper_barrel_tool_tip_text, f"Upper barrel tool tip text is not matching, expected string text is {expected_upper_barrel_tool_tip_text}, but got {actual_upper_barrel_tool_tip_text}. ")
        # click upper barrel dd
        self.fc.fd["pen_control"].click_upper_barrel_dropdown()
        expected_touch_on_off_text = lang_settings["commonButtonAction"]["touchOnOff"]
        actual_touch_on_off_text = self.fc.fd["pen_control"].get_upper_barrel_touch_on_off()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel01.png".format(language))
        soft_assertion.assert_equal(actual_touch_on_off_text, expected_touch_on_off_text, f"Touch on off text is not matching, expected string text is {expected_touch_on_off_text}, but got {actual_touch_on_off_text}. ")
        expected_erase_text = lang_settings["barrelButtonAction"]["erase"]
        actual_erase_text = self.fc.fd["pen_control"].get_upper_barrel_erase()
        soft_assertion.assert_equal(actual_erase_text, expected_erase_text, f"Erase text is not matching, expected string text is {expected_erase_text}, but got {actual_erase_text}. ")
        expected_barrel_right_text = lang_settings["barrelButtonAction"]["rightClick"]
        actual_barrel_right_text = self.fc.fd["pen_control"].get_upper_barrel_right_click()
        soft_assertion.assert_equal(actual_barrel_right_text, expected_barrel_right_text, f"Right click text is not matching, expected string text is {expected_barrel_right_text}, but got {actual_barrel_right_text}. ")
        expected_page_up_text = lang_settings["commonButtonAction"]["pageUp"]
        actual_page_up_text = self.fc.fd["pen_control"].get_upper_barrel_page_up()
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Page up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        expected_page_down_text = lang_settings["commonButtonAction"]["pageDown"]
        actual_page_down_text = self.fc.fd["pen_control"].get_upper_barrel_page_down()
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        expected_go_back_text = lang_settings["barrelButtonAction"]["goBack"]
        actual_go_back_text = self.fc.fd["pen_control"].get_upper_barrel_go_back()
        soft_assertion.assert_equal(actual_go_back_text, expected_go_back_text, f"Go back text is not matching, expected string text is {expected_go_back_text}, but got {actual_go_back_text}. ")
        expected_go_forward_text = lang_settings["barrelButtonAction"]["goForward"]
        actual_go_forward_text = self.fc.fd["pen_control"].get_upper_barrel_go_forward()
        soft_assertion.assert_equal(actual_go_forward_text, expected_go_forward_text, f"GO forward text is not matching, expected string text is {expected_go_forward_text}, but got {actual_go_forward_text}. ")
        expected_copy_text = lang_settings["barrelButtonAction"]["copy"]
        actual_copy_text = self.fc.fd["pen_control"].get_upper_barrel_copy()
        soft_assertion.assert_equal(actual_copy_text, expected_copy_text, f"Copy text is not matching, expected string text is {expected_copy_text}, but got {actual_copy_text}. ")
        expected_paste_text = lang_settings["barrelButtonAction"]["paste"]
        actual_paste_text = self.fc.fd["pen_control"].get_upper_barrel_paste()
        soft_assertion.assert_equal(actual_paste_text, expected_paste_text, f"Paste text is not matching, expected string text is {expected_paste_text}, but got {actual_paste_text}. ")
        expected_undo_text = lang_settings["barrelButtonAction"]["undo"]
        actual_undo_text = self.fc.fd["pen_control"].get_upper_barrel_undo()
        soft_assertion.assert_equal(actual_undo_text, expected_undo_text, f"Undo text is not matching, expected string text is {expected_undo_text}, but got {actual_undo_text}. ")
        expected_redo_text = lang_settings["barrelButtonAction"]["redo"]
        actual_redo_text = self.fc.fd["pen_control"].get_upper_barrel_redo()
        soft_assertion.assert_equal(actual_redo_text, expected_redo_text, f"Redo text is not matching, expected string text is {expected_redo_text}, but got {actual_redo_text}. ")
        expected_left_click_text = lang_settings["barrelButtonAction"]["leftClick"]
        actual_left_click_text = self.fc.fd["pen_control"].get_upper_barrel_left_click()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel02.png".format(language))
        soft_assertion.assert_equal(expected_left_click_text, actual_left_click_text, f"Left click is not matching, expected string text is {actual_left_click_text}, but got {expected_left_click_text}. ")
        expected_middle_click_text = lang_settings["barrelButtonAction"]["middleClick"]
        actual_middle_click_text = self.fc.fd["pen_control"].get_upper_barrel_middle_click()
        soft_assertion.assert_equal(actual_middle_click_text, expected_middle_click_text, f"middle click text is not matching, expected string text is {expected_middle_click_text}, but got {actual_middle_click_text}. ")
        self.driver.swipe(direction="down", distance=0.75)
        expected_fourth_click_text = lang_settings["barrelButtonAction"]["forthClick"]
        actual_fourth_click_text = self.fc.fd["pen_control"].get_upper_barrel_fourth_click()
        soft_assertion.assert_equal(actual_fourth_click_text, expected_fourth_click_text, f"forth click text is not matching, expected string text is {expected_fourth_click_text}, but got {actual_fourth_click_text}. ")
        expected_fifth_click_text = lang_settings["barrelButtonAction"]["fifthClick"]
        actual_fifth_click_text = self.fc.fd["pen_control"].get_upper_barrel_fifth_click()
        soft_assertion.assert_equal(actual_fifth_click_text, expected_fifth_click_text, f"fifth click text is not matching, expected string text is {expected_fifth_click_text}, but got {actual_fifth_click_text}. ")
        expected_window_search_text = lang_settings["commonButtonAction"]["windowsSearch"]
        actual_window_search_text = self.fc.fd["pen_control"].get_upper_barrel_window_search()
        soft_assertion.assert_equal(actual_window_search_text, expected_window_search_text, f"Window Search text is not matching, expected string text is {expected_window_search_text}, but got {actual_window_search_text}. ")
        expected_ms_whiteboard_text = lang_settings["commonButtonAction"]["msWhiteBoard"]
        actual_ms_whiteboard_text = self.fc.fd["pen_control"].get_upper_barrel_ms_whiteboard()
        soft_assertion.assert_equal(actual_ms_whiteboard_text, expected_ms_whiteboard_text, f"MS White board is not matching, expected string text is {expected_ms_whiteboard_text}, but got {actual_ms_whiteboard_text}. ")
        self.driver.swipe(direction="down", distance=1)
        expected_screen_snipping_text = lang_settings["commonButtonAction"]["screenSnipping"]
        actual_screen_snipping_text = self.fc.fd["pen_control"].get_upper_barrel_screen_snipping()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel03.png".format(language))
        soft_assertion.assert_equal(actual_screen_snipping_text, expected_screen_snipping_text, f"Screen snipping text is not matching, expected string text is {expected_screen_snipping_text}, but got {actual_screen_snipping_text}. ")
        expected_switch_application_text = lang_settings["commonButtonAction"]["switchApp"]
        actual_switch_application_text = self.fc.fd["pen_control"].get_upper_barrel_switch_application()
        soft_assertion.assert_equal(actual_switch_application_text, expected_switch_application_text, f"Switch app text is not matching, expected string text is {expected_switch_application_text}, but got {actual_switch_application_text}. ")
        expected_web_browser_text = lang_settings["barrelButtonAction"]["openBrowser"]
        actual_web_browser_text = self.fc.fd["pen_control"].get_upper_barrel_web_browser()
        soft_assertion.assert_equal(actual_web_browser_text, expected_web_browser_text, f"open browser text is not matching, expected string text is {expected_web_browser_text}, but got {actual_web_browser_text}. ")
        expected_open_default_email_text = lang_settings["barrelButtonAction"]["openMail"]
        actual_open_default_email_text = self.fc.fd["pen_control"].get_upper_barrel_email()
        soft_assertion.assert_equal(actual_open_default_email_text, expected_open_default_email_text, f"open mail text is not matching, expected string text is {expected_open_default_email_text}, but got {actual_open_default_email_text}. ")
        expected_play_pause_text = lang_settings["commonButtonAction"]["playPause"]
        actual_play_pause_text = self.fc.fd["pen_control"].get_upper_barrel_play_pause()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        expected_next_track_text = lang_settings["commonButtonAction"]["nextTrack"]
        actual_next_track_text = self.fc.fd["pen_control"].get_upper_barrel_next_track()
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"Next track text is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        self.driver.swipe(direction="down", distance=1)
        expected_previous_track_text = lang_settings["commonButtonAction"]["previousTrack"]
        actual_previous_track_text = self.fc.fd["pen_control"].get_upper_barrel_previous_track()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_long_upper_barrel04.png".format(language))
        soft_assertion.assert_equal(actual_previous_track_text, expected_previous_track_text, f"previous track text is not matching, expected string text is {expected_previous_track_text}, but got {actual_previous_track_text}. ")
        expected_volume_up_text = lang_settings["commonButtonAction"]["volumeUp"]
        actual_volume_up_text = self.fc.fd["pen_control"].get_upper_barrel_volume_up()
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        expected_volume_down_email_text = lang_settings["commonButtonAction"]["volumeDown"]
        actual_volume_down_email_text = self.fc.fd["pen_control"].get_upper_barrel_volume_down()
        soft_assertion.assert_equal(actual_volume_down_email_text, expected_volume_down_email_text, f"Volume down text is not matching, expected string text is {expected_volume_down_email_text}, but got {actual_volume_down_email_text}. ")
        expected_mute_text = lang_settings["commonButtonAction"]["muteAudio"]
        actual_mute_text = self.fc.fd["pen_control"].get_upper_barrel_mute()
        soft_assertion.assert_equal(actual_mute_text, expected_mute_text, f"Mute audio text is not matching, expected string text is {expected_mute_text}, but got {actual_mute_text}. ")
        expected_disable_text = lang_settings["commonButtonAction"]["disabled"]
        actual_disable_text = self.fc.fd["pen_control"].get_upper_barrel_disable()
        soft_assertion.assert_equal(actual_disable_text, expected_disable_text, f"Disable text is not matching, expected string text is {expected_disable_text}, but got {actual_disable_text}. ")
        expected_pen_menu_text = lang_settings["commonButtonAction"]["penMenu"]
        actual_pen_menu_text = self.fc.fd["pen_control"].get_upper_barrel_pen_menu()
        soft_assertion.assert_equal(actual_pen_menu_text, expected_pen_menu_text, f"Pen menu text is not matching, expected string text is {expected_pen_menu_text}, but got {actual_pen_menu_text}. ")
        self.driver.swipe(direction="up", distance=2)
        self.fc.fd["pen_control"].click_upper_barrel_right_click()
        self.driver.swipe(direction="down", distance=1)
        # Lower Barrel Button
        expected_lower_barrel_button_text = lang_settings["lowerBarrelButton"]["title"]
        actual_lower_barrel_button_text = self.fc.fd["pen_control"].get_lower_barrel_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_homepage_01.png".format(language))
        soft_assertion.assert_equal(actual_lower_barrel_button_text, expected_lower_barrel_button_text, f"Lower Barrel Button text is not matching, expected string text is {expected_lower_barrel_button_text}, but got {actual_lower_barrel_button_text}. ")
        # Hover-Click under lower barrel button
        expected_hover_click_lower_barrel_button_text = lang_settings["hoverToggle"]["title"]
        actual_hover_click_lower_barrel_button_text = self.fc.fd["pen_control"].get_hover_click_lower_barrel_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_low_barrel_01.png".format(language))
        soft_assertion.assert_equal(actual_hover_click_lower_barrel_button_text, expected_hover_click_lower_barrel_button_text, f"Hover -click text is not matching , expected string text is {expected_hover_click_lower_barrel_button_text}, but got {actual_hover_click_lower_barrel_button_text}. ")
        self.fc.fd["pen_control"].click_lower_barrel_tooltip()
        # lower barrel tool tip
        expected_lower_barrel_tool_tip_text = lang_settings["hoverToggle"]["tooltip"]
        actual_lower_barrel_tool_tip_text = self.fc.fd["pen_control"].get_lower_barrel_tool_tip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_low_barrel_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_lower_barrel_tool_tip_text, expected_lower_barrel_tool_tip_text, f"lower barrel tool tip text is not matching, expected string text is {expected_lower_barrel_tool_tip_text}, but got {actual_lower_barrel_tool_tip_text}. ")
        # click lower barrel dd
        self.fc.fd["pen_control"].click_lower_barrel_dropdown()
        expected_touch_on_off_text = lang_settings["commonButtonAction"]["touchOnOff"]
        actual_touch_on_off_text = self.fc.fd["pen_control"].get_lower_barrel_touch_on_off()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_low_barrel_02.png".format(language))
        soft_assertion.assert_equal(actual_touch_on_off_text, expected_touch_on_off_text, f"Touch on off text is not matching, expected string text is {expected_touch_on_off_text}, but got {actual_touch_on_off_text}. ")
        expected_erase_text = lang_settings["barrelButtonAction"]["erase"]
        actual_erase_text = self.fc.fd["pen_control"].get_lower_barrel_erase()
        soft_assertion.assert_equal(actual_erase_text, expected_erase_text, f"Erase text is not matching, expected string text is {expected_erase_text}, but got {actual_erase_text}. ")
        expected_barrel_right_text = lang_settings["barrelButtonAction"]["rightClick"]
        actual_barrel_right_text = self.fc.fd["pen_control"].get_lower_barrel_right_click()
        soft_assertion.assert_equal(actual_barrel_right_text, expected_barrel_right_text, f"Right click text is not matching, expected string text is {expected_barrel_right_text}, but got {actual_barrel_right_text}. ")
        expected_page_up_text = lang_settings["commonButtonAction"]["pageUp"]
        actual_page_up_text = self.fc.fd["pen_control"].get_lower_barrel_page_up()
        soft_assertion.assert_equal(actual_page_up_text, expected_page_up_text, f"Page up text is not matching, expected string text is {expected_page_up_text}, but got {actual_page_up_text}. ")
        expected_page_down_text = lang_settings["commonButtonAction"]["pageDown"]
        actual_page_down_text = self.fc.fd["pen_control"].get_lower_barrel_page_down()
        soft_assertion.assert_equal(actual_page_down_text, expected_page_down_text, f"Page down text is not matching, expected string text is {expected_page_down_text}, but got {actual_page_down_text}. ")
        expected_go_back_text = lang_settings["barrelButtonAction"]["goBack"]
        actual_go_back_text = self.fc.fd["pen_control"].get_lower_barrel_go_back()
        soft_assertion.assert_equal(actual_go_back_text, expected_go_back_text, f"GO back text is not macthing, expected string text is {expected_go_back_text}, but got {actual_go_back_text}. ")
        expected_go_forward_text = lang_settings["barrelButtonAction"]["goForward"]
        actual_go_forward_text = self.fc.fd["pen_control"].get_lower_barrel_go_forward()
        soft_assertion.assert_equal(actual_go_forward_text, expected_go_forward_text, f"Go forward text is not matching, expected string text is {expected_go_forward_text}, but got {actual_go_forward_text}. ")
        expected_copy_text = lang_settings["barrelButtonAction"]["copy"]
        actual_copy_text = self.fc.fd["pen_control"].get_lower_barrel_copy()
        soft_assertion.assert_equal(actual_copy_text, expected_copy_text, f"Copy text is not matching, expected string text is {expected_copy_text}, but got {actual_copy_text}. ")
        expected_paste_text = lang_settings["barrelButtonAction"]["paste"]
        actual_paste_text = self.fc.fd["pen_control"].get_lower_barrel_paste()
        soft_assertion.assert_equal(actual_paste_text, expected_paste_text, f"Paste text is not matching, expected string text is {expected_paste_text}, but got {actual_paste_text}. ")
        expected_undo_text = lang_settings["barrelButtonAction"]["undo"]
        actual_undo_text = self.fc.fd["pen_control"].get_lower_barrel_undo()
        soft_assertion.assert_equal(actual_undo_text, expected_undo_text, f"Undo text is not matching, expected string text is {expected_undo_text}, but got {actual_undo_text}. ")
        expected_redo_text = lang_settings["barrelButtonAction"]["redo"]
        actual_redo_text = self.fc.fd["pen_control"].get_lower_barrel_redo()
        soft_assertion.assert_equal(actual_redo_text, expected_redo_text, f"redo text is not matching, expected string text is {expected_redo_text}, but got {actual_redo_text}. ")
        expected_left_click_text = lang_settings["barrelButtonAction"]["leftClick"]
        actual_left_click_text = self.fc.fd["pen_control"].get_lower_barrel_left_click()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_low_barrel_03.png".format(language))
        soft_assertion.assert_equal(expected_left_click_text, actual_left_click_text, f"left click text is not matching, expected string text is {actual_left_click_text}, but got {expected_left_click_text}. ")
        expected_middle_click_text = lang_settings["barrelButtonAction"]["middleClick"]
        actual_middle_click_text = self.fc.fd["pen_control"].get_lower_barrel_middle_click()
        soft_assertion.assert_equal(actual_middle_click_text, expected_middle_click_text, f"middle click text is not matching, expected string text is {expected_middle_click_text}, but got {actual_middle_click_text}. ")
        self.driver.swipe(direction="down", distance=0.75)
        expected_fourth_click_text = lang_settings["barrelButtonAction"]["forthClick"]
        actual_fourth_click_text = self.fc.fd["pen_control"].get_lower_barrel_fourth_click()
        soft_assertion.assert_equal(actual_fourth_click_text, expected_fourth_click_text, f"forth click text is not matching, expected string text is {expected_fourth_click_text}, but got {actual_fourth_click_text}. ")
        expected_fifth_click_text = lang_settings["barrelButtonAction"]["fifthClick"]
        actual_fifth_click_text = self.fc.fd["pen_control"].get_lower_barrel_fifth_click()
        soft_assertion.assert_equal(actual_fifth_click_text, expected_fifth_click_text, f"fifth click text is not matching, expected string text is {expected_fifth_click_text}, but got {actual_fifth_click_text}. ")
        expected_window_search_text = lang_settings["commonButtonAction"]["windowsSearch"]
        actual_window_search_text = self.fc.fd["pen_control"].get_lower_barrel_window_search()
        soft_assertion.assert_equal(actual_window_search_text, expected_window_search_text, f"Window Search text is not matching, expected string text is {expected_window_search_text}, but got {actual_window_search_text}. ")
        expected_ms_whiteboard_text = lang_settings["commonButtonAction"]["msWhiteBoard"]
        actual_ms_whiteboard_text = self.fc.fd["pen_control"].get_lower_barrel_ms_whiteboard()
        soft_assertion.assert_equal(actual_ms_whiteboard_text, expected_ms_whiteboard_text, f"MS White board text is not matching, expected string text is {expected_ms_whiteboard_text}, but got {actual_ms_whiteboard_text}. ")
        self.driver.swipe(direction="down", distance=1)
        expected_screen_snipping_text = lang_settings["commonButtonAction"]["screenSnipping"]
        actual_screen_snipping_text = self.fc.fd["pen_control"].get_lower_barrel_screen_snipping()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_low_barrel_04.png".format(language))
        soft_assertion.assert_equal(actual_screen_snipping_text, expected_screen_snipping_text, f"Screen snipping text is not matching, expected string text is {expected_screen_snipping_text}, but got {actual_screen_snipping_text}. ")
        expected_switch_application_text = lang_settings["commonButtonAction"]["switchApp"]
        actual_switch_application_text = self.fc.fd["pen_control"].get_lower_barrel_switch_application()
        soft_assertion.assert_equal(actual_switch_application_text, expected_switch_application_text, f"Switch app text is not matching, expected string text is {expected_switch_application_text}, but got {actual_switch_application_text}. ")
        expected_web_browser_text = lang_settings["barrelButtonAction"]["openBrowser"]
        actual_web_browser_text = self.fc.fd["pen_control"].get_lower_barrel_web_browser()
        soft_assertion.assert_equal(actual_web_browser_text, expected_web_browser_text, f"open browser text is not matching, expected string text is {expected_web_browser_text}, but got {actual_web_browser_text}. ")
        expected_email_text = lang_settings["barrelButtonAction"]["openMail"]
        actual_email_text = self.fc.fd["pen_control"].get_lower_barrel_email()
        soft_assertion.assert_equal(actual_email_text, expected_email_text, f"open mail text is not matching, expected string text is {expected_email_text}, but got {actual_email_text}. ")
        expected_play_pause_text = lang_settings["commonButtonAction"]["playPause"]
        actual_play_pause_text = self.fc.fd["pen_control"].get_lower_barrel_play_pause()
        soft_assertion.assert_equal(actual_play_pause_text, expected_play_pause_text, f"Play pause text is not matching, expected string text is {expected_play_pause_text}, but got {actual_play_pause_text}. ")
        expected_next_track_text = lang_settings["commonButtonAction"]["nextTrack"]
        actual_next_track_text = self.fc.fd["pen_control"].get_lower_barrel_next_track()
        soft_assertion.assert_equal(actual_next_track_text, expected_next_track_text, f"Next track text is not matching, expected string text is {expected_next_track_text}, but got {actual_next_track_text}. ")
        self.driver.swipe(direction="down", distance=1)
        expected_previous_track_text = lang_settings["commonButtonAction"]["previousTrack"]
        actual_previous_track_text = self.fc.fd["pen_control"].get_lower_barrel_previous_track()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_low_barrel_05.png".format(language))
        soft_assertion.assert_equal(actual_previous_track_text, expected_previous_track_text, f"Previous track text is not matching, expected string text is {expected_previous_track_text}, but got {actual_previous_track_text}. ")
        expected_volume_up_text = lang_settings["commonButtonAction"]["volumeUp"]
        actual_volume_up_text = self.fc.fd["pen_control"].get_lower_barrel_volume_up()
        soft_assertion.assert_equal(actual_volume_up_text, expected_volume_up_text, f"Volume up text is not matching, expected string text is {expected_volume_up_text}, but got {actual_volume_up_text}. ")
        expected_volume_down_email_text = lang_settings["commonButtonAction"]["volumeDown"]
        actual_volume_down_email_text = self.fc.fd["pen_control"].get_lower_barrel_volume_down()
        soft_assertion.assert_equal(actual_volume_down_email_text, expected_volume_down_email_text, f"Volume down text is not matching, expected string text is {expected_volume_down_email_text}, but got {actual_volume_down_email_text}. ")
        expected_mute_text = lang_settings["commonButtonAction"]["muteAudio"]
        actual_mute_text = self.fc.fd["pen_control"].get_lower_barrel_mute_audio()
        soft_assertion.assert_equal(actual_mute_text, expected_mute_text, f"Mute audio text is not matching, expected string text is {expected_mute_text}, but got {actual_mute_text}. ")
        expected_disable_text = lang_settings["commonButtonAction"]["disabled"]
        actual_disable_text = self.fc.fd["pen_control"].get_lower_barrel_disable()
        soft_assertion.assert_equal(actual_disable_text, expected_disable_text, f"Disable text is not matching, expected string text is {expected_disable_text}, but got {actual_disable_text}. ")
        expected_pen_menu_text = lang_settings["commonButtonAction"]["penMenu"]
        actual_pen_menu_text = self.fc.fd["pen_control"].get_lower_barrel_pen_menu()
        soft_assertion.assert_equal(actual_pen_menu_text, expected_pen_menu_text, f"Pen menu text is not matching, expected string text is {expected_pen_menu_text}, but got {actual_pen_menu_text}. ")
        self.driver.swipe(direction="up", distance=2)
        self.driver.swipe(direction="up", distance=2)
        self.fc.fd["pen_control"].click_lower_barrel_erase()
        self.driver.swipe(direction="down", distance=2)
        # Pen Sensitivity
        expected_pen_sensitivity_text = lang_settings["penSensitivity"]["title"]
        actual_pen_sensitivity_text = self.fc.fd["pen_control"].get_pen_sensitivity_title_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pen_control_screenshot/{}_pen_control_homepage03.png".format(language))
        soft_assertion.assert_equal(actual_pen_sensitivity_text, expected_pen_sensitivity_text, f"Pen Sensitivity text is not matching, expected string text is {expected_pen_sensitivity_text}, but got {actual_pen_sensitivity_text}. ")
        # Pressure Sensitivity
        expected_pressure_sensitivity_text = lang_settings["penSensitivity"]["penTipSensitivity"]["title"]
        actual_pressure_sensitivity_text = self.fc.fd["pen_control"].get_pressure_title_text()
        soft_assertion.assert_equal(actual_pressure_sensitivity_text, expected_pressure_sensitivity_text, f"Pressure Sensitivity text is not matching, expected string text is {expected_pressure_sensitivity_text}, but got {actual_pressure_sensitivity_text}. ")
        # Tilt Sensitivity
        expected_tilt_sensitivity_text = lang_settings["penSensitivity"]["penTiltSensitivity"]["title"]
        actual_tilt_sensitivity_text = self.fc.fd["pen_control"].get_tilt_title_text()
        soft_assertion.assert_equal(actual_tilt_sensitivity_text, expected_tilt_sensitivity_text, f"Tilt Sensitivity text is not matching, expected string text is {expected_tilt_sensitivity_text}, but got {actual_tilt_sensitivity_text}. ")
        #  Low--Pressure Sensitivity
        expected_pressure_sensitivity_low_text = lang_settings["penSensitivity"]["penSensitivityLimit"]["low"]
        actual_pressure_sensitivity_low_text = self.fc.fd["pen_control"].get_low_pressure_sensitivity_text()
        soft_assertion.assert_equal(actual_pressure_sensitivity_low_text, expected_pressure_sensitivity_low_text, f" Low--Pressure Sensitivity text is not matching, expected string text is {expected_pressure_sensitivity_low_text}, but got {actual_pressure_sensitivity_low_text}. ")
        # High--Pressure Sensitivity
        expected_pressure_sensitivity_high_text = lang_settings["penSensitivity"]["penSensitivityLimit"]["high"]
        actual_pressure_sensitivity_high_text = self.fc.fd["pen_control"].get_high_pressure_sensitivity_text()
        soft_assertion.assert_equal(actual_pressure_sensitivity_high_text, expected_pressure_sensitivity_high_text, f"High--Pressure Sensitivity text is not matching, expected string text is {expected_pressure_sensitivity_high_text}, but got {actual_pressure_sensitivity_high_text}. ")
        # Low--Tilt Sensitivity
        expected_tilt_sensitivity_low_text = lang_settings["penSensitivity"]["penSensitivityLimit"]["low"]
        actual_tilt_sensitivity_low_text = self.fc.fd["pen_control"].get_low_tilt_text()
        soft_assertion.assert_equal(actual_tilt_sensitivity_low_text, expected_tilt_sensitivity_low_text, f"Low--Tilt Sensitivity text is not matching, expected string text is {expected_tilt_sensitivity_low_text}, but got {actual_tilt_sensitivity_low_text}. ")
        # High--Tilt Sensitivity
        expected_tilt_sensitivity_high_text = lang_settings["penSensitivity"]["penSensitivityLimit"]["high"]
        actual_tilt_sensitivity_high_text = self.fc.fd["pen_control"].get_high_tilt_text()
        soft_assertion.assert_equal(actual_tilt_sensitivity_high_text, expected_tilt_sensitivity_high_text, f" High--Tilt Sensitivity text is not matching, expected string text is {expected_tilt_sensitivity_high_text}, but got {actual_tilt_sensitivity_high_text}. ")
        # Restore Default Settings
        expected_restore_default_settings_text = lang_settings["resetToDefaultButton"]["title"]
        actual_restore_default_settings_text = self.fc.fd["pen_control"].get_restore_btn_text()
        soft_assertion.assert_equal(actual_restore_default_settings_text, expected_restore_default_settings_text, f"Restore Default Settings text is not matching, expected string text is {expected_restore_default_settings_text}, but got {actual_restore_default_settings_text}. ")
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
        soft_assertion.raise_assertion_errors()

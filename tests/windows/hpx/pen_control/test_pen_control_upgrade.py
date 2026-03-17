import os
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from SAF.misc.ssh_utils import SSH

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Pen_Control_Upgrade(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.sf = SystemFlow(cls.driver)
        cls.fc = FlowContainer(cls.driver)
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        os.environ['device']=cls.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        time.sleep(10)
        cls.fc.fd["home"].click_to_install_signed_build()
        time.sleep(60)
        cls.fc.launch_myHP()
        time.sleep(5)
          
    def test_01_upgrade_from_ms_store_C33140292(self):
        self.fc.ota_app_after_update()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        if os.environ.get('device').lower() == 'willie':
            soft_assertion.assert_true(self.fc.fd["pen_control"].verify_default_pen_name(), "Pen control title is not visible")
            soft_assertion.assert_true(self.fc.fd["pen_control"].verify_battery_status(), "Battery status is not visible")
            soft_assertion.assert_true(self.fc.fd["pen_control"].verify_proximity_icon(), "Proximity icon is not visible")
            #Restore defaults
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_restore_btn_text() == "Restore defaults","Restore defaults button text is not matching")
            #Right-click
            time.sleep(2)
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_click_consumer_btn_pen() == "Right-click","Right-click button text is not matching")
            #Erase
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_btn_consumer() == "Erase" , "Erase button text is not matching")
            #click Right-click btn on pen
            self.fc.fd["pen_control"].click_right_click_btn_consumer()
            #Upper barrel button
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_btn_right_click() == "Upper barrel button" ,"upper barrel button text is not matching")
            #Erase
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_text() == "Erase" ,"Erase text is not matching")
            #Right-click
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_click_pen_consumer() == "Right-click" , "Right-click text is not matching")
            #Disable pen buttons
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_disable_pen_buttons_consumer() == "Disable pen buttons" , "Disable pen buttons text is not matching")
            #Apps
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps() == "Apps" , "Apps text is not matching")
            #----------Apps elements------------
            #Take screenshot
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_take_screenshot_consumer() == "Take screenshot" , "Take screenshot text is not matching")
            #Switch between apps
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_switch_between_apps_consumer() == "Switch between apps" , "Switch between apps text is not matching")
            #Launch task manager
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_launch_task_manager_consumer() == "Launch task manager" , "Launch task manager text is not matching")
            #New browser tab
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_new_browser_tab_consumer() == "New browser tab" , "New browser tab text is not matching")
            #Show the desktop
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_show_the_desktop_consumer() == "Show the desktop" , "Show the desktop text is not matching")
            #click on Apps dropdown arrow
            self.fc.fd["pen_control"].click_apps_dropdown()
            #click pen drop down
            self.fc.fd["pen_control"].click_pen_dd()
            #Media control
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control() == "Media control" , "Media control text is not matching")
            #-------Media control elements------------
            #Play/Pause
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_play_pause_consumer() == "Play/Pause" , "Play/Pause text is not matching")
            #Volume up
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_up() == "Volume up" , "Volume up text is not matching")
            #Volume down
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_down() == "Volume down" , "Volume down text is not matching")
            #Mute/Unmute
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_mute_unmute_consumer() == "Mute/Unmute" , "Mute/Unmute text is not matching")
            #click on Media control dropdown arrow
            self.fc.fd["pen_control"].click_media_control_dropdown()
            #Productivity
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity() == "Productivity" , "Productivity text is not matching")
            #----------------Productivity elements----------------
            #Undo
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_undo_consumer() == "Undo" , "Undo text is not matching")
            #Shift key
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_shift_key_consumer() == "Shift key" , "Shift key text is not matching")
            #Control key
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_control_key_consumer() == "Control key" , "Control key text is not matching")
            #Alt key
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_alt_key_consumer() == "Alt key" , "Alt key text is not matching")
            #Windows key
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_windows_key_consumer() == "Windows key" , "Windows key text is not matching")
            #More link text
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_more_link_on_productivity() == "More" , "More link text is not matching")
            #click more link on Productivity
            self.fc.fd["pen_control"].click_more_link_on_productivity()
            #Tab key
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tab_key_consumer() == "Tab key" , "Tab key text is not matching")
            #Right arrow key
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_arrow_key_consumer() == "Right arrow key" , "Right arrow key text is not matching")
            #Left arrow key
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_left_arrow_key_consumer() == "Left arrow key" , "Left arrow key text is not matching")
            #Previous page
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_previous_page_consumer() == "Previous page" , "Previous page text is not matching")
            #Next page
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_next_page_consumer() == "Next page" , "Next page text is not matching")
            #Scroll 
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_scroll_consumer() == "Scroll" , "Scroll text is not matching" )
            #pen menu text
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title() == "Pen" , "Pen menu text is not matching")
            #click on Erase button on pen
            self.fc.fd["pen_control"].click_erase_btn_consumer()
            time.sleep(2)
            #Lower barrel button.
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_btn() == "Lower barrel button" , "Lower barrel button text is not matching")
        
        if os.environ.get('device').lower() == 'ultron' or os.environ.get('device').lower() == 'baymax':
            #pen control texts on image s
            #Single press
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_single_press_text() == "Single press" , "Single press text is not matching")
            #MS whiteboard
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_ms_whiteboard_commercial() == "MS Whiteboard" , "MS whiteboard text is not matching")
            #Double press
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_double_press_text() == "Double press" , "Double press text is not matching")
            #Screen snipping
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_screen_snipping_commercial() == "Screen snipping" , "Screen snipping text is not matching")
            #Long press
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_long_press_text() == "Long press" , "Long press text is not matching")
            #Sticky notes
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_sticky_notes_commercial() == "Sticky notes" , "Sticky notes text is not matching")
            #Restore defaults
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_restore_btn_text() == "Restore defaults" , "Restore defaults text is not matching")
            #Universal Select
            time.sleep(2)
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_universal_select_commercial() == "Universal Select" , "Universal Select text is not matching")
            #Erase
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_btn_consumer() == "Erase" , "Erase text is not matching")
            #Pen sensitivity
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_commercial() == "Pen sensitivity" , "Pen sensitivity text is not matching")
            #click on Pen sensitivity
            self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
            #Pen sensitivity window elements
            #Pen sensitivity title
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial() == "Pen sensitivity" , "Pen sensitivity title text is not matching")
            #Pressure
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pressure_title_text() == "Pressure" , "Pressure text is not matching")
            #Tilt
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_commercial() == "Tilt" , "Tilt text is not matching")
            #click on Erase
            self.fc.fd["pen_control"].click_erase_btn_commercial()
            time.sleep(2)
            #Pen section elements
            #Lower barrel button
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_btn() == "Lower barrel button" , "Lower barrel button text is not matching")
            #Hover-click
            soft_assertion
            #mouse hover tool tip on hover click
            self.fc.fd["pen_control"].click_lower_barrel_tooltip()
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_tool_tip() == "Hover-click" , "Hover-click text is not matching")
        
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
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_more_link_on_productivity() == "More" , "More text is not matching")
        
            #Productivity
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity() == "Productivity" , "Productivity text is not matching")
            #----------------Productivity remaining elements----------------
            #Universal Select
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_universal_select_text_commercial() == "Universal Select" , "Universal Select text is not matching")

            #Copy
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_copy_commercial() == "Copy" , "Copy text is not matching")
            #Paste
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_paste_commercial() == "Paste" , "Paste text is not matching")
            #Undo
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_undo_commercial() == "Undo" , "Undo text is not matching")
            #Redo
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_redo_commercial() == "Redo" , "Redo text is not matching")
        
            self.fc.fd["pen_control"].click_more_link_on_productivity()
            time.sleep(2)
            #Page up
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_page_up_commercial() == "Page up" , "Page up text is not matching")
            #Page down
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_page_down_commercial() == "Page down" , "Page down text is not matching")
            #Go back
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_go_back_commercial() == "Go back" , "Go back text is not matching")
            #Go forward
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_go_forward_commercial() == "Go forward" , "Go forward text is not matching")
            #click on productivity drop down
            self.fc.fd["pen_control"].click_productivity_dd()
        
            #click on pen dd
            self.fc.fd["pen_control"].click_pen_dd()
            #------------------Pen section elements------------------
            #Pen title
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title() == "Pen" , "Pen title text is not matching")
            #Erase
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_text_commercial() == "Erase" , "Erase text is not matching")
            #Right click
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_click_pen_commercial() == "Right click" , "Right click text is not matching")
            #Touch On/Off
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_touch_on_off_commercial() == "Touch On/Off" , "Touch On/Off text is not matching")
            #Left click
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_left_click_commercial() == "Left click" , "Left click text is not matching")
            #Middle click
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_middle_click_commercial() == "Middle click" , "Middle click text is not matching")
            #click on more link of Pen
            self.fc.fd["pen_control"].click_more_link_on_pen()
            #Fourth click
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_fourth_click_commercial() == "Fourth click" , "Fourth click text is not matching")
            #Fifth click
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_fifth_click_commercial() == "Fifth click" , "Fifth click text is not matching")
            #Pen menu
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_menu_commercial() == "Pen menu" , "Pen menu text is not matching")
            #Disabled
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_disabled_commercial() == "Disabled" , "Disabled text is not matching")
            #click on Pen drop down
            self.fc.fd["pen_control"].click_pen_dd()
            #click on Apps dd#click on Apps drop down
            self.fc.fd["pen_control"].click_apps_dropdown()
            #-------------Apps section elements----------------
            #Apps title
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps() == "Apps" , "Apps title text is not matching")
            #MS whiteboard
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_ms_whiteboard_commercial() == "MS Whiteboard" , "MS whiteboard text is not matching")
            #Screen snipping
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_screen_snipping_commercial() == "Screen snipping" , "Screen snipping text is not matching")
            #Switch application
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_switch_application_commercial() == "Switch application" , "Switch application text is not matching")
            #Web browser
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_web_browser_commercial() == "Web browser" , "Web browser text is not matching")
            #E-mail
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_e_mail_commercial() == "E-mail" , "E-mail text is not matching")
            #click on more of apps
            self.fc.fd["pen_control"].click_more_link_on_apps()
            time.sleep(2)
            #Windows search
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_windows_search_commercial() == "Windows search" , "Windows search text is not matching")
            #click on Apps drop down
            self.fc.fd["pen_control"].click_apps_dropdown()
            #click on media control dd
            self.fc.fd["pen_control"].click_media_control_dropdown()
            #------------------Media control section elements------------------
            #Media control title
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control() == "Media control" , "Media control title text is not matching")
            #Play/pause
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_play_pause_consumer() == "Play/Pause" , "Play/Pause text is not matching")
            #Next track
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_next_track_commercial() == "Next track" , "Next track text is not matching")
            #Previous track
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_previous_track_commercial() == "Previous track" , "Previous track text is not matching")
            #Volume up
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_up_commercial() == "Volume up" , "Volume up text is not matching")
            #volume down
            soft_assertion
            #Click MOre link of Media control
            self.fc.fd["pen_control"].click_more_link_on_media()
            #Mute audio
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_mute_audio_commercial() == "Mute audio" , "Mute audio text is not matching")
            #click on media control drop down
            self.fc.fd["pen_control"].click_media_control_dropdown()
        
            #click on Universal select button on pen
            self.fc.fd["pen_control"].click_universal_select_commercial()
            time.sleep(2)
            #Upper barrel button
            soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_btn_right_click() == "Upper barrel button" , "Upper barrel button text is not matching")
        
        self.fc.exit_hp_app_and_msstore()

import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
from SAF.misc.ssh_utils import SSH
import time, os
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Context_Aware_Accessibility(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        os.environ['device']=cls.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        cls.fc.launch_myHP()

    # This test case should run only on bopeep and willie
    def test_01_color_filter_toggle_C36767332(self):
        self.fc.close_windows_settings_panel()
        self.fc.open_color_filter_setting()
        self.fc.fd["display_control"].turn_toggle_color_filter_on()
        self.fc.close_windows_settings_panel()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        #all app btn
        soft_assertion.assert_true(self.fc.fd["display_control"].verify_default_global_app()), "Default global app is not displayed"
        #brightness and contrast text and slider
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_brightness_contrast_label() == "Brightness & Contrast","Brightness & Contrast label is not present or visible")
        soft_assertion.assert_true(self.fc.fd["display_control"].verify_brightness_slider_is_present(),"Brightness slider is not present or visible")
        soft_assertion.assert_true(self.fc.fd["display_control"].verify_contrast_slider_is_present(),"Contrast slider is not present or visible")
        soft_assertion.assert_true(self.fc.fd["display_control"].verify_default_global_app()),"Default global app is not displayed"
        soft_assertion.assert_contains("Add Application",self.fc.fd["display_control"].verify_add_application_text(),"Add Application text is not visible")
        #modes display as per bopeep and willie diff
        if os.environ.get('device').lower() == 'bopeep':
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_natural_mode_title() == "Neutral","Neutral mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_game_mode_title() == "Gaming","Gaming mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_reading_mode_title() == "Reading","Reading mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_night_mode_title() == "Night","Night mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_movie_mode_title() == "Movie","Movie mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_enhanceplus_mode_title() == "HP Enhance+","HP Enhance + mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_native_text() == "Native","Native mode title is not present or visible")
            self.fc.fd["display_control"].click_advaced_setting()
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_use_hdmi_input() == "Use HDMI input", "Use HDMI input text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_switch_text() == "Switch", "Switch text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_hpmi_input_description() == "Press Ctrl + Shift + S + D to switch back to the PC desktop text is not matched","Press Ctrl + Shift + S + D to switch back to the PC desktop text is not matched")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_color_adjestments(),"Color Adjustments", "Color Adjustments text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_blue_light_text() == "Low blue light" , "Low blue light text is not matching")
            toggle_state=self.fc.fd["display_control"].get_toggle_of_low_blue_light()
            if (toggle_state == '0'):
                self.fc.fd["display_control"].click_low_blue_light_toggle_on()
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_r_text() == "R", "R text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_g_text() == "G", "G text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_b_text() == "B", "B text is not matching")
        if os.environ.get('device').lower() == 'willie':
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_standard_title() == "Standard","Standard is not present")
            soft_assertion.assert_true(self.fc.fd["display_control"].verify_default_mode(), "Default mode is not displayed")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_work_tile() == "Work","Work mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_light_tile() == "Low Light","Low Light Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_entertainment_tile() == "Entertainment","Entertainment Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_blue_light_tile() == "Low blue light","Low Blue Light Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_advanced_title() == "Advanced","Advanced is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_sRGB_web_tile() == "sRGB (Web)","sRGB Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_adobe_RGB_tile() == "Adobe RGB (Printing and Imaging)","Adobe RGB Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_display_p3__tile() == "Display P3 (Photo and Video)","Display P3 Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_native_tile() == "Native","Native Tile is not present")            
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_hdr_windows_settings_text() == "Windows display settings", "Windows display settings text is not displayed")
            self.fc.fd["display_control"].click_advaced_setting()
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_blue_light_text() == "Low blue light" , "Low blue light text is not matching")
            toggle_state=self.fc.fd["display_control"].get_toggle_of_low_blue_light()
            if (toggle_state == '0'):
                self.fc.fd["display_control"].click_low_blue_light_toggle_on()
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_turn_on_advanced_settings() == "Turn on", "Turn on text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_turn_off_advanced_settings() == "Turn off", "Turn off text is not matching")

        #restore btn
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_restore_default_button() == "Restore Defaults","Restore defaults button is not present or visible")
        #setting btn in both tv
        soft_assertion.assert_true(self.fc.fd["display_control"].verify_advaced_setting_visible(), "Advanced settings button is not visible")
        self.fc.close_myHP()
        self.fc.open_color_filter_setting()
        time.sleep(2)
        self.fc.fd["display_control"].turn_toggle_color_filter_off()
        self.fc.close_windows_settings_panel()
        self.fc.launch_myHP()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        if os.environ.get('device').lower() == 'bopeep':
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_natural_mode_title() == "Neutral","Neutral mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_game_mode_title() == "Gaming","Gaming mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_reading_mode_title() == "Reading","Reading mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_night_mode_title() == "Night","Night mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_movie_mode_title() == "Movie","Movie mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_enhanceplus_mode_title() == "HP Enhance+","HP Enhance + mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_native_text() == "Native","Native mode title is not present or visible")
            self.fc.fd["display_control"].click_advaced_setting()
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_use_hdmi_input() == "Use HDMI input", "Use HDMI input text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_switch_text() == "Switch", "Switch text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_hpmi_input_description() == "Press Ctrl + Shift + S + D to switch back to the PC desktop text is not matched","Press Ctrl + Shift + S + D to switch back to the PC desktop text is not matched")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_color_adjestments(),"Color Adjustments", "Color Adjustments text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_blue_light_text() == "Low blue light" , "Low blue light text is not matching")
            toggle_state=self.fc.fd["display_control"].get_toggle_of_low_blue_light()
            if (toggle_state == '0'):
                self.fc.fd["display_control"].click_low_blue_light_toggle_on()
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_r_text() == "R", "R text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_g_text() == "G", "G text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_b_text() == "B", "B text is not matching")
        if os.environ.get('device').lower() == 'willie':
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_standard_title() == "Standard","Standard is not present")
            soft_assertion.assert_true(self.fc.fd["display_control"].verify_default_mode(), "Default mode is not displayed")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_work_tile() == "Work","Work mode title is not present or visible")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_light_tile() == "Low Light","Low Light Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_entertainment_tile() == "Entertainment","Entertainment Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_blue_light_tile() == "Low blue light","Low Blue Light Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_advanced_title() == "Advanced","Advanced is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_sRGB_web_tile() == "sRGB (Web)","sRGB Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_adobe_RGB_tile() == "Adobe RGB (Printing and Imaging)","Adobe RGB Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_display_p3__tile() == "Display P3 (Photo and Video)","Display P3 Tile is not present")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_native_tile() == "Native","Native Tile is not present")            
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_hdr_windows_settings_text() == "Windows display settings", "Windows display settings text is not displayed")
            self.fc.fd["display_control"].click_advaced_setting()
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect")
            soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_blue_light_text() == "Low blue light" , "Low blue light text is not matching")
            toggle_state=self.fc.fd["display_control"].get_toggle_of_low_blue_light()
            if (toggle_state == '0'):
                self.fc.fd["display_control"].click_low_blue_light_toggle_on()
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_turn_on_advanced_settings() == "Turn on", "Turn on text is not matching")
            soft_assertion.assert_equal(self.fc.fd["display_control"].get_turn_off_advanced_settings() == "Turn off", "Turn off text is not matching")

        #restore btn
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_restore_default_button() == "Restore Defaults","Restore defaults button is not present or visible")
        #setting btn in both tv
        soft_assertion.assert_true(self.fc.fd["display_control"].verify_advaced_setting_visible(), "Advanced settings button is not visible")
        self.fc.close_myHP()
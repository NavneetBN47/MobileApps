from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import MobileApps.resources.const.windows.const as w_const
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import ma_misc
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Adaptive_Audio(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
            cls.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
            cls.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx/properties.json"),cls.remote_artifact_path+"properties.json") 
            cls.fc.launch_myHP()
            if bool(cls.fc.fd["dropbox"].verify_dropbox_header_show()):
                cls.fc.fd["dropbox"].click_skip_button() 
            time.sleep(5)
            cls.fc.close_myHP()
            cls.fc.launch_myHP()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    # suite will only run on bopeep as this function is only in bopeep jenkin device.
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_launch_hpx_to_adaptive_audio_page_check_its_default_ui_when_camera_is_on_C33821444(self):
        time.sleep(2)
        if bool(self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button() 
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_speaker_on_bopeep()
        music_radio_button_selected = self.fc.fd["audio"].get_music_default_state()
        assert music_radio_button_selected == "1", "Music is not selected by default -{}".format(music_radio_button_selected)
      
        self.fc.fd["audio"].click_preset_movie_button()
        self.fc.fd["audio"].click_audio_settings_btn()

        adaptive_audio_text =self.fc.fd["audio"].get_adaptive_audio_text()
        assert adaptive_audio_text == "Adaptive Audio", "Adaptive Audio text is not visible -{}".format(adaptive_audio_text)
        
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is not on"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_enabled==True,"Auto Radio button is not enabled"
        
        adaptive_audio_auto_text =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button_text()
        assert adaptive_audio_auto_text == "Auto", "Auto is not selected by default -{}".format(adaptive_audio_auto_text)

        self.fc.fd["audio"].click_adaptive_audio_auto_tooltip_text()
        adaptive_audio_auto_tooltip_text =self.fc.fd["audio"].get_adaptive_audio_auto_tooltip_text()
        assert "Enjoy immersive movies" in adaptive_audio_auto_tooltip_text,"Tooltip text is not visible -{}".format(adaptive_audio_auto_tooltip_text)

        adaptive_audio_far_from_display_text =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_text()
        assert adaptive_audio_far_from_display_text ==  "Far from display", "Auto is not selected by default -{}".format(adaptive_audio_far_from_display_text)

        adaptive_audio_near_to_display_text =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button_text()
        assert adaptive_audio_near_to_display_text ==  "Near to display", "Auto is not selected by default -{}".format(adaptive_audio_near_to_display_text)
        self.fc.fd["audio"].close_audio_settings()

        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        self.fc.close_myHP()


    @pytest.mark.function
    @pytest.mark.consumer
    def test_02_launch_hpx_to_adaptive_audio_page_and_verify_adaptive_audio_doesnot_change_ui_with_external_device_C34279031(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        if bool(self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button() 
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_speaker_tab()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(10)
        self.fc.fd["audio"].click_preset_movie_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["audio"].click_audio_settings_btn()
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is not on"
        time.sleep(2)
        self.fc.fd["audio"].close_audio_settings()
        self.fc.fd["audio"].click_headset_tab()
        assert self.fc.fd["audio"].verify_presets_text_show() is False, "Presets text is visible"
        self.fc.fd["audio"].click_audio_settings_btn()
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is not on"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_disabled==True,"Auto Radio button is not enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_disabled==True,"Far from display Radio button is not enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_disabled==True,"Near to display Radio button is not enabled"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.fd["audio"].click_speaker_tab()
        time.sleep(2)
        self.fc.fd["audio"].click_preset_voice()
        voice_radio_button_selected = self.fc.fd["audio"].is_voice_status_selected()
        assert voice_radio_button_selected == "1", "Voice  is not selected -{}".format(voice_radio_button_selected)
        self.fc.fd["audio"].click_headset_tab()
        self.fc.fd["audio"].click_audio_settings_btn()
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is disabled"
        if state=="1":
            self.fc.fd['audio'].click_adaptive_audio_toggle_button()
        else:
        # If the element is not clickable, assert that it is greyed out
          assert is_disabled==True,"Toggle is not clickable hence is greyed out"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_disabled==False,"Auto Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_disabled==False,"Far from display Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_disabled==False,"Near to display Radio button is not disabled"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.fd["audio"].click_speaker_tab()
        time.sleep(2)
        self.fc.fd["audio"].click_preset_music()
        music_radio_button_selected = self.fc.fd["audio"].get_music_default_state()
        assert music_radio_button_selected == "1", "Music is not selected by default -{}".format(music_radio_button_selected)
        self.fc.fd["audio"].click_headset_tab()
        self.fc.fd["audio"].click_audio_settings_btn()
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is disabled"
        if state=="1":
            self.fc.fd['audio'].click_adaptive_audio_toggle_button()
        else:
        # If the element is not clickable, assert that it is greyed out
          assert is_disabled==True,"Toggle is not clickable hence is greyed out"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_enabled==False,"Auto Radio button is enabled"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_enabled==False,"Far from display Radio button is enabled"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_enabled==False,"Near to display Radio button is enabled"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.fd["audio"].click_speaker_tab()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        self.fc.close_myHP()
        
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.function
    @pytest.mark.consumer
    def test_03_Turn_on_camera_verify_all_toggles_and_options_work_well_C34379905(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        if bool(self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button() 
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_speaker_tab()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(10)
        self.fc.fd["audio"].click_preset_movie_button()
        movie_radio_button_selected = self.fc.fd["audio"].is_movie_status_selected()
        assert movie_radio_button_selected == "1", "Movie  is not selected -{}".format(movie_radio_button_selected)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["audio"].click_audio_settings_btn()
        time.sleep(2)
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is not on"
        self.fc.fd["audio"].click_adaptive_audio_toggle_button()
        time.sleep(5)
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_off_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_off_state()))
        assert state=="0","Adaptive audio toggle is on"
        self.fc.fd["audio"].click_adaptive_audio_toggle_off_button()
        time.sleep(5)
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is not on"

        is_enabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_enabled==True,"Auto Radio button is enabled"
        is_selected =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button_status()
        assert is_selected=="1","Auto Radio button is not selected"

        is_selected =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_status()
        assert is_selected == "0","Far from display Radio button is selected"
        self.fc.fd["audio"].click_far_from_display_radio_button()
        is_selected =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_status()
        assert is_selected == "1","Far from display Radio button is not selected"
 
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_enabled==True,"Near to display Radio button is enabled"
        is_selected =self.fc.fd["audio"].get_near_to_display_radio_button_state()
        assert is_selected == "0","Near to display Radio button is selected"
        self.fc.fd["audio"].click_near_to_display_radio_button()
        time.sleep(2)
        is_selected =self.fc.fd["audio"].get_near_to_display_radio_button_state()
        assert is_selected == "1","Near to display Radio button is not selected"

        self.fc.fd["audio"].click_auto_radio_button()
        is_selected =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button_status()
        assert is_selected=="1","Auto Radio button is not selected"
        self.fc.fd["audio"].close_audio_settings()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        self.fc.close_myHP()


    @pytest.mark.function
    @pytest.mark.consumer
    def test_04_launch_hpx_to_adaptive_audio_page_verify_it_will_just_enable_when_we_select_movie_option_with_camera_turn_on_C34313562(self):
        self.fc.reset_myhp_app()
        if bool(self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(10)
        music_radio_button_selected = self.fc.fd["audio"].get_music_default_state()
        assert music_radio_button_selected == "1", "Music is not selected by default -{}".format(music_radio_button_selected)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(2)
        self.fc.fd["audio"].click_audio_settings_btn()
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_disabled==False,"Auto Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_disabled==False,"Far from display Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_disabled==False,"Near to display Radio button is enabled"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.fd["audio"].click_preset_voice()
        voice_radio_button_selected = self.fc.fd["audio"].is_voice_status_selected()
        assert voice_radio_button_selected == "1", "Voice  is not selected -{}".format(voice_radio_button_selected)
        self.fc.fd["audio"].click_audio_settings_btn()
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_disabled==False,"Auto Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_disabled==False,"Far from display Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_disabled==False,"Near to display Radio button is enabled"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.fd["audio"].click_preset_movie_button()
        movie_radio_button_selected = self.fc.fd["audio"].is_movie_status_selected()
        assert movie_radio_button_selected == "1", "Movie  is not selected -{}".format(movie_radio_button_selected)
        self.fc.fd["audio"].click_audio_settings_btn()
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is not on"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_enabled==True,"Auto Radio button is not enabled"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_enabled==True,"Far from display Radio button is not enabled"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_enabled==True,"Near to display Radio button is not enabled"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["audio"].close_windows_camera()
        time.sleep(3)
        self.fc.fd["devices"].minimize_app()
        self.fc.fd["audio"].close_windows_camera()


    @pytest.mark.function
    @pytest.mark.consumer
    def test_05_launch_hpx_to_adaptive_audio_page_verify_presets_default_option_is_music_on_ai_supported_machine_C34715235(self):
        self.fc.reset_myhp_app()
        if bool(self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(10)
        music_radio_button_selected = self.fc.fd["audio"].get_music_default_state()
        assert music_radio_button_selected == "1", "Music is not selected by default -{}".format(music_radio_button_selected)
        self.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.close_myHP()


    @pytest.mark.consumer
    @pytest.mark.function
    def test_06_restore_button_works_well_C37543566(self):
        self.fc.reset_myhp_app()
        if bool(self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(10)
        self.fc.fd["audio"].click_preset_movie_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=4)
        self.fc.fd["audio"].click_audio_settings_btn()
        if self.fc.fd['audio'].get_adaptive_audio_toggle_button_state() == "1":
            self.fc.fd['audio'].click_adaptive_audio_toggle_button()
        time.sleep(2)
        self.fc.fd["audio"].close_audio_settings()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(2)
        self.fc.fd["audio"].click_preset_movie_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["audio"].close_windows_camera()

        self.fc.fd["audio"].click_audio_settings_btn()
        assert self.fc.fd['audio'].get_adaptive_audio_toggle_button_state() == "1","Adaptive audio toggle is not on"

	#This test should run only on bopeep where we have the camera turned off already 
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_07_check_adaptive_ui_when_camera_off_C33821453(self):
        self.fc.disable_camera_service()
        time.sleep(5)        
        self.fc.restart_myHP()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        assert audio_control_text == "Audio control","Audio Control is not visible at PC Device - {}".format(audio_control_text)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_preset_movie_button()
        time.sleep(2)
        self.fc.fd["audio"].click_audio_settings_btn()
        adaptive_audio_text =self.fc.fd["audio"].get_adaptive_audio_text()
        assert adaptive_audio_text == "Adaptive Audio", "Adaptive Audio text is not visible -{}".format(adaptive_audio_text)      
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is not on"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_enabled==False,"Auto Radio button is enabled"
        is_selected =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button_status()
        assert is_selected=="0","Auto Radio button is not selected"
        is_selected =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_status()
        assert is_selected == "1","Far from display Radio button is not selected"
        adaptive_audio_far_from_display_text =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_text()
        assert adaptive_audio_far_from_display_text ==  "Far from display", "radio button text is not Far from display"
        adaptive_audio_near_to_display_text =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button_text()
        assert adaptive_audio_near_to_display_text ==  "Near to display", "radio button text is not Near to display"
        is_enabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_enabled==True,"Near to display Radio button is enabled"
        self.fc.close_myHP()

    # @pytest.mark.function
    # @pytest.mark.consumer
    # def test_08_check_customize_settings_when_camera_off_C33821595(self):
    #     self.fc.disable_camera_service()
    #     time.sleep(5)
       
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
    #         self.fc.fd["devices"].maximize_app()
    #     self.fc.fd["navigation_panel"].navigate_to_welcome()
    #     audio_control_text = self.fc.fd["devices"].verify_audio_control()
    #     assert audio_control_text == "Audio control","Audio Control is not visible at PC Device - {}".format(audio_control_text)
    #     self.fc.fd["navigation_panel"].navigate_to_pc_audio()
    #     music_radio_button_selected = self.fc.fd["audio"].get_music_default_state()
    #     assert music_radio_button_selected == "1", "Music is not selected by default -{}".format(music_radio_button_selected)
 
    #     self.fc.fd["audio"].click_preset_movie_button()
    #     time.sleep(2)
    #     self.fc.fd["audio"].click_audio_settings_btn()
    #     adaptive_audio_text =self.fc.fd["audio"].get_adaptive_audio_text()
    #     assert adaptive_audio_text == "Adaptive Audio", "Adaptive Audio text is not visible -{}".format(adaptive_audio_text)
       
    #     state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
    #     logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
    #     assert state=="1","Adaptive audio toggle is not on"
    #     is_enabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
    #     assert is_enabled==False,"Auto Radio button is enabled"
    #     is_selected =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button_status()
    #     assert is_selected=="0","Auto Radio button is not selected"
    #     adaptive_audio_auto_text =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button_text()
    #     assert adaptive_audio_auto_text == "Auto", "Auto option is missing"
 
    #     is_selected =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_status()
    #     assert is_selected == "1","Far from display Radio button is not selected"
    #     adaptive_audio_far_from_display_text =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_text()
    #     assert adaptive_audio_far_from_display_text ==  "Far from display", "Auto is not selected by default -{}".format(adaptive_audio_far_from_display_text)
 
    #     adaptive_audio_near_to_display_text =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button_text()
    #     assert adaptive_audio_near_to_display_text ==  "Near to display", "Auto is not selected by default -{}".format(adaptive_audio_near_to_display_text)
    #     is_enabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
    #     assert is_enabled==True,"Near to display Radio button is enabled"
 
    #     self.fc.fd["audio"].click_near_to_display_radio_button()
    #     time.sleep(2)
    #     is_selected =self.fc.fd["audio"].get_near_to_display_radio_button_state()
    #     assert is_selected == "1","Near to display Radio button is not selected"
 
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
    #         self.fc.fd["devices"].maximize_app()
    #     self.fc.fd["navigation_panel"].navigate_to_welcome()
    #     audio_control_text = self.fc.fd["devices"].verify_audio_control()
    #     assert audio_control_text == "Audio control","Audio Control is not visible at PC Device - {}".format(audio_control_text)
    #     self.fc.fd["navigation_panel"].navigate_to_pc_audio()
 
    #     self.fc.fd["audio"].click_preset_movie_button()
    #     time.sleep(2)
    #     self.fc.fd["audio"].click_audio_settings_btn()
    #     adaptive_audio_text =self.fc.fd["audio"].get_adaptive_audio_text()
    #     assert adaptive_audio_text == "Adaptive Audio", "Adaptive Audio text is not visible -{}".format(adaptive_audio_text)
    #     is_selected =self.fc.fd["audio"].get_near_to_display_radio_button_state()
    #     assert is_selected == "1","Near to display Radio button is not selected"
 
    #     self.fc.close_myHP()
    #     self.fc.enable_camera_service()

    #this testcase only run on machine turn off camera(turn off camera shutter) on bopeep
    @pytest.mark.function
    @pytest.mark.consumer
    def test_9_turn_off_camera_verify_adaptive_audio_status_with_different_Presets_option_C34379907(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        music_radio_button_selected = self.fc.fd["audio"].is_music_status_selected()
        assert music_radio_button_selected == "1", " music not selected -{}".format(music_radio_button_selected)
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["audio"].click_audio_settings_btn()
        time.sleep(2)
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_off_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_off_state()))
        assert state=="0","Adaptive audio toggle is on"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_disabled==False,"Auto Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_disabled==False,"Far from display Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_disabled==False,"Near to display Radio button is not disabled"
        self.fc.fd["audio"].close_audio_settings()
        time.sleep(2)
        self.fc.fd["audio"].click_preset_voice()
        self.fc.fd["audio"].click_audio_settings_btn()
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_off_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_off_state()))
        assert state=="0","Adaptive audio toggle is on"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_disabled==False,"Auto Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_disabled==False,"Far from display Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_disabled==False,"Near to display Radio button is not disabled"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.fd["audio"].click_preset_movie()
        self.fc.fd["audio"].click_audio_settings_btn()
        state = self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()
        logging.info("Audio Toggle State {}".format(self.fc.fd['audio'].get_adaptive_audio_toggle_button_state()))
        assert state=="1","Adaptive audio toggle is off"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_auto_radio_button()
        assert is_disabled==False,"Auto Radio button is enabled"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button()
        assert is_disabled==True,"Far from display Radio button is enabled"
        is_selected =self.fc.fd["audio"].get_adaptive_audio_far_from_display_radio_button_status()
        assert is_selected == "1","Far from display Radio button is not selected"
        is_disabled =self.fc.fd["audio"].get_adaptive_audio_near_to_display_radio_button()
        assert is_disabled==True,"Near to display Radio button is disabled"
        self.fc.fd["audio"].close_audio_settings()
        time.sleep(3)
        self.fc.close_myHP()

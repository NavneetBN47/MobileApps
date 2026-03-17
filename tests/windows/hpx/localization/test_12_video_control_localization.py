import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')

#zh-HANS and zh_Hant does not get installed as zh-Hant-HK already runs once

@pytest.fixture(params=languages)
def language(request):
    return request.param

class Test_Suite_Video_Control_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        
    def test_01_video_control_module_first_page_tutorial_C34971877(self,language):
        soft_assertion = SoftAssert()
        self.fc.update_win_language(language)
        self.fc.launch_myHP()
        self.fc.close_myHP()
        self.fc.launch_myHP()  
        time.sleep(6)
        if bool (self.fc.fd["hp_registration"].verify_registration_page_is_display()):
            self.driver.swipe(direction="down", distance=3)
            if self.fc.fd["hp_registration"].verify_skip_button_show():
                self.fc.fd["hp_registration"].click_skip_button()
            else:
                logging.info("skip button not available")
        else:
            logging.info("registration page not displayed")
        if bool (self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button() 
        else:
            logging.info("Dropbox page not displayed")  
        langSettings = ma_misc.load_json_file("resources/test_data/hpx/videocontrollocalization.json")[language]["TS"]["context"]
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["video_control"].click_video_control()
        logging.info(f"Window size {self.fc.fd['video_control'].verify_video_control_window_maximize()}")
        if "Maximize" == self.fc.fd["video_control"].verify_video_control_window_maximize():
            self.fc.fd["video_control"].click_maximize_video_control_window()
        
        self.fc.fd["video_control"].mixer_help_button_to_navigate_back_to_tutorial_first_page()
        # #1st Tutorial page label
        actual_tutorial_first_page_lable_text=self.fc.fd["video_control"].get_enhance_video_control_text()
        logging.info(f"json text {langSettings[37]['message'][128]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][128]['translation'], actual_tutorial_first_page_lable_text,f"tutorial first page label text - Expected {langSettings[37]['message'][128]['translation']}, but got {actual_tutorial_first_page_lable_text}")
        
        #1st Tutorial page tip
        actual_tutorial_first_page_tip_text=self.fc.fd["video_control"].get_tutorial_first_page_tip_text()
        logging.info(f"json text {langSettings[37]['message'][129]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][129]['translation'] , actual_tutorial_first_page_tip_text,f"tutorial first page tip text - Expected {langSettings[37]['message'][129]['translation'] } but got {actual_tutorial_first_page_tip_text}")
        
        #1st Tutorial system startup label(Name attribute is not correct)
        actual_follow_system_startup_label_text=self.fc.fd["video_control"].get_start_hp_enhanced_camera_text()
        logging.info(f"json text {langSettings[37]['message'][130]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][130]['translation'] , actual_follow_system_startup_label_text,f"tutorial first page startup label text- Expected {langSettings[37]['message'][130]['translation']}, but got {actual_follow_system_startup_label_text}")
    
        #2nd Tutorial page label
        self.fc.fd["video_control"].click_next_arrow()
        actual_tutorial_second_page_lable_text=self.fc.fd["video_control"].get_lets_get_you_ready_text()
        logging.info(f"json text {langSettings[37]['message'][131]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][131]['translation'] , actual_tutorial_second_page_lable_text,f"tutorial second page label text - Expected {langSettings[37]['message'][131]['translation']} but got {actual_tutorial_second_page_lable_text}")
        #2nd Tutorial page tip
        actual_tutorial_second_page_tip_text=self.fc.fd["video_control"].get_tutorial_second_page_tip_text()
        logging.info(f"json text {langSettings[37]['message'][132]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][132]['translation'] , actual_tutorial_second_page_tip_text,f"tutorial second page tip text - Expected {langSettings[37]['message'][132]['translation']} but got {actual_tutorial_second_page_tip_text}")
        #Camera Input
        actual_camera_input_text=self.fc.fd["video_control"].get_camera_input_text()
        logging.info(f"json text {langSettings[37]['message'][133]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][133]['translation'] , actual_camera_input_text,f"Camera input text is not matching- Expected {langSettings[37]['message'][133]['translation']} but got {actual_camera_input_text}")
        #HP Enhanced Camera
        actual_hp_enhanced_camera_text=self.fc.fd["video_control"].get_hp_enhanced_camera_text()
        logging.info(f"json text {langSettings[37]['message'][126]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][126]['translation'] , actual_hp_enhanced_camera_text,f"HP Enhanced Camera text is not matching- Expected {langSettings[37]['message'][126]['translation']} but got {actual_hp_enhanced_camera_text}")
    
        #HP Wide Vision 5MP Camera- 
        # Text string is not available in json
        # actual_hp_wide_vision_camera_text=self.fc.fd["video_control"].get_hp_wide_vision_5mp_camera_text()
        # logging.info(f"json text {langSettings[37]['message'][134]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][134]['translation'] , actual_hp_wide_vision_camera_text,f"HP Wide vision 5 MP Camera text is not matching- Expected {langSettings[37]['message'][134]['translation']} but got {actual_hp_wide_vision_camera_text}")
       
        #Mixer
        self.fc.fd["video_control"].click_next_arrow()
        time.sleep(2)
        actual_mixer_text=self.fc.fd["video_control"].get_mixer_button_text()
        logging.info(f"json text {langSettings[24]['message'][2]['translation']}")
        soft_assertion.assert_equal(langSettings[24]['message'][2]['translation'] , actual_mixer_text,f"Mixer button text is not visible- Expected {langSettings[24]['message'][2]['translation']} but got {actual_mixer_text}")

        # # Mixer Layouts- json mismatch
        self.fc.fd["video_control"].click_mixer_button()
        # actual_mixer_layouts_text=self.fc.fd["video_control"].get_layouts_text()
        # logging.info(f"json text {langSettings[37]['message'][71]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][71]['translation'] , actual_mixer_layouts_text,f"Layout text is not visible- Expected {langSettings[37]['message'][71]['translation']} but got {actual_mixer_layouts_text}")

        self.fc.fd["video_control"].click_camera_settings_to_go_back_main_screen()
              
        #SideBar Share as Window
        actual_get_share_as_window_text=self.fc.fd["video_control"].get_share_as_window_text()
        logging.info(f"json text {langSettings[37]['message'][135]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][135]['translation'] , actual_get_share_as_window_text,f"Share as Window text is not visible- Expected {langSettings[37]['message'][135]['translation']} but got {actual_get_share_as_window_text}")

        # SideBar Save a PDF
        actual_get_save_a_pdf_text=self.fc.fd["video_control"].get_save_a_pdf_text()
        logging.info(f"json text {langSettings[23]['message'][2]['translation']}")
        soft_assertion.assert_equal(langSettings[23]['message'][2]['translation'] , actual_get_save_a_pdf_text,f"Save a PDF text is not visible- Expected {langSettings[23]['message'][2]['translation']} but got {actual_get_save_a_pdf_text}")
        self.fc.fd["video_control"].close_save_as_window()

        #Snap photo
        actual_get_snap_photo_text=self.fc.fd["video_control"].get_snap_phote_text()
        logging.info(f"json text {langSettings[23]['message'][3]['translation']}")
        soft_assertion.assert_equal(langSettings[23]['message'][3]['translation'] , actual_get_snap_photo_text,f"Snap photo text is not visible- Expected {langSettings[23]['message'][3]['translation']} but got {actual_get_snap_photo_text}")
        self.fc.fd["video_control"].close_save_as_window()

        #Start Recording
        time.sleep(5)
        actual_get_start_recording_text=self.fc.fd["video_control"].get_start_recording_text()
        logging.info(f"json text {langSettings[12]['message'][28]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][28]['translation'] , actual_get_start_recording_text,f"Start Recording text is not visible- Expected {langSettings[12]['message'][28]['translation']} but got {actual_get_start_recording_text}")
        
        #Cancel Recording
        self.fc.fd["video_control"].click_start_recording_text()
        actual_get_cancel_recording_text=self.fc.fd["video_control"].get_cancel_recording_text()
        logging.info(f"json text {langSettings[37]['message'][118]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][118]['translation'] , actual_get_cancel_recording_text,f"Cancel Recording text is not visible- Expected {langSettings[37]['message'][118]['translation']} but got {actual_get_cancel_recording_text}")

        #Cancel Recording ? popoup
        actual_get_cancel_recording_popup_text=self.fc.fd["video_control"].get_cancel_recording_pop_up_text()
        logging.info(f"json text {langSettings[37]['message'][119]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][119]['translation'] , actual_get_cancel_recording_popup_text,f"Cancel Recording? text is not visible- Expected {langSettings[37]['message'][119]['translation']} but got {actual_get_cancel_recording_popup_text}")

        #Cancel Recording pop_up tip text
        actual_get_cancel_recording_popup_tip_text=self.fc.fd["video_control"].get_cancel_recording_pop_up_tip_text()
        logging.info(f"json text {langSettings[37]['message'][120]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][120]['translation'] , actual_get_cancel_recording_popup_tip_text,f"Cancel Recording tip text is not visible- Expected {langSettings[37]['message'][120]['translation']} but got {actual_get_cancel_recording_popup_tip_text}")
        # assert langSettings[37]['message'][120]['translation'] in actual_get_cancel_recording_popup_tip_text,"Cancel Recording tip text is not visible- {}".format(actual_get_cancel_recording_popup_tip_text)

        #Go back text
        actual_get_go_back_text=self.fc.fd["video_control"].get_go_back_text()
        logging.info(f"json text {langSettings[37]['message'][121]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][121]['translation'] , actual_get_go_back_text,f"Go back text is not visible- Expected {langSettings[37]['message'][121]['translation']} but got {actual_get_go_back_text}")
        
        #Delete text
        actual_get_cancel_recording_popup_tip_text=self.fc.fd["video_control"].get_delete_from_pop_up_text()
        logging.info(f"json text {langSettings[37]['message'][53]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][53]['translation'] , actual_get_cancel_recording_popup_tip_text,f"Delete text is not visible- Expected {langSettings[37]['message'][53]['translation']} but got {actual_get_cancel_recording_popup_tip_text}")
        self.fc.fd["video_control"].click_delete_from_pop_up_text() 

        #THIS WHOLE BLOCK IS PASSING BUT STILL WILL FAIL AT LAST STRING DUE TO MISSING AUID FOR X 
        # #Start LiveStream
        # actual_get_start_livestream_text=self.fc.fd["video_control"].get_start_livestream_text()
        # logging.info(f"json text {langSettings[12]['message'][29]['translation']}")
        # soft_assertion.assert_equal(langSettings[12]['message'][29]['translation'] , actual_get_start_livestream_text,f"Start Livestream text is not visible- Expected {langSettings[12]['message'][29]['translation']} but got {actual_get_start_livestream_text}")

        # #Configure LiveStream
        # actual_get_configure_livestream_text=self.fc.fd["video_control"].get_configure_livestream_text()
        # logging.info(f"json text {langSettings[19]['message'][1]['translation']}")
        # soft_assertion.assert_equal(langSettings[19]['message'][1]['translation'] , actual_get_configure_livestream_text,f"Configure Livestream text is not visible- Expected {langSettings[19]['message'][1]['translation']} but got {actual_get_configure_livestream_text}")

        # #Connect a RTMP Server
        # actual_get_connect_a_rtmp_server_text=self.fc.fd["video_control"].get_connect_a_rtmp_server_text()
        # logging.info(f"json text {langSettings[19]['message'][2]['translation']}")
        # soft_assertion.assert_equal(langSettings[19]['message'][2]['translation'] , actual_get_connect_a_rtmp_server_text,f"Connect a RTMP Server text is not visible- Expected {langSettings[19]['message'][2]['translation']} but got {actual_get_connect_a_rtmp_server_text}")

        # #Stream URL
        # actual_get_stream_url_text=self.fc.fd["video_control"].get_stream_url_text()
        # logging.info(f"json text {langSettings[37]['message'][63]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][63]['translation'] , actual_get_stream_url_text,f"Stream URL text is not visible- Expected {langSettings[37]['message'][63]['translation']} but got {actual_get_stream_url_text}")

        # #Stream URL Tooltip
        # actual_get_stream_url_tooltip_text=self.fc.fd["video_control"].get_stream_url_tooltip_text()
        # logging.info(f"json text {langSettings[37]['message'][64]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][64]['translation'] , actual_get_stream_url_tooltip_text,f"Stream URL Tooltip text is not visible- Expected {langSettings[37]['message'][64]['translation']} but got {actual_get_stream_url_tooltip_text}")

        # #rtmp://
        # actual_get_rtmp_text=self.fc.fd["video_control"].get_rtmp_text()
        # logging.info(f"json text {langSettings[37]['message'][65]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][65]['translation'] , actual_get_rtmp_text,f"RTMP:// text is not visible- Expected {langSettings[37]['message'][65]['translation']} but got {actual_get_rtmp_text}")

        # #Stream Key
        # actual_get_stream_key_text=self.fc.fd["video_control"].get_stream_key_text()
        # logging.info(f"json text {langSettings[37]['message'][66]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][66]['translation'] , actual_get_stream_key_text,f"Stream key text is not visible- Expected {langSettings[37]['message'][66]['translation']} but got {actual_get_stream_key_text}")

        # #Paste Stream Key
        # actual_get_paste_stream_key_text=self.fc.fd["video_control"].get_paste_stream_key_text()
        # logging.info(f"json text {langSettings[37]['message'][67]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][67]['translation'] , actual_get_paste_stream_key_text,f"Paste Stream Key text is not visible- Expected {langSettings[37]['message'][67]['translation']} but got {actual_get_paste_stream_key_text}")

        # #Start Live Stream button 
        # actual_get_start_liveStream_button_text=self.fc.fd["video_control"].get_start_liveStream_button_text()
        # logging.info(f"json text {langSettings[19]['message'][7]['translation']}")
        # soft_assertion.assert_equal(langSettings[19]['message'][7]['translation'] , actual_get_start_liveStream_button_text,f"Start Live Stream text is not visible- Expected {langSettings[19]['message'][7]['translation']} but got {actual_get_start_liveStream_button_text}")
        # #Missing AUID for X button
        # self.fc.fd["video_control"].close_open_window()    
                    
        #Be Right Back
        actual_get_brb_text=self.fc.fd["video_control"].get_brb_text()
        logging.info(f"json text {langSettings[37]['message'][29]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][29]['translation'] , actual_get_brb_text,f"Be Right Back text is not visible- Expected {langSettings[37]['message'][29]['translation']} but got {actual_get_brb_text}")

        #End Be Right Back
        self.fc.fd["video_control"].click_brb_button()
        actual_get_end_brb_text=self.fc.fd["video_control"].get_end_brb_text()
        logging.info(f"json text {langSettings[37]['message'][38]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][38]['translation'] , actual_get_end_brb_text,f"End Be Right Back text is not visible- Expected {langSettings[37]['message'][38]['translation']} but got {actual_get_end_brb_text}")
        self.fc.fd["video_control"].click_end_brb_text()

        #Automatic Keystone
        actual_get_automatic_keystone_text=self.fc.fd["video_control"].get_automatic_keystone_text()
        logging.info(f"json text {langSettings[37]['message'][23]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][23]['translation'] , actual_get_automatic_keystone_text,f"Automatic Keystone text is not visible- Expected {langSettings[37]['message'][23]['translation']} but got {actual_get_automatic_keystone_text}")
        
        #End Automatic Keystone
        self.fc.fd["video_control"].click_automatic_keystone_button()
        actual_get_end_automatic_keystone_text=self.fc.fd["video_control"].get_end_automatic_keystone_text()
        logging.info(f"json text {langSettings[37]['message'][21]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][21]['translation'] , actual_get_end_automatic_keystone_text,f"End Automatic Keystone text is not visible- Expected {langSettings[37]['message'][21]['translation']} but got {actual_get_end_automatic_keystone_text}")
        self.fc.fd["video_control"].click_end_automatic_keystone_text() 
             
        #Manual Keystone
        actual_get_manual_keystone_text=self.fc.fd["video_control"].get_manual_keystone_text()
        logging.info(f"json text {langSettings[37]['message'][22]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][22]['translation'] , actual_get_manual_keystone_text,f"Manual Keystone text is not visible- Expected {langSettings[37]['message'][22]['translation']} but got {actual_get_manual_keystone_text}")

        #End Manual Keystone
        self.fc.fd["video_control"].click_manual_keystone_button()
        actual_get_end_manual_keystone_text=self.fc.fd["video_control"].get_end_manual_keystone_text()
        logging.info(f"json text {langSettings[37]['message'][20]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][20]['translation'] , actual_get_end_manual_keystone_text,f"End Manual Keystone text is not visible- Expected {langSettings[37]['message'][20]['translation']} but got {actual_get_end_manual_keystone_text}")
        
        #Accept Text
        actual_get_accept_text=self.fc.fd["video_control"].get_accept_text()
        logging.info(f"json text {langSettings[5]['message'][0]['translation']}")
        soft_assertion.assert_equal(langSettings[5]['message'][0]['translation'] , actual_get_accept_text,f"Accept text is not visible-Expected {langSettings[37]['message'][132]['translation']} but got {actual_get_accept_text}")

        #Cancel Text
        actual_get_cancel_text=self.fc.fd["video_control"].get_cancel_text()
        logging.info(f"json text {langSettings[5]['message'][2]['translation']}")
        soft_assertion.assert_equal(langSettings[5]['message'][2]['translation'] , actual_get_cancel_text,f"Cancel text is not visible- Expected {langSettings[37]['message'][132]['translation']} but got {actual_get_cancel_text}")
        self.fc.fd["video_control"].click_cancel_text()

        #Rotate
        actual_get_rotate_text=self.fc.fd["video_control"].get_rotate_text()
        logging.info(f"json text {langSettings[37]['message'][25]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][25]['translation'] , actual_get_rotate_text, f"Rotate text is not visible- Expected {langSettings[37]['message'][25]['translation']} but got {actual_get_rotate_text}")

        #Auto Frame
        actual_get_auto_frame_text=self.fc.fd["video_control"].get_auto_frame_text()
        logging.info(f"json text {langSettings[37]['message'][9]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][9]['translation'] , actual_get_auto_frame_text,f"Auto frame text is not visible- Expected {langSettings[37]['message'][9]['translation']} but got {actual_get_auto_frame_text}")

        #Auto Frame toggle 
        if self.fc.fd["video_control"].verify_auto_frame_toggle_status()=="0":
            logging.info("Auto frame Toggle State {}".format(self.fc.fd["video_control"].verify_auto_frame_toggle_status()))           
            self.fc.fd["video_control"].click_auto_frame_toggle_switch()
        else:
            self.fc.fd["video_control"].click_auto_frame_toggle_switch()
            self.fc.fd["video_control"].click_auto_frame_toggle_switch()
            logging.info("Auto frame Toggle State {}".format(self.fc.fd["video_control"].verify_auto_frame_toggle_status())) 
            self.fc.fd["video_control"].click_auto_frame_wide_frame()

        #Wide 
        self.fc.fd["video_control"].scroll_down_with_tab("wide_pic_frame_button")  
        actual_get_auto_frame_wide_text=self.fc.fd["video_control"].get_auto_frame_wide_frame_text()
        logging.info(f"json text {langSettings[37]['message'][11]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][11]['translation'] , actual_get_auto_frame_wide_text,f"Wide text is not visible- Expected {langSettings[37]['message'][11]['translation']} but got {actual_get_auto_frame_wide_text}")         

        #Portrait
        self.fc.fd["video_control"].click_auto_frame_portrait_frame()
        actual_get_auto_frame_portrait_frame_text=self.fc.fd["video_control"].get_auto_frame_portrait_frame_text()
        logging.info(f"json text {langSettings[37]['message'][12]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][12]['translation'] , actual_get_auto_frame_portrait_frame_text,f"Portrait text is not visible- Expected {langSettings[37]['message'][12]['translation']} but got {actual_get_auto_frame_portrait_frame_text}")

        #Tight Frame
        self.fc.fd["video_control"].click_auto_frame_tight_frame()
        actual_get_auto_frame_tight_frame_text=self.fc.fd["video_control"].get_auto_frame_tight_frame_text()
        logging.info(f"json text {langSettings[37]['message'][13]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][13]['translation'] , actual_get_auto_frame_tight_frame_text,f"Tight Frame text is not visible- Expected {langSettings[37]['message'][13]['translation']} but got {actual_get_auto_frame_tight_frame_text}")       

        #Gallery View
        actual_get_gallery_view_text=self.fc.fd["video_control"].get_gallery_view_text()
        logging.info(f"json text {langSettings[37]['message'][149]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][149]['translation'] , actual_get_gallery_view_text,f"Gallery View text is not visible- Expected {langSettings[37]['message'][149]['translation']} but got {actual_get_gallery_view_text}")        
    
        #Enhance
        self.fc.fd["video_control"].scroll_down_with_tab("enhance_text")
        time.sleep(2)
        if self.fc.fd["video_control"].verify_enhance_toggle_status()=="0":
            logging.info("Enhance Toggle State {}".format(self.fc.fd["video_control"].verify_enhance_toggle_status()))           
            self.fc.fd["video_control"].click_enhance_toggle_switch()
        else:
            self.fc.fd["video_control"].click_enhance_toggle_switch()
            self.fc.fd["video_control"].click_enhance_toggle_switch()
            logging.info("Enhance Toggle State {}".format(self.fc.fd["video_control"].verify_enhance_toggle_status())) 
            
        #Enhance    
        actual_get_enhance_text=self.fc.fd["video_control"].get_enhance_text()
        logging.info(f"json text {langSettings[37]['message'][16]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][16]['translation'] , actual_get_enhance_text,f"Enhance text is not visible- Expected {langSettings[37]['message'][16]['translation']} but got {actual_get_enhance_text}")

        #Backlight
        actual_get_backlight_adjustment_text=self.fc.fd["video_control"].get_backlight_adjustment_text()
        logging.info(f"json text {langSettings[37]['message'][36]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][36]['translation'] , actual_get_backlight_adjustment_text,f"Backlight text is not visible- Expected {langSettings[37]['message'][36]['translation']} but got {actual_get_backlight_adjustment_text}")

        #Low Light Adjustment
        actual_get_low_light_adjustment_text=self.fc.fd["video_control"].get_low_light_adjustment_text()
        logging.info(f"json text {langSettings[37]['message'][37]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][37]['translation'] , actual_get_low_light_adjustment_text,f"Low Light Adjustment text is not visible- Expected {langSettings[37]['message'][37]['translation']} but got {actual_get_low_light_adjustment_text}")

        #Natural Tone
        self.fc.fd["video_control"].scroll_down_with_tab("natural_tone_text")
        actual_get_natural_tone_text=self.fc.fd["video_control"].get_natural_tone_text()
        logging.info(f"json text {langSettings[37]['message'][54]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][54]['translation'] , actual_get_natural_tone_text,f"Natural Tone text is not visible- Expected {langSettings[37]['message'][54]['translation']} but got {actual_get_natural_tone_text}")

        #Natural Tone Tooltip
        actual_get_natural_tone_tooltip_text=self.fc.fd["video_control"].get_natural_tone_tooltip_text()
        logging.info(f"json text {langSettings[37]['message'][102]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][102]['translation'] , actual_get_natural_tone_tooltip_text,f"Natural Tone tooltip text is not visible- Expected {langSettings[37]['message'][102]['translation']} but got {actual_get_natural_tone_tooltip_text}")
               
        #Eye Contact(only on SH Sammy)
        # self.fc.fd["video_control"].scroll_down_with_tab("eye_contact_text")
        # actual_get_eye_contact_text=self.fc.fd["video_control"].get_eye_contact_text()
        # logging.info(f"json text {langSettings[37]['message'][144]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][144]['translation'] , actual_get_eye_contact_text,f"Eye contact text is not visible- Expected {langSettings[37]['message'][144]['translation']} but got {actual_get_eye_contact_text}")

        # #Eye Contact Tooltip(only on Sammy)
        # actual_get_eye_contact_tooltip_text=self.fc.fd["video_control"].get_eye_contact_tooltip_text()
        # logging.info(f"json text {langSettings[37]['message'][103]['translation']}")
        # soft_assertion.assert_equal(langSettings[37]['message'][103]['translation'] , actual_get_eye_contact_tooltip_text,f"Eye contact tooltip text is not visible- Expected {langSettings[37]['message'][103]['translation']} but got {actual_get_eye_contact_tooltip_text}")

        #Background
        actual_get_background_text=self.fc.fd["video_control"].get_background_text()
        logging.info(f"json text {langSettings[12]['message'][2]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][2]['translation'] , actual_get_background_text,f"Background text is not visible- Expected {langSettings[12]['message'][2]['translation']} but got {actual_get_background_text}")

        #Add new
        actual_get_add_new_text=self.fc.fd["video_control"].get_add_new_text()
        logging.info(f"json text {langSettings[37]['message'][55]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][55]['translation'] , actual_get_add_new_text,f"Add new text is not visible- Expected {langSettings[37]['message'][55]['translation']} but got {actual_get_add_new_text}")

        #Off
        actual_get_off_text=self.fc.fd["video_control"].get_off_text()
        logging.info(f"json text {langSettings[12]['message'][35]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][35]['translation'] , actual_get_off_text,f"Off text is not visible- Expected {langSettings[12]['message'][35]['translation']} but got {actual_get_off_text}")

        #Blur
        actual_get_blur_text=self.fc.fd["video_control"].get_blur_text()
        logging.info(f"json text {langSettings[12]['message'][32]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][32]['translation'] , actual_get_blur_text,f"Blur text is not visible- Expected {langSettings[12]['message'][32]['translation']} but got {actual_get_blur_text}")

        #Office 1
        actual_get_officeone_text=self.fc.fd["video_control"].get_officeone_text()
        logging.info(f"json text {langSettings[12]['message'][36]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][36]['translation'] , actual_get_officeone_text, f"Office 1 text is not visible- Expected {langSettings[12]['message'][36]['translation']} but got {actual_get_officeone_text}")

        #Office 2
        #self.fc.fd["video_control"].scroll_down_with_tab("office2_text")
        actual_get_officetwo_text=self.fc.fd["video_control"].get_officetwo_text()
        logging.info(f"json text {langSettings[12]['message'][36]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][36]['translation'] , actual_get_officetwo_text,f"Office 2 text is not visible- Expected {langSettings[12]['message'][36]['translation']} but got {actual_get_officetwo_text}")      

        #Appearance Filter
        # self.fc.fd["video_control"].scroll_down_with_tab("appearance_filter_text")
        actual_get_appearance_filter_text=self.fc.fd["video_control"].get_appearance_filter_text()
        logging.info(f"json text {langSettings[37]['message'][33]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][33]['translation'] , actual_get_appearance_filter_text,f"Appearance text is not visible- Expected {langSettings[37]['message'][33]['translation']} but got {actual_get_appearance_filter_text}")
  
        #Cafe
        actual_get_cafe_text=self.fc.fd["video_control"].get_cafe_text()
        logging.info(f"json text {langSettings[12]['message'][38]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][38]['translation'] , actual_get_cafe_text,f"Cafe text is not visible- Expected {langSettings[12]['message'][38]['translation']} but got {actual_get_cafe_text}")

        #Livingroom
        actual_get_living_room_text=self.fc.fd["video_control"].get_living_room_text()
        logging.info(f"json text {langSettings[12]['message'][39]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][39]['translation'] , actual_get_living_room_text,f"Living Room text is not visible- Expected {langSettings[12]['message'][39]['translation']} but got {actual_get_living_room_text}")

        #Outdoor
        #self.fc.fd["video_control"].scroll_down_with_tab("outdoor_text")
        actual_get_outdoor_text=self.fc.fd["video_control"].get_outdoor_text()
        logging.info(f"json text {langSettings[12]['message'][40]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][40]['translation'] , actual_get_outdoor_text,f"Outdoor text is not visible- Expected {langSettings[12]['message'][40]['translation']} but got {actual_get_outdoor_text}")

        #Cameras
        actual_get_cameras_text=self.fc.fd["video_control"].get_cameras_text()
        logging.info(f"json text {langSettings[6]['message'][0]['translation']}")
        soft_assertion.assert_equal(langSettings[6]['message'][0]['translation'] , actual_get_cameras_text,f"Outdoor text is not visible- Expected {langSettings[6]['message'][0]['translation']} but got {actual_get_cameras_text}")

        #Auto
        actual_get_default_auto_text=self.fc.fd["video_control"].get_default_auto_text()
        logging.info(f"json text {langSettings[37]['message'][107]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][107]['translation'] ,  actual_get_default_auto_text,f"Default Auto text is not visible- Expected {langSettings[37]['message'][107]['translation']} but got {actual_get_default_auto_text}")

        #2160p
        self.fc.fd["video_control"].click_default_auto_text()
        time.sleep(2)
        actual_auto_2160p_text=self.fc.fd["video_control"].get_auto_dropbox_2160p_text()
        logging.info(f"json text {langSettings[12]['message'][14]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][14]['translation'] , actual_auto_2160p_text,f"2160p text is not visible- Expected {langSettings[12]['message'][14]['translation']} but got {actual_auto_2160p_text}")

        #1440p
        actual_auto_1440p_text=self.fc.fd["video_control"].get_auto_dropbox_1440p_text()
        logging.info(f"json text {langSettings[12]['message'][15]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][15]['translation'] , actual_auto_1440p_text,f"1440p text is not visible- Expected {langSettings[12]['message'][15]['translation']} but got {actual_auto_1440p_text}")

        #1080p
        actual_auto_1080p_text=self.fc.fd["video_control"].get_auto_dropbox_1080p_text()
        logging.info(f"json text {langSettings[12]['message'][16]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][16]['translation'] , actual_auto_1080p_text,f"1080p text is not visible- Expected {langSettings[12]['message'][16]['translation']} but got {actual_auto_1080p_text}")

        #720p
        actual_auto_720p_text=self.fc.fd["video_control"].get_auto_dropbox_720p_text()
        logging.info(f"json text {langSettings[12]['message'][17]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][17]['translation'] , actual_auto_720p_text,f"720p text is not visible- Expected {langSettings[12]['message'][17]['translation']} but got {actual_auto_720p_text}")

        #360pSD
        actual_auto_360p_text=self.fc.fd["video_control"].get_auto_dropbox_360psd_text()
        logging.info(f"json text {langSettings[12]['message'][19]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][19]['translation'] , actual_auto_360p_text,f"360p text is not visible- Expected {langSettings[12]['message'][19]['translation']} but got {actual_auto_360p_text}")

        #Auto
        actual_auto_text=self.fc.fd["video_control"].get_auto_text()
        logging.info(f"json text {langSettings[12]['message'][8]['translation']}")
        soft_assertion.assert_equal(langSettings[12]['message'][8]['translation'] , actual_auto_text,f"Auto text is not visible- Expected {langSettings[12]['message'][8]['translation']} but got {actual_auto_text}")

        #Anti-flicker Off
        self.fc.fd["video_control"].click_default_auto_text()
        actual_get_anti_flicker_off_text=self.fc.fd["video_control"].get_anti_flicker_off_text()
        logging.info(f"json text {langSettings[37]['message'][138]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][138]['translation'] ,  actual_get_anti_flicker_off_text,f"Anti flicker Off text is not visible- Expected {langSettings[37]['message'][138]['translation']} but got {actual_get_anti_flicker_off_text}")

        #Off
        self.fc.fd["video_control"].click_anti_flicker_off()
        actual_get_anti_flicker_off_combobox_first_element_text=self.fc.fd["video_control"].get_anti_flicker_off_combobox_first_element_text()
        logging.info(f"json text {langSettings[37]['message'][142]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][142]['translation'] , actual_get_anti_flicker_off_combobox_first_element_text,f"Dropdown Off text is not visible- Expected {langSettings[37]['message'][142]['translation']} but got {actual_get_anti_flicker_off_combobox_first_element_text}")
   
        #50Hz
        actual_get_anti_flicker_off_combobox_second_element_text=self.fc.fd["video_control"].get_anti_flicker_off_combobox_second_element_text()
        logging.info(f"json text {langSettings[37]['message'][139]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][139]['translation'] , actual_get_anti_flicker_off_combobox_second_element_text,f"Dropdown 50HZ text is not visible- Expected {langSettings[37]['message'][139]['translation']} but got {actual_get_anti_flicker_off_combobox_second_element_text}") 
 
        #60Hz
        actual_get_anti_flicker_off_combobox_third_element_text=self.fc.fd["video_control"].get_anti_flicker_off_combobox_third_element_text()
        logging.info(f"json text {langSettings[37]['message'][140]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][140]['translation'] , actual_get_anti_flicker_off_combobox_third_element_text,f"Dropdown 60Hz text is not visible- Expected {langSettings[37]['message'][140]['translation']} but got {actual_get_anti_flicker_off_combobox_third_element_text}")

        #RestoreDefaultSettings 
        self.fc.fd["video_control"].scroll_down_with_tab("restore_default_settings_text")
        actual_restore_default_settings_text=self.fc.fd["video_control"].get_restore_default_settings_text()
        logging.info(f"json text {langSettings[37]['message'][39]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][39]['translation'] , actual_restore_default_settings_text,f"Restore Default Settings text is not visible- Expected {langSettings[37]['message'][39]['translation']} but got {actual_restore_default_settings_text}")

        #HP presence logo
        actual_get_hp_presence_logo_text=self.fc.fd["video_control"].get_hp_presence_logo_text()
        logging.info(f"json text {langSettings[37]['message'][105]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][105]['translation'] , actual_get_hp_presence_logo_text,f"Hp Presence text is not visible- Expected {langSettings[37]['message'][105]['translation']} but got {actual_get_hp_presence_logo_text}") 

        #Battery usage - Low, Medium or High
        actual_battery_usage_text=self.fc.fd["video_control"].get_low_battery_usage_text()
        if actual_battery_usage_text=="Low battery usage":
            logging.info(f"json text {langSettings[37]['message'][122]['translation']}")
            soft_assertion.assert_equal(langSettings[37]['message'][122]['translation'] , actual_battery_usage_text,f"Low Battery Usage text is not visible- Expected {langSettings[37]['message'][122]['translation']} but got {actual_battery_usage_text}") 
        elif actual_battery_usage_text=="Medium battery usage":
            logging.info(f"json text {langSettings[37]['message'][123]['translation']}")
            soft_assertion.assert_equal(langSettings[37]['message'][123]['translation'] , actual_battery_usage_text,f"Medium Battery Usage text is not visible- Expected {langSettings[37]['message'][123]['translation']} but got {actual_battery_usage_text}") 
        else:
            actual_battery_usage_text=="High battery usage"
            logging.info(f"json text {langSettings[37]['message'][124]['translation']}")
            soft_assertion.assert_equal(langSettings[37]['message'][124]['translation'] , actual_battery_usage_text,f"High Battery Usage text is not visible- Expected {langSettings[37]['message'][124]['translation']} but got {actual_battery_usage_text}") 

        #battery usage tooltip
        actual_get_low_battery_usage_tooltip_text=self.fc.fd["video_control"].get_battery_usage_tooltip_text()
        logging.info(f"json text {langSettings[37]['message'][125]['translation']}")
        soft_assertion.assert_equal(langSettings[37]['message'][125]['translation'] , actual_get_low_battery_usage_tooltip_text,f"Low Battery Usage tooltip text is not visible- Expected {langSettings[37]['message'][125]['translation']} but got {actual_get_low_battery_usage_tooltip_text}")

        #for last step Help text- missing json
        time.sleep(2)
        self.fc.fd["devices"].close_hp_video_app()
        self.fc.close_myHP()
        soft_assertion.raise_assertion_errors()
        # self.fc.close_myHP()
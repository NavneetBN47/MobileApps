import time
import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Gestures_UI(object):
    
    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_01_luanch_hpx_to_pcdevice_page_and_check_gesture_show_C43876455(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"

    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_02_naviagtion_to_gesture_module_and_check_default_ui_C43876456(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        # check gesture default ui
        # verify gesture card title
        assert self.fc.fd["gestures"].verify_gesture_card_title_show(), "Gesture card title not found"
        time.sleep(2)
        # verify Gesture Body Container show
        assert self.fc.fd["gestures"].verify_gesture_body_container_show(), "Gesture Body Container not found"
        time.sleep(2)
        # verify PauseResume_img show
        assert self.fc.fd["gestures"].verify_pause_resume_img_show(), "PauseResume_img not found"
        time.sleep(2)
        # # verify PauseResume_text show
        assert self.fc.fd["gestures"].get_pause_resume_text() == "Pause / Resume", "PauseResume_text not found"
        time.sleep(2)
        # verify PauseResumeTryOutButton show
        assert self.fc.fd["gestures"].verify_pause_resume_try_out_button_show(), "PauseResumeTryOutButton not found"
        time.sleep(2)
        # verify PauseResumeToggle show
        assert self.fc.fd["gestures"].verify_pause_resume_toggle_show(), "PauseResumeToggle not found"
        time.sleep(2)
        # verify PauseResumeToggle default toggle is 0
        assert self.fc.fd["gestures"].get_pause_resume_toggle_status() == "0", "PauseResumeToggle default toggle is not 0"
        time.sleep(2)
        # verify VolumeAdjust_img show
        assert self.fc.fd["gestures"].verify_volume_adjust_img_show(), "VolumeAdjust_img not found"
        time.sleep(2)
        # verify VolumeAdjust_text show
        assert self.fc.fd["gestures"].get_volume_adjust_text() == "Volume adjust", "VolumeAdjust_text not found"
        time.sleep(2)
        # verify VolumeAdjustTryOutButton show
        assert self.fc.fd["gestures"].verify_volume_adjust_try_out_button_show(), "VolumeAdjustTryOutButton not found"
        time.sleep(2)
        # verify VolumeAdjustToggle show
        assert self.fc.fd["gestures"].verify_volume_adjust_toggle_show(), "VolumeAdjustToggle not found"
        time.sleep(2)
        # verify VolumeAdjustToggle default toggle is 0
        assert self.fc.fd["gestures"].get_volume_adjust_toggle_status() == "0", "VolumeAdjustToggle default toggle is not 0"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        # verify PageScroll iamge show
        assert self.fc.fd["gestures"].verify_page_scroll_img_show(), "PageScroll_img not found"
        time.sleep(2)
        # verify PageScroll_text show
        assert self.fc.fd["gestures"].get_page_scroll_text() == "Page scroll", "PageScroll_text not found"
        time.sleep(2)
        # verify PageScrollTryOutButton show
        assert self.fc.fd["gestures"].verify_page_scroll_try_out_button_show(), "PageScrollTryOutButton not found"
        time.sleep(2)
        # verify PageScrollToggle show
        assert self.fc.fd["gestures"].verify_page_scroll_toggle_show(), "PageScrollToggle not found"
        time.sleep(2)
        # verify PageScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_page_scroll_toggle_status() == "0", "PageScrollToggle default toggle is not 0"
        time.sleep(2)
        # verify PhotoScroll_img show
        assert self.fc.fd["gestures"].verify_photo_scroll_img_show(), "PhotoScroll_img not found"
        time.sleep(2)
        # verify PhotoScroll_text show
        assert self.fc.fd["gestures"].get_photo_scroll_text() == "Photo scroll", "PhotoScroll_text not found"
        time.sleep(2)
        # verify PhotoScrollTryOutButton show
        assert self.fc.fd["gestures"].verify_photo_scroll_try_out_button_show(), "PhotoScrollTryOutButton not found"
        time.sleep(2)
        # verify PhotoScrollToggle show
        assert self.fc.fd["gestures"].verify_photo_scroll_toggle_show(), "PhotoScrollToggle not found"
        time.sleep(2)
        # verify PhotoScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_photo_scroll_toggle_status() == "0", "PhotoScrollToggle default toggle is not 0"
        time.sleep(2)
        # verify feedback message text show
        assert self.fc.fd["gestures"].verify_feedback_message_show(), "Feedback message not found"
        time.sleep(2)
        # verify feedback message tips icon show
        assert self.fc.fd["gestures"].verify_feedback_message_tips_icon_show(), "Feedback message tips icon not found"
        time.sleep(2)
        # # verify feedback message toggle show
        assert self.fc.fd["gestures"].verify_feedback_message_toggle_show(), "Feedback message toggle not found"
        time.sleep(2)
        # verify feedback message toggle default toggle is 1
        assert self.fc.fd["gestures"].get_feedback_message_toggle_status() == "1", "Feedback message toggle default toggle is not 1"
        time.sleep(2)
        # verify gesture restore default button show
        assert self.fc.fd["gestures"].verify_gesture_restore_default_button_show(), "Gesture restore default button not found"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_verify_pause_resume_try_out_ui_C43876467(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["gestures"].click_gesture_restore_default_button()
        time.sleep(2)
        self.fc.fd["gestures"].click_pause_resume_img()
        time.sleep(2)
        # verify PauseResumeTryOutButton show
        assert self.fc.fd["gestures"].verify_pause_resume_try_out_button_show(), "PauseResumeTryOutButton not found"
        time.sleep(2)
        # click on PauseResumeTryOutButton
        self.fc.fd["gestures"].click_pause_resume_try_out_button()
        time.sleep(3)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        time.sleep(3)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(2)
        # verify play Pause text show
        assert self.fc.fd["gestures"].verify_play_pause_text_show(), "Play Pause text not found"
        time.sleep(2)
        # verify gesture_modal_description show
        assert self.fc.fd["gestures"].verify_gesture_modal_description_show(), "Gesture modal description not found"
        time.sleep(2)
        # verify play/pause first cancel button show
        assert self.fc.fd["gestures"].verify_play_pause_first_cancel_button_show(), "Cancel button not found"
        time.sleep(2)
        # verify play/pause first start button show
        assert self.fc.fd["gestures"].verify_play_pause_first_start_button_show(), "Start button not found"
        time.sleep(2)
        # click play/pause first start button 
        self.fc.fd["gestures"].click_play_pause_first_start_button()
        time.sleep(2)
        # verify play/pause second cancel button show
        assert self.fc.fd["gestures"].verify_play_pause_second_cancel_button_show(), "Cancel button not found"
        time.sleep(2)
        # verify play/pause second done button show
        assert self.fc.fd["gestures"].verify_play_pause_second_done_button_show(), "Done button not found"
        time.sleep(2)
        # click play/pause second done button
        self.fc.fd["gestures"].click_play_pause_second_done_button()
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_verify_volume_adjust_try_out_ui_C52610657(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["gestures"].click_gesture_restore_default_button()
        time.sleep(2)
        self.fc.fd["gestures"].click_volume_adjust_img()
        time.sleep(2)
        # verify volume adjust try out button show
        assert self.fc.fd["gestures"].verify_volume_adjust_try_out_button_show(), "Volume adjust try out button not found"
        time.sleep(1)
        # click on volume adjust try out button
        self.fc.fd["gestures"].click_volume_adjust_try_out_button()
        time.sleep(3)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
           self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify volume adjust:up first cancel button show
        assert self.fc.fd["gestures"].verify_volume_adjust_up_first_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify volume adjust:up first start button show
        assert self.fc.fd["gestures"].verify_volume_adjust_up_first_start_button_show(), "Start button not found"
        time.sleep(1)
        # click volume adjust:up first start button
        self.fc.fd["gestures"].click_volume_adjust_up_first_start_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify volume adjust:up second cancel button show
        assert self.fc.fd["gestures"].verify_volume_adjust_up_second_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify volume adjust:up second next button show
        assert self.fc.fd["gestures"].verify_volume_adjust_up_second_next_button_show(), "Next button not found"
        time.sleep(1)
        # click volume adjust:up second next button
        self.fc.fd["gestures"].click_volume_adjust_up_second_next_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify volume adjust:down first cancel button show
        assert self.fc.fd["gestures"].verify_volume_adjust_down_first_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify volume adjust:down first start button show
        assert self.fc.fd["gestures"].verify_volume_adjust_down_first_start_button_show(), "Start button not found"
        time.sleep(1)
        # click volume adjust:down first start button
        self.fc.fd["gestures"].click_volume_adjust_down_first_start_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify volume adjust:down second cancel button show
        assert self.fc.fd["gestures"].verify_volume_adjust_down_second_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify volume adjust:down second done button show
        assert self.fc.fd["gestures"].verify_volume_adjust_down_second_done_button_show(), "Done button not found"
        time.sleep(1)
        # click volume adjust:down second done button
        self.fc.fd["gestures"].click_volume_adjust_down_second_done_button()
        time.sleep(1)


    @pytest.mark.ota
    @pytest.mark.function
    def test_05_verify_page_scroll_try_out_ui_C52610658(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(1)
        self.fc.fd["gestures"].click_gesture_restore_default_button()
        time.sleep(2)
        self.fc.fd["gestures"].click_page_scroll_img()
        time.sleep(2)
        # verify page scroll try out button show
        assert self.fc.fd["gestures"].verify_page_scroll_try_out_button_show(), "Page scroll try out button not found"
        time.sleep(1)
        # click on page scroll try out button
        self.fc.fd["gestures"].click_page_scroll_try_out_button()
        time.sleep(3)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        time.sleep(3)        
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # click image_overlay_wrapper
        self.fc.fd["gestures"].click_image_overlay_wrapper()
        time.sleep(2)
        # verify page scroll:up first cancel button show
        assert self.fc.fd["gestures"].verify_page_scroll_up_first_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify page scroll:up first start button show
        assert self.fc.fd["gestures"].verify_page_scroll_up_first_start_button_show(), "Start button not found"
        time.sleep(1)
        # click page scroll:up first start button
        self.fc.fd["gestures"].click_page_scroll_up_first_start_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify page scroll:up second cancel button show
        assert self.fc.fd["gestures"].verify_page_scroll_up_second_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify page scroll:up second next button show
        assert self.fc.fd["gestures"].verify_page_scroll_up_second_next_button_show(), "Next button not found"
        time.sleep(1)
        # click page scroll:up second next button
        self.fc.fd["gestures"].click_page_scroll_up_second_next_button() 
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify page scroll:down first cancel button show
        assert self.fc.fd["gestures"].verify_page_scroll_down_first_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify page scroll:down first start button show
        assert self.fc.fd["gestures"].verify_page_scroll_down_first_start_button_show(), "Start button not found"
        time.sleep(1)
        # click page scroll:down first start button
        self.fc.fd["gestures"].click_page_scroll_down_first_start_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify page scroll:down second cancel button show
        assert self.fc.fd["gestures"].verify_page_scroll_down_second_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify page scroll:down second done button show
        assert self.fc.fd["gestures"].verify_page_scroll_down_second_done_button_show(), "Done button not found"
        time.sleep(1)
        # click page scroll:down second done button
        self.fc.fd["gestures"].click_page_scroll_down_second_done_button()
        time.sleep(1)

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_verify_photo_scroll_try_out_ui_C52610677(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["gestures"].click_gesture_restore_default_button()
        time.sleep(2)
        self.fc.fd["gestures"].click_photo_scroll_img()
        time.sleep(2)
        # verify photo scroll try out button show
        assert self.fc.fd["gestures"].verify_photo_scroll_try_out_button_show(), "Photo scroll try out button not found"
        time.sleep(1)
        # click on photo scroll try out button
        self.fc.fd["gestures"].click_photo_scroll_try_out_button()
        time.sleep(3)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        time.sleep(3)        
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify photo scroll:previous first cancel button show
        assert self.fc.fd["gestures"].verify_photo_scroll_previous_first_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify photo scroll:previous first start button show
        assert self.fc.fd["gestures"].verify_photo_scroll_previous_first_start_button_show(), "Start button not found"
        time.sleep(1)
        # click photo scroll:previous first start button
        self.fc.fd["gestures"].click_photo_scroll_previous_first_start_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify photo scroll:previous second cancel button show
        assert self.fc.fd["gestures"].verify_photo_scroll_previous_second_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify photo scroll:previous second next button show
        assert self.fc.fd["gestures"].verify_photo_scroll_previous_second_next_button_show(), "Next button not found"
        time.sleep(1)
        # click photo scroll:previous second next button
        self.fc.fd["gestures"].click_photo_scroll_previous_second_next_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify photo scroll:next first cancel button show
        assert self.fc.fd["gestures"].verify_photo_scroll_next_first_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify photo scroll:next first start button show
        assert self.fc.fd["gestures"].verify_photo_scroll_next_first_start_button_show(), "Start button not found"
        time.sleep(1)
        # click photo scroll:next first start button
        self.fc.fd["gestures"].click_photo_scroll_next_first_start_button()
        time.sleep(1)
        # verify image_overlay_wrapper show
        assert self.fc.fd["gestures"].verify_image_overlay_wrapper_show(), "Image Overlay Wrapper not found"
        time.sleep(1)
        # verify photo scroll:next second cancel button show
        assert self.fc.fd["gestures"].verify_photo_scroll_next_second_cancel_button_show(), "Cancel button not found"
        time.sleep(1)
        # verify photo scroll:next second done button show
        assert self.fc.fd["gestures"].verify_photo_scroll_next_second_done_button_show(), "Done button not found"
        time.sleep(1)
        # click photo scroll:next second done button
        self.fc.fd["gestures"].click_photo_scroll_next_second_done_button()
        time.sleep(1)

    @pytest.mark.ota
    @pytest.mark.function
    def test_07_turn_on_and_off_all_toggle_in_gesture_verify_function_work_well_C43876458(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["gestures"].click_gesture_restore_default_button()
        time.sleep(2)

        # verify PauseResumeToggle show
        assert self.fc.fd["gestures"].verify_pause_resume_toggle_show(), "PauseResumeToggle not found"
        time.sleep(2)
        # print logging info before clicking PauseResumeToggle
        logging.info(f"Before click: PauseResumeToggle status is {self.fc.fd['gestures'].get_pause_resume_toggle_status()}")
        # verify PauseResumeToggle default toggle is 0
        assert self.fc.fd["gestures"].get_pause_resume_toggle_status() == "0", "PauseResumeToggle default toggle is not 0"
        time.sleep(2)
        # click PauseResumeToggle
        self.fc.fd["gestures"].click_pause_resume_toggle()
        time.sleep(2)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
            time.sleep(3) 
        # print logging info after clicking PauseResumeToggle
        logging.info(f"After click: PauseResumeToggle status is {self.fc.fd['gestures'].get_pause_resume_toggle_status()}")
        # verify PauseResumeToggle status is 1
        assert self.fc.fd["gestures"].get_pause_resume_toggle_status() == "1", "PauseResumeToggle status is not 1"
        time.sleep(2)


        # verify VolumeAdjustToggle show
        assert self.fc.fd["gestures"].verify_volume_adjust_toggle_show(), "VolumeAdjustToggle not found"
        time.sleep(2)
        # print logging info before clicking VolumeAdjustToggle
        logging.info(f"Before click: VolumeAdjustToggle status is {self.fc.fd['gestures'].get_volume_adjust_toggle_status()}")
        # verify VolumeAdjustToggle default toggle is 0
        assert self.fc.fd["gestures"].get_volume_adjust_toggle_status() == "0", "VolumeAdjustToggle default toggle is not 0"
        time.sleep(2)
        # click VolumeAdjustToggle
        self.fc.fd["gestures"].click_volume_adjust_toggle()
        time.sleep(2)
        # print logging info after clicking VolumeAdjustToggle
        logging.info(f"After click: VolumeAdjustToggle status is {self.fc.fd['gestures'].get_volume_adjust_toggle_status()}")
        # verify VolumeAdjustToggle status is 1
        assert self.fc.fd["gestures"].get_volume_adjust_toggle_status() == "1", "VolumeAdjustToggle status is not 1"
        time.sleep(2)

        # verify PageScrollToggle show
        assert self.fc.fd["gestures"].verify_page_scroll_toggle_show(), "PageScrollToggle not found"
        time.sleep(2)
        # print logging info before clicking PageScrollToggle
        logging.info(f"Before click: PageScrollToggle status is {self.fc.fd['gestures'].get_page_scroll_toggle_status()}")
        # verify PageScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_page_scroll_toggle_status() == "0", "PageScrollToggle default toggle is not 0"
        time.sleep(2)
        # click PageScrollToggle
        self.fc.fd["gestures"].click_page_scroll_toggle()
        time.sleep(2)
        # print logging info after clicking PageScrollToggle
        logging.info(f"After click: PageScrollToggle status is {self.fc.fd['gestures'].get_page_scroll_toggle_status()}")
        # verify PageScrollToggle status is 1
        assert self.fc.fd["gestures"].get_page_scroll_toggle_status() == "1", "PageScrollToggle status is not 1"
        time.sleep(2)

        # verify PhotoScrollToggle show
        assert self.fc.fd["gestures"].verify_photo_scroll_toggle_show(), "PhotoScrollToggle not found"
        time.sleep(2)
        # print logging info before clicking PhotoScrollToggle
        logging.info(f"Before click: PhotoScrollToggle status is {self.fc.fd['gestures'].get_photo_scroll_toggle_status()}")
        # verify PhotoScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_photo_scroll_toggle_status() == "0", "PhotoScrollToggle default toggle is not 0"
        time.sleep(2)
        # click PhotoScrollToggle
        self.fc.fd["gestures"].click_photo_scroll_toggle()
        time.sleep(2)
        # print logging info after clicking PhotoScrollToggle
        logging.info(f"After click: PhotoScrollToggle status is {self.fc.fd['gestures'].get_photo_scroll_toggle_status()}")
        # verify PhotoScrollToggle status is 1
        assert self.fc.fd["gestures"].get_photo_scroll_toggle_status() == "1", "PhotoScrollToggle status is not 1"
        time.sleep(2)

        # verify FeedbackMessageToggle show
        assert self.fc.fd["gestures"].verify_feedback_message_toggle_show(), "FeedbackMessageToggle not found"
        time.sleep(2)
        # print logging info before clicking FeedbackMessageToggle
        logging.info(f"Before click: FeedbackMessageToggle status is {self.fc.fd['gestures'].get_feedback_message_toggle_status()}")
        # verify FeedbackMessageToggle default toggle is 1
        assert self.fc.fd["gestures"].get_feedback_message_toggle_status() == "1", "FeedbackMessageToggle default toggle is not 1"
        time.sleep(2)
        # click FeedbackMessageToggle
        self.fc.fd["gestures"].click_feedback_message_toggle()
        time.sleep(2)
        # print logging info after clicking FeedbackMessageToggle
        logging.info(f"After click: FeedbackMessageToggle status is {self.fc.fd['gestures'].get_feedback_message_toggle_status()}")
        # verify FeedbackMessageToggle status is 0
        assert self.fc.fd["gestures"].get_feedback_message_toggle_status() == "0", "FeedbackMessageToggle status is not 0"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_08_verify_feedback_message_toggle_C43876466(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        # verify FeedbackMessage tips icon show
        assert self.fc.fd["gestures"].verify_feedback_message_tips_icon_show(), "Feedback message tips icon not found"
        time.sleep(2)
        # click FeedbackMessage tips icon
        self.fc.fd["gestures"].click_feedback_message_tips_icon()
        time.sleep(2)
        # get feedback message tips 
        assert self.fc.fd["gestures"].get_feedback_message_tips_text() == "Feedback messages only apply to Pause / Resume, Volume adjust and Photo scroll gesture statuses.", "Feedback message tips not found"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_09_click_restore_default_button_and_all_settings_can_be_restore_C43876460(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)        
        self.fc.fd["gestures"].click_pause_resume_img()
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["gestures"].verify_gesture_restore_default_button_show(), "Gesture restore default button not found"
        time.sleep(2)
        # click gesture restore default button
        self.fc.fd["gestures"].click_gesture_restore_default_button()
        time.sleep(2)

        # verify PauseResumeToggle show
        assert self.fc.fd["gestures"].verify_pause_resume_toggle_show(), "PauseResumeToggle not found"
        time.sleep(2)
        # verify PauseResumeToggle default toggle is 0
        assert self.fc.fd["gestures"].get_pause_resume_toggle_status() == "0", "PauseResumeToggle default toggle is not 0"
        time.sleep(2)
        # click PauseResumeToggle
        self.fc.fd["gestures"].click_pause_resume_toggle()
        time.sleep(2)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        time.sleep(3) 
        # verify PauseResumeToggle status is 1
        assert self.fc.fd["gestures"].get_pause_resume_toggle_status() == "1", "PauseResumeToggle status is not 1"
        time.sleep(2)
        
        # verify VolumeAdjustToggle show
        assert self.fc.fd["gestures"].verify_volume_adjust_toggle_show(), "VolumeAdjustToggle not found"
        time.sleep(2)
        # verify VolumeAdjustToggle default toggle is 0
        assert self.fc.fd["gestures"].get_volume_adjust_toggle_status() == "0", "VolumeAdjustToggle default toggle is not 0"
        time.sleep(2)
        # click VolumeAdjustToggle
        self.fc.fd["gestures"].click_volume_adjust_toggle()
        time.sleep(2)
        # verify VolumeAdjustToggle status is 1
        assert self.fc.fd["gestures"].get_volume_adjust_toggle_status() == "1", "VolumeAdjustToggle status is not 1"
        time.sleep(2)
        
        # verify PageScrollToggle show
        assert self.fc.fd["gestures"].verify_page_scroll_toggle_show(), "PageScrollToggle not found"
        time.sleep(2)
        # verify PageScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_page_scroll_toggle_status() == "0", "PageScrollToggle default toggle is not 0"
        time.sleep(2)
        # click PageScrollToggle
        self.fc.fd["gestures"].click_page_scroll_toggle()
        time.sleep(2)
        # verify PageScrollToggle status is 1
        assert self.fc.fd["gestures"].get_page_scroll_toggle_status() == "1", "PageScrollToggle status is not 1"
        time.sleep(2)
       
        # verify PhotoScrollToggle show
        assert self.fc.fd["gestures"].verify_photo_scroll_toggle_show(), "PhotoScrollToggle not found"
        time.sleep(2)
        # verify PhotoScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_photo_scroll_toggle_status() == "0", "PhotoScrollToggle default toggle is not 0"
        time.sleep(2)
        # click PhotoScrollToggle
        self.fc.fd["gestures"].click_photo_scroll_toggle()
        time.sleep(2)
        # verify PhotoScrollToggle status is 1
        assert self.fc.fd["gestures"].get_photo_scroll_toggle_status() == "1", "PhotoScrollToggle status is not 1"
        time.sleep(2)
        
        # verify FeedbackMessageToggle show
        assert self.fc.fd["gestures"].verify_feedback_message_toggle_show(), "FeedbackMessageToggle not found"
        time.sleep(2)
        # verify FeedbackMessageToggle default toggle is 1
        assert self.fc.fd["gestures"].get_feedback_message_toggle_status() == "1", "FeedbackMessageToggle default toggle is not 1"
        time.sleep(2)
        # click FeedbackMessageToggle
        self.fc.fd["gestures"].click_feedback_message_toggle()
        time.sleep(2)
        # verify FeedbackMessageToggle status is 0
        assert self.fc.fd["gestures"].get_feedback_message_toggle_status() == "0", "FeedbackMessageToggle status is not 0"
        time.sleep(2)
        
        # verify gesture restore default button show
        assert self.fc.fd["gestures"].verify_gesture_restore_default_button_show(), "Gesture restore default button not found"
        time.sleep(2)
        # click gesture restore default button
        self.fc.fd["gestures"].click_gesture_restore_default_button()
        time.sleep(3)
        
        # verify PauseResumeToggle default toggle is 0
        assert self.fc.fd["gestures"].get_pause_resume_toggle_status() == "0", "PauseResumeToggle default toggle is not 0"
        time.sleep(2)
        # verify VolumeAdjustToggle default toggle is 0
        assert self.fc.fd["gestures"].get_volume_adjust_toggle_status() == "0", "VolumeAdjustToggle default toggle is not 0"
        time.sleep(2)
        # verify PageScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_page_scroll_toggle_status() == "0", "PageScrollToggle default toggle is not 0"
        time.sleep(2)
        # verify PhotoScrollToggle default toggle is 0
        assert self.fc.fd["gestures"].get_photo_scroll_toggle_status() == "0", "PhotoScrollToggle default toggle is not 0"
        time.sleep(2)
        # verify FeedbackMessageToggle default toggle is 1
        assert self.fc.fd["gestures"].get_feedback_message_toggle_status() == "1", "FeedbackMessageToggle default toggle is not 1"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_10_navigate_to_each_button_use_tab_C51909730(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(2)
        # click on gesture card
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["gestures"].press_tab("pause_resume_toggle")
        time.sleep(2)
        assert self.fc.fd["gestures"].is_focus_on_element("pause_resume_toggle"), "PauseResumeToggle is not focused"
        time.sleep(2)
        self.fc.fd["gestures"].press_tab("volume_adjust_toggle")
        time.sleep(2)
        assert self.fc.fd["gestures"].is_focus_on_element("volume_adjust_toggle"), "VolumeAdjustToggle is not focused"
        time.sleep(2)
        self.fc.fd["gestures"].press_tab("page_scroll_toggle")
        time.sleep(2)
        assert self.fc.fd["gestures"].is_focus_on_element("page_scroll_toggle"), "PageScrollToggle is not focused"
        time.sleep(2)
        self.fc.fd["gestures"].press_tab("photo_scroll_toggle")
        time.sleep(2)
        assert self.fc.fd["gestures"].is_focus_on_element("photo_scroll_toggle"), "PhotoScrollToggle is not focused"
        time.sleep(2)
        self.fc.fd["gestures"].press_tab("feedback_message_toggle")
        time.sleep(2)
        assert self.fc.fd["gestures"].is_focus_on_element("feedback_message_toggle"), "FeedbackMessageToggle is not focused"

    

    @pytest.mark.ota
    @pytest.mark.function
    def test_11_press_alt_f4_from_keyboard_C51909739(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"

        self.fc.fd["gestures"].press_alt_f4_to_close_app()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show() is False,  "Wellbeing card is displayed after alt+f4" 
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_12_restart_machine_verify_gesture_function_C63995269(self, request):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["gestures"].click_pause_resume_img()
        time.sleep(2)
        assert self.fc.fd["gestures"].verify_gesture_restore_default_button_show(), "Gesture restore default button not found"


        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["gestures"].click_pause_resume_img()
        time.sleep(2)
        assert self.fc.fd["gestures"].verify_gesture_restore_default_button_show(), "Gesture restore default button not found"
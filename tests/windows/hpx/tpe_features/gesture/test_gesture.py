from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Gesture(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        time.sleep(5)

    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["testudo"])
    def test_01_gesture_show_on_home_and_device_page_C39033312(self):
        self.fc.restart_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["home"].verify_gesture_card_show_on_home_page()) is True, "Gesture card is not displayed on home page"

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert self.fc.fd["devices"].verify_gesture_show_on_device_page() is True, "Gesture is not displayed on device page"


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["testudo"])
    def test_02_check_gesture_ui_C39033442(self):
        self.fc.restart_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["home"].verify_gesture_card_show_on_home_page()) is True, "Gesture card is not displayed on home page"
 
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["gesture"].click_gesture_card()
        time.sleep(3)
 
        assert bool(self.fc.fd["gesture"].verify_gesture_panel_banner_show()) is True, "Gesture panel banner is not displayed"
        assert bool(self.fc.fd["gesture"].verify_gesture_panel_banner_description()) is True, "Gesture panel banner description is not displayed"
        assert bool(self.fc.fd["gesture"].verify_try_this_gesture_button_show()) is True, "Try this gesture button is not displayed"
        assert bool(self.fc.fd["gesture"].verify_pause_resume_card_title_show()) is True, "Pause resume card title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_pause_resume_toggle_show()) is True, "Pause resume toggle is not displayed"
        assert bool(self.fc.fd["gesture"].verify_pause_resume_card_description_show()) is True, "Pause resume card description is not displayed"
        assert self.fc.fd["gesture"].is_pause_resume_toggle_enabled() == "0", "Pause resume toggle is enabled"
        assert bool(self.fc.fd["gesture"].verify_volume_adjust_card_title_show()) is True, "Volume adjust card title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_volume_adjust_toggle_show()) is True, "Volume adjust toggle is not displayed"
        assert bool(self.fc.fd["gesture"].verify_volume_adjust_card_description_show()) is True, "Volume adjust card description is not displayed"
        assert self.fc.fd["gesture"].is_volume_adjust_toggle_enabled() == "0", "Volume adjust toggle is enabled"
        assert bool(self.fc.fd["gesture"].verify_page_scroll_card_title_show()) is True, "Page scroll card title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_page_scroll_toggle_show()) is True, "Page scroll toggle is displayed"
        assert bool(self.fc.fd["gesture"].verify_page_scroll_card_description_show()) is True, "Page scroll card description is not displayed"
        assert self.fc.fd["gesture"].is_page_scroll_toggle_enabled() == "0", "Page scroll toggle is on by default"
        assert bool(self.fc.fd["gesture"].verify_photo_scroll_card_title_show()) is True, "Photo scroll title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_photo_scroll_toggle_show()) is True, "Photo scroll toggle on gesture page is not displayed"
        assert bool(self.fc.fd["gesture"].verify_photo_scroll_card_description_show()) is True, "Photo scroll desciption is not displayed"
        assert self.fc.fd["gesture"].is_photo_scroll_toggle_enabled() == "0", "Photo scroll toggle is on by default"
        assert bool(self.fc.fd["gesture"].verify_restore_defaults_button_show()) is True, "Restore defaults button is not displayed"
        assert bool(self.fc.fd["gesture"].verify_settings_button_on_gesture_page_show()) is True, "Settings button on gesture page is not displayed"

        self.fc.fd["gesture"].click_pause_resume_card()
        time.sleep(2)
        self.fc.fd["gesture"].click_try_this_gesture_button()
        time.sleep(2)
        assert bool(self.fc.fd["gesture"].verify_play_pause_title_show()) is True, "Play / Pause title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_play_pause_description_show()) is True, "Play / Pause description is not displayed"
        assert bool(self.fc.fd["gesture"].verify_play_pause_close_button_show()) is True, "Play / Pause close button is not displayed"
        assert bool(self.fc.fd["gesture"].verify_play_pause_start_button_show()) is True, "Play / Pause start button is not displayed"
        self.fc.fd["gesture"].click_play_pause_close_button()
        time.sleep(2)
       
        self.fc.fd["gesture"].click_settings_button_on_gesture_page()
        time.sleep(2)
        assert bool(self.fc.fd["gesture"].verify_advanced_settings_page_close_button_show()) is True, "Advanced settings page close button is not displayed"
        assert bool(self.fc.fd["gesture"].verify_advanced_settings_page_title_show()) is True, "Advanced settings page is not displayed"
        assert bool(self.fc.fd["gesture"].verify_advanced_settings_page_second_title_show()) is True, "Advanced settings page second title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_feedback_message_toggle_show()) is True, "Feedback message toggle is not displayed"
        assert bool(self.fc.fd["gesture"].verify_feedback_message_description_show()) is True, "feedback message description is not displayed"
        assert self.fc.fd["gesture"].is_feedback_message_toggle_enabled() == "1", "Feedback message toggle is on by default"
        assert bool(self.fc.fd["gesture"].verify_picture_on_advanced_settings_page_show()) is True, "Picture on advanced settings page is not displayed"
        self.fc.fd["gesture"].click_close_button_on_advanced_settings_page()
        time.sleep(2)


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["testudo"])
    def test_03_check_gesture_toggle_button_work_well_C39033500(self):
        self.fc.restart_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["home"].verify_gesture_card_show_on_home_page()) is True, "Gesture card is not displayed on home page"
 
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["gesture"].click_gesture_card()
        time.sleep(3)
        assert bool(self.fc.fd["gesture"].verify_gesture_panel_banner_show()) is True, "Gesture panel banner is not displayed"

        self.fc.fd["gesture"].click_try_this_gesture_button()
        time.sleep(2)
        assert bool(self.fc.fd["gesture"].verify_play_pause_title_show()) is True, "Play / Pause title is not displayed"
        self.fc.fd["gesture"].click_play_pause_close_button()
        time.sleep(2)

        assert bool(self.fc.fd["gesture"].verify_pause_resume_toggle_show()) is True, "Pause resume toggle is not displayed"
        if self.fc.fd["gesture"].is_pause_resume_toggle_enabled() == "0":
            self.fc.fd["gesture"].click_pause_resume_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_pause_resume_toggle_enabled() == "1", "Pause resume toggle is not enabled"
        else:
            self.fc.fd["gesture"].click_pause_resume_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_pause_resume_toggle_enabled() == "0", "Pause resume toggle is not disabled"
        
        assert bool(self.fc.fd["gesture"].verify_volume_adjust_toggle_show()) is True, "Volume adjust toggle is not displayed"
        if self.fc.fd["gesture"].is_volume_adjust_toggle_enabled() == "0":
            self.fc.fd["gesture"].click_volume_adjust_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_volume_adjust_toggle_enabled() == "1", "Volume adjust toggle is not enabled"
        else:
            self.fc.fd["gesture"].click_volume_adjust_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_volume_adjust_toggle_enabled() == "0", "Volume adjust toggle is not disabled"
        
        assert bool(self.fc.fd["gesture"].verify_page_scroll_toggle_show()) is True, "Page scroll toggle is displayed"
        if self.fc.fd["gesture"].is_page_scroll_toggle_enabled() == "0":
            self.fc.fd["gesture"].click_page_scroll_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_page_scroll_toggle_enabled() == "1", "Page scroll toggle is not enabled"
        else:
            self.fc.fd["gesture"].click_page_scroll_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_page_scroll_toggle_enabled() == "0", "Page scroll toggle is not disabled"
        
        assert bool(self.fc.fd["gesture"].verify_photo_scroll_toggle_show()) is True, "Page scroll toggle is displayed"
        if self.fc.fd["gesture"].is_photo_scroll_toggle_enabled() == "0":
            self.fc.fd["gesture"].click_photo_scroll_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_photo_scroll_toggle_enabled() == "1", "Photo scroll toggle is not enabled"
        else:
            self.fc.fd["gesture"].click_photo_scroll_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_photo_scroll_toggle_enabled() == "0", "Photo scroll toggle is not disabled"

        self.fc.fd["gesture"].click_settings_button_on_gesture_page()
        time.sleep(2)
        assert self.fc.fd["gesture"].is_feedback_message_toggle_enabled() == "1", "Feedback message toggle is on by default"
        if self.fc.fd["gesture"].is_feedback_message_toggle_enabled() == "1":
            self.fc.fd["gesture"].click_feedback_message_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_feedback_message_toggle_enabled() == "0", "Feedback message toggle is not disabled"
        else:
            self.fc.fd["gesture"].click_feedback_message_toggle()
            time.sleep(2)
            assert self.fc.fd["gesture"].is_feedback_message_toggle_enabled() == "1", "Feedback message toggle is not enabled"
        self.fc.fd["gesture"].click_close_button_on_advanced_settings_page()


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["testudo"])
    def test_04_check_restore_defaults_function_C41593834(self):
        self.fc.restart_myHP()
        time.sleep(2)
        assert bool(self.fc.fd["home"].verify_gesture_card_show_on_home_page()) is True, "Gesture card is not displayed on home page"
 
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_gesture_module()

        self.fc.fd["gesture"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.fd["gesture"].click_pop_window_restore_defaults_button()
        time.sleep(2)
        self.fc.fd["gesture"].click_pause_resume_toggle()
        time.sleep(2)
        assert self.fc.fd["gesture"].is_pause_resume_toggle_enabled() == "1", "Pause resume toggle is disabled"
        time.sleep(2)
        self.fc.fd["gesture"].click_volume_adjust_toggle()
        time.sleep(2)
        assert self.fc.fd["gesture"].is_volume_adjust_toggle_enabled() == "1", "Volume adjust toggle is disabled"

        time.sleep(2)
        self.fc.fd["gesture"].click_settings_button_on_gesture_page()
        time.sleep(2)
        self.fc.fd["gesture"].click_feedback_message_toggle()
        assert self.fc.fd["gesture"].is_feedback_message_toggle_enabled() == "0", "Feedback message toggle is enabled"
        time.sleep(2)
        self.fc.fd["gesture"].click_close_button_on_advanced_settings_page()

        self.fc.fd["gesture"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.fd["gesture"].click_pop_window_restore_defaults_button()
        time.sleep(2)
        assert self.fc.fd["gesture"].is_pause_resume_toggle_enabled() == "0", "Pause resume toggle is not disabled"
        assert self.fc.fd["gesture"].is_volume_adjust_toggle_enabled() == "0", "Volume adjust toggle is not disabled"

        time.sleep(2)
        self.fc.fd["gesture"].click_settings_button_on_gesture_page()
        time.sleep(2)
        assert self.fc.fd["gesture"].is_feedback_message_toggle_enabled() == "1", "Feedback message toggle is not enabled"
        self.fc.fd["gesture"].click_close_button_on_advanced_settings_page()

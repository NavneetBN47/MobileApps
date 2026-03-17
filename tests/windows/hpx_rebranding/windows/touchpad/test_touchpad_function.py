import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Touchpad_Function(object):

    
    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_01_turn_on_off_enable_gesture_control_button_C43876470(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)

        self.fc.fd["touchpad"].click_restore_default_button()
        time.sleep(3)
        self.fc.fd["touchpad"].click_enable_gesture_control_button()

        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "1", "Enable gesture control button is off"
        time.sleep(3)
        self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(2)
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "Enable gesture control button is on"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_check_feedback_intensity_value_C43876472(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)

        self.fc.fd["touchpad"].click_adjust_feedback_intensity_link()
        time.sleep(3)
        self.fc.fd["touchpad"].click_windows_setting_feedback()
        time.sleep(3)

        assert self.fc.fd["touchpad"].get_windows_intensity_slider_value() == "50", "Windows intensity slider value is not 50"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_change_feedback_intensity_value_C43876474(self):
        time.sleep(3)
        intensity_calue = int(self.fc.fd["touchpad"].get_windows_intensity_slider_value())
        if intensity_calue < 100:
            self.fc.fd["touchpad"].set_slider_value_increase(4, "windows_intensity_slider")
            assert self.fc.fd["touchpad"].get_windows_intensity_slider_value() == "100", "Windows intensity slider value is not 100"
        else:
            self.fc.fd["touchpad"].set_slider_value_decrease(4, "windows_intensity_slider")
            assert self.fc.fd["touchpad"].get_windows_intensity_slider_value() == "0", "Windows intensity slider value is not 0"
        
        intensity_calue = int(self.fc.fd["touchpad"].get_windows_intensity_slider_value())
        if intensity_calue == 100:
            self.fc.fd["touchpad"].set_slider_value_decrease(2, "windows_intensity_slider")
        else:
            self.fc.fd["touchpad"].set_slider_value_increase(2, "windows_intensity_slider")
        self.fc.close_windows_settings_panel()
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_04_turn_off_windows_touchpad_toggle_C43879514(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)
        enable_gesture_control_button_state = self.fc.fd["touchpad"].verify_enable_gesture_control_button_state()
        if enable_gesture_control_button_state == "0":
            self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(3)
        self.fc.fd["touchpad"].click_adjust_feedback_intensity_link()
        time.sleep(3)
        self.fc.fd["touchpad"].click_windows_touchpad_togggle()
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.fd["touchpad"].verify_enable_touchpad_message_show() is True
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "Enable gesture control button is on"

        time.sleep(3)
        self.fc.fd["touchpad"].click_adjust_feedback_intensity_link()
        time.sleep(3)
        self.fc.fd["touchpad"].click_windows_touchpad_togggle()
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        enable_gesture_control_button_state = self.fc.fd["touchpad"].verify_enable_gesture_control_button_state()
        time.sleep(3)
        if enable_gesture_control_button_state == "1":
            self.fc.fd["touchpad"].click_enable_gesture_control_button()
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_05_turn_off_windows_touchpad_toggle_C43879512(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)
        enable_gesture_control_button_state = self.fc.fd["touchpad"].verify_enable_gesture_control_button_state()
        if enable_gesture_control_button_state == "0":
            self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(3)
        self.fc.fd["touchpad"].click_restore_default_button()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "Enable gesture control button is on"

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_contextual_config_for_touchpad_C53196591(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        # get contextual config touchpad card text ="Gesture control disabled"
        assert self.fc.fd["touchpad"].get_contextual_config_touchpad_card_text() =="Gesture control disabled", "Contextual config text is not displayed correctly"
        time.sleep(2)
        # click on Touchpad module card
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(2)
        # verify touchpad toggle default is off
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "Touchpad toggle is not off by default"
        time.sleep(2)
        # click back button to return pc-device page
        self.fc.fd["touchpad"].click_return_button_on_top_left_corner()
        time.sleep(2)
        # get contextual config touchpad card text ="Gesture control disabled"
        assert self.fc.fd["touchpad"].get_contextual_config_touchpad_card_text() =="Gesture control disabled", "Contextual config text is not displayed correctly"
        time.sleep(2)
        # click on Touchpad module card
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(2)
        # click enable gesture control button
        self.fc.fd["touchpad"].click_enable_gesture_control_button()
        time.sleep(2)
        # click back button to return pc-device page
        self.fc.fd["touchpad"].click_return_button_on_top_left_corner()
        time.sleep(2)
        # get contextual config touchpad card text ="Gesture control enabled"
        assert self.fc.fd["touchpad"].get_contextual_config_touchpad_card_text() =="Gesture control enabled", "Contextual config text is not displayed correctly"
        time.sleep(2)
        # click on Touchpad module card
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(2)
        self.fc.fd["touchpad"].click_restore_default_button()
        time.sleep(3)
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_07_navigate_to_each_button_use_tab_C51909716(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)

        self.fc.fd["touchpad"].press_tab("enable_gesture_button")
        time.sleep(2)
        assert self.fc.fd["touchpad"].is_focus_on_element("enable_gesture_button"), "Enable gesture button is not focused"
    

    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_08_press_alt_f4_from_keyboard_C51909725(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_touch_pad_lone_page(), "Touchpad card is not displayed"
        time.sleep(2)
        self.fc.fd["touchpad"].press_alt_f4_to_close_app()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_touch_pad_lone_page() is False, "Wellbeing card is displayed after alt+f4"
    

    @pytest.mark.function
    def test_09_module_launch_via_deeplink_C61634953(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://pctouchpad")
        time.sleep(5)
        assert self.fc.fd["touchpad"].verify_touchpad_title_show(), "Touchpad title is not shown"

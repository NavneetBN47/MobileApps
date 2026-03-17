import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smart_Experience(object):

    #this suite should run on ultron
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_smart_experience_navigation_using_keyboard_C51600499(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")    

        # Make sure toggle is OFF to start with 
        old_toggle_state = self.fc.fd["smart_experience"].get_auto_screen_dimming_toggle_button_state_ultron()
        if old_toggle_state == '1':
            self.fc.fd["smart_experience"].press_enter("auto_screen_dimming_toggle_button_ltwo_page")

        # press TAB and verify that the focus is on first toggle button
        self.fc.fd["smart_experience"].press_tab("auto_screen_dimming_text_ltwo_page")
        assert self.fc.fd["smart_experience"].is_focus_on_element("auto_screen_dimming_toggle_button_ltwo_page"), "Auto screen dimming toggle button is not highlighted."

        # press ENTER and verify that the toggle is turned ON
        self.fc.fd["smart_experience"].press_enter("auto_screen_dimming_toggle_button_ltwo_page")
        time.sleep(1)
        new_toggle_state = self.fc.fd["smart_experience"].get_auto_screen_dimming_toggle_button_state_ultron()
        assert  new_toggle_state == '1', "Auto screen dimming toggle switch is not ON."

        # press TAB and verify that the focus is on second toggle button
        self.fc.fd["smart_experience"].press_tab("auto_screen_dimming_toggle_button_ltwo_page")
        assert self.fc.fd["smart_experience"].is_focus_on_element("privacy_alert_toggle_button_ltwo_page"), "Privacy Alert toggle button is not highlighted."

        # press TAB and verify that the focus is on third toggle button
        self.fc.fd["smart_experience"].press_tab("privacy_alert_toggle_button_ltwo_page")
        assert self.fc.fd["smart_experience"].is_focus_on_element("enable_screen_blur_info_toggle_switch_ltwo_page"), "Enable screen blur info toggle switch is not highlighted."

        # press  SHIFT + TAB and verify that the focus is back on 2nd toggle button
        self.fc.fd["smart_experience"].press_reverse_tab("enable_screen_blur_info_toggle_switch_ltwo_page")
        assert self.fc.fd["smart_experience"].is_focus_on_element("privacy_alert_toggle_button_ltwo_page"), "Privacy Alert toggle button is not highlighted."

        # press  SHIFT + TAB and verify that the focus is back on 1st toggle button
        self.fc.fd["smart_experience"].press_reverse_tab("privacy_alert_toggle_button_ltwo_page")
        assert self.fc.fd["smart_experience"].is_focus_on_element("auto_screen_dimming_text_ltwo_page"), "Auto screen dimming text is not highlighted."

        # press ALT + F4 to close the app
        self.fc.fd["smart_experience"].press_alt_f4_to_close_app()

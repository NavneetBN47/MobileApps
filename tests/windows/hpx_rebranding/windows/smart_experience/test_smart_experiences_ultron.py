import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smart_Experience(object):

    @pytest.mark.commercial
    @pytest.mark.ota
    def test_01_navigate_to_presence_detection_card_C51244806(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page(), "Presence detection is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")        
        assert self.fc.fd["smart_experience"].verify_pivacy_alert_text_ultron_ltwo_page(), "Privacy Alert text is not displayed" 
        assert self.fc.fd["smart_experience"].verify_pivacy_alert_description_ultron_ltwo_page(), "Privacy Alert description is not displayed" 
        assert self.fc.fd["smart_experience"].verify_privacy_alert_toggle_button_ltwo_page(), "Privacy Alert toggle button is not displayed"        
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_ultron_text_ltwo_page(), "Auto Screen Dimming text is not displayed"
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_description_ultron_ltwo_page(), "Auto Screen Dimming description is not displayed"
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_toggle_button_ltwo_page(), "Auto Screen Dimming toggle button is not displayed"
        assert self.fc.fd["smart_experience"].verify_restore_default_button_ltwo_page(), "Restore Default button is not displayed"
    
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_02_presence_detection_ui_visability_C52983145(self):
        assert self.fc.fd["smart_experience"].verify_pivacy_alert_text_ultron_ltwo_page(), "Privacy Alert text is not displayed" 
        assert self.fc.fd["smart_experience"].verify_privacy_alert_toggle_button_ltwo_page(), "Privacy Alert toggle button is not displayed" 
        privacy_alert_description = self.fc.fd["smart_experience"].get_privacy_alert_description_two_page()
        assert privacy_alert_description == "Notifies you when an onlooker is detected in the background.", "Desription does not match. Expected: Notifies you when an onlooker is detected in the background. " + privacy_alert_description
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_ultron_text_ltwo_page(), "Auto Screen Dimming text is not displayed"
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_toggle_button_ltwo_page(), "Auto Screen Dimming toggle button is not displayed"
        auto_dimming_description = self.fc.fd["smart_experience"].get_auto_screen_dimming_description_two_page()
        assert auto_dimming_description == "When you look away from the screen, the screen will dim to save power.", "Description does not match. Expected: When you look away from the screen, the screen will dim to save power., Actual: " + auto_dimming_description
        assert self.fc.fd["smart_experience"].get_enable_screen_blur_toggle_button_state() == "0", "Screen Blur should be disabled by default"
        assert self.fc.fd["smart_experience"].verify_restore_default_button_ltwo_page(), "Restore Default button is not displayed"

    @pytest.mark.commercial
    @pytest.mark.ota
    def test_03_presence_detection_default_settings_C52984688(self):
        assert self.fc.fd["smart_experience"].get_enable_screen_blur_toggle_button_state() == "0", "Screen Blur should be disabled by default"      
        assert  self.fc.fd["smart_experience"].get_auto_screen_dimming_toggle_button_state_ultron() == "0", "Auto Screen Dimming should be disabled by default"
        assert  self.fc.fd["smart_experience"].get_pivacy_alert_toggle_button_state_ultron() == "0", "Privacy Alert should be disabled by default"
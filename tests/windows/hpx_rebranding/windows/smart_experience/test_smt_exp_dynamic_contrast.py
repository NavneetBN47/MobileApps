import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smart_Experience(object):
    
    #this test case is for masadansku5 as we only have 1 device available for this testing
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_for_dynamic_contrast_feature_C52987778(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        time.sleep(5)
        presence_detection_header_text_lwo_page = self.fc.fd["smart_experience"].get_camera_and_presence_detection_header_masadan_ltwo_page()
        assert presence_detection_header_text_lwo_page == "Presence detection","presence detection text is not present."
        
        assert self.fc.fd["smart_experience"].verify_intelligent_dynamic_contrast_text_ltwo_page(), "Intelligent dynamic contrast card text is not displayed"
        assert self.fc.fd["smart_experience"].verify_intelligent_dynamic_contrast_description_ltwo_page(), "Intelligent dynamic contrast card description is not displayed"
        assert self.fc.fd["smart_experience"].verify_attention_focus_text_ltwo_page(), "Attention focus card text is not displayed"
        assert self.fc.fd["smart_experience"].verify_attention_focus_description_ltwo_page(), "Attention focus card description is not displayed"

    #this test case is for masadansku5 as we only have 1 device available for this testing
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_persistent_of_attention_focus_C51244813(self):
        logging.info(f"Platform {self.platform.lower()}")
        current_state = self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state()
        if current_state == "0":
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["smart_experience"].click_attention_focus_toggle_button_toggle_button_state()
            current_state = self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state()
            assert current_state == "1", f"Expected '1' (On), but got '{current_state}'"
        
        self.fc.restart_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")

        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")

        current_state = self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state()
        assert current_state == "1", f"Expected '1' (On), but got '{current_state}'"
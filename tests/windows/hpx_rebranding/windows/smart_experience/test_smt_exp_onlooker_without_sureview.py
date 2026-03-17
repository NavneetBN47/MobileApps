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
    def test_01_onlooker_detection_on_screen_blur_supported_unit_C51244795(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")
    
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")
        self.fc.fd["smart_experience"].click_presence_detection_card()
        time.sleep(5)
        presence_detection_header_text_lwo_page = self.fc.fd["smart_experience"].get_camera_and_presence_detection_header_masadan_ltwo_page()
        assert presence_detection_header_text_lwo_page == "Presence detection","presence detection text is not present."
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        if current_state == "0":
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button()
            current_state = self.fc.fd["smart_experience"].get_enable_screen_blur_toggle_button_state()
            assert current_state == "0", f"Expected '0' (Off), but got '{current_state}'"
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        if current_state == "1":
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button() 
            current_state = self.fc.fd["smart_experience"].get_enable_screen_blur_toggle_button_state()
            assert current_state == "0", f"Expected '0' (Off), but got '{current_state}'"

    #this test case is for masadansku5 as we only have 1 device available for this testing 
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_persistent_of_onlooker_detection_C51244812(self):
        logging.info(f"Platform {self.platform.lower()}")
       
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        if current_state == "0":
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button()
            current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
            assert current_state == "1", f"Expected '1' (On), but got '{current_state}'"
        self.fc.close_myHP()
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        # self.fc.swipe_window(direction="down", distance=2)
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")

        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Camera and presence detection card is not present."
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")
        self.fc.fd["smart_experience"].click_presence_detection_card()
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        assert current_state == "1", f"Expected '1' (On), but got '{current_state}'"
        self.fc.close_myHP()
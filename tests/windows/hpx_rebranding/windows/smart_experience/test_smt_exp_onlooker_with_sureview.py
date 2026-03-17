import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Smart_Experience(object):

    #this test case is for masadanxsku4 as we only have 1 device availiable for this testing
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_onlooker_detection_on_sure_view_supported_unit_C51244792(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        self.fc.fd["smart_experience"].click_presence_detection_card()
        time.sleep(5)
        presence_detection_header_text_lwo_page = self.fc.fd["smart_experience"].get_camera_and_presence_detection_header_masadan_ltwo_page()
        assert presence_detection_header_text_lwo_page == "Presence detection","Presence detection text is not present."
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        if current_state == "0":
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button()
            current_state = self.fc.fd["smart_experience"].get_enable_sure_view_toggle_button_state()
            assert current_state == "0", f"Expected '0' (Off), but got '{current_state}'"
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        if current_state == "1":
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button() 
            current_state = self.fc.fd["smart_experience"].get_enable_sure_view_toggle_button_state()
            assert current_state == "0", f"Expected '0' (Off), but got '{current_state}'"

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_tooltip_description_sureview_C51244816(self):
        logging.info(f"Platform {self.platform.lower()}")
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        if current_state == "0":
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button()
            current_state = self.fc.fd["smart_experience"].get_enable_sure_view_toggle_button_state()
            assert current_state == "0", f"Expected '0' (Off), but got '{current_state}'"
        self.fc.fd["smart_experience"].click_sure_view_tooltip()
        sure_view_tooltip_description_text = self.fc.fd["smart_experience"].get_sure_view_tooltip_description_text()
        assert "Automatically turn on SureView " in sure_view_tooltip_description_text, f"Tooltip text mismatch: {sure_view_tooltip_description_text}"
        self.fc.close_myHP()
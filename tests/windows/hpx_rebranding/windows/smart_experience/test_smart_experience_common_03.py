import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smart_Experience(object):

    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_01_contextual_config_presence_detection_C53532685(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=5) 
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        assert self.fc.fd["smart_experience"].verify_auto_hdr_text_ltwo_page(), "Auto HDR card text is not displayed"
        assert self.fc.fd["smart_experience"].verify_auto_hdr_description_ltwo_page(), "Auto HDR card description is not displayed"
        time.sleep(3)
        self.fc.fd["smart_experience"].get_focus_on_app("auto_hdr_text_ltwo_page")
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["smart_experience"].click_restore_default_button_ltwo_page()
        if self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "1":
            time.sleep(10)
            #App is loosing focus while clicking on the back button
            self.fc.fd["smart_experience"].get_focus_on_app("auto_hdr_text_ltwo_page")
            self.fc.swipe_window(direction="up", distance=3)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            for _ in range(2):
                self.fc.swipe_window(direction="down", distance=3)
                if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                    break
                else:
                    self.fc.swipe_window(direction="up", distance=3)
                    self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(10)
            self.fc.swipe_window(direction="down", distance=3)
            description = self.fc.fd["smart_experience"].get_presence_detection_contextual_text()
            assert description == "Auto HDR enabled", f"Expected 'Auto HDR enabled', but got: {description}"
        else:
            pytest.fail("Failed to enable Auto HDR")
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        time.sleep(3)
        if self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "1":
            self.fc.fd["smart_experience"].get_focus_on_app("auto_hdr_text_ltwo_page")
            self.fc.fd["smart_experience"].click_auto_hdr_toggle_button()
            if self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "0":
                self.fc.swipe_window(direction="up", distance=3)
                self.fc.fd["devicesMFE"].click_back_button_rebranding()
                for _ in range(2):
                    self.fc.swipe_window(direction="down", distance=3)
                    if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                        break
                    else:
                        self.fc.fd["devicesMFE"].click_back_button_rebranding()
                self.fc.swipe_window(direction="down", distance=3)
                description = self.fc.fd["smart_experience"].get_presence_detection_contextual_text()
                assert description == "Auto HDR disabled", f"Expected 'Auto HDR disabled', but got: {description}"
            else:
                pytest.fail("Failed to disable Auto HDR")   

    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_02_reset_application_C51244823(self):
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        self.fc.fd["smart_experience"].get_focus_on_app("auto_hdr_text_ltwo_page")
        self.fc.swipe_window(direction="up", distance=3)
        if current_state == "0":
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button()
            current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
            assert current_state == "1", f"Expected '1' (On), but got '{current_state}'"
        current_state = self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state()
        if current_state == "0":
            self.fc.fd["smart_experience"].click_attention_focus_toggle_button_toggle_button_state()
            current_state = self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state()
            assert current_state == "1", f"Expected '1' (On), but got '{current_state}'"
        self.fc.reset_hp_application()
        time.sleep(3)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=5) 
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        assert self.fc.fd["smart_experience"].verify_auto_hdr_text_ltwo_page(), "Auto HDR card text is not displayed"
        assert self.fc.fd["smart_experience"].verify_auto_hdr_description_ltwo_page(), "Auto HDR card description is not displayed"
        time.sleep(3)
        current_state = self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state()
        assert current_state == "0", f"Expected '0' (Off), but got '{current_state}'"
        current_state = self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state()
        assert current_state == "0", f"Expected '0' (Off), but got '{current_state}'"
        self.fc.close_myHP()
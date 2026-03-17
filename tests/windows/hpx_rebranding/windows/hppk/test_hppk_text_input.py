import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Hppk_Text_Input(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_select_text_input_C42901051(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_text_input_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].input_text_input("www!2345,.aas:/.,.//>*(0)")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["hppk"].click_key_text_input_save_button()
        time.sleep(2)
        self.fc.fd["hppk"].click_prog_key_back_btn()

        assert self.fc.fd["hppk"].get_key_sequence_config_value() == "Text input"


    @pytest.mark.ota
    @pytest.mark.function
    def test_02_configurations_persistent_for_text_input_C42901054(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_automation_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_website(), "Website value is not visible in dropdown"
        time.sleep(2)
        self.fc.fd["hppk"].click_application_from_dropdown()
        time.sleep(2)
        self.fc.fd["hppk"].click_application_list_cancel_button()
        time.sleep(2)
        self.fc.fd["hppk"].click_text_input_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_prog_key_back_btn()

        assert self.fc.fd["hppk"].get_key_sequence_config_value() == "Text input"
    

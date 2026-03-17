import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Hppk_UI(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_hppk_hpone_ui_C43812328(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        assert self.fc.fd["hppk"].verify_programmabe_card_visible(), "Programmable key card is not displayed"
        assert self.fc.fd["hppk"].verify_support_key_card_visible(), "support key card is not displayed"
        assert self.fc.fd["hppk"].verify_pc_device_key_card_visible(), "pc device card is not displayed"

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_hppk_programmable_key_detail_ui_C42900998(self):
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        self.fc.fd["hppk"].verify_assign_programmable_header_text() == "Assign programmable key"
        # automation, key sequence, text input, myHP programmable key text verify
        assert self.fc.fd["hppk"].verify_automation_text() == "Automation", "Automation radio button text is not visible"
        assert self.fc.fd["hppk"].verify_key_sequence_text() == "Key sequence", "Key sequence radio button text is not visible"
        assert self.fc.fd["hppk"].verify_text_input_text() == "Text input", "Text input radio button text is not visible"
        assert self.fc.fd["hppk"].verify_programmable_key_text() == "HP programmable key", "myHP Programmable Key radio button text is not visible"
        # automation, key sequence, text input, myHP programmable key radio button verify
        assert self.fc.fd["hppk"].verify_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_programmable_key_radio_button_is_selected()) == True

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_hppk_support_key_detail_ui_C42901005(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_support_key_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].verify_support_key_header_text() == "Assign support key"
        assert self.fc.fd["hppk"].verify_support_key_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_support_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_support_key_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_hp_support_radio_button_is_selected()) == True

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_hppk_pc_device_key_detail_ui_C42901007(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(2)
        self.fc.fd["hppk"].click_hpone_pc_device_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].verify_pc_device_key_header_text() == "Assign PC device key"
        assert self.fc.fd["hppk"].verify_pc_device_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_pc_device_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_pc_device_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_hp_pc_device_radio_button_is_selected()) == True


import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Hppk_Commercial_UI(object):

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_hppk_commercial_ui_C42900996(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        assert self.fc.fd["hppk"].verify_progkey_info_icon_visible(), "Programmable key info icon is not displayed"
        assert self.fc.fd["hppk"].verify_progkey_menucard_shift_visible(), "Programmable key shift card is not visible"
        assert self.fc.fd["hppk"].verify_progkey_menucard_ctl_visible(), "Programmable key ctrl card is not visible"
        assert self.fc.fd["hppk"].verify_progkey_menucard_alt_visible(), "Programmable key alt card is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_hppk_programmable_key_detail_ui_C51871477(self):
        if self.fc.fd["hppk"].verify_programmabe_header_visible() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
            time.sleep(3)
        self.fc.fd["hppk"].click_progkey_menucard_arrow_btn()
        self.fc.fd["hppk"].verify_assign_programmable_header_text() == "Assign programmable key"
        assert self.fc.fd["hppk"].verify_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_programmable_key_radio_button_is_selected()) == True
        self.fc.fd["hppk"].click_prog_key_back_btn()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_hppk_shift_key_detail_ui_C42900999(self):
        if self.fc.fd["hppk"].verify_programmabe_header_visible() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
            time.sleep(3)
        self.fc.fd["hppk"].click_progkey_menucard_shift_arrow_btn()
        self.fc.fd["hppk"].verify_shift_key_header_text() == "Assign shift + programmable key"
        # automation, key sequence, text input, myHP programmable key text and radio button verify
        assert self.fc.fd["hppk"].verify_automation_text() == "Automation", "Automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_key_sequence_text() == "Key sequence", "Key sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_text_input_text() == "Text input", "Text input radio button is not visible"
        assert self.fc.fd["hppk"].verify_programmable_key_text() == "Not assigned", "myHP Programmable Key radio button is not visible"

        assert self.fc.fd["hppk"].verify_shift_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_shift_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_shift_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_shift_not_assigned_radio_button_is_selected()) == True
        self.fc.fd["hppk"].click_prog_key_back_btn()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_hppk_ctrl_key_detail_ui_C42901000(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)
        self.fc.fd["hppk"].click_progkey_menucard_ctl_arrow_btn()
        self.fc.fd["hppk"].verify_ctl_key_header_text() == "Assign ctrl + programmable key"
        assert self.fc.fd["hppk"].verify_ctl_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_ctl_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_ctl_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_ctl_not_assigned_radio_button_is_selected()) == True
        self.fc.fd["hppk"].click_prog_key_back_btn()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_hppk_alt_key_detail_ui_C42901001(self):
        if self.fc.fd["hppk"].verify_programmabe_header_visible() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
            time.sleep(3)
        self.fc.fd["hppk"].click_progkey_menucard_alt_arrow_btn()
        self.fc.fd["hppk"].verify_alt_key_header_text() == "Assign alt + programmable key"
        assert self.fc.fd["hppk"].verify_alt_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_alt_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_alt_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_alt_not_assigned_radio_button_is_selected()) == True

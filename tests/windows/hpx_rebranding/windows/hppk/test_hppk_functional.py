import pytest
import time
from selenium.webdriver.common.keys import Keys

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Hppk_Functional(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_launch_hppk_via_deeplink_C50950188(self):
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.launch_module_using_deeplink("hpx://progkey")
        time.sleep(10)
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        assert "Programmable key" in self.fc.fd["hppk"].verify_programmabe_header_text(), "Programmable Keys text is not matching"

    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_click_on_programmable_key_C43812383(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].verify_assign_programmable_header_text() == "Assign programmable key"
        assert self.fc.fd["hppk"].verify_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_programmable_key_radio_button_is_selected()) == True

    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_click_on_support_page_key_C43812401(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)
        self.fc.fd["hppk"].click_hpone_support_key_menucard_arrow_btn()
        self.fc.fd["hppk"].verify_support_key_header_text() == "Assign support key"
        assert self.fc.fd["hppk"].verify_support_key_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_support_key_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_support_key_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_hp_support_radio_button_is_selected()) == True
    
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_04_click_on_pc_device_page_key_C43812406(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)
        self.fc.fd["hppk"].click_hpone_pc_device_menucard_arrow_btn()
        self.fc.fd["hppk"].verify_pc_device_key_header_text() == "Assign PC device key"
        assert self.fc.fd["hppk"].verify_pc_device_automation_radio_btn_visible(), "automation radio button is not visible"
        assert self.fc.fd["hppk"].verify_pc_device_sequence_radio_btn_visible(), "sequence radio button is not visible"
        assert self.fc.fd["hppk"].verify_pc_device_text_input_radio_btn_visible(), "input text radio button is not visible"
        assert bool(self.fc.fd["hppk"].verify_hp_pc_device_radio_button_is_selected()) == True
    

    @pytest.mark.function
    def test_05_hppk_with_tab_key_navigation_C42901068(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)

        self.fc.fd["hppk"].press_tab("progkey_menu_card_value")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("progkey_menu_card_value"), "Programmable key menu card is not focused"
        time.sleep(2)
        self.fc.fd["hppk"].press_tab("supportkey_menu_card_value")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("supportkey_menu_card_value"), "Support key menu card is not focused"
        time.sleep(2)
        self.fc.fd["hppk"].press_tab("pcdevicekey_menu_card_value")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("pcdevicekey_menu_card_value"), "PC device key menu card is not focused"
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].press_tab("automation_radio_btn")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("automation_radio_btn"), "Automation radio button is not focused"
        time.sleep(2)
        self.fc.fd["hppk"].press_tab("key_sequence_radio_btn")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("key_sequence_radio_btn"), "Key sequence radio button is not focused"
        time.sleep(2)
        self.fc.fd["hppk"].press_tab("text_input_radio_btn")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("text_input_radio_btn"), "Text input radio button is not focused"
        time.sleep(2)
        self.fc.fd["hppk"].press_tab("hp_prog_key_radio_btn")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("hp_prog_key_radio_btn"), "HP programmable key radio button is not focused"
        time.sleep(2)

        self.fc.fd["hppk"].press_reverse_tab("text_input_radio_btn")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("text_input_radio_btn"), "Text input radio button is not focused"
        time.sleep(2)
        self.fc.fd["hppk"].press_reverse_tab("key_sequence_radio_btn")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("key_sequence_radio_btn"), "Key sequence radio button is not focused"
        time.sleep(2)
        self.fc.fd["hppk"].press_reverse_tab("automation_radio_btn")
        time.sleep(2)
        assert self.fc.fd["hppk"].is_focus_on_element("automation_radio_btn"), "Automation radio button is not focused"


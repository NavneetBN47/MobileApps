import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Hp_Go(object):

    #this suite should only run on Lapaz platforms
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_hpgo_verify_hp_go_card_in_pc_device_C52101499(self):
        self.fc.maximize_and_verify_device_card()
        time.sleep(2)
        self.fc.fd["hp_go"].scroll_to_element("hp_go_card_on_pcdevice_page")
        assert self.fc.fd["devices_details_pc_mfe"].verify_hp_go_card_show_on_pc_device_page(), "hp go card is not displayed"
        hp_go_text_on_hpgo_card = self.fc.fd["devices_details_pc_mfe"].get_hp_go_text_on_hpgo_card()
        assert hp_go_text_on_hpgo_card == "HP Go", f"hp go text is not displayed on hp go card, actual text: {hp_go_text_on_hpgo_card}"
        hpgo_usage_text = self.fc.fd["devices_details_pc_mfe"].get_usage_on_hpgo_card()
        assert hpgo_usage_text == "Low usage", f"usage text is not displayed on hp go card, actual text: {hpgo_usage_text}"
        assert self.fc.fd["devices_details_pc_mfe"].verify_hpgo_icon_on_card(), "hp go icon is not displayed on hp go card"
        assert self.fc.fd["hp_go"].verify_hp_go_in_system_tray(), "hp go tile is not displayed in system tray"

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_hpgo_verify_page_content_C52101500(self):
        self.fc.fd["devices_details_pc_mfe"].click_hp_go_card()
        for _ in range(5):
            if self.fc.fd["hp_go"].verify_hp_go_status_text():
                logging.info("HP Go status text is displayed successfully.")
                break
            else:
                logging.info("HP Go status text is not displayed.")
                self.fc.restart_app_navigate_to_hp_go()
        
        time.sleep(2)
        assert self.fc.fd["hp_go"].verify_hp_go_title_on_hp_go_page(), "HP Go title is not displayed"
        hp_go_title_text = self.fc.fd["hp_go"].get_hp_go_title()
        assert hp_go_title_text == "HP Go", f"HP Go title text is not displayed correctly, actual text: {hp_go_title_text}"
        assert self.fc.fd["hp_go"].verify_hp_go_information_txt_on_hp_go_page(), "HP Go information text is not displayed"
        hp_go_information_text = self.fc.fd["hp_go"].get_hp_go_information_txt()
        assert hp_go_information_text == "HP Go information", f"HP Go information text is not displayed correctly, actual text: {hp_go_information_text}"
        assert self.fc.fd["hp_go"].verify_hp_go_connection_txt_on_hp_go_page(), "HP Go connection text is not displayed"
        connection_text = self.fc.fd["hp_go"].get_connection_txt()
        assert connection_text == "Connection", f"HP Go connection text is not displayed correctly, actual text: {connection_text}"
        connection_hpgo_text = self.fc.fd["hp_go"].get_connection_hp_go()
        assert connection_hpgo_text == "HP Go", f"HP Go text is not displayed correctly, actual text: {connection_hpgo_text}"
        hp_go_status_text = self.fc.fd["hp_go"].get_hp_go_status_text()
        assert hp_go_status_text == "Active", f"Active status text is not displayed correctly, actual text: {hp_go_status_text}"
        hp_go_usage_text = self.fc.fd["hp_go"].get_hp_go_usage_text()
        assert hp_go_usage_text == "Low" or hp_go_usage_text == "Medium" or hp_go_usage_text == "High", f"Low/Medium/High usage text is not displayed correctly, actual text: {hp_go_usage_text}"
        assert self.fc.fd["hp_go"].verify_eid_number(), "EID number is not displayed"
        assert self.fc.fd["hp_go"].verify_eid_copy_btn(), "EID copy button is not displayed"
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_hpgo_copy_icon_C52101502(self):
        self.fc.fd["hp_go"].click_eid_copy_btn()
        eid_number =self.fc.fd["hp_go"].get_eid_number()
        logging.info(f"EID number copied from app: {eid_number}")
        eid_from_clipboard = self.fc.get_clipboard_content()
        logging.info(f"EID number from clipboard: {eid_from_clipboard}")
        assert eid_number == eid_from_clipboard, "EID number is not copied to clipboard"

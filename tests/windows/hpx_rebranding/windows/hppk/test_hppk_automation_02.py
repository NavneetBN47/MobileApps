import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Hppk_Automation_02(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_add_invalid_website_C42901017(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_website(), "Website value is not visible in dropdown"
        self.fc.fd["hppk"].click_website_from_dropdown()
        self.fc.fd["hppk"].add_website("www")
        self.fc.fd["hppk"].click_enter_key("website_text_field")
        time.sleep(3)
        assert self.fc.fd["hppk"].verify_app_delete_btn_visible() is False, "Website delete button is visible"
        self.fc.fd["hppk"].add_website("www hp com")
        self.fc.fd["hppk"].click_enter_key("website_text_field")
        assert self.fc.fd["hppk"].verify_app_delete_btn_visible() is False, "Website delete button is visible"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_select_website_C42901016(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_website(), "Website value is not visible in dropdown"
        time.sleep(2)
        self.fc.fd["hppk"].click_website_from_dropdown()
        time.sleep(2)
        self.fc.fd["hppk"].click_website_cancel_button()
        time.sleep(2)
        assert self.fc.fd["hppk"].verify_assign_programmable_header(), "Assign Programmable Key header is not visible"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_esc_key_for_website_C42901020(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        self.fc.fd["hppk"].click_website_from_dropdown()
        time.sleep(2)
        self.fc.fd["hppk"].add_website("www.hp.com")
        time.sleep(3)
        self.fc.fd["hppk"].click_enter_key("website_text_field")
        assert self.fc.fd["hppk"].verify_assign_programmable_header(), "Assign Programmable Key header is not visible"
    
    
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Hppk_Key_Sequence(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_select_key_sequence_C42901037(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_hp_prog_key_radio_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].input_key_sequence("AAAAA")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["hppk"].click_key_sequence_save_button()
        time.sleep(2)
        self.fc.fd["hppk"].click_prog_key_back_btn()

        assert self.fc.fd["hppk"].get_key_sequence_config_value() == "A+A+A+A+A"


    @pytest.mark.ota
    @pytest.mark.function
    def test_02_configurations_persistent_for_key_sequence_C42901053(self):
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
        self.fc.fd["hppk"].click_application_from_dropdown()
        time.sleep(2)
        self.fc.fd["hppk"].click_application_list_cancel_button()
        time.sleep(2)
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        time.sleep(2)
        assert self.fc.fd["hppk"].verify_key_sequence_text_field_show(), "Key sequence text field is not visible"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_key_sequence_l2_page_C53193681(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        time.sleep(2)
        if self.fc.fd["hppk"].verify_key_sequence_delete_icon_show():
            time.sleep(2)
            self.fc.fd["hppk"].delete_key_sequence()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_radio_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].input_key_sequence("WWWWW")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["hppk"].click_key_sequence_save_button()
        time.sleep(2)
        self.fc.fd["hppk"].click_prog_key_back_btn()

        assert self.fc.fd["hppk"].get_key_sequence_config_value() == "W+W+W+W+W"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_configurations_persistent_automation_C42901052(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(2)
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_application(), "Application value is not visible in dropdown"
        self.fc.fd["hppk"].click_application_from_dropdown()
        self.fc.fd["hppk"].select_admin_tool_from_application_dropdown()
        self.fc.fd["hppk"].click_enter_key("prog_key_detail_admin_app")
        time.sleep(3)
        assert self.fc.fd["hppk"].verify_app_delete_btn_visible(), "Application delete button is not visible"
        assert self.fc.fd["hppk"].verify_admin_tool_app_visible(), "Admin Tool application is not visible"
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(3)

        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(2)
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        time.sleep(2)
        if self.fc.fd["hppk"].verify_key_sequence_delete_icon_show():
            time.sleep(2)
            self.fc.fd["hppk"].delete_key_sequence()
        time.sleep(3)
        self.fc.fd["hppk"].click_automation_radio_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        time.sleep(2)
        self.fc.fd["hppk"].input_key_sequence("WWWWW")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        if self.fc.fd["hppk"].get_key_sequence_config_value() != "W+W+W+W+W":
            time.sleep(2)
            self.fc.fd["hppk"].input_key_sequence("WWWWW")
            time.sleep(2)
        self.fc.fd["hppk"].delete_key_sequence()
        assert self.fc.fd["hppk"].get_key_sequence_config_value() != "W+W+W+W+W", "Key sequence is not deleted"
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["hppk"].click_prog_key_back_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()

        time.sleep(2)
        assert self.fc.fd["hppk"].verify_admin_tool_app_visible(), "Admin Tool application is not visible"
        time.sleep(2)
        self.fc.fd["hppk"].click_app_delete_btn()
    

    @pytest.mark.function
    def test_05_back_button_C42901062(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(2)
        assert self.fc.fd["hppk"].verify_programmabe_header_visible()
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
    

    @pytest.mark.function
    def test_06_hppk_consistency_C42901056(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"

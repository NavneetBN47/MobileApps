from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Hppk_Automation(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_ui_select_automation_C42901009(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_automation_radio_btn()
        assert self.fc.fd["hppk"].verify_automation_dropdown_visible(), "Automation dropdown is not displayed"
        assert self.fc.fd["hppk"].verify_add_action_text_visible(), "Add action text is not visible"
        self.fc.fd["hppk"].click_prog_key_detail_back_btn()

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_verify_automation_dropdown_values_C42901010(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_automation_radio_btn()
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_application(), "Application value is not visible in dropdown"
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_website(), "Website value is not visible in dropdown"
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_folder(), "Folder value is not visible in dropdown"
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_file(), "File value is not visible in dropdown"
        self.fc.fd["hppk"].click_automation_dropbox_btn()

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_add_application_using_enter_key_C42901013(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_automation_radio_btn()
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_application(), "Application value is not visible in dropdown"
        self.fc.fd["hppk"].click_application_from_dropdown()
        self.fc.fd["hppk"].select_admin_tool_from_application_dropdown()
        self.fc.fd["hppk"].click_enter_key("prog_key_detail_admin_app")
        time.sleep(3)
        assert self.fc.fd["hppk"].verify_app_delete_btn_visible(), "Application delete button is not visible"
        assert self.fc.fd["hppk"].verify_admin_tool_app_visible(), "Admin Tool application is not visible"
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["hppk"].click_app_delete_btn()
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_verify_esc_key_for_application_C42901014(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        if self.fc.fd["hppk"].verify_app_delete_btn_visible():
            time.sleep(2)
            self.fc.fd["hppk"].click_app_delete_btn()
            time.sleep(2)
        self.fc.fd["hppk"].click_automation_radio_btn()
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_application(), "Application value is not visible in dropdown"
        self.fc.fd["hppk"].click_application_from_dropdown()
        self.fc.fd["hppk"].select_admin_tool_from_application_dropdown()
        self.fc.fd["hppk"].click_esc_key("prog_key_detail_admin_app")
        time.sleep(2)
        assert bool(self.fc.fd["hppk"].verify_admin_tool_app_visible()) is False, "Admin Tool application is visible"
        assert bool(self.fc.fd["hppk"].verify_app_delete_btn_visible()) is False, "Application delete button is visible"
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(3)
        self.fc.fd["hppk"].click_automation_dropbox_btn()
        time.sleep(2)
        assert self.fc.fd["hppk"].verify_automation_dropbox_value_application(), "Application value is not visible in dropdown"
      

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_automation_delete_application_C42901015(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
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
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(3)
        self.fc.fd["hppk"].click_app_delete_btn()
        time.sleep(2)
        assert bool(self.fc.fd["hppk"].verify_admin_tool_app_visible()) is False, "Admin Tool application is visible"
        assert bool(self.fc.fd["hppk"].verify_app_delete_btn_visible()) is False, "Application delete button is visible"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_enter_key_for_website_C42901019(self):
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
        self.fc.fd["hppk"].click_website_from_dropdown()
        self.fc.fd["hppk"].add_website("www.hp.com")
        self.fc.fd["hppk"].click_enter_key("website_text_field")
        time.sleep(3)
        assert self.fc.fd["hppk"].verify_app_delete_btn_visible(), "Website delete button is not visible"
        assert self.fc.fd["hppk"].verify_website_icon_visible(), "Website icon is not visible"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_07_delete_for_website_C42901021(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(3)
        self.fc.fd["hppk"].click_app_delete_btn()
        time.sleep(2)
        assert bool(self.fc.fd["hppk"].verify_app_delete_btn_visible()) is False, "Website delete button is visible"
        assert self.fc.fd["hppk"].verify_website_icon_visible() is False, "Website icon is visible"

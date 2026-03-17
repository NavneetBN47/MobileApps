import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Task_Group_03(object):


    @pytest.mark.function
    def test_01_create_new_task_group_decline_C60184436(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        self.fc.fd["task_group"].click_privacy_pop_windows_decline_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group create new button is not displayed after declining privacy pop up"
    

    @pytest.mark.function
    def test_02_create_new_task_group_agree_C60184437(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        self.fc.fd["task_group"].click_privacy_pop_window_agree_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show() is False, "Task group create new button is not displayed after agreeing to privacy pop up"
    

    @pytest.mark.function
    def test_03_create_task_group_for_primary_display_C60184438(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        self.fc.fd["task_group"].click_windows_explorer_on_taskbar()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)

        self.fc.fd["task_group"].input_short_key_name("HPX1")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["task_group"].click_shortkey_dropdown()
        time.sleep(2)
        self.fc.fd["task_group"].select_shortkey_shift12()
        time.sleep(2)
        self.fc.fd["task_group"].click_edit_task_group_save_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show(), "Explorer icon is not displayed in task group list"
        time.sleep(2)
        self.fc.fd["task_group"].click_task_arrow_icon()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()


    @pytest.mark.function
    def test_04_save_group_name_and_shift12_C60184439(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_task_arrow_icon_show():
            time.sleep(2)
            self.fc.fd["task_group"].click_task_arrow_icon()
            time.sleep(2)
            self.fc.fd["task_group"].click_delete_task_button()
            time.sleep(2)
            if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
                self.fc.fd["task_group"].click_delete_pop_window_continue_button()

        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        self.fc.fd["task_group"].click_windows_explorer_on_taskbar()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)

        self.fc.fd["task_group"].input_short_key_name("HPX1")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["task_group"].click_shortkey_dropdown()
        time.sleep(2)
        self.fc.fd["task_group"].select_shortkey_shift12()
        time.sleep(2)
        self.fc.fd["task_group"].click_edit_task_group_save_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show(), "Explorer icon is not displayed in task group list"
        time.sleep(2)
        self.fc.fd["task_group"].click_task_arrow_icon()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()
    

    @pytest.mark.function
    def test_05_save_group_name_and_alt12_C60184440(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_task_arrow_icon_show():
            time.sleep(2)
            self.fc.fd["task_group"].click_task_arrow_icon()
            time.sleep(2)
            self.fc.fd["task_group"].click_delete_task_button()
            time.sleep(2)
            if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
                self.fc.fd["task_group"].click_delete_pop_window_continue_button()

        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        self.fc.fd["task_group"].click_windows_explorer_on_taskbar()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)

        self.fc.fd["task_group"].input_short_key_name("HPX1")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["task_group"].click_shortkey_dropdown()
        time.sleep(2)
        self.fc.fd["task_group"].select_shortkey_alt12()
        time.sleep(2)
        self.fc.fd["task_group"].click_edit_task_group_save_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show(), "Explorer icon is not displayed in task group list"
        time.sleep(2)
        self.fc.fd["task_group"].click_task_arrow_icon()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()


    @pytest.mark.function
    def test_06_save_group_name_and_ctrl12_C60184441(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_task_arrow_icon_show():
            time.sleep(2)
            self.fc.fd["task_group"].click_task_arrow_icon()
            time.sleep(2)
            self.fc.fd["task_group"].click_delete_task_button()
            time.sleep(2)
            if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
                self.fc.fd["task_group"].click_delete_pop_window_continue_button()

        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        self.fc.fd["task_group"].click_windows_explorer_on_taskbar()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)

        self.fc.fd["task_group"].input_short_key_name("HPX1")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["task_group"].click_shortkey_dropdown()
        time.sleep(2)
        self.fc.fd["task_group"].select_shortkey_ctrl12()
        time.sleep(2)
        self.fc.fd["task_group"].click_edit_task_group_save_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show(), "Explorer icon is not displayed in task group list"
        time.sleep(2)
        self.fc.fd["task_group"].click_task_arrow_icon()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()
    

    @pytest.mark.function
    def test_07_capture_the_task_using_create_new_button_C60184442(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_task_arrow_icon_show():
            time.sleep(2)
            self.fc.fd["task_group"].click_task_arrow_icon()
            time.sleep(2)
            self.fc.fd["task_group"].click_delete_task_button()
            time.sleep(2)
            if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
                self.fc.fd["task_group"].click_delete_pop_window_continue_button()

        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        self.fc.fd["task_group"].click_windows_explorer_on_taskbar()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)

        assert self.fc.fd["task_group"].verify_delete_task_button_show(), "Delete task button is not displayed"
    

    @pytest.mark.function
    def test_08_capture_a_task_without_any_apps_opened_C60184455(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.close_windows_explorer_app()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group creaate new button is not displayed"
    

    @pytest.mark.function
    def test_09_capture_admin_apps_C60184458(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group creaate new button is not displayed"

        time.sleep(2)
        self.fc.open_windows_terminal()
        time.sleep(2)
        self.fc.fd["task_group"].input_short_key_name("terminal1")
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["task_group"].click_shortkey_dropdown()
        time.sleep(2)
        self.fc.fd["task_group"].select_shortkey_shift12()
        time.sleep(2)
        self.fc.fd["task_group"].click_edit_task_group_save_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_terminal_icon_show(), "Terminal icon is not displayed in task group list"
        time.sleep(2)
        self.fc.fd["task_group"].click_task_arrow_terminal_icon()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()
        time.sleep(2)
        self.fc.close_windows_terminal()

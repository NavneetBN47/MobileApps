import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Task_Group_02(object):


    @pytest.mark.function
    def test_01_verify_user_concent_dialogue_C60176374(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_privacy_pop_window_title_show(), "Task group privacy pop up window title is not displayed"
        assert self.fc.fd["task_group"].verify_privacy_pop_window_desc_show(), "Task group privacy pop up window description is not displayed"
        assert self.fc.fd["task_group"].verify_privacy_pop_window_decline_button_show(), "Task group privacy pop up window decline button is not displayed"
        assert self.fc.fd["task_group"].verify_privacy_pop_window_agree_button_show(), "Task group privacy pop up window agree button is not displayed"


    @pytest.mark.function
    def test_02_unassign_shortkey_from_task_C60176407(self):
        self.fc.restart_myHP()
        time.sleep(2)
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
        self.fc.fd["task_group"].click_edit_task_group_save_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_edit_task_group_save_button_show(), "A task should not save without a short cut key assigned"

    @pytest.mark.function
    def test_03_delete_complete_task_group_C60184443(self):
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

        assert self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show(), "Delete pop window checkbox is not displayed"
        assert self.fc.fd["task_group"].verify_delete_pop_window_continue_button_show(), "Delete pop window continue button is not displayed"
        assert self.fc.fd["task_group"].verify_delete_pop_window_cancel_button_show(), "Delete pop window cancel button is not displayed"
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_pop_window_continue_button()

        time.sleep(2)

        self.fc.fd["task_group"].click_task_group_create_new_button()
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

        assert self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show(), "Delete pop window checkbox is not displayed"
        time.sleep(2)
        self.fc.fd["task_group"].select_delete_pop_window_checkbox()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_pop_window_continue_button()
        time.sleep(2)

        self.fc.fd["task_group"].click_task_group_create_new_button()
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
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show() is False, "Delete pop window checkbox is displayed"
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show() is False, "Task group item is still displayed after deletion"


    @pytest.mark.function
    def test_04_delete_app_from_task_group_C60184444(self):
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
        self.fc.fd["task_group"].click_windows_ms_store_on_taskbar()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_ms_store_delete_icon_show(), "Microsoft store icon is not displayed in task group capture window"
        time.sleep(2)
        self.fc.fd["task_group"].click_ms_store_delete_icon()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_delete_pop_window_continue_button_show() is False, "Delete pop window continue button is still displayed after deleting Microsoft store app"
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_ms_store_delete_icon_show() is False, "Microsoft store icon is still displayed in task group capture window"
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show(), "Delete pop window checkbox is not displayed"
    

    @pytest.mark.function
    def test_05_re_capture_task_group_C60184445(self):
        time.sleep(2)
        self.fc.close_msstore_app()
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
        
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
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
    def test_06_re_capture_task_group_after_delete_open_app_C60184452(self):
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
        self.fc.close_windows_explorer_app()
        time.sleep(6)
        self.fc.fd["task_group"].click_task_group_create_new_button_with_app()
        time.sleep(2)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)

        assert self.fc.fd["task_group"].verify_edit_task_group_save_button_show() is False, "Save button is displayed even after re-capturing no application on desktop"

        time.sleep(2)
        self.fc.fd["task_group"].click_task_arrow_icon()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()

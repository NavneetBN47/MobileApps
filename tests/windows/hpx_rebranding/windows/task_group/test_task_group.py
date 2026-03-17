import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Task_Group(object):

    @pytest.mark.function
    def test_01_verify_task_group_navigation_C60176284(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group creaate new button is not displayed"
        time.sleep(2)
        for _ in range(3):
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(2)
            if self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page():
                break
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        time.sleep(2)
        for _ in range(3):
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(2)
            if self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page():
                break
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group creaate new button is not displayed"

    
    @pytest.mark.function
    def test_02_verify_task_group_UI_visibility_C60176373(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_title_show(), "Task group title is not displayed"
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_description_show(), "Task group description is not displayed" 
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group creaate new button is not displayed"
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_video_container_show(), "Task group video container is not displayed"

    @pytest.mark.function
    def test_03_capture_dialogue_box_C60176375(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        if self.fc.fd["task_group"].verify_privacy_pop_window_agree_button_show():
            self.fc.fd["task_group"].click_privacy_pop_window_agree_button()
        time.sleep(5)
        capture_your_group_text = self.driver.get_text_by_coordinates(x_offset=959, y_offset=501)
        edit_layout_instruction_text = self.driver.get_text_by_coordinates(x_offset=959, y_offset=565)
        capture_text = self.driver.get_text_by_coordinates(x_offset=959, y_offset=635)
        cancel_text = self.driver.get_text_by_coordinates(x_offset=959, y_offset=692)
        assert capture_your_group_text == "Capture Your Group", f"Unexpected label at (959, 501): '{capture_your_group_text}'"
        assert "Edit your layout" in edit_layout_instruction_text, f"Unexpected label at (959, 565): '{edit_layout_instruction_text}'"
        assert capture_text == "Capture", f"Unexpected label at (959, 635): '{capture_text}'"
        assert cancel_text == "Cancel", f"Unexpected label at (959, 692): '{cancel_text}'"
        time.sleep(2)
        logging.info("Clicking cancel button.")
        self.driver.click_by_coordinates(x=959, y=692)
        logging.info("Cancel button click complete.")
        time.sleep(5)
        self.fc.fd["task_group"].click_task_group_create_new_button()
        time.sleep(5)
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
    

    @pytest.mark.function
    def test_04_ui_first_page_after_a_task_group_C60176376(self):
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
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()
    

    @pytest.mark.function
    def test_05_assign_a_duplicate_shortcut_key_C60176405(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
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

        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["task_group"].click_shortkey_dropdown()
        time.sleep(2)
        self.fc.fd["task_group"].select_shortkey_shift12()
        time.sleep(2)
        self.fc.fd["task_group"].click_edit_task_group_save_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show() is False, "Explorer icon is displayed in task group list with duplicate shortcut key"
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()
    

    @pytest.mark.function
    def test_06_verify_task_group_presist_across_application_restart_C60774367(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
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

        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
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
    def test_07_see_how_it_works_link_C60176398(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
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
        assert self.fc.fd["task_group"].verify_how_it_works_link_show(), "How it works link is not displayed in task group list"
        time.sleep(2)
        self.fc.fd["task_group"].click_how_it_works_link()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_how_to_use_task_group_title_show(), "How to use task group title is not displayed"
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_how_to_use_task_group_desc_show(), "How to use task group description is not displayed"
        time.sleep(2)
        self.fc.fd["task_group"].click_how_to_use_task_group_understand_button()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show(), "Explorer icon is not displayed in task group list"

        self.fc.fd["task_group"].click_task_arrow_icon()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["task_group"].click_delete_task_button()
        time.sleep(2)
        if self.fc.fd["task_group"].verify_delete_pop_window_checkbox_show():
            self.fc.fd["task_group"].click_delete_pop_window_continue_button()


    @pytest.mark.function
    @pytest.mark.consumer
    def test_08_launch_app_through_deeplink_C64138181(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        self.fc.launch_module_using_deeplink("hpx://pctaskgroups")
        time.sleep(10)
        assert self.fc.fd["task_group"].verify_task_group_title_show(), "Task group title is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    def test_09_capture_apps_which_are_minimized_to_task_bar_C60184460(self):
        time.sleep(2)
        self.fc.close_windows_explorer_app()
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        self.fc.fd["task_group"].click_windows_explorer_on_taskbar()
        time.sleep(2)
        self.fc.fd["task_group"].minimize_windows_explorer_on_taskbar()
        time.sleep(2)
        self.fc.launch_myHP()

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
        logging.info("Clicking capture button.")
        self.driver.click_by_coordinates(x=959, y=635)
        logging.info("Capture button click complete.")
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_arrow_icon_show() is False, "Explorer icon is displayed in task group list after capturing minimized app"

from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_HPPK_New_UI_03(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    def test_01_added_values_persistent_in_automation_C38499306(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        self.fc.fd["hppk"].click_automation_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_automation_radio_button_is_selected()))
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_enter_key("website_add")
        time.sleep(2)
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_delete_icon(), "delete button is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_action_content_box(), "website url is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_action_content_box_value(), "www.google.com", "website url is not visible")
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_key_sequence_radio_button_is_selected()),"Key sequence radio button is not selected")
        self.fc.fd["hppk"].click_key_sequence_input_box()
        self.fc.fd["hppk"].click_esc_key("key_sequence_input_box")
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_key_sequence_close_button()),"Close button is not visible")        
        self.fc.fd["hppk"].click_key_sequence_close_button()
        time.sleep(2)
        self.fc.fd["hppk"].click_automation_radio_btn()
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_delete_icon(), "delete button is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_action_content_box(), "website url is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_action_content_box_value(), "www.google.com", "website url is not visible")
        self.fc.fd["hppk"].click_delete_icon()
        time.sleep(2)
        soft_assertion.raise_assertion_errors()

    def test_02_added_values_persistent_in_text_input_C38499308(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        self.fc.fd["hppk"].click_text_input_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_text_input_radio_button_is_selected()),"Text input radio button is not selected")
        self.fc.fd["hppk"].enter_char_in_text_input("new message")
        self.fc.fd["hppk"].click_text_input_save_button()
        if bool(self.fc.fd["hppk"].verify_change_shortcut_modal_title()) == True:
            self.fc.fd["hppk"].click_continue_button_on_change_shortcut_pop_up()
            time.sleep(3)
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_textbox_text_value(), "new message", "new message text is not visible")
        self.fc.fd["hppk"].click_automation_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_automation_radio_button_is_selected()))
        time.sleep(2)
        self.fc.fd["hppk"].click_add_action()
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_application_text(), "Application", "Application text is not visible")
        self.fc.fd["hppk"].click_application()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_applications_header_visible()), "Verify Applications header is not visible")
        time.sleep(2)
        self.fc.fd["hppk"].click_cancel_app_button()
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        self.fc.fd["hppk"].click_text_input_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_text_input_radio_button_is_selected()),"Text input radio button is not selected")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_textbox_text_value(), "new message", "new message text is not visible")
        self.fc.fd["hppk"].enter_char_in_text_input("")
        soft_assertion.raise_assertion_errors()

    def test_03_added_values_persistent_in_key_sequence_C38499307(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_key_sequence_radio_button_is_selected()),"Key sequence radio button is not selected")
        self.fc.fd["hppk"].click_key_sequence_input_box()
        self.fc.fd["hppk"].click_esc_key("key_sequence_input_box")
        time.sleep(2)
        self.fc.fd["hppk"].click_key_sequence_save_button()
        if bool(self.fc.fd["hppk"].verify_change_shortcut_modal_title()) == True:
            self.fc.fd["hppk"].click_continue_button_on_change_shortcut_pop_up()
            time.sleep(3)
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_saved_text_key_sequence(), "Saved!", "Saved button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_textbox_text_value(),"Escape","Escape text is not visible")
        self.fc.fd["hppk"].click_automation_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_automation_radio_button_is_selected()))
        self.fc.fd["hppk"].click_add_action()
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_application_text(), "Application", "Application text is not visible")
        self.fc.fd["hppk"].click_application()
        time.sleep(2)
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_applications_header_visible()), "Verify Applications header is not visible")
        self.fc.fd["hppk"].click_cancel_app_button()
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_key_sequence_radio_button_is_selected()),"Key sequence radio button is not selected")
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_saved_text_key_sequence(), "Saved!", "Saved button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_textbox_text_value(),"Escape","Escape text is not visible")
        soft_assertion.raise_assertion_errors()

    def test_04_confirmation_alert_C38499309(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        self.fc.fd["hppk"].click_automation_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_automation_radio_button_is_selected()))
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_enter_key("website_add")
        time.sleep(2)
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_delete_icon(), "delete button is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_action_content_box(), "website url is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_action_content_box_value(), "www.google.com", "website url is not visible")

        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_key_sequence_radio_button_is_selected()),"Key sequence radio button is not selected")
        self.fc.fd["hppk"].click_key_sequence_input_box()
        self.fc.fd["hppk"].click_esc_key("key_sequence_input_box")
        time.sleep(2)
        self.fc.fd["hppk"].click_key_sequence_save_button()
        if bool(self.fc.fd["hppk"].verify_change_shortcut_modal_title()) == True:
            soft_assertion.assert_equal(self.fc.fd["hppk"].get_change_shortcut_modal_title(),"Change shortcut","Change shortcut title is not matching")
            desc_text = self.fc.fd["hppk"].get_change_shortcut_modal_subtitle()
            expected_desc_text = "You are about to change the assigned shortcut for this key. Doing so will erase any previous shortcuts you assigned. Do you wish to continue?"
            soft_assertion.assert_equal(desc_text, expected_desc_text,"Change shourtcut subtitle is not matching")
            soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_cancel_btn_modal_visible()),"Cancel button is not visible")
            soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_continue_btn_modal_visible()),"Continue button is not visible")
            self.fc.fd["hppk"].click_continue_button_on_change_shortcut_pop_up()
            time.sleep(3)
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_saved_text_key_sequence(), "Saved!", "Saved button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_textbox_text_value(),"Escape","Escape text is not visible")

        self.fc.fd["hppk"].click_text_input_radio_btn()
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_text_input_radio_button_is_selected()),"Text input radio button is not selected")
        self.fc.fd["hppk"].enter_char_in_text_input("new message")
        self.fc.fd["hppk"].click_text_input_save_button()
        if bool(self.fc.fd["hppk"].verify_change_shortcut_modal_title()) == True:
            soft_assertion.assert_equal(self.fc.fd["hppk"].get_change_shortcut_modal_title(),"Change shortcut","Change shourtcut title is not matching")
            desc_text = self.fc.fd["hppk"].get_change_shortcut_modal_subtitle()
            expected_desc_text = "You are about to change the assigned shortcut for this key. Doing so will erase any previous shortcuts you assigned. Do you wish to continue?"
            soft_assertion.assert_equal(desc_text, expected_desc_text,"Change shourtcut subtitle is not matching")
            soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_cancel_btn_modal_visible()),"Cancel button is not visible")
            soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_continue_btn_modal_visible()),"Continue button is not visible")
            self.fc.fd["hppk"].click_cancel_btn_modal()
            time.sleep(2)
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_text_input_radio_button_is_selected()),"Text input radio button is not selected")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_05_hppk_visible_in_home_page_C38499256(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        assert bool(self.fc.fd["home"].verify_home_module_show_on_global_navigation_panel()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_devices_menu_navigation()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_support_menu_navigation()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_settings_menu_navigation()) is True
        assert bool(self.fc.fd["home"].verify_Programmable_Key_card_visible()) is True

    def test_06_launch_hppk_via_deeplink_C49014495(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://progkey")
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_prog_key_nav_text(), "Programmable key", "Programmable Key text is not visible")
        soft_assertion.raise_assertion_errors()

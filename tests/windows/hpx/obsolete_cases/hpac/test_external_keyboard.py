from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()
        
    
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_verify_keyboard_ui_C33294673(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        assert self.fc.fd["external_keyboard"].get_title_text() == "Keyboard"
        time.sleep(2)
        self.fc.fd["external_keyboard"].click_title()
        assert self.fc.fd["external_keyboard"].get_title_tooltips_text() == "Keyboard"
        assert bool(self.fc.fd["external_keyboard"].verify_battery_icon_show()) is True
        assert self.fc.fd["external_keyboard"].get_keyboard_des_text() == "HP 970/975 Series Keyboard"
        assert bool(self.fc.fd["external_keyboard"].verify_info_icon_show()) is True
        assert self.fc.fd["external_keyboard"].get_lighting_setup_text() == "Lighting setup"
        assert self.fc.fd["external_keyboard"].get_proximity_sensor_text() == "Proximity sensor"
        assert self.fc.fd["external_keyboard"].get_backlight_auto_adjust_text() == "Backlight auto adjust"
        assert self.fc.fd["external_keyboard"].get_restore_button_text() == "Restore defaults"
    
    
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_header_info_C33312251(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        self.fc.fd["external_keyboard"].click_info_icon()
        time.sleep(2)
        assert bool(self.fc.fd["external_keyboard"].verify_production_number_show()) is True
        assert bool(self.fc.fd["external_keyboard"].verify_serial_number_show()) is True
        assert bool(self.fc.fd["external_keyboard"].verify_firmware_version_show()) is True
        assert bool(self.fc.fd["external_keyboard"].verify_production_number_text_show()) is True
        assert bool(self.fc.fd["external_keyboard"].verify_serial_number_text_show()) is True
        assert bool(self.fc.fd["external_keyboard"].verify_firmware_version_text_show()) is True
        self.fc.fd["external_keyboard"].click_productnumber_copy_icon()
        expected_productnumber_tooltip_text = "Copied"
        actual_productnumber_tooltip_text = self.fc.fd["external_keyboard"].get_productnumber_copy_text()
        assert actual_productnumber_tooltip_text == expected_productnumber_tooltip_text
        self.fc.fd["external_keyboard"].click_serialnumber_copy_icon()
        expected_serialnumber_tooltip_text = "Copied"
        actual_serialnumber_tooltip_text = self.fc.fd["external_keyboard"].get_serialnumber_copy_text()
        assert actual_serialnumber_tooltip_text == expected_serialnumber_tooltip_text
    

    
    def test_03_create_custom_device_name_C33336732(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        self.fc.fd["external_keyboard"].click_rename_icon()
        time.sleep(2)
        self.fc.fd["external_keyboard"].enter_device_name("HPXKeyboard")
        time.sleep(2)
        assert self.fc.fd["external_keyboard"].get_title_text() == "HPXKeyboard"

        self.fc.fd["external_keyboard"].click_rename_icon()
        time.sleep(2)
        self.fc.fd["external_keyboard"].enter_device_name("Keyboard")
        time.sleep(2)

        assert self.fc.fd["external_keyboard"].get_title_text() == "Keyboard"

        
    def test_04_create_long_string_custom_device_name_C33336739(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        self.fc.fd["external_keyboard"].click_rename_icon()
        self.fc.fd["external_keyboard"].enter_device_name("1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr")
        time.sleep(2)
        assert self.fc.fd["external_keyboard"].get_title_text() == "1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr"
        time.sleep(2)

        self.fc.fd["external_keyboard"].click_rename_icon()
        self.fc.fd["external_keyboard"].enter_device_name("Keyboard")
        time.sleep(2)

        assert self.fc.fd["external_keyboard"].get_title_text() == "Keyboard"
    

    @pytest.mark.require_sanity_check(["sanity"])
    def test_05_verify_toggle_status_C36590430(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        time.sleep(2)
        self.fc.fd["external_keyboard"].click_restore_button()
        time.sleep(2)

        assert self.fc.fd["external_keyboard"].verify_proximity_sensor_btn_status() == "1"
        time.sleep(2)
        self.fc.fd["external_keyboard"].click_proximity_sensor_btn()
        assert self.fc.fd["external_keyboard"].verify_proximity_sensor_btn_status() == "0"
        time.sleep(2)

        assert self.fc.fd["external_keyboard"].verify_backlight_adjust_btn_status() == "0"
        time.sleep(2)
        self.fc.fd["external_keyboard"].click_backlight_adjust_btn()

        assert self.fc.fd["external_keyboard"].verify_backlight_adjust_btn_status() == "1"
        time.sleep(2)
        self.fc.fd["external_keyboard"].click_proximity_sensor_btn()

    
    def test_06_verify_lighting_setup_tooltips_C33312351(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        self.fc.fd["external_keyboard"].click_proximity_sensor_tootips_btn()
        assert self.fc.fd["external_keyboard"].verify_proximity_sensor_tootips_message1() == "What is Smart Sensor"
        assert self.fc.fd["external_keyboard"].verify_proximity_sensor_tootips_message2() == "Detects when you are near your keyboard to turn on the backlight."
        time.sleep(2)
        self.fc.fd["external_keyboard"].close_proximity_sensor_tootips()

        time.sleep(2)
        self.fc.fd["external_keyboard"].click_backlight_adjust_tooltips_btn()
        self.fc.fd["external_keyboard"].click_backlight_adjust_tooltips_btn()
        assert self.fc.fd["external_keyboard"].verify_backlight_adjust_tooltips_message1() == "Backlight Auto Adjustment"
        assert self.fc.fd["external_keyboard"].verify_backlight_adjust_tooltips_message2() == "Automatically adjusts keyboard backlight based on ambient lighting."
    

    @pytest.mark.require_sanity_check(["sanity"])
    def test_07_verify_restore_button_works_C33312354(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()


        if self.fc.fd["external_keyboard"].verify_proximity_sensor_btn_status() != "1":
            self.fc.fd["external_keyboard"].click_proximity_sensor_btn()
        
        if self.fc.fd["external_keyboard"].verify_backlight_adjust_btn_status() != "0":
            self.fc.fd["external_keyboard"].click_backlight_adjust_btn()

        time.sleep(2)
        self.fc.fd["external_keyboard"].set_time_slider_value_increase(100,"time_slider")
        self.fc.fd["external_keyboard"].set_brightness_slider_value_decrease(50,"brightness_slider")

        time.sleep(2)
        assert self.fc.fd["external_keyboard"].get_time_slider_value() == "100"
        assert self.fc.fd["external_keyboard"].get_brightness_slider_value() == "50"

        time.sleep(2)
        self.fc.fd["external_keyboard"].click_restore_button()

        time.sleep(2)
        assert self.fc.fd["external_keyboard"].verify_proximity_sensor_btn_status() == "1"
        assert self.fc.fd["external_keyboard"].verify_backlight_adjust_btn_status() == "0"
        assert self.fc.fd["external_keyboard"].get_time_slider_value() == "15"
        assert self.fc.fd["external_keyboard"].get_brightness_slider_value() == "100"
    

    @pytest.mark.require_sanity_check(["sanity"])
    def test_08_verify_settings_remembered_C36591348(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()

        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        time.sleep(2)
        self.fc.fd["external_keyboard"].click_restore_button()
        self.fc.fd["external_keyboard"].click_proximity_sensor_btn()
        time.sleep(2)
        self.fc.fd["external_keyboard"].set_time_slider_value_increase(100,"time_slider")

        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        settings_header  = self.fc.fd["settings"].verify_settings_header()
        assert settings_header == "Settings"

        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        self.fc.fd["external_keyboard"].verify_keyboard_module_show()

        assert self.fc.fd["external_keyboard"].verify_proximity_sensor_btn_status() == "0"
        assert self.fc.fd["external_keyboard"].get_time_slider_value() == "100"


    def test_09_kb_two_click_and_hover_on_Function_key_verify_the_new_ui_default_toggle_and_tips_C36589784(self):
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        self.fc.fd["external_keyboard"].click_restore_button()
        #click on fn key
        self.fc.fd["external_keyboard"].click_fn_key()
        assert "0"==self.fc.fd["external_keyboard"].get_function_key_lock_on_start_toggle_status()
        assert "0"==self.fc.fd["external_keyboard"].get_function_key_lock_toggle_status()
        time.sleep(3)
        #fn_key
        fn_key_text=self.fc.fd["external_keyboard"].get_fn_key_text()
        assert fn_key_text=="Fn Key","Fn Key is not visible at function key side bar - {}".format(fn_key_text)
        #fn_key tooltip
        self.fc.fd["external_keyboard"].click_fn_key_tooltip_icon()
        fn_tooltip_text=self.fc.fd["external_keyboard"].get_fn_key_tooltip_text()
        assert "Use the control below" in fn_tooltip_text,"function_key_tooltip_text is not visible - {}".format(fn_tooltip_text)
        self.fc.fd["external_keyboard"].click_fn_key_tooltip_icon()
        #Function lock on start
        function_lock_on_start_text=self.fc.fd["external_keyboard"].get_function_lock_on_start()
        assert function_lock_on_start_text=="Function Lock On Start","Function Lock On Start is not visible at function key side bar - {}".format(function_lock_on_start_text)
        #Function lock on start tooltip
        self.fc.fd["external_keyboard"].click_function_lock_on_start_tooltip_icon()
        function_lock_start_tooltip_text=self.fc.fd["external_keyboard"].get_function_lock_on_start_tooltip_icon()
        assert "Set the state of the function" in function_lock_start_tooltip_text,"function key lock on start tooltip_text is not visible - {}".format(function_lock_start_tooltip_text)      
        self.fc.fd["external_keyboard"].click_function_lock_on_start_tooltip_icon()
        #Function lock
        function_lock_text=self.fc.fd["external_keyboard"].get_function_lock()
        assert function_lock_text=="Function Lock","Function Lock is not visible at function key side bar - {}".format(function_lock_text)
        #Function lock tooltip
        self.fc.fd["external_keyboard"].click_function_lock_tooltip_icon()
        function_lock_tooltip_text=self.fc.fd["external_keyboard"].get_function_lock_tooltip_icon()
        assert "The current state of the function key" in function_lock_tooltip_text,"function key lock text is not visible - {}".format(function_lock_tooltip_text)
        self.fc.fd["external_keyboard"].click_function_lock_tooltip_icon()
        self.fc.fd["external_keyboard"].click_restore_button()
    
    def test_10_use_search_function_verify_it_can_work_well_C39049791(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        assert self.fc.fd["external_keyboard"].verify_keyboard_module_show() is True
        self.fc.fd["external_keyboard"].click_mute_key_to_open_side_panel()
        assert self.fc.fd["external_keyboard"].verify_search_txt_box() is True
        assert self.fc.fd["external_keyboard"].verify_productivity_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_copy_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_cut_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_paste_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_undo_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_redo_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_more_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_media_control_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_app_and_file_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_open_file_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_file_save_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_open_folder_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_documents_text_on_side_panel() is True
        self.fc.fd["external_keyboard"].enter_text_in_search_box("1")
        assert self.fc.fd["external_keyboard"].verify_keyboard_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_key_f1_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_key_f10_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_key_f11_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_key_f12_text_on_side_panel() is True
        self.fc.fd["external_keyboard"].enter_text_in_search_box("12")
        assert self.fc.fd["external_keyboard"].verify_keyboard_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_key_f12_text_on_side_panel() is True
        self.fc.fd["external_keyboard"].enter_text_in_search_box("der")
        assert self.fc.fd["external_keyboard"].verify_app_and_file_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_open_folder_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_download_folder_text_on_side_panel() is True
        self.fc.fd["external_keyboard"].enter_text_in_search_box("43")
        assert self.fc.fd["external_keyboard"].verify_Cannot_find_the_action_txt() is True
        self.fc.fd["external_keyboard"].enter_text_in_search_box("d")
        self.fc.fd["external_keyboard"].click_x_on_search_txt_box()
        assert self.fc.fd["external_keyboard"].verify_search_txt_box() is True
        assert self.fc.fd["external_keyboard"].verify_productivity_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_copy_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_cut_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_paste_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_undo_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_redo_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_more_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_media_control_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_app_and_file_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_open_file_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_file_save_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_open_folder_text_on_side_panel() is True
        assert self.fc.fd["external_keyboard"].verify_documents_text_on_side_panel() is True

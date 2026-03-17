from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time 

pytest.app_info = "HPX"

class Test_Suite_Pen_Control(object):
    
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)

    
    def test_02_pen_control_ui_C32194630(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        assert self.fc.fd["pen_control"].get_single_press_text() == "Single Press"
        assert self.fc.fd["pen_control"].get_double_press_text() == "Double Press"
        assert self.fc.fd["pen_control"].get_long_press_text() == "Long Press"
        assert self.fc.fd["pen_control"].get_upper_barrel_text() == "Upper Barrel Button"
        assert self.fc.fd["pen_control"].get_lower_barrel_text() == "Lower Barrel Button"

        assert bool(self.fc.fd["pen_control"].verify_resotre_button_show()) is True

    def test_03_pen_control_header_info_C32194634(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        assert bool(self.fc.fd["pen_control"].verify_product_number_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_serial_number_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_battery_title_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_connection_title_show()) is True
        assert self.fc.fd["pen_control"].get_connection_status() == "Connected"
        assert self.fc.fd["pen_control"].get_product_number_value() == "16402"
        assert self.fc.fd["pen_control"].get_serial_number_value() == "401334"
    
    def test_04_verify_upper_barrel_button_C32194644(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        self.fc.fd["pen_control"].click_upper_barrel_dropdown()
        assert bool(self.fc.fd["pen_control"].verify_go_forward_show()) is True
    
    def test_05_verify_upper_barrel_dorpdownlist_C32194645(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        self.fc.fd["pen_control"].click_upper_barrel_dropdown()
        assert bool(self.fc.fd["pen_control"].verify_go_forward_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_touch_on_off_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_erase_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_right_click_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_page_up_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_paste_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_undo_show()) is True
    
    def test_06_verify_lower_barrel_button_C32194648(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        self.fc.fd["pen_control"].click_lower_barrel_dropdown()
        assert bool(self.fc.fd["pen_control"].verify_go_forward_show()) is True
    
    def test_07_verify_upper_barrel_dorpdownlist_C32194649(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        self.fc.fd["pen_control"].click_lower_barrel_dropdown()
        assert bool(self.fc.fd["pen_control"].verify_go_forward_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_touch_on_off_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_erase_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_right_click_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_page_up_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_paste_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_undo_show()) is True

    def test_08_verify_pen_pressure_sensitivity_C32194655(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=2)

        
        assert bool(self.fc.fd["pen_control"].verify_pen_sensitivity_title_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_pressure_title_title_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_pressure_slider_show()) is True
    
    def test_09_verify_pen_pressure_sensitivity_slider_C32194656(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=2)

        
        assert self.fc.fd["pen_control"].get_pressure_slider_value() == "Pressure Sensitivity 50 percent"

        time.sleep(2)
        self.fc.fd["pen_control"].increase_pressure_slider_value(100, "pressure_slider")
        assert self.fc.fd["pen_control"].get_pressure_slider_value() == "Pressure Sensitivity 100 percent"
        
        time.sleep(2)
        self.fc.fd["pen_control"].decrease_pressure_slider_value(100, "pressure_slider")
        assert self.fc.fd["pen_control"].get_pressure_slider_value() == "Pressure Sensitivity 0 percent"
    
    def test_10_verify_pen_pressure_sensitivity_C32194657(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=2)

        
        assert bool(self.fc.fd["pen_control"].verify_tilt_title_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_pressure_title_title_show()) is True
        assert bool(self.fc.fd["pen_control"].verify_tilt_slider_show()) is True

    def test_11_verify_pen_tile_sensitivity_slider_C32194658(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=2)

        
        assert self.fc.fd["pen_control"].get_tilt_slider_value() == "Pressure Sensitivity 50 percent"

        time.sleep(2)
        self.fc.fd["pen_control"].increase_tilt_slider_value(100, "pressure_slider")
        assert self.fc.fd["pen_control"].get_pressure_slider_value() == "Pressure Sensitivity 100 percent"
        
        time.sleep(2)
        self.fc.fd["pen_control"].decrease_tilt_slider_value(100, "pressure_slider")
        assert self.fc.fd["pen_control"].get_pressure_slider_value() == "Pressure Sensitivity 0 percent"
    
    def test_12_verify_restore_button_C32194659(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=2)

        assert bool(self.fc.fd["pen_control"].verify_right_click_show()) is True
        self.fc.fd["pen_control"].click_lower_barrel_dropdown()
        self.fc.fd["pen_control"].click_go_forward()
        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_right_click_show()) is False

        self.fc.fd["pen_control"].click_restore_button()
        assert bool(self.fc.fd["pen_control"].verify_right_click_show()) is True

    def test_13_verify_upper_barrel_button_hover_click_toggle_switch_C32194647(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        time.sleep(2)
        self.fc.fd["pen_control"].verify_upper_barrel_button_hover_toggle_off() == True
        self.fc.fd["pen_control"].click_upper_barrel_button_hover_toggle_off()
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_button_hover_toggle_on()) is True 

        time.sleep(2)
        self.fc.fd["pen_control"].click_upper_barrel_dropdown()
        assert bool(self.fc.fd["pen_control"].verify_erase_show()) is True

        time.sleep(5)
        self.fc.fd["pen_control"].click_upper_barrel_button_hover_toggle_on()
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_button_hover_toggle_off()) is True 
        self.driver.swipe(direction="down", distance=2)
        time.sleep(3)
        self.fc.fd["pen_control"].click_restore_button()

    def test_14_verify_lower_barrel_button_hover_click_toggle_switch_C32194651(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        self.driver.swipe(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["pen_control"].verify_lower_barrel_button_hover_toggle_off() is True
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_off()
        assert bool(self.fc.fd["pen_control"].verify_lower_barrel_button_hover_toggle_on()) is True 

        time.sleep(3)
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_on()
        assert bool(self.fc.fd["pen_control"].verify_lower_barrel_button_hover_toggle_off()) is True
        time.sleep(2)
        self.fc.fd["pen_control"].click_restore_button()

    def test_15_verify_pen_control_header_new_information_C33733310(self):
        time.sleep(3)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_default_pen_name()) is True
        assert bool(self.fc.fd["pen_control"].verify_edit_button()) is True
        assert bool(self.fc.fd["pen_control"].verify_bluetooth_status()) is True
        assert bool(self.fc.fd["pen_control"].verify_info_icon()) is True

    def test_16_verify_app_crash_multiple_time_app_launch_C32594246(self):
        for _ in range(10):
            print("Launch the My HPX app")
            self.fc.restart_app()
            time.sleep(5)
       
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(3)
        self.fc.fd["pen_control"].click_upper_barrel_button_hover_toggle_off()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=2)
        time.sleep(2)
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_off()

        for _ in range(10):
            print("Launch the My HPX app")
            self.fc.restart_app()
            time.sleep(5)

        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(3)
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_button_hover_toggle_on()) is True 
        time.sleep(2)
        self.driver.swipe(direction="down", distance=2)
        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_lower_barrel_button_hover_toggle_on()) is True 

    def test_20_reset_to_default_settings_C32194660(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.maximize_window()
        self.driver.swipe(direction="down", distance=3)
        time.sleep(5)

        #RESTORE DEFAULTS

        assert bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()) is True
        time.sleep(3)
        self.fc.fd["pen_control"].click_restore_defaults_btn() 
        time.sleep(3)

        #TOP BUTTON

        self.driver.swipe(direction="up", distance=3)
        assert self.fc.fd["pen_control"].get_single_press_text() == "Single Press"
        assert self.fc.fd["pen_control"].get_single_press_default_text() == "MS whiteboard"

        assert self.fc.fd["pen_control"].get_double_press_text() == "Double Press"
        assert self.fc.fd["pen_control"].get_double_press_default_text() == "Screen snipping"
        
        assert self.fc.fd["pen_control"].get_long_press_text() == "Long Press"
        assert self.fc.fd["pen_control"].get_long_press_default_text() == "Cortana"

        #UPPER BARREL BUTTON

        assert self.fc.fd["pen_control"].get_upper_barrel_text() == "Upper Barrel Button"
        assert self.fc.fd["pen_control"].get_upper_barrel_btn_default_text() == "Right click"
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_button_hover_toggle_off()) is True

        self.driver.swipe(direction="down", distance=3)

        #LOWER BARREL BUTTON

        assert self.fc.fd["pen_control"].get_lower_barrel_text() == "Lower Barrel Button"
        assert self.fc.fd["pen_control"].get_lower_barrel_btn_default_text() == "Erase"
        assert bool(self.fc.fd["pen_control"].verify_lower_barrel_button_hover_toggle_off()) is True 

        #PEN SENSITIVITY

        self.driver.swipe(direction="down", distance=2)
        assert bool(self.fc.fd["pen_control"].verify_pressure_title_title_show()) is True
        assert self.fc.fd["pen_control"].get_pressure_slider_default_text() == "Pressure Sensitivity"

        assert bool(self.fc.fd["pen_control"].verify_tilt_title_show()) is True
        assert self.fc.fd["pen_control"].get_tilt_slider_default_text() == "Tilt Sensitivity"

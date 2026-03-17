from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Trio_Pen_Control_Commercial(object):
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
            cls.fc.close_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_verify_upper_barrel_button_text_C42215544(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_defaults_btn()
        time.sleep(5)
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        actual_upper_barrel_text = self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial()
        actual_upper_barrel_text == "Universal Select", "Universal Select text Mismatch"
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        assert self.fc.fd["pen_control"].verify_upper_barrel_button_text_show_commercial() == "Upper barrel button", "Upper barrel button text Mismatch"
        assert self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial() == actual_upper_barrel_text, "Universal Select text Mismatch"
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_click_and_verify_lower_barrel_button_text_C42215548(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        actual_lower_barrel_button_text = self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        actual_lower_barrel_button_text == "Erase", "Erase text Mismatch"
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower barrel button text Mismatch"
        assert self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial() == actual_lower_barrel_button_text, "Erase text Mismatch"
        assert self.fc.fd["pen_control"].get_erase_toggle_is_select_commercial() == "1", "Erase toggle is not selected"
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_pen_sensitivity_menu_visible_C42215555(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_tilt_sensitivity_slider_C42215559(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        time.sleep(3)
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_sensivity_slider_visible(), "Pen sensitivity slider is not visible")       
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "1", "Pen sensitivity slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_increase(1,"tilt_sensitivity_slider")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "2", "Pen sensitivity max slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_decrease(2,"tilt_sensitivity_slider")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "0", "Pen sensitivity min slider value is not correct")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_tilt_sensitivity_slider_values_C42215558(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_sensivity_slider_visible(), "Pen sensivity slider is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "1", "Pen sensitivity slider value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_max_value("tilt_sensitivity_slider"), "2", "Pen sensitivity max slider value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_min_value("tilt_sensitivity_slider"), "0", "Pen sensitivity min slider value is not correct")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_tip_pressure_slider_values_C42215556(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pressure_title_text(), "Pressure", "Pressure title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_tip_pressure_slider_visible(), "Pen tilt pressure slider is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "3", "Pen tip pressure slider value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_max_value("tip_pressure_slider"), "6", "Pen tip pressure slider max value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_min_value("tip_pressure_slider"), "0", "Pen tip pressure slider min value is not correct")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_pressure_tip_slider_dragdrop_C42215557(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pressure_title_text(), "Pressure", "Pressure title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_tip_pressure_slider_visible(), "Pen tip pressure slider is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "3", "Pen tip pressure slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_increase(1,"tip_pressure_slider")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "4", "Pen tip pressure max slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_decrease(2,"tip_pressure_slider")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "2", "Pen tip pressure min slider value is not correct")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_restore_default_button_hide_show_C42215560(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        pen_lower_barrel_text = self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        pen_upper_barrel_text = self.fc.fd["pen_control"].get_right_click_consumer_btn_pen()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(pen_lower_barrel_text, "Erase", "Lower barrel button default setting is not visible")
        soft_assertion.assert_equal(pen_upper_barrel_text, "Universal Select", "Upper barrel button default setting is not visible")
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        if self.fc.fd["pen_control"].get_lower_barrel_btn() == "Lower barrel button":
            soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()), "Restore defaults button should not show")
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_action_list_not_show_commercial()), "Action list is not show")
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()), "Restore defaults button is not show")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_restore_button_default_settings_C42215561(self):
        time.sleep(5)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(2)
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_consumer_is_selected(), "1", "erase radio button is not selected")
        print(self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_consumer_is_selected())
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial(), "Erase", "Erase default value is not selected")
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial(),"Universal Select", "Universal Select default value is not visible")        
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_name_tooltips(), "HP 705 Rechargeable Multi Pen", "Pen name tooltip is not matching with default value")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_side_menu_navigation_pen_name(), "Pen", "Default pen name is not visible in side menu")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_10_upper_lower_barrel_hover_click_tooltip_desc_C42215562(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        actual_tooltip_desc = "Enable assigned button action while hovering pen tip over screen."
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_lower_barrel_tooltip()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_tool_tip(),actual_tooltip_desc,"Lower barrel tooltip description is not visible")
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_upper_barrel_tool_tip()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_tool_tip(),actual_tooltip_desc,"Lower barrel tooltip description is not visible")
        soft_assertion.raise_assertion_errors()

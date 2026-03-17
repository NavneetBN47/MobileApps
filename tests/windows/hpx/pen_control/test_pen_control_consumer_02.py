from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Pen_Control_Consumer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
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
            time.sleep(2)
            cls.fc.launch_myHP()
        time.sleep(5)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.ota
    def test_01_action_list_C38472742(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_btn_right_click(), "Upper barrel button", "upper barrel title is not visible")
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_upper_barrel_right_click_radio_button_is_selected()))
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_click_pen_consumer(), "Right-click", "Right-click defaul value is not visible")
        soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()))

        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_btn(),"Lower barrel button", "Lower barrel button title is not visible")
        soft_assertion.assert_equal((self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_is_selected()),"1", "Lower barrel erase radio button is not selected")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_text(), "Erase", "Erase defaul value is not selected")
        soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()))

        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_action_list_not_show_commercial()), "Action list should not show on commercial platform")
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()), "Restore Button is not visible")
        soft_assertion.raise_assertion_errors()

    def test_02_restore_default_button_C38494091(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        pen_lower_barrel_text = self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        pen_upper_barrel_text = self.fc.fd["pen_control"].get_right_click_consumer_btn_pen()
        soft_assertion.assert_equal(pen_lower_barrel_text, "Erase", "Lower barrel button default setting is not visible")
        soft_assertion.assert_equal(pen_upper_barrel_text, "Right-click", "Upper barrel button default setting is not visible")
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        if self.fc.fd["pen_control"].get_lower_barrel_btn() == "Lower barrel button":
            soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()), "Restore Button is visible")

        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_action_list_not_show_commercial()), "Action list should not show on commercial platform")
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()), "Restore Button is not visible")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_03_restore_button_default_settings_C38494092(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        pen_lower_barrel_text = self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        pen_upper_barrel_text = self.fc.fd["pen_control"].get_right_click_consumer_btn_pen()
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion.assert_equal((self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_is_selected()), "1", "Lower barrel erase radio button is not selected")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_text(), pen_lower_barrel_text, "Erase default value is not selected")

        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_upper_barrel_right_click_radio_button_is_selected()), "Upper barrel right click radio button is not selected")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_click_pen_consumer(), pen_upper_barrel_text, "Right-click default value is not visible")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_04_verify_consumer_default_UI_C38422106(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_battery_status(), "Battery status is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_edit_button(), "Edit button is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial(), "Upper barrel image button is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial(), "Lower barrel image button is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_restore_default_button(), "Restore button is not visible")
        soft_assertion.raise_assertion_errors()
    

    def test_05_navigation_bar_C38472564(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_side_menu_navigation_pen_name(), "Pen", "Default pen name text Mismatch")
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        soft_assertion.assert_true(self.fc.fd["navigation_panel"].verify_navigationicon_show())
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_default_pen_name(), "HP Digital Pen", "Pen name of changed text Mismatch")

        time.sleep(2)
        self.fc.fd["pen_control"].click_edit_button()
        time.sleep(2)
        self.fc.fd["pen_control"].change_pen_name_consumer("HP Pen Rename")

        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_default_pen_name(), "HP Pen Rename", "Pen name of changed text Mismatch")

        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_side_menu_navigation_pen_name(), "HP Pen Rename", "Pen name of changed text Mismatch")

        time.sleep(2)
        self.fc.fd["pen_control"].click_edit_button()
        time.sleep(2)
        self.fc.fd["pen_control"].change_pen_name_consumer("HP Digital Pen")
        time.sleep(2)
        assert self.fc.fd["pen_control"].get_default_pen_name() == "HP Digital Pen", "Default pen name text Mismatch"


    def test_06_launch_of_the_application_C38421998(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_side_menu_navigation_pen_name(), "Pen", "Default pen name is not visible in sidemenu")
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        soft_assertion.assert_true(self.fc.fd["navigation_panel"].verify_navigationicon_show(), "Navigation icon is not show")
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_default_pen_name(), "HP Digital Pen", "Default pen name text Mismatch")
    
    def test_07_proximity_icon_C42581918(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        assert self.fc.fd["pen_control"].verify_proximity_icon(), "Proximity icon is not visible"
        self.fc.fd["pen_control"].click_proximity_icon()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_proximity_icon_tooltip_text(), "Connection proximity", "Connection proximity icon text is not visible")

    @pytest.mark.ota
    def test_08_pen_control_header_information_C38430486(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(1)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_default_pen_name()) is True
        assert bool(self.fc.fd["pen_control"].verify_edit_button()) is True
        assert bool(self.fc.fd["pen_control"].verify_battery_status()) is True
        assert bool(self.fc.fd["pen_control"].verify_connection_proximity_show()) is True

    @pytest.mark.ota
    def test_09_pen_name_C38472562(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(1)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_default_pen_name()) is True
        time.sleep(2)
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_consumer() == "HP Digital Pen", "Default pen name text Mismatch"
        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_edit_button()) is True
        time.sleep(2)
        self.fc.fd["pen_control"].click_edit_button()
        time.sleep(2)
        self.fc.fd["pen_control"].change_pen_name_consumer("HP Pen Rename")
        time.sleep(2)
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_consumer() == "HP Pen Rename", "Pen name of changed text Mismatch"
        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_battery_status()) is True
        assert bool(self.fc.fd["pen_control"].verify_connection_proximity_show()) is True

    def test_10_launch_via_deeplink_C48980886(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://pencontrol")
        soft_assertion = SoftAssert()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_pen_is_selected_from_navbar()), "pen is not selected from navbar")
        soft_assertion.raise_assertion_errors()

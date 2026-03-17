from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_External_Mouse(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)


    def test_01_mouse_default_setting_C33328041(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        
        assert self.fc.fd["external_mouse"].get_middle_click_text() == "Middle click"
        assert self.fc.fd["external_mouse"].get_scroll_left_text() == "Scroll left"
        assert self.fc.fd["external_mouse"].get_right_click_text() == "Right click"
        assert self.fc.fd["external_mouse"].get_scroll_right_text() == "Scroll right"
        assert self.fc.fd["external_mouse"].get_forward_text() == "Forward"
        assert self.fc.fd["external_mouse"].get_task_view_text() == "Task view"
        assert self.fc.fd["external_mouse"].get_back_text() == "Back"

    
    def test_02_mouse_ui_verify_C33294674(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse"
        time.sleep(2)
        self.fc.fd["external_mouse"].click_title()
        assert self.fc.fd["external_mouse"].get_title_tooltips_text() == "Mouse"
        assert self.fc.fd["external_mouse"].get_middle_click_text() == "Middle click"
        assert self.fc.fd["external_mouse"].get_scroll_left_text() == "Scroll left"
        assert self.fc.fd["external_mouse"].get_right_click_text() == "Right click"
        assert self.fc.fd["external_mouse"].get_scroll_right_text() == "Scroll right"
        assert self.fc.fd["external_mouse"].get_forward_text() == "Forward"
        assert self.fc.fd["external_mouse"].get_task_view_text() == "Task view"
        assert self.fc.fd["external_mouse"].get_back_text() == "Back"
        assert self.fc.fd["external_mouse"].get_mouse_sensitivity_text() == "Mouse sensitivity"
        assert self.fc.fd["external_mouse"].get_restore_button_text() == "Restore defaults"
    

    def test_03_verift_mouse_header_C33322547(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse"
        time.sleep(2)
        self.fc.fd["external_mouse"].click_eidt_name_btn()
        self.fc.fd["external_mouse"].enter_device_name("Mouse123")
        time.sleep(2)
        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse123"
        assert bool(self.fc.fd["external_mouse"].verify_connect_status_icon_show()) is True

        time.sleep(2)
        self.fc.fd["external_mouse"].click_device_info_icon()
        time.sleep(2)

        assert self.fc.fd["external_mouse"].get_product_numer_title() == "Product Number"
        assert self.fc.fd["external_mouse"].get_serial_number_title() == "Serial Number"
        assert self.fc.fd["external_mouse"].get_firmware_version_title() == "Firmware Version"

        self.fc.fd["external_mouse"].click_eidt_name_btn()
        self.fc.fd["external_mouse"].enter_device_name("Mouse")
        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse"

    
    def test_04_change_device_name_C33336715(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        time.sleep(2)
        self.fc.fd["external_mouse"].click_eidt_name_btn()
        self.fc.fd["external_mouse"].enter_device_name("Mouse123$$%@$--_")
        time.sleep(2)
        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse123$$%@$--_"

        self.fc.fd["external_mouse"].click_eidt_name_btn()
        self.fc.fd["external_mouse"].enter_device_name("Mouse")
        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse"
    

    def test_05_verify_device_name_can_be_remembered_C33322753(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        time.sleep(2)
        self.fc.fd["external_mouse"].click_eidt_name_btn()
        self.fc.fd["external_mouse"].enter_device_name("Mouse123")
        time.sleep(2)
        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse123"

        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        settings_header  = self.fc.fd["settings"].verify_settings_header()
        assert settings_header == "Settings"

        self.fc.fd["navigation_panel"].navigate_external_mouse_module()
        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse123"

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        assert self.fc.fd["external_mouse"].get_title_text() == "Mouse123"
    

    def test_06_verify_sensitivity_default_value_C33328045(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        time.sleep(2)
        self.fc.fd["external_mouse"].click_sensitivity_button()
        time.sleep(2)
        assert self.fc.fd["external_mouse"].get_sensitivity_slider_value() == "1550"
    

    def test_07_change_sensitivity_default_value_C33328110(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        time.sleep(2)
        self.fc.fd["external_mouse"].click_sensitivity_button()
        time.sleep(2)
        if self.fc.fd["external_mouse"].get_sensitivity_slider_value() != "1550":
            self.fc.fd["external_mouse"].set_sensitivity_slider_value_increase(100, "mouse_sensitivity_slider")
            time.sleep(2)
            assert self.fc.fd["external_mouse"].get_sensitivity_slider_value() == "3000"
        else:
            self.fc.fd["external_mouse"].set_sensitivity_slider_value_decrease(100, "mouse_sensitivity_slider")
            assert self.fc.fd["external_mouse"].get_sensitivity_slider_value() == "800"

    
    def test_08_verify_sensitivity_default_value_can_be_remembered_C35970548(self):
        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_external_mouse_module()

        self.fc.fd["external_mouse"].verify_mouse_module_show()

        time.sleep(2)
        self.fc.fd["external_mouse"].click_restore_button()

        time.sleep(2)
        self.fc.fd["external_mouse"].click_sensitivity_button()
        time.sleep(2)
        self.fc.fd["external_mouse"].set_sensitivity_slider_value_increase(100, "mouse_sensitivity_slider")
        time.sleep(2)
        assert self.fc.fd["external_mouse"].get_sensitivity_slider_value() == "3000"

        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        settings_header  = self.fc.fd["settings"].verify_settings_header()
        assert settings_header == "Settings"

        self.fc.fd["navigation_panel"].navigate_external_mouse_module()
        self.fc.fd["external_mouse"].verify_mouse_module_show()
        self.fc.fd["external_mouse"].click_sensitivity_button()
        time.sleep(2)
        assert self.fc.fd["external_mouse"].get_sensitivity_slider_value() == "3000"

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].navigate_external_mouse_module()
        self.fc.fd["external_mouse"].verify_mouse_module_show()
        self.fc.fd["external_mouse"].click_sensitivity_button()
        time.sleep(2)
        assert self.fc.fd["external_mouse"].get_sensitivity_slider_value() == "3000"

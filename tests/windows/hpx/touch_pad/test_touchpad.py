from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging
#import wmi


pytest.app_info = "HPX"
class Test_Suite_touchpad(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        time.sleep(2)
        

    def test_01_verify_touchpad_module_card_C35876478(self):
        self.fc.restart_app()
        time.sleep(5)
        #check the hamberger menu is expanded or not.
        if self.fc.fd["navigation_panel"].verify_hamburger_menu_navigation() == 'Open Navigation':
            self.fc.fd["navigation_panel"].click_hamburger_navigation()
        #Open the hamburger menu.
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu() 
        time.sleep(5)
        #Check if the "Device" list arrow button open or close.
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        self.fc.fd["devices"].verify_touchpad_PCDevice_header() is True
        time.sleep(5)
        assert bool(self.fc.fd["devices"].verify_touchpad_PCDevice_header()) is True
        assert bool(self.fc.fd["devices"].verify_touchpad_PCDevice_header_text()) is True
        assert bool(self.fc.fd["devices"].verify_touchpad_PCDevice_header_description()) is True

    def test_02_verify_touchpad_card_text_C35876478(self):
        time.sleep(5)
        assert self.fc.fd["devices"].get_touchpad_PCDevice_header_text() == "Touchpad"
        assert self.fc.fd["devices"].get_touchpad_PCDevice_header_description() == "Enable gesture control"
        time.sleep(3)
        
    def test_03_verify_touchpad_UI_C35876478(self):
        #Click on the touchpad card and go into the touchpad page.
        self.fc.fd["devices"].verify_touchpad_PCDevice_header() is True
        self.fc.fd["devices"].click_touchpad_header()
        time.sleep(5)
        assert self.fc.fd["touchpad"].get_touchpad_header_text() == "Touchpad"
        assert self.fc.fd["touchpad"].get_touchpad_title_text() == "Enable gesture control"
        assert self.fc.fd["touchpad"].get_touchpad_brightness_text() == "Brightness"
        assert self.fc.fd["touchpad"].get_touchpad_volume_text() == "Volume"
        assert self.fc.fd["touchpad"].get_touchpad_win_setting_text() == "Adjust feedback intensity"
        self.fc.fd["touchpad"].hover_touchpad_tooltip()
        assert self.fc.fd["touchpad"].get_touchpad_tooltip_text() == "To adjust the settings, simply slide your finger up and down within the designated zones." 

    def test_04_verify_touchpad_UI_function_C35876478(self):
        time.sleep(5)
        #Default is off
        assert self.fc.fd["touchpad"].get_touchpad_enable_toggle_switch_status() == "0"
        self.fc.fd["touchpad"].click_touchpad_enable_toggle_switch()
        assert self.fc.fd["touchpad"].get_touchpad_enable_toggle_switch_status() == "1"
import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "HPX"

class Test_Suite_System_Control(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        time.sleep(5)
        cls.driver.swipe(direction="down", distance=3)
        if cls.fc.fd["hp_registration"].verify_skip_button_show():
            cls.fc.fd["hp_registration"].click_skip_button()
    

    @pytest.mark.consumer
    @pytest.mark.function
    def test_01_verify_myHP_app_module_sanity_C33694760(self):
        #Launch myHP application--Application launched
        #1.Click on the Hamburger menu.2.Verify all module are present---Menu is expanded.All tab are is visible.
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_welcome_module_show()) is True
        if (self.fc.fd["navigation_panel"].verify_hamburger_menu_navigation() == 'Open Navigation'):
            logging.info("Hamburger menu is not expanded")
            self.fc.fd["navigation_panel"].click_hamburger_navigation()
        else:
            logging.info("Hamburger menu is expanded")
        #home,device,support,setting menu present in left navigation panel
        assert bool(self.fc.fd["navigation_panel"].verify_welcome_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_pcdevice_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_navigate_PCdevice_module()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_support_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_setting_module_show()) is True

    @pytest.mark.consumer
    @pytest.mark.function
    def test_02_verify_system_control_card_C33694761(self):
        time.sleep(4)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        self.fc.fd["devices"].verify_system_control_card() is True
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(5)
        assert bool(self.fc.fd["system_control"].verify_system_control_title()) is True
        assert bool(self.fc.fd["system_control"].verify_system_control_subtitle()) is True

    @pytest.mark.consumer
    @pytest.mark.function
    def test_04_verify_system_control_consistency_C33694784(self):
        time.sleep(4)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(8)
        self.fc.fd["devices"].verify_system_control_card() is True
        self.fc.fd["devices"].click_system_control_card()
        time.sleep(5)
        assert bool(self.fc.fd["system_control"].verify_system_control_title()) is True
        for _ in range(10):
            self.fc.restart_app()
            time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(8)
        self.fc.fd["devices"].verify_system_control_card() is True
        self.fc.fd["devices"].click_system_control_card()
        assert bool(self.fc.fd["system_control"].verify_system_control_title()) is True
        for _ in range(10):
            self.fc.restart_app()
            time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(8)
        self.fc.fd["devices"].verify_system_control_card() is True
        self.fc.fd["devices"].click_system_control_card()
        assert bool(self.fc.fd["system_control"].verify_system_control_title()) is True
    
    @pytest.mark.consumer
    @pytest.mark.function
    def test_03_verify_test_get_or_set_calls_sanity_C33694765(self):
        #Launch HPX application and navigate to System Control Page from PC device.--HPX application is launched and successfully navigated to System Control page.
        time.sleep(5)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].verify_performance_control_title_consumer()) is True
        #Select any thermal settings(Ex: Cool--Thermal settings is selected(Ex: Cool)
        self.fc.fd["system_control"].click_cool_consumer()
        #Thermal settings is selected(Ex: Cool)
        assert bool(self.fc.fd["system_control"].verify_cool_mode_selected_consumer()) is True
        #Navigate to other module and come back to System Control.
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        #Same thermal setting should be selected when navigated back to system control
        assert bool(self.fc.fd["system_control"].verify_cool_mode_selected_consumer()) is True
        self.fc.close_app()
        time.sleep(5)
        self.fc.launch_app()
        time.sleep(5)
        #Same thermal setting should be selected when app is relaunched
        self.fc.fd["navigation_panel"].verify_welcome_module_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
        assert bool(self.fc.fd["system_control"].verify_cool_mode_selected_consumer()) is True

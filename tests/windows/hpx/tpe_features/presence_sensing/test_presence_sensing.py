from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Presence_Sensing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
        time.sleep(5)

    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_check_presence_sensing_module_show_up_C44005637(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["presence_sensing"].verify_presence_sensing_module_on_home_page()) is True, "Presence sensing module is not visible on home page"
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_presence_sensing_module_show()) is True, "Presence sensing module is  not visible"

    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_check_presence_sensing_module_settings_page_show_up_C44005640(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_presence_sensing_module_show()) is True, "Presence sensing module is  not visible"
        self.fc.fd["navigation_panel"].click_presence_sensing_module()
        assert bool(self.fc.fd["navigation_panel"].verify_power_battery_settings_page_show()) is True, "Power and battery settings page is not visible"
        self.fc.fd["navigation_panel"].click_close_button_on_power_battery_settings_page()
        time.sleep(2)


    @pytest.mark.consumer
    @pytest.mark.function
    def test_03_check_presence_sensing_module_always_show_up_C44005695(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["presence_sensing"].verify_presence_sensing_module_on_home_page()) is True, "Presence sensing module is not visible on home page"
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_presence_sensing_module_show()) is True, "Presence sensing module is  not visible"

        self.fc.fd["presence_sensing"].navigate_to_settings_page()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_presence_sensing_module_show()) is True, "Presence sensing module is  not visible"

        self.fc.restart_myHP()
        assert bool(self.fc.fd["presence_sensing"].verify_presence_sensing_module_on_home_page()) is True, "Presence sensing module is not visible on home page"
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_presence_sensing_module_show()) is True, "Presence sensing module is  not visible"
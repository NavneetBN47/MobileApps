from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Display_Control_HDR_Portrait(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            time.sleep(3)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)

    #This suite should only run in bopeep according to test rail
    @pytest.mark.ota
    def test_01_brightness_slider_with_windows_setting_C41042195(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        hpx_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")

        time.sleep(2)
        self.sf.click_windows_battery_icon()

        time.sleep(2)
        system_brightness_value = int(self.sf.get_windows_brightness_value())
        if system_brightness_value != 0:
            self.sf.windows_brightness_decrease(50)
        else:
            self.sf.windows_brightness_increase(50)
        
        new_system_brightness_value = self.sf.get_windows_brightness_value()
        self.sf.click_windows_battery_icon()

        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"
        time.sleep(5)
        self.fc.fd["display_control"].click_see_more_link()
        time.sleep(5)
        self.fc.fd["display_control"].click_discard_changes_button()

        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == hpx_brightness_value

        time.sleep(5)
        self.sf.click_windows_battery_icon()

        time.sleep(2)
        system_brightness_value = int(self.sf.get_windows_brightness_value())
        if system_brightness_value != 0:
            self.sf.windows_brightness_decrease(50)
        else:
            self.sf.windows_brightness_increase(50)
        new_system_brightness_value = self.sf.get_windows_brightness_value()
        time.sleep(3)
        self.sf.click_windows_battery_icon()
        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"
        time.sleep(5)
        self.fc.fd["display_control"].click_see_more_link()
        time.sleep(5)
        self.fc.fd["display_control"].click_keep_new_changes_button()

        time.sleep(3)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") != hpx_brightness_value, "Brightness value is not changed"
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == new_system_brightness_value, "Brightness value is not changed"

    
    @pytest.mark.ota
    def test_02_brightness_slider_with_windows_setting_C41042197(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        hpx_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")

        time.sleep(2)
        self.sf.click_windows_battery_icon()

        time.sleep(2)
        system_brightness_value = int(self.sf.get_windows_brightness_value())
        if system_brightness_value != 0:
            self.sf.windows_brightness_decrease(50)
        else:
            self.sf.windows_brightness_increase(50)
        
        new_system_brightness_value = self.sf.get_windows_brightness_value()
        self.sf.click_windows_battery_icon()

        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"
        self.fc.fd["display_control"].click_see_more_link()
        time.sleep(5)
        self.fc.fd["display_control"].click_discard_changes_button()

        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == hpx_brightness_value, "Brightness value is not changed"

        time.sleep(5)
        self.sf.click_windows_battery_icon()

        time.sleep(2)
        system_brightness_value = int(self.sf.get_windows_brightness_value())
        if system_brightness_value != 0:
            self.sf.windows_brightness_decrease(50)
        else:
            self.sf.windows_brightness_increase(50)
        new_system_brightness_value = self.sf.get_windows_brightness_value()
        time.sleep(3)
        self.sf.click_windows_battery_icon()
        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"
        self.fc.fd["display_control"].click_see_more_link()
        time.sleep(5)
        self.fc.fd["display_control"].click_keep_new_changes_button()

        time.sleep(3)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") != hpx_brightness_value, "Brightness value is not changed"
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == new_system_brightness_value, "Brightness value is not changed"
    

    @pytest.mark.ota
    def test_03_brightness_slider_with_windows_setting_C41063336(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        hpx_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")

        time.sleep(2)
        self.sf.click_windows_battery_icon()

        time.sleep(2)
        system_brightness_value = int(self.sf.get_windows_brightness_value())
        if system_brightness_value != 0:
            self.sf.windows_brightness_decrease(50)
        else:
            self.sf.windows_brightness_increase(50)
        
        self.sf.click_windows_battery_icon()

        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"

        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"
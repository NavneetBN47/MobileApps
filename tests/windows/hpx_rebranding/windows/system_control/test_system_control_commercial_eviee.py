import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer
from MobileApps.libs.flows.windows.hpx_rebranding.utility.registry_utilities import RegistryUtilities


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_System_Control_Commercial_Eviee(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)      
        cls.re = RegistryUtilities(cls.driver.ssh)    
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.launch_myHP()
            time.sleep(10)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.add_capture_logs_file()
            time.sleep(5)
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\HP\\HP App\\SysControl"
        cls.re.update_value_type_dword(registry_path, "Enabled", 1)
        sro_registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\HP\\HP App\\SysControl\\ResOpt"
        cls.re.update_value_type_dword(sro_registry_path, "Enabled", 1)
        try: 
            cls.fc.copy_rebrand_logs_with_timestamp()
            time.sleep(2)
            if request.config.getoption("--ota-test") is not None:
                cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")
        try:
            time.sleep(2)
            cls.fc.close_myHP()
            time.sleep(2)
            cls.fc.fd["system_control"].open_system_settings_power_and_battery()
            time.sleep(5)
            cls.fc.fd["devicesMFE"].maximize_app()
            time.sleep(2)
            cls.fc.fd["system_control"].click_windows_energy_saver_item()
            time.sleep(2)
            if cls.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "1":
                time.sleep(2)
                cls.fc.fd["system_control"].click_windows_energy_saver_button()
                time.sleep(2)
                cls.fc.close_windows_settings_panel()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")
        
    
    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_01_verify_system_control_show_C44275075(self):
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)

    #     assert self.fc.fd["system_control"].verify_smart_sense_title_show(), "Smart sense title is not displayed"
    #     assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance control title is not displayed"
    #     assert self.fc.fd["system_control"].verify_power_saving_mode_title_show(), "Power saving mode title is not displayed"
    

    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_02_system_control_module_UI_v2_C51244950(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)

    #     assert self.fc.fd["system_control"].verify_smart_sense_title_show(), "Smart sense title is not displayed"
    #     assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance control title is not displayed"
    #     assert self.fc.fd["system_control"].verify_power_saving_mode_title_show(), "Power saving mode title is not displayed"
    #     assert self.fc.fd["system_control"].verify_optimize_oled_title_show(), "Optimize OLED title is not displayed"
    #     assert self.fc.fd["system_control"].verify_optimize_oled_toggle_show(), "Optimize OLED toggle is not displayed"
    

    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_03_verify_system_control_module_tooltips_v2_C51244951(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)

    #     assert self.fc.fd["system_control"].get_smart_sense_tooltip_text() == "Automatically adapt the system to your demand with optimization for performance, fan noise and temperature based on the application you are using, placement of the laptop, and battery status.", "Smart sense tooltip text is not displayed"
    #     assert self.fc.fd["system_control"].get_performance_tooltip_text() == "Ideal for software that requires heavy use of the CPU. When enabled, fan speed will increase to cool the device.", "Performance control tooltip text is not displayed"
    #     assert self.fc.fd["system_control"].get_optimize_oled_tooltip_text() == "When enabled, this helps improve battery life by optimizing OLED panel power consumption.This mode can moderately affect the screen brightness and picture quality.", "Optimize OLED tooltip text is not displayed"
    

    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_04_myhp_UI_C51244945(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     assert bool(self.fc.fd["devicesMFE"].verify_device_card_show_up()) is True, "Device card is not displayed on home page"
    

    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_05_performance_with_energy_saver_C52996479(self):
    #     self.fc.close_myHP()
    #     time.sleep(2)

    #     # open system settings power and battery
    #     self.fc.fd["system_control"].open_system_settings_power_and_battery()
    #     time.sleep(5)
    #     self.fc.fd["devicesMFE"].maximize_app()
    #     time.sleep(2)
    #     # click windows energy saver item
    #     self.fc.fd["system_control"].click_windows_energy_saver_item()
    #     time.sleep(2)
    #     if self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "1":
    #         time.sleep(2)
    #         self.fc.fd["system_control"].click_windows_energy_saver_button()
    #         time.sleep(2)
    #     # verify energy saver button state is on
    #     assert self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "0", "Windows Energy Saver button is not on"
    #     time.sleep(2)
    #     # close windows settings panel
    #     self.fc.close_windows_settings_panel()
    #     time.sleep(3)

    #     # restart myHP
    #     self.fc.restart_myHP()
    #     time.sleep(2)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)
    #     self.fc.fd["system_control"].click_performance_toggle()
    #     time.sleep(2)
    #     self.fc.close_myHP()
    #     time.sleep(2)  

    #     # open system settings power and battery
    #     self.fc.open_winodws_power_sleep_page()
    #     time.sleep(2)
    #     self.fc.fd["system_control"].click_windows_energy_saver_item()
    #     time.sleep(2)
    #     if self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "0":
    #         time.sleep(2)
    #         self.fc.fd["system_control"].click_windows_energy_saver_button()
    #     time.sleep(2)
    #     self.fc.close_windows_settings_panel()
    #     time.sleep(2)

    #     # restart myHP
    #     self.fc.restart_myHP()
    #     time.sleep(2)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)
    #     if self.fc.fd["system_control"].verify_energy_saver_enabled_title_show() is False:
    #         time.sleep(2)
    #         self.fc.restart_myHP()
    #         time.sleep(2)
    #         self.fc.fd["devicesMFE"].click_device_card()
    #         time.sleep(3)
    #         self.fc.swipe_window(direction="down", distance=6)
    #         time.sleep(2)
    #         self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #         time.sleep(2)
    #         assert self.fc.fd["system_control"].verify_energy_saver_enabled_title_show(), "Energy saver enabled tilte is not show"
    #     else:
    #         assert self.fc.fd["system_control"].verify_energy_saver_enabled_title_show(), "Energy saver enabled tilte is not show"
    #     time.sleep(2)
    #     self.fc.close_myHP()
    #     time.sleep(2)

    #     # open system settings power and battery
    #     self.fc.open_winodws_power_sleep_page()
    #     time.sleep(2)
    #     self.fc.fd["system_control"].click_windows_energy_saver_item()
    #     time.sleep(2)
    #     self.fc.fd["system_control"].click_windows_energy_saver_button()
    #     time.sleep(2)
    #     self.fc.close_windows_settings_panel()
    #     time.sleep(2)
        
    #     # restart myHP
    #     self.fc.restart_myHP()
    #     time.sleep(2)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].verify_energy_saver_enabled_title_show() is False, "Energy saver enabled tilte is show"
    
    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_06_optimize_power_consumption_v2_C51244967(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)

    #     if self.fc.fd["system_control"].get_optimize_oled_toggle_state() == "1":
    #         self.fc.fd["system_control"].click_optimize_oled_toggle()
    #         time.sleep(2)
    #         assert self.fc.fd["system_control"].get_optimize_oled_toggle_state() == "0", "Optimize OLED toggle is not displayed"
    #         time.sleep(2)
    #         self.fc.fd["system_control"].click_optimize_oled_toggle()
    #         time.sleep(2)
    #         assert self.fc.fd["system_control"].get_optimize_oled_toggle_state() == "1", "Optimize OLED toggle is not displayed"
    #     else:
    #         self.fc.fd["system_control"].click_optimize_oled_toggle()
    #         time.sleep(2)
    #         assert self.fc.fd["system_control"].get_optimize_oled_toggle_state() == "1", "Optimize OLED toggle is not displayed" 
    #         time.sleep(2)
    #         self.fc.fd["system_control"].click_optimize_oled_toggle()
    #         time.sleep(2)
    #         assert self.fc.fd["system_control"].get_optimize_oled_toggle_state() == "0", "Optimize OLED toggle is not displayed"

    @pytest.mark.ota
    @pytest.mark.function
    def test_07_battery_saver_and_energy_saver_warning_banner_C51244953(self):
        self.fc.close_myHP()
        time.sleep(2)

        # open system settings power and battery
        self.fc.fd["system_control"].open_system_settings_power_and_battery()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(2)
        # click windows energy saver item
        self.fc.fd["system_control"].click_windows_energy_saver_item()
        time.sleep(2)
        # if energy saver button state is on, click it to turn on
        if self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "0":
            time.sleep(2)
            self.fc.fd["system_control"].click_windows_energy_saver_button()
            time.sleep(2)
        # verify energy saver button state is on
        assert self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "1", "Windows Energy Saver button is not on"
        time.sleep(2)
        # close windows settings panel
        self.fc.close_windows_settings_panel()
        time.sleep(2)

        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        # verify energy_saver_enabled banner pop up
        assert self.fc.fd["system_control"].verify_energy_saver_enabled_banner_show(), "Energy Saver Enabled title is not displayed"
        time.sleep(1)
        # get energy_saver_enabled banner description
        assert self.fc.fd["system_control"].verify_energy_saver_enabled_banner_description_show(), "Energy Saver Enabled description is not displayed"
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)

        # open system settings power and battery
        self.fc.fd["system_control"].open_system_settings_power_and_battery()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(2)
        # click windows energy saver item
        self.fc.fd["system_control"].click_windows_energy_saver_item()
        time.sleep(2)
        # verify energy saver button state is on
        assert self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "1", "Windows Energy Saver button is not on"
        time.sleep(2)
        # click energy saver button
        self.fc.fd["system_control"].click_windows_energy_saver_button()
        time.sleep(2)
        # verify energy saver button state is off
        assert self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "0", "Windows Energy Saver button is not off"
        time.sleep(2)
        # close windows settings panel
        self.fc.close_windows_settings_panel()
        time.sleep(2)

        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        # verify energy_saver_enabled banner not pop up
        assert self.fc.fd["system_control"].verify_energy_saver_enabled_banner_show() is False, "Energy Saver Enabled title is displayed"
        time.sleep(1)
        self.fc.close_myHP()
        time.sleep(2)
    
    # # Feature is not ready for production 
    # @pytest.mark.function
    # def test_08_verify_smart_resource_optimizer_show_C58467626(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)

    #     assert self.fc.fd["system_control"].verify_smart_sense_title_show(), "Smart sense title is not displayed"
    #     time.sleep(2)

    #     assert self.fc.fd["system_control"].verify_smart_resource_optimizer_toggle_show(), "Smart Resource Optimizer toggle is not displayed"
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].get_smart_resource_optimizer_description() == "Optimize performance for your most-used apps by prioritizing CPU resources.", "Smart Resource Optimizer description is not displayed"
    

    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_09_navigate_to_each_button_use_tab_C50723553(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(3)

    #     self.fc.fd["system_control"].press_tab("smart_sense_radio_button_commercial")
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].is_focus_on_element("smart_sense_radio_button_commercial"), "Smart sense radio button is not focused"
    #     time.sleep(2)
    #     self.fc.fd["system_control"].press_tab("system_control_performance_toggle")
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].is_focus_on_element("system_control_performance_toggle"), "System control performance toggle is not focused"
    #     time.sleep(2)
    #     self.fc.fd["system_control"].press_tab("optimize_oled_toggle")
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].is_focus_on_element("optimize_oled_toggle"), "Optimize OLED toggle is not focused"
    #     time.sleep(2)
    #     self.fc.fd["system_control"].press_tab("smart_resource_optimizer_toggle")
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].is_focus_on_element("smart_resource_optimizer_toggle"), "Smart resource optimizer toggle is not focused"
    

    # @pytest.mark.function
    # def test_10_press_alt_f4_from_keyboard_C50723562(self):
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System Control card is not displayed"
    #     time.sleep(2)
    #     self.fc.fd["system_control"].press_alt_f4_to_close_app()
    #     time.sleep(2)
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show() is False, "System Control card is displayed after alt+f4"
    

    # @pytest.mark.function
    # def test_11_modify_the_registry_to_disable_enable_system_control_C59779361(self):
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System Control card is not displayed"
    #     time.sleep(2)
    #     registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\HP\\HP App\\SysControl"
    #     self.re.update_value_type_dword(registry_path, "Enabled", 0)
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show() is False, "System Control card is displayed after modify the registry to disable it"
    #     time.sleep(2)
    #     self.re.update_value_type_dword(registry_path, "Enabled", 1)
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System Control card is not displayed after modify the registry to enable it"
    

    # @pytest.mark.function
    # def test_12_modify_the_registry_to_disable_enable_smart_resource_optimizer_C59779378(self):
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System Control card is not displayed"
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].verify_smart_resource_optimizer_toggle_show(), "Smart Resource Optimizer toggle is not displayed"
    #     registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\HP\\HP App\\SysControl\\ResOpt"
    #     self.re.update_value_type_dword(registry_path, "Enabled", 0)
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].verify_smart_resource_optimizer_toggle_show() is False, "Smart Resource Optimizer toggle is displayed after modify the registry to disable it"
    #     time.sleep(2)
    #     self.re.update_value_type_dword(registry_path, "Enabled", 1)
    #     self.fc.restart_myHP()
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_device_card()
    #     time.sleep(3)
    #     self.fc.swipe_window(direction="down", distance=6)
    #     time.sleep(2)
    #     self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
    #     time.sleep(2)
    #     assert self.fc.fd["system_control"].verify_smart_resource_optimizer_toggle_show(), "Smart Resource Optimizer toggle is not displayed"

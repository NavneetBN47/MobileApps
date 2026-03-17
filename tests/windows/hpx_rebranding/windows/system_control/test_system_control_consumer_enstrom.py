import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_System_Control_Consumer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)      
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
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_bi_directional_function_on_support_device_C43876454(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance Control title is not displayed" 
        time.sleep(1)
        assert self.fc.fd["system_control"].verify_system_control_cool_title_show(), "Cool title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_quiet_title_show(), "Quiet title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_powersaver_title_show(), "Power Saver title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_title_show(), "Performance title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        # if performanced button not selected, click it
        if self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "false":
            self.fc.fd["system_control"].click_performance_toggle()
            time.sleep(2)
        # verify performanced button is selected
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        time.sleep(3)
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
        if self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "1":
            time.sleep(2)
            self.fc.fd["system_control"].click_windows_energy_saver_button()
            time.sleep(2)
        # verify energy saver button state is off
        assert self.fc.fd["system_control"].verify_windows_energy_saver_button_state() == "0", "Windows Energy Saver button is not on"
        time.sleep(2)
        # click energy saver button
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
        time.sleep(1)
        # verify power saver button is selected
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "true", "Power Saver mode is not selected"
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
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        # verify energy_saver_enabled banner not pop up
        assert self.fc.fd["system_control"].verify_energy_saver_enabled_banner_show() is False, "Energy Saver Enabled title is displayed"
        time.sleep(1)
        # verify performanced button is selected
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)

        # open system settings power and battery
        self.fc.fd["system_control"].open_system_settings_power_and_battery()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(2)
        # verify power mode text state in system settings
        assert self.fc.fd["system_control"].get_power_mode_text_state_in_system_settings() == "Best Performance", "Power mode text is not Energy Saver"
        # close windows settings panel
        time.sleep(2)
        self.fc.close_windows_settings_panel()
        time.sleep(2) 

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_navigate_to_each_button_use_tab_C51909745(self):
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)

        self.fc.fd["system_control"].press_tab("smart_sense_radio_button")
        time.sleep(2)
        assert self.fc.fd["system_control"].is_focus_on_element("smart_sense_radio_button"), "Smart sense radio button is not focused"
        time.sleep(2)
        self.fc.fd["system_control"].press_tab("system_control_balanced_toggle")
        time.sleep(2)
        assert self.fc.fd["system_control"].is_focus_on_element("system_control_balanced_toggle"), "System control balanced toggle is not focused"
        time.sleep(2)
        self.fc.fd["system_control"].press_tab("system_control_cool_toggle")
        time.sleep(2)
        assert self.fc.fd["system_control"].is_focus_on_element("system_control_cool_toggle"), "System control cool toggle is not focused"
        time.sleep(2)
        self.fc.fd["system_control"].press_tab("system_control_quiet_toggle")
        time.sleep(2)
        assert self.fc.fd["system_control"].is_focus_on_element("system_control_quiet_toggle"), "System control quiet toggle is not focused"
        time.sleep(2)
        self.fc.fd["system_control"].press_tab("system_control_performance_toggle")
        time.sleep(2)
        assert self.fc.fd["system_control"].is_focus_on_element("system_control_performance_toggle"), "System control performance toggle is not focused"
        time.sleep(2)
        self.fc.fd["system_control"].press_tab("dim_background_toggle")
        time.sleep(2)
        assert self.fc.fd["system_control"].is_focus_on_element("dim_background_toggle"), "System control dim background toggle is not focused"


    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_03_press_alt_f4_from_keyboard_C51909754(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System Control card is not displayed"
        time.sleep(2)
        self.fc.fd["system_control"].press_alt_f4_to_close_app()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show() is False, "System Control card is displayed after alt+f4" 
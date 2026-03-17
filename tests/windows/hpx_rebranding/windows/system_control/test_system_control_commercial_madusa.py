import time
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_System_Control_Commercial_Madusa(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_system_control_module_UI_v1_C51244948(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_smart_sense_title_show(), "Smart sense title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_cool_title_show(), "Cool title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_quiet_title_show(), "Quiet title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance control title is not displayed"
        assert self.fc.fd["system_control"].verify_power_saving_mode_title_show(), "Power saving mode title is not displayed"
        assert self.fc.fd["system_control"].verify_optimize_oled_title_show(), "Optimize OLED title is not displayed"
        assert self.fc.fd["system_control"].verify_optimize_oled_toggle_show(), "Optimize OLED toggle is not displayed"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_verify_system_control_module_tooltips_v1_C51244949(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        assert self.fc.fd["system_control"].get_smart_sense_tooltip_text() == "Automatically adapt the system to your demand with optimization for performance, fan noise and temperature based on the application you are using, placement of the laptop, and battery status.", "Smart sense tooltip text is not displayed"
        assert self.fc.fd["system_control"].get_cool_tooltip_text() == "Ideal for situations where the device feels warm to the touch. When enabled, fan speed will increase and CPU performance decreases to cool the device.", "Cool tooltip text is not displayed"
        assert self.fc.fd["system_control"].get_quiet_tooltip_text() == "Ideal for quiet environments. When enabled, the fan will not turn on or will operate at minimum speed. CPU performance will decrease.", "Quiet tooltip text is not displayed"
        assert self.fc.fd["system_control"].get_performance_tooltip_text() == "Ideal for software that requires heavy use of the CPU. When enabled, fan speed will increase to cool the device.", "Performance control tooltip text is not displayed"
        assert self.fc.fd["system_control"].get_optimize_oled_tooltip_text() == "When enabled, this helps improve battery life by optimizing OLED panel power consumption.This mode can moderately affect the screen brightness and picture quality.", "Optimize OLED tooltip text is not displayed"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_verify_optimize_oled_consumption_show_C51244965(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_optimize_oled_toggle_show(), "Optimize OLED toggle is not displayed"
        assert self.fc.fd["system_control"].get_optimize_oled_tooltip_text() == "When enabled, this helps improve battery life by optimizing OLED panel power consumption.This mode can moderately affect the screen brightness and picture quality.", "Optimize OLED tooltip text is not displayed"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_performance_control_for_workstation_C51244952(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)

        assert self.fc.fd["system_control"].verify_smart_sense_title_show(), "Smart sense title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance control title is not displayed"
        assert self.fc.fd["system_control"].verify_power_saving_mode_title_show(), "Power saving mode title is not displayed"
        assert self.fc.fd["system_control"].verify_optimize_oled_title_show(), "Optimize OLED title is not displayed"
        assert self.fc.fd["system_control"].verify_optimize_oled_toggle_show(), "Optimize OLED toggle is not displayed"
    

    @pytest.mark.function
    def test_05_cotextual_config_system_control_C53231630(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["system_control"].click_performance_toggle()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        assert self.fc.fd["system_control"].verify_high_performance_mode_show(), "High performance mode is not displayed"   
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_06_reluanch_for_system_control_C44275076(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["system_control"].click_performance_toggle()
        time.sleep(3)
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        # blocked by HPXWC-32514
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_07_navigate_to_other_module_and_relaunch_system_control_C51244954(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["system_control"].click_performance_toggle()
        time.sleep(3)
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_hppk_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        # blocked by HPXWC-33632
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        # blocked by HPXWC-33632
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
         
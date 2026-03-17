import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_usb_and_charger")
class Test_Suite_System_Control(object):
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_change_pc_power_state_verify_power_saver_will_disable_and_enable_and_power_saver_mode_will_switch_back_C43876445(self):
        self.vcosmos.remove_charger_and_usb()
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        #power saver is enabled to select after charger is removed
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_enable_disable_state() == "true", "Power saver mode is disabled"
        self.fc.fd["system_control"].click_balanced_toggle()
        assert self.fc.fd["system_control"].get_system_control_balance_radiobutton_is_selected() =="true", "Balance mode is not selected"
        self.fc.fd["system_control"].click_powersaver_toggle()
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "true", "Power Saver mode is not selected"
        self.vcosmos.add_charger_and_usb()
        #once the charger is inserted power saver is disabled and cannot be selected
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_enable_disable_state() == "false", "Power saver mode is enabled"
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "false", "Power Saver mode is selected"
        assert self.fc.fd["system_control"].get_system_control_balance_radiobutton_is_selected() =="true", "Balance mode is not selected"
        #once the charger is connected again power saver is enabled and selects automatically
        self.vcosmos.remove_charger_and_usb()
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_enable_disable_state() == "true", "Power saver mode is disabled"
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "true", "Power Saver mode is not selected"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_switch_back_and_relaunch_verify_setting_can_remember_C43876450(self):
        #Power saver mode
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "true", "Power Saver mode is not selected"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "true", "Power Saver mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "true", "Power Saver mode is not selected"
        #Cool mode
        self.fc.fd["system_control"].click_cool_toggle()
        assert self.fc.fd["system_control"].get_system_control_cool_radiobutton_is_selected() == "true", "Cool mode is not selected"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_control_cool_radiobutton_is_selected() == "true", "Cool mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_control_cool_radiobutton_is_selected() == "true", "Cool mode is not selected"
        #Quiet mode
        self.fc.fd["system_control"].click_quiet_toggle()
        assert self.fc.fd["system_control"].get_system_quiet_radiobutton_is_selected() == "true", "Quiet mode is not selected"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_quiet_radiobutton_is_selected() == "true", "Quiet mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_quiet_radiobutton_is_selected() == "true", "Quiet mode is not selected"
        #Performance mode
        self.fc.fd["system_control"].click_performance_toggle()
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        # Smart sense mode
        self.fc.fd["system_control"].click_smart_sense_radio_button()
        assert self.fc.fd["system_control"].get_system_smart_sense_radiobutton_is_selected() == "true", "Smart sense mode is not selected"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_smart_sense_radiobutton_is_selected() == "true", "Smart sense mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_smart_sense_radiobutton_is_selected() == "true", "Smart sense mode is not selected"
        #Balanced mode
        self.fc.fd["system_control"].click_balanced_toggle()
        assert self.fc.fd["system_control"].get_system_control_balance_radiobutton_is_selected() == "true", "Balanced mode is not selected"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_control_balance_radiobutton_is_selected() == "true", "Balanced mode is not selected"
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].get_system_control_balance_radiobutton_is_selected() == "true", "Balanced mode is not selected"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_select_each_mode_in_system_control_verify_each_mode_function_will_work_well_C43876446(self):
        #Balanced mode
        self.fc.fd["system_control"].click_balanced_toggle()
        assert self.fc.fd["system_control"].get_system_control_balance_radiobutton_is_selected() == "true", "Balanced mode is not selected"
        output = self.fc.system_control_cmd()
        assert "1" == output,"Balanced mode is not byte 1"
        #Cool mode
        self.fc.fd["system_control"].click_cool_toggle()
        assert self.fc.fd["system_control"].get_system_control_cool_radiobutton_is_selected() == "true", "Cool mode is not selected"
        output = self.fc.system_control_cmd()
        assert "2" == output,"Cool mode is not byte 2"
        #Quiet mode
        self.fc.fd["system_control"].click_quiet_toggle()
        assert self.fc.fd["system_control"].get_system_quiet_radiobutton_is_selected() == "true", "Quiet mode is not selected"
        output = self.fc.system_control_cmd()
        assert "3" == output,"Quiet mode is not byte 3"
        #Performance mode
        self.fc.fd["system_control"].click_performance_toggle()
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        output = self.fc.system_control_cmd()
        assert "0" == output,"Performance mode is byte not 0"
        #Power saver mode
        self.fc.fd["system_control"].click_powersaver_toggle()
        assert self.fc.fd["system_control"].get_system_control_powersaver_radiobutton_is_selected() == "true", "Power Saver mode is not selected"
        output = self.fc.system_control_cmd()
        assert "4" == output,"Power saver mode byte is not 4"
        # Smart sense mode
        self.fc.fd["system_control"].click_smart_sense_radio_button()
        assert self.fc.fd["system_control"].get_system_smart_sense_radiobutton_is_selected() == "true", "Smart sense mode is not selected"
        output = self.fc.system_control_cmd()
        assert "5" == output,"Smart Sense mode byte is not 5"

        #Insert charger back so device is charged all time
        self.vcosmos.add_charger_and_usb()
        self.vcosmos.clean_up_logs()
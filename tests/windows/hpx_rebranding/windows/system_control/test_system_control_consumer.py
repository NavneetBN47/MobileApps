import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_System_Control_Consumer(object):
    
    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_01_verify_system_control_show_C43876441(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System Control card is not displayed"  
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_system_control_default_ui_C43876442(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance Control title is not displayed" 
        assert self.fc.fd["system_control"].verify_system_control_cool_title_show(), "Cool title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_quiet_title_show(), "Quiet title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_powersaver_title_show(), "Power Saver title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_title_show(), "Performance title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_focus_mode_title_show(), "Focus Mode title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_dim_background_title_show(), "Dim Background title is not displayed"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_click_system_control_each_mode_C43876443(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["system_control"].click_balanced_toggle()
        time.sleep(2)
        self.fc.fd["system_control"].click_cool_toggle()
        time.sleep(2)
        self.fc.fd["system_control"].click_quiet_toggle()
        time.sleep(2)
        self.fc.fd["system_control"].click_powersaver_toggle()
        time.sleep(2)
        self.fc.fd["system_control"].click_performance_toggle()

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_hover_on_each_tips_icon_C43876444(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance Control title is not displayed" 
        time.sleep(1)
        # verify smart sence title show
        assert self.fc.fd["system_control"].verify_smart_sense_title_show(),"smart sence title is not displayed"
        # verify smart sence tips icon show
        assert self.fc.fd["system_control"].verify_smart_sence_tips_icon_show(),"smart sence tips icon is not displayed"
        # click smart sence tips icon
        self.fc.fd["system_control"].click_smart_sence_tips_icon()
        time.sleep(2)
        # verify smart sence tips show
        assert self.fc.fd["system_control"].get_smart_sence_tips() == "Adapt the system automatically to your demand, using AI. Optimize for performance, fan, noise, and temperature based on the application you're using, laptop placement, and battery status. Smart Sense doesn't include Performance mode or Cool mode.","tips now show"
        time.sleep(2)
        # verify balanced title show
        assert self.fc.fd["system_control"].verify_balanced_title_show(),"balanced tilte is now shown"
        # verify balanced tips icon show
        assert self.fc.fd["system_control"].verify_balanced_tips_icon_show(),"balanced tips icon is not displayed"
        # click balanced tips icon
        self.fc.fd["system_control"].click_balanced_icon()
        time.sleep(2)
        # verify balanced tips show
        assert self.fc.fd["system_control"].get_balanced_tips() == "Balance fan speed, performance, and temperature.","tips not show"
        time.sleep(2)
        # verify cool title show
        assert self.fc.fd["system_control"].verify_system_control_cool_title_show(), "Cool title is not displayed"
        # verify cool tips icon show
        assert self.fc.fd["system_control"].verify_cool_tips_icon_show(),"cool tips icon is not shown"  
        # click cool tips icon
        self.fc.fd["system_control"].click_cool_tips_icon()
        time.sleep(2)
        # verify cool tips show
        assert self.fc.fd["system_control"].get_cool_tips() == "Increase fan speed and decrease CPU performance to cool the device. Ideal for situations where the device feels warm to the touch.","tips not show"
        # verify quiet title show
        assert self.fc.fd["system_control"].verify_system_control_quiet_title_show(), "Quiet title is not displayed"
        # verify quiet tips show
        assert self.fc.fd["system_control"].verify_quiet_tips_icon_show(),"quiet tips icon is not show"
        # click queit tips icon
        self.fc.fd["system_control"].click_quiet_tips_icon()
        time.sleep(2)
        # verify quiet tips show
        assert self.fc.fd["system_control"].get_quiet_tips() == "Keep operating at minimum speed. CPU performance will decrease. Ideal for quiet environments.","tips not show"
        time.sleep(2)
        # verify power saver title show
        assert self.fc.fd["system_control"].verify_system_control_powersaver_title_show(), "Power Saver title is not displayed"
        # verify power saver tips icon show
        assert self.fc.fd["system_control"].verify_power_saver_tips_icon_show(),"power saver tips icon is not show"
        # click power saver tips icon
        self.fc.fd["system_control"].click_power_saver_tips_icon()
        time.sleep(2)
        # verify power saver tips
        assert self.fc.fd["system_control"].get_power_saver_tips() == "Preserve power to lower your carbon footprint and/or extend PC battery life. This will limit CPU performance, improve OLED panel power saving, or both.","tips now show"
        time.sleep(2)
        # verify performanced title show
        assert self.fc.fd["system_control"].verify_system_control_performance_title_show(), "Performance title is not displayed"
        # verify performanced tips icon show
        assert self.fc.fd["system_control"].verify_performanced_tips_icon_show(),"tips icon is not show"
        # click performanced tips icon
        self.fc.fd["system_control"].click_performanced_tips_icon()
        time.sleep(2)
        # verify performanced tips
        assert self.fc.fd["system_control"].get_performanced_tips() == "Increase fan speed to cool the device when you're using software that requires heavy use of the CPU. Fan noise and overall device temperature might increase.","tips not show"
        #verify focus mode title show
        assert self.fc.fd["system_control"].verify_system_control_focus_mode_title_show(), "Focus Mode title is not displayed"
        # verify dim background windows title show
        assert self.fc.fd["system_control"].verify_system_control_dim_background_title_show(), "Dim Background title is not displayed"
        # verify dim background windows tips icon show
        assert self.fc.fd["system_control"].verify_dim_background_window_tips_icon_show()," dim background windows tips icon is not show"
        # click dim background windows tips icon
        self.fc.fd["system_control"].click_dim_background_window_tips_icon()
        time.sleep(2)
        # verify dim background windows tips
        assert self.fc.fd["system_control"].get_dim_background_window_tips() == "Keep the selected window in focus while other windows dim to save battery life and keep you focused (not compatible with external displays).","tips not show"
        time.sleep(2)
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_05_verify_focus_mode_on_support_device_C43876452(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance Control title is not displayed" 
        time.sleep(1)
        # verify focus mode title show
        assert self.fc.fd["system_control"].verify_system_control_focus_mode_title_show(), "Focus Mode title is not displayed"
        # verify dim background windows title show
        assert self.fc.fd["system_control"].verify_system_control_dim_background_title_show(), "Dim Background title is not displayed"
        # verify dim background windows tips icon show
        assert self.fc.fd["system_control"].verify_dim_background_window_tips_icon_show()," dim background windows tips icon is not show"
        # click dim background windows tips icon
        self.fc.fd["system_control"].click_dim_background_window_tips_icon()
        time.sleep(2)
        # verify dim background windows tips
        assert self.fc.fd["system_control"].get_dim_background_window_tips() == "Keep the selected window in focus while other windows dim to save battery life and keep you focused (not compatible with external displays).","tips not show"
        time.sleep(2)
        # verify dim background toggle show
        assert self.fc.fd["system_control"].verify_dim_background_toggle_show(), "dim background toggle is not displayed"
        # verify dim background toggle default is off
        assert self.fc.fd["system_control"].verify_dim_background_toggle_default_state() == "0","dim background toggle default is not off"
        # click dim background toggle
        self.fc.fd["system_control"].click_focus_mode_toggle()
        time.sleep(2)
        # verify dim background toggle is 1
        assert self.fc.fd["system_control"].verify_dim_background_toggle_default_state() == "1","dim background toggle is not on"
        time.sleep(2)
        # click dim background toggle
        self.fc.fd["system_control"].click_focus_mode_toggle()
        time.sleep(2)
        # verify dim background toggle default is off
        assert self.fc.fd["system_control"].verify_dim_background_toggle_default_state() == "0","dim background toggle default is not off"
        time.sleep(2)
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_restart_machine_verify_system_control_function_C64672403(self, request):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"


        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_system_control_card()
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"
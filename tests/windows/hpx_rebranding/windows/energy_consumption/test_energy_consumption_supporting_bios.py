import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Energy_Consumption(object):

    # Suite supposed to be run longhornz and supported BIOS
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_supported_platform_C51250958(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(10)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is True, "Energy consumption module is  not visible"

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_energy_consumption_invoking_C51250961(self):
        time.sleep(5)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_energy_consumption_consistency_C51250975(self):
        for _ in range(3):
            self.fc.restart_myHP()
            time.sleep(5)
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(10)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        for _ in range(3):
            self.fc.restart_myHP()
            time.sleep(5)
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(10)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        for _ in range(3):
            self.fc.restart_myHP()
            time.sleep(5)
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(15)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=2)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible" 

    @pytest.mark.ota
    def test_04_energy_consumption_consistency_check_for_consumption_dropdown_C51250963(self):
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_consumption_trends_dropdown()) is True, "Consistency dropdown is  not visible"
        self.fc.fd["energy_consumption"].select_value_from_consumption_trends_dropdown("last_6_days")
        self.fc.fd["energy_consumption"].select_value_from_consumption_trends_dropdown("last_6_months")
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_consumption_trends_dropdown()) is True, "Consistency dropdown is  not visible"

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_energy_consumption_card_energy_efficiency_guides_this_provides_hints_that_how_end_user_can_save_the_total_energy_consumption_C51250972(self):
        self.fc.swipe_window(direction="down", distance=10)
        assert bool(self.fc.fd["energy_consumption"].verify_how_to_adjust_power_and_sleep_settings_in_windows_link()) == True, "Power and Sleep Settings link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_caring_for_your_battery_in_windows_link()) == True, "Caring for your battery link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_battery_saving_tips_for_windows_link()) == True, "Battery saving tips link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_change_the_power_mode_for_your_windows_pc_link()) == True, "Change the power mode link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_manage_background_activity_for_apps_in_windows_link()) == True, "Manage background activity link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_learn_more_about_energy_recommendations_microsoft_support_link()) == True, "Learn more about energy recommendations link is not displayed"
        self.fc.fd["energy_consumption"].click_how_to_adjust_power_and_sleep_settings_in_windows_link()
        time.sleep(3)
        assert "https://support.microsoft.com/en-us/windows/power-settings-in-windows-11-0d6a2b6b-2e87-4611-9980-ac9ea2175734" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_caring_for_your_battery_in_windows_link()
        assert "https://support.microsoft.com/en-us/windows/caring-for-your-battery-in-windows-2db3e37f-5e7d-488e-9086-ed15320519e4" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_battery_saving_tips_for_windows_link()
        assert "https://support.microsoft.com/en-us/windows/battery-saving-tips-for-windows-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_change_the_power_mode_for_your_windows_pc_link()
        assert "https://support.microsoft.com/en-us/windows/change-the-power-mode-for-your-windows-pc-c2aff038-22c9-f46d-5ca0-78696fdf2de8" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_manage_background_activity_for_apps_in_windows_link()
        assert "https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_learn_more_about_energy_recommendations_microsoft_support_link()
        assert "https://support.microsoft.com/en-us/windows/learn-more-about-energy-recommendations-1c9b5a49-6d8f-4c04-80dc-5e3c20a9f04e" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_energy_consumption_card_more_helpful_links_C51250973(self):
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=12)
        assert bool(self.fc.fd["energy_consumption"].verify_product_carbon_footprint_link()) is True, "product carbon footprint link is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_energy_environment_link()) is True, "energy environment link is not visible"
        self.fc.fd["energy_consumption"].click_product_carbon_footprint_link_text()
        assert bool(self.fc.fd["energy_consumption"].verify_product_carbon_footprint_report_title()) is True, "product carbon footprint report title is not visible"
        #click app on task bar
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()
        time.sleep(3)
        self.fc.fd["energy_consumption"].click_energy_environment_link()
        assert bool(self.fc.fd["energy_consumption"].verify_epa_home_page_title()) is True, "epa home page title is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_energy_environment_report_title()) is True, "energy environment report title is not visible"
        #close browser
        self.fc.fd["energy_consumption"].click_myhp_on_task_bar()

    @pytest.mark.ota
    def test_07_energy_consumption_go_beyond_C51250967(self):
        self.fc.swipe_window(direction="up", distance=10)
        assert bool(self.fc.fd["energy_consumption"].verify_hp_logo()) == True, "HP logo is not displayed"
        assert bool (self.fc.fd["energy_consumption"].verify_energy_recommendation_logo()) == True, "Energy recommendation logo is not displayed"
        assert self.fc.fd["energy_consumption"].get_hp_excite_msg() == "HP is excited to help you understand your PC's energy consumption.", "Incorrect message"
        #Click on Hyperlink
        time.sleep(3)
        self.fc.fd["energy_consumption"].click_small_go_beyond_hyperlink("small_go_beyond_hyperlink")
        time.sleep(3)
        self.fc.fd["energy_consumption"].click_edge_on_taskbar()
        time.sleep(3)
        assert 'https://www.hp.com/us-en/sustainable-impact.html' in self.fc.fd["energy_consumption"].get_webpage_url() , "Incorrect URL"
        time.sleep(3)        
        self.fc.fd["energy_consumption"].click_download_report_button()
        assert '/h20195' in self.fc.fd["energy_consumption"].get_webpage_url() , "Incorrect URL"
        self.fc.kill_edge_process()

    @pytest.mark.ota
    def test_08_supported_platform_with_supported_Bios_C51250990(self):
        self.fc.fd["energy_consumption"].get_focus_on_app("total_energy_consumption")
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=5)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible" 
        assert bool(self.fc.fd["energy_consumption"].verify_learn_more_link()) is False, "BIOS update link is visible"

    def test_09_energy_consumption_enabling_the_fusion_C51250959(self):
        self.fc.kill_chrome_process()
        time.sleep(3)
        status = self.fc.get_hpsysinfo_fusion_services()
        assert status['stdout'].find('Running') == 138 , "HSA Systeminfo service is not installed and running in the service panel"               
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        self.fc.swipe_window(direction="up", distance=5)
        assert bool(self.fc.fd["energy_consumption"].verify_data_consumption_header())is True, "Real date tme is  not visible"

    @pytest.mark.ota
    def test_10_energy_consumption_behaviour_disabling_stop_the_fusion_C51250960(self):
        self.fc.stop_hpsysinfo_fusion_services()
        self.fc.restart_myHP()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(10)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is False, "Energy consumption module is  not visible"
        time.sleep(3)
        self.fc.close_myHP()
        self.fc.start_hpsysinfo_fusion_services()
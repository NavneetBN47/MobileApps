from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_energy_consumption_02(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    # Suite supposed to be run on Baymax, Longhornz and Ernesto    
    @pytest.mark.ota
    def test_01_energy_consumption_card_energy_efficiency_guides_this_provides_hints_that_how_end_user_can_save_the_total_energy_consumption_C42142069(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        self.fc.swipe_window(direction="down", distance=6)
        assert bool(self.fc.fd["energy_consumption"].verify_how_to_adjust_power_and_sleep_settings_in_windows_link()) == True, "Power and Sleep Settings link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_caring_for_your_battery_in_windows_link()) == True, "Caring for your battery link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_battery_saving_tips_for_windows_link()) == True, "Battery saving tips link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_change_the_power_mode_for_your_windows_pc_link()) == True, "Change the power mode link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_manage_background_activity_for_apps_in_windows_link()) == True, "Manage background activity link is not displayed"
        assert bool(self.fc.fd["energy_consumption"].verify_learn_more_about_energy_recommendations_microsoft_support_link()) == True, "Learn more about energy recommendations link is not displayed"
        self.fc.fd["energy_consumption"].click_how_to_adjust_power_and_sleep_settings_in_windows_link()        
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://support.microsoft.com/en-us/windows/how-to-adjust-power-and-sleep-settings-in-windows-26f623b5-4fcc-4194-863d-b824e5ea7679', "Incorrect URL"
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_caring_for_your_battery_in_windows_link()
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://support.microsoft.com/en-us/windows/caring-for-your-battery-in-windows-2db3e37f-5e7d-488e-9086-ed15320519e4', "Incorrect URL"
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_battery_saving_tips_for_windows_link()
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://support.microsoft.com/en-us/windows/battery-saving-tips-for-windows-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99', "Incorrect URL"
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_change_the_power_mode_for_your_windows_pc_link()
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://support.microsoft.com/en-us/windows/change-the-power-mode-for-your-windows-pc-c2aff038-22c9-f46d-5ca0-78696fdf2de8', "Incorrect URL"
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_manage_background_activity_for_apps_in_windows_link()
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef', "Incorrect URL"
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_learn_more_about_energy_recommendations_microsoft_support_link()
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://support.microsoft.com/en-us/windows/learn-more-about-energy-recommendations-1c9b5a49-6d8f-4c04-80dc-5e3c20a9f04e', "Incorrect URL"
        self.fc.fd["home"].click_close()
    
    @pytest.mark.ota
    def test_02_energy_consumption_go_beyond_C42142064(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        assert bool(self.fc.fd["energy_consumption"].verify_hp_logo()) == True, "HP logo is not displayed"
        assert bool (self.fc.fd["energy_consumption"].verify_energy_recommendation_logo()) == True, "Energy recommendation logo is not displayed"
        assert self.fc.fd["energy_consumption"].get_hp_excite_msg() == "HP is excited to help you understand your PC's energy consumption.", "Incorrect message"
        #Click on Hyperlink
        self.fc.fd["energy_consumption"].click_go_beyond_hyperlink()
        time.sleep(3)
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://www.hp.com/us-en/sustainable-impact.html', "Incorrect URL"
        self.fc.fd["energy_consumption"].click_download_report_button()
        assert self.fc.fd["energy_consumption"].get_webpage_url() == 'https://www8.hp.com/h20195/v2/GetPDF.aspx/c06040843.pdf', "Incorrect URL"
   
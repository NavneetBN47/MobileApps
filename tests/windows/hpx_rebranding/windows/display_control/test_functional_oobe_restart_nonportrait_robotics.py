import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.utility.vcosmos_utilities import VcosmosUtilities
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe_robotics")
class Test_Suite_Display_control(object):
    
    #this suite should only run in Thompson with RGB robotics
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_oobe_applications_reboot_validation_C52975794(self,request):
        # clean up logs possibly left by previous tests
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()

        #restore all apps default values in case of previous case failure
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=4)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle switch is enabled"
        slider_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert slider_value == "90", f"Brightness slider is not at default value of 90 actual value is {slider_value}"

        #select disney + and restore and validate default values
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(5)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch is not enabled"
        slider_value = self.fc.fd["display_control"].get_brightness_slider_value()
        assert slider_value == "100", f"Brightness slider is not at default value of 100 actual value is {slider_value}"

        #close HP app
        self.fc.close_myHP()

        #launch disney + app from start menu and verify RGB values
        self.fc.fd["display_control"].launch_all_apps("Disney")
        time.sleep(10)
        self.vcosmos.get_red_green_blue_clear_value()
        self.fc.kill_disney_video_process()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 850, f"Clear value is not greater than 850 actual value is {clear_int}"
            assert red_int >= 550, f"Red value is not greater than 550 actual value is {red_int}"
            assert green_int >= 620, f"Green value is not greater than 620 actual value is {green_int}"
            assert blue_int >= 410, f"Blue value is not greater than 410 actual value is {blue_int}"
        self.vcosmos.clean_up_logs()

        #restart machine and verify settings are retained
        restart_machine(self, request)

        #restart vcosmos utility after reboot
        self.vcosmos = VcosmosUtilities(self.fc.driver.ssh)

        self.fc.fd["display_control"].launch_all_apps("Disney")
        self.vcosmos.clean_up_logs()
        time.sleep(10)
        self.vcosmos.get_red_green_blue_clear_value()
        self.fc.kill_disney_video_process()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 850, f"Clear value is not greater than 850 actual value is {clear_int}"
            assert red_int >= 550, f"Red value is not greater than 550 actual value is {red_int}"
            assert green_int >= 620, f"Green value is not greater than 620 actual value is {green_int}"
            assert blue_int >= 410, f"Blue value is not greater than 410 actual value is {blue_int}"
        self.vcosmos.clean_up_logs()
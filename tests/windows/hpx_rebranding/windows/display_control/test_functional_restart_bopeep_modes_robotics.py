import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.utility.vcosmos_utilities import VcosmosUtilities
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_control(object):
    
    #this suite should only run in Bopeep with RGB robotics
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_display_modes_after_restart_C53000350(self,request):
        # clean up logs possibly left by previous tests
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        
        #restore all apps default values in case of previous case failure
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=4)
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_gaming_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")
        time.sleep(10)
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Gaming", f"Display mode is not Gaming actual value is {current_mode}"
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page", 44)
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "44", f"Brightness slider is not at value of 44 actual value is {current_brightness}"

        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 51 <= clear_int <= 81, f"Clear value is not between 51 and 81 actual value is {clear_int}"
            assert 26 <= red_int <= 56, f"Red value is not between 26 and 56 actual value is {red_int}"
            assert 35 <= green_int <= 65, f"Green value is not between 35 and 65 actual value is {green_int}"
            assert 14 <= blue_int <= 44, f"Blue value is not between 14 and 44 actual value is {blue_int}"
        self.vcosmos.clean_up_logs()

        #restart machine and verify settings are retained
        restart_machine(self, request)

        #restart vcosmos utility after reboot
        self.vcosmos = VcosmosUtilities(self.fc.driver.ssh)

        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert 51 <= clear_int <= 81, f"Clear value is not between 51 and 81 actual value is {clear_int}"
            assert 26 <= red_int <= 56, f"Red value is not between 26 and 56 actual value is {red_int}"
            assert 35 <= green_int <= 65, f"Green value is not between 35 and 65 actual value is {green_int}"
            assert 14 <= blue_int <= 44, f"Blue value is not between 14 and 44 actual value is {blue_int}"
        self.vcosmos.clean_up_logs()

        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        if "Restore HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
            time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        current_mode = self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page()
        assert current_mode == "Gaming", f"Display mode is not Gaming actual value is {current_mode}"
        current_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
        assert current_brightness == "44", f"Brightness slider is not at value of 44 actual value is {current_brightness}"
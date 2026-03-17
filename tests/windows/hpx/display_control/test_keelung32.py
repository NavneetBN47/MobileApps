from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import re
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_keelung(object):
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
    
    #this suite should run only on keelung 32
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_display_modes_ui_for_keelung32_C42808949(self):
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_display_modes_title() == "Display modes","Display modes is not present"
        assert self.fc.fd["display_control"].verify_natural_mode_title() == "Neutral","Neutral mode is not found" 
        assert self.fc.fd["display_control"].verify_warm_mode_title() == "Warm","Warm mode is not found"
        assert self.fc.fd["display_control"].verify_bt709_mode_title() == "BT709 (D65)","BT709 (D65) mode is not found"
        assert self.fc.fd["display_control"].verify_srgb_d65_mode_title() == "sRGB (D65)","sRGB (D65) mode is not found"
        assert self.fc.fd["display_control"].verify_cool_mode_title() == "Cool","Cool mode is not found"
        assert self.fc.fd["display_control"].verify_enhanceplus_mode_title() == "HP Enhance+","HP Enhanc mode is not found"
        assert self.fc.fd["display_control"].verify_native_tile() == "Native","Natice mode is not found"
        assert self.fc.fd["display_control"].verify_p3_d65_mode_title() == "P3 (D65)","P3 (D65) mode title is not found"

    def test_02_default_value_for_all_modes_for_first_launch_on_Keelung32_C42808951(self):
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(2)
        self.fc.fd["display_control"].click_restore_default_button()
        time.sleep(5)
        self.fc.fd["display_control"].click_neutral_mode_container()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "36","Brightness slider value is not 36"
        self.fc.fd["display_control"].click_warm_mode()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "6","Brightness slider value is not 6"
        self.fc.fd["display_control"].click_enhanceplus_mode()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "36","Brightness slider value is not 36"
        self.fc.fd["display_control"].click_native_tile()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "100","Brightness slider value is not 100"
        self.fc.fd["display_control"].click_cool_mode_title()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "22","Brightness slider value is not 22"
        self.fc.fd["display_control"].click_bt709_mode_title()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "6","Brightness slider value is not 6"
        self.fc.fd["display_control"].click_srgb_d65_mode_title()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "36","Brightness slider value is not 36"
        self.fc.fd["display_control"].click_p3_d65_mode_title()
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "36","Brightness slider value is not 36"
        self.fc.fd["display_control"].click_restore_default_button()
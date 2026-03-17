from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_keelung27(object):
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

    #This suite only runs on keelung27
    def test_01_display_modes_ui_C42808908(self):
        time.sleep(3)
        self.driver.swipe(direction="down", distance=3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        time.sleep(5)
         # Select native mode
        # verify native image mode show
        assert bool(self.fc.fd["display_control"].verify_native_tile()) is True, "Native image mode is not selected"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "neutral image mode is not selected"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_warm_mode_title()) is True, "neutral image mode is not selected"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_cool_mode_title()) is True, "neutral image mode is not selected"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "neutral image mode is not selected"
        time.sleep(1) 
        self.fc.close_myHP()

    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_display_modes_default_values_C42808910(self):
        time.sleep(3)
        self.driver.swipe(direction="down", distance=3)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        time.sleep(5)
        #Clicking on restore default as reset is not working but this is not a step in testcase
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "76", "The default brightness slider value is not 76"
        time.sleep(1)
        self.fc.fd["display_control"].click_warm_mode()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "18", "The default brightness slider value is not 18"
        time.sleep(1)
        self.fc.fd["display_control"].click_cool_mode_title()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "50", "The default brightness slider value is not 50"
        time.sleep(1)
        self.fc.fd["display_control"].click_enhanceplus_mode()
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "76", "The default brightness slider value is not 76"
        time.sleep(1)
        self.fc.fd["display_control"].click_native_tile()
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "The default brightness slider value is not 100"
        time.sleep(1)
        self.fc.close_myHP()
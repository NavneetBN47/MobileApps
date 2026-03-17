from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_touchpadhpone(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,request, windows_test_setup):
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
            time.sleep(3)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_verify_touchpad_module_show_C33426140(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # verify touchpad icon show
        assert bool(self.fc.fd["touchpadhpone"].verify_touchpad_icon_show()) is True, "touchpad icon is not show"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota

    def test_02_verify_touchpad_UI_C33619860(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # verify touchpad icon show
        assert bool(self.fc.fd["touchpadhpone"].verify_touchpad_icon_show()) is True, "touchpad icon is not show"
        time.sleep(1)
        # click touchpad icon
        self.fc.fd["touchpadhpone"].click_touchpad_iocn()
        time.sleep(1)
        # verify default touchpad ui
        assert bool(self.fc.fd["touchpadhpone"].verify_enable_gesture_control_text_show()) is True, "enable gesture control text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["touchpadhpone"].verify_enable_gesture_control_tipsicon_show()) is True, "enable gesture control tipsicon is not show"
        time.sleep(1)
        assert bool(self.fc.fd["touchpadhpone"].verify_enable_gesture_control_toggle_show()) is True, "enable gesture control toggle is not show"
        time.sleep(1)
        assert self.fc.fd["touchpadhpone"].get_default_enable_gesture_control_toggle_state() == "0", "default enable gesture control toggle state is on"
        time.sleep(1)
        assert bool(self.fc.fd["touchpadhpone"].verify_brightness_text_show()) is True, "brightness text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["touchpadhpone"].verify_volume_text_show()) is True, "volume text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["touchpadhpone"].verify_SVG_image_show()) is True, "SVG image is not show"
        time.sleep(1)
        assert bool(self.fc.fd["touchpadhpone"].verify_adjust_feedback_intensity_link_button_show()) is True, "adjust feedback intensity link button is not show"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_03_turn_on_off_Enable_gestures_control_toggle_C33620082(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # verify touchpad icon
        assert bool(self.fc.fd["touchpadhpone"].verify_touchpad_icon_show()) is True, "touchpad icon is not show"
        time.sleep(1)
        # click touchpad icon
        self.fc.fd["touchpadhpone"].click_touchpad_iocn()
        time.sleep(1)
        # verify enable gesture control toggle show
        assert bool(self.fc.fd["touchpadhpone"].verify_enable_gesture_control_toggle_show()) is True, "enable gesture control toggle is not show"
        time.sleep(1)
        # verify default enable gesture control toggle is off
        assert self.fc.fd["touchpadhpone"].get_default_enable_gesture_control_toggle_state() == "0", "default enable gesture control toggle state is on"
        time.sleep(1)
        # verify adjust feedback intensity link button show
        assert bool(self.fc.fd["touchpadhpone"].verify_adjust_feedback_intensity_link_button_show()) is True, "adjust feedback intensity link button is not show"
        time.sleep(1)
        # turn on enable gestures control toggle
        self.fc.fd["touchpadhpone"].click_enable_gesture_control_toggle()
        time.sleep(1)
        # verify default enable gesture control toggle is on
        assert self.fc.fd["touchpadhpone"].get_default_enable_gesture_control_toggle_state() == "1", "default enable gesture control toggle state is off"
        time.sleep(1)
        # turn off enable gestures control toggle
        self.fc.fd["touchpadhpone"].click_enable_gesture_control_toggle()
        time.sleep(1)
        # verify default enable gesture control toggle is off
        assert self.fc.fd["touchpadhpone"].get_default_enable_gesture_control_toggle_state() == "0", "default enable gesture control toggle state is on"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_04_click_adjust_feedback_intensity_link_verify_link_to_OS_touchpad_setting_page_C34972800(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # verify touchpad icon
        assert bool(self.fc.fd["touchpadhpone"].verify_touchpad_icon_show()) is True, "touchpad icon is not show"
        time.sleep(1)
        # click touchpad icon
        self.fc.fd["touchpadhpone"].click_touchpad_iocn()
        time.sleep(1)
        # verify adjust feedback intensity link button show
        assert bool(self.fc.fd["touchpadhpone"].verify_adjust_feedback_intensity_link_button_show()) is True, "adjust feedback intensity link button is not show"
        time.sleep(1)
        # click adjust feedback intensity link button
        self.fc.fd["touchpadhpone"].click_adjust_feedback_intensity_link_button()
        time.sleep(1)
        # verify_OS_touchpad_setting_page_show_and_touchpad_toggle_is_on
        assert bool(self.fc.fd["touchpadhpone"].verify_os_touchpad_setting_page_show_and_touchpad_toggle_is_on()) is True, "OS touchpad setting page is not show"
        time.sleep(1)
        # verify_os_setting_page_touchpad_feedback_toggle_is_on
        assert bool(self.fc.fd["touchpadhpone"].verify_os_setting_page_touchpad_feedback_toggle_is_on()) is True, "OS setting page touchpad feedback toggle is not on"
        # close OS touchpad setting page
        self.fc.fd["touchpadhpone"].close_OS_touchpad_setting_page()
        time.sleep(1)
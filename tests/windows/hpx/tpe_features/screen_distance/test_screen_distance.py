from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Screen_Distance(object):
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
            time.sleep(3)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_screen_distance_UI_C37469417(self):
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_screen_distance()

        assert self.fc.fd["screen_distance"].verify_screen_distance_title_show() == "Screen Distance"
        assert self.fc.fd["screen_distance"].verify_screen_distance_subtitle_show() == "Sitting too close to your monitor can cause eye strain. You will receive a notification if you move too close to your monitor or too close from your preferred distance. This feature requires access to your camera."
        assert self.fc.fd["screen_distance"].verify_alert_option_title_show() == "Alert Options"
        time.sleep(2)
        if self.fc.fd["screen_distance"].verify_screen_distance_button_status() == "Off":
            self.fc.fd["screen_distance"].click_screen_distance_button()
        time.sleep(3)
        assert bool(self.fc.fd["screen_distance"].verify_screen_distance_button_show()) is True
        assert bool(self.fc.fd["screen_distance"].verify_nudge_option_show()) is True
        assert bool(self.fc.fd["screen_distance"].verify_alert_option_show()) is True
        assert bool(self.fc.fd["screen_distance"].verify_blur_option_show()) is True
        assert self.fc.fd["screen_distance"].verify_set_preferred_title_show() == "Set Preferred Distance"
        assert self.fc.fd["screen_distance"].verify_set_preferred_subtitle_show() == "Set a custom threshold for your preferred distance. Your device camera will be used to detect the distance between you and your device."
        assert bool(self.fc.fd["screen_distance"].verify_change_button_show()) is True
        assert bool(self.fc.fd["screen_distance"].verify_restore_button_show()) is True
    

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_screen_distance_tooltips_C37469418(self):
        time.sleep(2)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_screen_distance()

        time.sleep(2)
        self.fc.fd["screen_distance"].click_screen_distance_tootlips()
        assert self.fc.fd["screen_distance"].verify_screen_distance_tootlips() == "This feature only works when your built-in camera is facing you (pictured below). This feature does not support external monitors."
    

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_03_verify_restore_button_C37469419(self):
        time.sleep(2)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_screen_distance()

        time.sleep(2)
        if self.fc.fd["screen_distance"].verify_screen_distance_button_status() == "0":
            time.sleep(2)
            self.fc.fd["screen_distance"].click_screen_distance_button()

        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["screen_distance"].click_restore_button()
        time.sleep(2)
        assert self.fc.fd["screen_distance"].verify_screen_distance_button_status() == "0"
        assert bool(self.fc.fd["screen_distance"].verify_nudge_button_show()) is False
        assert bool(self.fc.fd["screen_distance"].verify_alert_button_show()) is False
        assert bool(self.fc.fd["screen_distance"].verify_blur_button_show()) is False

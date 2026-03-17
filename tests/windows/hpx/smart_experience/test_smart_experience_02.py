from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Smart_Experiences_02(object):
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
            time.sleep(2)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

        

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.required_platform("ultron")
    @pytest.mark.ota
    def test_01_privacy_alert_card_and_auto_screen_dimming_card_main_screen_C32810461(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        privacy_alert_text=self.fc.fd["devices"].get_privacy_alert_card_on_pcdevice()
        auto_screen_dimming_text=self.fc.fd["devices"].get_auto_screen_dimming_card_on_pcdevice()
        assert privacy_alert_text == "Privacy alert" and auto_screen_dimming_text == "Auto screen dimming"
    
    @pytest.mark.required_platform("ultron")
    def test_02_click_privacy_alert_navigation_item_verify_privacy_alert_is_displayed_C33268455(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        self.fc.fd["devices"].click_privacy_alert()
        assert bool(self.fc.fd["smart_experience"].verify_privacy_alert_title()) is True
        assert bool(self.fc.fd["smart_experience"].verify_privacy_alert_subtitle()) is True
        assert bool(self.fc.fd["smart_experience"].verify_privacy_alert_restoreBtn()) is True
        assert bool(self.fc.fd["smart_experience"].verify_snooze_duration_title()) is True

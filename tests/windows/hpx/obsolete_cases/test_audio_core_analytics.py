from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging

pytest.app_info = "HPX"
class Test_Suite_Audio_Core_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.delete_capture_analytics_files()
        time.sleep(3)

    @pytest.mark.require_stack(["stage", "pie"]) 
    def test_01_audio_core_analytics_C33352585(self):
        self.fc.restart_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.driver.swipe(direction="down", distance=2)
        time.sleep(5)
        self.fc.fd["audio"].click_restore_button()
        event = self.fc.capture_analytics_event("AUID_PCAudio_pcAudio_RestoreDefaultsButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Restore Defaults Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_pcAudio_RestoreDefaultsButton", "AUID Field did not generate"
    